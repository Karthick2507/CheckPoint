"""Core Great Expectations validation framework.

``GEValidationFramework`` wires up the GE 1.x Fluent objects and runs a suite
against any :class:`~data_sources.base.DataSource`:

    data source -> asset -> batch definition -> suite -> validation definition
    -> run -> normalized :class:`ValidationOutcome`

The framework is fully source-agnostic: it registers the GE SQL datasource from
the ``DataSource``'s ``connection_string`` + ``engine_kwargs``, so Presto,
Snowflake, or (in tests) sqlite all run through the identical code path.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

import great_expectations as gx

from core.validate.expectations import build_expectations
from core.validate.suite_config import META_ID_KEY, AssetConfig, SuiteConfig
from data_sources.base import DataSource


def _json_safe(value: Any) -> Any:
    """Best-effort conversion of arbitrary values to JSON-serializable form."""
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    try:
        json.dumps(value)
        return value
    except TypeError:
        return str(value)


@dataclass
class ExpectationResultRow:
    """A single expectation's outcome inside a validation run."""

    expectation_type: str
    column: str | None
    success: bool
    kwargs: dict[str, Any] = field(default_factory=dict)
    observed_value: Any = None
    unexpected_count: int | None = None
    unexpected_percent: float | None = None
    exception_message: str | None = None
    severity: str = "warning"
    expectation_id: str | None = None


@dataclass
class ValidationOutcome:
    """Normalized, serializable result of validating one suite."""

    suite_name: str
    asset_name: str
    success: bool
    evaluated: int
    successful: int
    failed: int
    results: list[ExpectationResultRow] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    @property
    def success_percent(self) -> float:
        return 100.0 * self.successful / self.evaluated if self.evaluated else 0.0

    @property
    def failures(self) -> list["ExpectationResultRow"]:
        return [row for row in self.results if not row.success]

    @property
    def critical_failures(self) -> list["ExpectationResultRow"]:
        return [row for row in self.failures if row.severity == "critical"]

    @property
    def has_critical_failure(self) -> bool:
        return bool(self.critical_failures)

    def to_dict(self) -> dict[str, Any]:
        return {
            "suite_name": self.suite_name,
            "asset_name": self.asset_name,
            "success": self.success,
            "evaluated": self.evaluated,
            "successful": self.successful,
            "failed": self.failed,
            "success_percent": round(self.success_percent, 2),
            "results": [
                {
                    "expectation_type": row.expectation_type,
                    "expectation_id": row.expectation_id,
                    "column": row.column,
                    "success": row.success,
                    "severity": row.severity,
                    "kwargs": _json_safe(row.kwargs),
                    "observed_value": _json_safe(row.observed_value),
                    "unexpected_count": row.unexpected_count,
                    "unexpected_percent": row.unexpected_percent,
                    "exception_message": row.exception_message,
                }
                for row in self.results
            ],
            "meta": _json_safe(self.meta),
        }

    @classmethod
    def from_suite_result(cls, suite_result: Any, suite_name: str, asset_name: str) -> "ValidationOutcome":
        """Build a ``ValidationOutcome`` from a GE ``ExpectationSuiteValidationResult``."""
        rows: list[ExpectationResultRow] = []
        for item in getattr(suite_result, "results", []) or []:
            config = getattr(item, "expectation_config", None)
            exp_type = getattr(config, "type", None) or "unknown"
            kwargs = dict(getattr(config, "kwargs", {}) or {})
            meta = dict(getattr(config, "meta", {}) or {})
            result_detail = dict(getattr(item, "result", {}) or {})
            exc_info = getattr(item, "exception_info", {}) or {}
            rows.append(
                ExpectationResultRow(
                    expectation_type=exp_type,
                    column=kwargs.get("column"),
                    success=bool(getattr(item, "success", False)),
                    expectation_id=meta.get(META_ID_KEY),
                    kwargs=kwargs,
                    observed_value=result_detail.get("observed_value"),
                    unexpected_count=result_detail.get("unexpected_count"),
                    unexpected_percent=result_detail.get("unexpected_percent"),
                    exception_message=(exc_info.get("exception_message") if isinstance(exc_info, dict) else None),
                )
            )

        stats = dict(getattr(suite_result, "statistics", {}) or {})
        evaluated = int(stats.get("evaluated_expectations", len(rows)))
        successful = int(stats.get("successful_expectations", sum(1 for r in rows if r.success)))
        return cls(
            suite_name=suite_name,
            asset_name=asset_name,
            success=bool(getattr(suite_result, "success", False)),
            evaluated=evaluated,
            successful=successful,
            failed=evaluated - successful,
            results=rows,
            meta=dict(getattr(suite_result, "meta", {}) or {}),
        )


class GEValidationFramework:
    """Runs config-driven Great Expectations suites against any DataSource."""

    def __init__(self, data_source: DataSource, context: Any | None = None) -> None:
        self.data_source = data_source
        self.context = context if context is not None else gx.get_context(mode="ephemeral")

    # -- object wiring ---------------------------------------------------

    def register_datasource(self) -> Any:
        """Register (or fetch) the GE SQL datasource from this DataSource."""
        try:
            return self.context.data_sources.get(self.data_source.name)
        except (KeyError, ValueError, LookupError):
            pass
        except Exception:
            # Older/newer GE may raise a bespoke "not found" error; fall through.
            pass
        return self.context.data_sources.add_sql(
            name=self.data_source.name,
            connection_string=self.data_source.connection_string(),
            kwargs=self.data_source.engine_kwargs(),
        )

    def _get_or_create_asset(self, source: Any, asset_cfg: AssetConfig) -> Any:
        existing = {a.name: a for a in getattr(source, "assets", [])}
        if asset_cfg.name in existing:
            return existing[asset_cfg.name]
        if asset_cfg.type == "query":
            return source.add_query_asset(name=asset_cfg.name, query=asset_cfg.query)
        kwargs: dict[str, Any] = {"name": asset_cfg.name, "table_name": asset_cfg.table_name}
        if asset_cfg.schema_name:
            kwargs["schema_name"] = asset_cfg.schema_name
        return source.add_table_asset(**kwargs)

    @staticmethod
    def _get_or_create_batch_definition(asset: Any, name: str) -> Any:
        for batch_def in getattr(asset, "batch_definitions", []):
            if batch_def.name == name:
                return batch_def
        return asset.add_batch_definition_whole_table(name=name)

    def build_suite(self, suite_cfg: SuiteConfig) -> Any:
        """Create (replacing any existing) the expectation suite for ``suite_cfg``."""
        try:
            self.context.suites.delete(name=suite_cfg.name)
        except Exception:
            pass  # suite did not exist yet
        suite = self.context.suites.add(gx.ExpectationSuite(name=suite_cfg.name))
        for expectation in build_expectations(suite_cfg.expectations):
            suite.add_expectation(expectation)
        return suite

    # -- execution -------------------------------------------------------

    def run(self, suite_cfg: SuiteConfig) -> ValidationOutcome:
        """Validate ``suite_cfg``'s asset against its expectations and return the outcome."""
        source = self.register_datasource()
        asset = self._get_or_create_asset(source, suite_cfg.asset)
        batch_definition = self._get_or_create_batch_definition(asset, suite_cfg.asset.batch)
        suite = self.build_suite(suite_cfg)

        validation_definition = self.context.validation_definitions.add_or_update(
            gx.ValidationDefinition(
                name=f"{suite_cfg.name}__validation",
                data=batch_definition,
                suite=suite,
            )
        )
        suite_result = validation_definition.run()
        outcome = ValidationOutcome.from_suite_result(
            suite_result,
            suite_name=suite_cfg.name,
            asset_name=suite_cfg.asset.name,
        )
        # Tag each result with the severity declared in the suite config so the
        # warn-and-continue reporting can tier failures without blocking. The
        # id round-tripped through GE meta identifies the exact config entry.
        for row in outcome.results:
            row.severity = suite_cfg.severity_by_id(row.expectation_id)
        return outcome

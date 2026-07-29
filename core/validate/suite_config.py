"""Suite configuration models for the validation layer.

A suite config binds an **asset** (a table or a query on some data source) to a
list of **expectations**. The data source itself is configured separately under
``config/connections/`` and resolved via the ``data_sources`` layer, so a suite
is portable across Presto, Snowflake, or any other registered source.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from data_sources.config import load_yaml


@dataclass
class AssetConfig:
    """The data to validate: a ``table`` asset or a ``query`` asset."""

    name: str
    type: str = "table"  # "table" | "query"
    table_name: str | None = None
    schema_name: str | None = None
    query: str | None = None
    batch: str = "whole_table"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AssetConfig":
        asset_type = str(data.get("type") or "table").lower()
        if asset_type not in ("table", "query"):
            raise ValueError(f"Unsupported asset type: {asset_type!r} (expected 'table' or 'query')")

        name = data.get("name")
        if not name:
            raise ValueError("Asset config requires a 'name'")

        if asset_type == "table" and not data.get("table_name"):
            raise ValueError("Table asset requires 'table_name'")
        if asset_type == "query" and not data.get("query"):
            raise ValueError("Query asset requires 'query'")

        return cls(
            name=str(name),
            type=asset_type,
            table_name=data.get("table_name"),
            schema_name=data.get("schema_name"),
            query=data.get("query"),
            batch=str(data.get("batch") or "whole_table"),
        )


@dataclass
class ExpectationConfig:
    """A single expectation: its snake_case ``type``, kwargs, and severity.

    ``severity`` (``critical`` | ``warning``) drives the warn-and-continue
    reporting: it is recorded on every result but never blocks the run.
    """

    type: str
    kwargs: dict[str, Any] = field(default_factory=dict)
    severity: str = "warning"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ExpectationConfig":
        exp_type = data.get("type")
        if not exp_type:
            raise ValueError("Each expectation requires a 'type'")
        severity = str(data.get("severity") or "warning").lower()
        if severity not in ("critical", "warning"):
            raise ValueError(f"Invalid severity {severity!r} (expected 'critical' or 'warning')")
        kwargs = {key: value for key, value in data.items() if key not in ("type", "severity")}
        return cls(type=str(exp_type), kwargs=kwargs, severity=severity)


@dataclass
class SuiteConfig:
    """A named expectation suite bound to an asset."""

    name: str
    asset: AssetConfig
    expectations: list[ExpectationConfig] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SuiteConfig":
        suite = data.get("suite") or {}
        name = suite.get("name") or data.get("name")
        if not name:
            raise ValueError("Suite config requires a 'suite.name'")

        asset_data = suite.get("asset") or data.get("asset")
        if not asset_data:
            raise ValueError("Suite config requires an 'asset' section")

        expectations = [ExpectationConfig.from_dict(item) for item in (data.get("expectations") or [])]
        if not expectations:
            raise ValueError("Suite config requires at least one entry under 'expectations'")

        return cls(
            name=str(name),
            asset=AssetConfig.from_dict(asset_data),
            expectations=expectations,
        )

    def severity_of(self, expectation_type: str, kwargs: dict[str, Any]) -> str:
        """Return the configured severity for a matching expectation (default warning)."""
        for cfg in self.expectations:
            if cfg.type == expectation_type and cfg.kwargs == kwargs:
                return cfg.severity
        for cfg in self.expectations:  # fall back to a type-only match
            if cfg.type == expectation_type:
                return cfg.severity
        return "warning"


def load_suite_config(path: str | Path) -> SuiteConfig:
    """Load a suite config from a YAML file."""
    return SuiteConfig.from_dict(load_yaml(path))

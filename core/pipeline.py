"""Pipeline orchestrator — the ETL spine.

Chains the stages through three quality gates, warn-and-continue throughout:

    extract -> [gate: raw] -> transform -> [gate: curated] -> load -> [gate: post]

Nothing here raises on a data-quality failure. Every validation outcome and
check result is collected into a :class:`PipelineResult`; severity is recorded
so a caller (or future fail-fast switch) can act on ``has_critical_failure``.
Connections and suites are resolved via injected callables, keeping this layer
free of YAML/IO concerns (the CLI wires those in).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from core.extract import Extractor
from core.load import Loader, LoadResult
from core.pipeline_config import PipelineConfig
from core.transform import Transformer
from core.validate import GEValidationFramework, ValidationOutcome, load_suite_config
from core.validate.suite_config import SuiteConfig
from data_sources.base import DataSource
from quality import CHECK_TYPES, CheckResult, QualityCheck, VolumeDriftCheck
from runtime.run_context import RunContext
from runtime.state import FileState


def build_check(spec: dict[str, Any], default_target: str | None) -> QualityCheck:
    """Construct a QualityCheck from a config spec dict."""
    spec = dict(spec)
    check_type = spec.pop("type", None)
    if check_type not in CHECK_TYPES:
        raise ValueError(
            f"Unknown quality check {check_type!r}. Available: {', '.join(sorted(CHECK_TYPES))}"
        )
    target = spec.pop("target", None) or default_target
    if not target:
        raise ValueError(f"Quality check {check_type!r} requires a 'target'")
    return CHECK_TYPES[check_type](target=target, **spec)


@dataclass
class PipelineResult:
    pipeline: str
    run_id: str
    context: RunContext
    validations: list[ValidationOutcome] = field(default_factory=list)
    checks: list[CheckResult] = field(default_factory=list)
    extract_rows: int = 0
    transform_rows: int | None = None
    load: LoadResult | None = None

    @property
    def passed(self) -> bool:
        return all(v.success for v in self.validations) and all(c.success for c in self.checks)

    @property
    def has_critical_failure(self) -> bool:
        val_crit = any(v.has_critical_failure for v in self.validations)
        chk_crit = any((not c.success and c.severity == "critical") for c in self.checks)
        return val_crit or chk_crit

    @property
    def failure_count(self) -> int:
        return sum(len(v.failures) for v in self.validations) + sum(1 for c in self.checks if not c.success)

    def to_dict(self) -> dict[str, Any]:
        return {
            "pipeline": self.pipeline,
            "run_id": self.run_id,
            "passed": self.passed,
            "has_critical_failure": self.has_critical_failure,
            "failure_count": self.failure_count,
            "extract_rows": self.extract_rows,
            "transform_rows": self.transform_rows,
            "load": None if self.load is None else self.load.__dict__,
            "validations": [v.to_dict() for v in self.validations],
            "checks": [c.to_dict() for c in self.checks],
            "context": self.context.to_dict(),
        }


class Pipeline:
    """Executes a :class:`PipelineConfig` against resolved data sources."""

    def __init__(
        self,
        config: PipelineConfig,
        resolve_source: Callable[[str], DataSource],
        suite_loader: Callable[[str], SuiteConfig] = load_suite_config,
        state: FileState | None = None,
        context: RunContext | None = None,
    ) -> None:
        self.config = config
        self.resolve_source = resolve_source
        self.suite_loader = suite_loader
        self.context = context or RunContext(pipeline=config.name, env=config.env)
        self.state = state if state is not None else FileState(self.context.state_dir)
        self.extractor = Extractor()
        self.transformer = Transformer()
        self.loader = Loader()

    # -- gate helpers ----------------------------------------------------

    def _validate(self, source: DataSource, suite_path: str, gate: str, result: "PipelineResult") -> None:
        suite = self.suite_loader(suite_path)
        outcome = GEValidationFramework(source).run(suite)
        outcome.meta["gate"] = gate
        outcome.meta["source"] = source.name
        result.validations.append(outcome)
        self.context.record(
            f"validate:{gate}",
            suite=outcome.suite_name,
            passed=outcome.success,
            failed=outcome.failed,
            critical=outcome.has_critical_failure,
        )

    def _run_checks(self, source: DataSource, result: "PipelineResult") -> None:
        default_target = self.config.source.table
        for spec in self.config.checks:
            check = build_check(spec, default_target)
            if isinstance(check, VolumeDriftCheck):
                res = check.run(source, state=self.state, run_id=self.context.run_id, batch_id=self.context.batch_id)
            else:
                res = check.run(source, state=self.state)
            result.checks.append(res)
            self.context.record(
                f"check:{res.check}", target=res.target, passed=res.success, severity=res.severity
            )

    # -- execution -------------------------------------------------------

    def run(self) -> PipelineResult:
        self.context.ensure_dirs()
        cfg = self.config
        result = PipelineResult(pipeline=cfg.name, run_id=self.context.run_id, context=self.context)

        source = self.resolve_source(cfg.source.connection)

        # 1. Extract
        extract = self.extractor.extract(
            source,
            table=cfg.source.table,
            query=cfg.source.query,
            batch_key=cfg.source.batch_key,
            batch_id=self.context.batch_id,
            incremental=cfg.extract.incremental,
            limit=cfg.extract.limit,
        )
        result.extract_rows = extract.row_count
        self.context.record("extract", rows=extract.row_count, sql=extract.sql)

        # 2. Gate: raw (suite + custom checks on the source)
        if cfg.suite_raw:
            self._validate(source, cfg.suite_raw, "raw", result)
        self._run_checks(source, result)

        # 3. Transform (ELT on the source)
        payload = extract.rows
        transform = self.transformer.apply(source, cfg.transform)
        if transform.applied:
            payload = transform.rows
            result.transform_rows = transform.row_count
            self.context.record("transform", rows=transform.row_count)

        # 4. Gate: curated
        if cfg.suite_curated:
            self._validate(source, cfg.suite_curated, "curated", result)

        # 5. Load
        if cfg.target and cfg.target.connection and cfg.target.table and cfg.target.mode != "none":
            target = self.resolve_source(cfg.target.connection)
            load_result = self.loader.load(
                target,
                cfg.target.table,
                payload,
                mode=cfg.target.mode,
                keys=cfg.target.keys,
            )
            result.load = load_result
            self.context.record("load", target=cfg.target.table, mode=load_result.mode, inserted=load_result.inserted)

            # 6. Gate: post-load
            if cfg.suite_post:
                self._validate(target, cfg.suite_post, "post", result)

        self.context.record(
            "complete", passed=result.passed, critical=result.has_critical_failure, failures=result.failure_count
        )
        return result

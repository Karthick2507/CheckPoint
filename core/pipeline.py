"""Pipeline orchestrator — the ETL spine.

Chains the stages through three quality gates, warn-and-continue throughout:

    extract -> [gate: raw] -> transform -> [gate: curated] -> load -> [gate: post]

``run()`` never raises. Two kinds of failure are collected rather than thrown:

* **data-quality failures** — expectation/check results, tiered by severity;
* **operational failures** — a bad table, an auth error, a missing suite file,
  a load error. These are recorded as :class:`StageError` entries so the run
  still produces a manifest and a warnings report. A run that blows up silently
  is worse than one that reports what broke.

A stage that fails is skipped, and dependent stages are skipped with it (no
load without a payload), but every independent stage still runs so one broken
gate cannot hide the rest of the picture.

Connections and suites are resolved via injected callables, keeping this layer
free of YAML/IO concerns (the CLI wires those in).
"""

from __future__ import annotations

import traceback
from dataclasses import dataclass, field
from typing import Any, Callable

from core.extract import Extractor
from core.load import Loader, LoadResult, PushdownLoader, PushdownResult
from core.pipeline_config import PipelineConfig
from core.transform import Transformer
from core.validate import GEValidationFramework, ValidationOutcome, load_suite_config
from core.validate.scoping import scope_suite_to_batch
from core.validate.suite_config import SuiteConfig
from data_sources.base import DataSource
from quality import CHECK_TYPES, CheckResult, QualityCheck, VolumeDriftCheck
from runtime.run_context import RunContext
from runtime.state import FileState
from runtime.templating import render_all, render_sql


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
class StageError:
    """An operational failure in one stage — recorded, not raised."""

    stage: str
    error_type: str
    message: str
    detail: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage,
            "error_type": self.error_type,
            "message": self.message,
            "detail": self.detail,
        }


@dataclass
class PipelineResult:
    pipeline: str
    run_id: str
    context: RunContext
    validations: list[ValidationOutcome] = field(default_factory=list)
    checks: list[CheckResult] = field(default_factory=list)
    errors: list[StageError] = field(default_factory=list)
    extract_rows: int = 0
    transform_rows: int | None = None
    load: LoadResult | PushdownResult | None = None
    execution: str = "rows"

    @property
    def passed(self) -> bool:
        return (
            not self.errors
            and all(v.success for v in self.validations)
            and all(c.success for c in self.checks)
        )

    @property
    def has_critical_failure(self) -> bool:
        val_crit = any(v.has_critical_failure for v in self.validations)
        chk_crit = any((not c.success and c.severity == "critical") for c in self.checks)
        # An operational failure is always critical: the run did not do its job.
        return val_crit or chk_crit or bool(self.errors)

    @property
    def failure_count(self) -> int:
        return (
            sum(len(v.failures) for v in self.validations)
            + sum(1 for c in self.checks if not c.success)
            + len(self.errors)
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "pipeline": self.pipeline,
            "run_id": self.run_id,
            "passed": self.passed,
            "has_critical_failure": self.has_critical_failure,
            "failure_count": self.failure_count,
            "execution": self.execution,
            "extract_rows": self.extract_rows,
            "transform_rows": self.transform_rows,
            "load": None if self.load is None else dict(self.load.__dict__),
            "validations": [v.to_dict() for v in self.validations],
            "checks": [c.to_dict() for c in self.checks],
            "errors": [e.to_dict() for e in self.errors],
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
        self.pushdown_loader = PushdownLoader()

    # -- execution strategy ------------------------------------------------

    def execution_mode(self) -> str:
        """Resolve the configured execution mode to ``rows`` or ``pushdown``.

        ``auto`` chooses pushdown when the target lives on the *same* connection
        as the source — the warehouse can then run ``INSERT … SELECT`` and no
        rows travel through Python. Cross-system moves fall back to rows.
        """
        cfg = self.config
        configured = (cfg.execution or "auto").lower()
        if configured == "pushdown":
            return "pushdown"
        if configured == "rows":
            return "rows"
        same_warehouse = bool(
            cfg.target
            and cfg.target.connection
            and cfg.target.connection == cfg.source.connection
            and cfg.target.mode != "none"
        )
        return "pushdown" if same_warehouse else "rows"

    def can_stream(self) -> tuple[bool, str]:
        """Whether the row-based path can stream, and why not if it can't.

        Streaming holds no full result set, so it cannot feed a transform (which
        needs a materialized set) and cannot serve a destructive load (which
        would delete before knowing whether the stream yields anything — the
        empty-payload hazard from P0-1).
        """
        cfg = self.config
        if not cfg.extract.stream:
            return False, "not enabled"
        if cfg.transform:
            return False, "a transform needs a materialized result set"
        target = cfg.target
        if not (target and target.connection and target.table and target.mode != "none"):
            return False, "streaming needs a load target"
        if target.mode != "append":
            return False, f"streaming supports only append loads (target mode is {target.mode!r})"
        return True, ""

    def _source_sql(self, cfg: PipelineConfig, template_context: dict[str, Any]) -> str:
        """The SELECT that defines the source data set."""
        if cfg.source.query:
            return render_sql(cfg.source.query, template_context)
        return self.extractor.build_table_sql(
            cfg.source.table or "",
            batch_key=cfg.source.batch_key,
            batch_id=self.context.batch_id,
            incremental=cfg.extract.incremental,
            limit=cfg.extract.limit,
        )

    # -- failure capture --------------------------------------------------

    def _fail(self, result: "PipelineResult", stage: str, exc: BaseException) -> None:
        """Record an operational failure instead of letting it escape."""
        error = StageError(
            stage=stage,
            error_type=type(exc).__name__,
            message=str(exc) or repr(exc),
            detail="".join(traceback.format_exception_only(type(exc), exc)).strip(),
        )
        result.errors.append(error)
        self.context.record(f"error:{stage}", error_type=error.error_type, message=error.message)

    # -- gate helpers ----------------------------------------------------

    def _validate(
        self,
        source: DataSource,
        suite_path: str,
        gate: str,
        result: "PipelineResult",
        template_context: dict[str, Any] | None = None,
    ) -> None:
        try:
            suite = self.suite_loader(suite_path)
            # A query asset may be templated on the run's batch, same as
            # transform SQL, so a gate can validate just this batch.
            if template_context and suite.asset.query:
                suite.asset.query = render_sql(suite.asset.query, template_context)
            # Narrow the asset to the current batch when the suite asks for it,
            # so the gate validates this run's slice rather than all history.
            scoped = scope_suite_to_batch(suite, self.context.batch_id, template_context)
            outcome = GEValidationFramework(source).run(scoped)
            if scoped is not suite:
                outcome.meta["batch_scoped"] = True
                outcome.meta["batch_id"] = self.context.batch_id
        except Exception as exc:
            self._fail(result, f"validate:{gate}", exc)
            return
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
            # Each check is independent: one bad spec must not sink the rest.
            try:
                check = build_check(spec, default_target)
                if isinstance(check, VolumeDriftCheck):
                    res = check.run(
                        source, state=self.state, run_id=self.context.run_id, batch_id=self.context.batch_id
                    )
                else:
                    res = check.run(source, state=self.state)
            except Exception as exc:
                self._fail(result, f"check:{spec.get('type', '?')}", exc)
                continue
            result.checks.append(res)
            self.context.record(
                f"check:{res.check}", target=res.target, passed=res.success, severity=res.severity
            )

    # -- execution -------------------------------------------------------

    def run(self) -> PipelineResult:
        """Execute the pipeline. Never raises — failures are recorded."""
        cfg = self.config
        result = PipelineResult(pipeline=cfg.name, run_id=self.context.run_id, context=self.context)

        try:
            self.context.ensure_dirs()
        except Exception as exc:  # pragma: no cover - filesystem failure
            self._fail(result, "setup", exc)

        # Resolve the source. Without it nothing downstream can run.
        try:
            source = self.resolve_source(cfg.source.connection)
        except Exception as exc:
            self._fail(result, "resolve_source", exc)
            self._record_complete(result)
            return result

        # SQL in the config may reference {{ batch_id }}, {{ run_id }}, vars, ...
        template_context = self.context.template_context(cfg.vars)
        execution = self.execution_mode()
        result.execution = execution
        self.context.record("execution", mode=execution)

        source_sql = self._source_sql(cfg, template_context)

        # 1. Extract. Pushdown never materializes rows — the data stays in the
        # warehouse and the SELECT is embedded into the load statement.
        payload: list[dict[str, Any]] = []
        extract_ok = True
        streaming = False
        if execution == "rows":
            streaming, why_not = self.can_stream()
            if streaming:
                # Extract and load are fused: chunks go straight to the target
                # so memory stays bounded by chunk_size, not by table size.
                result.execution = "stream"
                self.context.record("extract:stream", sql=source_sql, chunk_size=cfg.extract.chunk_size)
            else:
                if cfg.extract.stream:
                    self.context.record("extract:stream_unavailable", reason=why_not)
                extract_ok = False
                try:
                    extract = self.extractor.extract(source, query=source_sql)
                    result.extract_rows = extract.row_count
                    payload = extract.rows
                    extract_ok = True
                    self.context.record("extract", rows=extract.row_count, sql=extract.sql)
                except Exception as exc:
                    self._fail(result, "extract", exc)
        else:
            self.context.record("extract:pushdown", sql=source_sql, materialized=False)

        # 2. Gate: raw (suite + custom checks on the source). These are
        # independent of extract, so they still run if extract failed.
        if cfg.suite_raw:
            self._validate(source, cfg.suite_raw, "raw", result, template_context)
        self._run_checks(source, result)

        # 3. Transform (ELT on the source)
        transform_ok = True
        select_sql = source_sql
        try:
            steps = render_all(cfg.transform, template_context)
            if execution == "pushdown":
                # Run setup steps; keep the curated SELECT for INSERT … SELECT.
                prepared = self.transformer.prepare(source, steps)
                if prepared:
                    select_sql = prepared
                    self.context.record("transform:pushdown", sql=prepared, materialized=False)
            else:
                transform = self.transformer.apply(source, steps)
                if transform.applied:
                    payload = transform.rows
                    select_sql = transform.sql
                    result.transform_rows = transform.row_count
                    self.context.record("transform", rows=transform.row_count)
        except Exception as exc:
            transform_ok = False
            self._fail(result, "transform", exc)

        # 4. Gate: curated
        if cfg.suite_curated:
            self._validate(source, cfg.suite_curated, "curated", result, template_context)

        # 5. Load — only with a trustworthy payload. Loading after a failed
        # extract or transform would write a partial or stale result set.
        wants_load = bool(
            cfg.target and cfg.target.connection and cfg.target.table and cfg.target.mode != "none"
        )
        if wants_load and not (extract_ok and transform_ok):
            self.context.record("load:skipped", reason="upstream stage failed")
        elif wants_load:
            target = None
            try:
                target = self.resolve_source(cfg.target.connection)
                if streaming:
                    _, chunks = self.extractor.stream(
                        source, query=source_sql, chunk_size=cfg.extract.chunk_size
                    )
                    load_result = self.loader.load_stream(
                        target, cfg.target.table, chunks, mode=cfg.target.mode
                    )
                    result.extract_rows = load_result.inserted
                elif execution == "pushdown":
                    load_result = self.pushdown_loader.load(
                        source,  # same warehouse hosts both sides
                        cfg.target.table,
                        select_sql,
                        mode=cfg.target.mode,
                        keys=cfg.target.keys,
                        allow_empty=cfg.target.allow_empty,
                    )
                    if load_result.inserted is not None:
                        result.transform_rows = load_result.inserted
                else:
                    load_result = self.loader.load(
                        target,
                        cfg.target.table,
                        payload,
                        mode=cfg.target.mode,
                        keys=cfg.target.keys,
                        allow_empty=cfg.target.allow_empty,
                    )
                result.load = load_result
                self.context.record(
                    "load",
                    target=cfg.target.table,
                    mode=load_result.mode,
                    inserted=load_result.inserted,
                    skipped=load_result.skipped,
                    reason=load_result.reason,
                )
            except Exception as exc:
                self._fail(result, "load", exc)

            # 6. Gate: post-load — only meaningful if the load itself ran.
            if cfg.suite_post and target is not None and result.load is not None:
                self._validate(target, cfg.suite_post, "post", result, template_context)

        self._record_complete(result)
        return result

    def _record_complete(self, result: "PipelineResult") -> None:
        self.context.record(
            "complete",
            passed=result.passed,
            critical=result.has_critical_failure,
            failures=result.failure_count,
            errors=len(result.errors),
        )

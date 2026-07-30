"""Render a :class:`~core.pipeline.PipelineResult` to files and the console.

Files only (per the design): each run writes

    etl_output/runs/<run_id>/
    ├── run_manifest.json      # full machine-readable record + lineage
    ├── warnings_report.md     # the detailed warn-and-continue capture
    └── validation/<suite>_validation.json|md

The warnings report is the heart of the warn-and-continue model: nothing blocks
the pipeline, but every failure — GE expectation or custom check — is captured
here with its severity so it can be triaged later.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.validate.reporting import write_reports

if TYPE_CHECKING:  # avoid a runtime import cycle
    from core.pipeline import PipelineResult


@dataclass
class WarnRow:
    gate: str
    severity: str
    dimension: str
    target: str
    subject: str
    observed: Any
    detail: str


def collect_warnings(result: "PipelineResult") -> list[WarnRow]:
    """Flatten every failure: operational errors, validation gates, and checks."""
    rows: list[WarnRow] = []

    # Operational failures first — a stage that did not run outranks any
    # expectation result, because the run did not do its job.
    for error in getattr(result, "errors", []):
        rows.append(
            WarnRow(
                gate=error.stage,
                severity="critical",
                dimension="operational",
                target=result.pipeline,
                subject=error.error_type,
                observed=None,
                detail=error.message,
            )
        )

    for outcome in result.validations:
        gate = str(outcome.meta.get("gate", "?"))
        for row in outcome.failures:
            detail = ""
            if row.unexpected_count is not None:
                detail = f"unexpected={row.unexpected_count}"
            if row.exception_message:
                detail = f"error: {row.exception_message}"
            rows.append(
                WarnRow(
                    gate=gate,
                    severity=row.severity,
                    dimension="expectation",
                    target=f"{outcome.asset_name}" + (f".{row.column}" if row.column else ""),
                    subject=row.expectation_type,
                    observed=row.observed_value,
                    detail=detail,
                )
            )

    for check in result.checks:
        if check.success:
            continue
        rows.append(
            WarnRow(
                gate="check",
                severity=check.severity,
                dimension=check.dimension,
                target=check.target,
                subject=check.check,
                observed=check.observed,
                detail=check.details,
            )
        )

    # A refused destructive load is an operational event the operator must see.
    load = result.load
    if load is not None and load.skipped and load.reason and load.mode in ("overwrite", "merge"):
        rows.append(
            WarnRow(
                gate="load",
                severity="critical",
                dimension="load",
                target=load.target,
                subject=f"{load.mode}_skipped",
                observed=0,
                detail=load.reason,
            )
        )

    # A destructive load that could not be made atomic is a durability risk.
    if load is not None and not load.skipped and not load.atomic and load.mode in ("overwrite", "merge"):
        rows.append(
            WarnRow(
                gate="load",
                severity="warning",
                dimension="load",
                target=load.target,
                subject="non_atomic_load",
                observed=load.inserted,
                detail=load.reason or f"'{load.mode}' load was not atomic on this target",
            )
        )

    # critical first, then by gate
    rows.sort(key=lambda r: (r.severity != "critical", r.gate))
    return rows


# --------------------------------------------------------------------------
# File writers
# --------------------------------------------------------------------------


def write_run_manifest(result: "PipelineResult") -> Path:
    ctx = result.context
    ctx.ensure_dirs()
    path = ctx.run_dir / "run_manifest.json"
    payload = result.to_dict()
    if result.passed:
        payload["status"] = "passed"
    elif getattr(result, "errors", []):
        payload["status"] = "error"
    elif result.has_critical_failure:
        payload["status"] = "critical"
    else:
        payload["status"] = "warning"
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    return path


def write_warnings_report(result: "PipelineResult") -> Path:
    ctx = result.context
    ctx.ensure_dirs()
    path = ctx.run_dir / "warnings_report.md"
    path.write_text(_warnings_markdown(result), encoding="utf-8")
    return path


def write_validation_reports(result: "PipelineResult") -> list[Path]:
    ctx = result.context
    out = ctx.subdir("validation")
    written: list[Path] = []
    for outcome in result.validations:
        written.extend(write_reports(outcome, output_dir=out))
    return written


def write_pipeline_reports(result: "PipelineResult") -> dict[str, Any]:
    """Write manifest + warnings + per-suite validation reports for a run."""
    manifest = write_run_manifest(result)
    warnings = write_warnings_report(result)
    validations = write_validation_reports(result)
    return {"manifest": manifest, "warnings": warnings, "validations": validations}


def _warnings_markdown(result: "PipelineResult") -> str:
    ctx = result.context
    warnings = collect_warnings(result)
    critical = [w for w in warnings if w.severity == "critical"]
    if result.passed:
        status = "✅ PASSED"
    elif getattr(result, "errors", []):
        status = "⛔ ERROR"
    elif result.has_critical_failure:
        status = "🔴 CRITICAL"
    else:
        status = "🟡 WARNINGS"

    lines: list[str] = [
        f"# Warnings Report — `{result.pipeline}`",
        "",
        f"- **Run:** `{result.run_id}`",
        f"- **Env:** {ctx.env}  ·  **Batch:** `{ctx.batch_id}`  ·  **Started:** {ctx.started_at}",
        f"- **Status:** {status}",
        f"- **Extracted rows:** {result.extract_rows}"
        + (f"  ·  **Transformed rows:** {result.transform_rows}" if result.transform_rows is not None else "")
        + (f"  ·  **Loaded rows:** {result.load.inserted}" if result.load else ""),
        f"- **Failures:** {len(warnings)} total  ·  {len(critical)} critical",
        "",
    ]

    if not warnings:
        lines += ["No failures — all validation gates and checks passed. 🎉", ""]
        return "\n".join(lines) + "\n"

    errors = getattr(result, "errors", [])
    if errors:
        lines += [
            "## ⛔ Operational errors (the run did not complete normally)",
            "",
            "| Stage | Error | Message |",
            "|:------|:------|:--------|",
        ]
        for error in errors:
            lines.append(f"| `{error.stage}` | `{error.error_type}` | {error.message} |")
        lines.append("")

    lines += [
        "## All failures",
        "",
        "| Gate | Severity | Dimension | Target | Check / Expectation | Observed | Detail |",
        "|:-----|:---------|:----------|:-------|:--------------------|:---------|:-------|",
    ]
    for w in warnings:
        sev = "🔴 critical" if w.severity == "critical" else "🟡 warning"
        observed = "" if w.observed is None else f"`{w.observed}`"
        lines.append(
            f"| {w.gate} | {sev} | {w.dimension} | `{w.target}` | `{w.subject}` | {observed} | {w.detail} |"
        )
    lines.append("")

    if critical:
        lines += ["## Critical failures (triage first)", ""]
        for w in critical:
            lines.append(f"### `{w.subject}` — {w.target}")
            lines.append(f"- gate: **{w.gate}**  ·  dimension: {w.dimension}")
            if w.observed is not None:
                lines.append(f"- observed: `{w.observed}`")
            if w.detail:
                lines.append(f"- {w.detail}")
            lines.append("")

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Console
# --------------------------------------------------------------------------


def render_pipeline_console(result: "PipelineResult", console: Console | None = None) -> None:
    console = console or Console()
    if result.passed:
        color, status = "green", "PASSED"
    elif getattr(result, "errors", []):
        color, status = "red", "ERROR — run did not complete"
    elif result.has_critical_failure:
        color, status = "red", "CRITICAL FAILURE"
    else:
        color, status = "yellow", "WARNINGS"

    load_line = f"  ·  loaded {result.load.inserted}" if result.load else ""
    console.print(
        Panel(
            f"[bold]{result.pipeline}[/bold]  ·  run [cyan]{result.run_id}[/cyan]\n"
            f"[{color}]{status}[/{color}]  — {result.failure_count} failure(s)\n"
            f"extracted {result.extract_rows}"
            + (f"  ·  transformed {result.transform_rows}" if result.transform_rows is not None else "")
            + load_line,
            title="ETL Pipeline Summary",
            border_style=color,
        )
    )

    table = Table(show_lines=False, header_style="bold")
    table.add_column("Gate")
    table.add_column("Result", justify="center")
    table.add_column("Suite / Check")
    table.add_column("Detail")

    for error in getattr(result, "errors", []):
        table.add_row(error.stage, "[red]⛔[/red]", error.error_type, error.message)

    for outcome in result.validations:
        mark = "[green]✓[/green]" if outcome.success else "[red]✗[/red]"
        table.add_row(
            str(outcome.meta.get("gate", "?")),
            mark,
            outcome.suite_name,
            f"{outcome.successful}/{outcome.evaluated} passed",
        )
    for check in result.checks:
        mark = "[green]✓[/green]" if check.success else ("[red]✗[/red]" if check.severity == "critical" else "[yellow]![/yellow]")
        table.add_row("check", mark, check.check, check.details)

    if result.validations or result.checks or getattr(result, "errors", []):
        console.print(table)

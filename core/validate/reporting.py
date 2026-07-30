"""Render :class:`ValidationOutcome` objects to the console and to files.

* :func:`render_console` prints a color-coded summary (green pass / red fail)
  using ``rich``.
* :func:`write_json_report` / :func:`write_markdown_report` persist the run so
  results can be diffed, attached to tickets, or checked into CI artifacts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.validate.framework import ValidationOutcome

DEFAULT_OUTPUT_DIR = Path("etl_output")


def render_console(outcome: ValidationOutcome, console: Console | None = None) -> None:
    """Print a color-coded validation summary."""
    console = console or Console()

    status_color = "green" if outcome.success else "red"
    status_text = "PASSED" if outcome.success else "FAILED"
    console.print(
        Panel(
            f"[bold]{outcome.suite_name}[/bold]  ·  asset [cyan]{outcome.asset_name}[/cyan]\n"
            f"[{status_color}]{status_text}[/{status_color}]  "
            f"— {outcome.successful}/{outcome.evaluated} expectations passed "
            f"({outcome.success_percent:.1f}%)",
            title="GE Validation Summary",
            border_style=status_color,
        )
    )

    table = Table(show_lines=False, header_style="bold")
    table.add_column("Result", justify="center")
    table.add_column("Expectation")
    table.add_column("Column")
    table.add_column("Observed / Detail")

    for row in outcome.results:
        mark = "[green]✓[/green]" if row.success else "[red]✗[/red]"
        detail = ""
        if row.observed_value is not None:
            detail = f"observed={row.observed_value}"
        elif row.unexpected_count is not None:
            detail = f"unexpected={row.unexpected_count}"
        if row.exception_message:
            detail = f"[red]error: {row.exception_message}[/red]"
        table.add_row(mark, row.expectation_type, row.column or "—", detail)

    console.print(table)


def write_json_report(outcome: ValidationOutcome, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> Path:
    """Write ``<suite>_validation.json`` and return its path."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{outcome.suite_name}_validation.json"
    path.write_text(json.dumps(outcome.to_dict(), indent=2, default=str), encoding="utf-8")
    return path


def write_markdown_report(outcome: ValidationOutcome, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> Path:
    """Write ``<suite>_validation.md`` and return its path."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{outcome.suite_name}_validation.md"
    path.write_text(_markdown(outcome), encoding="utf-8")
    return path


def _markdown(outcome: ValidationOutcome) -> str:
    status = "✅ PASSED" if outcome.success else "❌ FAILED"
    lines: list[str] = [
        f"# GE Validation Report — `{outcome.suite_name}`",
        "",
        f"- **Asset:** `{outcome.asset_name}`",
        f"- **Status:** {status}",
        f"- **Passed:** {outcome.successful}/{outcome.evaluated} "
        f"({outcome.success_percent:.1f}%)",
        f"- **Failed:** {outcome.failed}",
        "",
        "## Expectations",
        "",
        "| Result | Expectation | Column | Observed / Detail |",
        "|:------:|:------------|:-------|:------------------|",
    ]
    for row in outcome.results:
        mark = "✅" if row.success else "❌"
        detail = ""
        if row.observed_value is not None:
            detail = f"observed = `{row.observed_value}`"
        elif row.unexpected_count is not None:
            detail = f"unexpected = {row.unexpected_count}"
        if row.exception_message:
            detail = f"error: {row.exception_message}"
        lines.append(f"| {mark} | `{row.expectation_type}` | {row.column or '—'} | {detail} |")

    failures = [row for row in outcome.results if not row.success]
    if failures:
        lines += ["", "## Failed Expectations", ""]
        for row in failures:
            lines.append(f"### `{row.expectation_type}`" + (f" — column `{row.column}`" if row.column else ""))
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(row.kwargs, indent=2, default=str))
            lines.append("```")
            lines.append("")

    return "\n".join(lines) + "\n"


def write_reports(
    outcome: ValidationOutcome,
    output_dir: str | Path = DEFAULT_OUTPUT_DIR,
    formats: Iterable[str] = ("json", "markdown"),
) -> list[Path]:
    """Write the requested report formats and return their paths."""
    written: list[Path] = []
    formats = set(formats)
    if "json" in formats:
        written.append(write_json_report(outcome, output_dir))
    if "markdown" in formats or "md" in formats:
        written.append(write_markdown_report(outcome, output_dir))
    return written

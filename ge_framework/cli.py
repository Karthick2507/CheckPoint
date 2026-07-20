"""Typer CLI for the GE validation framework.

Examples
--------
Run a suite against a Presto datasource::

    python -m ge_framework.cli validate \
        --datasource config/datasource.example.yml \
        --suite config/suites/request.example.yml \
        --auth-token <token>

List the expectation types available in this GE install::

    python -m ge_framework.cli list-expectations
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console

from ge_framework.config import load_datasource_config, load_suite_config
from ge_framework.framework import GEValidationFramework
from ge_framework.reporting import DEFAULT_OUTPUT_DIR, render_console, write_reports

app = typer.Typer(add_completion=False, help="Great Expectations validations against Presto/Trino.")
console = Console()


@app.command()
def validate(
    datasource: Annotated[Path, typer.Option(help="Path to the datasource YAML config.")],
    suite: Annotated[list[Path], typer.Option(help="Path to a suite YAML config (repeatable).")],
    host: Annotated[Optional[str], typer.Option(help="Override datasource host.")] = None,
    user: Annotated[Optional[str], typer.Option(help="Override datasource user.")] = None,
    auth_token: Annotated[Optional[str], typer.Option(help="Override auth token (Bearer).")] = None,
    output_dir: Annotated[Path, typer.Option(help="Directory for JSON/markdown reports.")] = DEFAULT_OUTPUT_DIR,
    no_reports: Annotated[bool, typer.Option("--no-reports", help="Skip writing report files.")] = False,
) -> None:
    """Validate one or more suites against the datasource and report results."""
    ds_config = load_datasource_config(datasource)
    if host:
        ds_config.host = host
    if user:
        ds_config.user = user
    if auth_token:
        ds_config.auth_token = auth_token

    framework = GEValidationFramework(ds_config)

    all_passed = True
    for suite_path in suite:
        suite_config = load_suite_config(suite_path)
        console.print(f"[bold]Running suite[/bold] [cyan]{suite_config.name}[/cyan] …")
        outcome = framework.run(suite_config)
        render_console(outcome, console=console)

        if not no_reports:
            for path in write_reports(outcome, output_dir=output_dir):
                console.print(f"[green]Report written:[/green] {path}")

        all_passed = all_passed and outcome.success

    if not all_passed:
        console.print("[red]One or more suites failed.[/red]")
        raise typer.Exit(code=1)
    console.print("[green]All suites passed.[/green]")


@app.command("list-expectations")
def list_expectations(
    filter_text: Annotated[Optional[str], typer.Argument(help="Only show types containing this text.")] = None,
) -> None:
    """List the expectation types available in the installed GE version."""
    import great_expectations.expectations as gxe

    names = sorted(
        name
        for name in dir(gxe)
        if name.startswith("Expect") and isinstance(getattr(gxe, name), type)
    )
    for name in names:
        snake = _camel_to_snake(name)
        if filter_text and filter_text.lower() not in snake.lower():
            continue
        console.print(snake)


def _camel_to_snake(name: str) -> str:
    out = [name[0].lower()]
    for char in name[1:]:
        out.append("_" + char.lower() if char.isupper() else char)
    return "".join(out)


def main() -> None:
    app()


if __name__ == "__main__":
    sys.exit(app())  # pragma: no cover

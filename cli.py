"""Command-line entrypoint for the ETL framework (cron-first).

Commands
--------
    run-pipeline   run a declarative pipeline end-to-end (extract/validate/
                   transform/load) and write per-run reports
    validate       run one or more expectation suites against a connection
    list-expectations   list GE expectation types available in this install
    list-sources        list registered data-source connector types

Connections are resolved by name from ``--connections-dir`` (default
``config/connections``): each file's ``connection.name`` is its key, so a
pipeline's ``source.connection: mrm_presto`` maps to ``mrm_presto.yml``.

Warn-and-continue: a run always completes and writes its reports. ``--fail-on``
only controls the *exit code* (for CI/cron), never whether the pipeline runs.

Examples
--------
    export PRESTO_AUTH_TOKEN=...
    python -m cli run-pipeline --pipeline config/pipelines/request_daily.example.yml
    python -m cli validate --connection config/connections/mrm_presto.example.yml \
        --suite config/suites/request_quality.example.yml
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console

from core.pipeline import Pipeline
from core.pipeline_config import load_pipeline_config
from core.validate import GEValidationFramework, load_suite_config
from core.validate.reporting import render_console as render_validation
from core.validate.reporting import write_reports as write_validation_reports
from data_sources import available_sources, create_data_source, load_connection_config
from data_sources.config import load_yaml
from reporting import render_pipeline_console, write_pipeline_reports
from runtime.run_context import RunContext

app = typer.Typer(add_completion=False, help="Great Expectations ETL framework over pluggable data sources.")
console = Console()

DEFAULT_CONNECTIONS_DIR = Path("config/connections")


def _load_connections(connections_dir: Path) -> dict[str, dict]:
    """Map connection name -> config for every YAML in ``connections_dir``."""
    connections: dict[str, dict] = {}
    if not connections_dir.exists():
        return connections
    for path in sorted(connections_dir.glob("*.y*ml")):
        data = load_yaml(path)
        conn = data.get("connection") or data
        name = conn.get("name")
        if name:
            connections[name] = conn
    return connections


def _exit_code(has_critical: bool, passed: bool, fail_on: str) -> int:
    fail_on = fail_on.lower()
    if fail_on == "never":
        return 0
    if fail_on == "any":
        return 0 if passed else 1
    return 1 if has_critical else 0  # default: "critical"


@app.command("run-pipeline")
def run_pipeline(
    pipeline: Annotated[Path, typer.Option(help="Path to the pipeline YAML config.")],
    connections_dir: Annotated[Path, typer.Option(help="Directory of connection configs.")] = DEFAULT_CONNECTIONS_DIR,
    output_dir: Annotated[Path, typer.Option(help="Root for run output (etl_output).")] = Path("etl_output"),
    env: Annotated[Optional[str], typer.Option(help="Override the pipeline env.")] = None,
    fail_on: Annotated[str, typer.Option(help="Exit non-zero on: critical | any | never.")] = "critical",
) -> None:
    """Run a declarative pipeline end-to-end and write per-run reports."""
    cfg = load_pipeline_config(pipeline)
    if env:
        cfg.env = env

    connections = _load_connections(connections_dir)

    def resolve(name: str):
        if name not in connections:
            raise typer.BadParameter(
                f"Connection {name!r} not found in {connections_dir}. "
                f"Known: {', '.join(sorted(connections)) or '(none)'}"
            )
        return create_data_source(connections[name])

    context = RunContext(pipeline=cfg.name, env=cfg.env, output_root=output_dir)
    console.print(f"[bold]Running pipeline[/bold] [cyan]{cfg.name}[/cyan]  (run {context.run_id})")

    result = Pipeline(cfg, resolve_source=resolve, context=context).run()

    render_pipeline_console(result, console=console)
    paths = write_pipeline_reports(result)
    console.print(f"[green]Manifest:[/green] {paths['manifest']}")
    console.print(f"[green]Warnings report:[/green] {paths['warnings']}")

    raise typer.Exit(code=_exit_code(result.has_critical_failure, result.passed, fail_on))


@app.command()
def validate(
    connection: Annotated[Path, typer.Option(help="Path to a connection YAML config.")],
    suite: Annotated[list[Path], typer.Option(help="Path to a suite YAML config (repeatable).")],
    output_dir: Annotated[Path, typer.Option(help="Directory for JSON/markdown reports.")] = Path("etl_output"),
    fail_on: Annotated[str, typer.Option(help="Exit non-zero on: critical | any | never.")] = "critical",
    no_reports: Annotated[bool, typer.Option("--no-reports", help="Skip writing report files.")] = False,
) -> None:
    """Validate one or more suites against a data source."""
    source = create_data_source(load_connection_config(connection))
    framework = GEValidationFramework(source)

    any_critical = False
    all_passed = True
    for suite_path in suite:
        suite_cfg = load_suite_config(suite_path)
        console.print(f"[bold]Validating[/bold] [cyan]{suite_cfg.name}[/cyan] …")
        outcome = framework.run(suite_cfg)
        render_validation(outcome, console=console)
        if not no_reports:
            for path in write_validation_reports(outcome, output_dir=output_dir):
                console.print(f"[green]Report:[/green] {path}")
        any_critical = any_critical or outcome.has_critical_failure
        all_passed = all_passed and outcome.success

    raise typer.Exit(code=_exit_code(any_critical, all_passed, fail_on))


@app.command("list-expectations")
def list_expectations(
    filter_text: Annotated[Optional[str], typer.Argument(help="Only show types containing this text.")] = None,
) -> None:
    """List the expectation types available in the installed GE version."""
    import great_expectations.expectations as gxe

    for name in sorted(n for n in dir(gxe) if n.startswith("Expect") and isinstance(getattr(gxe, n), type)):
        snake = _camel_to_snake(name)
        if filter_text and filter_text.lower() not in snake.lower():
            continue
        console.print(snake)


@app.command("list-sources")
def list_sources() -> None:
    """List registered data-source connector types."""
    for name in available_sources():
        console.print(name)


def _camel_to_snake(name: str) -> str:
    out = [name[0].lower()]
    for char in name[1:]:
        out.append("_" + char.lower() if char.isupper() else char)
    return "".join(out)


def main() -> None:  # pragma: no cover
    app()


if __name__ == "__main__":  # pragma: no cover
    app()

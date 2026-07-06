"""Generic CLI entrypoint: validate any table that has a config/<table>.yaml.

    python run_validation.py --table slot  --host ... --user ... --auth-token ...
    python run_validation.py --table request ...

Mirrors BCV_analyzer/bcv_analyzer.py's connection conventions (same args,
same Presto/Trino gateway + VPN requirements).
"""
from __future__ import annotations
import os
from pathlib import Path
from typing import Annotated
import typer
from ge_validator.runner import config_path_for_table, run_validation

def main(
    table: Annotated[str, typer.Option("--table", help="Table name; loads config/<table>.yaml")] = "request",
    host: Annotated[str | None, typer.Option(help="Presto/Trino host")] = os.getenv("PRESTO_HOST"),
    port: Annotated[int, typer.Option(help="Presto/Trino port")] = int(os.getenv("PRESTO_PORT", "8080")),
    user: Annotated[str | None, typer.Option(help="Presto/Trino user")] = os.getenv("PRESTO_USER"),
    request_timeout: Annotated[float, typer.Option(help="Request timeout in seconds")] = float(
        os.getenv("PRESTO_REQUEST_TIMEOUT", "5")
    ),
    auth_token: Annotated[str | None, typer.Option("--auth-token", help="Presto gateway token")] = os.getenv(
        "PRESTO_AUTH_TOKEN"
    ),
    auth_header: Annotated[str | None, typer.Option("--auth-header", help="Auth header name")] = os.getenv(
        "PRESTO_AUTH_HEADER"
    ),
    transaction_limit: Annotated[int, typer.Option(help="Rows to sample for reconciliation")] = 10,
    config: Annotated[
        Path | None, typer.Option("--config", help="Explicit config path (overrides --table)")
    ] = None,
) -> None:
    if not host or not user:
        raise SystemExit("Missing required connection args: host, user")

    config_path = config or config_path_for_table(table)
    if not config_path.exists():
        raise SystemExit(f"No config found for table '{table}': {config_path}")

    run_validation(
        config_path=config_path,
        host=host,
        port=port,
        user=user,
        request_timeout=request_timeout,
        auth_token=auth_token,
        auth_header=auth_header,
        transaction_limit=transaction_limit,
    )


if __name__ == "__main__":
    typer.run(main)

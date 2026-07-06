"""CLI entrypoint for the `request` table vertical slice.

Kept for back-compat; it's a thin wrapper over the generic runner. New tables
should use run_validation.py --table <name>. Both share ge_validator/runner.py.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Annotated

import typer

from ge_validator.runner import config_path_for_table, run_validation

_DEFAULT_CONFIG = config_path_for_table("request")


def main(
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
    config_path: Annotated[Path, typer.Option("--config", help="Table config YAML")] = _DEFAULT_CONFIG,
) -> None:
    if not host or not user:
        raise SystemExit("Missing required connection args: host, user")

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

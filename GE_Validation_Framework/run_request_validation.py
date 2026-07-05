"""CLI entrypoint for the `request` table GE validation vertical slice.

Mirrors BVC_Analyzer_Sample/bcv_analyzer.py's CLI conventions (same connection
args, same Presto/Trino gateway requirements) so both tools can be run the same way.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Annotated

import typer

_BCV_ANALYZER_DIR = Path(__file__).resolve().parent.parent / "BVC_Analyzer_Sample"
if str(_BCV_ANALYZER_DIR) not in sys.path:
    sys.path.insert(0, str(_BCV_ANALYZER_DIR))

import bcv_analyzer  # noqa: E402

from ge_validator import datasource, report, schema_suite  # noqa: E402
from ge_validator.config import load_table_config  # noqa: E402
from ge_validator.reconciliation import (  # noqa: E402
    build_reconciliation_dataframe,
    build_reconciliation_suite,
    run_reconciliation_suite,
    sample_src_and_bcv,
)

_DEFAULT_CONFIG = Path(__file__).resolve().parent / "config" / "request.yaml"


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
    transaction_limit: Annotated[
        int, typer.Option(help="Rows to sample for reconciliation")
    ] = 10,
    config_path: Annotated[Path, typer.Option("--config", help="Table config YAML")] = _DEFAULT_CONFIG,
) -> None:
    if not host or not user:
        raise SystemExit("Missing required connection args: host, user")

    config = load_table_config(config_path)

    src_catalog, src_schema = config.src_table.split(".")[:2]
    bcv_catalog, bcv_schema = config.bcv_table.split(".")[:2]

    src_connection_kwargs = bcv_analyzer.build_connection_kwargs(
        host, port, user, src_catalog, src_schema, request_timeout, auth_token, auth_header,
    )
    bcv_connection_kwargs = bcv_analyzer.build_connection_kwargs(
        host, port, user, bcv_catalog, bcv_schema, request_timeout, auth_token, auth_header,
    )

    context = datasource.get_context()
    bcv_datasource = datasource.add_sql_datasource(
        context,
        name=f"{config.table}_bcv",
        connection_string=datasource.build_trino_connection_string(host, port, user, bcv_catalog, bcv_schema),
    )

    # --- Schema-level validation ---
    schema = schema_suite.build_schema_suite(context, config)
    schema_validation = schema_suite.run_schema_suite(context, bcv_datasource, config, schema)
    schema_result = schema_validation.run()
    report.print_summary(f"{config.table} — schema", report.summarize(schema_result, config))

    # --- Row-level reconciliation ---
    columns = [c.name for c in config.confirmed_matching_columns] + [
        d.column for d in config.known_type_diffs
    ]
    src_rows, bcv_rows = sample_src_and_bcv(
        config, src_connection_kwargs, bcv_connection_kwargs, columns, transaction_limit=transaction_limit,
    )
    if not bcv_rows:
        print(f"\nNo BCV rows matched the sampled SRC keys for '{config.table}' — skipping reconciliation.")
        return

    dataframe = build_reconciliation_dataframe(config, src_rows, bcv_rows, columns)
    reconciliation_suite = build_reconciliation_suite(context, config, columns)
    reconciliation_validation = run_reconciliation_suite(context, config, reconciliation_suite, dataframe)
    reconciliation_result = reconciliation_validation.run(batch_parameters={"dataframe": dataframe})
    report.print_summary(f"{config.table} — reconciliation", report.summarize(reconciliation_result, config))


if __name__ == "__main__":
    typer.run(main)

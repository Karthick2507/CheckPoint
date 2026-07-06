"""Table-agnostic orchestration shared by every CLI entrypoint.

Both run_validation.py (generic, --table) and run_request_validation.py delegate
here, so the schema + reconciliation flow lives in exactly one place.
"""
from __future__ import annotations

import sys
from pathlib import Path

_BCV_ANALYZER_DIR = Path(__file__).resolve().parents[1].parent / "BCV_analyzer"
if str(_BCV_ANALYZER_DIR) not in sys.path:
    sys.path.insert(0, str(_BCV_ANALYZER_DIR))

import bcv_analyzer  # noqa: E402

from ge_validator import datasource, report, schema_suite
from ge_validator.config import load_table_config
from ge_validator.reconciliation import (
    build_reconciliation_dataframe,
    build_reconciliation_suite,
    run_reconciliation_suite,
    sample_src_and_bcv,
)

CONFIG_DIR = Path(__file__).resolve().parents[1] / "config"


def config_path_for_table(table: str) -> Path:
    return CONFIG_DIR / f"{table}.yaml"


def run_validation(
    config_path: Path,
    host: str,
    port: int,
    user: str,
    request_timeout: float,
    auth_token: str | None,
    auth_header: str | None,
    transaction_limit: int = 10,
) -> None:
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

    # --- Schema-level validation ---
    # Read the BCV schema over bcv_analyzer's connection (DESCRIBE), then run GE
    # column-existence expectations against a pandas batch. Avoids GE's native Trino
    # SQLAlchemy engine, which the Presto gateway rejects on its connection probe.
    bcv_schema = schema_suite.fetch_bcv_schema(config, bcv_connection_kwargs)
    schema = schema_suite.build_schema_suite(context, config)
    schema_validation, schema_dataframe = schema_suite.run_schema_suite(context, config, schema, bcv_schema)
    schema_result = schema_validation.run(batch_parameters={"dataframe": schema_dataframe})
    report.print_summary(f"{config.table} — schema (column existence)", report.summarize(schema_result, config))

    type_diff_results = schema_suite.verify_type_diffs(bcv_schema, config)
    schema_suite.print_type_diff_summary(f"{config.table} — schema (type diffs)", type_diff_results)

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
    report.print_summary(
        f"{config.table} — reconciliation", report.summarize(reconciliation_result, config)
    )

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import great_expectations as gx
import great_expectations.expectations as gxe
import pandas as pd
from great_expectations.data_context import AbstractDataContext

from ge_validator.config import TableValidationConfig

# bcv_analyzer.py is a flat script with no package structure (no __init__.py / pyproject.toml),
# so it can't be imported as a normal package -- add its directory to sys.path instead of
# duplicating its already-tested SQL-building and execute_sql logic here.
_BCV_ANALYZER_DIR = Path(__file__).resolve().parents[2] / "BVC_Analyzer_Sample"
if str(_BCV_ANALYZER_DIR) not in sys.path:
    sys.path.insert(0, str(_BCV_ANALYZER_DIR))

import bcv_analyzer  # noqa: E402


def sample_src_and_bcv(
    config: TableValidationConfig,
    src_connection_kwargs: dict[str, Any],
    bcv_connection_kwargs: dict[str, Any],
    columns: list[str],
    transaction_limit: int = 10,
    now: datetime | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Sample the same rows from SRC and BCV, reusing bcv_analyzer's TABLESAMPLE +
    sampled-bit-flag + batch_id anchoring so this framework observes the exact same
    row set bcv_analyzer.py would (see README's "Sampling contract").
    """
    batch_id = bcv_analyzer.build_value_validation_batch_id(now)
    sql_batches = bcv_analyzer.build_value_validation_sql_batches(
        config.table, columns, batch_id, config.key_columns, limit=transaction_limit,
    )
    if len(sql_batches) != 1:
        raise ValueError(
            f"Expected a single batch for {len(columns)} columns; got {len(sql_batches)}."
            " This framework doesn't yet chunk >500-column validations -- see bcv_analyzer.py's"
            " own batching if that's ever needed here."
        )
    batch = sql_batches[0]

    src_rows = bcv_analyzer.execute_sql(batch["src_sql"], connection_kwargs=src_connection_kwargs)
    keys = bcv_analyzer.get_row_keys(src_rows, config.key_columns)
    if not keys:
        return src_rows, []

    bcv_sql = bcv_analyzer.build_value_validation_bcv_sql(
        config.table, batch["columns"], batch_id, config.key_columns, keys, limit=transaction_limit,
    )
    bcv_rows = bcv_analyzer.execute_sql(bcv_sql, connection_kwargs=bcv_connection_kwargs)
    return src_rows, bcv_rows


def build_reconciliation_dataframe(
    config: TableValidationConfig,
    src_rows: list[dict[str, Any]],
    bcv_rows: list[dict[str, Any]],
    columns: list[str],
) -> pd.DataFrame:
    """Join SRC/BCV rows by key, normalizing known-equivalent values (README's
    "Silent null-semantics false positives" break point) before comparison.

    Produces one row per matched key with `src__<col>` / `bcv__<col>` pairs, ready
    for GE's expect_column_pair_values_to_be_equal per column.
    """
    equivalences = config.known_value_equivalences
    bcv_by_key = {
        bcv_analyzer.extract_row_key(row, config.key_columns): row for row in bcv_rows
    }

    records = []
    for src_row in src_rows:
        key = bcv_analyzer.extract_row_key(src_row, config.key_columns)
        bcv_row = bcv_by_key.get(key)
        if bcv_row is None:
            continue  # unmatched keys are surfaced via the row-count check, not silently dropped
        record = {"_key": bcv_analyzer.format_row_key(key)}
        for column in columns:
            src_value = bcv_analyzer.get_case_insensitive(src_row, column)
            bcv_value = bcv_analyzer.get_case_insensitive(bcv_row, column)
            record[f"src__{column}"] = equivalences.normalize(column, src_value)
            record[f"bcv__{column}"] = equivalences.normalize(column, bcv_value)
        records.append(record)

    return pd.DataFrame.from_records(records)


def build_reconciliation_suite(
    context: AbstractDataContext, config: TableValidationConfig, columns: list[str],
) -> gx.ExpectationSuite:
    suite = context.suites.add(gx.ExpectationSuite(name=f"{config.table}_reconciliation_suite"))
    for column in columns:
        suite.add_expectation(
            gxe.ExpectColumnPairValuesToBeEqual(column_A=f"src__{column}", column_B=f"bcv__{column}")
        )
    return suite


def run_reconciliation_suite(
    context: AbstractDataContext,
    config: TableValidationConfig,
    suite: gx.ExpectationSuite,
    dataframe: pd.DataFrame,
) -> gx.core.validation_definition.ValidationDefinition:
    datasource = context.data_sources.add_or_update_pandas(name=f"{config.table}_reconciliation_pandas")
    asset = datasource.add_dataframe_asset(name=f"{config.table}_reconciliation_asset")
    batch_definition = asset.add_batch_definition_whole_dataframe(f"{config.table}_reconciliation_full")

    validation_definition = context.validation_definitions.add(
        gx.ValidationDefinition(
            name=f"{config.table}_reconciliation_validation",
            data=batch_definition,
            suite=suite,
        )
    )
    return validation_definition

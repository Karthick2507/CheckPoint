from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import great_expectations as gx
import great_expectations.expectations as gxe
import pandas as pd
from great_expectations.data_context import AbstractDataContext

from ge_validator.config import TableValidationConfig

# Reuse bcv_analyzer's connection path to read the BCV schema. GE's native SQLAlchemy
# Trino datasource issues prepared-statement / EXECUTE IMMEDIATE probes that the Presto
# gateway rejects ("mismatched input ''SELECT 1''"), whereas bcv_analyzer runs plain
# cursor.execute(DESCRIBE ...) which the gateway accepts. So the schema step fetches the
# column list the same way reconciliation samples rows, then runs GE column-existence
# expectations against an in-memory pandas batch (backend-agnostic, no Trino dialect).
_BCV_ANALYZER_DIR = Path(__file__).resolve().parents[2] / "BCV_analyzer"
if str(_BCV_ANALYZER_DIR) not in sys.path:
    sys.path.insert(0, str(_BCV_ANALYZER_DIR))

import bcv_analyzer  # noqa: E402


def fetch_bcv_schema(config: TableValidationConfig, bcv_connection_kwargs: dict[str, Any]) -> dict[str, str]:
    """Return {column_name: trino_type} for the BCV table via DESCRIBE, over the working
    bcv_analyzer connection (not GE's incompatible SQLAlchemy engine)."""
    describe_sql = bcv_analyzer.build_bcv_describe_sql(config.table)
    rows = bcv_analyzer.execute_sql(describe_sql, connection_kwargs=bcv_connection_kwargs)
    schema: dict[str, str] = {}
    for row in rows:
        column = str(bcv_analyzer.get_case_insensitive(row, "column"))
        col_type = str(bcv_analyzer.get_case_insensitive(row, "type"))
        if column:
            schema[column] = col_type
    return schema


def build_schema_dataframe(bcv_schema: dict[str, str]) -> pd.DataFrame:
    """A single-row frame whose columns are the BCV's real columns, so GE's
    ExpectColumnToExist can run against a pandas batch."""
    return pd.DataFrame([{column: None for column in bcv_schema}])


def build_schema_suite(context: AbstractDataContext, config: TableValidationConfig) -> gx.ExpectationSuite:
    """Column-existence expectations for every column the mapping says the BCV should have.

    Deliberately does NOT assert on config.known_dropped_prefixes columns (documented as
    intentionally absent) nor on config.excluded_columns (never surfaced in the BCV) --
    asserting their absence would just re-test a decision already made. Column *types* are
    checked separately in verify_type_diffs() against the DESCRIBE metadata, since GE's
    pandas type inference can't validate Trino type strings like 'array(bigint)'.
    """
    suite = context.suites.add(gx.ExpectationSuite(name=f"{config.table}_schema_suite"))
    for column in config.confirmed_matching_columns:
        suite.add_expectation(gxe.ExpectColumnToExist(column=column.name))
    for diff in config.known_type_diffs:
        suite.add_expectation(gxe.ExpectColumnToExist(column=diff.column))
    return suite


def run_schema_suite(
    context: AbstractDataContext,
    config: TableValidationConfig,
    suite: gx.ExpectationSuite,
    bcv_schema: dict[str, str],
) -> tuple[gx.core.validation_definition.ValidationDefinition, pd.DataFrame]:
    """Wire the existence suite to a pandas batch built from the real BCV schema.
    Returns the validation definition and the dataframe to pass as batch_parameters."""
    dataframe = build_schema_dataframe(bcv_schema)
    ds = context.data_sources.add_or_update_pandas(name=f"{config.table}_schema_pandas")
    asset = ds.add_dataframe_asset(name=f"{config.table}_schema_asset")
    batch_definition = asset.add_batch_definition_whole_dataframe(f"{config.table}_schema_full")

    validation_definition = context.validation_definitions.add(
        gx.ValidationDefinition(
            name=f"{config.table}_schema_validation",
            data=batch_definition,
            suite=suite,
        )
    )
    return validation_definition, dataframe


def _normalize_type(type_str: str) -> str:
    return type_str.replace(" ", "").lower()


def verify_type_diffs(bcv_schema: dict[str, str], config: TableValidationConfig) -> list[dict[str, Any]]:
    """Confirm each documented type diff still matches the live BCV type from DESCRIBE.

    Returns one record per known_type_diff: whether the live BCV type still equals the
    documented bcv_type. A mismatch means the documented state has drifted -- worth
    surfacing, especially for the diffs flagged as real issues (expected == False).
    """
    results: list[dict[str, Any]] = []
    for diff in config.known_type_diffs:
        actual = bcv_schema.get(diff.column)
        matches = actual is not None and _normalize_type(actual) == _normalize_type(diff.bcv_type)
        results.append({
            "column": diff.column,
            "expected_bcv_type": diff.bcv_type,
            "actual_bcv_type": actual if actual is not None else "(column missing)",
            "matches": matches,
            "is_known_issue": not diff.expected,
        })
    return results


def print_type_diff_summary(title: str, results: list[dict[str, Any]]) -> None:
    print(f"\n== {title} ==")
    if not results:
        print("No documented type diffs to check.")
        return
    for r in results:
        status = "OK   " if r["matches"] else "DRIFT"
        tag = "  [known issue]" if r["is_known_issue"] else ""
        print(f"  {status} {r['column']}")
        if not r["matches"]:
            print(f"        expected {r['expected_bcv_type']!r}, live BCV is {r['actual_bcv_type']!r}{tag}")

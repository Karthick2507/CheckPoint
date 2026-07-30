"""Capture the rows that failed validation.

A warnings report tells you *that* 412 rows were null; it does not tell you
*which* ones, so triage means hand-writing a query to go find them. Quarantine
writes the offending rows to disk as CSV, one file per failing expectation::

    etl_output/runs/<run_id>/quarantine/<suite>__<expectation_id>.csv

Great Expectations already collects a sample of unexpected values when asked
(``result_format: COMPLETE``/``SUMMARY``), so this reuses that rather than
re-querying the warehouse. Only failing expectations produce a file, and the
sample is capped so a fully broken batch cannot write a million-row CSV.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # avoid a runtime import cycle
    from core.pipeline import PipelineResult
    from core.validate.framework import ValidationOutcome

_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

DEFAULT_SAMPLE_LIMIT = 1000


def _slug(value: str) -> str:
    return _SAFE.sub("_", value)[:120]


def quarantine_rows(row: Any, limit: int = DEFAULT_SAMPLE_LIMIT) -> list[dict[str, Any]]:
    """Extract the offending values GE recorded for a failed expectation."""
    detail = getattr(row, "result_detail", None) or {}
    unexpected = detail.get("partial_unexpected_list") or detail.get("unexpected_list") or []
    column = row.column or "value"
    records: list[dict[str, Any]] = []
    for value in unexpected[:limit]:
        if isinstance(value, dict):
            records.append(value)
        else:
            records.append({column: value})
    return records


def write_quarantine(
    outcome: "ValidationOutcome",
    quarantine_dir: Path,
    limit: int = DEFAULT_SAMPLE_LIMIT,
) -> list[Path]:
    """Write one CSV per failing expectation that has offending rows."""
    written: list[Path] = []
    for row in outcome.failures:
        records = quarantine_rows(row, limit=limit)
        if not records:
            continue  # e.g. a table-level expectation has no offending rows
        name = _slug(f"{outcome.suite_name}__{row.expectation_id or row.expectation_type}")
        path = quarantine_dir / f"{name}.csv"
        quarantine_dir.mkdir(parents=True, exist_ok=True)

        fieldnames: list[str] = []
        for record in records:
            for key in record:
                if key not in fieldnames:
                    fieldnames.append(key)

        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(records)
        written.append(path)

        # For expectations whose offending values are not self-identifying (a
        # null-check yields a column of nulls), GE can supply a query that
        # locates the actual rows. That is the artifact an analyst wants.
        index_query = (getattr(row, "result_detail", None) or {}).get("unexpected_index_query")
        if index_query:
            query_path = path.with_suffix(".sql")
            query_path.write_text(
                f"-- rows failing {row.expectation_type}"
                + (f" on column {row.column}" if row.column else "")
                + f"\n{index_query}\n",
                encoding="utf-8",
            )
            written.append(query_path)
    return written


def write_run_quarantine(result: "PipelineResult", limit: int = DEFAULT_SAMPLE_LIMIT) -> list[Path]:
    """Write quarantine files for every failing expectation in a run."""
    quarantine_dir = result.context.subdir("quarantine")
    written: list[Path] = []
    for outcome in result.validations:
        written.extend(write_quarantine(outcome, quarantine_dir, limit=limit))
    return written

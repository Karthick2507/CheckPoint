"""Row-level quarantine tests (P2).

``quarantine/`` was created on every run and documented in DESIGN.md, but
nothing ever wrote to it. A warnings report says *that* 412 rows were bad; it
does not say *which*, so triage meant hand-writing a query. Quarantine writes
the offending rows out.
"""

from __future__ import annotations

import csv
import sqlite3

import pytest
import yaml

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from core.validate import GEValidationFramework, SuiteConfig
from data_sources.base import DataSource
from reporting import write_pipeline_reports, write_run_quarantine
from reporting.quarantine import quarantine_rows, write_quarantine
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


@pytest.fixture()
def source(tmp_path):
    db = tmp_path / "s.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (id INTEGER, grade TEXT, score INTEGER)")
    con.executemany(
        "INSERT INTO t VALUES (?, ?, ?)",
        [(1, "A", 10), (2, "ZZZ", 20), (3, "B", 9999), (4, "QQQ", 30)],
    )
    con.commit()
    con.close()
    return _SqliteSource({"name": "src", "path": str(db)})


def _outcome(source, expectations):
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"type": "table", "name": "t", "table_name": "t"}},
            "expectations": expectations,
        }
    )
    return GEValidationFramework(source).run(suite)


def _read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


# --------------------------------------------------------------------------
# Extracting offending values
# --------------------------------------------------------------------------


def test_offending_values_are_captured(source):
    outcome = _outcome(
        source, [{"type": "expect_column_values_to_be_in_set", "column": "grade", "value_set": ["A", "B"]}]
    )
    assert outcome.success is False
    records = quarantine_rows(outcome.failures[0])
    values = {r["grade"] for r in records}
    assert values == {"ZZZ", "QQQ"}, "the actual bad values, not just a count"


def test_sample_is_capped(source):
    outcome = _outcome(
        source, [{"type": "expect_column_values_to_be_in_set", "column": "grade", "value_set": ["A", "B"]}]
    )
    assert len(quarantine_rows(outcome.failures[0], limit=1)) == 1


def test_passing_expectation_yields_nothing(source):
    outcome = _outcome(source, [{"type": "expect_column_to_exist", "column": "id"}])
    assert outcome.success is True
    assert outcome.failures == []


# --------------------------------------------------------------------------
# Writing files
# --------------------------------------------------------------------------


def test_writes_csv_per_failing_expectation(source, tmp_path):
    outcome = _outcome(
        source,
        [
            {"type": "expect_column_values_to_be_in_set", "column": "grade", "value_set": ["A", "B"],
             "id": "grade_set"},
            {"type": "expect_column_values_to_be_between", "column": "score", "min_value": 0,
             "max_value": 100, "id": "score_range"},
        ],
    )
    written = write_quarantine(outcome, tmp_path / "q")
    names = sorted(p.name for p in written if p.suffix == ".csv")
    assert names == ["s__grade_set.csv", "s__score_range.csv"]

    rows = _read(tmp_path / "q" / "s__score_range.csv")
    assert [r["score"] for r in rows] == ["9999"]


def test_no_file_for_table_level_expectation(source, tmp_path):
    """A row-count expectation has no offending rows to quarantine."""
    outcome = _outcome(source, [{"type": "expect_table_row_count_to_be_between", "min_value": 100}])
    assert outcome.success is False
    assert write_quarantine(outcome, tmp_path / "q") == []


def test_filenames_are_sanitized(source, tmp_path):
    outcome = _outcome(
        source,
        [{"type": "expect_column_values_to_be_in_set", "column": "grade", "value_set": ["A", "B"],
          "id": "weird/id with spaces"}],
    )
    written = write_quarantine(outcome, tmp_path / "q")
    assert written and "/" not in written[0].name
    assert written[0].parent == tmp_path / "q"


def test_nothing_written_when_all_pass(source, tmp_path):
    outcome = _outcome(source, [{"type": "expect_column_to_exist", "column": "id"}])
    assert write_quarantine(outcome, tmp_path / "q") == []


# --------------------------------------------------------------------------
# Through the pipeline
# --------------------------------------------------------------------------


def _run(tmp_path, source, expectations):
    suite_path = tmp_path / "raw.yml"
    suite_path.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": "raw", "asset": {"type": "table", "name": "t", "table_name": "t"}},
                "expectations": expectations,
            }
        )
    )
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "validate": {"raw": str(suite_path)},
            }
        }
    )
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out", state_root=tmp_path / "state")
    return Pipeline(cfg, resolve_source=lambda n: source, state=FileState(tmp_path / "st"), context=ctx).run()


def test_pipeline_writes_quarantine(tmp_path, source):
    result = _run(
        tmp_path,
        source,
        [{"type": "expect_column_values_to_be_in_set", "column": "grade", "value_set": ["A", "B"],
          "id": "grade_set", "severity": "critical"}],
    )
    paths = write_pipeline_reports(result)
    assert paths["quarantine"], "the documented quarantine dir must actually be populated"

    csv_path = next(p for p in paths["quarantine"] if p.suffix == ".csv")
    assert csv_path.parent == result.context.run_dir / "quarantine"
    assert {r["grade"] for r in _read(csv_path)} == {"ZZZ", "QQQ"}


def test_clean_run_leaves_quarantine_empty(tmp_path, source):
    result = _run(tmp_path, source, [{"type": "expect_column_to_exist", "column": "id"}])
    paths = write_pipeline_reports(result)
    assert paths["quarantine"] == []
    assert list((result.context.run_dir / "quarantine").iterdir()) == []


def test_write_run_quarantine_covers_all_gates(tmp_path, source):
    result = _run(
        tmp_path,
        source,
        [{"type": "expect_column_values_to_be_between", "column": "score", "min_value": 0, "max_value": 100}],
    )
    written = write_run_quarantine(result)
    assert len(written) >= 1
    assert all(p.exists() for p in written)

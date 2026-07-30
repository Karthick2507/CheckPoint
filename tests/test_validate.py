"""Tests for the validation layer (core/validate).

End-to-end tests run real Great Expectations validations against a temporary
sqlite database, driven through a ``DataSource`` — the same code path Presto and
Snowflake use — so the full flow is exercised without a live gateway.
"""

from __future__ import annotations

import json
import sqlite3

import pytest

from core.validate import (
    GEValidationFramework,
    SuiteConfig,
    ValidationOutcome,
    build_expectation,
    expectation_class_name,
    write_json_report,
    write_markdown_report,
)
from core.validate.suite_config import AssetConfig, ExpectationConfig, load_suite_config
from data_sources.base import DataSource


# --------------------------------------------------------------------------
# Suite config parsing
# --------------------------------------------------------------------------


def test_suite_config_parsing(tmp_path):
    cfg = tmp_path / "s.yml"
    cfg.write_text(
        "suite:\n"
        "  name: q\n"
        "  asset:\n"
        "    type: table\n"
        "    name: t\n"
        "    table_name: t\n"
        "expectations:\n"
        "  - type: expect_column_values_to_not_be_null\n"
        "    column: id\n"
        "    severity: critical\n"
    )
    sc = load_suite_config(cfg)
    assert sc.name == "q"
    assert sc.asset.type == "table"
    assert sc.expectations[0].type == "expect_column_values_to_not_be_null"
    assert sc.expectations[0].kwargs == {"column": "id"}
    assert sc.expectations[0].severity == "critical"


def test_default_severity_is_warning():
    ec = ExpectationConfig.from_dict({"type": "expect_column_to_exist", "column": "x"})
    assert ec.severity == "warning"


def test_invalid_severity_rejected():
    with pytest.raises(ValueError, match="Invalid severity"):
        ExpectationConfig.from_dict({"type": "expect_column_to_exist", "column": "x", "severity": "urgent"})


def test_query_asset_requires_query():
    with pytest.raises(ValueError):
        AssetConfig.from_dict({"type": "query", "name": "q"})


def test_suite_requires_expectations(tmp_path):
    cfg = tmp_path / "s.yml"
    cfg.write_text("suite:\n  name: q\n  asset:\n    name: t\n    table_name: t\nexpectations: []\n")
    with pytest.raises(ValueError):
        load_suite_config(cfg)


def test_severity_lookup_by_id():
    """Severity resolves via the config-assigned id (see tests/test_severity.py)."""
    sc = SuiteConfig.from_dict(
        {
            "suite": {"name": "q", "asset": {"name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "id", "severity": "critical"},
                {"type": "expect_table_row_count_to_be_between", "min_value": 1},
            ],
        }
    )
    assert sc.severity_by_id(sc.expectations[0].id) == "critical"
    assert sc.severity_by_id(sc.expectations[1].id) == "warning"


# --------------------------------------------------------------------------
# Expectation factory
# --------------------------------------------------------------------------


def test_expectation_class_name():
    assert expectation_class_name("expect_column_values_to_not_be_null") == "ExpectColumnValuesToNotBeNull"
    assert expectation_class_name("expect_table_row_count_to_be_between") == "ExpectTableRowCountToBeBetween"


def test_build_expectation_ok():
    exp = build_expectation(ExpectationConfig(type="expect_column_values_to_not_be_null", kwargs={"column": "x"}))
    assert exp.column == "x"


def test_build_expectation_unknown_type():
    with pytest.raises(ValueError, match="Unknown expectation"):
        build_expectation(ExpectationConfig(type="expect_the_impossible", kwargs={}))


def test_build_expectation_bad_kwargs():
    with pytest.raises(ValueError, match="Invalid arguments"):
        build_expectation(ExpectationConfig(type="expect_column_values_to_not_be_null", kwargs={}))


# --------------------------------------------------------------------------
# End-to-end run against sqlite (via a DataSource)
# --------------------------------------------------------------------------


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


@pytest.fixture()
def sqlite_source(tmp_path):
    db = tmp_path / "data.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE request (transaction_id TEXT, duration INTEGER)")
    con.executemany(
        "INSERT INTO request VALUES (?, ?)",
        [("t1", 10), ("t2", 20), ("t3", None), ("t4", 30)],
    )
    con.commit()
    con.close()
    return _SqliteSource({"name": "local", "path": str(db)})


def _run(source, suite_cfg: SuiteConfig) -> ValidationOutcome:
    return GEValidationFramework(source).run(suite_cfg)


def test_end_to_end_pass(sqlite_source):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_pass", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "transaction_id"},
                {"type": "expect_table_row_count_to_be_between", "min_value": 1},
            ],
        }
    )
    outcome = _run(sqlite_source, suite_cfg)
    assert outcome.success is True
    assert outcome.evaluated == 2
    assert outcome.successful == 2
    assert outcome.failed == 0


def test_end_to_end_failure_and_severity(sqlite_source):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_fail", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "duration", "severity": "critical"},
                {"type": "expect_column_values_to_be_between", "column": "duration", "min_value": 0, "max_value": 25},
            ],
        }
    )
    outcome = _run(sqlite_source, suite_cfg)
    assert outcome.success is False
    assert outcome.failed == 2
    # warn-and-continue: severity tags flow through, critical is detectable
    assert outcome.has_critical_failure is True
    crit = outcome.critical_failures
    assert len(crit) == 1
    assert crit[0].column == "duration"
    assert crit[0].expectation_type == "expect_column_values_to_not_be_null"


def test_query_asset_end_to_end(sqlite_source):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {
                "name": "req_query",
                "asset": {
                    "type": "query",
                    "name": "request_q",
                    "query": "SELECT transaction_id FROM request WHERE duration IS NOT NULL",
                },
            },
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "transaction_id"},
            ],
        }
    )
    outcome = _run(sqlite_source, suite_cfg)
    assert outcome.success is True


def test_outcome_is_json_serializable(sqlite_source):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_json", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [{"type": "expect_table_row_count_to_be_between", "min_value": 1}],
        }
    )
    outcome = _run(sqlite_source, suite_cfg)
    data = json.dumps(outcome.to_dict())  # must not raise
    assert '"severity"' in data


def test_reports_written(sqlite_source, tmp_path):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_report", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "duration"},
            ],
        }
    )
    outcome = _run(sqlite_source, suite_cfg)
    json_path = write_json_report(outcome, output_dir=tmp_path)
    md_path = write_markdown_report(outcome, output_dir=tmp_path)
    assert json_path.exists()
    assert md_path.exists()
    data = json.loads(json_path.read_text())
    assert data["suite_name"] == "req_report"
    assert "Failed Expectations" in md_path.read_text()

"""Severity-resolution tests (P0 hardening).

Severity drives the whole triage model, so a result must map back to the exact
suite entry that produced it. Matching on kwargs was unreliable (GE normalises
and augments them), which silently gave every same-type expectation the first
one's severity. Identity now travels through GE ``meta``.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.validate import GEValidationFramework, SuiteConfig
from core.validate.suite_config import META_ID_KEY, ExpectationConfig
from core.validate.expectations import build_expectation
from data_sources.base import DataSource


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


@pytest.fixture()
def source(tmp_path):
    db = tmp_path / "d.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (a TEXT, b TEXT, c INTEGER)")
    con.executemany("INSERT INTO t VALUES (?, ?, ?)", [("x", None, 5), (None, "y", 500)])
    con.commit()
    con.close()
    return _SqliteSource({"name": "s", "path": str(db)})


# --------------------------------------------------------------------------
# Config-level identity
# --------------------------------------------------------------------------


def test_ids_are_assigned_by_position():
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "a"},
                {"type": "expect_column_values_to_not_be_null", "column": "b"},
            ],
        }
    )
    assert suite.expectations[0].id == "0:expect_column_values_to_not_be_null"
    assert suite.expectations[1].id == "1:expect_column_values_to_not_be_null"


def test_explicit_id_is_respected():
    cfg = ExpectationConfig.from_dict({"type": "expect_column_to_exist", "column": "a", "id": "pk_exists"})
    assert cfg.id == "pk_exists"
    assert "id" not in cfg.kwargs


def test_duplicate_explicit_ids_rejected():
    with pytest.raises(ValueError, match="Duplicate expectation id"):
        SuiteConfig.from_dict(
            {
                "suite": {"name": "s", "asset": {"name": "t", "table_name": "t"}},
                "expectations": [
                    {"type": "expect_column_to_exist", "column": "a", "id": "dup"},
                    {"type": "expect_column_to_exist", "column": "b", "id": "dup"},
                ],
            }
        )


def test_build_meta_merges_user_meta():
    cfg = ExpectationConfig.from_dict(
        {"type": "expect_column_to_exist", "column": "a", "meta": {"owner": "data-eng"}}, index=3
    )
    meta = cfg.build_meta()
    assert meta["owner"] == "data-eng"
    assert meta[META_ID_KEY] == cfg.id
    assert "meta" not in cfg.kwargs


def test_expectation_carries_meta_id():
    cfg = ExpectationConfig.from_dict({"type": "expect_column_values_to_not_be_null", "column": "a"}, index=7)
    expectation = build_expectation(cfg)
    assert expectation.meta[META_ID_KEY] == cfg.id


def test_severity_by_id_lookup():
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_to_exist", "column": "a", "id": "warn_one"},
                {"type": "expect_column_to_exist", "column": "b", "id": "crit_one", "severity": "critical"},
            ],
        }
    )
    assert suite.severity_by_id("warn_one") == "warning"
    assert suite.severity_by_id("crit_one") == "critical"
    assert suite.severity_by_id("unknown") == "warning"
    assert suite.severity_by_id(None) == "warning"


# --------------------------------------------------------------------------
# The regression: same type, different severities
# --------------------------------------------------------------------------


def test_same_type_expectations_keep_distinct_severities(source):
    """Previously both rows collapsed to the FIRST entry's severity."""
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s1", "asset": {"type": "table", "name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "a", "severity": "warning"},
                {"type": "expect_column_values_to_not_be_null", "column": "b", "severity": "critical"},
            ],
        }
    )
    outcome = GEValidationFramework(source).run(suite)
    by_column = {r.column: r for r in outcome.results}

    assert by_column["a"].severity == "warning"
    assert by_column["b"].severity == "critical"
    assert outcome.has_critical_failure is True
    assert [r.column for r in outcome.critical_failures] == ["b"]


def test_critical_first_then_warning_order_does_not_matter(source):
    """The reverse order must work too — no positional bias."""
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s2", "asset": {"type": "table", "name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "b", "severity": "critical"},
                {"type": "expect_column_values_to_not_be_null", "column": "a", "severity": "warning"},
            ],
        }
    )
    outcome = GEValidationFramework(source).run(suite)
    by_column = {r.column: r for r in outcome.results}
    assert by_column["b"].severity == "critical"
    assert by_column["a"].severity == "warning"


def test_every_result_carries_its_id(source):
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s3", "asset": {"type": "table", "name": "t", "table_name": "t"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "a", "id": "a_notnull"},
                {"type": "expect_column_values_to_be_between", "column": "c", "min_value": 0, "max_value": 10,
                 "id": "c_range", "severity": "critical"},
            ],
        }
    )
    outcome = GEValidationFramework(source).run(suite)
    ids = {r.expectation_id for r in outcome.results}
    assert ids == {"a_notnull", "c_range"}
    # c has a 500 value -> fails, and it is the critical one
    crit = outcome.critical_failures
    assert len(crit) == 1
    assert crit[0].expectation_id == "c_range"


def test_expectation_id_is_serialized(source):
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s4", "asset": {"type": "table", "name": "t", "table_name": "t"}},
            "expectations": [{"type": "expect_column_to_exist", "column": "a", "id": "exists"}],
        }
    )
    outcome = GEValidationFramework(source).run(suite)
    payload = outcome.to_dict()
    assert payload["results"][0]["expectation_id"] == "exists"

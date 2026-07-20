"""Tests for the GE validation framework.

The end-to-end tests run real Great Expectations checkpoints against a
temporary sqlite database. The framework's SQL plumbing is database-agnostic,
so this exercises the full path (datasource -> asset -> suite -> validation ->
result normalization) without needing a live Presto/Trino gateway.
"""

from __future__ import annotations

import json
import sqlite3

import great_expectations as gx
import pytest

from ge_framework.config import (
    AssetConfig,
    DatasourceConfig,
    ExpectationConfig,
    SuiteConfig,
    load_datasource_config,
    load_suite_config,
)
from ge_framework.expectations import build_expectation, expectation_class_name
from ge_framework.framework import GEValidationFramework, ValidationOutcome
from ge_framework.presto import (
    build_connect_args,
    build_connection_string,
    build_http_headers,
)
from ge_framework.reporting import write_json_report, write_markdown_report


# --------------------------------------------------------------------------
# Presto connection layer
# --------------------------------------------------------------------------


def test_connection_string():
    ds = DatasourceConfig(name="p", host="h.example.net", port=8080, user="alice", catalog="c", schema="s")
    assert build_connection_string(ds) == "trino://alice@h.example.net:8080/c/s"


def test_bearer_header_default():
    assert build_http_headers("tok", None) == {"Authorization": "Bearer tok"}
    assert build_http_headers("tok", "Authorization") == {"Authorization": "Bearer tok"}


def test_custom_header_is_raw_token():
    assert build_http_headers("tok", "X-Presto-Token") == {"X-Presto-Token": "tok"}


def test_no_token_no_headers():
    assert build_http_headers(None, None) == {}


def test_connect_args_includes_scheme_and_headers():
    ds = DatasourceConfig(
        name="p", host="h", catalog="c", schema="s", auth_token="tok", http_scheme="https", request_timeout=15
    )
    args = build_connect_args(ds)
    assert args["http_scheme"] == "https"
    assert args["request_timeout"] == 15
    assert args["http_headers"] == {"Authorization": "Bearer tok"}


def test_connect_args_omits_headers_without_token():
    ds = DatasourceConfig(name="p", host="h", catalog="c", schema="s")
    assert "http_headers" not in build_connect_args(ds)


# --------------------------------------------------------------------------
# Config loading
# --------------------------------------------------------------------------


def test_datasource_env_interpolation_and_fallback(monkeypatch, tmp_path):
    monkeypatch.setenv("PRESTO_AUTH_TOKEN", "env-token")
    monkeypatch.setenv("MY_HOST", "gw.example.net")
    cfg = tmp_path / "ds.yml"
    cfg.write_text(
        "datasource:\n"
        "  name: p\n"
        "  host: ${MY_HOST}\n"
        "  catalog: c\n"
        "  schema: s\n"
        "  auth_token: ${PRESTO_AUTH_TOKEN}\n"
    )
    ds = load_datasource_config(cfg)
    assert ds.host == "gw.example.net"
    assert ds.auth_token == "env-token"


def test_datasource_missing_required_field(tmp_path):
    cfg = tmp_path / "ds.yml"
    cfg.write_text("datasource:\n  name: p\n  catalog: c\n")
    with pytest.raises(ValueError):
        load_datasource_config(cfg)


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
    )
    sc = load_suite_config(cfg)
    assert sc.name == "q"
    assert sc.asset.type == "table"
    assert sc.expectations[0].type == "expect_column_values_to_not_be_null"
    assert sc.expectations[0].kwargs == {"column": "id"}


def test_query_asset_requires_query():
    with pytest.raises(ValueError):
        AssetConfig.from_dict({"type": "query", "name": "q"})


def test_suite_requires_expectations(tmp_path):
    cfg = tmp_path / "s.yml"
    cfg.write_text("suite:\n  name: q\n  asset:\n    name: t\n    table_name: t\nexpectations: []\n")
    with pytest.raises(ValueError):
        load_suite_config(cfg)


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
# End-to-end run against sqlite
# --------------------------------------------------------------------------


@pytest.fixture()
def sqlite_db(tmp_path):
    db = tmp_path / "data.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE request (transaction_id TEXT, duration INTEGER)")
    con.executemany(
        "INSERT INTO request VALUES (?, ?)",
        [("t1", 10), ("t2", 20), ("t3", None), ("t4", 30)],
    )
    con.commit()
    con.close()
    return db


def _run_against_sqlite(db, suite_cfg: SuiteConfig) -> ValidationOutcome:
    ds = DatasourceConfig(name="local", host="x", catalog="c", schema="s")
    context = gx.get_context(mode="ephemeral")
    context.data_sources.add_sql(name=ds.name, connection_string=f"sqlite:///{db}")
    framework = GEValidationFramework(ds, context=context)
    return framework.run(suite_cfg)


def test_end_to_end_pass(sqlite_db):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_pass", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "transaction_id"},
                {"type": "expect_table_row_count_to_be_between", "min_value": 1},
            ],
        }
    )
    outcome = _run_against_sqlite(sqlite_db, suite_cfg)
    assert outcome.success is True
    assert outcome.evaluated == 2
    assert outcome.successful == 2
    assert outcome.failed == 0


def test_end_to_end_failure_and_details(sqlite_db):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_fail", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "duration"},
                {"type": "expect_column_values_to_be_between", "column": "duration", "min_value": 0, "max_value": 25},
            ],
        }
    )
    outcome = _run_against_sqlite(sqlite_db, suite_cfg)
    assert outcome.success is False
    assert outcome.failed == 2
    # both failures have a non-null column recorded
    assert {r.column for r in outcome.results} == {"duration"}
    # unexpected counts are surfaced
    assert any(r.unexpected_count for r in outcome.results if not r.success)


def test_query_asset_end_to_end(sqlite_db):
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
    outcome = _run_against_sqlite(sqlite_db, suite_cfg)
    assert outcome.success is True


def test_outcome_is_json_serializable(sqlite_db):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_json", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [{"type": "expect_table_row_count_to_be_between", "min_value": 1}],
        }
    )
    outcome = _run_against_sqlite(sqlite_db, suite_cfg)
    # to_dict must be fully JSON-serializable (meta may hold GE objects)
    json.dumps(outcome.to_dict())


def test_reports_written(sqlite_db, tmp_path):
    suite_cfg = SuiteConfig.from_dict(
        {
            "suite": {"name": "req_report", "asset": {"type": "table", "name": "request", "table_name": "request"}},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "duration"},
            ],
        }
    )
    outcome = _run_against_sqlite(sqlite_db, suite_cfg)
    json_path = write_json_report(outcome, output_dir=tmp_path)
    md_path = write_markdown_report(outcome, output_dir=tmp_path)
    assert json_path.exists()
    assert md_path.exists()
    data = json.loads(json_path.read_text())
    assert data["suite_name"] == "req_report"
    assert "Failed Expectations" in md_path.read_text()

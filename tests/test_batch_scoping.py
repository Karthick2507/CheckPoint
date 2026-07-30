"""Batch-scoped validation tests (P1).

Every gate previously validated the WHOLE table. For an incremental pipeline
that is both wrong and expensive:

* a bad batch is diluted into all of history, so threshold expectations pass;
* uniqueness fails forever once one historical duplicate exists;
* every expectation full-scans a TiB table on every run.

Scoping narrows the asset to the batch the pipeline just processed.
"""

from __future__ import annotations

import sqlite3

import pytest
import yaml

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from core.validate import GEValidationFramework, SuiteConfig
from core.validate.scoping import build_batch_predicate, scope_asset_to_batch, scope_suite_to_batch
from core.validate.suite_config import AssetConfig
from data_sources.base import DataSource
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


# --------------------------------------------------------------------------
# Predicate + asset rewriting
# --------------------------------------------------------------------------


def test_predicate_from_batch_key():
    asset = AssetConfig.from_dict({"name": "t", "table_name": "t", "batch_key": "pb"})
    assert build_batch_predicate(asset, "B1") == "pb = 'B1'"


def test_predicate_escapes_quotes():
    asset = AssetConfig.from_dict({"name": "t", "table_name": "t", "batch_key": "pb"})
    assert build_batch_predicate(asset, "O'Brien") == "pb = 'O''Brien'"


def test_predicate_numeric_batch_unquoted():
    asset = AssetConfig.from_dict({"name": "t", "table_name": "t", "batch_key": "pb"})
    assert build_batch_predicate(asset, 20260101) == "pb = 20260101"


def test_batch_filter_takes_precedence_and_is_templated():
    asset = AssetConfig.from_dict(
        {"name": "t", "table_name": "t", "batch_key": "pb", "batch_filter": "pb >= '{{ batch_id }}'"}
    )
    assert build_batch_predicate(asset, "B1", {"batch_id": "B1"}) == "pb >= 'B1'"


def test_no_scoping_without_batch_key():
    asset = AssetConfig.from_dict({"name": "t", "table_name": "t"})
    assert build_batch_predicate(asset, "B1") is None
    assert scope_asset_to_batch(asset, "B1") is asset
    assert asset.is_batch_scoped is False


def test_table_asset_becomes_scoped_query():
    asset = AssetConfig.from_dict({"name": "t", "table_name": "req", "batch_key": "pb"})
    scoped = scope_asset_to_batch(asset, "B1")
    assert scoped.type == "query"
    assert scoped.query == "SELECT * FROM req WHERE pb = 'B1'"
    assert scoped.table_name is None


def test_schema_name_is_qualified():
    asset = AssetConfig.from_dict(
        {"name": "t", "table_name": "req", "schema_name": "default", "batch_key": "pb"}
    )
    assert scope_asset_to_batch(asset, "B1").query == "SELECT * FROM default.req WHERE pb = 'B1'"


def test_query_asset_is_wrapped():
    asset = AssetConfig.from_dict(
        {"type": "query", "name": "q", "query": "SELECT a, pb FROM t;", "batch_key": "pb"}
    )
    scoped = scope_asset_to_batch(asset, "B1")
    assert scoped.query == "SELECT * FROM (SELECT a, pb FROM t) AS _scoped WHERE pb = 'B1'"


def test_scope_suite_leaves_unscoped_suite_untouched():
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"name": "t", "table_name": "t"}},
            "expectations": [{"type": "expect_column_to_exist", "column": "a"}],
        }
    )
    assert scope_suite_to_batch(suite, "B1") is suite


def test_scope_suite_preserves_expectations():
    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"name": "t", "table_name": "t", "batch_key": "pb"}},
            "expectations": [{"type": "expect_column_to_exist", "column": "a", "severity": "critical"}],
        }
    )
    scoped = scope_suite_to_batch(suite, "B1")
    assert scoped is not suite
    assert scoped.name == suite.name
    assert [e.id for e in scoped.expectations] == [e.id for e in suite.expectations]
    assert scoped.expectations[0].severity == "critical"


# --------------------------------------------------------------------------
# The behaviour that actually matters
# --------------------------------------------------------------------------


@pytest.fixture()
def history(tmp_path):
    """A big clean history plus a small dirty current batch."""
    db = tmp_path / "h.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE req (id INTEGER, pb TEXT, v TEXT)")
    # 200 good historical rows
    con.executemany(
        "INSERT INTO req VALUES (?, ?, ?)", [(i, "OLD", f"v{i}") for i in range(200)]
    )
    # today's batch: 4 rows, 2 of them NULL
    con.executemany(
        "INSERT INTO req VALUES (?, ?, ?)",
        [(1000, "B1", "x"), (1001, "B1", None), (1002, "B1", None), (1003, "B1", "y")],
    )
    con.commit()
    con.close()
    return _SqliteSource({"name": "src", "path": str(db)})


def _suite(batch_key=None, mostly=0.9):
    asset = {"type": "table", "name": "req", "table_name": "req"}
    if batch_key:
        asset["batch_key"] = batch_key
    return SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": asset},
            "expectations": [
                {"type": "expect_column_values_to_not_be_null", "column": "v", "mostly": mostly},
            ],
        }
    )


def test_whole_table_dilutes_a_bad_batch(history):
    """Unscoped: 2 bad rows in 204 = 99% non-null, so the gate PASSES."""
    outcome = GEValidationFramework(history).run(_suite())
    assert outcome.success is True, "this is the false negative that scoping fixes"


def test_batch_scoped_catches_the_bad_batch(history):
    """Scoped to B1: 2 bad rows in 4 = 50% non-null, so the gate FAILS."""
    scoped = scope_suite_to_batch(_suite(batch_key="pb"), "B1")
    outcome = GEValidationFramework(history).run(scoped)
    assert outcome.success is False, "the bad batch must be caught"
    assert outcome.results[0].unexpected_count == 2


def test_scoped_uniqueness_ignores_historical_duplicates(tmp_path):
    """A historical duplicate must not fail today's clean batch forever."""
    db = tmp_path / "u.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (id INTEGER, pb TEXT)")
    con.executemany(
        "INSERT INTO t VALUES (?, ?)",
        [(1, "OLD"), (1, "OLD"), (10, "B1"), (11, "B1")],  # dup in history only
    )
    con.commit()
    con.close()
    source = _SqliteSource({"name": "s", "path": str(db)})

    suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s", "asset": {"name": "t", "table_name": "t", "batch_key": "pb"}},
            "expectations": [{"type": "expect_column_values_to_be_unique", "column": "id"}],
        }
    )
    assert GEValidationFramework(source).run(suite).success is False, "unscoped sees the old dup"
    scoped = scope_suite_to_batch(suite, "B1")
    assert GEValidationFramework(source).run(scoped).success is True, "today's batch is clean"


# --------------------------------------------------------------------------
# Through the pipeline
# --------------------------------------------------------------------------


def test_pipeline_scopes_the_gate(tmp_path, history):
    suite_path = tmp_path / "raw.yml"
    suite_path.write_text(
        yaml.safe_dump(
            {
                "suite": {
                    "name": "raw",
                    "asset": {"type": "table", "name": "req", "table_name": "req", "batch_key": "pb"},
                },
                "expectations": [
                    {"type": "expect_column_values_to_not_be_null", "column": "v", "mostly": 0.9}
                ],
            }
        )
    )
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "req", "batch_key": "pb"},
                "validate": {"raw": str(suite_path)},
            }
        }
    )
    ctx = RunContext(pipeline="p", batch_id="B1", output_root=tmp_path / "out")
    result = Pipeline(
        cfg, resolve_source=lambda n: history, state=FileState(tmp_path / "st"), context=ctx
    ).run()

    assert result.errors == []
    outcome = result.validations[0]
    assert outcome.meta.get("batch_scoped") is True
    assert outcome.meta.get("batch_id") == "B1"
    assert outcome.success is False, "the dirty batch is caught once scoped"

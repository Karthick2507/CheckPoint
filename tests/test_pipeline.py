"""End-to-end pipeline tests against sqlite sources.

Exercises the full spine (extract -> gate:raw -> transform -> gate:curated ->
load -> gate:post) including cross-"source" loading (source and target are
distinct sqlite DataSources), all warn-and-continue.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.extract import Extractor
from core.load import Loader
from core.pipeline import Pipeline, build_check
from core.pipeline_config import PipelineConfig
from core.transform import Transformer
from data_sources.base import DataSource
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


def _make_db(path, ddl, insert_sql=None, rows=None):
    con = sqlite3.connect(path)
    con.execute(ddl)
    if insert_sql and rows:
        con.executemany(insert_sql, rows)
    con.commit()
    con.close()


# --------------------------------------------------------------------------
# Extractor
# --------------------------------------------------------------------------


def test_extractor_incremental_sql():
    ext = Extractor()
    sql = ext.build_table_sql("request", batch_key="pb", batch_id="20260101", incremental=True, limit=10)
    assert sql == "SELECT * FROM request WHERE pb = '20260101' LIMIT 10"


def test_extractor_incremental_requires_batch_key():
    with pytest.raises(ValueError, match="batch_key"):
        Extractor().build_table_sql("t", incremental=True)


def test_extractor_reads_rows(tmp_path):
    db = tmp_path / "s.db"
    _make_db(db, "CREATE TABLE t (a INTEGER)", "INSERT INTO t VALUES (?)", [(1,), (2,)])
    src = _SqliteSource({"name": "s", "path": str(db)})
    result = Extractor().extract(src, table="t")
    assert result.row_count == 2


# --------------------------------------------------------------------------
# Transformer & Loader
# --------------------------------------------------------------------------


def test_transformer_returns_last_select(tmp_path):
    db = tmp_path / "s.db"
    _make_db(db, "CREATE TABLE t (a INTEGER)", "INSERT INTO t VALUES (?)", [(1,), (2,), (3,)])
    src = _SqliteSource({"name": "s", "path": str(db)})
    result = Transformer().apply(src, ["SELECT a FROM t WHERE a > 1"])
    assert result.applied is True
    assert result.row_count == 2


def test_loader_append_and_overwrite(tmp_path):
    db = tmp_path / "t.db"
    _make_db(db, "CREATE TABLE dst (a INTEGER, b TEXT)")
    tgt = _SqliteSource({"name": "t", "path": str(db)})
    loader = Loader()
    loader.load(tgt, "dst", [{"a": 1, "b": "x"}, {"a": 2, "b": "y'z"}], mode="append")
    assert tgt.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 2
    # overwrite replaces
    loader.load(tgt, "dst", [{"a": 9, "b": "z"}], mode="overwrite")
    rows = tgt.execute("SELECT a FROM dst")
    assert [r["a"] for r in rows] == [9]


def test_loader_merge_upsert(tmp_path):
    db = tmp_path / "t.db"
    _make_db(db, "CREATE TABLE dst (id INTEGER, v TEXT)", "INSERT INTO dst VALUES (?, ?)", [(1, "old"), (2, "keep")])
    tgt = _SqliteSource({"name": "t", "path": str(db)})
    Loader().load(tgt, "dst", [{"id": 1, "v": "new"}, {"id": 3, "v": "add"}], mode="merge", keys=["id"])
    rows = {r["id"]: r["v"] for r in tgt.execute("SELECT id, v FROM dst")}
    assert rows == {1: "new", 2: "keep", 3: "add"}


# --------------------------------------------------------------------------
# build_check
# --------------------------------------------------------------------------


def test_build_check_from_spec():
    check = build_check({"type": "freshness", "timestamp_column": "ts", "max_lag_hours": 6}, "events")
    assert check.target == "events"
    assert check.timestamp_column == "ts"


def test_build_check_unknown_type():
    with pytest.raises(ValueError, match="Unknown quality check"):
        build_check({"type": "nonsense"}, "t")


# --------------------------------------------------------------------------
# Pipeline config parsing
# --------------------------------------------------------------------------


def test_pipeline_config_parsing():
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "request", "batch_key": "pb"},
                "extract": {"mode": "incremental", "limit": 100},
                "transform": ["SELECT * FROM request"],
                "target": {"connection": "tgt", "table": "clean", "mode": "merge", "keys": ["id"]},
                "validate": {"raw": "r.yml", "post": "p.yml"},
                "checks": [{"type": "volume_drift"}],
            }
        }
    )
    assert cfg.name == "p"
    assert cfg.extract.incremental is True
    assert cfg.target.mode == "merge"
    assert cfg.suite_raw == "r.yml"
    assert cfg.checks[0]["type"] == "volume_drift"


def test_pipeline_config_requires_source():
    with pytest.raises(ValueError, match="source"):
        PipelineConfig.from_dict({"pipeline": {"name": "p"}})


# --------------------------------------------------------------------------
# Full pipeline end-to-end (cross-source)
# --------------------------------------------------------------------------


@pytest.fixture()
def sources(tmp_path):
    src_db = tmp_path / "src.db"
    _make_db(
        src_db,
        "CREATE TABLE request (transaction_id TEXT, duration INTEGER)",
        "INSERT INTO request VALUES (?, ?)",
        [("t1", 10), ("t2", 20), ("t3", 30)],
    )
    tgt_db = tmp_path / "tgt.db"
    _make_db(tgt_db, "CREATE TABLE request_clean (transaction_id TEXT, duration INTEGER)")

    src = _SqliteSource({"name": "src", "path": str(src_db)})
    tgt = _SqliteSource({"name": "tgt", "path": str(tgt_db)})
    return {"src": src, "tgt": tgt}


def _suite(tmp_path, name, asset_table, expectations):
    import yaml

    path = tmp_path / f"{name}.yml"
    path.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": name, "asset": {"type": "table", "name": asset_table, "table_name": asset_table}},
                "expectations": expectations,
            }
        )
    )
    return str(path)


def test_full_pipeline_cross_source(tmp_path, sources):
    raw = _suite(
        tmp_path,
        "raw",
        "request",
        [{"type": "expect_column_values_to_not_be_null", "column": "transaction_id", "severity": "critical"}],
    )
    post = _suite(
        tmp_path,
        "post",
        "request_clean",
        [{"type": "expect_table_row_count_to_be_between", "min_value": 1}],
    )
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "request_daily",
                "source": {"connection": "src", "table": "request"},
                "transform": ["SELECT transaction_id, duration FROM request WHERE duration >= 20"],
                "target": {"connection": "tgt", "table": "request_clean", "mode": "append"},
                "validate": {"raw": raw, "post": post},
                "checks": [{"type": "volume_drift", "target": "request"}],
            }
        }
    )
    ctx = RunContext(pipeline="request_daily", output_root=tmp_path / "out")
    pipeline = Pipeline(cfg, resolve_source=lambda name: sources[name], state=FileState(tmp_path / "state"), context=ctx)
    result = pipeline.run()

    # transform kept only duration >= 20 -> 2 rows loaded into the target
    assert result.transform_rows == 2
    assert result.load.inserted == 2
    assert sources["tgt"].execute("SELECT COUNT(*) AS n FROM request_clean")[0]["n"] == 2

    # both validation gates ran (raw + post) and both passed
    assert len(result.validations) == 2
    assert result.passed is True
    assert result.has_critical_failure is False

    # volume check ran and established a baseline
    assert len(result.checks) == 1
    assert result.checks[0].check == "volume_drift"


def test_pipeline_warn_and_continue_does_not_raise(tmp_path, sources):
    # a raw suite that WILL fail (critical), pipeline must still complete + load
    raw = _suite(
        tmp_path,
        "raw",
        "request",
        [{"type": "expect_column_values_to_be_between", "column": "duration", "min_value": 0, "max_value": 5,
          "severity": "critical"}],
    )
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "request"},
                "target": {"connection": "tgt", "table": "request_clean", "mode": "append"},
                "validate": {"raw": raw},
            }
        }
    )
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out")
    result = Pipeline(cfg, resolve_source=lambda name: sources[name], state=FileState(tmp_path / "st"), context=ctx).run()

    # failed critically but did NOT raise and STILL loaded (warn-and-continue)
    assert result.has_critical_failure is True
    assert result.passed is False
    assert result.load.inserted == 3

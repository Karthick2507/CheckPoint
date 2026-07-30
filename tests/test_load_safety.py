"""Safety tests for the load stage (P0 hardening).

Covers the destructive-load guards: an empty payload must never be allowed to
delete a target table by accident.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.load import Loader
from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from data_sources.base import DataSource
from reporting import collect_warnings
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


@pytest.fixture()
def target(tmp_path):
    db = tmp_path / "t.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO dst VALUES (?, ?)", [(1, "a"), (2, "b"), (3, "c")])
    con.commit()
    con.close()
    return _SqliteSource({"name": "tgt", "path": str(db)})


def _count(source, table="dst") -> int:
    return source.execute(f"SELECT COUNT(*) AS n FROM {table}")[0]["n"]


# --------------------------------------------------------------------------
# The core guard
# --------------------------------------------------------------------------


def test_overwrite_with_empty_payload_does_not_wipe_target(target):
    result = Loader().load(target, "dst", [], mode="overwrite")
    assert _count(target) == 3, "empty overwrite must not delete existing rows"
    assert result.skipped is True
    assert result.inserted == 0
    assert "refused" in result.reason


def test_merge_with_empty_payload_does_not_delete(target):
    result = Loader().load(target, "dst", [], mode="merge", keys=["id"])
    assert _count(target) == 3
    assert result.skipped is True
    assert "refused" in result.reason


def test_allow_empty_opts_into_truncate(target):
    result = Loader().load(target, "dst", [], mode="overwrite", allow_empty=True)
    assert _count(target) == 0, "explicit allow_empty should truncate"
    assert result.skipped is False


def test_append_with_empty_payload_is_a_noop(target):
    result = Loader().load(target, "dst", [], mode="append")
    assert _count(target) == 3
    assert result.inserted == 0
    assert result.skipped is False  # append is not destructive


def test_overwrite_with_rows_still_replaces(target):
    result = Loader().load(target, "dst", [{"id": 9, "v": "z"}], mode="overwrite")
    assert _count(target) == 1
    assert result.inserted == 1
    assert result.skipped is False


def test_mode_none_is_skipped(target):
    result = Loader().load(target, "dst", [{"id": 9, "v": "z"}], mode="none")
    assert _count(target) == 3
    assert result.skipped is True


# --------------------------------------------------------------------------
# Wired through the pipeline + surfaced in reporting
# --------------------------------------------------------------------------


def _pipeline(tmp_path, sources, target_cfg):
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                # transform filters everything out -> empty payload
                "source": {"connection": "src", "table": "src_t"},
                "transform": ["SELECT id, v FROM src_t WHERE 1 = 0"],
                "target": target_cfg,
            }
        }
    )
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out")
    return Pipeline(cfg, resolve_source=lambda n: sources[n], state=FileState(tmp_path / "st"), context=ctx).run()


@pytest.fixture()
def sources(tmp_path, target):
    src_db = tmp_path / "s.db"
    con = sqlite3.connect(src_db)
    con.execute("CREATE TABLE src_t (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO src_t VALUES (?, ?)", [(1, "x")])
    con.commit()
    con.close()
    return {"src": _SqliteSource({"name": "src", "path": str(src_db)}), "tgt": target}


def test_pipeline_refuses_empty_overwrite(tmp_path, sources, target):
    result = _pipeline(tmp_path, sources, {"connection": "tgt", "table": "dst", "mode": "overwrite"})
    assert _count(target) == 3, "pipeline must not wipe the target on an empty transform"
    assert result.load.skipped is True


def test_pipeline_allow_empty_truncates(tmp_path, sources, target):
    result = _pipeline(
        tmp_path, sources, {"connection": "tgt", "table": "dst", "mode": "overwrite", "allow_empty": True}
    )
    assert _count(target) == 0
    assert result.load.skipped is False


def test_skipped_destructive_load_appears_in_warnings(tmp_path, sources):
    result = _pipeline(tmp_path, sources, {"connection": "tgt", "table": "dst", "mode": "overwrite"})
    warnings = collect_warnings(result)
    subjects = {w.subject for w in warnings}
    assert "overwrite_skipped" in subjects
    row = next(w for w in warnings if w.subject == "overwrite_skipped")
    assert row.severity == "critical", "a refused destructive load must be loud"

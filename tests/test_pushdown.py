"""Pushdown execution tests (P1).

The row-based loader reads every row into Python and writes it back as
``INSERT … VALUES`` — unusable at TiB scale. Pushdown keeps the data in the
warehouse (``INSERT … SELECT``), so cost is independent of row count.

These tests assert both the generated SQL *and* that no rows are materialized.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.load import PushdownLoader
from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from data_sources.base import DataSource
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


class _CountingSource(_SqliteSource):
    """Records every statement so we can prove what was (not) executed."""

    type = "counting"

    def __init__(self, config):
        super().__init__(config)
        self.executed: list[str] = []

    def execute(self, sql: str):
        self.executed.append(sql)
        return super().execute(sql)


@pytest.fixture()
def warehouse(tmp_path):
    """One database holding both the source and the target table."""
    db = tmp_path / "w.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE src (id INTEGER, pb TEXT, v TEXT)")
    con.execute("CREATE TABLE dst (id INTEGER, pb TEXT, v TEXT)")
    con.executemany(
        "INSERT INTO src VALUES (?, ?, ?)",
        [(1, "B1", "a"), (2, "B1", "b"), (3, "B2", "c")],
    )
    con.commit()
    con.close()
    return _CountingSource({"name": "wh", "path": str(db)})


def _rows(source, table):
    return source.execute(f"SELECT id, v FROM {table} ORDER BY id")


# --------------------------------------------------------------------------
# Statement construction
# --------------------------------------------------------------------------


def test_append_builds_insert_select():
    stmts = PushdownLoader().build_statements("dst", "SELECT * FROM src", mode="append")
    assert stmts == ["INSERT INTO dst SELECT * FROM src"]


def test_overwrite_prepends_delete():
    stmts = PushdownLoader().build_statements("dst", "SELECT * FROM src", mode="overwrite")
    assert stmts[0] == "DELETE FROM dst"
    assert stmts[1].startswith("INSERT INTO dst ")


def test_merge_deletes_incoming_keys_in_warehouse():
    stmts = PushdownLoader().build_statements("dst", "SELECT * FROM src", mode="merge", keys=["id"])
    assert "DELETE FROM dst WHERE (id) IN (SELECT id FROM (SELECT * FROM src) AS _incoming)" == stmts[0]


def test_merge_requires_keys():
    with pytest.raises(ValueError, match="requires 'keys'"):
        PushdownLoader().build_statements("dst", "SELECT 1", mode="merge")


def test_column_list_is_emitted():
    stmts = PushdownLoader().build_statements("dst", "SELECT a, b FROM s", columns=["a", "b"])
    assert stmts[0] == "INSERT INTO dst (a, b) SELECT a, b FROM s"


def test_trailing_semicolon_stripped():
    stmts = PushdownLoader().build_statements("dst", "SELECT * FROM src;", mode="append")
    assert ";" not in stmts[0]


def test_unsupported_mode_rejected():
    with pytest.raises(ValueError, match="Unsupported pushdown load mode"):
        PushdownLoader().build_statements("dst", "SELECT 1", mode="upsert")


# --------------------------------------------------------------------------
# Execution against a real warehouse
# --------------------------------------------------------------------------


def test_pushdown_append_moves_data_without_materializing(warehouse):
    result = PushdownLoader().load(warehouse, "dst", "SELECT * FROM src WHERE pb = 'B1'", mode="append")
    assert result.inserted == 2
    assert [r["id"] for r in _rows(warehouse, "dst")] == [1, 2]

    # No statement ever selected the payload rows back to Python: the only
    # SELECT issued is the COUNT, plus the INSERT … SELECT.
    selects = [s for s in warehouse.executed if s.strip().upper().startswith("SELECT")]
    assert all("COUNT(*)" in s or "id, v" in s for s in selects), selects


def test_pushdown_overwrite_replaces(warehouse):
    warehouse.execute("INSERT INTO dst VALUES (99, 'old', 'z')")
    PushdownLoader().load(warehouse, "dst", "SELECT * FROM src WHERE pb = 'B1'", mode="overwrite")
    assert [r["id"] for r in _rows(warehouse, "dst")] == [1, 2]


def test_pushdown_merge_upserts(warehouse):
    warehouse.execute("INSERT INTO dst VALUES (1, 'B1', 'stale')")
    warehouse.execute("INSERT INTO dst VALUES (9, 'B9', 'keep')")
    PushdownLoader().load(warehouse, "dst", "SELECT * FROM src WHERE pb = 'B1'", mode="merge", keys=["id"])
    rows = {r["id"]: r["v"] for r in _rows(warehouse, "dst")}
    assert rows == {1: "a", 2: "b", 9: "keep"}


def test_pushdown_empty_guard_refuses_destructive(warehouse):
    warehouse.execute("INSERT INTO dst VALUES (7, 'x', 'existing')")
    result = PushdownLoader().load(warehouse, "dst", "SELECT * FROM src WHERE pb = 'NONE'", mode="overwrite")
    assert result.skipped is True
    assert "refused" in result.reason
    assert len(_rows(warehouse, "dst")) == 1, "target must be untouched"


def test_pushdown_allow_empty_truncates(warehouse):
    warehouse.execute("INSERT INTO dst VALUES (7, 'x', 'existing')")
    result = PushdownLoader().load(
        warehouse, "dst", "SELECT * FROM src WHERE pb = 'NONE'", mode="overwrite", allow_empty=True
    )
    assert result.skipped is False
    assert _rows(warehouse, "dst") == []


def test_pushdown_rolls_back_on_failure(warehouse):
    """DELETE must not survive an INSERT that fails: same guarantee as P0-2."""
    warehouse.execute("INSERT INTO dst VALUES (7, 'x', 'existing')")
    before = _rows(warehouse, "dst")

    with pytest.raises(Exception):
        # The SELECT references a missing table, so the INSERT fails *after*
        # the DELETE has already run inside the transaction.
        PushdownLoader().load(
            warehouse, "dst", "SELECT id, pb, v FROM ghost_table", mode="overwrite", count_rows=False
        )

    assert _rows(warehouse, "dst") == before, "failed pushdown must not truncate the target"


def test_pushdown_mode_none_skips(warehouse):
    result = PushdownLoader().load(warehouse, "dst", "SELECT * FROM src", mode="none")
    assert result.skipped is True
    assert _rows(warehouse, "dst") == []


# --------------------------------------------------------------------------
# Mode selection
# --------------------------------------------------------------------------


def _pipeline(tmp_path, pipeline_dict, sources):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, batch_id="B1", output_root=tmp_path / "out")
    return Pipeline(cfg, resolve_source=lambda n: sources[n], state=FileState(tmp_path / "st"), context=ctx)


def test_auto_chooses_pushdown_for_same_connection(tmp_path, warehouse):
    p = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src"},
                "target": {"connection": "wh", "table": "dst"},
            }
        },
        {"wh": warehouse},
    )
    assert p.execution_mode() == "pushdown"


def test_auto_chooses_rows_for_cross_system(tmp_path, warehouse):
    p = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src"},
                "target": {"connection": "other", "table": "dst"},
            }
        },
        {"wh": warehouse},
    )
    assert p.execution_mode() == "rows"


def test_auto_chooses_rows_when_no_target(tmp_path, warehouse):
    p = _pipeline(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "wh", "table": "src"}}},
        {"wh": warehouse},
    )
    assert p.execution_mode() == "rows"


def test_explicit_mode_overrides(tmp_path, warehouse):
    p = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "execution": "rows",
                "source": {"connection": "wh", "table": "src"},
                "target": {"connection": "wh", "table": "dst"},
            }
        },
        {"wh": warehouse},
    )
    assert p.execution_mode() == "rows"


def test_invalid_execution_mode_rejected():
    with pytest.raises(ValueError, match="Invalid execution mode"):
        PipelineConfig.from_dict(
            {"pipeline": {"name": "p", "execution": "magic", "source": {"connection": "s", "table": "t"}}}
        )


# --------------------------------------------------------------------------
# Full pipeline in pushdown mode
# --------------------------------------------------------------------------


def test_pipeline_pushdown_end_to_end(tmp_path, warehouse):
    pipeline = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src", "batch_key": "pb"},
                "extract": {"mode": "incremental"},
                "transform": ["SELECT id, pb, v FROM src WHERE pb = '{{ batch_id }}'"],
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
        {"wh": warehouse},
    )
    result = pipeline.run()

    assert result.errors == []
    assert result.execution == "pushdown"
    assert result.extract_rows == 0, "pushdown must not materialize rows"
    assert [r["id"] for r in _rows(warehouse, "dst")] == [1, 2], "only the batch landed"
    assert result.load.inserted == 2

    # The framework never issued a bare 'SELECT * FROM src' to pull the payload.
    assert not any(s.strip() == "SELECT * FROM src" for s in warehouse.executed)


def test_pipeline_pushdown_without_transform_uses_source_select(tmp_path, warehouse):
    pipeline = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src", "batch_key": "pb"},
                "extract": {"mode": "incremental"},
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
        {"wh": warehouse},
    )
    result = pipeline.run()
    assert result.errors == []
    assert [r["id"] for r in _rows(warehouse, "dst")] == [1, 2]


def test_pipeline_rows_mode_still_works(tmp_path, warehouse):
    """Cross-system behaviour must be unchanged."""
    pipeline = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "execution": "rows",
                "source": {"connection": "wh", "table": "src"},
                "transform": ["SELECT id, pb, v FROM src WHERE pb = 'B1'"],
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
        {"wh": warehouse},
    )
    result = pipeline.run()
    assert result.execution == "rows"
    assert result.extract_rows == 3, "rows mode does materialize"
    assert result.load.inserted == 2


def test_execution_mode_in_manifest(tmp_path, warehouse):
    pipeline = _pipeline(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src"},
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
        {"wh": warehouse},
    )
    result = pipeline.run()
    assert result.to_dict()["execution"] == "pushdown"

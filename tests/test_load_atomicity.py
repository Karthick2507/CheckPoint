"""Atomicity tests for the load stage (P0 hardening).

A destructive load deletes before it inserts. If the insert fails, the delete
must be rolled back — otherwise rows are lost permanently.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.load import Loader
from data_sources.base import Capabilities, DataSource
from reporting import collect_warnings
from core.pipeline import PipelineResult
from runtime.run_context import RunContext


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


class _NonTransactionalSource(_SqliteSource):
    """Mimics Trino/Presto: cannot roll back."""

    type = "no_tx"

    def capabilities(self) -> Capabilities:
        return Capabilities(dialect="no_tx", supports_transactions=False)


@pytest.fixture()
def target(tmp_path):
    db = tmp_path / "t.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO dst VALUES (?, ?)", [(1, "old"), (2, "keep")])
    con.commit()
    con.close()
    return _SqliteSource({"name": "tgt", "path": str(db)})


def _rows(source):
    return {r["id"]: r["v"] for r in source.execute("SELECT id, v FROM dst")}


# --------------------------------------------------------------------------
# Rollback behaviour
# --------------------------------------------------------------------------


def test_failed_merge_rolls_back_the_delete(target):
    """The bug: id=1 was deleted, the insert failed, the row was gone forever."""
    before = _rows(target)
    assert before == {1: "old", 2: "keep"}

    with pytest.raises(Exception):
        # unknown column makes the INSERT fail after the DELETE has run
        Loader().load(
            target, "dst", [{"id": 1, "v": "new", "nope": "boom"}], mode="merge", keys=["id"]
        )

    assert _rows(target) == before, "failed merge must not lose the deleted row"


def test_failed_overwrite_rolls_back_the_delete(target):
    before = _rows(target)
    with pytest.raises(Exception):
        Loader().load(target, "dst", [{"id": 9, "v": "z", "nope": "boom"}], mode="overwrite")
    assert _rows(target) == before, "failed overwrite must not truncate the table"


def test_successful_merge_still_commits(target):
    Loader().load(target, "dst", [{"id": 1, "v": "new"}, {"id": 3, "v": "add"}], mode="merge", keys=["id"])
    assert _rows(target) == {1: "new", 2: "keep", 3: "add"}


def test_successful_overwrite_still_commits(target):
    Loader().load(target, "dst", [{"id": 7, "v": "only"}], mode="overwrite")
    assert _rows(target) == {7: "only"}


def test_append_commits(target):
    Loader().load(target, "dst", [{"id": 5, "v": "e"}], mode="append")
    assert _rows(target)[5] == "e"


# --------------------------------------------------------------------------
# Transaction primitive
# --------------------------------------------------------------------------


def test_transaction_commits_all_statements(target):
    with target.transaction() as tx:
        tx.execute("INSERT INTO dst VALUES (10, 'a')")
        tx.execute("INSERT INTO dst VALUES (11, 'b')")
    assert {10, 11}.issubset(set(_rows(target)))


def test_transaction_rolls_back_on_error(target):
    before = _rows(target)
    with pytest.raises(Exception):
        with target.transaction() as tx:
            tx.execute("INSERT INTO dst VALUES (10, 'a')")
            tx.execute("INSERT INTO nonexistent_table VALUES (1)")
    assert _rows(target) == before, "no statement in a failed transaction may persist"


def test_transaction_can_read(target):
    with target.transaction() as tx:
        rows = tx.execute("SELECT COUNT(*) AS n FROM dst")
    assert rows[0]["n"] == 2


# --------------------------------------------------------------------------
# Honest capability reporting
# --------------------------------------------------------------------------


def test_atomic_flag_true_for_transactional_target(target):
    result = Loader().load(target, "dst", [{"id": 1, "v": "x"}], mode="merge", keys=["id"])
    assert result.atomic is True
    assert result.reason == ""


def test_atomic_flag_false_for_non_transactional_target(tmp_path):
    db = tmp_path / "n.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.commit()
    con.close()
    source = _NonTransactionalSource({"name": "notx", "path": str(db)})
    result = Loader().load(source, "dst", [{"id": 1, "v": "x"}], mode="overwrite")
    assert result.atomic is False
    assert "not atomic" in result.reason


def test_presto_declares_no_transactions():
    from data_sources.presto import PrestoDataSource

    caps = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s"}).capabilities()
    assert caps.supports_transactions is False


def test_non_atomic_load_surfaces_in_warnings(tmp_path):
    db = tmp_path / "n.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER)")
    con.commit()
    con.close()
    source = _NonTransactionalSource({"name": "notx", "path": str(db)})
    load = Loader().load(source, "dst", [{"id": 1}], mode="overwrite")

    ctx = RunContext(pipeline="p", output_root=tmp_path / "out")
    result = PipelineResult(pipeline="p", run_id=ctx.run_id, context=ctx, load=load)
    subjects = {w.subject for w in collect_warnings(result)}
    assert "non_atomic_load" in subjects


# --------------------------------------------------------------------------
# Commit failures must not be swallowed
# --------------------------------------------------------------------------


def test_write_commit_failure_raises(tmp_path, monkeypatch):
    db = tmp_path / "c.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (a INTEGER)")
    con.commit()
    con.close()
    source = _SqliteSource({"name": "s", "path": str(db)})

    real_raw = source.get_engine().raw_connection

    class _BadCommit:
        def __init__(self, inner):
            self._inner = inner

        def __getattr__(self, item):
            return getattr(self._inner, item)

        def commit(self):
            raise RuntimeError("commit refused")

    monkeypatch.setattr(source.get_engine(), "raw_connection", lambda: _BadCommit(real_raw()))

    with pytest.raises(RuntimeError, match="commit refused"):
        source.execute("INSERT INTO t VALUES (1)")

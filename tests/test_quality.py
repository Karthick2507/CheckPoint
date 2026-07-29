"""Tests for the custom quality checks (freshness, volume, schema, referential)."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta

import pytest

from data_sources.base import DataSource
from quality import (
    FreshnessCheck,
    ReferentialIntegrityCheck,
    SchemaDriftCheck,
    VolumeDriftCheck,
)
from quality.base import normalize_columns
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


@pytest.fixture()
def source(tmp_path):
    db = tmp_path / "d.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE events (id INTEGER, ts TEXT, parent_id INTEGER)")
    con.execute("CREATE TABLE parents (pid INTEGER)")
    con.commit()
    con.close()
    return _SqliteSource({"name": "local", "path": str(db)})


def _insert(source, sql, rows):
    engine = source.get_engine()
    raw = engine.raw_connection()
    try:
        cur = raw.cursor()
        cur.executemany(sql, rows)
        raw.commit()
    finally:
        raw.close()


# --------------------------------------------------------------------------
# normalize_columns
# --------------------------------------------------------------------------


def test_normalize_columns_presto_and_sqlite():
    presto = normalize_columns([{"Column": "a", "Type": "varchar"}, {"Column": "b", "Type": "bigint"}])
    assert presto == [{"name": "a", "type": "varchar"}, {"name": "b", "type": "bigint"}]
    pragma = normalize_columns([{"cid": 0, "name": "a", "type": "INTEGER"}])
    assert pragma == [{"name": "a", "type": "INTEGER"}]


# --------------------------------------------------------------------------
# Freshness
# --------------------------------------------------------------------------


def test_freshness_pass(source):
    now = datetime(2026, 7, 29, 12, 0, 0)
    recent = (now - timedelta(hours=2)).isoformat()
    _insert(source, "INSERT INTO events (id, ts) VALUES (?, ?)", [(1, recent)])
    check = FreshnessCheck("events", timestamp_column="ts", max_lag_hours=6)
    result = check.run(source, now=now)
    assert result.success is True
    assert result.observed == pytest.approx(2.0, abs=0.01)


def test_freshness_fail_when_stale(source):
    now = datetime(2026, 7, 29, 12, 0, 0)
    old = (now - timedelta(hours=48)).isoformat()
    _insert(source, "INSERT INTO events (id, ts) VALUES (?, ?)", [(1, old)])
    result = FreshnessCheck("events", "ts", max_lag_hours=6).run(source, now=now)
    assert result.success is False


def test_freshness_fail_when_empty(source):
    result = FreshnessCheck("events", "ts", max_lag_hours=6).run(source, now=datetime.now())
    assert result.success is False
    assert "empty" in result.details.lower() or "no usable" in result.details.lower()


# --------------------------------------------------------------------------
# Volume drift
# --------------------------------------------------------------------------


def test_volume_first_run_establishes_baseline(source, tmp_path):
    state = FileState(tmp_path / "state")
    _insert(source, "INSERT INTO events (id) VALUES (?)", [(i,) for i in range(100)])
    result = VolumeDriftCheck("events").run(source, state=state)
    assert result.success is True
    assert result.observed == 100
    # history now has one entry
    assert state.baseline_row_count("local", "events") == 100.0


def test_volume_drift_detected(source, tmp_path):
    state = FileState(tmp_path / "state")
    # seed baseline history at ~100
    for _ in range(3):
        state.append_row_count("local", "events", 100)
    _insert(source, "INSERT INTO events (id) VALUES (?)", [(i,) for i in range(200)])
    result = VolumeDriftCheck("events", tolerance=0.25).run(source, state=state)
    assert result.success is False
    assert result.observed == 200
    assert result.metadata["deviation"] == pytest.approx(1.0, abs=0.01)


def test_volume_within_tolerance(source, tmp_path):
    state = FileState(tmp_path / "state")
    for _ in range(3):
        state.append_row_count("local", "events", 100)
    _insert(source, "INSERT INTO events (id) VALUES (?)", [(i,) for i in range(110)])
    result = VolumeDriftCheck("events", tolerance=0.25).run(source, state=state)
    assert result.success is True


# --------------------------------------------------------------------------
# Schema drift
# --------------------------------------------------------------------------


def test_schema_first_run_establishes_baseline(source, tmp_path):
    state = FileState(tmp_path / "state")
    result = SchemaDriftCheck("events").run(source, state=state)
    assert result.success is True
    assert state.load_schema_snapshot("local", "events") is not None


def test_schema_drift_detects_added_column(source, tmp_path):
    state = FileState(tmp_path / "state")
    SchemaDriftCheck("events").run(source, state=state)  # baseline (id, ts, parent_id)
    source.execute("ALTER TABLE events ADD COLUMN extra TEXT")
    source.dispose()
    result = SchemaDriftCheck("events").run(source, state=state)
    assert result.success is False
    assert "extra" in result.metadata["added"]


# --------------------------------------------------------------------------
# Referential integrity
# --------------------------------------------------------------------------


def test_referential_pass(source):
    _insert(source, "INSERT INTO parents (pid) VALUES (?)", [(1,), (2,)])
    _insert(source, "INSERT INTO events (id, parent_id) VALUES (?, ?)", [(1, 1), (2, 2)])
    result = ReferentialIntegrityCheck("events", "parent_id", "parents", "pid").run(source)
    assert result.success is True
    assert result.observed == 0


def test_referential_detects_orphans(source):
    _insert(source, "INSERT INTO parents (pid) VALUES (?)", [(1,)])
    _insert(source, "INSERT INTO events (id, parent_id) VALUES (?, ?)", [(1, 1), (2, 99)])
    result = ReferentialIntegrityCheck("events", "parent_id", "parents", "pid").run(source)
    assert result.success is False
    assert result.observed == 1

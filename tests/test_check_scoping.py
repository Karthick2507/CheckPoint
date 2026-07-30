"""Batch scoping for freshness and referential-integrity checks (P3).

Volume-drift got batch scoping in P2; these two had the same blindness:

* **Freshness** takes ``MAX(ts)`` over the whole table, so a month-old batch
  hides behind any fresher historical row and the check reports healthy.
* **Referential integrity** re-scans all history every run, and one historical
  orphan fails the check forever no matter how clean today's batch is.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta

import pytest

from data_sources.base import DataSource
from quality import FreshnessCheck, ReferentialIntegrityCheck, SchemaDriftCheck, VolumeDriftCheck
from runtime.state import FileState

NOW = datetime(2026, 7, 30, 12, 0, 0)


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


@pytest.fixture()
def warehouse(tmp_path):
    """Healthy history, plus a current batch that is stale and has an orphan."""
    db = tmp_path / "w.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE ev (id INTEGER, pb TEXT, ts TEXT, parent INTEGER)")
    con.execute("CREATE TABLE par (pid INTEGER)")
    con.executemany("INSERT INTO par VALUES (?)", [(1,), (2,)])
    con.executemany(
        "INSERT INTO ev VALUES (?, ?, ?, ?)",
        [
            # history: fresh and referentially clean
            (1, "OLD", (NOW - timedelta(hours=1)).isoformat(), 1),
            (2, "OLD", (NOW - timedelta(hours=2)).isoformat(), 2),
            # today's batch: a month stale, and pointing at a missing parent
            (3, "B4", (NOW - timedelta(days=30)).isoformat(), 999),
        ],
    )
    con.commit()
    con.close()
    return _SqliteSource({"name": "s", "path": str(db)})


# --------------------------------------------------------------------------
# Freshness
# --------------------------------------------------------------------------


def test_unscoped_freshness_hides_a_stale_batch(warehouse):
    """MAX(ts) over the whole table finds the fresh historical row and PASSES."""
    result = FreshnessCheck("ev", "ts", max_lag_hours=6).run(warehouse, now=NOW)
    assert result.success is True, "this is the false negative scoping fixes"
    assert "WHOLE TABLE" in result.details


def test_scoped_freshness_catches_a_stale_batch(warehouse):
    """Scoped to B4, the newest row really is 30 days old, so it FAILS."""
    check = FreshnessCheck("ev", "ts", max_lag_hours=6, batch_key="pb")
    result = check.run(warehouse, now=NOW, batch_id="B4")
    assert result.success is False
    assert result.observed == pytest.approx(720, abs=1)  # 30 days in hours
    assert result.metadata["scoped"] is True


def test_scoped_freshness_passes_for_a_fresh_batch(warehouse):
    check = FreshnessCheck("ev", "ts", max_lag_hours=6, batch_key="pb")
    assert check.run(warehouse, now=NOW, batch_id="OLD").success is True


def test_freshness_missing_batch_fails(warehouse):
    """A batch that never landed has no rows, hence no timestamp."""
    check = FreshnessCheck("ev", "ts", max_lag_hours=6, batch_key="pb")
    result = check.run(warehouse, now=NOW, batch_id="NEVER_LANDED")
    assert result.success is False
    assert "no rows for this scope" in result.details


def test_freshness_sql_scoping():
    assert FreshnessCheck("ev", "ts", 6).max_timestamp_sql("B1") == (
        "SELECT MAX(ts) AS max_ts FROM ev"
    )
    assert FreshnessCheck("ev", "ts", 6, batch_key="pb").max_timestamp_sql("B1") == (
        "SELECT MAX(ts) AS max_ts FROM ev WHERE pb = 'B1'"
    )


def test_freshness_batch_filter_is_templated():
    check = FreshnessCheck("ev", "ts", 6, batch_filter="pb >= '{{ batch_id }}'")
    sql = check.max_timestamp_sql("B1", {"batch_id": "B1"})
    assert sql.endswith("WHERE pb >= 'B1'")


# --------------------------------------------------------------------------
# Referential integrity
# --------------------------------------------------------------------------


def test_unscoped_referential_fails_forever_on_a_historical_orphan(tmp_path):
    """One old orphan condemns every future run, however clean the new batch."""
    db = tmp_path / "r.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE ev (id INTEGER, pb TEXT, parent INTEGER)")
    con.execute("CREATE TABLE par (pid INTEGER)")
    con.executemany("INSERT INTO par VALUES (?)", [(1,)])
    con.executemany(
        "INSERT INTO ev VALUES (?, ?, ?)",
        [(1, "OLD", 999), (2, "B4", 1)],  # historical orphan; today is clean
    )
    con.commit()
    con.close()
    source = _SqliteSource({"name": "s", "path": str(db)})

    unscoped = ReferentialIntegrityCheck("ev", "parent", "par", "pid")
    assert unscoped.run(source).success is False, "the old orphan still fails it"

    scoped = ReferentialIntegrityCheck("ev", "parent", "par", "pid", batch_key="pb")
    assert scoped.run(source, batch_id="B4").success is True, "today's batch is clean"


def test_scoped_referential_still_catches_a_new_orphan(warehouse):
    check = ReferentialIntegrityCheck("ev", "parent", "par", "pid", batch_key="pb")
    result = check.run(warehouse, batch_id="B4")
    assert result.success is False
    assert result.observed == 1
    assert result.metadata["scoped"] is True


def test_referential_scopes_only_the_child_side(warehouse):
    """Parents legitimately predate the batch, so they must not be filtered."""
    sql = ReferentialIntegrityCheck("ev", "parent", "par", "pid", batch_key="pb").orphans_sql("B4")
    assert "c.pb = 'B4'" in sql
    assert "p.pb" not in sql


def test_referential_unscoped_sql_unchanged():
    sql = ReferentialIntegrityCheck("ev", "parent", "par", "pid").orphans_sql()
    assert "WHERE p.pid IS NULL AND c.parent IS NOT NULL" in sql


# --------------------------------------------------------------------------
# Shared base behaviour
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "check",
    [
        FreshnessCheck("t", "ts", 6, batch_key="pb"),
        ReferentialIntegrityCheck("t", "c", "p", "k", batch_key="pb"),
        VolumeDriftCheck("t", batch_key="pb"),
    ],
)
def test_scoped_checks_report_scoping(check):
    assert check.is_batch_scoped is True
    assert check.batch_predicate("B1") == "pb = 'B1'"
    assert check.scope_note() == "batch-scoped"


@pytest.mark.parametrize(
    "check",
    [
        FreshnessCheck("t", "ts", 6),
        ReferentialIntegrityCheck("t", "c", "p", "k"),
        VolumeDriftCheck("t"),
    ],
)
def test_unscoped_checks_say_so(check):
    assert check.is_batch_scoped is False
    assert check.batch_predicate("B1") is None
    assert "WHOLE TABLE" in check.scope_note()


def test_alias_qualifies_the_predicate():
    check = ReferentialIntegrityCheck("t", "c", "p", "k", batch_key="pb")
    assert check.batch_predicate("B1", alias="c") == "c.pb = 'B1'"


# --------------------------------------------------------------------------
# Uniform call signature from the pipeline
# --------------------------------------------------------------------------


def test_all_checks_accept_batch_arguments(warehouse, tmp_path):
    """The pipeline calls every check the same way; none may reject the kwargs."""
    state = FileState(tmp_path / "st")
    common = {"state": state, "batch_id": "B4", "template_context": {"batch_id": "B4"}}
    FreshnessCheck("ev", "ts", 6, batch_key="pb").run(warehouse, **common)
    ReferentialIntegrityCheck("ev", "parent", "par", "pid", batch_key="pb").run(warehouse, **common)
    SchemaDriftCheck("ev").run(warehouse, **common)
    VolumeDriftCheck("ev", batch_key="pb").run(warehouse, run_id="r", **common)

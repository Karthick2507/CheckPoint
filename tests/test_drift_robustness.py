"""Robust, batch-scoped drift detection tests (P2).

Three defects, each demonstrated and then fixed:

1. counting the whole table hides a failed batch on an append-only warehouse;
2. a mean baseline is dragged by the very anomalies it should catch;
3. a bad run was written into the baseline, so an anomaly became the new normal.
"""

from __future__ import annotations

import sqlite3

import pytest

from data_sources.base import DataSource
from quality import VolumeDriftCheck
from quality.stats import mad, median_value, relative_deviation, robust_z_score
from runtime.sql import build_batch_predicate, sql_literal, where_clause
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


@pytest.fixture()
def append_only(tmp_path):
    """100k historical rows; each day appends a ~1000-row batch."""
    db = tmp_path / "a.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (id INTEGER, pb TEXT)")
    con.executemany("INSERT INTO t VALUES (?, ?)", [(i, "OLD") for i in range(100_000)])
    con.commit()
    con.close()
    return _SqliteSource({"name": "s", "path": str(db)})


def _add_batch(source, batch, n):
    with source.transaction() as tx:
        for i in range(n):
            tx.execute(f"INSERT INTO t VALUES ({i}, '{batch}')")


# --------------------------------------------------------------------------
# Defect 1: whole-table counting hides a failed batch
# --------------------------------------------------------------------------


def test_whole_table_count_hides_a_failed_batch(append_only, tmp_path):
    """Unscoped: an empty batch barely moves a 100k total, so it PASSES."""
    state = FileState(tmp_path / "s1")
    check = VolumeDriftCheck("t", tolerance=0.25, min_history=3)
    for day in range(1, 4):
        _add_batch(append_only, f"B{day}", 1000)
        check.run(append_only, state=state, batch_id=f"B{day}")

    result = check.run(append_only, state=state, batch_id="B4")  # zero new rows
    assert result.success is True, "this is the false negative that scoping fixes"
    assert "WHOLE TABLE" in result.details, "and the report says the scope is wrong"


def test_batch_scoped_count_catches_a_failed_batch(append_only, tmp_path):
    """Scoped: today's batch is 0 against a ~1000 median, so it FAILS."""
    state = FileState(tmp_path / "s2")
    check = VolumeDriftCheck("t", tolerance=0.25, min_history=3, batch_key="pb")
    for day in range(1, 4):
        _add_batch(append_only, f"B{day}", 1000)
        assert check.run(append_only, state=state, batch_id=f"B{day}").success is True

    result = check.run(append_only, state=state, batch_id="B4")  # batch never landed
    assert result.success is False, "the empty batch must be caught"
    assert result.observed == 0
    assert result.metadata["baseline_median"] == 1000


def test_scoped_and_unscoped_history_do_not_mix():
    scoped = VolumeDriftCheck("t", batch_key="pb")
    unscoped = VolumeDriftCheck("t")
    assert scoped.scope_key != unscoped.scope_key


def test_count_sql_scoping():
    assert VolumeDriftCheck("t").count_sql("B1") == "SELECT COUNT(*) AS n FROM t"
    assert (
        VolumeDriftCheck("t", batch_key="pb").count_sql("B1")
        == "SELECT COUNT(*) AS n FROM t WHERE pb = 'B1'"
    )


def test_count_sql_batch_filter_is_templated():
    check = VolumeDriftCheck("t", batch_filter="pb >= '{{ batch_id }}'")
    assert check.count_sql("B1", {"batch_id": "B1"}) == "SELECT COUNT(*) AS n FROM t WHERE pb >= 'B1'"


# --------------------------------------------------------------------------
# Defect 2: the mean is dragged by outliers
# --------------------------------------------------------------------------


def test_median_resists_an_outlier_that_the_mean_does_not():
    history = [1000, 1000, 1000, 1000, 50_000]  # one spike
    assert median_value(history) == 1000
    mean = sum(history) / len(history)
    assert mean > 10_000, "the mean is dragged far from typical"


def test_drift_uses_the_median_baseline(tmp_path):
    class _Fixed(_SqliteSource):
        def execute(self, sql):
            return [{"n": 1300}]

    source = _Fixed({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    for count in (1000, 1000, 1000, 1000, 50_000):  # includes a spike
        state.append_row_count("s", "t", count)

    result = VolumeDriftCheck("t", tolerance=0.25, window=5, min_history=3).run(source, state=state)
    # median 1000 -> 1300 is 30% off and fails. Against the mean (~10,800) it
    # would look like a 88% *drop* and also fail, but for the wrong reason.
    assert result.metadata["baseline_median"] == 1000
    assert result.success is False


def test_stats_helpers():
    assert median_value([]) is None
    assert median_value([3, 1, 2]) == 2
    assert mad([10, 10, 10]) == 0
    assert mad([1, 2, 3, 4, 100]) == 1
    assert relative_deviation(120, 100) == pytest.approx(0.2)
    assert relative_deviation(5, 0) is None, "no relative scale against zero"
    assert robust_z_score(10, [10, 10, 10]) is None, "zero spread has no z-score"
    assert robust_z_score(100, [1, 2, 3, 4, 5]) > 3


# --------------------------------------------------------------------------
# Defect 3: baseline poisoning
# --------------------------------------------------------------------------


def test_failed_run_is_excluded_from_future_baselines(tmp_path):
    """An anomaly must not quietly become the new normal."""
    counts = iter([1000, 1000, 1000, 9_000_000, 1000])

    class _Scripted(_SqliteSource):
        def execute(self, sql):
            return [{"n": next(counts)}]

    source = _Scripted({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    check = VolumeDriftCheck("t", tolerance=0.25, min_history=3)

    for _ in range(3):
        check.run(source, state=state)          # establish 1000, 1000, 1000
    spike = check.run(source, state=state)      # 9,000,000 -> fails
    assert spike.success is False

    # The spike was recorded as an anomaly, so the baseline is still 1000 and
    # the next normal run passes rather than being judged against the spike.
    assert state.baseline_row_counts("s", "t") == [1000, 1000, 1000]
    assert check.run(source, state=state).success is True


def test_anomaly_status_is_recorded(tmp_path):
    counts = iter([100, 100, 100, 10_000])

    class _Scripted(_SqliteSource):
        def execute(self, sql):
            return [{"n": next(counts)}]

    source = _Scripted({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    check = VolumeDriftCheck("t", min_history=3)
    for _ in range(4):
        check.run(source, state=state)
    statuses = [row["status"] for row in state.row_count_history("s", "t")]
    assert statuses == ["ok", "ok", "ok", "anomaly"]


# --------------------------------------------------------------------------
# Honesty about insufficient history, and the zero baseline
# --------------------------------------------------------------------------


def test_insufficient_history_says_so(tmp_path):
    class _Fixed(_SqliteSource):
        def execute(self, sql):
            return [{"n": 100}]

    source = _Fixed({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    result = VolumeDriftCheck("t", min_history=3).run(source, state=state)
    assert result.success is True
    assert "Not enough history" in result.details
    assert result.metadata["history"] == 0


def test_min_history_must_be_met_before_judging(tmp_path):
    class _Fixed(_SqliteSource):
        def execute(self, sql):
            return [{"n": 100}]

    source = _Fixed({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    check = VolumeDriftCheck("t", min_history=3)
    for expected_history in (0, 1, 2):
        result = check.run(source, state=state)
        assert result.metadata["history"] == expected_history
        assert "Not enough history" in result.details
    assert "median baseline" in check.run(source, state=state).details


def test_zero_baseline_flags_new_volume(tmp_path):
    counts = iter([0, 0, 0, 500])

    class _Scripted(_SqliteSource):
        def execute(self, sql):
            return [{"n": next(counts)}]

    source = _Scripted({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    check = VolumeDriftCheck("t", min_history=3)
    for _ in range(3):
        check.run(source, state=state)
    result = check.run(source, state=state)
    # Previously `deviation = ... if baseline else 0.0` made this PASS silently.
    assert result.success is False
    assert "appeared where the baseline had none" in result.details


def test_zero_baseline_zero_count_is_unchanged(tmp_path):
    class _Fixed(_SqliteSource):
        def execute(self, sql):
            return [{"n": 0}]

    source = _Fixed({"name": "s", "path": str(tmp_path / "x.db")})
    state = FileState(tmp_path / "st")
    check = VolumeDriftCheck("t", min_history=3)
    for _ in range(3):
        check.run(source, state=state)
    assert check.run(source, state=state).success is True


# --------------------------------------------------------------------------
# Shared SQL helpers (previously three divergent copies)
# --------------------------------------------------------------------------


def test_sql_literal_handles_non_finite_floats():
    """NaN/Inf were emitted verbatim and produced invalid SQL."""
    assert sql_literal(float("nan")) == "NULL"
    assert sql_literal(float("inf")) == "NULL"
    assert sql_literal(float("-inf")) == "NULL"


def test_sql_literal_basics():
    assert sql_literal(None) == "NULL"
    assert sql_literal(True) == "TRUE"
    assert sql_literal(42) == "42"
    assert sql_literal("O'Brien") == "'O''Brien'"


def test_build_batch_predicate_helper():
    assert build_batch_predicate("pb", "B1") == "pb = 'B1'"
    assert build_batch_predicate(None, "B1") is None
    assert build_batch_predicate("pb", "B1", "pb > '{{ batch_id }}'", {"batch_id": "B0"}) == "pb > 'B0'"


def test_where_clause_helper():
    assert where_clause(None) == ""
    assert where_clause("a = 1") == " WHERE a = 1"

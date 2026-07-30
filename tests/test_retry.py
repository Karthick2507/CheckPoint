"""Retry tests (P3).

A Presto gateway blip failed the whole run: the framework had no retry logic at
all (the previous BCV tool had it and it was lost in the rewrite). Retries are
deliberately conservative — transient errors only, reads only, backoff with
jitter.
"""

from __future__ import annotations

import sqlite3

import pytest

from data_sources.base import DataSource, _looks_like_read
from runtime.retry import (
    DEFAULT_POLICY,
    RetryPolicy,
    is_transient,
    with_retry,
)


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


# --------------------------------------------------------------------------
# Classifying failures
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "message",
    [
        "connection reset by peer",
        "Read timed out",
        "503 Service Unavailable",
        "gateway timeout",
        "broken pipe",
        "server closed the connection unexpectedly",
    ],
)
def test_transient_errors_are_retryable(message):
    assert is_transient(RuntimeError(message)) is True


@pytest.mark.parametrize(
    "message",
    [
        "syntax error at or near SELECT",
        "Table 'foo' does not exist",
        "no such table: request",
        "permission denied for relation t",
        "unauthorized",
    ],
)
def test_permanent_errors_are_not_retryable(message):
    assert is_transient(RuntimeError(message)) is False


def test_permanent_marker_beats_transient_marker():
    """"table not found" must not retry just because it mentions a gateway."""
    assert is_transient(RuntimeError("gateway says: table not found")) is False


def test_unknown_errors_are_not_retried():
    assert is_transient(ValueError("something odd")) is False


# --------------------------------------------------------------------------
# The retry loop
# --------------------------------------------------------------------------


def test_succeeds_without_retrying():
    calls = []
    result = with_retry(lambda: calls.append(1) or "ok", sleep=lambda d: None)
    assert result == "ok"
    assert len(calls) == 1


def test_retries_then_succeeds():
    attempts = {"n": 0}

    def flaky():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise RuntimeError("connection reset")
        return "recovered"

    slept: list[float] = []
    assert with_retry(flaky, sleep=slept.append) == "recovered"
    assert attempts["n"] == 3
    assert len(slept) == 2, "slept between attempts"


def test_gives_up_after_attempts_and_reraises():
    attempts = {"n": 0}

    def always_flaky():
        attempts["n"] += 1
        raise RuntimeError("connection reset")

    with pytest.raises(RuntimeError, match="connection reset"):
        with_retry(always_flaky, policy=RetryPolicy(attempts=3), sleep=lambda d: None)
    assert attempts["n"] == 3, "exactly the configured number of attempts"


def test_permanent_failure_is_not_retried():
    attempts = {"n": 0}

    def bad_sql():
        attempts["n"] += 1
        raise RuntimeError("no such table: ghost")

    with pytest.raises(RuntimeError):
        with_retry(bad_sql, sleep=lambda d: None)
    assert attempts["n"] == 1, "must fail fast, not burn minutes on a hopeless query"


def test_backoff_grows_and_is_capped():
    policy = RetryPolicy(initial_delay=1.0, multiplier=2.0, max_delay=5.0, jitter=0)
    assert policy.delay_for(1) == 1.0
    assert policy.delay_for(2) == 2.0
    assert policy.delay_for(3) == 4.0
    assert policy.delay_for(4) == 5.0, "capped"
    assert policy.delay_for(10) == 5.0


def test_jitter_varies_the_delay():
    policy = RetryPolicy(initial_delay=10.0, jitter=0.5)
    delays = {policy.delay_for(1) for _ in range(20)}
    assert len(delays) > 1, "jitter must spread a recovering fleet"
    assert all(10.0 <= d <= 15.0 for d in delays)


def test_on_retry_callback_receives_context():
    seen: list[tuple[int, str, float]] = []

    def flaky():
        if len(seen) < 1:
            raise RuntimeError("timeout")
        return "ok"

    with_retry(
        flaky,
        on_retry=lambda attempt, exc, delay: seen.append((attempt, str(exc), delay)),
        sleep=lambda d: None,
    )
    assert seen[0][0] == 1
    assert "timeout" in seen[0][1]


def test_single_attempt_policy_never_retries():
    attempts = {"n": 0}

    def flaky():
        attempts["n"] += 1
        raise RuntimeError("timeout")

    with pytest.raises(RuntimeError):
        with_retry(flaky, policy=RetryPolicy(attempts=1), sleep=lambda d: None)
    assert attempts["n"] == 1


# --------------------------------------------------------------------------
# Read vs write classification
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "sql",
    ["SELECT 1", "  select 1", "WITH x AS (SELECT 1) SELECT * FROM x", "DESCRIBE t",
     "SHOW TABLES", "EXPLAIN SELECT 1", "PRAGMA table_info(t)", "-- note\nSELECT 1"],
)
def test_reads_are_retryable(sql):
    assert _looks_like_read(sql) is True


@pytest.mark.parametrize(
    "sql",
    ["INSERT INTO t VALUES (1)", "DELETE FROM t", "UPDATE t SET a = 1",
     "CREATE TABLE t (a INT)", "DROP TABLE t", "MERGE INTO t", ""],
)
def test_writes_are_not_retryable(sql):
    assert _looks_like_read(sql) is False, "re-issuing a write can duplicate rows"


# --------------------------------------------------------------------------
# Wired into DataSource
# --------------------------------------------------------------------------


def test_execute_retries_a_transient_read(tmp_path):
    db = tmp_path / "a.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (a INTEGER)")
    con.execute("INSERT INTO t VALUES (1)")
    con.commit()
    con.close()

    class _Flaky(_SqliteSource):
        def __init__(self, config):
            super().__init__(config)
            self.calls = 0

        def _execute_once(self, sql):
            self.calls += 1
            if self.calls == 1:
                raise RuntimeError("connection reset by peer")
            return super()._execute_once(sql)

    source = _Flaky({"name": "s", "path": str(db), "retry_initial_delay": 0})
    assert source.execute("SELECT a FROM t") == [{"a": 1}]
    assert source.calls == 2, "retried once, then succeeded"


def test_execute_does_not_retry_a_write(tmp_path):
    class _Flaky(_SqliteSource):
        def __init__(self, config):
            super().__init__(config)
            self.calls = 0

        def _execute_once(self, sql):
            self.calls += 1
            raise RuntimeError("connection reset by peer")

    source = _Flaky({"name": "s", "path": str(tmp_path / "b.db"), "retry_initial_delay": 0})
    with pytest.raises(RuntimeError):
        source.execute("INSERT INTO t VALUES (1)")
    assert source.calls == 1, "a write must not be blindly re-issued"


def test_execute_retry_can_be_forced(tmp_path):
    class _Flaky(_SqliteSource):
        def __init__(self, config):
            super().__init__(config)
            self.calls = 0

        def _execute_once(self, sql):
            self.calls += 1
            raise RuntimeError("timeout")

    source = _Flaky({"name": "s", "path": str(tmp_path / "c.db"), "retry_initial_delay": 0})
    with pytest.raises(RuntimeError):
        source.execute("INSERT INTO t VALUES (1)", retry=True)
    assert source.calls == DEFAULT_POLICY.attempts


def test_retry_policy_comes_from_config(tmp_path):
    source = _SqliteSource(
        {"name": "s", "path": str(tmp_path / "d.db"), "retry_attempts": 7, "retry_max_delay": 2}
    )
    assert source.retry_policy.attempts == 7
    assert source.retry_policy.max_delay == 2

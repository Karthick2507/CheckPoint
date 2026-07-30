"""State durability tests (P2).

Baselines for schema-drift and volume-drift previously lived under the
gitignored, per-run ``etl_output/`` tree, so in CI, cron, or any container they
were empty on every run: both checks reported "first observation — establishing
baseline" forever and could never detect drift.

These tests cover the durable location plus the safety properties that make
file-based state trustworthy: atomic writes, locking, retention, and tolerance
of corrupt data.
"""

from __future__ import annotations

import csv
import json
import threading
from pathlib import Path

import pytest

from runtime.run_context import DEFAULT_STATE_DIR, RunContext
from runtime.state import DEFAULT_MAX_HISTORY, FileState


# --------------------------------------------------------------------------
# The location fix
# --------------------------------------------------------------------------


def test_state_dir_is_outside_the_run_output_tree(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path / "etl_output")
    assert ctx.state_dir == DEFAULT_STATE_DIR
    assert tmp_path / "etl_output" not in ctx.state_dir.parents
    assert "etl_output" not in str(ctx.state_dir)


def test_state_root_is_configurable(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out", state_root=tmp_path / "durable")
    assert ctx.state_dir == tmp_path / "durable"


def test_state_survives_a_new_run_context(tmp_path):
    """The point of the fix: run 2 sees what run 1 recorded."""
    durable = tmp_path / "durable"

    ctx1 = RunContext(pipeline="p", output_root=tmp_path / "out1", state_root=durable)
    FileState(ctx1.state_dir).append_row_count("presto", "request", 100)

    # a completely fresh run, new output dir — as in a new container
    ctx2 = RunContext(pipeline="p", output_root=tmp_path / "out2", state_root=durable)
    assert FileState(ctx2.state_dir).baseline_row_count("presto", "request") == 100.0


def test_state_dir_not_gitignored():
    ignore = Path(".gitignore").read_text()
    assert "\nstate/\n" not in ignore, "state/ must not be ignored or baselines never persist"


# --------------------------------------------------------------------------
# Atomic writes
# --------------------------------------------------------------------------


def test_schema_snapshot_write_is_atomic(tmp_path):
    state = FileState(tmp_path)
    state.save_schema_snapshot("s", "t", [{"name": "a", "type": "varchar"}])
    leftovers = list(tmp_path.rglob("*.tmp"))
    assert leftovers == [], "no temp files may be left behind"


def test_corrupt_snapshot_is_treated_as_no_baseline(tmp_path):
    """A torn write must not crash the next run."""
    state = FileState(tmp_path)
    state.save_schema_snapshot("s", "t", [{"name": "a"}])
    path = next((tmp_path / "schema_snapshots").glob("*.json"))
    path.write_text("{ this is not json")
    assert state.load_schema_snapshot("s", "t") is None


def test_corrupt_history_line_is_skipped(tmp_path):
    state = FileState(tmp_path)
    state.append_row_count("s", "t", 100)
    state.append_row_count("s", "t", 200)
    path = next((tmp_path / "row_count_history").glob("*.csv"))
    with path.open("a") as handle:
        handle.write("garbage,line,here,notanumber,ok\n")
    history = state.row_count_history("s", "t")
    assert [h["row_count"] for h in history] == [100, 200], "bad line skipped, good data kept"


# --------------------------------------------------------------------------
# Concurrency
# --------------------------------------------------------------------------


def test_concurrent_appends_do_not_corrupt_history(tmp_path):
    state = FileState(tmp_path)
    errors: list[Exception] = []

    def append(n: int) -> None:
        try:
            for i in range(10):
                FileState(tmp_path).append_row_count("s", "t", n * 100 + i)
        except Exception as exc:  # pragma: no cover - failure path
            errors.append(exc)

    threads = [threading.Thread(target=append, args=(n,)) for n in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert errors == []
    history = state.row_count_history("s", "t")
    assert len(history) == 40, "every append must survive"

    # the file must still be well-formed CSV with one header
    path = next((tmp_path / "row_count_history").glob("*.csv"))
    lines = path.read_text().strip().splitlines()
    assert lines[0].startswith("timestamp")
    assert sum(1 for line in lines if line.startswith("timestamp")) == 1


# --------------------------------------------------------------------------
# Retention
# --------------------------------------------------------------------------


def test_history_is_capped(tmp_path):
    state = FileState(tmp_path, max_history=10)
    for i in range(25):
        state.append_row_count("s", "t", i)
    history = state.row_count_history("s", "t")
    assert len(history) == 10, "history must stay bounded"
    assert [h["row_count"] for h in history] == list(range(15, 25)), "keeps the most recent"


def test_default_retention_is_bounded():
    assert DEFAULT_MAX_HISTORY > 0


# --------------------------------------------------------------------------
# Anomaly exclusion
# --------------------------------------------------------------------------


def test_anomalous_observations_excluded_from_baseline(tmp_path):
    """A bad run must not quietly become the new normal."""
    state = FileState(tmp_path)
    for _ in range(3):
        state.append_row_count("s", "t", 100, status="ok")
    state.append_row_count("s", "t", 5_000_000, status="anomaly")

    assert state.baseline_row_counts("s", "t") == [100, 100, 100]
    assert state.baseline_row_count("s", "t") == 100.0
    assert 5_000_000 in state.baseline_row_counts("s", "t", include_anomalies=True)


def test_status_defaults_to_ok(tmp_path):
    state = FileState(tmp_path)
    state.append_row_count("s", "t", 42)
    assert state.row_count_history("s", "t")[0]["status"] == "ok"


def test_baseline_none_without_history(tmp_path):
    assert FileState(tmp_path).baseline_row_count("s", "t") is None


def test_window_limits_baseline(tmp_path):
    state = FileState(tmp_path)
    for count in (10, 20, 30, 40):
        state.append_row_count("s", "t", count)
    assert state.baseline_row_counts("s", "t", window=2) == [30, 40]

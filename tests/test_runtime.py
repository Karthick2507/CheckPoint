"""Tests for the runtime layer (run context + file state)."""

from __future__ import annotations

from datetime import datetime

from runtime.run_context import RunContext, default_batch_id
from runtime.state import FileState


# --------------------------------------------------------------------------
# RunContext
# --------------------------------------------------------------------------


def test_run_context_generates_ids(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path)
    assert ctx.run_id
    assert ctx.batch_id
    assert ctx.started_at
    assert ctx.run_dir == tmp_path / "runs" / ctx.run_id


def test_default_batch_id_is_prev_hour():
    now = datetime(2026, 7, 29, 10, 45, 30)
    # 24h earlier, rounded to the hour -> 2026-07-28 10:00:00
    assert default_batch_id(now) == "20260728100000"


def test_ensure_dirs_and_subdir(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path).ensure_dirs()
    assert (ctx.run_dir / "validation").is_dir()
    assert (ctx.run_dir / "quarantine").is_dir()
    assert (ctx.run_dir / "logs").is_dir()
    custom = ctx.subdir("extra")
    assert custom.is_dir()


def test_lineage_record(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path)
    ctx.record("extract", rows=100, source="presto")
    ctx.record("validate", suite="s")
    assert [e["stage"] for e in ctx.lineage] == ["extract", "validate"]
    assert ctx.lineage[0]["rows"] == 100
    assert ctx.to_dict()["run_id"] == ctx.run_id


# --------------------------------------------------------------------------
# FileState: schema snapshots
# --------------------------------------------------------------------------


def test_schema_snapshot_roundtrip(tmp_path):
    state = FileState(tmp_path)
    assert state.load_schema_snapshot("presto", "request") is None
    cols = [{"name": "id", "type": "varchar"}, {"name": "n", "type": "integer"}]
    state.save_schema_snapshot("presto", "request", cols)
    loaded = state.load_schema_snapshot("presto", "request")
    assert loaded["columns"] == cols
    assert loaded["source"] == "presto"
    assert loaded["table"] == "request"


def test_schema_snapshot_filename_sanitized(tmp_path):
    state = FileState(tmp_path)
    state.save_schema_snapshot("presto", "mrm_log_flat.default.request", [{"name": "a"}])
    # no path separators leak into the filename
    files = list((tmp_path / "schema_snapshots").glob("*.json"))
    assert len(files) == 1
    assert "/" not in files[0].name


# --------------------------------------------------------------------------
# FileState: row-count history
# --------------------------------------------------------------------------


def test_row_count_history_and_baseline(tmp_path):
    state = FileState(tmp_path)
    assert state.baseline_row_count("presto", "request") is None

    for count in (100, 110, 90):
        state.append_row_count("presto", "request", count, run_id="r", batch_id="b")

    history = state.row_count_history("presto", "request")
    assert [h["row_count"] for h in history] == [100, 110, 90]
    assert state.baseline_row_count("presto", "request") == 100.0  # mean of 3


def test_baseline_window(tmp_path):
    state = FileState(tmp_path)
    for count in (10, 20, 30, 40):
        state.append_row_count("presto", "t", count)
    # window of 2 -> mean of last two (30, 40) = 35
    assert state.baseline_row_count("presto", "t", window=2) == 35.0

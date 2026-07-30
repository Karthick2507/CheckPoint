"""Streaming extract tests (P1).

``execute`` calls ``fetchall``, so memory grows with the result set. Pushdown
avoids the problem entirely for same-warehouse work, but a cross-system move
(Presto -> Snowflake) genuinely has to carry rows — it just must not hold them
all at once.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.extract import Extractor
from core.load import Loader
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


@pytest.fixture()
def source(tmp_path):
    db = tmp_path / "s.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE src (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO src VALUES (?, ?)", [(i, f"v{i}") for i in range(1000)])
    con.commit()
    con.close()
    return _SqliteSource({"name": "src", "path": str(db)})


@pytest.fixture()
def target(tmp_path):
    db = tmp_path / "t.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.commit()
    con.close()
    return _SqliteSource({"name": "tgt", "path": str(db)})


# --------------------------------------------------------------------------
# DataSource.stream
# --------------------------------------------------------------------------


def test_stream_yields_chunks(source):
    chunks = list(source.stream("SELECT id, v FROM src", chunk_size=250))
    assert len(chunks) == 4
    assert all(len(c) == 250 for c in chunks)
    assert chunks[0][0] == {"id": 0, "v": "v0"}


def test_stream_never_holds_more_than_chunk_size(source):
    """The memory guarantee: no chunk exceeds the configured size."""
    for chunk in source.stream("SELECT id FROM src", chunk_size=100):
        assert len(chunk) <= 100


def test_stream_handles_partial_final_chunk(source):
    chunks = list(source.stream("SELECT id FROM src LIMIT 250", chunk_size=100))
    assert [len(c) for c in chunks] == [100, 100, 50]


def test_stream_empty_result(source):
    assert list(source.stream("SELECT id FROM src WHERE id < 0")) == []


def test_stream_no_result_set_yields_nothing(source):
    assert list(source.stream("CREATE TABLE IF NOT EXISTS tmp_x (a INTEGER)")) == []


def test_stream_total_matches_execute(source):
    streamed = sum(len(c) for c in source.stream("SELECT id FROM src", chunk_size=137))
    assert streamed == len(source.execute("SELECT id FROM src"))


# --------------------------------------------------------------------------
# Extractor.stream
# --------------------------------------------------------------------------


def test_extractor_stream_returns_sql_and_chunks(source):
    sql, chunks = Extractor().stream(source, table="src", chunk_size=400)
    assert sql == "SELECT * FROM src"
    assert [len(c) for c in chunks] == [400, 400, 200]


def test_extractor_stream_incremental_sql(source):
    sql, chunks = Extractor().stream(
        source, table="src", batch_key="id", batch_id=1, incremental=True
    )
    assert sql == "SELECT * FROM src WHERE id = 1"
    assert sum(len(c) for c in chunks) == 1


def test_extractor_stream_requires_table_or_query(source):
    with pytest.raises(ValueError, match="either 'table' or 'query'"):
        Extractor().stream(source)


# --------------------------------------------------------------------------
# Loader.load_stream
# --------------------------------------------------------------------------


def test_load_stream_appends_all_chunks(source, target):
    _, chunks = Extractor().stream(source, table="src", chunk_size=300)
    result = Loader().load_stream(target, "dst", chunks)
    assert result.inserted == 1000
    assert target.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 1000


def test_load_stream_skips_empty_chunks(target):
    result = Loader().load_stream(target, "dst", [[], [{"id": 1, "v": "a"}], []])
    assert result.inserted == 1


def test_load_stream_rejects_destructive_modes(target):
    with pytest.raises(ValueError, match="only 'append'"):
        Loader().load_stream(target, "dst", [[{"id": 1}]], mode="overwrite")


def test_load_stream_is_transactional(source, target):
    """A failure mid-stream must not leave half the rows behind."""
    def bad_chunks():
        yield [{"id": 1, "v": "a"}]
        yield [{"id": 2, "nope": "boom"}]  # unknown column -> INSERT fails

    with pytest.raises(Exception):
        Loader().load_stream(target, "dst", bad_chunks())
    assert target.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 0


# --------------------------------------------------------------------------
# Eligibility rules
# --------------------------------------------------------------------------


def _pipeline(tmp_path, pipeline_dict, sources):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, batch_id="B1", output_root=tmp_path / "out")
    return Pipeline(cfg, resolve_source=lambda n: sources[n], state=FileState(tmp_path / "st"), context=ctx)


def _cfg(**overrides):
    base = {
        "name": "p",
        "source": {"connection": "src", "table": "src"},
        "extract": {"stream": True},
        "target": {"connection": "tgt", "table": "dst", "mode": "append"},
    }
    base.update(overrides)
    return {"pipeline": base}


def test_streaming_enabled(tmp_path, source, target):
    p = _pipeline(tmp_path, _cfg(), {"src": source, "tgt": target})
    ok, why = p.can_stream()
    assert ok is True and why == ""


def test_streaming_off_by_default(tmp_path, source, target):
    p = _pipeline(tmp_path, _cfg(extract={}), {"src": source, "tgt": target})
    assert p.can_stream() == (False, "not enabled")


def test_streaming_declined_with_transform(tmp_path, source, target):
    p = _pipeline(tmp_path, _cfg(transform=["SELECT id FROM src"]), {"src": source, "tgt": target})
    ok, why = p.can_stream()
    assert ok is False and "transform" in why


def test_streaming_declined_for_destructive_load(tmp_path, source, target):
    p = _pipeline(
        tmp_path,
        _cfg(target={"connection": "tgt", "table": "dst", "mode": "overwrite"}),
        {"src": source, "tgt": target},
    )
    ok, why = p.can_stream()
    assert ok is False and "append" in why


def test_streaming_declined_without_target(tmp_path, source):
    cfg = _cfg()
    cfg["pipeline"].pop("target")
    p = _pipeline(tmp_path, cfg, {"src": source})
    ok, why = p.can_stream()
    assert ok is False and "target" in why


# --------------------------------------------------------------------------
# End to end
# --------------------------------------------------------------------------


def test_pipeline_streams_cross_system(tmp_path, source, target):
    result = _pipeline(
        tmp_path, _cfg(extract={"stream": True, "chunk_size": 250}), {"src": source, "tgt": target}
    ).run()

    assert result.errors == []
    assert result.execution == "stream"
    assert result.load.inserted == 1000
    assert result.extract_rows == 1000
    assert target.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 1000


def test_pipeline_falls_back_when_streaming_impossible(tmp_path, source, target):
    """Requesting streaming with a transform must still work, just buffered."""
    result = _pipeline(
        tmp_path,
        _cfg(execution="rows", transform=["SELECT id, v FROM src WHERE id < 10"]),
        {"src": source, "tgt": target},
    ).run()

    assert result.errors == []
    assert result.execution == "rows", "fell back to the buffered path"
    assert result.load.inserted == 10
    reasons = [e for e in result.context.lineage if e["stage"] == "extract:stream_unavailable"]
    assert reasons and "transform" in reasons[0]["reason"]

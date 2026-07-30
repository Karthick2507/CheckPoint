"""Resource lifecycle tests (P3).

Two leaks: every gate built a fresh Great Expectations context (re-registering
the datasource and opening another engine), and nothing ever disposed the
engines a run created — fine for a one-shot CLI, a slow leak in a scheduler
process that runs pipelines all day.
"""

from __future__ import annotations

import sqlite3

import pytest
import yaml

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from core.validate import GEValidationFramework, SuiteConfig
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
    type = "counting"

    def __init__(self, config):
        super().__init__(config)
        self.disposals = 0

    def dispose(self) -> None:
        self.disposals += 1
        super().dispose()


@pytest.fixture()
def source(tmp_path):
    db = tmp_path / "s.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO t VALUES (?, ?)", [(1, "a"), (2, "b")])
    con.commit()
    con.close()
    return _CountingSource({"name": "src", "path": str(db)})


def _suite_file(tmp_path, name, expectations):
    path = tmp_path / f"{name}.yml"
    path.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": name, "asset": {"type": "table", "name": "t", "table_name": "t"}},
                "expectations": expectations,
            }
        )
    )
    return str(path)


def _pipeline(tmp_path, source, pipeline_dict):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, output_root=tmp_path / "out", state_root=tmp_path / "state")
    return Pipeline(cfg, resolve_source=lambda n: source, state=FileState(tmp_path / "st"), context=ctx)


# --------------------------------------------------------------------------
# One GE context per run, not per gate
# --------------------------------------------------------------------------


def test_ge_context_is_reused(tmp_path, source):
    pipeline = _pipeline(tmp_path, source, {"pipeline": {"name": "p", "source": {"connection": "src", "table": "t"}}})
    first = pipeline.ge_context()
    assert pipeline.ge_context() is first, "the same context must serve every gate"


def test_all_gates_share_one_context(tmp_path, source):
    exp = [{"type": "expect_column_to_exist", "column": "id"}]
    contexts: list[int] = []

    pipeline = _pipeline(
        tmp_path,
        source,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "validate": {
                    "raw": _suite_file(tmp_path, "raw", exp),
                    "curated": _suite_file(tmp_path, "curated", exp),
                },
            }
        },
    )
    original = GEValidationFramework.run

    def spy(self, suite_cfg):
        contexts.append(id(self.context))
        return original(self, suite_cfg)

    GEValidationFramework.run = spy
    try:
        result = pipeline.run()
    finally:
        GEValidationFramework.run = original

    assert result.errors == []
    assert len(contexts) == 2, "both gates ran"
    assert len(set(contexts)) == 1, "…through a single GE context"


def test_shared_context_keeps_distinct_assets_apart(tmp_path, source):
    """Same asset name, different data: the second must not silently reuse the first."""
    import great_expectations as gx

    context = gx.get_context(mode="ephemeral")
    table_suite = SuiteConfig.from_dict(
        {
            "suite": {"name": "s1", "asset": {"type": "table", "name": "shared", "table_name": "t"}},
            "expectations": [{"type": "expect_table_row_count_to_be_between", "min_value": 2}],
        }
    )
    query_suite = SuiteConfig.from_dict(
        {
            "suite": {
                "name": "s2",
                "asset": {"type": "query", "name": "shared", "query": "SELECT * FROM t WHERE id = 1"},
            },
            "expectations": [{"type": "expect_table_row_count_to_be_between", "min_value": 1, "max_value": 1}],
        }
    )
    framework = GEValidationFramework(source, context=context)
    assert framework.run(table_suite).success is True   # 2 rows
    assert framework.run(query_suite).success is True   # 1 row — not the table's 2


# --------------------------------------------------------------------------
# Disposal
# --------------------------------------------------------------------------


def test_run_disposes_sources(tmp_path, source):
    pipeline = _pipeline(tmp_path, source, {"pipeline": {"name": "p", "source": {"connection": "src", "table": "t"}}})
    pipeline.run()
    assert source.disposals == 1, "engines must be released when the run ends"


def test_disposal_happens_even_on_failure(tmp_path, source):
    pipeline = _pipeline(
        tmp_path, source, {"pipeline": {"name": "p", "source": {"connection": "src", "table": "ghost"}}}
    )
    result = pipeline.run()
    assert result.errors, "the run failed"
    assert source.disposals == 1, "and still cleaned up"


def test_connection_resolved_once_per_run(tmp_path, source):
    """Source and target on the same connection must not resolve twice."""
    calls: list[str] = []

    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "execution": "rows",
                "source": {"connection": "src", "table": "t"},
                "target": {"connection": "src", "table": "t2", "mode": "append"},
            }
        }
    )
    source.execute("CREATE TABLE t2 (id INTEGER, v TEXT)")
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out", state_root=tmp_path / "state")

    def resolve(name):
        calls.append(name)
        return source

    Pipeline(cfg, resolve_source=resolve, state=FileState(tmp_path / "st"), context=ctx).run()
    assert calls == ["src"], "resolved once and cached, not once per stage"


def test_dispose_is_idempotent(tmp_path, source):
    pipeline = _pipeline(tmp_path, source, {"pipeline": {"name": "p", "source": {"connection": "src", "table": "t"}}})
    pipeline.run()
    pipeline.dispose()  # extra call must be harmless
    assert source.disposals == 1


def test_datasource_dispose_clears_the_engine(tmp_path):
    src = _SqliteSource({"name": "s", "path": str(tmp_path / "d.db")})
    src.execute("CREATE TABLE x (a INTEGER)")
    assert src._engine is not None
    src.dispose()
    assert src._engine is None
    # still usable afterwards — dispose releases, it does not break the source
    src.execute("INSERT INTO x VALUES (1)")
    assert src.execute("SELECT COUNT(*) AS n FROM x")[0]["n"] == 1

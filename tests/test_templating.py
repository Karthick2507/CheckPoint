"""SQL templating tests (P1).

Pipeline SQL referencing ``{{ batch_id }}`` previously reached the warehouse
verbatim — there was no templating engine at all, so the shipped example config
was broken. Rendering is strict: an unknown variable must raise rather than
silently produce ``WHERE process_batch_id = ''``.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from data_sources.base import DataSource
from runtime.run_context import RunContext
from runtime.state import FileState
from runtime.templating import TemplateRenderError, render_all, render_sql


# --------------------------------------------------------------------------
# Renderer
# --------------------------------------------------------------------------


def test_renders_batch_id():
    sql = render_sql("SELECT * FROM t WHERE pb = '{{ batch_id }}'", {"batch_id": "20260101000000"})
    assert sql == "SELECT * FROM t WHERE pb = '20260101000000'"


def test_plain_sql_passes_through_untouched():
    sql = "SELECT * FROM t WHERE a = 1"
    assert render_sql(sql, {"batch_id": "x"}) is sql


def test_unknown_variable_raises_not_silently_blank():
    with pytest.raises(TemplateRenderError, match="undefined variable"):
        render_sql("SELECT * FROM t WHERE pb = '{{ nope }}'", {"batch_id": "x"})


def test_error_lists_available_variables():
    with pytest.raises(TemplateRenderError, match="batch_id"):
        render_sql("{{ nope }}", {"batch_id": "x", "run_id": "y"})


def test_invalid_template_raises():
    with pytest.raises(TemplateRenderError, match="Invalid SQL template"):
        render_sql("SELECT {{ unclosed ", {"batch_id": "x"})


def test_render_all_renders_each_statement():
    out = render_all(["SELECT '{{ a }}'", "SELECT '{{ b }}'"], {"a": "1", "b": "2"})
    assert out == ["SELECT '1'", "SELECT '2'"]


def test_supports_conditionals_and_filters():
    sql = render_sql("{% if env == 'prod' %}A{% else %}B{% endif %}", {"env": "prod"})
    assert sql == "A"


def test_sandboxed_blocks_attribute_traversal():
    """Config-supplied templates must not reach into Python internals."""
    with pytest.raises(Exception):
        render_sql("{{ batch_id.__class__.__mro__ }}", {"batch_id": "x"})


def test_empty_sql_is_safe():
    assert render_sql("", {}) == ""


# --------------------------------------------------------------------------
# RunContext supplies the variables
# --------------------------------------------------------------------------


def test_template_context_exposes_run_identity(tmp_path):
    ctx = RunContext(pipeline="p", env="prod", output_root=tmp_path)
    context = ctx.template_context()
    assert context["batch_id"] == ctx.batch_id
    assert context["run_id"] == ctx.run_id
    assert context["pipeline"] == "p"
    assert context["env"] == "prod"


def test_template_context_merges_user_vars(tmp_path):
    ctx = RunContext(pipeline="p", output_root=tmp_path)
    context = ctx.template_context({"region": "us-east"})
    assert context["region"] == "us-east"
    assert context["batch_id"] == ctx.batch_id


def test_pipeline_config_parses_vars():
    cfg = PipelineConfig.from_dict(
        {"pipeline": {"name": "p", "source": {"connection": "s", "table": "t"}, "vars": {"region": "eu"}}}
    )
    assert cfg.vars == {"region": "eu"}


# --------------------------------------------------------------------------
# End-to-end through the pipeline
# --------------------------------------------------------------------------


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
    con.execute("CREATE TABLE t (id INTEGER, pb TEXT)")
    con.executemany("INSERT INTO t VALUES (?, ?)", [(1, "BATCH_A"), (2, "BATCH_A"), (3, "BATCH_B")])
    con.commit()
    con.close()
    return _SqliteSource({"name": "src", "path": str(db)})


def _run(tmp_path, pipeline_dict, source, batch_id="BATCH_A"):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, batch_id=batch_id, output_root=tmp_path / "out")
    return Pipeline(cfg, resolve_source=lambda n: source, state=FileState(tmp_path / "st"), context=ctx).run()


def test_transform_sql_is_templated(tmp_path, source):
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "transform": ["SELECT id FROM t WHERE pb = '{{ batch_id }}'"],
            }
        },
        source,
    )
    assert result.errors == []
    assert result.transform_rows == 2, "only BATCH_A rows should survive templating"


def test_source_query_is_templated(tmp_path, source):
    result = _run(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "src", "query": "SELECT id FROM t WHERE pb = '{{ batch_id }}'"}}},
        source,
    )
    assert result.errors == []
    assert result.extract_rows == 2


def test_user_vars_available_in_transform(tmp_path, source):
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "vars": {"wanted": "BATCH_B"},
                "transform": ["SELECT id FROM t WHERE pb = '{{ wanted }}'"],
            }
        },
        source,
    )
    assert result.transform_rows == 1


def test_bad_template_is_recorded_not_raised(tmp_path, source):
    """A template error must be a recorded StageError, not a crash."""
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "transform": ["SELECT id FROM t WHERE pb = '{{ typo_var }}'"],
            }
        },
        source,
    )
    assert any(e.stage == "transform" for e in result.errors)
    assert result.passed is False


def test_shipped_example_pipeline_renders(tmp_path):
    """The documented example used {{ batch_id }} and previously never rendered."""
    import os

    os.environ.setdefault("PRESTO_AUTH_TOKEN", "x")
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "request_daily",
                "source": {"connection": "mrm_presto", "table": "request", "batch_key": "process_batch_id"},
                "transform": ["SELECT a FROM request WHERE process_batch_id = '{{ batch_id }}'"],
            }
        }
    )
    ctx = RunContext(pipeline=cfg.name, batch_id="20260101000000", output_root=tmp_path)
    rendered = render_all(cfg.transform, ctx.template_context(cfg.vars))
    assert "{{" not in rendered[0]
    assert "20260101000000" in rendered[0]

"""Resilience tests (P0 hardening).

``Pipeline.run()`` must never raise. Operational failures — a bad table, a
missing suite, a broken check spec, a load error — have to be recorded as
StageErrors so the run still produces a manifest and a warnings report.
Previously any of these aborted the run and wrote nothing at all.
"""

from __future__ import annotations

import json
import sqlite3

import pytest
import yaml

from core.pipeline import Pipeline, PipelineConfig
from data_sources.base import DataSource
from reporting import collect_warnings, write_pipeline_reports
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
    con.execute("CREATE TABLE t (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO t VALUES (?, ?)", [(1, "a"), (2, "b")])
    con.commit()
    con.close()
    return _SqliteSource({"name": "src", "path": str(db)})


def _run(tmp_path, pipeline_dict, sources):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, output_root=tmp_path / "out")
    return Pipeline(
        cfg,
        resolve_source=lambda n: sources[n],
        state=FileState(tmp_path / "st"),
        context=ctx,
    ).run()


def _suite_file(tmp_path, name, table, expectations):
    path = tmp_path / f"{name}.yml"
    path.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": name, "asset": {"type": "table", "name": table, "table_name": table}},
                "expectations": expectations,
            }
        )
    )
    return str(path)


# --------------------------------------------------------------------------
# run() never raises
# --------------------------------------------------------------------------


def test_missing_table_is_recorded_not_raised(tmp_path, source):
    result = _run(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "src", "table": "does_not_exist"}}},
        {"src": source},
    )
    assert result.errors, "the failure must be recorded"
    assert result.errors[0].stage == "extract"
    assert result.passed is False
    assert result.has_critical_failure is True


def test_missing_suite_file_is_recorded(tmp_path, source):
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "validate": {"raw": str(tmp_path / "nope.yml")},
            }
        },
        {"src": source},
    )
    stages = [e.stage for e in result.errors]
    assert "validate:raw" in stages
    assert result.extract_rows == 2, "extract still succeeded"


def test_bad_check_spec_is_recorded(tmp_path, source):
    """A query source with no target previously raised out of the pipeline."""
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "query": "SELECT id FROM t"},
                "checks": [{"type": "volume_drift"}],
            }
        },
        {"src": source},
    )
    assert any(e.stage.startswith("check:") for e in result.errors)
    assert result.extract_rows == 2


def test_unresolvable_connection_is_recorded(tmp_path):
    def resolve(name):
        raise KeyError(f"no connection {name!r}")

    cfg = PipelineConfig.from_dict({"pipeline": {"name": "p", "source": {"connection": "ghost", "table": "t"}}})
    ctx = RunContext(pipeline="p", output_root=tmp_path / "out")
    result = Pipeline(cfg, resolve_source=resolve, state=FileState(tmp_path / "st"), context=ctx).run()
    assert result.errors[0].stage == "resolve_source"


def test_bad_transform_sql_is_recorded(tmp_path, source):
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "transform": ["SELECT * FROM nonexistent"],
            }
        },
        {"src": source},
    )
    assert any(e.stage == "transform" for e in result.errors)


def test_independent_checks_continue_after_one_fails(tmp_path, source):
    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "checks": [
                    {"type": "not_a_real_check"},
                    {"type": "volume_drift", "target": "t"},
                ],
            }
        },
        {"src": source},
    )
    assert len(result.errors) == 1, "only the bad spec failed"
    assert len(result.checks) == 1, "the good check still ran"


# --------------------------------------------------------------------------
# A failed upstream stage must not produce a bogus load
# --------------------------------------------------------------------------


def test_load_skipped_when_transform_fails(tmp_path, source):
    tgt_db = tmp_path / "t.db"
    con = sqlite3.connect(tgt_db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.executemany("INSERT INTO dst VALUES (?, ?)", [(99, "existing")])
    con.commit()
    con.close()
    target = _SqliteSource({"name": "tgt", "path": str(tgt_db)})

    result = _run(
        tmp_path,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "src", "table": "t"},
                "transform": ["SELECT * FROM nonexistent"],
                "target": {"connection": "tgt", "table": "dst", "mode": "overwrite"},
            }
        },
        {"src": source, "tgt": target},
    )
    assert result.load is None, "must not load after a failed transform"
    assert target.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 1, "target untouched"


# --------------------------------------------------------------------------
# Reports are always written
# --------------------------------------------------------------------------


def test_reports_written_even_on_operational_failure(tmp_path, source):
    result = _run(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "src", "table": "does_not_exist"}}},
        {"src": source},
    )
    paths = write_pipeline_reports(result)
    assert paths["manifest"].exists()
    assert paths["warnings"].exists()

    manifest = json.loads(paths["manifest"].read_text())
    assert manifest["status"] == "error"
    assert manifest["errors"], "errors must be in the manifest"
    assert manifest["errors"][0]["stage"] == "extract"

    md = paths["warnings"].read_text()
    assert "Operational errors" in md
    assert "OperationalError" in md or "extract" in md


def test_errors_appear_in_warnings_as_critical(tmp_path, source):
    result = _run(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "src", "table": "does_not_exist"}}},
        {"src": source},
    )
    warnings = collect_warnings(result)
    assert warnings, "an operational error must produce a warning row"
    assert warnings[0].severity == "critical"
    assert warnings[0].dimension == "operational"


def test_healthy_run_still_passes(tmp_path, source):
    raw = _suite_file(tmp_path, "raw", "t", [{"type": "expect_column_values_to_not_be_null", "column": "id"}])
    result = _run(
        tmp_path,
        {"pipeline": {"name": "p", "source": {"connection": "src", "table": "t"}, "validate": {"raw": raw}}},
        {"src": source},
    )
    assert result.errors == []
    assert result.passed is True
    assert json.loads(write_pipeline_reports(result)["manifest"].read_text())["status"] == "passed"

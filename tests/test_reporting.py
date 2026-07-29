"""Tests for the reporting layer (manifest + warnings report)."""

from __future__ import annotations

import json
import sqlite3

import pytest
import yaml

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
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
def sources(tmp_path):
    src = tmp_path / "src.db"
    con = sqlite3.connect(src)
    con.execute("CREATE TABLE request (transaction_id TEXT, duration INTEGER)")
    con.executemany("INSERT INTO request VALUES (?, ?)", [("t1", 10), ("t2", 200), ("t3", 300)])
    con.commit()
    con.close()
    tgt = tmp_path / "tgt.db"
    con = sqlite3.connect(tgt)
    con.execute("CREATE TABLE request_clean (transaction_id TEXT, duration INTEGER)")
    con.commit()
    con.close()
    return {"src": _SqliteSource({"name": "src", "path": str(src)}),
            "tgt": _SqliteSource({"name": "tgt", "path": str(tgt)})}


def _suite(tmp_path, name, table, expectations):
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


def _run_failing_pipeline(tmp_path, sources):
    raw = _suite(
        tmp_path,
        "raw",
        "request",
        [
            {"type": "expect_column_values_to_be_between", "column": "duration", "min_value": 0, "max_value": 50,
             "severity": "critical"},
        ],
    )
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "request_daily",
                "source": {"connection": "src", "table": "request"},
                "target": {"connection": "tgt", "table": "request_clean", "mode": "append"},
                "validate": {"raw": raw},
                "checks": [{"type": "freshness", "target": "request", "timestamp_column": "transaction_id",
                            "max_lag_hours": 1, "severity": "warning"}],
            }
        }
    )
    ctx = RunContext(pipeline="request_daily", output_root=tmp_path / "out")
    return Pipeline(cfg, resolve_source=lambda n: sources[n], state=FileState(tmp_path / "st"), context=ctx).run()


def test_collect_warnings(tmp_path, sources):
    result = _run_failing_pipeline(tmp_path, sources)
    warnings = collect_warnings(result)
    # one critical GE failure (duration range) + one check failure (freshness)
    subjects = {w.subject for w in warnings}
    assert "expect_column_values_to_be_between" in subjects
    assert "freshness" in subjects
    # critical sorts first
    assert warnings[0].severity == "critical"


def test_write_pipeline_reports(tmp_path, sources):
    result = _run_failing_pipeline(tmp_path, sources)
    paths = write_pipeline_reports(result)

    manifest = paths["manifest"]
    warnings = paths["warnings"]
    assert manifest.exists()
    assert warnings.exists()

    data = json.loads(manifest.read_text())
    assert data["pipeline"] == "request_daily"
    assert data["status"] in ("critical", "warning")
    assert data["has_critical_failure"] is True

    md = warnings.read_text()
    assert "Warnings Report" in md
    assert "Critical failures" in md
    assert "expect_column_values_to_be_between" in md

    # per-suite validation reports were written under validation/
    assert any(p.name.endswith("_validation.json") for p in paths["validations"])


def test_clean_run_reports_no_failures(tmp_path, sources):
    raw = _suite(tmp_path, "raw", "request",
                 [{"type": "expect_column_to_exist", "column": "transaction_id"}])
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "clean",
                "source": {"connection": "src", "table": "request"},
                "validate": {"raw": raw},
            }
        }
    )
    ctx = RunContext(pipeline="clean", output_root=tmp_path / "out")
    result = Pipeline(cfg, resolve_source=lambda n: sources[n], state=FileState(tmp_path / "st"), context=ctx).run()
    paths = write_pipeline_reports(result)
    md = paths["warnings"].read_text()
    assert "No failures" in md
    assert json.loads(paths["manifest"].read_text())["status"] == "passed"

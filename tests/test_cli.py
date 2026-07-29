"""Tests for the CLI entrypoint (via typer's CliRunner)."""

from __future__ import annotations

import sqlite3

import yaml
from typer.testing import CliRunner

from cli import _exit_code, _load_connections, app

runner = CliRunner()


def test_list_sources():
    result = runner.invoke(app, ["list-sources"])
    assert result.exit_code == 0
    assert "presto" in result.stdout
    assert "snowflake" in result.stdout


def test_list_expectations_filter():
    result = runner.invoke(app, ["list-expectations", "not_be_null"])
    assert result.exit_code == 0
    assert "expect_column_values_to_not_be_null" in result.stdout


def test_exit_code_policy():
    assert _exit_code(has_critical=True, passed=False, fail_on="critical") == 1
    assert _exit_code(has_critical=False, passed=False, fail_on="critical") == 0
    assert _exit_code(has_critical=False, passed=False, fail_on="any") == 1
    assert _exit_code(has_critical=True, passed=False, fail_on="never") == 0


def test_load_connections(tmp_path):
    (tmp_path / "a.yml").write_text(
        yaml.safe_dump({"connection": {"name": "conn_a", "type": "presto", "host": "h", "catalog": "c", "schema": "s"}})
    )
    conns = _load_connections(tmp_path)
    assert "conn_a" in conns
    assert conns["conn_a"]["type"] == "presto"


def _sqlite_conn_file(tmp_path, name, db_path):
    # Register a sqlite connector on the fly so the CLI can resolve it.
    import data_sources.registry as registry
    from data_sources.base import DataSource

    if "sqlite_test" not in registry._REGISTRY:

        @registry.register("sqlite_test")
        class _SqliteSource(DataSource):  # noqa: D401
            def connection_string(self):
                return f"sqlite:///{self.config['path']}"

            def describe_sql(self, table):
                return f"PRAGMA table_info({table})"

    path = tmp_path / f"{name}.yml"
    path.write_text(yaml.safe_dump({"connection": {"name": name, "type": "sqlite_test", "path": str(db_path)}}))
    return path


def test_validate_command_end_to_end(tmp_path):
    db = tmp_path / "d.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE request (id TEXT)")
    con.executemany("INSERT INTO request VALUES (?)", [("a",), ("b",)])
    con.commit()
    con.close()

    conn_file = _sqlite_conn_file(tmp_path, "local", db)
    suite = tmp_path / "s.yml"
    suite.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": "req", "asset": {"type": "table", "name": "request", "table_name": "request"}},
                "expectations": [{"type": "expect_column_values_to_not_be_null", "column": "id"}],
            }
        )
    )

    result = runner.invoke(
        app,
        ["validate", "--connection", str(conn_file), "--suite", str(suite),
         "--output-dir", str(tmp_path / "out")],
    )
    assert result.exit_code == 0, result.stdout
    assert "req" in result.stdout


def test_run_pipeline_command_end_to_end(tmp_path):
    src_db = tmp_path / "src.db"
    con = sqlite3.connect(src_db)
    con.execute("CREATE TABLE request (transaction_id TEXT, duration INTEGER)")
    con.executemany("INSERT INTO request VALUES (?, ?)", [("t1", 10), ("t2", 20)])
    con.commit()
    con.close()

    conns_dir = tmp_path / "connections"
    conns_dir.mkdir()
    _sqlite_conn_file(conns_dir, "src", src_db)

    raw = tmp_path / "raw.yml"
    raw.write_text(
        yaml.safe_dump(
            {
                "suite": {"name": "raw", "asset": {"type": "table", "name": "request", "table_name": "request"}},
                "expectations": [{"type": "expect_column_values_to_not_be_null", "column": "transaction_id"}],
            }
        )
    )
    pipeline = tmp_path / "p.yml"
    pipeline.write_text(
        yaml.safe_dump(
            {
                "pipeline": {
                    "name": "req_pipe",
                    "source": {"connection": "src", "table": "request"},
                    "validate": {"raw": str(raw)},
                }
            }
        )
    )

    result = runner.invoke(
        app,
        ["run-pipeline", "--pipeline", str(pipeline), "--connections-dir", str(conns_dir),
         "--output-dir", str(tmp_path / "out")],
    )
    assert result.exit_code == 0, result.stdout
    assert "req_pipe" in result.stdout
    # manifest was written
    assert list((tmp_path / "out" / "runs").glob("*/run_manifest.json"))

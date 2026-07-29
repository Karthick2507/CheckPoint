"""Tests for the pluggable data_sources layer."""

from __future__ import annotations

import sqlite3

import pytest

from data_sources import (
    DataSource,
    available_sources,
    create_data_source,
    load_connection_config,
)
from data_sources.presto import PrestoDataSource
from data_sources.snowflake import SnowflakeDataSource


# --------------------------------------------------------------------------
# Registry / factory
# --------------------------------------------------------------------------


def test_builtin_sources_registered():
    names = available_sources()
    assert "presto" in names
    assert "trino" in names  # alias
    assert "snowflake" in names


def test_create_presto_by_type():
    ds = create_data_source({"type": "presto", "host": "h", "catalog": "c", "schema": "s"})
    assert isinstance(ds, PrestoDataSource)
    assert ds.type == "presto"


def test_create_trino_alias_maps_to_presto():
    ds = create_data_source({"type": "trino", "host": "h", "catalog": "c", "schema": "s"})
    assert isinstance(ds, PrestoDataSource)


def test_unknown_type_raises():
    with pytest.raises(ValueError, match="Unknown data source type"):
        create_data_source({"type": "oracle"})


def test_missing_type_raises():
    with pytest.raises(ValueError, match="requires a 'type'"):
        create_data_source({"host": "h"})


# --------------------------------------------------------------------------
# Presto connector
# --------------------------------------------------------------------------


def test_presto_connection_string():
    ds = PrestoDataSource({"host": "h.example.net", "port": 8080, "user": "alice", "catalog": "c", "schema": "s"})
    assert ds.connection_string() == "trino://alice@h.example.net:8080/c/s"


def test_presto_host_normalization_from_url():
    ds = PrestoDataSource({"host": "https://gw.example.net:9090", "user": "u", "catalog": "c", "schema": "s"})
    assert ds.connection_string() == "trino://u@gw.example.net:9090/c/s"


def test_presto_default_user_and_port():
    ds = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s"})
    assert ds.connection_string() == "trino://great_expectations@h:8080/c/s"


def test_presto_requires_catalog_schema():
    with pytest.raises(ValueError, match="missing required field"):
        PrestoDataSource({"host": "h"}).connection_string()


def test_presto_bearer_session_headers():
    ds = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s", "auth_token": "tok"})
    kwargs = ds.engine_kwargs()
    connect_args = kwargs["connect_args"]
    assert connect_args["http_scheme"] == "https"
    assert connect_args["max_attempts"] == 1
    session = connect_args["http_session"]
    assert session.headers["Authorization"] == "Bearer tok"


def test_presto_custom_header_raw_token():
    ds = PrestoDataSource(
        {"host": "h", "catalog": "c", "schema": "s", "auth_token": "tok", "auth_header": "X-Presto-Token"}
    )
    session = ds.engine_kwargs()["connect_args"]["http_session"]
    assert session.headers["X-Presto-Token"] == "tok"


def test_presto_no_token_no_session():
    ds = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s"})
    assert "http_session" not in ds.engine_kwargs()["connect_args"]


def test_presto_capabilities():
    caps = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s"}).capabilities()
    assert caps.dialect == "presto"
    assert caps.supports_pushdown is True


# --------------------------------------------------------------------------
# Snowflake connector
# --------------------------------------------------------------------------


def test_snowflake_connection_string():
    ds = SnowflakeDataSource(
        {
            "account": "xy12345",
            "user": "svc",
            "auth_token": "pw",
            "database": "ANALYTICS",
            "schema": "PUBLIC",
            "warehouse": "ETL_WH",
            "role": "ETL_ROLE",
        }
    )
    url = ds.connection_string()
    assert url.startswith("snowflake://svc:pw@xy12345/ANALYTICS/PUBLIC?")
    assert "warehouse=ETL_WH" in url
    assert "role=ETL_ROLE" in url


def test_snowflake_requires_account():
    with pytest.raises(ValueError, match="missing required field"):
        SnowflakeDataSource({"user": "u"}).connection_string()


def test_snowflake_describe_sql_dialect_specific():
    ds = SnowflakeDataSource({"account": "a"})
    assert ds.describe_sql("t") == "DESCRIBE TABLE t"


# --------------------------------------------------------------------------
# Shared execution machinery (exercised via sqlite)
# --------------------------------------------------------------------------


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


def test_execute_returns_dicts(tmp_path):
    db = tmp_path / "d.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE t (a INTEGER, b TEXT)")
    con.executemany("INSERT INTO t VALUES (?, ?)", [(1, "x"), (2, "y")])
    con.commit()
    con.close()

    ds = _SqliteSource({"path": str(db)})
    rows = ds.execute("SELECT a, b FROM t ORDER BY a")
    assert rows == [{"a": 1, "b": "x"}, {"a": 2, "b": "y"}]

    described = ds.describe("t")
    assert {r["name"] for r in described} == {"a", "b"}
    ds.dispose()


def test_execute_no_result_set_returns_empty(tmp_path):
    db = tmp_path / "d.db"
    ds = _SqliteSource({"path": str(db)})
    assert ds.execute("CREATE TABLE t (a INTEGER)") == []
    ds.dispose()


# --------------------------------------------------------------------------
# Connection config loading
# --------------------------------------------------------------------------


def test_load_connection_config_env_interpolation(monkeypatch, tmp_path):
    monkeypatch.setenv("MY_TOKEN", "secret")
    cfg = tmp_path / "conn.yml"
    cfg.write_text(
        "connection:\n"
        "  type: presto\n"
        "  host: h\n"
        "  catalog: c\n"
        "  schema: s\n"
        "  auth_token: ${MY_TOKEN}\n"
    )
    data = load_connection_config(cfg)
    assert data["type"] == "presto"
    assert data["auth_token"] == "secret"

    ds = create_data_source(data)
    session = ds.engine_kwargs()["connect_args"]["http_session"]
    assert session.headers["Authorization"] == "Bearer secret"

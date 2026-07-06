from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import great_expectations as gx
from great_expectations.data_context import AbstractDataContext
from great_expectations.datasource.fluent import SQLDatasource

# Reuse bcv_analyzer's connection helpers so GE's SQLAlchemy engine connects to Trino
# exactly the way the (working) reconciliation path does -- same host normalization,
# same https scheme, same bearer-token session. See reconciliation.py for the sys.path note.
_BCV_ANALYZER_DIR = Path(__file__).resolve().parents[2] / "BCV_analyzer"
if str(_BCV_ANALYZER_DIR) not in sys.path:
    sys.path.insert(0, str(_BCV_ANALYZER_DIR))

import bcv_analyzer  # noqa: E402


def get_context() -> AbstractDataContext:
    return gx.get_context(mode="ephemeral")


def build_trino_connection_string(host: str, port: int, user: str, catalog: str, schema: str) -> str:
    """trino:// URL for GE's SQLAlchemy engine, with host/port normalized the same way
    bcv_analyzer does.

    Critically, this strips any scheme (e.g. a `https://` accidentally passed in --host)
    and any embedded `:port` from the host before assembling the URL. Without this, a host
    like `https://gw:8080` produced `trino://user@https://gw:8080:8080/...`, which SQLAlchemy
    parses to an empty port -> `ValueError: invalid literal for int() with base 10: ''`.
    """
    normalized = bcv_analyzer.normalize_connection_kwargs(
        {"host": host, "port": port, "user": user, "catalog": catalog, "schema": schema}
    )
    return bcv_analyzer.build_engine_url(
        host=normalized["host"],
        port=normalized["port"],
        user=user,
        catalog=catalog,
        schema=schema,
    )


def build_engine_kwargs(connection_kwargs: dict[str, Any]) -> dict[str, Any]:
    """create_engine kwargs so GE's Trino engine speaks HTTPS with the bearer token.

    Mirrors bcv_analyzer.build_connect_args (http_scheme=https + an authenticated
    http_session), wrapped as {"connect_args": ...} which GE forwards to
    sqlalchemy.create_engine and, from there, to trino.dbapi.connect.
    """
    normalized = bcv_analyzer.normalize_connection_kwargs(connection_kwargs)
    return {"connect_args": bcv_analyzer.build_connect_args(normalized)}


def add_sql_datasource(
    context: AbstractDataContext,
    name: str,
    connection_string: str,
    engine_kwargs: dict[str, Any] | None = None,
) -> SQLDatasource:
    return context.data_sources.add_or_update_sql(
        name=name,
        connection_string=connection_string,
        kwargs=engine_kwargs or {},
    )

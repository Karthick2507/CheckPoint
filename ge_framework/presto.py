"""Presto/Trino connection helpers for the GE validation framework.

These mirror ``bcv_analyzer.py`` so both tools authenticate identically:

* the SQLAlchemy URL is ``trino://<user>@<host>:<port>/<catalog>/<schema>``, and
* the Bearer-token / custom-header auth is passed through ``connect_args``.

Great Expectations' Fluent ``add_sql(...)`` forwards its ``kwargs`` straight to
``sqlalchemy.create_engine``, so ``{"connect_args": build_connect_args(ds)}`` is
all that is needed to reach an authenticated gateway.
"""

from __future__ import annotations

from typing import Any

from ge_framework.config import DatasourceConfig


def build_connection_string(ds: DatasourceConfig) -> str:
    """Return the Trino SQLAlchemy URL for ``ds``."""
    return f"trino://{ds.user}@{ds.host}:{ds.port}/{ds.catalog}/{ds.schema}"


def build_http_headers(auth_token: str | None, auth_header: str | None) -> dict[str, str]:
    """Build auth headers, matching ``bcv_analyzer.build_http_headers``."""
    if not auth_token:
        return {}
    header_name = auth_header or "Authorization"
    if header_name.lower() == "authorization":
        return {header_name: f"Bearer {auth_token}"}
    return {header_name: auth_token}


def build_connect_args(ds: DatasourceConfig) -> dict[str, Any]:
    """Build the ``connect_args`` dict passed to ``create_engine``."""
    connect_args: dict[str, Any] = {
        "http_scheme": ds.http_scheme,
        "request_timeout": ds.request_timeout,
    }
    headers = build_http_headers(ds.auth_token, ds.auth_header)
    if headers:
        connect_args["http_headers"] = headers
    return connect_args


def build_engine_kwargs(ds: DatasourceConfig) -> dict[str, Any]:
    """Build the ``kwargs`` mapping for ``context.data_sources.add_sql``."""
    return {"connect_args": build_connect_args(ds)}

"""Presto / Trino connector.

Connection machinery:

* SQLAlchemy URL ``trino://<user>@<host>:<port>/<catalog>/<schema>``,
* host normalization via ``urlparse`` (accepts ``host:port`` or a full URL),
* Bearer-token auth carried on a ``requests.Session`` (``http_session``),
  ``http_scheme="https"``, ``request_timeout``, ``max_attempts=1``.

Config keys: ``host``, ``catalog``, ``schema`` (required); ``user``, ``port``,
``http_scheme``, ``request_timeout``, ``auth_token``, ``auth_header`` (optional).
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urlparse

from data_sources.base import Capabilities, DataSource
from data_sources.registry import register


@register("presto", "trino")
class PrestoDataSource(DataSource):
    def _host_and_port(self) -> tuple[str, int]:
        raw_host = str(self.config.get("host") or "").strip()
        port = int(self.config.get("port") or 8080)
        if not raw_host:
            return raw_host, port
        parsed = urlparse(raw_host if "://" in raw_host else f"https://{raw_host}")
        host = parsed.hostname or raw_host
        if parsed.port is not None:
            port = parsed.port
        return host, port

    def connection_string(self) -> str:
        self._require("host", "catalog", "schema")
        host, port = self._host_and_port()
        user = self.config.get("user") or "great_expectations"
        catalog = self.config["catalog"]
        schema = self.config["schema"]
        return f"trino://{user}@{host}:{port}/{catalog}/{schema}"

    def _http_headers(self) -> dict[str, str]:
        token = self.config.get("auth_token")
        if not token:
            return {}
        header_name = self.config.get("auth_header") or "Authorization"
        if header_name.lower() == "authorization":
            return {header_name: f"Bearer {token}"}
        return {header_name: token}

    def engine_kwargs(self) -> dict[str, Any]:
        connect_args: dict[str, Any] = {
            "http_scheme": self.config.get("http_scheme") or "https",
            "request_timeout": float(self.config.get("request_timeout") or 30.0),
            "max_attempts": 1,
        }
        headers = self._http_headers()
        if headers:
            import requests

            session = requests.Session()
            session.headers.update(headers)
            connect_args["http_session"] = session
        return {"connect_args": connect_args}

    def capabilities(self) -> Capabilities:
        # Trino/Presto over Hive-like connectors cannot roll back DML, so a
        # delete+insert load here is NOT atomic. Declared honestly so the loader
        # can flag it rather than silently pretend otherwise.
        return Capabilities(
            dialect="presto",
            supports_pushdown=True,
            identifier_quote='"',
            supports_transactions=False,
        )

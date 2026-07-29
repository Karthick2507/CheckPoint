"""Snowflake connector.

This proves the framework's multi-source design: Snowflake plugs in as a folder
+ a single ``@register`` line, and validates through the *same* Great
Expectations code path as Presto (GE is dialect-driven off the connection
string). It builds a ``snowflake://`` SQLAlchemy URL.

Executing against a live Snowflake additionally requires the
``snowflake-sqlalchemy`` driver (not in the base requirements). Until that is
installed the connector still constructs correct URLs/kwargs — it is the
extension point, ready to be exercised when a Snowflake source is onboarded.

Config keys: ``account`` (required); ``user``, ``auth_token``/``password``,
``database``/``catalog``, ``schema``, ``warehouse``, ``role`` (optional).
"""

from __future__ import annotations

from typing import Any
from urllib.parse import quote_plus, urlencode

from data_sources.base import Capabilities, DataSource
from data_sources.registry import register


@register("snowflake")
class SnowflakeDataSource(DataSource):
    def connection_string(self) -> str:
        self._require("account")
        account = self.config["account"]
        user = self.config.get("user") or ""
        password = self.config.get("auth_token") or self.config.get("password") or ""
        database = self.config.get("database") or self.config.get("catalog") or ""
        schema = self.config.get("schema") or ""

        credentials = ""
        if user:
            credentials = quote_plus(user)
            if password:
                credentials += f":{quote_plus(password)}"
            credentials += "@"

        url = f"snowflake://{credentials}{account}/{database}/{schema}"

        params = {}
        if self.config.get("warehouse"):
            params["warehouse"] = self.config["warehouse"]
        if self.config.get("role"):
            params["role"] = self.config["role"]
        if params:
            url += "?" + urlencode(params)
        return url

    def describe_sql(self, table: str) -> str:
        return f"DESCRIBE TABLE {table}"

    def capabilities(self) -> Capabilities:
        return Capabilities(dialect="snowflake", supports_pushdown=True, identifier_quote='"')

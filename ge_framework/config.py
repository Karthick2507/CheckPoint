"""Configuration models and YAML loaders for the GE validation framework.

Two YAML documents drive the framework:

* a **datasource** config describing how to reach the Presto/Trino gateway, and
* one or more **suite** configs describing an asset (table or query) and the
  expectations to run against it.

String values support ``${ENV_VAR}`` interpolation so secrets such as the auth
token never have to be written into the YAML file. A handful of datasource
fields also fall back to the same ``PRESTO_*`` environment variables that
``bcv_analyzer.py`` honours, keeping the two tools consistent.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

_ENV_PATTERN = re.compile(r"\$\{([^}]+)\}")


def _interpolate(value: Any) -> Any:
    """Recursively replace ``${VAR}`` tokens in strings with env-var values.

    An undefined variable resolves to an empty string, matching the tolerant
    behaviour of shell interpolation and letting optional fields stay unset.
    """
    if isinstance(value, str):
        return _ENV_PATTERN.sub(lambda m: os.environ.get(m.group(1), ""), value)
    if isinstance(value, list):
        return [_interpolate(item) for item in value]
    if isinstance(value, dict):
        return {key: _interpolate(item) for key, item in value.items()}
    return value


def _load_yaml(path: str | Path) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(text) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping at the top level of {path}")
    return _interpolate(data)


@dataclass
class DatasourceConfig:
    """How to connect to the Presto/Trino gateway.

    ``auth_token``/``auth_header`` mirror ``bcv_analyzer.build_http_headers``:
    when the header is ``Authorization`` the token is sent as a Bearer token,
    otherwise the raw token is sent under the custom header name.
    """

    name: str
    host: str
    catalog: str
    schema: str
    user: str = "great_expectations"
    port: int = 8080
    http_scheme: str = "https"
    request_timeout: float = 30.0
    auth_token: str | None = None
    auth_header: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DatasourceConfig":
        # Allow the config to omit fields and fall back to the PRESTO_* env
        # vars that bcv_analyzer already documents.
        host = data.get("host") or os.environ.get("PRESTO_HOST")
        user = data.get("user") or os.environ.get("PRESTO_USER") or "great_expectations"
        auth_token = data.get("auth_token") or os.environ.get("PRESTO_AUTH_TOKEN")
        auth_header = data.get("auth_header") or os.environ.get("PRESTO_AUTH_HEADER")
        port = data.get("port") or os.environ.get("PRESTO_PORT") or 8080

        missing = [f for f in ("host", "catalog", "schema") if not (data.get(f) or (f == "host" and host))]
        if missing:
            raise ValueError(f"Datasource config missing required field(s): {', '.join(missing)}")

        return cls(
            name=data.get("name") or "presto",
            host=str(host),
            catalog=str(data["catalog"]),
            schema=str(data["schema"]),
            user=str(user),
            port=int(port),
            http_scheme=str(data.get("http_scheme") or "https"),
            request_timeout=float(data.get("request_timeout") or 30.0),
            auth_token=auth_token or None,
            auth_header=auth_header or None,
        )


@dataclass
class AssetConfig:
    """The data to validate: a ``table`` asset or a ``query`` asset."""

    name: str
    type: str = "table"  # "table" | "query"
    table_name: str | None = None
    schema_name: str | None = None
    query: str | None = None
    batch: str = "whole_table"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AssetConfig":
        asset_type = str(data.get("type") or "table").lower()
        if asset_type not in ("table", "query"):
            raise ValueError(f"Unsupported asset type: {asset_type!r} (expected 'table' or 'query')")

        name = data.get("name")
        if not name:
            raise ValueError("Asset config requires a 'name'")

        if asset_type == "table" and not data.get("table_name"):
            raise ValueError("Table asset requires 'table_name'")
        if asset_type == "query" and not data.get("query"):
            raise ValueError("Query asset requires 'query'")

        return cls(
            name=str(name),
            type=asset_type,
            table_name=data.get("table_name"),
            schema_name=data.get("schema_name"),
            query=data.get("query"),
            batch=str(data.get("batch") or "whole_table"),
        )


@dataclass
class ExpectationConfig:
    """A single expectation: its snake_case ``type`` plus keyword arguments."""

    type: str
    kwargs: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ExpectationConfig":
        exp_type = data.get("type")
        if not exp_type:
            raise ValueError("Each expectation requires a 'type'")
        kwargs = {key: value for key, value in data.items() if key != "type"}
        return cls(type=str(exp_type), kwargs=kwargs)


@dataclass
class SuiteConfig:
    """A named expectation suite bound to an asset."""

    name: str
    asset: AssetConfig
    expectations: list[ExpectationConfig] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SuiteConfig":
        suite = data.get("suite") or {}
        name = suite.get("name") or data.get("name")
        if not name:
            raise ValueError("Suite config requires a 'suite.name'")

        asset_data = suite.get("asset") or data.get("asset")
        if not asset_data:
            raise ValueError("Suite config requires an 'asset' section")

        expectations = [ExpectationConfig.from_dict(item) for item in (data.get("expectations") or [])]
        if not expectations:
            raise ValueError("Suite config requires at least one entry under 'expectations'")

        return cls(
            name=str(name),
            asset=AssetConfig.from_dict(asset_data),
            expectations=expectations,
        )


def load_datasource_config(path: str | Path) -> DatasourceConfig:
    """Load a datasource config from a YAML file (``datasource:`` section)."""
    data = _load_yaml(path)
    return DatasourceConfig.from_dict(data.get("datasource") or data)


def load_suite_config(path: str | Path) -> SuiteConfig:
    """Load a suite config from a YAML file."""
    return SuiteConfig.from_dict(_load_yaml(path))

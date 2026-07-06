from __future__ import annotations

import great_expectations as gx
from great_expectations.data_context import AbstractDataContext
from great_expectations.datasource.fluent import SQLDatasource


def build_trino_connection_string(host: str, port: int, user: str, catalog: str, schema: str) -> str:
    """Same URL shape as bcv_analyzer.build_engine_url, so both tools connect identically."""
    return f"trino://{user}@{host}:{port}/{catalog}/{schema}"


def get_context() -> AbstractDataContext:
    return gx.get_context(mode="ephemeral")


def add_sql_datasource(context: AbstractDataContext, name: str, connection_string: str) -> SQLDatasource:
    return context.data_sources.add_or_update_sql(name=name, connection_string=connection_string)

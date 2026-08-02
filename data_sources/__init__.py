"""Pluggable data-source connectors for the ETL framework.

Importing this package registers the built-in connectors (Presto, Snowflake).
Downstream code only needs :func:`create_data_source` and the
:class:`DataSource` interface — never a concrete connector class.

    from data_sources import create_data_source, load_connection_config

    ds = create_data_source(load_connection_config("config/connections/mrm_presto.yml"))
    rows = ds.execute("SELECT 1")
"""

from data_sources.base import Capabilities, DataSource
from data_sources.config import load_connection_config, load_yaml
from data_sources.registry import available_sources, create_data_source, register

# Import connectors so their @register decorators populate the registry.
from data_sources.presto import PrestoDataSource  # noqa: E402,F401
from data_sources.snowflake import SnowflakeDataSource  # noqa: E402,F401
from data_sources.sqlite import SqliteDataSource  # noqa: E402,F401

__all__ = [
    "DataSource",
    "Capabilities",
    "create_data_source",
    "available_sources",
    "register",
    "load_connection_config",
    "load_yaml",
    "PrestoDataSource",
    "SnowflakeDataSource",
    "SqliteDataSource",
]

"""Registry / factory that maps a ``type`` string to a connector class.

Adding a new source is: create ``data_sources/<name>/connector.py``, decorate
the class with ``@register("<name>")``, and import it in
``data_sources/__init__.py`` so the decorator runs. Nothing else in the
framework needs to change.
"""

from __future__ import annotations

from typing import Any, Callable

from data_sources.base import DataSource

_REGISTRY: dict[str, type[DataSource]] = {}


def register(*source_types: str) -> Callable[[type[DataSource]], type[DataSource]]:
    """Class decorator registering a connector under one or more type names.

    The first name becomes the canonical ``type`` on the class; aliases (e.g.
    ``"trino"`` for the Presto connector) map to the same class.
    """
    if not source_types:
        raise ValueError("register() requires at least one source type name")

    def decorator(cls: type[DataSource]) -> type[DataSource]:
        cls.type = source_types[0]
        for name in source_types:
            _REGISTRY[name.lower()] = cls
        return cls

    return decorator


def available_sources() -> list[str]:
    """Return the sorted list of registered source type names."""
    return sorted(_REGISTRY)


def create_data_source(config: dict[str, Any]) -> DataSource:
    """Instantiate the connector named by ``config['type']``."""
    source_type = str(config.get("type") or "").lower()
    if not source_type:
        raise ValueError("Connection config requires a 'type' (e.g. 'presto', 'snowflake')")
    connector_cls = _REGISTRY.get(source_type)
    if connector_cls is None:
        raise ValueError(
            f"Unknown data source type {source_type!r}. "
            f"Available: {', '.join(available_sources()) or '(none registered)'}"
        )
    return connector_cls(config)

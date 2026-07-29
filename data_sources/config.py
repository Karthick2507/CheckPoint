"""Loader for connection YAML configs, with ``${ENV_VAR}`` interpolation.

Secrets (tokens, passwords) live in the environment and are referenced as
``${VAR}`` in the YAML, so credentials never sit in the config files.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

import yaml

_ENV_PATTERN = re.compile(r"\$\{([^}]+)\}")


def interpolate_env(value: Any) -> Any:
    """Recursively replace ``${VAR}`` tokens in strings with env-var values."""
    if isinstance(value, str):
        return _ENV_PATTERN.sub(lambda m: os.environ.get(m.group(1), ""), value)
    if isinstance(value, list):
        return [interpolate_env(item) for item in value]
    if isinstance(value, dict):
        return {key: interpolate_env(item) for key, item in value.items()}
    return value


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML mapping with env interpolation applied."""
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping at the top level of {path}")
    return interpolate_env(data)


def load_connection_config(path: str | Path) -> dict[str, Any]:
    """Load a connection config; accepts a top-level ``connection:`` section."""
    data = load_yaml(path)
    return data.get("connection") or data

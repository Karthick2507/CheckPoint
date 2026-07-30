"""SQL templating for pipeline configs.

Pipeline SQL needs the run's identity — above all the batch being processed::

    SELECT ... FROM request WHERE process_batch_id = '{{ batch_id }}'

Rendering is deliberately strict and sandboxed:

* **StrictUndefined** — an unknown placeholder raises instead of rendering an
  empty string. Silently shipping ``WHERE process_batch_id = ''`` to a warehouse
  would return nothing and look like a legitimately empty batch.
* **SandboxedEnvironment** — templates come from config files, so they must not
  be able to reach into Python objects.

Available variables: ``batch_id``, ``run_id``, ``pipeline``, ``env``, plus
anything under the pipeline's ``vars:`` block.
"""

from __future__ import annotations

from typing import Any

from jinja2 import StrictUndefined
from jinja2.exceptions import TemplateError, UndefinedError
from jinja2.sandbox import SandboxedEnvironment

_ENV = SandboxedEnvironment(undefined=StrictUndefined, autoescape=False)


class TemplateRenderError(ValueError):
    """Raised when a SQL template references an unknown variable or is invalid."""


def render_sql(sql: str, context: dict[str, Any]) -> str:
    """Render ``sql`` against ``context``.

    Returns the input unchanged when it contains no template markers, so plain
    SQL never pays the parsing cost or risks a spurious template error.
    """
    if not sql or ("{{" not in sql and "{%" not in sql):
        return sql
    try:
        return _ENV.from_string(sql).render(**context)
    except UndefinedError as exc:
        available = ", ".join(sorted(context)) or "(none)"
        raise TemplateRenderError(
            f"SQL template references an undefined variable: {exc.message}. Available: {available}"
        ) from exc
    except TemplateError as exc:
        raise TemplateRenderError(f"Invalid SQL template: {exc}") from exc


def render_all(statements: list[str], context: dict[str, Any]) -> list[str]:
    """Render a list of SQL statements against ``context``."""
    return [render_sql(statement, context) for statement in statements]

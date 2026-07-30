"""Shared SQL primitives.

Lives in ``runtime`` because both ``core`` and ``quality`` need these, and both
already depend on ``runtime``. Consolidating them here also removes the three
divergent copies of ``sql_literal`` that had accumulated across the extract,
load, and validation layers.
"""

from __future__ import annotations

import math
from typing import Any


def sql_literal(value: Any) -> str:
    """Render ``value`` as a SQL literal.

    Non-finite floats become NULL: ``nan``/``inf`` are not valid SQL and would
    otherwise be emitted verbatim, producing a syntax error mid-load.
    """
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return "NULL"
        return repr(value)
    if isinstance(value, int):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def build_batch_predicate(
    batch_key: str | None,
    batch_id: Any,
    batch_filter: str | None = None,
    template_context: dict[str, Any] | None = None,
) -> str | None:
    """Return a WHERE predicate restricting a table to one batch.

    ``batch_filter`` wins when supplied and is rendered with the run's template
    variables; otherwise a simple ``<batch_key> = <batch_id>`` equality is used.
    Returns ``None`` when neither is configured (i.e. no scoping requested).
    """
    if batch_filter:
        from runtime.templating import render_sql

        return render_sql(batch_filter, template_context or {})
    if batch_key:
        return f"{batch_key} = {sql_literal(batch_id)}"
    return None


def where_clause(predicate: str | None) -> str:
    """`` WHERE <predicate>`` or an empty string."""
    return f" WHERE {predicate}" if predicate else ""

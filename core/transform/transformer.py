"""Transform stage — ELT: transformations expressed as SQL run on the source.

``steps`` is an ordered list of SQL statements. All but the last are executed as
setup DDL (e.g. ``CREATE OR REPLACE VIEW``); the **last** statement is the
curated ``SELECT`` whose result set is the transform output. Keeping compute in
the warehouse is the scalable default at TiB scale.

The curated SELECT is also returned as ``sql`` so a validation gate can wrap it
as a GE query asset (validate the transformed data, not just the raw source).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from data_sources.base import DataSource


@dataclass
class TransformResult:
    rows: list[dict[str, Any]] = field(default_factory=list)
    sql: str = ""
    row_count: int = 0
    applied: bool = False


class Transformer:
    def apply(self, source: DataSource, steps: list[str]) -> TransformResult:
        """Run ``steps`` on ``source``; return the last SELECT's result set."""
        steps = [s for s in (steps or []) if s and s.strip()]
        if not steps:
            return TransformResult(applied=False)

        for setup_sql in steps[:-1]:
            source.execute(setup_sql)  # DDL / setup, no result set expected

        curated_sql = steps[-1]
        rows = source.execute(curated_sql)
        return TransformResult(rows=rows, sql=curated_sql, row_count=len(rows), applied=True)

    def prepare(self, source: DataSource, steps: list[str]) -> str | None:
        """Run the setup steps and return the curated SELECT *without* running it.

        Used by the pushdown path: the final SELECT is not executed here, it is
        embedded into an ``INSERT … SELECT`` so the warehouse never ships rows
        back to the framework.
        """
        steps = [s for s in (steps or []) if s and s.strip()]
        if not steps:
            return None
        for setup_sql in steps[:-1]:
            source.execute(setup_sql)
        return steps[-1]

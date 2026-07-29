"""Extract rows from a source, with optional incremental batch filtering.

The extractor builds and runs the source SELECT and returns rows plus the SQL it
issued (kept for lineage / reports). Incremental mode filters on the table's
``batch_key`` equal to the run's ``batch_id`` — aligning with the Presto batch
partitioning the tables already use.

For TiB-scale in-warehouse ELT you would push down (INSERT ... SELECT) rather
than pull rows into memory; the row-based path here powers cross-source moves
and is what the tests exercise.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from data_sources.base import DataSource


@dataclass
class ExtractResult:
    rows: list[dict[str, Any]] = field(default_factory=list)
    sql: str = ""
    row_count: int = 0


def _sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


class Extractor:
    """Reads from a table (with optional incremental filter) or a raw query."""

    def build_table_sql(
        self,
        table: str,
        batch_key: str | None = None,
        batch_id: str | None = None,
        incremental: bool = False,
        limit: int | None = None,
    ) -> str:
        sql = f"SELECT * FROM {table}"
        if incremental:
            if not batch_key:
                raise ValueError("incremental extract requires a source 'batch_key'")
            sql += f" WHERE {batch_key} = {_sql_literal(batch_id)}"
        if limit:
            sql += f" LIMIT {int(limit)}"
        return sql

    def extract(
        self,
        source: DataSource,
        table: str | None = None,
        query: str | None = None,
        batch_key: str | None = None,
        batch_id: str | None = None,
        incremental: bool = False,
        limit: int | None = None,
    ) -> ExtractResult:
        if query:
            sql = query
        elif table:
            sql = self.build_table_sql(table, batch_key, batch_id, incremental, limit)
        else:
            raise ValueError("extract requires either 'table' or 'query'")
        rows = source.execute(sql)
        return ExtractResult(rows=rows, sql=sql, row_count=len(rows))

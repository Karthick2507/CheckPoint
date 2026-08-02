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
from typing import Any, Iterator

from data_sources.base import DataSource

DEFAULT_CHUNK_SIZE = 10_000


@dataclass
class ExtractResult:
    rows: list[dict[str, Any]] = field(default_factory=list)
    sql: str = ""
    row_count: int = 0


from runtime.sql import sql_literal as _sql_literal  # single shared implementation


class Extractor:
    """Reads from a table (with optional incremental filter) or a raw query."""

    def build_table_sql(
        self,
        table: str,
        batch_key: str | None = None,
        batch_id: str | None = None,
        incremental: bool = False,
        limit: int | None = None,
        projection: str = "*",
    ) -> str:
        """Build the source SELECT.

        ``projection`` comes from the pipeline's schema contract; it is ``*``
        only when no contract is declared, which leaves the pipeline exposed to
        upstream column drift.
        """
        sql = f"SELECT {projection} FROM {table}"
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

    def stream(
        self,
        source: DataSource,
        table: str | None = None,
        query: str | None = None,
        batch_key: str | None = None,
        batch_id: str | None = None,
        incremental: bool = False,
        limit: int | None = None,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
    ) -> tuple[str, Iterator[list[dict[str, Any]]]]:
        """Return the SQL and a generator yielding row chunks.

        Memory stays bounded by ``chunk_size`` rather than by the result set,
        which is what makes a large cross-system move survivable.
        """
        if query:
            sql = query
        elif table:
            sql = self.build_table_sql(table, batch_key, batch_id, incremental, limit)
        else:
            raise ValueError("extract requires either 'table' or 'query'")
        return sql, source.stream(sql, chunk_size=chunk_size)

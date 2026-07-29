"""Load stage — write rows into a target table.

Modes:

* ``append``    — insert rows as-is.
* ``overwrite`` — ``DELETE FROM target`` then insert.
* ``merge``     — delete rows whose key(s) match incoming rows, then insert
                  (delete+insert upsert; supports single or composite keys).
* ``none``      — skip loading (validation-only pipelines).

Rows are written as batched ``INSERT ... VALUES`` with SQL-literal escaping, so
the loader works across dialects and, crucially, **across sources** (e.g. Presto
to Snowflake). For very large in-warehouse loads, an ``INSERT ... SELECT``
pushdown is the scale path; this row-based loader targets cross-source moves and
is what the tests exercise.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from data_sources.base import DataSource

_INSERT_BATCH = 500


@dataclass
class LoadResult:
    target: str
    mode: str
    inserted: int
    deleted: int = 0


def sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


class Loader:
    def load(
        self,
        target: DataSource,
        table: str,
        rows: Sequence[dict[str, Any]],
        mode: str = "append",
        keys: Sequence[str] | None = None,
    ) -> LoadResult:
        mode = (mode or "append").lower()
        if mode == "none":
            return LoadResult(target=table, mode=mode, inserted=0)

        deleted = 0
        if mode == "overwrite":
            target.execute(f"DELETE FROM {table}")
        elif mode == "merge":
            deleted = self._delete_matching(target, table, rows, keys)
        elif mode != "append":
            raise ValueError(f"Unsupported load mode: {mode!r}")

        inserted = self._insert(target, table, rows)
        return LoadResult(target=table, mode=mode, inserted=inserted, deleted=deleted)

    # -- internals -------------------------------------------------------

    def _delete_matching(
        self,
        target: DataSource,
        table: str,
        rows: Sequence[dict[str, Any]],
        keys: Sequence[str] | None,
    ) -> int:
        if not rows:
            return 0
        if not keys:
            raise ValueError("merge load mode requires 'keys'")
        deleted = 0
        for batch in _chunks(rows, _INSERT_BATCH):
            conditions = []
            for row in batch:
                clause = " AND ".join(f"{key} = {sql_literal(row.get(key))}" for key in keys)
                conditions.append(f"({clause})")
            where = " OR ".join(conditions)
            result = target.execute(f"DELETE FROM {table} WHERE {where}")
            deleted += 0  # row count not reliably returned across DBAPIs
            del result
        return deleted

    def _insert(self, target: DataSource, table: str, rows: Sequence[dict[str, Any]]) -> int:
        if not rows:
            return 0
        columns = list(rows[0].keys())
        col_list = ", ".join(columns)
        inserted = 0
        for batch in _chunks(rows, _INSERT_BATCH):
            values_sql = ", ".join(
                "(" + ", ".join(sql_literal(row.get(col)) for col in columns) + ")" for row in batch
            )
            target.execute(f"INSERT INTO {table} ({col_list}) VALUES {values_sql}")
            inserted += len(batch)
        return inserted


def _chunks(seq: Sequence[Any], size: int):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]

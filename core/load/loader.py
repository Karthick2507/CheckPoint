"""Load stage — write rows into a target table.

Modes:

* ``append``    — insert rows as-is.
* ``overwrite`` — ``DELETE FROM target`` then insert.
* ``merge``     — delete rows whose key(s) match incoming rows, then insert
                  (delete+insert upsert; supports single or composite keys).
* ``none``      — skip loading (validation-only pipelines).

**Empty-payload guard.** ``overwrite`` and ``merge`` are destructive: they delete
before they insert. If the payload is empty — a late or missing upstream batch,
a transform that filtered everything out, a failed extract — deleting would wipe
the target and replace it with nothing. Such a load is therefore **skipped** and
reported as ``skipped_empty``. Set ``allow_empty=True`` (config: ``allow_empty:
true``) to opt into a deliberate "truncate to empty" load.

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


DESTRUCTIVE_MODES = ("overwrite", "merge")


@dataclass
class LoadResult:
    target: str
    mode: str
    inserted: int
    deleted: int = 0
    skipped: bool = False
    reason: str = ""


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
        allow_empty: bool = False,
    ) -> LoadResult:
        mode = (mode or "append").lower()
        if mode == "none":
            return LoadResult(target=table, mode=mode, inserted=0, skipped=True, reason="mode is 'none'")

        # Refuse to delete when there is nothing to put back (see module docstring).
        if not rows and mode in DESTRUCTIVE_MODES and not allow_empty:
            return LoadResult(
                target=table,
                mode=mode,
                inserted=0,
                skipped=True,
                reason=(
                    f"refused to run destructive '{mode}' load with an empty payload "
                    f"(would delete {table} and insert nothing); set allow_empty: true to override"
                ),
            )

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

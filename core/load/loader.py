"""Load stage — write rows into a target table.

Modes:

* ``append``    — insert rows as-is.
* ``overwrite`` — ``DELETE FROM target`` then insert.
* ``merge``     — delete rows whose key(s) match incoming rows, then insert
                  (delete+insert upsert; supports single or composite keys).
* ``none``      — skip loading (validation-only pipelines).

**Atomicity.** The delete and the insert of a destructive load run inside a
single transaction (:meth:`DataSource.transaction`), so a failure part-way
rolls back rather than leaving the target with rows deleted and nothing put
back. Sources that cannot roll back (Trino/Presto over Hive-like connectors)
declare ``supports_transactions=False``; the load still runs but is reported
with ``atomic=False`` so the operator knows the guarantee did not apply.

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
from typing import Any, Iterable, Sequence

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
    # False when the source cannot roll back, i.e. a mid-load failure could
    # leave the target partially written. Surfaced in the run report.
    atomic: bool = True


# Single shared implementation (also handles NaN/Inf, which the old local copy
# emitted verbatim and broke the INSERT).
from runtime.sql import sql_literal  # noqa: E402


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

        if mode not in ("append",) + DESTRUCTIVE_MODES:
            raise ValueError(f"Unsupported load mode: {mode!r}")
        if mode == "merge" and rows and not keys:
            raise ValueError("merge load mode requires 'keys'")

        atomic = bool(target.capabilities().supports_transactions)

        # Delete and insert must land together: a failure between them would
        # otherwise delete rows and never put them back.
        with target.transaction() as tx:
            deleted = 0
            if mode == "overwrite":
                tx.execute(f"DELETE FROM {table}")
            elif mode == "merge":
                deleted = self._delete_matching(tx, table, rows, keys)
            inserted = self._insert(tx, table, rows)

        return LoadResult(
            target=table,
            mode=mode,
            inserted=inserted,
            deleted=deleted,
            atomic=atomic,
            reason=(
                ""
                if atomic
                else f"target does not support transactions; '{mode}' load was not atomic"
            ),
        )

    def load_stream(
        self,
        target: DataSource,
        table: str,
        chunks: Iterable[Sequence[dict[str, Any]]],
        mode: str = "append",
    ) -> LoadResult:
        """Append row chunks as they arrive, never holding the full set.

        Pairs with :meth:`Extractor.stream` for cross-system moves that are too
        large to materialize. Only ``append`` is supported: a destructive mode
        would have to delete before knowing whether the stream yields anything,
        which is exactly the empty-payload hazard P0-1 guards against.
        """
        mode = (mode or "append").lower()
        if mode != "append":
            raise ValueError(
                f"streaming load supports only 'append' (got {mode!r}); "
                "use the pushdown loader for large destructive loads"
            )

        atomic = bool(target.capabilities().supports_transactions)
        inserted = 0
        with target.transaction() as tx:
            for chunk in chunks:
                if not chunk:
                    continue
                inserted += self._insert(tx, table, chunk)

        return LoadResult(
            target=table,
            mode=mode,
            inserted=inserted,
            atomic=atomic,
            reason="" if atomic else "target does not support transactions; streamed load was not atomic",
        )

    # -- internals (operate on a Transaction, not the DataSource) ---------

    def _delete_matching(
        self,
        tx: Any,
        table: str,
        rows: Sequence[dict[str, Any]],
        keys: Sequence[str] | None,
    ) -> int:
        if not rows or not keys:
            return 0
        deleted = 0
        for batch in _chunks(rows, _INSERT_BATCH):
            conditions = []
            for row in batch:
                clause = " AND ".join(f"{key} = {sql_literal(row.get(key))}" for key in keys)
                conditions.append(f"({clause})")
            where = " OR ".join(conditions)
            tx.execute(f"DELETE FROM {table} WHERE {where}")
            deleted += len(batch)  # keys targeted for replacement
        return deleted

    def _insert(self, tx: Any, table: str, rows: Sequence[dict[str, Any]]) -> int:
        if not rows:
            return 0
        columns = list(rows[0].keys())
        col_list = ", ".join(columns)
        inserted = 0
        for batch in _chunks(rows, _INSERT_BATCH):
            values_sql = ", ".join(
                "(" + ", ".join(sql_literal(row.get(col)) for col in columns) + ")" for row in batch
            )
            tx.execute(f"INSERT INTO {table} ({col_list}) VALUES {values_sql}")
            inserted += len(batch)
        return inserted


def _chunks(seq: Sequence[Any], size: int):
    for i in range(0, len(seq), size):
        yield seq[i : i + size]

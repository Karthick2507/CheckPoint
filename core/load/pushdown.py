"""Pushdown load — ``INSERT INTO target SELECT …`` executed in the warehouse.

The row-based :class:`~core.load.loader.Loader` reads every row into Python and
writes it back as ``INSERT … VALUES``. That is necessary to move data *between*
systems (Presto → Snowflake), but it is the wrong tool when source and target
live in the same warehouse: at TiB scale it will not finish, and it burns
memory proportional to the result set.

This loader keeps the data where it is. The transform SQL becomes the SELECT of
an ``INSERT … SELECT``, so the warehouse does the work and the framework only
issues statements. Cost is independent of row count.

Requires the source and target to be the **same** connection (the warehouse has
to be able to see both sides of the statement); the pipeline verifies that
before choosing this path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from data_sources.base import DataSource


@dataclass
class PushdownResult:
    """Outcome of a pushdown load. Row counts come from the warehouse."""

    target: str
    mode: str
    statements: list[str]
    inserted: int | None = None  # None when the source cannot report it
    skipped: bool = False
    reason: str = ""
    atomic: bool = True

    # Keep the shape compatible with LoadResult for reporting/manifest.
    @property
    def deleted(self) -> int:
        return 0


def _strip_trailing_semicolon(sql: str) -> str:
    return sql.strip().rstrip(";").strip()


class PushdownLoader:
    """Executes set-based loads without materializing rows in Python."""

    def build_statements(
        self,
        table: str,
        select_sql: str,
        mode: str = "append",
        keys: Sequence[str] | None = None,
        columns: Sequence[str] | None = None,
    ) -> list[str]:
        """Build the statement sequence for a pushdown load."""
        select_sql = _strip_trailing_semicolon(select_sql)
        column_clause = f" ({', '.join(columns)})" if columns else ""
        statements: list[str] = []

        if mode == "overwrite":
            statements.append(f"DELETE FROM {table}")
        elif mode == "merge":
            if not keys:
                raise ValueError("pushdown merge requires 'keys'")
            # Delete the keys the incoming set will replace, computed by the
            # warehouse from the same SELECT — no keys round-trip through Python.
            key_tuple = ", ".join(keys)
            statements.append(
                f"DELETE FROM {table} WHERE ({key_tuple}) IN "
                f"(SELECT {key_tuple} FROM ({select_sql}) AS _incoming)"
            )
        elif mode != "append":
            raise ValueError(f"Unsupported pushdown load mode: {mode!r}")

        statements.append(f"INSERT INTO {table}{column_clause} {select_sql}")
        return statements

    def count_sql(self, select_sql: str) -> str:
        """SQL counting the rows the SELECT would produce."""
        return f"SELECT COUNT(*) AS n FROM ({_strip_trailing_semicolon(select_sql)}) AS _c"

    def load(
        self,
        source: DataSource,
        table: str,
        select_sql: str,
        mode: str = "append",
        keys: Sequence[str] | None = None,
        columns: Sequence[str] | None = None,
        allow_empty: bool = False,
        count_rows: bool = True,
    ) -> PushdownResult:
        """Run the pushdown load against ``source`` (which also hosts the target)."""
        mode = (mode or "append").lower()
        if mode == "none":
            return PushdownResult(
                target=table, mode=mode, statements=[], inserted=0, skipped=True, reason="mode is 'none'"
            )

        atomic = bool(source.capabilities().supports_transactions)

        # Same empty-payload guard as the row-based loader: never delete when
        # the incoming set is empty unless that is explicitly intended.
        inserted: int | None = None
        if count_rows:
            rows = source.execute(self.count_sql(select_sql))
            inserted = int(rows[0]["n"]) if rows else 0
            if inserted == 0 and mode in ("overwrite", "merge") and not allow_empty:
                return PushdownResult(
                    target=table,
                    mode=mode,
                    statements=[],
                    inserted=0,
                    skipped=True,
                    reason=(
                        f"refused to run destructive '{mode}' pushdown with an empty result set "
                        f"(would delete {table} and insert nothing); set allow_empty: true to override"
                    ),
                )

        statements = self.build_statements(table, select_sql, mode=mode, keys=keys, columns=columns)
        with source.transaction() as tx:
            for statement in statements:
                tx.execute(statement)

        return PushdownResult(
            target=table,
            mode=mode,
            statements=statements,
            inserted=inserted,
            atomic=atomic,
            reason="" if atomic else f"target does not support transactions; '{mode}' load was not atomic",
        )

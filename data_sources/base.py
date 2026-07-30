"""The ``DataSource`` contract every connector obeys.

A data source is anything the ETL framework can read from or write to via a
SQLAlchemy dialect. Concrete connectors (Presto, Snowflake, ...) only have to
supply a ``connection_string`` and, if needed, ``engine_kwargs`` (auth); the
shared ``execute``/``describe`` machinery here does the rest.

This is the seam that makes the framework source-agnostic: every other layer
(extract, validate, transform, load) depends on this interface, never on a
specific database.
"""

from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Iterator


@dataclass
class Capabilities:
    """What a source can do, so higher layers can adapt (e.g. ELT pushdown)."""

    dialect: str
    supports_pushdown: bool = True
    identifier_quote: str = '"'
    # Whether multi-statement work can be made atomic. Warehouses such as
    # Trino/Presto (over Hive-like connectors) cannot roll back a DELETE, so
    # callers must be told when atomicity is unavailable rather than assume it.
    supports_transactions: bool = True


_READ_PREFIXES = ("select", "with", "describe", "show", "explain", "pragma")


def _looks_like_read(sql: str) -> bool:
    """Whether ``sql`` is safe to re-issue after a transient failure.

    Only read statements qualify: re-running a partially applied INSERT or
    DELETE could duplicate or double-delete rows. Anything unrecognised is
    treated as a write, which is the safe default.
    """
    statement = (sql or "").lstrip().lstrip("(").lstrip()
    # Skip leading SQL comments so a commented query is still classified.
    while statement.startswith("--"):
        _, _, statement = statement.partition("\n")
        statement = statement.lstrip()
    return statement[:8].lower().startswith(_READ_PREFIXES)


class Transaction:
    """Runs statements on a single connection inside one transaction."""

    def __init__(self, cursor: Any) -> None:
        self._cursor = cursor
        self.statements: list[str] = []

    def execute(self, sql: str) -> list[dict[str, Any]]:
        self.statements.append(sql)
        self._cursor.execute(sql)
        if self._cursor.description is None:
            return []
        columns = [column[0] for column in self._cursor.description]
        return [dict(zip(columns, row)) for row in self._cursor.fetchall()]


class DataSource(ABC):
    """Abstract base for all connectors.

    Subclasses set their registry key via ``@register(...)`` and implement
    ``connection_string``. Everything else has a working default.
    """

    type: str = "base"

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = dict(config or {})
        self.name = self.config.get("name") or self.type
        self._engine: Any = None
        self._retry_policy: Any = None

    # -- required of every source ----------------------------------------

    @abstractmethod
    def connection_string(self) -> str:
        """Return the SQLAlchemy URL for this source."""

    def engine_kwargs(self) -> dict[str, Any]:
        """Extra kwargs for ``create_engine`` (e.g. ``connect_args`` for auth)."""
        return {}

    def capabilities(self) -> Capabilities:
        """Describe dialect quirks; override for source-specific behaviour."""
        return Capabilities(dialect=self.type)

    # -- shared engine / execution ---------------------------------------

    def get_engine(self) -> Any:
        """Lazily create and cache a SQLAlchemy engine for this source."""
        if self._engine is None:
            from sqlalchemy import create_engine

            self._engine = create_engine(self.connection_string(), **self.engine_kwargs())
        return self._engine

    # -- retry policy ------------------------------------------------------

    @property
    def retry_policy(self) -> Any:
        """Retry policy for transient failures, from connection config."""
        from runtime.retry import RetryPolicy

        if self._retry_policy is None:
            self._retry_policy = RetryPolicy(
                attempts=int(self.config.get("retry_attempts") or 3),
                initial_delay=float(self.config.get("retry_initial_delay") or 1.0),
                max_delay=float(self.config.get("retry_max_delay") or 30.0),
            )
        return self._retry_policy

    def execute(self, sql: str, retry: bool | None = None) -> list[dict[str, Any]]:
        """Run ``sql`` and return rows as a list of dicts.

        Transient failures (gateway blips, dropped sockets, timeouts) are
        retried with exponential backoff. **Reads retry; writes do not** unless
        ``retry=True`` is passed explicitly — re-issuing a statement that may
        have partially applied is how duplicate rows get created. A query whose
        failure is permanent (missing table, syntax error) is never retried.
        """
        from runtime.retry import with_retry

        should_retry = _looks_like_read(sql) if retry is None else retry
        if not should_retry:
            return self._execute_once(sql)
        return with_retry(
            lambda: self._execute_once(sql),
            policy=self.retry_policy,
            description=f"query on {self.name}",
            on_retry=self._log_retry,
        )

    def _log_retry(self, attempt: int, exc: BaseException, delay: float) -> None:
        print(
            f"[{self.name}] transient failure on attempt {attempt} "
            f"({type(exc).__name__}: {exc}); retrying in {delay:.1f}s",
            file=sys.stderr,
        )

    def _execute_once(self, sql: str) -> list[dict[str, Any]]:
        engine = self.get_engine()
        connection = engine.raw_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            if cursor.description is None:
                # DML/DDL (INSERT/DELETE/CREATE ...): commit so writes persist.
                connection.commit()
                return []
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()
            # Read paths need no commit; closing releases the connection.
            return [dict(zip(columns, row)) for row in rows]
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as exc:  # pragma: no cover - defensive cleanup
                    print(f"Warning: failed to close cursor cleanly: {exc}", file=sys.stderr)
            try:
                connection.close()
            except Exception as exc:  # pragma: no cover - defensive cleanup
                print(f"Warning: failed to close connection cleanly: {exc}", file=sys.stderr)

    def stream(self, sql: str, chunk_size: int = 10_000) -> Iterator[list[dict[str, Any]]]:
        """Yield result rows in chunks instead of materializing them all.

        ``execute`` calls ``fetchall``, so memory grows with the result set —
        fine for a DESCRIBE, fatal for a large extract. This uses ``fetchmany``
        so a cross-system move stays bounded regardless of table size.

        The connection stays open for the life of the generator; callers should
        consume it promptly (``close()`` the generator to release early).
        """
        engine = self.get_engine()
        connection = engine.raw_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            if cursor.description is None:
                return
            columns = [column[0] for column in cursor.description]
            while True:
                rows = cursor.fetchmany(chunk_size)
                if not rows:
                    break
                yield [dict(zip(columns, row)) for row in rows]
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as exc:  # pragma: no cover - defensive cleanup
                    print(f"Warning: failed to close cursor cleanly: {exc}", file=sys.stderr)
            try:
                connection.close()
            except Exception as exc:  # pragma: no cover - defensive cleanup
                print(f"Warning: failed to close connection cleanly: {exc}", file=sys.stderr)

    @contextmanager
    def transaction(self) -> Iterator[Transaction]:
        """Run several statements atomically on one connection.

        Commits on clean exit; rolls back and re-raises on any exception. On
        sources that cannot roll back (see ``Capabilities.supports_transactions``)
        the rollback is best-effort — callers should consult the capability and
        report when atomicity could not be guaranteed.
        """
        engine = self.get_engine()
        connection = engine.raw_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            tx = Transaction(cursor)
            try:
                yield tx
                connection.commit()
            except Exception:
                try:
                    connection.rollback()
                except Exception as exc:  # pragma: no cover - source cannot roll back
                    print(f"Warning: rollback failed ({exc}); target may be inconsistent", file=sys.stderr)
                raise
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as exc:  # pragma: no cover - defensive cleanup
                    print(f"Warning: failed to close cursor cleanly: {exc}", file=sys.stderr)
            try:
                connection.close()
            except Exception as exc:  # pragma: no cover - defensive cleanup
                print(f"Warning: failed to close connection cleanly: {exc}", file=sys.stderr)

    # -- schema introspection --------------------------------------------

    def describe_sql(self, table: str) -> str:
        """SQL to describe a table's columns. Override per dialect if needed."""
        return f"DESCRIBE {table}"

    def describe(self, table: str) -> list[dict[str, Any]]:
        """Return the column metadata rows for ``table``."""
        return self.execute(self.describe_sql(table))

    def dispose(self) -> None:
        """Dispose of the cached engine and its connection pool."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None

    def _require(self, *keys: str) -> None:
        """Raise a clear error if any required config key is missing."""
        missing = [key for key in keys if not self.config.get(key)]
        if missing:
            raise ValueError(
                f"{self.type} connection config missing required field(s): {', '.join(missing)}"
            )

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"<{self.__class__.__name__} name={self.name!r} type={self.type!r}>"

"""SQLite connector — zero-infrastructure local runs.

Not a warehouse, but genuinely useful: it lets anyone run a complete pipeline
(extract, transform, all three validation gates, the custom checks, load,
reporting) on a laptop with nothing installed beyond this package. The
quick-start in the README uses it, and the test-suite drives the whole framework
through it.

Config keys: ``path`` (required) — the database file; ``:memory:`` also works,
though state written to an in-memory database vanishes with the process.
"""

from __future__ import annotations

from data_sources.base import Capabilities, DataSource
from data_sources.registry import register


@register("sqlite")
class SqliteDataSource(DataSource):
    def connection_string(self) -> str:
        self._require("path")
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        # sqlite has no DESCRIBE; PRAGMA returns name/type columns, which
        # quality.base.normalize_columns already understands.
        return f"PRAGMA table_info({table})"

    def capabilities(self) -> Capabilities:
        return Capabilities(
            dialect="sqlite",
            supports_pushdown=True,
            identifier_quote='"',
            supports_transactions=True,
        )

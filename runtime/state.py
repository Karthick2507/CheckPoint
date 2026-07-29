"""File-based state store for the stateful quality checks.

"Files only" (no results DB), so baselines live under ``etl_output/state/``:

    state/
    ├── schema_snapshots/<source>__<table>.json   # last-seen columns (schema-drift)
    └── row_count_history/<source>__<table>.csv    # row counts over time (volume-drift)

Keeping these as flat files makes them trivially inspectable, diff-able, and
commit-able if a team wants to pin an approved baseline.
"""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

_HISTORY_FIELDS = ("timestamp", "run_id", "batch_id", "row_count")


def _slug(source: str, table: str) -> str:
    return _SAFE.sub("_", f"{source}__{table}")


class FileState:
    """Persist and read back baselines used by stateful quality checks."""

    def __init__(self, state_dir: str | Path) -> None:
        self.state_dir = Path(state_dir)
        self.schema_dir = self.state_dir / "schema_snapshots"
        self.rowcount_dir = self.state_dir / "row_count_history"

    # -- schema snapshots (schema-drift) ---------------------------------

    def _schema_path(self, source: str, table: str) -> Path:
        return self.schema_dir / f"{_slug(source, table)}.json"

    def save_schema_snapshot(self, source: str, table: str, columns: list[dict[str, Any]]) -> Path:
        """Persist the current column set for ``source.table``."""
        self.schema_dir.mkdir(parents=True, exist_ok=True)
        path = self._schema_path(source, table)
        payload = {
            "source": source,
            "table": table,
            "captured_at": datetime.now().isoformat(timespec="seconds"),
            "columns": columns,
        }
        path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
        return path

    def load_schema_snapshot(self, source: str, table: str) -> dict[str, Any] | None:
        """Return the last saved schema snapshot, or ``None`` if there is none."""
        path = self._schema_path(source, table)
        if not path.exists():
            return None
        return json.loads(path.read_text(encoding="utf-8"))

    # -- row-count history (volume-drift) --------------------------------

    def _rowcount_path(self, source: str, table: str) -> Path:
        return self.rowcount_dir / f"{_slug(source, table)}.csv"

    def append_row_count(
        self,
        source: str,
        table: str,
        row_count: int,
        run_id: str = "",
        batch_id: str = "",
    ) -> Path:
        """Append one row-count observation to the table's history."""
        self.rowcount_dir.mkdir(parents=True, exist_ok=True)
        path = self._rowcount_path(source, table)
        is_new = not path.exists()
        with path.open("a", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=_HISTORY_FIELDS)
            if is_new:
                writer.writeheader()
            writer.writerow(
                {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "run_id": run_id,
                    "batch_id": batch_id,
                    "row_count": int(row_count),
                }
            )
        return path

    def row_count_history(self, source: str, table: str) -> list[dict[str, Any]]:
        """Return the full row-count history (oldest first)."""
        path = self._rowcount_path(source, table)
        if not path.exists():
            return []
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        for row in rows:
            row["row_count"] = int(row["row_count"])
        return rows

    def baseline_row_count(self, source: str, table: str, window: int = 5) -> float | None:
        """Average of the last ``window`` historical row counts (baseline).

        Returns ``None`` when there is no history yet (first run establishes it).
        """
        history = self.row_count_history(source, table)
        if not history:
            return None
        recent = [row["row_count"] for row in history[-window:]]
        return sum(recent) / len(recent)

"""Durable file-based state store for the stateful quality checks.

Schema-drift and volume-drift compare *this* run against previous runs, so the
baselines must outlive the run that wrote them::

    state/
    ├── schema_snapshots/<source>__<table>.json   # last-seen columns
    └── row_count_history/<source>__<table>.csv    # counts over time

**Durability.** State lives in its own root (``state/`` by default), *not* under
the run-output tree — that tree is gitignored and recreated per run, so
baselines stored there vanished every time and drift detection silently never
fired in CI, cron, or containers. Point ``--state-dir`` at a persistent volume,
a synced directory, or commit it, depending on how you deploy.

**Safety.** Writes are atomic (temp file + ``os.replace``) so a crash mid-write
cannot leave a half-written baseline that breaks the next run, and each file is
flock-guarded so two concurrent runs cannot interleave into a corrupt history.
Malformed rows are skipped rather than raising.

**Retention.** History is capped (``max_history``) so files stay bounded.
"""

from __future__ import annotations

import csv
import io
import json
import os
import re
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Iterator

try:  # POSIX only; locking degrades to a no-op elsewhere.
    import fcntl
except ImportError:  # pragma: no cover - non-POSIX
    fcntl = None  # type: ignore[assignment]

_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

_HISTORY_FIELDS = ("timestamp", "run_id", "batch_id", "row_count", "status")

DEFAULT_STATE_DIR = Path("state")
DEFAULT_MAX_HISTORY = 500


def _slug(source: str, table: str) -> str:
    return _SAFE.sub("_", f"{source}__{table}")


@contextmanager
def _locked(path: Path) -> Iterator[None]:
    """Hold an exclusive lock for ``path`` while the body runs."""
    if fcntl is None:  # pragma: no cover - non-POSIX
        yield
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def _atomic_write(path: Path, text: str) -> None:
    """Write ``text`` to ``path`` atomically (temp file + replace)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


class FileState:
    """Persist and read back baselines used by stateful quality checks."""

    def __init__(self, state_dir: str | Path = DEFAULT_STATE_DIR, max_history: int = DEFAULT_MAX_HISTORY) -> None:
        self.state_dir = Path(state_dir)
        self.schema_dir = self.state_dir / "schema_snapshots"
        self.rowcount_dir = self.state_dir / "row_count_history"
        self.max_history = int(max_history)

    # -- schema snapshots (schema-drift) ---------------------------------

    def _schema_path(self, source: str, table: str) -> Path:
        return self.schema_dir / f"{_slug(source, table)}.json"

    def save_schema_snapshot(self, source: str, table: str, columns: list[dict[str, Any]]) -> Path:
        """Persist the current column set for ``source.table``."""
        path = self._schema_path(source, table)
        payload = {
            "source": source,
            "table": table,
            "captured_at": datetime.now().isoformat(timespec="seconds"),
            "columns": columns,
        }
        with _locked(path):
            _atomic_write(path, json.dumps(payload, indent=2, default=str))
        return path

    def load_schema_snapshot(self, source: str, table: str) -> dict[str, Any] | None:
        """Return the last saved snapshot, or ``None`` if absent or unreadable.

        A corrupt snapshot is treated as "no baseline" rather than raising: the
        next run re-establishes it instead of failing the pipeline.
        """
        path = self._schema_path(source, table)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None

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
        status: str = "ok",
    ) -> Path:
        """Append one observation, capped at ``max_history`` entries.

        ``status`` lets a caller mark an observation as anomalous so it can be
        excluded from future baselines (see :meth:`baseline_row_counts`).
        """
        path = self._rowcount_path(source, table)
        record = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "run_id": run_id,
            "batch_id": batch_id,
            "row_count": int(row_count),
            "status": status,
        }
        with _locked(path):
            history = self._read_unlocked(path)
            history.append(record)
            if len(history) > self.max_history:
                history = history[-self.max_history :]
            buffer = io.StringIO()
            writer = csv.DictWriter(buffer, fieldnames=_HISTORY_FIELDS)
            writer.writeheader()
            writer.writerows(history)
            _atomic_write(path, buffer.getvalue())
        return path

    @staticmethod
    def _read_unlocked(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        try:
            with path.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
        except OSError:  # pragma: no cover - unreadable state
            return []
        parsed: list[dict[str, Any]] = []
        for row in rows:
            try:
                row["row_count"] = int(row["row_count"])
            except (KeyError, TypeError, ValueError):
                continue  # skip a torn or malformed line rather than raising
            row.setdefault("status", "ok")
            parsed.append(row)
        return parsed

    def row_count_history(self, source: str, table: str) -> list[dict[str, Any]]:
        """Return the observation history (oldest first)."""
        return self._read_unlocked(self._rowcount_path(source, table))

    def baseline_row_counts(
        self,
        source: str,
        table: str,
        window: int = 5,
        include_anomalies: bool = False,
    ) -> list[int]:
        """Recent counts eligible to form a baseline.

        Observations marked anomalous are excluded by default: letting a bad
        run into the baseline is how an anomaly quietly becomes the new normal.
        """
        history = self.row_count_history(source, table)
        if not include_anomalies:
            history = [row for row in history if row.get("status", "ok") == "ok"]
        return [row["row_count"] for row in history[-window:]]

    def baseline_row_count(self, source: str, table: str, window: int = 5) -> float | None:
        """Mean of the recent eligible counts, or ``None`` with no history."""
        recent = self.baseline_row_counts(source, table, window=window)
        if not recent:
            return None
        return sum(recent) / len(recent)

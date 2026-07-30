"""Per-run context: identity, timing, output layout, and lineage.

Every pipeline execution gets a :class:`RunContext` that fixes a ``run_id`` and
``batch_id`` up front and owns the on-disk output layout::

    etl_output/
    └── runs/<run_id>/
        ├── run_manifest.json      # written by the reporting layer
        ├── warnings_report.md
        ├── validation/
        ├── quarantine/
        └── logs/

The ``batch_id`` follows the Presto batch convention (current time minus 24h,
rounded to the hour) so the ETL framework aligns with the batch partitioning
already used on the source tables.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

DEFAULT_OUTPUT_ROOT = Path("etl_output")


def default_batch_id(now: datetime | None = None) -> str:
    """Return the default batch id: (now - 24h) rounded down to the hour."""
    batch_time = (now or datetime.now()) - timedelta(hours=24)
    return batch_time.replace(minute=0, second=0, microsecond=0).strftime("%Y%m%d%H%M%S")


def _new_run_id(now: datetime) -> str:
    return f"{now.strftime('%Y%m%dT%H%M%S')}_{uuid.uuid4().hex[:8]}"


@dataclass
class RunContext:
    """Identity + output layout for a single pipeline run."""

    pipeline: str = "adhoc"
    env: str = "dev"
    run_id: str = ""
    batch_id: str = ""
    started_at: str = ""
    output_root: Path = DEFAULT_OUTPUT_ROOT
    lineage: list[dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        now = datetime.now()
        if not self.run_id:
            self.run_id = _new_run_id(now)
        if not self.batch_id:
            self.batch_id = default_batch_id(now)
        if not self.started_at:
            self.started_at = now.isoformat(timespec="seconds")
        self.output_root = Path(self.output_root)

    # -- output layout ---------------------------------------------------

    @property
    def run_dir(self) -> Path:
        return self.output_root / "runs" / self.run_id

    @property
    def state_dir(self) -> Path:
        return self.output_root / "state"

    def subdir(self, name: str) -> Path:
        """Return (creating) a subdirectory of this run's output dir."""
        path = self.run_dir / name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def ensure_dirs(self) -> "RunContext":
        """Create the standard run subdirectories."""
        for name in ("validation", "quarantine", "logs"):
            self.subdir(name)
        return self

    # -- lineage ---------------------------------------------------------

    def record(self, stage: str, **details: Any) -> None:
        """Append a lineage event (stage + arbitrary details) to the run."""
        self.lineage.append(
            {
                "stage": stage,
                "at": datetime.now().isoformat(timespec="seconds"),
                **details,
            }
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "pipeline": self.pipeline,
            "env": self.env,
            "batch_id": self.batch_id,
            "started_at": self.started_at,
            "lineage": self.lineage,
        }

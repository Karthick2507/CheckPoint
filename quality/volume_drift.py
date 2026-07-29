"""Volume-drift check — did the row count move too far from its baseline?

Compares the current ``COUNT(*)`` against a rolling baseline (mean of the last
``window`` runs, from :class:`~runtime.state.FileState`). The first run has no
baseline, so it succeeds and simply records the count. Every run appends its
observation to the history.
"""

from __future__ import annotations

from typing import Any

from quality.base import QualityCheck


class VolumeDriftCheck(QualityCheck):
    check = "volume_drift"
    dimension = "volume"

    def __init__(
        self,
        target: str,
        tolerance: float = 0.25,
        window: int = 5,
        severity: str = "warning",
    ) -> None:
        super().__init__(target, severity)
        self.tolerance = float(tolerance)
        self.window = int(window)

    def run(self, source: Any, state: Any | None = None, run_id: str = "", batch_id: str = "") -> Any:
        rows = source.execute(f"SELECT COUNT(*) AS n FROM {self.target}")
        count = int(rows[0]["n"]) if rows else 0

        baseline = None
        if state is not None:
            baseline = state.baseline_row_count(source.name, self.target, window=self.window)

        if baseline is None:
            result = self._result(
                success=True,
                observed=count,
                expected="(no baseline yet)",
                details="First observation — establishing volume baseline.",
            )
        else:
            deviation = abs(count - baseline) / baseline if baseline else 0.0
            success = deviation <= self.tolerance
            result = self._result(
                success=success,
                observed=count,
                expected=f"{baseline:.0f} ± {self.tolerance:.0%}",
                details=(
                    f"Row count {count} deviates {deviation:.1%} from baseline {baseline:.0f} "
                    f"({'within' if success else 'exceeds'} {self.tolerance:.0%} tolerance)."
                ),
                metadata={"baseline": baseline, "deviation": round(deviation, 4)},
            )

        # Record this observation for future baselines (after computing baseline
        # so the current count never influences its own comparison).
        if state is not None:
            state.append_row_count(source.name, self.target, count, run_id=run_id, batch_id=batch_id)
        return result

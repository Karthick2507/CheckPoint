"""Volume-drift check — did this batch's row count move away from normal?

**Scope the count to the batch.** Counting the whole table is meaningless for an
append-only warehouse: the total only ever grows, so the baseline chases it
upward and a completely failed batch is invisible (100,000 historical rows + 0
new rows still counts ~100,000). Set ``batch_key`` and the check counts only the
slice this run processed, which is the thing that can actually go wrong.

**Robust baseline.** The centre is the *median* of recent eligible observations,
not the mean, so one bad run cannot drag it (see :mod:`quality.stats`). Runs
that fail the check are recorded as anomalies and excluded from future
baselines, so an anomaly never becomes the new normal.

**Honest about not knowing.** With fewer than ``min_history`` observations the
check reports success but says it is still establishing a baseline, rather than
comparing against one or two samples and pretending that is a trend.
"""

from __future__ import annotations

from typing import Any

from quality.base import QualityCheck
from quality.stats import mad, median_value, relative_deviation, robust_z_score
from runtime.sql import build_batch_predicate, where_clause


class VolumeDriftCheck(QualityCheck):
    check = "volume_drift"
    dimension = "volume"

    def __init__(
        self,
        target: str,
        tolerance: float = 0.25,
        window: int = 5,
        min_history: int = 3,
        batch_key: str | None = None,
        batch_filter: str | None = None,
        severity: str = "warning",
    ) -> None:
        super().__init__(target, severity)
        self.tolerance = float(tolerance)
        self.window = int(window)
        self.min_history = max(1, int(min_history))
        self.batch_key = batch_key
        self.batch_filter = batch_filter

    # -- SQL ---------------------------------------------------------------

    def count_sql(self, batch_id: Any = None, template_context: dict[str, Any] | None = None) -> str:
        predicate = build_batch_predicate(self.batch_key, batch_id, self.batch_filter, template_context)
        return f"SELECT COUNT(*) AS n FROM {self.target}{where_clause(predicate)}"

    @property
    def scope_key(self) -> str:
        """History is kept per scope so batch counts never mix with table counts."""
        return f"{self.target}#batch" if (self.batch_key or self.batch_filter) else self.target

    # -- execution ---------------------------------------------------------

    def run(
        self,
        source: Any,
        state: Any | None = None,
        run_id: str = "",
        batch_id: str = "",
        template_context: dict[str, Any] | None = None,
    ) -> Any:
        scoped = bool(self.batch_key or self.batch_filter)
        rows = source.execute(self.count_sql(batch_id, template_context))
        count = int(rows[0]["n"]) if rows else 0

        history = (
            state.baseline_row_counts(source.name, self.scope_key, window=self.window)
            if state is not None
            else []
        )
        result = self._evaluate(count, history, scoped)

        # Record the observation for future baselines, tagging a failure so it
        # is excluded from them (computed after the comparison, so the current
        # count never influences its own verdict).
        if state is not None:
            state.append_row_count(
                source.name,
                self.scope_key,
                count,
                run_id=run_id,
                batch_id=batch_id,
                status="ok" if result.success else "anomaly",
            )
        return result

    def _evaluate(self, count: int, history: list[int], scoped: bool) -> Any:
        note = "batch-scoped" if scoped else "WHOLE TABLE (set batch_key to scope to the batch)"

        if len(history) < self.min_history:
            return self._result(
                success=True,
                observed=count,
                expected=f"(establishing baseline: {len(history)}/{self.min_history} observations)",
                details=(
                    f"Counted {count} rows ({note}). Not enough history to judge drift yet — "
                    f"{len(history)} of {self.min_history} observations."
                ),
                metadata={"history": len(history), "scoped": scoped},
            )

        centre = median_value(history)
        deviation = relative_deviation(count, centre)

        if deviation is None:
            # Baseline is zero: there is no relative scale, so any arrival is a
            # change worth flagging (and 0 -> 0 is unchanged).
            success = count == 0
            return self._result(
                success=success,
                observed=count,
                expected=0,
                details=(
                    f"Baseline is 0 rows and this run counted {count} ({note}). "
                    + ("No change." if success else "Volume appeared where the baseline had none.")
                ),
                metadata={"baseline": 0, "scoped": scoped, "history": len(history)},
            )

        success = deviation <= self.tolerance
        return self._result(
            success=success,
            observed=count,
            expected=f"{centre:.0f} ± {self.tolerance:.0%}",
            details=(
                f"Counted {count} rows ({note}); median baseline {centre:.0f} over "
                f"{len(history)} runs. Deviation {deviation:.1%} "
                f"({'within' if success else 'exceeds'} {self.tolerance:.0%} tolerance)."
            ),
            metadata={
                "baseline_median": centre,
                "baseline_mad": mad(history),
                "deviation": round(deviation, 4),
                "robust_z": robust_z_score(count, history),
                "history": len(history),
                "scoped": scoped,
            },
        )

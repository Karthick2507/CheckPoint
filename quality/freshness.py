"""Freshness check — is the newest row recent enough?

Compares ``MAX(<timestamp_column>)`` against ``now`` and fails when the lag
exceeds ``max_lag_hours``. An empty result (no max timestamp) fails.

**Scope this to the batch.** Unscoped, ``MAX()`` is taken over the whole table,
so a stale batch is hidden by any fresher historical row and the check reports
healthy while today's data is a month old. With ``batch_key`` set the check asks
the question that matters: is *this* batch recent?
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from quality.base import QualityCheck
from runtime.sql import where_clause


class FreshnessCheck(QualityCheck):
    check = "freshness"
    dimension = "freshness"

    def __init__(
        self,
        target: str,
        timestamp_column: str,
        max_lag_hours: float,
        severity: str = "warning",
        batch_key: str | None = None,
        batch_filter: str | None = None,
    ) -> None:
        super().__init__(target, severity, batch_key=batch_key, batch_filter=batch_filter)
        self.timestamp_column = timestamp_column
        self.max_lag_hours = float(max_lag_hours)

    def max_timestamp_sql(
        self,
        batch_id: Any = None,
        template_context: dict[str, Any] | None = None,
    ) -> str:
        predicate = self.batch_predicate(batch_id, template_context)
        return (
            f"SELECT MAX({self.timestamp_column}) AS max_ts "
            f"FROM {self.target}{where_clause(predicate)}"
        )

    @staticmethod
    def _as_datetime(value: Any) -> datetime | None:
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(str(value))
        except ValueError:
            return None

    def run(
        self,
        source: Any,
        state: Any | None = None,
        now: datetime | None = None,
        batch_id: Any = None,
        template_context: dict[str, Any] | None = None,
    ) -> Any:
        now = now or datetime.now()
        rows = source.execute(self.max_timestamp_sql(batch_id, template_context))
        max_ts_raw = rows[0]["max_ts"] if rows else None
        max_ts = self._as_datetime(max_ts_raw)
        note = self.scope_note()

        if max_ts is None:
            return self._result(
                success=False,
                observed=max_ts_raw,
                expected=f"<= {self.max_lag_hours}h old",
                details=(
                    f"No usable MAX({self.timestamp_column}) ({note}) — "
                    "no rows for this scope, or an unparseable timestamp."
                ),
                metadata={"scoped": self.is_batch_scoped},
            )

        lag_hours = (now - max_ts).total_seconds() / 3600.0
        success = lag_hours <= self.max_lag_hours
        return self._result(
            success=success,
            observed=round(lag_hours, 2),
            expected=self.max_lag_hours,
            details=(
                f"Newest row is {lag_hours:.2f}h old ({note}); "
                f"{'within' if success else 'exceeds'} the {self.max_lag_hours}h threshold."
            ),
            metadata={
                "max_timestamp": max_ts.isoformat(),
                "column": self.timestamp_column,
                "scoped": self.is_batch_scoped,
            },
        )

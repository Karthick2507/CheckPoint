"""Freshness check — is the newest row recent enough?

Compares ``MAX(<timestamp_column>)`` in the table against ``now`` and fails when
the lag exceeds ``max_lag_hours``. An empty table (no max timestamp) fails.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from quality.base import QualityCheck


class FreshnessCheck(QualityCheck):
    check = "freshness"
    dimension = "freshness"

    def __init__(
        self,
        target: str,
        timestamp_column: str,
        max_lag_hours: float,
        severity: str = "warning",
    ) -> None:
        super().__init__(target, severity)
        self.timestamp_column = timestamp_column
        self.max_lag_hours = float(max_lag_hours)

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

    def run(self, source: Any, state: Any | None = None, now: datetime | None = None) -> Any:
        now = now or datetime.now()
        sql = f"SELECT MAX({self.timestamp_column}) AS max_ts FROM {self.target}"
        rows = source.execute(sql)
        max_ts_raw = rows[0]["max_ts"] if rows else None
        max_ts = self._as_datetime(max_ts_raw)

        if max_ts is None:
            return self._result(
                success=False,
                observed=max_ts_raw,
                expected=f"<= {self.max_lag_hours}h old",
                details=f"No usable MAX({self.timestamp_column}) — table empty or unparseable timestamp.",
            )

        lag_hours = (now - max_ts).total_seconds() / 3600.0
        success = lag_hours <= self.max_lag_hours
        return self._result(
            success=success,
            observed=round(lag_hours, 2),
            expected=self.max_lag_hours,
            details=(
                f"Newest row is {lag_hours:.2f}h old "
                f"({'within' if success else 'exceeds'} {self.max_lag_hours}h threshold)."
            ),
            metadata={"max_timestamp": max_ts.isoformat(), "column": self.timestamp_column},
        )

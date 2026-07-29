"""Referential-integrity check — do all child keys exist in the parent?

Runs an anti-join and counts orphans: child rows whose key has no match in the
parent. Zero orphans passes. Scales in-warehouse (ELT pushdown) rather than
pulling both tables out, which is why this is a SQL check rather than a native
GE ``expect_column_values_to_be_in_set``.
"""

from __future__ import annotations

from typing import Any

from quality.base import QualityCheck


class ReferentialIntegrityCheck(QualityCheck):
    check = "referential_integrity"
    dimension = "referential_integrity"

    def __init__(
        self,
        target: str,
        child_key: str,
        parent_table: str,
        parent_key: str,
        severity: str = "warning",
    ) -> None:
        super().__init__(target, severity)
        self.child_key = child_key
        self.parent_table = parent_table
        self.parent_key = parent_key

    def _orphans_sql(self) -> str:
        return (
            f"SELECT COUNT(*) AS orphans FROM {self.target} c "
            f"LEFT JOIN {self.parent_table} p "
            f"ON c.{self.child_key} = p.{self.parent_key} "
            f"WHERE p.{self.parent_key} IS NULL AND c.{self.child_key} IS NOT NULL"
        )

    def run(self, source: Any, state: Any | None = None) -> Any:
        rows = source.execute(self._orphans_sql())
        orphans = int(rows[0]["orphans"]) if rows else 0
        success = orphans == 0
        return self._result(
            success=success,
            observed=orphans,
            expected=0,
            details=(
                "All child keys resolve to a parent."
                if success
                else f"{orphans} orphan row(s): {self.target}.{self.child_key} "
                f"with no match in {self.parent_table}.{self.parent_key}."
            ),
            metadata={
                "child_key": self.child_key,
                "parent_table": self.parent_table,
                "parent_key": self.parent_key,
            },
        )

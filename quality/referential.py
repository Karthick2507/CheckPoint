"""Referential-integrity check — do all child keys exist in the parent?

Runs an anti-join and counts orphans: child rows whose key has no match in the
parent. Zero orphans passes. The join runs in-warehouse rather than pulling both
tables out, which is why this is a SQL check rather than a native GE
``expect_column_values_to_be_in_set``.

**Scope the child side to the batch.** Unscoped, the anti-join re-scans every
row ever written on every run, and — worse — a single historical orphan makes
the check fail forever no matter how clean today's batch is. ``batch_key``
restricts the child side to this run's slice; the parent side stays whole,
because a child may legitimately reference a parent from any earlier batch.
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
        batch_key: str | None = None,
        batch_filter: str | None = None,
    ) -> None:
        super().__init__(target, severity, batch_key=batch_key, batch_filter=batch_filter)
        self.child_key = child_key
        self.parent_table = parent_table
        self.parent_key = parent_key

    def orphans_sql(
        self,
        batch_id: Any = None,
        template_context: dict[str, Any] | None = None,
    ) -> str:
        conditions = [
            f"p.{self.parent_key} IS NULL",
            f"c.{self.child_key} IS NOT NULL",
        ]
        # Only the child side is scoped: parents legitimately predate the batch.
        predicate = self.batch_predicate(batch_id, template_context, alias="c")
        if predicate:
            conditions.append(predicate)
        return (
            f"SELECT COUNT(*) AS orphans FROM {self.target} c "
            f"LEFT JOIN {self.parent_table} p "
            f"ON c.{self.child_key} = p.{self.parent_key} "
            f"WHERE {' AND '.join(conditions)}"
        )

    def run(
        self,
        source: Any,
        state: Any | None = None,
        batch_id: Any = None,
        template_context: dict[str, Any] | None = None,
    ) -> Any:
        rows = source.execute(self.orphans_sql(batch_id, template_context))
        orphans = int(rows[0]["orphans"]) if rows else 0
        success = orphans == 0
        note = self.scope_note()
        return self._result(
            success=success,
            observed=orphans,
            expected=0,
            details=(
                f"All child keys resolve to a parent ({note})."
                if success
                else f"{orphans} orphan row(s) ({note}): {self.target}.{self.child_key} "
                f"with no match in {self.parent_table}.{self.parent_key}."
            ),
            metadata={
                "child_key": self.child_key,
                "parent_table": self.parent_table,
                "parent_key": self.parent_key,
                "scoped": self.is_batch_scoped,
            },
        )

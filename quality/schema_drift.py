"""Schema-drift check — has the table's column set changed since baseline?

Compares the current columns (via ``source.describe``) against the last saved
snapshot (:class:`~runtime.state.FileState`). The first run establishes the
baseline and succeeds. Thereafter, added/removed columns or type changes fail.
The baseline is *not* auto-updated on drift — drift must be acknowledged — unless
``update_on_success`` re-saves a clean match to track intentional evolution.
"""

from __future__ import annotations

from typing import Any

from quality.base import QualityCheck, normalize_columns


class SchemaDriftCheck(QualityCheck):
    check = "schema_drift"
    dimension = "schema"

    def __init__(self, target: str, severity: str = "warning", update_on_success: bool = False) -> None:
        super().__init__(target, severity)
        self.update_on_success = update_on_success

    def run(self, source: Any, state: Any | None = None) -> Any:
        current = normalize_columns(source.describe(self.target))
        current_map = {col["name"]: col["type"] for col in current}

        snapshot = state.load_schema_snapshot(source.name, self.target) if state is not None else None
        if snapshot is None:
            if state is not None:
                state.save_schema_snapshot(source.name, self.target, current)
            return self._result(
                success=True,
                observed=len(current),
                expected="(no baseline yet)",
                details=f"First observation — establishing schema baseline ({len(current)} columns).",
            )

        previous = normalize_columns(snapshot.get("columns", []))
        previous_map = {col["name"]: col["type"] for col in previous}

        added = sorted(set(current_map) - set(previous_map))
        removed = sorted(set(previous_map) - set(current_map))
        type_changed = sorted(
            name
            for name in set(current_map) & set(previous_map)
            if current_map[name] != previous_map[name]
        )

        success = not (added or removed or type_changed)
        if success and self.update_on_success and state is not None:
            state.save_schema_snapshot(source.name, self.target, current)

        parts = []
        if added:
            parts.append(f"added: {', '.join(added)}")
        if removed:
            parts.append(f"removed: {', '.join(removed)}")
        if type_changed:
            parts.append(f"type changed: {', '.join(type_changed)}")
        details = "No schema drift." if success else "Schema drift — " + "; ".join(parts)

        return self._result(
            success=success,
            observed=len(current),
            expected=len(previous),
            details=details,
            metadata={"added": added, "removed": removed, "type_changed": type_changed},
        )

"""Base types for the custom quality checks.

These checks cover the quality dimensions that native Great Expectations does
not express well against a live warehouse — freshness, volume-drift,
schema-drift, referential integrity. Each returns a :class:`CheckResult` shaped
like a GE result so the reporting layer treats them uniformly (warn-and-continue:
severity is recorded, never raised).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    return str(value)


@dataclass
class CheckResult:
    """The normalized outcome of one custom quality check."""

    check: str
    dimension: str
    target: str
    success: bool
    severity: str = "warning"
    observed: Any = None
    expected: Any = None
    details: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "check": self.check,
            "dimension": self.dimension,
            "target": self.target,
            "success": self.success,
            "severity": self.severity,
            "observed": _json_safe(self.observed),
            "expected": _json_safe(self.expected),
            "details": self.details,
            "metadata": {k: _json_safe(v) for k, v in self.metadata.items()},
        }


def normalize_columns(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Normalize DESCRIBE / PRAGMA output to ``[{"name","type"}, ...]``.

    Handles Presto/Trino (``Column``/``Type``), Snowflake (``name``/``type``),
    and sqlite ``PRAGMA table_info`` (``name``/``type``) by case-insensitive
    key lookup.
    """
    normalized: list[dict[str, str]] = []
    for row in rows:
        lower = {str(k).lower(): v for k, v in row.items()}
        name = lower.get("column") or lower.get("name") or lower.get("col_name")
        col_type = lower.get("type") or lower.get("data_type") or ""
        if name is None:
            continue
        normalized.append({"name": str(name), "type": str(col_type)})
    return normalized


class QualityCheck(ABC):
    """A custom quality check bound to a target table/asset.

    **Batch scoping.** Set ``batch_key`` (the partition column) or
    ``batch_filter`` (arbitrary, templated) and the check measures only the
    slice this run processed. Without it a check reads all history, which is
    both slower every run and frequently wrong: a stale batch hides behind a
    fresher historical row, and one historical violation fails every future run
    forever.
    """

    check: str = "check"
    dimension: str = "quality"

    def __init__(
        self,
        target: str,
        severity: str = "warning",
        batch_key: str | None = None,
        batch_filter: str | None = None,
    ) -> None:
        self.target = target
        self.severity = severity
        self.batch_key = batch_key
        self.batch_filter = batch_filter

    @property
    def is_batch_scoped(self) -> bool:
        return bool(self.batch_key or self.batch_filter)

    def batch_predicate(
        self,
        batch_id: Any = None,
        template_context: dict[str, Any] | None = None,
        alias: str | None = None,
    ) -> str | None:
        """The WHERE predicate for this check's batch, if it is scoped.

        ``alias`` qualifies the column for use inside a join.
        """
        from runtime.sql import build_batch_predicate

        key = f"{alias}.{self.batch_key}" if (alias and self.batch_key) else self.batch_key
        return build_batch_predicate(key, batch_id, self.batch_filter, template_context)

    def scope_note(self) -> str:
        """Human-readable note about what the check measured."""
        return "batch-scoped" if self.is_batch_scoped else "WHOLE TABLE (set batch_key to scope)"

    @abstractmethod
    def run(self, source: Any, state: Any | None = None) -> CheckResult:
        """Execute the check against ``source`` (optionally using ``state``)."""

    def _result(self, success: bool, **kwargs: Any) -> CheckResult:
        return CheckResult(
            check=self.check,
            dimension=self.dimension,
            target=self.target,
            success=success,
            severity=self.severity,
            **kwargs,
        )

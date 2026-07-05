from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ColumnSpec:
    name: str
    type: str | None = None


@dataclass
class TypeDiff:
    column: str
    src_type: str
    bcv_type: str
    expected: bool
    note: str
    source: str


@dataclass
class KnownIssue:
    id: str
    description: str
    source: str


@dataclass
class DroppedPrefix:
    prefix: str
    note: str
    source: str


@dataclass
class ValueEquivalences:
    column_specific: dict[str, list[Any]] = field(default_factory=dict)
    generic_groups: list[list[Any]] = field(default_factory=list)

    def normalize(self, column: str, value: Any) -> Any:
        """Map value to a canonical representative if it's in a known-equivalent set for this column."""
        for group in [self.column_specific.get(column, []), *self.generic_groups]:
            if not group:
                continue
            normalized_group = [_normalize_key(v) for v in group]
            if _normalize_key(value) in normalized_group:
                return normalized_group[0]
        return _normalize_key(value)


def _normalize_key(value: Any) -> str:
    """Canonical form used only for equivalence-group membership checks.

    Python None must line up with the "null"/"none" string tokens config groups
    use to represent NULL (config is YAML, so it can only express NULL-ish
    concepts as strings) -- otherwise a real NULL from a query never matches
    the group its string-literal counterpart is in.
    """
    if value is None:
        return "null"
    return str(value).strip().lower()


@dataclass
class TableValidationConfig:
    table: str
    src_table: str
    bcv_table: str
    key_columns: list[str]
    sampled_bit_flag: int
    confirmed_matching_columns: list[ColumnSpec]
    excluded_columns: list[str]
    known_dropped_prefixes: list[DroppedPrefix]
    known_type_diffs: list[TypeDiff]
    known_value_equivalences: ValueEquivalences
    known_issues: list[KnownIssue]
    ivt_dependent_columns: list[str]

    @property
    def known_issue_columns(self) -> set[str]:
        """Columns referenced by an open known_issue, e.g. via known_type_diffs with expected=False."""
        return {diff.column for diff in self.known_type_diffs if not diff.expected}

    def is_dropped_column(self, column: str) -> bool:
        return any(column.startswith(dp.prefix) for dp in self.known_dropped_prefixes)


def load_table_config(path: str | Path) -> TableValidationConfig:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))

    equivalences_raw = data.get("known_value_equivalences", {})
    equivalences = ValueEquivalences(
        column_specific={
            entry["column"]: entry["equivalent_values"]
            for entry in equivalences_raw.get("column_specific", [])
        },
        generic_groups=equivalences_raw.get("generic_groups", []),
    )

    return TableValidationConfig(
        table=data["table"],
        src_table=data["src_table"],
        bcv_table=data["bcv_table"],
        key_columns=data["key_columns"],
        sampled_bit_flag=data["sampled_bit_flag"],
        confirmed_matching_columns=[
            ColumnSpec(name=c["name"], type=c.get("type")) for c in data["confirmed_matching_columns"]
        ],
        excluded_columns=data.get("excluded_columns", []),
        known_dropped_prefixes=[
            DroppedPrefix(prefix=p["prefix"], note=p["note"], source=p["source"])
            for p in data.get("known_dropped_prefixes", [])
        ],
        known_type_diffs=[
            TypeDiff(
                column=d["column"],
                src_type=d["src_type"],
                bcv_type=d["bcv_type"],
                expected=d["expected"],
                note=d["note"],
                source=d["source"],
            )
            for d in data.get("known_type_diffs", [])
        ],
        known_value_equivalences=equivalences,
        known_issues=[
            KnownIssue(id=i["id"], description=i["description"], source=i["source"])
            for i in data.get("known_issues", [])
        ],
        ivt_dependent_columns=data.get("ivt_dependent_columns", []),
    )

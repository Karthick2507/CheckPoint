"""Explicit schema contract between source and target.

Two defects this replaces:

* **``SELECT *``.** Extract projected everything, so an upstream column
  addition, removal, or reorder flowed straight into the target with nothing
  noticing. A pipeline should state the columns it depends on.
* **``rows[0].keys()``.** The loader took its column list from the *first* row,
  so a later row carrying a different key silently lost that value — no error,
  no warning, no trace in the report.

A :class:`SchemaContract` names the columns a pipeline reads, optionally
renaming them for the target, and can verify a payload actually matches before
anything is written.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from runtime.sql import quote_identifier


class SchemaContractError(ValueError):
    """A payload does not match the declared contract."""


@dataclass
class ColumnSpec:
    """One projected column: where it comes from, what it is called after."""

    source: str
    alias: str | None = None

    @property
    def output(self) -> str:
        return self.alias or self.source

    def select_expression(self, quote: str = '"') -> str:
        # The source side may be an expression (a function call, a cast), so it
        # is only quoted when it looks like a plain identifier.
        source_sql = self.source if _is_expression(self.source) else quote_identifier(self.source, quote)
        if self.alias and self.alias != self.source:
            return f"{source_sql} AS {quote_identifier(self.alias, quote)}"
        return source_sql


def _is_expression(value: str) -> bool:
    """Whether ``value`` is SQL rather than a bare column name."""
    return any(char in value for char in "()+-*/ ,'")


@dataclass
class SchemaContract:
    """The columns a pipeline reads, and their names on the target."""

    columns: list[ColumnSpec] = field(default_factory=list)
    strict: bool = True

    @property
    def declared(self) -> bool:
        return bool(self.columns)

    @property
    def output_names(self) -> list[str]:
        return [column.output for column in self.columns]

    @classmethod
    def from_config(cls, value: Any, strict: bool = True) -> "SchemaContract":
        """Build a contract from ``columns:`` config.

        Accepts a list of names, a mapping of ``source: target``, or a list of
        ``{source, as}`` entries::

            columns: [id, name]
            columns: {request__transaction_id: transaction_id}
            columns:
              - source: request__transaction_id
                as: transaction_id
        """
        if not value:
            return cls(strict=strict)

        specs: list[ColumnSpec] = []
        if isinstance(value, Mapping):
            specs = [ColumnSpec(source=str(k), alias=str(v)) for k, v in value.items()]
        elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            for item in value:
                if isinstance(item, Mapping):
                    source = item.get("source") or item.get("name")
                    if not source:
                        raise ValueError("Each column entry requires a 'source'")
                    specs.append(ColumnSpec(source=str(source), alias=_alias_of(item)))
                else:
                    specs.append(ColumnSpec(source=str(item)))
        else:
            raise ValueError(f"Unsupported 'columns' config: {type(value).__name__}")

        duplicates = _duplicates([spec.output for spec in specs])
        if duplicates:
            raise ValueError(f"Duplicate output column(s) in contract: {', '.join(sorted(duplicates))}")
        return cls(columns=specs, strict=strict)

    # -- SQL ---------------------------------------------------------------

    def projection(self, quote: str = '"') -> str:
        """The SELECT list — ``*`` only when no contract is declared."""
        if not self.declared:
            return "*"
        return ", ".join(column.select_expression(quote) for column in self.columns)

    # -- payload enforcement -----------------------------------------------

    def conform(self, rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
        """Return ``rows`` projected onto the contract.

        With a contract declared, every row is reduced to exactly the declared
        columns (missing ones become NULL, extras are dropped deliberately
        rather than by accident). In ``strict`` mode a row missing a declared
        column is an error instead of a silent NULL.
        """
        if not self.declared:
            return list(rows)

        names = self.output_names
        conformed: list[dict[str, Any]] = []
        for index, row in enumerate(rows):
            if self.strict:
                missing = [name for name in names if name not in row]
                if missing:
                    raise SchemaContractError(
                        f"row {index} is missing declared column(s): {', '.join(missing)}"
                    )
            conformed.append({name: row.get(name) for name in names})
        return conformed

    def check_uniform(self, rows: Sequence[dict[str, Any]]) -> None:
        """Raise if rows disagree about their columns (no contract declared).

        Without this the loader silently used the first row's keys and dropped
        every value under a key that row happened not to have.
        """
        if not rows:
            return
        expected = set(rows[0].keys())
        for index, row in enumerate(rows[1:], start=1):
            keys = set(row.keys())
            if keys != expected:
                extra = ", ".join(sorted(keys - expected)) or "-"
                missing = ", ".join(sorted(expected - keys)) or "-"
                raise SchemaContractError(
                    f"row {index} has a different shape from row 0 "
                    f"(unexpected: {extra}; missing: {missing}). "
                    "Declare source.columns to pin the schema."
                )


def _alias_of(item: Mapping[str, Any]) -> str | None:
    for key in ("as", "alias", "target"):
        if item.get(key):
            return str(item[key])
    return None


def _duplicates(values: Sequence[str]) -> set[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return dupes

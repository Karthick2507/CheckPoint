"""Declarative pipeline configuration (analyst-facing YAML).

A pipeline wires a source, optional transform, optional target, the validation
suites for each gate, and the custom quality checks. Connections and suites are
referenced by name/path and resolved at run time, so a pipeline is portable
across environments and sources.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from data_sources.config import load_yaml


@dataclass
class SourceSpec:
    connection: str
    table: str | None = None
    query: str | None = None
    batch_key: str | None = None


@dataclass
class ExtractSpec:
    mode: str = "full"  # full | incremental
    limit: int | None = None

    @property
    def incremental(self) -> bool:
        return self.mode.lower() == "incremental"


# How the pipeline moves data:
#   "rows"     — read into Python and INSERT … VALUES (cross-system moves)
#   "pushdown" — INSERT … SELECT executed in the warehouse (same-warehouse, any scale)
#   "auto"     — pushdown when source and target are the same connection and a
#                transform SELECT exists, otherwise rows
EXECUTION_MODES = ("auto", "rows", "pushdown")


@dataclass
class TargetSpec:
    connection: str | None = None
    table: str | None = None
    mode: str = "append"  # append | overwrite | merge | none
    keys: list[str] = field(default_factory=list)
    # Opt in to a destructive load (overwrite/merge) with an empty payload.
    # Off by default so a missing upstream batch cannot wipe the target.
    allow_empty: bool = False


@dataclass
class PipelineConfig:
    name: str
    env: str = "dev"
    source: SourceSpec = None  # type: ignore[assignment]
    extract: ExtractSpec = field(default_factory=ExtractSpec)
    transform: list[str] = field(default_factory=list)
    target: TargetSpec | None = None
    suite_raw: str | None = None
    suite_curated: str | None = None
    suite_post: str | None = None
    checks: list[dict[str, Any]] = field(default_factory=list)
    schedule: str | None = None
    # User-defined variables exposed to SQL templates alongside batch_id/run_id.
    vars: dict[str, Any] = field(default_factory=dict)
    # How data moves: auto | rows | pushdown (see EXECUTION_MODES).
    execution: str = "auto"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PipelineConfig":
        pipeline = data.get("pipeline") or data
        name = pipeline.get("name")
        if not name:
            raise ValueError("Pipeline config requires a 'name'")

        source_data = pipeline.get("source")
        if not source_data or not source_data.get("connection"):
            raise ValueError("Pipeline config requires a 'source' with a 'connection'")
        source = SourceSpec(
            connection=source_data["connection"],
            table=source_data.get("table"),
            query=source_data.get("query"),
            batch_key=source_data.get("batch_key"),
        )
        if not source.table and not source.query:
            raise ValueError("Pipeline source requires a 'table' or a 'query'")

        extract_data = pipeline.get("extract") or {}
        extract = ExtractSpec(
            mode=str(extract_data.get("mode") or "full"),
            limit=extract_data.get("limit"),
        )

        transform = list(pipeline.get("transform") or [])

        target = None
        target_data = pipeline.get("target")
        if target_data:
            target = TargetSpec(
                connection=target_data.get("connection"),
                table=target_data.get("table"),
                mode=str(target_data.get("mode") or "append"),
                keys=list(target_data.get("keys") or []),
                allow_empty=bool(target_data.get("allow_empty") or False),
            )

        execution = str(pipeline.get("execution") or "auto").lower()
        if execution not in EXECUTION_MODES:
            raise ValueError(
                f"Invalid execution mode {execution!r} (expected one of {', '.join(EXECUTION_MODES)})"
            )

        validate = pipeline.get("validate") or {}
        return cls(
            name=str(name),
            env=str(pipeline.get("env") or "dev"),
            source=source,
            extract=extract,
            transform=transform,
            target=target,
            suite_raw=validate.get("raw"),
            suite_curated=validate.get("curated"),
            suite_post=validate.get("post"),
            checks=list(pipeline.get("checks") or []),
            schedule=pipeline.get("schedule"),
            vars=dict(pipeline.get("vars") or {}),
            execution=execution,
        )


def load_pipeline_config(path: str | Path) -> PipelineConfig:
    return PipelineConfig.from_dict(load_yaml(path))

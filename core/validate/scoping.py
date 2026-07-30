"""Narrow a validation asset to the batch the pipeline is processing.

Without this, every gate runs ``add_batch_definition_whole_table`` and each
expectation scans the entire table. Two consequences, both bad:

* **Wrong answers.** A thousand bad rows in today's batch are diluted into
  billions of good historical rows, so a threshold expectation passes.
  Conversely ``expect_column_values_to_be_unique`` fails forever the moment one
  historical duplicate exists, regardless of the batch being loaded.
* **Ruinous cost.** Every expectation full-scans a TiB table on every run.

Scoping rewrites the asset as a query restricted to the current batch, so the
gate validates exactly the slice that was just processed.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

from core.validate.suite_config import AssetConfig, SuiteConfig
from runtime.templating import render_sql


def sql_literal(value: Any) -> str:
    """Render a batch value as a SQL literal."""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def build_batch_predicate(
    asset: AssetConfig,
    batch_id: Any,
    template_context: dict[str, Any] | None = None,
) -> str | None:
    """Return the WHERE predicate restricting ``asset`` to ``batch_id``."""
    if asset.batch_filter:
        return render_sql(asset.batch_filter, template_context or {})
    if asset.batch_key:
        return f"{asset.batch_key} = {sql_literal(batch_id)}"
    return None


def scope_asset_to_batch(
    asset: AssetConfig,
    batch_id: Any,
    template_context: dict[str, Any] | None = None,
) -> AssetConfig:
    """Return a copy of ``asset`` narrowed to the current batch.

    A table asset becomes a query asset (``SELECT * FROM t WHERE <predicate>``);
    a query asset is wrapped so the predicate applies to its result set. Assets
    without ``batch_key``/``batch_filter`` are returned unchanged.
    """
    predicate = build_batch_predicate(asset, batch_id, template_context)
    if not predicate:
        return asset

    if asset.type == "query":
        inner = (asset.query or "").strip().rstrip(";").strip()
        scoped_sql = f"SELECT * FROM ({inner}) AS _scoped WHERE {predicate}"
    else:
        table = asset.table_name
        if asset.schema_name and "." not in str(table):
            table = f"{asset.schema_name}.{table}"
        scoped_sql = f"SELECT * FROM {table} WHERE {predicate}"

    return replace(
        asset,
        type="query",
        query=scoped_sql,
        table_name=None,
        schema_name=None,
    )


def scope_suite_to_batch(
    suite: SuiteConfig,
    batch_id: Any,
    template_context: dict[str, Any] | None = None,
) -> SuiteConfig:
    """Return ``suite`` with its asset narrowed to the current batch."""
    scoped = scope_asset_to_batch(suite.asset, batch_id, template_context)
    if scoped is suite.asset:
        return suite
    return replace(suite, asset=scoped)

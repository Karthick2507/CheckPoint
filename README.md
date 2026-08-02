# CheckPoint — ETL & Data Quality Framework

A config-driven **ETL + data-quality framework** built on **[Great Expectations](https://greatexpectations.io/) (1.x Fluent API)** with a **pluggable multi-source connector layer**. It extracts, validates, transforms, and loads data across sources, running Great Expectations plus custom warehouse-aware checks at every stage — all warn-and-continue, files-only output.

Full architecture: **[`DESIGN.md`](DESIGN.md)**.

## Architecture at a glance

```
SOURCE ─► EXTRACT ─►[gate: raw]─► TRANSFORM ─►[gate: curated]─► LOAD ─►[gate: post]─► TARGET
                         │                          │                       │
                         └──────── Great Expectations + custom checks ───────┘
```

| Layer | Package | Role |
|-------|---------|------|
| Connectors | `data_sources/` | `DataSource` ABC + registry; Presto & Snowflake connectors — add a source with one folder + one `@register` line |
| Extract / Transform / Load | `core/extract`, `core/transform`, `core/load` | incremental & streaming reads, ELT SQL, `INSERT … SELECT` pushdown or row-based append/overwrite/merge |
| Validate | `core/validate/` | Great Expectations, source-agnostic, scoped to the current batch |
| Quality | `quality/` | freshness, volume-drift, schema-drift, referential integrity — batch-scoped, robust baselines |
| Runtime | `runtime/` | run context (run_id/batch_id/lineage), durable baselines, SQL templating, retries |
| Reporting | `reporting/` | run manifest + warnings report + quarantined rows |
| Orchestrator | `core/pipeline.py` | chains the stages through 3 quality gates |
| CLI | `cli.py` | `run-pipeline`, `validate`, `list-expectations`, `list-sources` |

## Install

```bash
pip install -r requirements.txt
```

## Configure (three YAML kinds)

**1. Connection** (`config/connections/`) — a source or target; `type` picks the connector:

```yaml
connection:
  name: mrm_presto
  type: presto                    # or: snowflake, trino, …
  host: presto-gateway.presto.fw1.aws.fwmrm.net
  catalog: mrm_log_flat
  schema: default
  auth_token: ${PRESTO_AUTH_TOKEN}   # sent as "Authorization: Bearer <token>"
```

**2. Suite** (`config/suites/`) — an asset + expectations, each with a `severity`:

```yaml
suite:
  name: request_raw
  asset:
    type: table
    name: request
    table_name: mrm_log_flat.default.request
    batch_key: process_batch_id     # validate THIS batch, not all history
expectations:
  - id: pk_not_null                 # stable id -> reliable severity + reporting
    type: expect_column_values_to_not_be_null
    column: request__transaction_id
    severity: critical
```

**3. Pipeline** (`config/pipelines/`) — source → transform → target + gates + checks:

```yaml
pipeline:
  name: request_daily
  execution: auto                   # auto | pushdown | rows  (see below)
  source:
    connection: mrm_presto
    table: mrm_log_flat.default.request
    batch_key: process_batch_id
    columns:                        # schema contract: projection + rename
      request__transaction_id: transaction_id
      request__event_time: event_time
  extract: { mode: incremental }    # add `stream: true` for large cross-system moves
  transform:
    - "SELECT request__transaction_id AS transaction_id FROM mrm_log_flat.default.request WHERE process_batch_id = '{{ batch_id }}'"
  target:  { connection: analytics_snowflake, table: ANALYTICS.PUBLIC.REQUEST_CLEAN, mode: merge, keys: [transaction_id] }
  validate: { raw: config/suites/request_raw.example.yml, curated: config/suites/request_curated.example.yml, post: config/suites/request_post.example.yml }
  checks:
    - { type: freshness, target: mrm_log_flat.default.request, timestamp_column: request__event_time, max_lag_hours: 6, severity: critical }
    - { type: volume_drift, target: mrm_log_flat.default.request, batch_key: process_batch_id, tolerance: 0.25, severity: warning }
```

SQL is rendered with `{{ batch_id }}`, `{{ run_id }}`, `{{ env }}` and anything under `vars:`. Rendering is **strict** — an unknown variable fails the stage rather than silently producing an empty predicate.

## Execution model

| Mode | What runs | Use for |
|------|-----------|---------|
| **pushdown** | `INSERT INTO target SELECT …` in the warehouse — no rows enter Python | Same-warehouse work at any scale |
| **rows** | read into Python, write back as `INSERT … VALUES` | Moving data *between* systems |
| **stream** | `fetchmany` chunks piped into the target (`extract.stream: true`) | Large cross-system moves — memory bounded by `chunk_size` |

`auto` picks pushdown when source and target share a connection, else rows.

**Load safety:** `overwrite`/`merge` refuse to run with an empty payload (a missing upstream batch must not wipe the target) unless `allow_empty: true`; delete and insert run in one transaction, and targets that cannot roll back are reported with `atomic: false` rather than pretending.

## Schema contract

`source.columns` names the columns a pipeline reads and what they are called on the target — projection and mapping in one place. Without it the extract is `SELECT *`, so an upstream column addition, removal, or reorder flows straight through unnoticed. It accepts a list (`[a, b]`), a `source: target` mapping, or `{source:, as:}` entries.

`strict_columns: true` (the default) makes a row missing a declared column fail the run instead of being written as a silent NULL. With no contract declared, the framework still insists rows agree with each other — the loader takes its column list from the first row and would otherwise drop every value under a key that row happens to lack.

## Reliability

Transient failures (timeouts, resets, 502/503/504) retry with exponential backoff and jitter — configurable per connection via `retry_attempts` / `retry_initial_delay` / `retry_max_delay`. Permanent failures (missing table, syntax error) never retry. **Reads retry; writes do not**, because re-issuing a partially applied `INSERT` is how duplicate rows appear.

Identifiers are quoted with the dialect's own quote character, so a column named `order` or `select` works. One Great Expectations context serves every gate, connections resolve once per run, and every engine is disposed when the run ends.

## Run

```bash
export PRESTO_AUTH_TOKEN=<token>          # VPN required for the prod gateway

# Run a full pipeline (extract -> validate -> transform -> validate -> load -> validate).
# --state-dir must point somewhere persistent for drift checks to work.
python -m cli run-pipeline \
  --pipeline config/pipelines/request_daily.example.yml \
  --state-dir /var/lib/checkpoint/state

# Validate suites against a connection (no ETL):
python -m cli validate \
  --connection config/connections/mrm_presto.example.yml \
  --suite config/suites/request_quality.example.yml

# Discover expectations / registered sources:
python -m cli list-expectations not_be_null
python -m cli list-sources
```

`--fail-on {critical|any|never}` sets the process **exit code** (for cron/CI). Warn-and-continue is unchanged — the pipeline always runs fully and writes its reports regardless.

## Output (files only)

```
etl_output/runs/<run_id>/  # disposable, per run
├── run_manifest.json      # full record + lineage + status
├── warnings_report.md     # every failure, critical first
├── validation/<suite>_validation.json|md
└── quarantine/            # the rows that actually failed, as CSV

state/                     # PERSISTENT — must survive between runs
├── schema_snapshots/      # schema-drift baselines
└── row_count_history/     # volume-drift baselines
```

> **`state/` must persist.** It holds the baselines that schema-drift and
> volume-drift compare against. In CI, cron, or a container, point
> `--state-dir` at a durable volume (or commit the directory) — otherwise every
> run starts with no baseline and those two checks can never detect anything.

## Quality dimensions

Native GE covers **completeness** and **uniqueness** (in suites). The `quality/` package adds **freshness**, **volume-drift**, **schema-drift**, and **referential integrity** — the dimensions that need warehouse-aware logic and baselines.

Freshness, volume-drift and referential-integrity checks are batch-scoped (`batch_key`), and volume-drift uses a **median** baseline: on an append-only table a whole-table count only ever grows, so a failed batch would be invisible, and a mean would be dragged by the very spikes it should catch. Failed runs are recorded as anomalies and excluded from future baselines, and nothing is judged until `min_history` observations exist.

## Tests

```bash
python -m pytest tests/ -q
```

The connector layer is dialect-agnostic, so the full flow — extract, transform, load (incl. cross-source), all three GE gates, the four custom checks, and reporting — is exercised end-to-end against **sqlite**, no live Presto required (336 tests).

## Extending: add a data source

```python
# data_sources/bigquery/connector.py
from data_sources.base import DataSource
from data_sources.registry import register

@register("bigquery")
class BigQueryDataSource(DataSource):
    def connection_string(self):
        return f"bigquery://{self.config['project']}/{self.config['dataset']}"
```

Import it in `data_sources/__init__.py` and it's usable from any connection/pipeline YAML. See [`DESIGN.md`](DESIGN.md) §4.

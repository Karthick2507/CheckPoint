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
| Extract / Transform / Load | `core/extract`, `core/transform`, `core/load` | read rows (incremental), ELT SQL pushdown, append/overwrite/merge |
| Validate | `core/validate/` | Great Expectations, source-agnostic (validates any `DataSource`) |
| Quality | `quality/` | freshness, volume-drift, schema-drift, referential integrity |
| Runtime | `runtime/` | run context (run_id/batch_id/lineage) + file-based baselines |
| Reporting | `reporting/` | run manifest + warnings report + per-suite reports |
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
  asset: { type: table, name: request, table_name: mrm_log_flat.default.request }
expectations:
  - type: expect_column_values_to_not_be_null
    column: request__transaction_id
    severity: critical
```

**3. Pipeline** (`config/pipelines/`) — source → transform → target + gates + checks:

```yaml
pipeline:
  name: request_daily
  source:  { connection: mrm_presto, table: mrm_log_flat.default.request, batch_key: process_batch_id }
  extract: { mode: incremental }
  transform:
    - "SELECT request__transaction_id AS transaction_id FROM mrm_log_flat.default.request WHERE process_batch_id = '{{ batch_id }}'"
  target:  { connection: analytics_snowflake, table: ANALYTICS.PUBLIC.REQUEST_CLEAN, mode: merge, keys: [transaction_id] }
  validate: { raw: config/suites/request_raw.example.yml, curated: config/suites/request_curated.example.yml, post: config/suites/request_post.example.yml }
  checks:
    - { type: freshness, target: mrm_log_flat.default.request, timestamp_column: request__event_time, max_lag_hours: 6, severity: critical }
    - { type: volume_drift, target: mrm_log_flat.default.request, tolerance: 0.25, severity: warning }
```

## Run

```bash
export PRESTO_AUTH_TOKEN=<token>          # VPN required for the prod gateway

# Run a full pipeline (extract -> validate -> transform -> validate -> load -> validate):
python -m cli run-pipeline --pipeline config/pipelines/request_daily.example.yml

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
etl_output/runs/<run_id>/
├── run_manifest.json      # full record + lineage + status
├── warnings_report.md     # every failure, critical first
└── validation/<suite>_validation.json|md
etl_output/state/          # schema snapshots + row-count baselines
```

## Quality dimensions

Native GE covers **completeness** and **uniqueness** (in suites). The `quality/` package adds **freshness**, **volume-drift**, **schema-drift**, and **referential integrity** — the dimensions that need warehouse-aware logic and baselines.

## Tests

```bash
python -m pytest tests/ -q
```

The connector layer is dialect-agnostic, so the full flow — extract, transform, load (incl. cross-source), all three GE gates, the four custom checks, and reporting — is exercised end-to-end against **sqlite**, no live Presto required (74 tests).

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

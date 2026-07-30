# ETL Framework — Design

A config-driven **ETL + data-quality framework** built on **Great Expectations
(1.x Fluent API)** with a **pluggable multi-source connector layer** (Presto
first; Snowflake and others drop in). This document is the frozen architecture
the implementation follows.

---

## 1. Purpose

Two jobs, one framework:

1. **ETL** — extract from a source, transform (ELT/SQL pushdown), load to a target.
2. **Data quality** — validate the data at every stage with Great Expectations
   plus custom warehouse-aware checks.

Great Expectations is **not** "the ETL" — it is the **quality gate** between
stages. Extract and Load are plumbing; Transform is business logic; GE + the
custom checks enforce the contracts.

```
SOURCE ─► EXTRACT ─►[gate: raw]─► TRANSFORM ─►[gate: curated]─► LOAD ─►[gate: post]─► TARGET
                         │                          │                       │
                         └──────── Great Expectations + custom checks ───────┘
                                    (warn-and-continue, severity-tagged)
```

## 2. Principles

1. **Config-driven** — pipelines, connections, and suites are declarative YAML.
2. **Source-agnostic** — everything depends on the `DataSource` interface, never
   a concrete database.
3. **Idempotent & incremental** — runs filter by `batch_key = batch_id`; a re-run
   is safe.
4. **Quality-gated** — GE contracts between every stage.
5. **Warn-and-continue** — nothing blocks the run; every failure is captured in a
   report, tagged `critical` or `warning`.
6. **Observable & files-only** — each run writes a manifest, a warnings report,
   and per-suite validation reports; baselines persist as files (no results DB).

## 3. Layered architecture

```
etl_framework/
├── data_sources/          # pluggable connectors (the source-agnostic seam)
│   ├── base.py            #   DataSource ABC + shared execute/describe
│   ├── registry.py        #   @register + create_data_source factory
│   ├── config.py          #   connection YAML loader (${ENV} interpolation)
│   ├── presto/            #   Presto/Trino connector (Bearer-token auth)
│   └── snowflake/         #   Snowflake connector (proves multi-source design)
├── core/
│   ├── extract/           # read rows (table/query, incremental by batch_id)
│   ├── transform/         # ELT: ordered SQL steps run on the source
│   ├── validate/          # Great Expectations (folded-in), source-agnostic
│   ├── load/              # append / overwrite / merge into a target
│   ├── pipeline_config.py # declarative PipelineConfig
│   └── pipeline.py        # the orchestrator (extract→gates→transform→load)
├── quality/               # the 4 non-native checks
│   ├── freshness.py
│   ├── volume_drift.py
│   ├── schema_drift.py
│   └── referential.py
├── runtime/
│   ├── run_context.py     # run_id / batch_id / lineage / output layout
│   └── state.py           # file-based baselines (schema snapshots, row counts)
├── reporting/             # manifest + warnings report + console
├── config/                # analyst-facing YAML
│   ├── connections/       #   sources & targets
│   ├── pipelines/         #   what runs, in what order
│   └── suites/            #   expectation suites (+ severity)
├── cli.py                 # run-pipeline / validate / list-*
└── tests/                 # sqlite-backed, exercises every layer for real
```

## 4. The multi-source connector layer

The pivotal design element. Every source implements one contract:

```python
class DataSource(ABC):
    type: str
    def connection_string(self) -> str        # SQLAlchemy URL
    def engine_kwargs(self) -> dict           # connect_args / auth
    def execute(self, sql) -> list[dict]      # shared machinery
    def describe(self, table) -> list[dict]   # schema introspection
    def capabilities(self) -> Capabilities    # dialect quirks
```

Because Great Expectations' Fluent `add_sql(connection_string, kwargs)` is
dialect-driven, **Presto (`trino://`) and Snowflake (`snowflake://`) validate
through the identical GE code path** — the connector merely supplies the URL and
auth. The *same* `connection_string` + `engine_kwargs` also feed direct
execution, so there is **one connection code path** for both GE and raw SQL.

**Adding a source** = one folder + one line:

```python
@register("bigquery")
class BigQueryDataSource(DataSource):
    def connection_string(self): return "bigquery://<project>/<dataset>"
```

…then import it in `data_sources/__init__.py`. Nothing else changes.

## 5. Quality dimensions

Native GE covers two dimensions; the framework adds the four that need
warehouse-aware logic. All run warn-and-continue.

| Dimension | Where | How |
|---|---|---|
| Completeness | GE suite | `expect_column_values_to_not_be_null` |
| Uniqueness | GE suite | `expect_column_values_to_be_unique` |
| Freshness | `quality/freshness.py` | `MAX(ts)` vs `now()` lag threshold |
| Volume-drift | `quality/volume_drift.py` | `COUNT(*)` vs rolling `FileState` baseline |
| Schema-drift | `quality/schema_drift.py` | `describe()` vs saved schema snapshot |
| Referential integrity | `quality/referential.py` | anti-join orphan count (ELT pushdown) |

Freshness/volume/schema depend on `runtime.state.FileState` for their baselines —
which is why "files only" still supports stateful checks.

## 6. Warn-and-continue model

- Every expectation and check carries `severity: critical | warning`
  (default `warning`).
- The pipeline **always completes** — no stage halts on a failure, and a failing
  gate does not stop the load.
- Every failure is captured in `warnings_report.md`, critical first.
- Severity is **recorded, not enforced** — flipping to fail-fast later is a
  policy change (`Pipeline` already exposes `has_critical_failure`), not a
  redesign. The CLI's `--fail-on` uses it for the **exit code** only.

## 7. Output (files only)

```
etl_output/
├── runs/<run_id>/
│   ├── run_manifest.json          # full record + lineage + status
│   ├── warnings_report.md         # the detailed warn capture (critical first)
│   └── validation/<suite>_validation.json|md
└── state/
    ├── schema_snapshots/<source>__<table>.json   # schema-drift baseline
    └── row_count_history/<source>__<table>.csv    # volume-drift baseline
```

`run_id = <UTC timestamp>_<8 hex>`; `batch_id = (now − 24h)` rounded to the hour
(matching the Presto batch partitioning already used on the source tables).

## 8. Configuration model (two audiences)

Engineers own the Python layers (`data_sources/`, `core/`, `quality/`,
`runtime/`, `reporting/`). Analysts own YAML only:

- `config/connections/*.yml` — a source/target (`type` picks the connector).
- `config/suites/*.yml` — an asset + expectations (+ severity).
- `config/pipelines/*.yml` — source → extract → transform → target, the per-gate
  suites, and the custom checks.

Secrets are `${ENV_VAR}` references, never literals.

## 9. Execution flow

`Pipeline.run()`:

1. **Extract** — build the source SELECT (incremental filter on `batch_key`), run it.
2. **Gate: raw** — run `suite_raw` on the source + all custom checks.
3. **Transform** — run the ELT SQL steps on the source; the last SELECT is the
   curated payload.
4. **Gate: curated** — run `suite_curated` (typically a query asset).
5. **Load** — write the payload into the target (`append`/`overwrite`/`merge`).
6. **Gate: post** — run `suite_post` on the target.

Returns a `PipelineResult` aggregating all `ValidationOutcome`s + `CheckResult`s,
with `passed`, `has_critical_failure`, and `failure_count`.

## 10. Testing strategy

The connector layer's SQL machinery is dialect-agnostic, so the **entire flow is
exercised against a temporary sqlite database** — extract, transform, load
(including cross-"source" loads), all three GE gates, the four custom checks, and
report generation — **without needing a live Presto/Trino gateway**. Pure units
(connection strings, config parsing, expectation factory, exit-code policy) are
tested directly. Current coverage: **74 tests**.

## 11. Decisions log (locked)

| Decision | Choice |
|---|---|
| Scope | Validation **and** ETL |
| Quality dimensions | All six (completeness, uniqueness, freshness, volume, schema, referential) |
| Failure model | Warn-and-continue + detailed report |
| Results/history | Files only |
| Orchestration | Cron / CLI first (orchestrator-agnostic core) |
| Audience | Engineers (Python) + analysts (YAML) |
| Sources | Multi-source; Presto first, Snowflake + others pluggable under `data_sources/` |
| GE placement | Folded into `core/validate/`, source-agnostic |

## 12. Future extensions

- Airflow / Dagster wrappers over the same CLI (core is orchestrator-agnostic).
- Row-level quarantine (`etl_output/runs/<id>/quarantine/`) for bad-row capture.
- `INSERT … SELECT` pushdown load for in-warehouse, TiB-scale moves.
- Additional connectors (BigQuery, Databricks, Postgres) — one folder each.
- GE Data Docs generation as an optional report format.

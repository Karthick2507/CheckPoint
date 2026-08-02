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
   per-suite validation reports and quarantined rows; baselines persist as
   files (no results DB).
7. **Set-based by default** — same-warehouse work is pushed down as
   `INSERT … SELECT`; rows only enter Python for genuine cross-system moves,
   and then in bounded chunks.
8. **Scoped to the batch** — gates and drift checks measure the slice this run
   processed, not all of history.

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
│   ├── extract/           # read rows (table/query, incremental, streaming)
│   ├── transform/         # ELT: ordered SQL steps run on the source
│   ├── validate/          # Great Expectations (folded-in), source-agnostic
│   │   └── scoping.py     #   narrow an asset to the current batch
│   ├── load/              # loader.py (rows) + pushdown.py (INSERT … SELECT)
│   ├── pipeline_config.py # declarative PipelineConfig
│   ├── schema.py          # SchemaContract: projection + column mapping
│   └── pipeline.py        # the orchestrator (extract→gates→transform→load)
├── quality/               # the 4 non-native checks
│   ├── freshness.py
│   ├── volume_drift.py
│   ├── schema_drift.py
│   ├── referential.py
│   └── stats.py           # median / MAD — robust baselines
├── runtime/
│   ├── run_context.py     # run_id / batch_id / lineage / output layout
│   ├── state.py           # durable baselines (atomic writes, flock, retention)
│   ├── templating.py      # strict, sandboxed Jinja SQL rendering
│   ├── retry.py           # transient-failure retry with backoff
│   └── sql.py             # sql_literal / identifier quoting / batch predicate
├── reporting/             # manifest + warnings report + quarantine + console
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
    def execute(self, sql) -> list[dict]      # shared machinery, with retry
    def stream(self, sql, chunk_size) -> Iterator[list[dict]]   # bounded memory
    def transaction(self) -> Transaction      # atomic multi-statement work
    def describe(self, table) -> list[dict]   # schema introspection
    def capabilities(self) -> Capabilities    # dialect quirks
```

`Capabilities` is not decoration — it drives real behaviour: `identifier_quote`
quotes emitted SQL (so a column named `order` works), and
`supports_transactions` decides whether a destructive load can be made atomic or
must be reported as `atomic=False`.

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
| Volume-drift | `quality/volume_drift.py` | `COUNT(*)` vs **median** baseline (± tolerance) |
| Schema-drift | `quality/schema_drift.py` | `describe()` vs saved schema snapshot |
| Referential integrity | `quality/referential.py` | anti-join orphan count (in-warehouse) |

Volume/schema depend on `runtime.state.FileState` for their baselines.

**Scope checks to the batch** with `batch_key` (or `batch_filter`). Unscoped,
each of these reads all history, which is slower every run *and* frequently
wrong:

- *Volume* — on an append-only table the total only grows, so the baseline
  chases it and a failed batch is invisible (100k historical rows + 0 new rows
  still counts ~100k).
- *Freshness* — `MAX(ts)` finds any fresher historical row, so a month-old
  batch reports healthy.
- *Referential integrity* — one historical orphan fails the check forever
  regardless of today's data. Only the **child** side is scoped; parents may
  legitimately predate the batch.

Schema-drift is deliberately *not* batch-scoped: schema is a property of the
table, not of a batch.

**Volume-drift baselines are robust.** The centre is the **median** (a mean is
dragged by the very spikes it should catch), runs that fail are recorded as
anomalies and excluded from later baselines, and nothing is judged until
`min_history` observations exist.

## 6. Warn-and-continue model

- Every expectation and check carries `severity: critical | warning`
  (default `warning`).
- The pipeline **always completes** — no stage halts on a failure, and a failing
  gate does not stop the load.
- Every failure is captured in `warnings_report.md`, critical first.
- Severity is **recorded, not enforced** — flipping to fail-fast later is a
  policy change (`Pipeline` already exposes `has_critical_failure`), not a
  redesign. The CLI's `--fail-on` uses it for the **exit code** only.

Operational failures (a bad table, an auth error, a missing suite) are captured
too: they become `StageError` entries rather than escaping `run()`, so a broken
run still produces a manifest and a report naming the stage that failed.

## 7. Output (files only)

Two roots, with different lifetimes — this distinction matters:

```
etl_output/                        # DISPOSABLE, per run (gitignored)
└── runs/<run_id>/
    ├── run_manifest.json          # full record + lineage + status
    ├── warnings_report.md         # the detailed warn capture (critical first)
    ├── validation/<suite>_validation.json|md
    └── quarantine/<suite>__<expectation_id>.csv   # the offending rows
                    └── ….sql      # query locating them, when GE supplies one

state/                             # PERSISTENT, across runs (NOT gitignored)
├── schema_snapshots/<source>__<table>.json   # schema-drift baseline
└── row_count_history/<source>__<table>.csv    # volume-drift baseline
```

**State must outlive the run.** It deliberately sits outside `etl_output/`:
when baselines lived under that (gitignored, per-run) tree, every CI, cron, or
container run started empty, so schema-drift and volume-drift reported "first
observation" forever and could never detect anything. Point `--state-dir` at a
durable volume, or commit it. Writes are atomic and flock-guarded so concurrent
runs cannot corrupt a baseline, and history is capped by `max_history`.

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

All SQL in a pipeline (transform steps, source query, suite query assets,
`batch_filter`) is rendered with Jinja against `batch_id`, `run_id`, `pipeline`,
`env` and the pipeline's `vars`. Rendering is **strict**: an unknown `{{ name }}`
fails the stage rather than producing a blank predicate that would silently
match nothing and look like an empty batch.

## 9. Execution model

How data moves is chosen by `execution: auto | rows | pushdown`:

| Mode | What runs | Use for |
|---|---|---|
| **pushdown** | `INSERT INTO target SELECT …` in the warehouse; no rows enter Python | Same-warehouse work at any scale — cost independent of row count |
| **rows** | read into Python, write back as `INSERT … VALUES` | Moving data *between* systems (Presto → Snowflake) |
| **stream** | `fetchmany` chunks piped straight into the target | Large cross-system moves; memory bounded by `chunk_size`, not table size |

`auto` picks pushdown when source and target are the same connection, else rows.
Streaming is opt-in (`extract.stream`) and applies to the row path; it declines
(recording why, never erroring) when a transform needs a materialized set or the
load is destructive.

**Load safety.** Destructive modes (`overwrite`, `merge`) refuse to run with an
empty payload — a late upstream batch must not delete a table and put nothing
back — unless `allow_empty: true`. Delete and insert run in one transaction, so
a failure part-way rolls back; targets that cannot roll back (Trino/Presto over
Hive-like connectors) declare `supports_transactions=False` and the load is
reported with `atomic=False` rather than pretending.

## 10. Schema contract

`source.columns` declares the columns a pipeline reads and their names on the
target — projection and mapping in one place:

```yaml
source:
  columns:
    request__transaction_id: transaction_id
    request__event_time: event_time
  strict_columns: true
```

Without it the extract is `SELECT *`, and an upstream column addition, removal,
or reorder flows straight to the target with nothing noticing. The contract also
pins the payload before a load: `strict_columns` makes a row missing a declared
column an error rather than a silent NULL. With no contract declared the
framework at least insists the rows agree with each other — the loader takes its
columns from row 0, and previously dropped every value under a key row 0 lacked.

## 11. Reliability

- **Retries.** Transient failures (timeouts, resets, 502/503/504, gateway
  errors) retry with exponential backoff and jitter. Permanent failures
  (missing table, syntax error, permission denied) never retry — they cannot
  succeed and retrying only delays the report. **Reads retry; writes do not**
  unless the caller opts in, because re-issuing a partially applied `INSERT` is
  how duplicate rows appear.
- **Resources.** One GE context serves every gate (a fresh ephemeral context per
  gate re-registered the datasource and opened another engine), connections
  resolve once per run, and `run()` disposes every engine in a `finally` so a
  long-lived scheduler process does not accumulate pools.

## 12. Execution flow

`Pipeline.run()` — never raises:

1. **Extract** — build the source SELECT (incremental filter on `batch_key`).
   Pushdown skips materialization entirely.
2. **Gate: raw** — `suite_raw` on the source + all custom checks.
3. **Transform** — ELT SQL on the source; in pushdown the curated SELECT is
   kept for `INSERT … SELECT` instead of being executed.
4. **Gate: curated** — `suite_curated`.
5. **Load** — into the target, unless an upstream stage failed.
6. **Gate: post** — `suite_post` on the target.

Each gate is narrowed to the current batch when its asset declares `batch_key`.
Returns a `PipelineResult` aggregating `ValidationOutcome`s, `CheckResult`s and
`StageError`s, with `passed`, `has_critical_failure`, and `failure_count`.

## 13. Testing strategy

The connector layer's SQL machinery is dialect-agnostic, so the **entire flow is
exercised against a temporary sqlite database** — extract, transform, load
(including cross-"source" loads), all three GE gates, the four custom checks, and
report generation — **without needing a live Presto/Trino gateway**. Pure units
(connection strings, config parsing, expectation factory, exit-code policy) are
tested directly, and every P0-P2 fix ships with a test that first reproduces
the original defect. Current coverage: **336 tests**.

## 14. Decisions log (locked)

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

## 15. Future extensions

- Airflow / Dagster wrappers over the same CLI (core is orchestrator-agnostic).
- Additional connectors (BigQuery, Databricks, Postgres) — one folder each.
- GE Data Docs generation as an optional report format.

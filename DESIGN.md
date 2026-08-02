# CheckPoint — Design

How the framework works internally, and **why** each piece is the way it is.
For installation and usage, see [`README.md`](README.md).

---

## Table of contents

1. [Purpose](#1-purpose)
2. [Principles](#2-principles)
3. [Layered architecture](#3-layered-architecture)
4. [The connector seam](#4-the-connector-seam)
5. [Extract](#5-extract)
6. [Transform](#6-transform)
7. [Validate](#7-validate)
8. [Quality checks](#8-quality-checks)
9. [Load](#9-load)
10. [Schema contract](#10-schema-contract)
11. [Runtime services](#11-runtime-services)
12. [Reporting](#12-reporting)
13. [Data flow](#13-data-flow)
14. [Control flow](#14-control-flow)
15. [Reliability](#15-reliability)
16. [Configuration model](#16-configuration-model)
17. [Testing strategy](#17-testing-strategy)
18. [Decisions log](#18-decisions-log)
19. [Future extensions](#19-future-extensions)

---

## 1. Purpose

Two jobs, one framework:

1. **ETL** — extract from a source, transform, load to a target.
2. **Data quality** — validate at every stage with Great Expectations plus custom warehouse-aware checks.

The organising idea:

> **Great Expectations is not "the ETL".** It is the **quality gate between stages**. Extract and Load are plumbing; Transform is business logic; GE and the custom checks enforce the contracts *between* them.

```
SOURCE ─► EXTRACT ─►[gate: raw]─► TRANSFORM ─►[gate: curated]─► LOAD ─►[gate: post]─► TARGET
                         │                          │                       │
                         └──────── Great Expectations + custom checks ───────┘
                                    (warn-and-continue, severity-tagged)
```

Three gates rather than one, because each answers a different question:

| Gate | Question | Catches |
|---|---|---|
| **raw** | Is the source fit to process? | Upstream problems, before you waste compute |
| **curated** | Did the transform produce what we intended? | Logic bugs in your own SQL |
| **post** | Did the data actually land? | Load failures, partial writes, target drift |

---

## 2. Principles

1. **Config-driven** — pipelines, connections, and suites are declarative YAML.
2. **Source-agnostic** — everything depends on the `DataSource` interface, never a concrete database.
3. **Idempotent & incremental** — runs filter by `batch_key = batch_id`; a re-run is safe.
4. **Quality-gated** — contracts between every stage.
5. **Warn-and-continue** — nothing blocks the run; every failure is captured and tagged `critical` or `warning`.
6. **Observable, files-only** — each run writes a manifest, a warnings report, per-suite results, and quarantined rows. No results database.
7. **Set-based by default** — same-warehouse work is pushed down as `INSERT … SELECT`; rows enter Python only for genuine cross-system moves, and then in bounded chunks.
8. **Scoped to the batch** — gates and drift checks measure the slice this run processed, not all of history.
9. **Honest about limits** — where a guarantee cannot be provided (Trino cannot roll back DML), the framework reports that rather than pretending.

---

## 3. Layered architecture

```
CheckPoint/
├── data_sources/          # the source-agnostic seam
│   ├── base.py            #   DataSource ABC: execute / stream / transaction / describe
│   ├── registry.py        #   @register + create_data_source factory
│   ├── config.py          #   connection YAML loader (${ENV} interpolation)
│   ├── presto/            #   Presto/Trino (Bearer-token auth)
│   ├── snowflake/         #   Snowflake
│   └── sqlite/            #   SQLite — zero-infrastructure local runs
├── core/
│   ├── extract/           #   reads: incremental, projected, optionally streamed
│   ├── transform/         #   ELT: ordered SQL steps run on the source
│   ├── validate/          #   Great Expectations, source-agnostic
│   │   ├── framework.py   #     GE wiring + normalized ValidationOutcome
│   │   ├── suite_config.py#     suites, expectation ids, severity
│   │   ├── scoping.py     #     narrow an asset to the current batch
│   │   └── expectations.py#     snake_case -> GE expectation factory
│   ├── load/
│   │   ├── loader.py      #     row-based append / overwrite / merge / stream
│   │   └── pushdown.py    #     INSERT … SELECT in the warehouse
│   ├── schema.py          #   SchemaContract: projection + column mapping
│   ├── pipeline_config.py #   declarative PipelineConfig
│   └── pipeline.py        #   the orchestrator
├── quality/               # the four non-native checks
│   ├── base.py            #   QualityCheck ABC + batch scoping + CheckResult
│   ├── freshness.py  volume_drift.py  schema_drift.py  referential.py
│   └── stats.py           #   median / MAD — robust baselines
├── runtime/
│   ├── run_context.py     #   run_id / batch_id / lineage / output layout
│   ├── state.py           #   durable baselines (atomic writes, flock, retention)
│   ├── templating.py      #   strict, sandboxed Jinja SQL rendering
│   ├── retry.py           #   transient-failure retry with backoff
│   └── sql.py             #   sql_literal / identifier quoting / batch predicates
├── reporting/             # manifest, warnings report, quarantine, console
├── config/                # analyst-facing YAML
├── examples/quickstart/   # a complete runnable pipeline, no infrastructure
├── cli.py
└── tests/                 # 338 tests, sqlite-backed, exercising every layer
```

**Dependency direction:** `cli → core → {data_sources, quality, runtime}`, and `reporting → core`. Nothing in `data_sources/` or `runtime/` knows about pipelines, which is what keeps the seam clean.

---

## 4. The connector seam

The pivotal design element. Every source implements one contract:

```python
class DataSource(ABC):
    type: str
    def connection_string(self) -> str                          # SQLAlchemy URL
    def engine_kwargs(self) -> dict                             # connect_args / auth
    def execute(self, sql, retry=None) -> list[dict]            # with retry on reads
    def stream(self, sql, chunk_size) -> Iterator[list[dict]]   # bounded memory
    def transaction(self) -> Transaction                        # atomic multi-statement
    def describe(self, table) -> list[dict]                     # schema introspection
    def capabilities(self) -> Capabilities                      # dialect facts
```

**Why this works so well with Great Expectations:** GE's Fluent `add_sql(connection_string, kwargs)` is dialect-driven. So `trino://`, `snowflake://`, and `sqlite://` all validate through the *identical* GE code path — the connector merely supplies the URL and auth. The same `connection_string` + `engine_kwargs` also feed direct execution, giving **one connection code path** for both GE and raw SQL.

**`Capabilities` is not decoration.** It drives real behaviour:

| Field | Effect |
|---|---|
| `identifier_quote` | Quotes emitted SQL, so a column named `order` or `select` works |
| `supports_transactions` | Decides whether a destructive load is atomic, or must be reported `atomic=false` |
| `supports_pushdown` | Whether set-based execution is viable |
| `dialect` | Diagnostics and dialect-specific SQL |

**Adding a source** is one folder plus one import — see [README § Extending](README.md#extending). Nothing else in the framework changes.

---

## 5. Extract

Builds and runs the source `SELECT`.

- **Incremental** — `WHERE <batch_key> = <batch_id>` aligns with the warehouse's own partitioning, so the engine can prune.
- **Projected** — the [schema contract](#10-schema-contract) supplies the column list. Without one it is `SELECT *`, which leaves you exposed to upstream drift.
- **Streaming** — `stream()` yields `fetchmany` chunks so memory is bounded by `chunk_size` rather than by the result set.

In **pushdown** mode extract does not run at all: the SELECT it *would* have issued is embedded into the load statement instead.

---

## 6. Transform

ELT by design: transformations are **SQL executed in the warehouse**, not Python operating on rows.

`transform:` is an ordered list. All but the last statement are setup DDL (create a view, a temp table); the **last statement is the curated SELECT** that defines the output.

- **rows mode** — `apply()` executes the final SELECT and materializes the payload.
- **pushdown mode** — `prepare()` runs the setup steps but returns the final SELECT *unexecuted*, so it can be embedded in `INSERT … SELECT`. The warehouse never ships rows back.

---

## 7. Validate

`GEValidationFramework` maps a declarative suite onto GE's Fluent objects:

```
DataSource ─► GE datasource ─► asset (table|query) ─► batch definition
                                                          │
suite YAML ─► expectations (+ meta id) ─► ExpectationSuite ┴─► ValidationDefinition ─► run
                                                                                        │
                                                          normalized ValidationOutcome ◄┘
```

**Severity resolution is id-based, and this matters.** Each expectation carries a stable `id`, stamped into GE's `meta` and round-tripped onto the result. Matching results back to config by *kwargs* — the obvious approach — fails, because GE normalises and augments kwargs; the fallback then assigned every same-type expectation the *first* one's severity. A `critical` null-check would be reported as a `warning`. The id makes the mapping exact.

**Batch scoping** (`core/validate/scoping.py`) rewrites a batch-scoped table asset into a query restricted to the run's batch (query assets are wrapped). Without it every gate scans all history, which is:

- **Wrong** — a thousand bad rows in today's batch are diluted into billions of good historical rows, so a `mostly:` threshold passes. Conversely, one historical duplicate makes `expect_column_values_to_be_unique` fail forever.
- **Ruinously expensive** — every expectation full-scans a TiB table on every run.

`ValidationOutcome` is a normalized, JSON-safe result type. Reporting depends on *it*, not on GE — so the validation engine could be swapped without touching the reporting layer.

---

## 8. Quality checks

Native GE covers two dimensions well. The other four need warehouse-aware logic:

| Dimension | Where | How |
|---|---|---|
| Completeness | GE suite | `expect_column_values_to_not_be_null` |
| Uniqueness | GE suite | `expect_column_values_to_be_unique` |
| Freshness | `quality/freshness.py` | `MAX(ts)` vs `now()` lag threshold |
| Volume-drift | `quality/volume_drift.py` | `COUNT(*)` vs **median** baseline ± tolerance |
| Schema-drift | `quality/schema_drift.py` | `describe()` vs saved snapshot |
| Referential integrity | `quality/referential.py` | anti-join orphan count, in-warehouse |

### Scope them to the batch

Unscoped, each reads all history — slower every run *and* frequently wrong:

- **Volume** — on an append-only table the total only grows, so the baseline chases it and a failed batch is invisible: 100k historical rows + 0 new rows still counts ~100k.
- **Freshness** — `MAX(ts)` finds any fresher historical row, so a month-old batch reports healthy.
- **Referential integrity** — one historical orphan fails the check forever regardless of today's data. Only the **child** side is scoped; parents may legitimately predate the batch.

**Schema-drift is deliberately not batch-scoped** — schema is a property of the table, not of a batch.

### Robust baselines

- **Median, not mean.** A mean is dragged toward the very spikes it should catch; after a few bad runs the anomaly *is* the baseline. MAD is reported alongside as a spread measure.
- **Anomaly exclusion.** Runs that fail are recorded with `status=anomaly` and excluded from future baselines.
- **Minimum history.** Below `min_history` observations the check reports "establishing baseline" rather than judging against one or two samples.
- **Zero baseline is explicit.** `0 → 500 rows` has no meaningful relative deviation, so it is flagged rather than silently dividing.

---

## 9. Load

Two strategies behind one decision:

| Strategy | Mechanism | For |
|---|---|---|
| `pushdown.py` | `INSERT INTO t SELECT …` | Same warehouse, any scale |
| `loader.py` | `INSERT … VALUES`, batched | Cross-system moves |

`merge` in pushdown mode is elegant: the keys to delete are computed *by the warehouse* from the same SELECT, so nothing round-trips through Python.

### Load safety

Three guarantees, each earned from a specific failure mode:

1. **Empty-payload guard.** `overwrite`/`merge` delete before inserting. With an empty payload — a late upstream batch, a transform that filtered everything — that deletes the target and puts nothing back. Such a load is **refused** and reported, unless `allow_empty: true`.
2. **Atomicity.** Delete and insert run in one transaction. A failure part-way rolls back rather than leaving rows deleted and not replaced.
3. **Honest reporting.** Trino/Presto over Hive-like connectors cannot roll back DML. Those sources declare `supports_transactions=False` and the load is reported `atomic=false` — the guarantee is not silently assumed.

---

## 10. Schema contract

`source.columns` declares the columns a pipeline reads and their names on the target — projection and mapping in one place:

```yaml
source:
  columns:
    request__transaction_id: transaction_id
    request__event_time: event_time
  strict_columns: true
```

Two defects this replaces:

- **`SELECT *`** — extract projected everything, so an upstream column addition, removal, or reorder flowed straight to the target with nothing noticing.
- **`rows[0].keys()`** — the loader took its column list from the *first* row, so a later row carrying a different key silently lost that value: no error, no warning, no trace in the report.

With a contract, the payload is conformed to it before the load; `strict_columns` makes a missing declared column an error rather than a silent NULL. **Without** a contract the framework still insists rows agree with each other, so the old silent drop becomes a reported failure.

---

## 11. Runtime services

| Module | Responsibility |
|---|---|
| `run_context.py` | `run_id`, `batch_id`, lineage, output layout |
| `state.py` | Durable baselines for the stateful checks |
| `templating.py` | Strict, sandboxed Jinja SQL rendering |
| `retry.py` | Transient-failure retry with backoff |
| `sql.py` | `sql_literal`, identifier quoting, batch predicates |

### State must outlive the run

State lives in its own root (`state/`), **not** under the per-run output tree. When baselines lived under that gitignored, per-run directory, every CI, cron, or container run started empty — schema-drift and volume-drift reported "first observation" forever and could never detect anything. Two of six quality dimensions were decorative.

Safety properties: **atomic writes** (temp file + `os.replace`) so a torn write cannot poison the next run; **flock-guarded** access so concurrent runs cannot interleave into a corrupt CSV (POSIX only — see [README § Platform notes](README.md#platform-notes)); **retention caps** so files stay bounded; corrupt rows are skipped rather than raising.

### Templating is strict and sandboxed

- **StrictUndefined** — an unknown `{{ name }}` raises. A blank predicate would produce `WHERE batch = ''`, return nothing, and look exactly like a legitimately empty batch. Failing loudly is the only safe behaviour.
- **SandboxedEnvironment** — templates come from config files and must not traverse Python objects.

---

## 12. Reporting

`collect_warnings()` flattens everything into one severity-ranked list, ordered: **operational errors first** (the run did not do its job), then critical, then warnings.

| Artifact | Audience |
|---|---|
| `run_manifest.json` | Machines — full results, lineage, the SQL issued at each stage |
| `warnings_report.md` | Humans — every failure, critical first |
| `validation/*.json\|md` | Per-suite GE detail |
| `quarantine/*.csv` | **The actual offending rows** |
| `quarantine/*.sql` | A query locating them, when GE supplies one |

Quarantine matters because a report saying "412 rows were null" does not tell you *which*. The `.sql` sidecar is often the more useful artifact: for a null-check the offending values are all `NULL`, so the *locating query* is what an analyst actually needs.

---

## 13. Data flow

How data physically moves — the distinction that determines viability at scale.

**Pushdown — data never leaves the warehouse:**

```
┌──────────────────── WAREHOUSE ────────────────────┐
│  source ──► SELECT (your transform) ──► target    │
│                    ▲                              │
└────────────────────┼──────────────────────────────┘
                     │ statements only, no rows
               ┌─────┴─────┐
               │ FRAMEWORK │  issues DELETE + INSERT…SELECT
               └───────────┘  reads back only COUNT(*)
```

Cost is **independent of row count**.

**Rows — data passes through Python:**

```
SOURCE ──SELECT──► [list[dict]] ──INSERT VALUES──► TARGET
                        │
                 schema contract applied
```

**Streaming — bounded memory for large cross-system moves:**

```
SOURCE ──fetchmany(chunk_size)──► [chunk] ──INSERT──► TARGET
         └────────── repeat ──────────┘
```

Measured on 200,000 rows × ~500 B: **183 MB** buffered vs **8 MB** streamed.

**Gates read independently.** Validation gates and quality checks issue their own queries against the source or target — they never consume the payload. That is why they behave identically in pushdown mode, where no payload exists in Python at all.

---

## 14. Control flow

```
run()                                              ── never raises ──
 │
 ├─ setup            create dirs, mint run_id + batch_id
 ├─ resolve source   ──✗─► record StageError, ABORT (nothing can proceed)
 ├─ extract          (skipped in pushdown)   ──✗─► record, continue
 │
 ├─ GATE raw         suite + every check, each independent
 ├─ transform        ──✗─► record, continue
 ├─ GATE curated
 │
 ├─ load             upstream failed?      ──► SKIP
 │                   empty + destructive?  ──► REFUSE
 │                   else                  ──► one transaction
 │
 ├─ GATE post        only if the load ran
 └─ finally          write reports, dispose engines
```

### Invariants

| Guarantee | Rationale |
|---|---|
| **`run()` never raises** | Operational errors become `StageError`s. A run that blows up silently is worse than one that reports what broke. |
| **Reports always written** | Even a failed run yields a manifest and a report naming the failing stage. Written in a `finally`. |
| **Data failures never abort** | A failing gate does not stop the load. Severity is recorded; `--fail-on` decides the exit code. |
| **Operational failures skip dependents** | A failed extract/transform skips the load — a partial or stale write is worse than none. |
| **Independent work continues** | One broken check does not sink the others. |
| **Resources always released** | Engines disposed in a `finally`. |

### Warn-and-continue, precisely

Severity is **recorded, not enforced**. `Pipeline` exposes `has_critical_failure`, and the CLI's `--fail-on` maps it to an exit code. Switching to fail-fast is therefore a *policy* change, not a redesign.

---

## 15. Reliability

**Retries.** Transient failures (timeouts, resets, 502/503/504, gateway errors) retry with exponential backoff and jitter — jitter so a fleet recovering from a gateway restart does not stampede it. Permanent failures (missing table, syntax error, permission denied) **never** retry: they cannot succeed, and retrying only delays the report. A permanent marker beats a transient one, so *"gateway says: table not found"* fails fast.

**Reads retry; writes do not.** Re-issuing a partially applied `INSERT` is how duplicate rows appear. Writes retry only when a caller explicitly opts in. Unrecognised statements are treated as writes — the safe default.

**Resources.** One GE context serves every gate (a fresh context per gate re-registered the datasource and opened another engine), connections resolve once per run, and every engine is disposed in a `finally`.

> Sharing one GE context introduced a subtlety worth recording: two suites may legitimately use the same asset *name* for different data (a raw table and a batch-scoped query). The framework verifies a cached asset actually matches the requested definition and registers a discriminated name when it does not — otherwise the second suite would silently validate the first's data.

---

## 16. Configuration model

Two audiences, cleanly split:

- **Engineers** own the Python layers — `data_sources/`, `core/`, `quality/`, `runtime/`, `reporting/`.
- **Analysts** own YAML only — `config/connections/`, `config/suites/`, `config/pipelines/`.

Adding a table to monitor, a new expectation, or a new pipeline requires **no Python**. Secrets are `${ENV_VAR}` references, never literals.

---

## 17. Testing strategy

The connector layer's SQL machinery is dialect-agnostic, so the **entire flow is exercised against a temporary SQLite database** — extract, transform, load (including cross-source and streaming), all three GE gates, the four custom checks, quarantine, and report generation — **without a live warehouse**. Pure units (connection strings, config parsing, expectation factory, retry classification, exit-code policy) are tested directly.

**Every correctness fix ships with a test that first reproduces the original defect.** Several tests assert the *bug* and the *fix* side by side — for instance, that an unscoped check passes on a bad batch while the scoped one fails. The suite therefore documents *why* each behaviour exists.

Current coverage: **338 tests**.

---

## 18. Decisions log

| Decision | Choice | Rationale |
|---|---|---|
| Scope | Validation **and** ETL | One framework, gates between stages |
| Quality dimensions | All six | Two native GE, four custom |
| Failure model | Warn-and-continue + detailed report | Reporting beats aborting; policy decides blocking |
| Results storage | Files only | No database dependency |
| Orchestration | cron/CLI first | Orchestrator-agnostic core |
| Audience | Engineers (Python) + analysts (YAML) | Config/code split |
| Sources | Multi-source, pluggable | Presto first; Snowflake, SQLite prove the seam |
| GE placement | Folded into `core/validate/` | A layer, not a bolt-on |
| Execution | Pushdown by default, rows for cross-system | Set-based work is the only thing that scales |
| Scoping | Batch-scoped gates and checks | Correctness first, cost second |
| Severity | Stable ids through GE `meta` | kwargs matching is unreliable |
| State | Separate persistent root | Baselines must outlive the run |
| Baselines | Median + anomaly exclusion | A mean is dragged by the anomalies it should catch |
| Retries | Reads only, transient only | Never risk duplicating a write |

---

## 19. Future extensions

- Airflow / Dagster wrappers over the same CLI (the core is orchestrator-agnostic).
- Additional connectors — BigQuery, Databricks, Postgres — one folder each.
- GE Data Docs as an optional report format.
- Partition-swap loads for Trino, to get atomicity where transactions cannot.
- A pluggable validator seam, if a second validation engine is ever wanted.

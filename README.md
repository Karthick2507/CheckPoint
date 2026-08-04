# CheckPoint — ETL & Data Quality Framework

A config-driven **ETL + data-quality framework** built on **[Great Expectations](https://greatexpectations.io/) (1.x Fluent API)** with a **pluggable multi-source connector layer** (Presto/Trino, Snowflake, SQLite — more in one folder each).

You describe pipelines in YAML. The framework extracts, validates, transforms, validates again, loads, and validates once more — writing a full report of everything that happened, and never silently swallowing a failure.

- **Architecture and internals:** [`DESIGN.md`](DESIGN.md)
- **Try it in 3 minutes with no infrastructure:** [Quick start](#quick-start-3-minutes)

---

## Table of contents

1. [What it does](#what-it-does)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation) — [macOS/Linux](#macos--linux) · [Windows](#windows)
4. [Quick start (3 minutes)](#quick-start-3-minutes)
5. [Configuration](#configuration)
6. [Running it](#running-it)
7. [Data flow](#data-flow)
8. [Control flow](#control-flow)
9. [Output: what you get after a run](#output-what-you-get-after-a-run)
10. [Scheduling](#scheduling)
11. [Sharing with your team](#sharing-with-your-team)
12. [Extending](#extending)
13. [Troubleshooting](#troubleshooting)
14. [Platform notes](#platform-notes)
15. [Testing](#testing)
16. [Known limitations](#known-limitations)

---

## What it does

```
SOURCE ─► EXTRACT ─►[gate: raw]─► TRANSFORM ─►[gate: curated]─► LOAD ─►[gate: post]─► TARGET
                         │                          │                        │
                         └──────── Great Expectations + custom checks ───────┘
                                    (warn-and-continue, severity-tagged)
```

Great Expectations is **not** the ETL here — it is the **quality gate between stages**. Extract and Load are plumbing, Transform is your business logic, and GE plus four custom warehouse-aware checks enforce the contracts.

| Layer | Package | Role |
|-------|---------|------|
| Connectors | `data_sources/` | `DataSource` ABC + registry; Presto/Trino, Snowflake, SQLite |
| Extract | `core/extract/` | Incremental reads, optional chunked streaming |
| Transform | `core/transform/` | ELT — your SQL, run in the warehouse |
| Validate | `core/validate/` | Great Expectations, source-agnostic, batch-scoped |
| Load | `core/load/` | `INSERT … SELECT` pushdown, or row-based append/overwrite/merge |
| Quality | `quality/` | Freshness, volume-drift, schema-drift, referential integrity |
| Runtime | `runtime/` | Run context, durable baselines, SQL templating, retries |
| Reporting | `reporting/` | Manifest, warnings report, quarantined rows |
| Orchestrator | `core/pipeline.py` | Chains the stages through the three gates |
| CLI | `cli.py` | `run-pipeline`, `validate`, `list-expectations`, `list-sources` |

---

## Prerequisites

| Requirement | Notes |
|---|---|
| **Python 3.10+** | Developed and tested on **3.11**. 3.10 is the floor (the code uses `X \| Y` type syntax). |
| **pip** | Ships with Python. |
| **~300 MB disk** | Great Expectations and pandas are large dependencies. |
| **Network access to your warehouse** | Only if using Presto/Snowflake. The quick start needs nothing. |

**Only if you are connecting to a real warehouse:**

- **Presto/Trino** — a reachable gateway host, and an auth token if it requires one. On a corporate network this usually means **VPN**.
- **Snowflake** — an account identifier, user, password/token, warehouse, and role. Also `pip install snowflake-sqlalchemy` (not installed by default).

**Nothing else.** No database server, no Docker, no Airflow, no cloud account. The framework is a Python package plus YAML files.

Check your Python:

```bash
python3 --version     # macOS / Linux
python --version      # Windows
```

---

## Installation

Get the code:

```bash
git clone <your-repo-url> CheckPoint
cd CheckPoint
```

> Always install into a **virtual environment**. It keeps this project's large dependencies away from your system Python.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows

**PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

> If PowerShell blocks activation with *"running scripts is disabled"*, run once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Command Prompt (cmd.exe):**
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
```

### Verify the install

```bash
python -m cli list-sources
```

Expected:
```
presto
snowflake
sqlite
trino
```

If that prints, you are ready. (`trino` is an alias for `presto` — same connector.)

### Optional extras

```bash
pip install snowflake-sqlalchemy   # only if you target Snowflake
pip install pytest                 # only if you want to run the test-suite
```

---

## Quick start (3 minutes)

Runs a complete pipeline against a local SQLite file — **no warehouse, no credentials, no network**. It exercises every part of the framework.

**Step 1 — create the demo database:**

```bash
python examples/quickstart/seed.py
```

This makes 7 orders across two batches. Today's batch (`B2`) contains **two deliberate defects**: a NULL customer and a negative amount.

**Step 2 — run the pipeline:**

```bash
python -m cli run-pipeline \
  --pipeline examples/quickstart/pipeline.yml \
  --connections-dir examples/quickstart/connections \
  --state-dir examples/quickstart/state \
  --batch-id B2
```

*(Windows PowerShell: replace the trailing `\` with a backtick `` ` ``, or put it all on one line.)*

**Step 3 — read the result.** You should see:

```
╭──────────────── ETL Pipeline Summary ────────────────╮
│ quickstart_orders  ·  run 20260802T170553_e5c865ca   │
│ CRITICAL FAILURE  — 2 failure(s)                     │
│ extracted 0  ·  transformed 4  ·  loaded 4           │
╰──────────────────────────────────────────────────────╯
┏━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━┳──────────────────┓
┃ Gate    ┃ Result ┃ Suite / Check  ┃ Detail           ┃
┡━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━╇──────────────────┩
│ raw     │   ✗    │ orders_raw     │ 2/3 passed       │
│ curated │   ✗    │ orders_curated │ 1/2 passed       │
│ post    │   ✓    │ orders_post    │ 2/2 passed       │
│ check   │   ✓    │ freshness      │ 1.00h old …      │
│ check   │   ✓    │ volume_drift   │ establishing …   │
│ check   │   ✓    │ schema_drift   │ establishing …   │
└─────────┴────────┴────────────────┴──────────────────┘
```

**Three things to notice — they are the framework's core behaviours:**

1. **It found the defects.** The raw gate caught the NULL customer; the curated gate caught the negative amount.
2. **It completed anyway and loaded 4 rows.** That is *warn-and-continue*: bad data is reported and quarantined, never silently swallowed, but a failing check does not abort the run. You choose whether it blocks, using `--fail-on`.
3. **`extracted 0` is correct, not a bug.** Source and target are the same database, so the framework chose **pushdown**: the work ran as `INSERT … SELECT` inside SQLite and no rows travelled through Python. That is what makes it viable on TiB-scale tables.

**Step 4 — inspect the evidence:**

```bash
cat etl_output/runs/*/warnings_report.md      # every failure, critical first
ls  etl_output/runs/*/quarantine/             # the actual offending rows, as CSV
cat etl_output/runs/*/quarantine/*.csv
```

**Step 5 — see batch-scoping work.** Run the *clean* earlier batch:

```bash
python -m cli run-pipeline \
  --pipeline examples/quickstart/pipeline.yml \
  --connections-dir examples/quickstart/connections \
  --state-dir examples/quickstart/state \
  --batch-id B1
```

All three gates now pass (`3/3`, `2/2`, `2/2`) — because each gate validates only the batch being processed, not the whole table. The defects in `B2` are invisible here, and that is the point.

The run still reports one critical failure: the **freshness** check. `B1` is seeded three days old against a 24-hour threshold, so it is genuinely stale. That is the batch-scoped freshness check doing its job — unscoped, it would have found `B2`'s recent rows and wrongly declared `B1` fresh.

> **On exit codes:** both runs exit `1`, because `--fail-on` defaults to `critical` and each has a critical failure. Add `--fail-on never` to always exit `0` (useful for monitoring), or `--fail-on any` to fail on warnings too.

---

## Configuration

Three kinds of YAML. Analysts own all three; no Python required.

```
config/
├── connections/   # WHERE the data lives   (one file per source/target)
├── suites/        # WHAT "good" means      (expectations)
└── pipelines/     # WHAT runs, in what order
```

### 1. Connection — where the data lives

`config/connections/mrm_presto.yml`

```yaml
connection:
  name: mrm_presto              # pipelines refer to this name
  type: presto                  # presto | trino | snowflake | sqlite
  host: presto-gateway.example.net
  port: 8080
  user: ${PRESTO_USER}          # ${VAR} reads an environment variable
  catalog: mrm_log_flat
  schema: default
  http_scheme: https
  request_timeout: 30
  auth_token: ${PRESTO_AUTH_TOKEN}   # sent as "Authorization: Bearer <token>"
  auth_header: Authorization

  # Transient failures retry with exponential backoff + jitter.
  retry_attempts: 3
  retry_initial_delay: 1
  retry_max_delay: 30
```

**Never put secrets in these files.** Use `${ENV_VAR}` and set the variable in your shell, CI secret store, or scheduler.

<details>
<summary>Snowflake and SQLite examples</summary>

```yaml
connection:
  name: analytics_snowflake
  type: snowflake
  account: xy12345.us-east-1
  user: ${SNOWFLAKE_USER}
  auth_token: ${SNOWFLAKE_PASSWORD}
  database: ANALYTICS
  schema: PUBLIC
  warehouse: ETL_WH
  role: ETL_ROLE
```

```yaml
connection:
  name: local
  type: sqlite
  path: ./data/local.db
```
</details>

### 2. Suite — what "good" means

`config/suites/orders_raw.yml`

```yaml
suite:
  name: orders_raw
  asset:
    type: table                 # table | query
    name: orders
    table_name: orders
    batch_key: batch_id         # validate THIS batch, not all history

expectations:
  - id: customer_present        # stable id → reliable severity + reporting
    type: expect_column_values_to_not_be_null
    column: customer_id
    severity: critical          # critical | warning (default warning)
```

| Field | Meaning |
|---|---|
| `type` | Any Great Expectations expectation, snake_case. List them: `python -m cli list-expectations` |
| `id` | Stable identifier. Auto-assigned by position if omitted — **set it explicitly** so reordering the list does not change report identity |
| `severity` | `critical` or `warning`. Recorded on every result; drives triage and `--fail-on` |
| `batch_key` | Narrows the gate to the run's batch. Strongly recommended |
| `batch_filter` | Arbitrary templated predicate when a single equality is not enough |

A **query asset** validates arbitrary SQL instead of a table:

```yaml
asset:
  type: query
  name: orders_curated
  query: "SELECT id, amount FROM orders WHERE batch_id = '{{ batch_id }}'"
```

### 3. Pipeline — what runs

`config/pipelines/orders_daily.yml`

```yaml
pipeline:
  name: orders_daily
  env: prod
  execution: auto               # auto | pushdown | rows

  vars:                         # available to every SQL template below
    min_amount: 0

  source:
    connection: mrm_presto
    table: orders
    batch_key: batch_id
    columns:                    # schema contract: projection + rename
      order_id: id
      customer_id: customer
    strict_columns: true

  extract:
    mode: incremental           # full | incremental
    limit: 100000               # optional
    stream: false               # chunked reads for big cross-system moves
    chunk_size: 10000

  transform:                    # ELT — runs in the warehouse
    - "SELECT order_id AS id, customer_id AS customer FROM orders WHERE batch_id = '{{ batch_id }}'"

  target:
    connection: analytics_snowflake
    table: ORDERS_CLEAN
    mode: merge                 # append | overwrite | merge | none
    keys: [id]
    allow_empty: false          # never wipe the target with an empty payload

  validate:
    raw: config/suites/orders_raw.yml
    curated: config/suites/orders_curated.yml
    post: config/suites/orders_post.yml

  checks:
    - { type: freshness, target: orders, timestamp_column: created_at, batch_key: batch_id, max_lag_hours: 6, severity: critical }
    - { type: volume_drift, target: orders, batch_key: batch_id, tolerance: 0.25, min_history: 3 }
    - { type: schema_drift, target: orders }
    - { type: referential_integrity, target: orders, child_key: customer_id, parent_table: customers, parent_key: id, batch_key: batch_id }

  schedule: "0 6 * * *"         # documentation only — cron actually runs it
```

### SQL templating

Every SQL string (transform steps, source query, suite query assets, `batch_filter`) is rendered with:

| Variable | Value |
|---|---|
| `{{ batch_id }}` | The batch being processed |
| `{{ run_id }}` | Unique id for this run |
| `{{ pipeline }}` | Pipeline name |
| `{{ env }}` | Environment |
| `{{ your_var }}` | Anything under `vars:` |

Rendering is **strict**: an unknown `{{ name }}` fails the stage rather than rendering empty and silently matching nothing.

### Execution modes

| Mode | What runs | Use for |
|---|---|---|
| **pushdown** | `INSERT INTO target SELECT …` in the warehouse; no rows enter Python | Same-warehouse work, any scale |
| **rows** | Read into Python, write back as `INSERT … VALUES` | Moving data *between* systems |
| **stream** | `fetchmany` chunks piped straight to the target | Large cross-system moves; memory bounded by `chunk_size` |

`auto` picks pushdown when source and target share a connection, otherwise rows. Streaming is opt-in via `extract.stream` and declines (recording why) when a transform or a destructive load makes it impossible.

---

## Running it

### Commands

```bash
python -m cli run-pipeline      # run a full pipeline
python -m cli validate          # run suites only, no ETL
python -m cli list-expectations # discover GE expectation types
python -m cli list-sources      # list registered connector types
```

### `run-pipeline`

```bash
python -m cli run-pipeline \
  --pipeline config/pipelines/orders_daily.yml \
  --connections-dir config/connections \
  --state-dir /var/lib/checkpoint/state \
  --batch-id 20260801120000 \
  --fail-on critical
```

| Option | Default | Purpose |
|---|---|---|
| `--pipeline` | *required* | Path to the pipeline YAML |
| `--connections-dir` | `config/connections` | Directory of connection files |
| `--state-dir` | `state` | **Must persist between runs** — see below |
| `--output-dir` | `etl_output` | Where per-run reports go |
| `--batch-id` | `now − 24h`, hour-rounded | Which batch to process. **Required for backfills and re-runs** |
| `--env` | from config | Override the environment label |
| `--fail-on` | `critical` | Exit-code policy: `critical` \| `any` \| `never` |

### `validate` — quality checks without ETL

```bash
python -m cli validate \
  --connection config/connections/mrm_presto.yml \
  --suite config/suites/orders_raw.yml \
  --suite config/suites/orders_curated.yml
```

Repeat `--suite` for multiple. Add `--no-reports` to print only.

### Exit codes

| Code | Meaning |
|---|---|
| `0` | Success under the chosen `--fail-on` policy |
| `1` | Failure under the chosen policy |

`--fail-on` affects **only the exit code**. The pipeline always runs fully and always writes its reports — that is the warn-and-continue guarantee. Use `critical` for production, `any` for strict CI, `never` for monitoring that should never page.

### ⚠️ `--state-dir` must persist

It holds the schema and row-count baselines that **schema-drift** and **volume-drift** compare against. If it is wiped between runs — a fresh container, a clean CI workspace, a temp directory — those two checks report *"establishing baseline"* forever and **can never detect anything**.

- **Server/cron:** a fixed path like `/var/lib/checkpoint/state`
- **Docker/Kubernetes:** a mounted volume or PVC
- **CI:** a cache/artifact restored between runs
- **Small teams:** commit `state/` to git (it is deliberately *not* gitignored)

---

## Data flow

How the *data* physically moves. This differs by execution mode — the distinction that determines whether the framework survives at scale.

**Pushdown (same warehouse) — data never leaves the database:**

```
┌─────────────────────── WAREHOUSE ───────────────────────┐
│  source table ──► SELECT (transform) ──► target table   │
│                        ▲                                │
└────────────────────────┼────────────────────────────────┘
                         │ statements only
                   ┌─────┴─────┐
                   │ FRAMEWORK │   COUNT(*) for reporting;
                   │  (Python) │   zero data rows
                   └───────────┘
```

The framework issues `DELETE` + `INSERT INTO target SELECT …` and reads nothing back. **Cost is independent of row count.**

**Rows (cross-system) — data passes through Python:**

```
SOURCE ──SELECT──► [Python: list[dict]] ──INSERT VALUES──► TARGET
                          │
                   schema contract applied here
```

Necessary to move Presto → Snowflake. Memory is proportional to the result set, so use `stream: true` for large moves:

```
SOURCE ──fetchmany(10k)──► [chunk] ──INSERT──► TARGET
        └── repeat, bounded memory ──┘
```

**Measured:** 200,000 rows × ~500 B — buffered peak **183 MB**, streamed peak **8 MB**.

**What the gates read:** validation gates and quality checks issue their *own* queries against the source or target. They do not consume the payload, which is why they work identically in pushdown mode where no payload exists in Python.

---

## Control flow

The order of operations, and what happens when something fails.

```
run()
 │
 ├─ 1. Setup ─────── create run dirs, mint run_id + batch_id
 ├─ 2. Resolve ───── open the source connection        ──✗─► record, ABORT (nothing can proceed)
 ├─ 3. Extract ───── (skipped entirely in pushdown)    ──✗─► record, continue
 │
 ├─ 4. GATE: raw ─── suite + all custom checks         ──✗─► record failures, continue
 │                   (each check independent)
 │
 ├─ 5. Transform ─── ELT SQL on the source             ──✗─► record, continue
 ├─ 6. GATE: curated                                    ──✗─► record, continue
 │
 ├─ 7. Load ─────────┬─ upstream stage failed? ─────────► SKIP the load
 │                   ├─ empty payload + destructive? ───► REFUSE (never wipe a target)
 │                   └─ otherwise: one transaction ─────► delete + insert together
 │
 ├─ 8. GATE: post ── only if the load actually ran
 │
 └─ 9. Finish ────── write manifest + warnings + quarantine, dispose engines
```

**The invariants that matter:**

| Guarantee | Why |
|---|---|
| **`run()` never raises** | Operational errors become `StageError` entries. A run that blows up silently is worse than one that reports what broke. |
| **Reports are always written** | Even a failed run produces a manifest and a warnings report naming the stage that failed. |
| **Data failures never abort** | A failing gate does not stop the load. Severity is *recorded*; `--fail-on` decides the exit code. |
| **Operational failures skip dependents** | A failed extract or transform skips the load — writing a partial or stale payload is worse than not writing. |
| **Independent work continues** | One broken check does not sink the other checks or the other gates. |
| **Destructive loads are atomic** | Delete and insert are one transaction. Where a target cannot roll back (Trino), the run reports `atomic: false` rather than pretending. |
| **Resources are always released** | Engines are disposed in a `finally`. |

---

## Output: what you get after a run

Two roots, with **different lifetimes** — this distinction matters:

```
etl_output/                     # DISPOSABLE, per run (gitignored)
└── runs/<run_id>/
    ├── run_manifest.json       # machine-readable: every result + lineage + status
    ├── warnings_report.md      # human-readable: every failure, critical first
    ├── validation/             # per-suite GE results (JSON + Markdown)
    ├── quarantine/             # the actual offending rows, as CSV
    │   └── *.sql               # query to locate them, when GE provides one
    └── logs/

state/                          # PERSISTENT, across runs (NOT gitignored)
├── schema_snapshots/           # schema-drift baselines
└── row_count_history/          # volume-drift baselines
```

| Status | Meaning |
|---|---|
| `passed` | Everything succeeded |
| `warning` | Only `warning`-severity failures |
| `critical` | At least one `critical` failure |
| `error` | An operational failure — the run did not do its job |

`run_id` = `<UTC timestamp>_<8 hex>`. `batch_id` = `now − 24h` rounded to the hour, or whatever you pass to `--batch-id`.

---

## Scheduling

The framework is orchestrator-agnostic. It is a CLI that exits 0 or 1 — anything that can run a command can run it.

### cron (macOS / Linux)

```bash
crontab -e
```

```cron
0 6 * * * cd /opt/checkpoint && /opt/checkpoint/.venv/bin/python -m cli run-pipeline \
  --pipeline config/pipelines/orders_daily.yml \
  --state-dir /var/lib/checkpoint/state \
  >> /var/log/checkpoint/orders_daily.log 2>&1
```

Use **absolute paths** — cron does not inherit your shell environment, including `PATH` or your `PRESTO_AUTH_TOKEN`. Set variables at the top of the crontab or source a file in the command.

### Windows Task Scheduler

```powershell
$action  = New-ScheduledTaskAction -Execute "C:\checkpoint\.venv\Scripts\python.exe" `
  -Argument "-m cli run-pipeline --pipeline config\pipelines\orders_daily.yml --state-dir C:\ProgramData\checkpoint\state" `
  -WorkingDirectory "C:\checkpoint"
$trigger = New-ScheduledTaskTrigger -Daily -At 6am
Register-ScheduledTask -TaskName "CheckPoint orders_daily" -Action $action -Trigger $trigger
```

Or via the Task Scheduler GUI: **Create Task → Actions → Start a program**, with *Start in* set to the project directory.

### GitHub Actions

```yaml
name: orders_daily
on:
  schedule: [{ cron: "0 6 * * *" }]
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -r requirements.txt

      # Restore drift baselines, or the stateful checks are blind
      - uses: actions/cache@v4
        with:
          path: state
          key: checkpoint-state-${{ github.run_id }}
          restore-keys: checkpoint-state-

      - run: python -m cli run-pipeline --pipeline config/pipelines/orders_daily.yml --fail-on critical
        env:
          PRESTO_USER: ${{ secrets.PRESTO_USER }}
          PRESTO_AUTH_TOKEN: ${{ secrets.PRESTO_AUTH_TOKEN }}

      - uses: actions/upload-artifact@v4
        if: always()                      # upload reports even when the job fails
        with: { name: etl-reports, path: etl_output/ }
```

### Airflow

```python
BashOperator(
    task_id="orders_daily",
    bash_command=(
        "cd /opt/checkpoint && .venv/bin/python -m cli run-pipeline "
        "--pipeline config/pipelines/orders_daily.yml "
        "--state-dir /var/lib/checkpoint/state "
        "--batch-id {{ ds_nodash }}000000"
    ),
)
```

Note how Airflow's `ds` maps cleanly onto `--batch-id` — that is what makes backfills work.

---

## Sharing with your team

**What to commit:**

| Commit | Never commit |
|---|---|
| All code | `.venv/` |
| `config/**` (YAML with `${ENV_VAR}` placeholders) | Real tokens or passwords |
| `state/` *(optional — see below)* | `etl_output/` (already gitignored) |
| `requirements.txt`, docs | `*.db` files |

Secrets travel through **environment variables**, never the repo. Give teammates a `.env.example` listing the variables they need, with empty values.

**Handing the project to someone else — they need exactly this:**

```bash
git clone <repo> && cd CheckPoint
python3 -m venv .venv && source .venv/bin/activate    # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
export PRESTO_AUTH_TOKEN=...                          # Windows: $env:PRESTO_AUTH_TOKEN="..."
python -m cli run-pipeline --pipeline config/pipelines/orders_daily.yml
```

Point them at the [quick start](#quick-start-3-minutes) first — it proves their install works without needing any credentials.

**Sharing the `state/` directory.** Baselines are per-environment. Either commit `state/` (simple, fine for one shared environment) or keep it on a durable volume per environment (correct when dev/staging/prod have different data volumes). Do not share one state directory across environments — prod's volumes would poison dev's baselines.

**Sharing results.** `etl_output/runs/<run_id>/` is self-contained: zip it and send it. `warnings_report.md` renders directly in GitHub, Slack, or Confluence.

---

## Extending

### Add a data source

Two files, no changes anywhere else:

```python
# data_sources/bigquery/connector.py
from data_sources.base import Capabilities, DataSource
from data_sources.registry import register

@register("bigquery")
class BigQueryDataSource(DataSource):
    def connection_string(self) -> str:
        self._require("project", "dataset")
        return f"bigquery://{self.config['project']}/{self.config['dataset']}"

    def capabilities(self) -> Capabilities:
        return Capabilities(dialect="bigquery", identifier_quote="`")
```

```python
# data_sources/__init__.py — add the import so @register runs
from data_sources.bigquery import BigQueryDataSource  # noqa
```

Now `type: bigquery` works in any connection file. Validation, quality checks, and both load paths work unchanged.

### Add a quality check

Subclass `QualityCheck`, implement `run()`, and register it in `quality/__init__.py`'s `CHECK_TYPES`. Inherit `batch_key`/`batch_filter` scoping for free from the base class.

---

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'cli'` | Run from the **project root**, or the venv is not active. |
| `Unknown data source type 'x'` | Typo in `type:`, or the connector was not imported in `data_sources/__init__.py`. Check `python -m cli list-sources`. |
| `Connection 'x' not found` | The `name:` inside the connection file must match what the pipeline references — the *filename* is irrelevant. Check `--connections-dir`. |
| Drift checks always say *"establishing baseline"* | `--state-dir` is not persisting. See [the warning above](#️-state-dir-must-persist). |
| `SQL template references an undefined variable` | A `{{ name }}` is not a built-in and is not under `vars:`. This is deliberate — a blank predicate would silently match nothing. |
| Run reports `refused to run destructive 'overwrite' load with an empty payload` | Working as designed: an empty extract would have wiped the target. Investigate upstream; use `allow_empty: true` only if truncation is genuinely intended. |
| `extracted 0` but rows loaded | Correct in **pushdown** mode — no rows pass through Python. |
| Gates fail on old data you already fixed | The suite lacks `batch_key`, so it is validating all history. Add it. |
| `snowflake-sqlalchemy` errors | `pip install snowflake-sqlalchemy`. |
| Presto connection hangs/times out | Usually **VPN**. Verify the host is reachable, and that your token has not expired. |
| `atomic: false` in the report | The target cannot roll back (Trino/Hive). The load ran but was not atomic — this is honest disclosure, not an error. |

**Getting more detail:** every run writes `run_manifest.json` with the full lineage — the exact SQL issued at each stage, timings, and every result. It is the first place to look.

---

## Platform notes

The framework is pure Python and runs on **macOS, Linux, and Windows**. Differences:

| Topic | macOS / Linux | Windows |
|---|---|---|
| Activate venv | `source .venv/bin/activate` | `.\.venv\Scripts\Activate.ps1` |
| Set an env var | `export VAR=value` | PowerShell: `$env:VAR="value"` · cmd: `set VAR=value` |
| Python command | `python3` | `python` |
| Line continuation | `\` | backtick `` ` `` (PowerShell) |
| Scheduling | cron | Task Scheduler |
| Paths in YAML | `/` | `/` works too — use forward slashes everywhere |

### ⚠️ Windows: state file locking

`state/` writes are protected by `fcntl` file locks, which are **POSIX-only**. On Windows the framework detects this and continues **without locking** — writes are still atomic (temp file + replace), so a crash cannot corrupt a baseline, but **two pipelines writing the same `state/` directory at the same time could interleave**.

- Fine: one pipeline at a time, or pipelines with separate `--state-dir` paths.
- Risky: several concurrent runs sharing one state directory on Windows. Give each its own `--state-dir`, or schedule them sequentially.

macOS and Linux are fully lock-protected.

---

## Testing

```bash
pip install pytest
python -m pytest tests/ -q
```

**338 tests.** The connector layer is dialect-agnostic, so the *entire* flow — extract, transform, load (including cross-source and streaming), all three GE gates, the four custom checks, quarantine, and reporting — is exercised end-to-end against **SQLite**, with no live Presto required.

Every correctness fix ships with a test that first reproduces the original defect, so the tests document *why* the behaviour exists, not just that it works.

Run one area:

```bash
python -m pytest tests/test_pipeline.py -q        # orchestration
python -m pytest tests/test_drift_robustness.py -q # drift detection
python -m pytest tests/test_load_safety.py -q      # destructive-load guards
```

---

## Known limitations

Stated plainly so you can plan around them:

- **Not yet exercised against a live Presto or Snowflake.** Everything is verified end-to-end against SQLite, which covers the logic but not gateway auth, Trino's DML limitations, or real partition pruning. Expect first-run surprises there.
- **Snowflake needs `snowflake-sqlalchemy`** installed separately; the connector builds correct URLs but has never opened a live connection.
- **On Presto/Trino targets, `merge` and `overwrite` are not atomic.** Trino over Hive-like connectors cannot roll back DML. The framework reports `atomic: false` instead of pretending — that is disclosure, not a fix. Prefer `append` with a partition swap on Trino.
- **No built-in orchestrator integration** — cron/CLI by design. Airflow/Dagster wrap the same CLI.
- **State locking is POSIX-only** (see [Platform notes](#platform-notes)).
- **`schema_drift` is not batch-scoped** — schema is a property of the table, not a batch. This is intentional.

---

## Where to go next

- **[`DESIGN.md`](DESIGN.md)** — architecture, the connector seam, quality-dimension internals, and the decisions log with rationale.
- **`examples/quickstart/`** — a complete, runnable pipeline to copy from.
- **`config/`** — annotated example configs for Presto and Snowflake.

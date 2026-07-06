# CheckPoint — Hoover → Hoover++ ETL Validation

This repository holds two complementary tools for validating the **Hoover → Hoover++** ETL migration, plus the training docs (`trainingDocs/`) they are derived from.

| Tool | Folder | Role |
|---|---|---|
| **BCV Analyzer** | `BCV_analyzer/` | A CLI **discovery tool** — diffs the SRC (`mrm_log_flat.default.<table>`) schema against the BCV (`etl.public_test1.<table>`) view, mines column usage, and recommends what to backfill. |
| **GE Validation** | `GE_Validation/` | A **regression guardrail** built on Great Expectations — checks that the migration decisions (encoded in `config/<table>.yaml`) still hold, run after run. |

**How they relate (two time horizons, not two steps in one run):** BCV Analyzer is run *once by a human* whenever the schema changes, to discover what changed and decide which columns are confirmed-matching / benign / real bugs. That decision is written into a `GE_Validation/config/<table>.yaml`. GE Validation then runs *repeatedly and automatically* against that frozen config. It reuses BCV's sampling *code* (imports it), not its output — so there is no `BCV → GE` pipeline on every run. The flow is **BCV → (human writes config) → GE runs forever**.

- **Part I** below documents the **GE Validation** framework — start here for concepts, how to run, and per-table mappings.
- **Part II** is the **BCV Analyzer** CLI reference (also mirrored in `BCV_analyzer/README.md`).

---

# Part I — GE Validation (Great Expectations framework)

A Great Expectations (GE / GX) based validation framework for the Hoover → Hoover++ migration, modeled on the reference tool `BCV_analyzer/bcv_analyzer.py`. This document is the Task 1 deliverable: Key Concepts, Source→Target Mappings, documented data-break points, and validation strategy — scoped to the `request` table as the first vertical slice. The pattern generalizes to `ad`, `slot`, `candidate`, `auction`, `ack` (see [Extending to other tables](#extending-to-other-tables)).

All claims below are cited to files under `trainingDocs/`. Where a doc is inconsistent with itself or with `bcv_analyzer.py`, that's called out explicitly rather than silently resolved — surfacing exactly that kind of conflict is one of the stated goals of this exercise.

---

## How to Run

### Prerequisites
1. **VPN** connected — the production Presto/Trino gateway is only reachable over VPN (same requirement as `bcv_analyzer.py`).
2. **A Presto auth token** — see the wiki link in `BCV_analyzer/README.md` for how to generate one.
3. **Python 3.11+**.

### Install
A single install covers everything — `requirements.txt` already includes the `bcv_analyzer.py` libraries this framework reuses (`questionary`, `rich`, `openpyxl`), so you do **not** need to install the BVC requirements separately:

```bash
cd GE_Validation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Run a validation
Use the generic entrypoint and name any table that has a `config/<table>.yaml`:

```bash
python run_validation.py --table request \
  --host presto-gateway.presto.fw1.aws.fwmrm.net:8080 \
  --user <you> --auth-token <token>

python run_validation.py --table slot \
  --host presto-gateway.presto.fw1.aws.fwmrm.net:8080 \
  --user <you> --auth-token <token>
```

Connection args mirror `bcv_analyzer.py` and also read from the same env vars (`PRESTO_HOST`, `PRESTO_USER`, `PRESTO_AUTH_TOKEN`, …), so you can export those once and just run `python run_validation.py --table slot`. Add `--transaction-limit 100` (or `1000`) to sample more rows for the reconciliation step.

Each run does both layers back-to-back for that one table: schema check against the BCV table, then row-level reconciliation. `run_request_validation.py` is kept as a thin back-compat wrapper; new tables should use `run_validation.py --table <name>`.

### Do I run BVC first, then GE?
**No — not at runtime.** GE does not consume `bcv_analyzer.py`'s output; it reuses its *code* (imports its sampling functions) and connects to Presto itself. BVC and GE sit on **two different time horizons:**

- **BVC** is run *once by a human* whenever the schema changes, to discover what changed and decide which columns are confirmed-matching / benign / real bugs. That decision is written into `config/<table>.yaml`.
- **GE** then runs *repeatedly and automatically* against that frozen config as a regression guard. It only needs BVC again when the schema structurally changes and the config must be re-derived.

So the pipeline is *BVC → (human writes config) → GE runs forever*, not *BVC → GE* on every run.

### Verify without a gateway
No VPN/gateway handy? The logic is exercised end-to-end against local sqlite/pandas fixtures:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

---

## Key Concepts

**Hoover vs. Hoover++.** Hoover is the current 7-table ad-serving log model (`request`, `visitor`, `auction`, `candidate`, `ad`, `slot`, `ack`), with heavy duplication of shared context across tables — the `ack` table alone needs 5,000+ fields just to link callbacks back to entities (`MVP Demo about Hoover++.md`, lines 5–12). Hoover++ merges these into one table, pushes unnesting to consumers, splits `ack` into three sub-entities (Ad/Slot/Request Acks), and moves from batch to streaming ingestion (`MVP Demo`, lines 14–19, 80–84).

**Column selection was usage-driven, not arbitrary.** A field was kept if used by ETL, SOS, or Arena; otherwise it was kept only if meaningfully queried via LQS (excluding headless "sa" accounts); everything else was dropped (`MVP Demo`, line 23). `bcv_analyzer.py`'s ETL/SOS/Insights/Arena/LQS/CP/AF/Others usage-threshold logic formalizes exactly this rule — it isn't an invented heuristic, it's the documented column-retention policy made executable.

**Streaming settling time is load-bearing for validation.** Hoover++ is deliberately "inaccurate" for its first ~2 hours until an IVT backfill job joins in (`MVP Demo`, line 32). Any validation run before that window shows false diffs. This is not hypothetical — the `request` diff doc shows network-level row-count mismatches of thousands of rows resolving to exactly 0 on re-run, attributed to "data had NOT settled" (`mrm_log_flat.default.request vs etl.public_test1.request.md`, lines 627–641). **A validation framework must parametrize its query window by an offset (~3–4 hours back from "now"), never validate the current hour.**

**What a BCV actually is.** A Backward Compatible View is not a copy of Hoover — it's a SQL view over Hoover++'s merged data, reshaped to the old Hoover schema (`etl.public_test1.<table>` mirroring `mrm_log_flat.default.<table>`), so old queries and validators run unmodified against the new pipeline (`Hoover++ Validations Event Level.md`, lines 7–24). `BCV_analyzer` — the named reference framework — is a real internal tool that finds columns missing from a BCV and scores whether the omission is acceptable using this same usage-threshold logic (`ack backwards compatible view.md`, lines 56–58).

**The central data-quality principle: every discrepancy is triaged Y/N, not just detected.** Y = documented, expected, semantically equivalent (exclude from failure). N = real regression (needs a fix). This triage is tracked centrally — `Discrepancy Tracker.md` lists 19 tracked L3-level discrepancies with this exact Y/N column; `Event Level (Backward Compatible Views).md` does the same for event-level ones. **This is the one thing a GE suite cannot get from GE's defaults**: a plain `expect_column_values_to_be_equal`-style check will re-fail on every known-benign difference (protobuf-zero-vs-Avro-null, `[]` vs `null`, timestamp/timezone casting) on every single run, forever, unless the exclusion list is encoded as a first-class part of the suite. `config/request.yaml` in this framework is that encoding.

**Quantitative tolerances are already defined and map cleanly onto GE's vocabulary** (`Hoover - Hoover++ Validation Plan.md`, §3): row counts within 0.01% tolerance; non-double fields require exact match; double fields allow <0.01 absolute / <0.1% relative difference. These map directly to `expect_table_row_count_to_be_between` and numeric-tolerance expectations — this is the one area where GE's native primitives fit without any translation layer.

**Sampling contract.** Rows are marked "sampled" via `bitwise_and(request__bit_flags, 576460752303423488) > 0` (bit 59), fed by a dedicated low-rate Kafka partition (`Hoover++ Validations Event Level.md`, lines 32–38). `bcv_analyzer.py`'s `TABLESAMPLE` batch-1 query already filters on this exact flag — confirming the reference tool deliberately reuses the team's existing sampling contract rather than inventing its own. This framework's reconciliation step does the same.

---

## Source → Target Mapping — `request`

**Correction to a natural first assumption:** `Cross-System Field Mapping- Hoover, Hoover++, UBT, and Reporting Prod(WIP).md` (6,510 lines) looks like it should be the Hoover→Hoover++ crosswalk, but it isn't one yet — its "Field in Hoover++" column is blank across all 6,490 data rows (verified programmatically). It documents Hoover→UBT and (rarely) Hoover→Reporting-Prod mappings only; the file is genuinely "(WIP)" as titled. The real Hoover→Hoover++ mapping for `request` lives in `Request fields analysis on BCV.md` and `mrm_log_flat.default.request vs etl.public_test1.request.md`, expressed as same-column-name diffing plus a documented exception list — not an explicit rename table.

| Category | Detail | Source |
|---|---|---|
| Naming | SRC keeps `__`-flattened struct paths (`request__transaction_id`); BCV keeps the **same names** for columns that exist on both sides — this is same-name diffing, not a rename layer | `mrm_log_flat...vs etl...request.md` |
| Rename (documented, **unresolved**) | `batch_id` → `process_batch_id` — but the validation SQL later in the same source still queries `batch_id`. Flagged as a doc/code inconsistency, not silently reconciled | `Request fields analysis on BCV.md` line 28 vs diff doc line 4183 |
| Dropped (LQS-internal) | `__path__`, `__offset__`, `__file_size__`, `__footer_size__` — matches `bcv_analyzer.py`'s `exclude.csv` exactly | `Request fields analysis on BCV.md`, "Excluded Columns" |
| Dropped (bulk, confirmed intentional) | 311 `inventory__asset_chain__*` and ~302 `inventory__site_section_chain__*` columns absent from the H++ view — dominated by revenue, priority/rule, funnel-metrics, and order/listing sub-fields. Confirmed as a discussed decision (28/05/2026), not an oversight | diff doc lines 2071–3560 |
| Type change (documented, requires normalization) | `request__timestamp`: SRC `timestamp(3)` → BCV `timestamp(3) with time zone`; BCV uses `from_unixtime()` vs Hoover's direct cast | `Request fields analysis on BCV.md` lines 33–35 |
| Type change (likely bug, tracked as issue) | `execution_networks__...__phase_metrics__value`: SRC `array(array(array(bigint)))` → BCV `array(array(array(integer)))` — source protobuf field is `uint32`, so `integer` narrows it; flagged, not silently accepted | same doc, line 36 |
| Value semantics | Unset repeated fields: `[]` (Hoover, a known bug in old raw→Avro conversion) vs `null` (Hoover++, correct). One level deeper: `[[]]` vs `[None]` | same doc, "Major Categories of Diff" #1–2 |
| Value semantics (expected, timing-dependent) | Postbid-IVT-dependent fields (`client_facing_ivt_reason_flag`, `flags`, `mrc_compliance_label`, `traffic_type`) differ only because the validated H++ build lacked postbid IVT processing at validation time | same doc, lines 127–152 |
| Logic change | `Audience` entity is instantiated in H++ only when `audience_item_ids`/`kv_term_ids` is non-null (Hoover always instantiates it) — intentional, avoids empty entities | same doc, line 148 |

**Auto-suppressed "known equivalences"** already baked into the team's existing validation tooling — this framework reuses them verbatim rather than re-deriving them:
- `request__yield_optimization_ids`: `[]` (SRC) ≡ `null` (BCV)
- `request__client_facing_ivt_reason_flag`: `null` (SRC) ≡ `0` (BCV)
- Generic null-equivalence group: `['', '0', '\N', 'false', 'none', 'null']`
- Generic empty-collection-equivalence group: `['', '[]', '\N', 'none', 'null', '{}']`

**Confirmed-matching baseline** (safe to encode as passing schema expectations today): `request__context__rbp_device_type`, `rbp_platform`, `inventory__asset_chain__role`/`network_id`, `inventory__site_section_chain__role`/`network_id`, `visitor__dma_code_id`, `visitor__country`, `request_info__slot_ad_unit_ids`, `execution_networks__role`.

---

## Potential Data Break Points

1. **Validating too early.** Querying before the ~3–4 hour settling window produces false row-count and field mismatches that aren't bugs — the single most likely way to generate noise. Every checkpoint run in this framework parametrizes its time window; never validates "now."
2. **Silent null-semantics false positives.** Without the equivalence-group normalization, a raw string/value comparison (as in `bcv_analyzer.py`'s current `compare_value_validation_results`) will flag `[]` vs `null`, `0` vs `null`, etc. as mismatches on every run. This framework normalizes known-equivalent values *before* comparing, so only genuinely new divergences surface.
3. **Undocumented reappearance of dropped columns.** If a future BCV view change re-adds one of the bulk-dropped `inventory__asset_chain__*`/`inventory__site_section_chain__*` columns, that's a schema change nobody decided on — worth a positive `expect_column_to_not_exist`-style check on the intentionally-dropped set, not just checks on what should exist.
4. **The `batch_id`/`process_batch_id` rename inconsistency.** Until resolved, any hand-written SQL against the BCV view risks silently querying the wrong (possibly empty or stale) column. Tracked as an explicit open issue in `config/request.yaml`, not treated as either "matched" or "excluded."
5. **The `phase_metrics__value` type narrowing (`bigint`→`integer`).** If the source protobuf field genuinely is `uint32`-range, this may be silently truncating values above `2^31-1` rather than being a harmless type relabel. Tracked as an open issue, not auto-passed.

## Validation Strategy

Two layers, matching the team's existing two-layer approach (`Hoover - Hoover++ Validation Plan.md`):

1. **Schema-level** — does the BCV table have the columns this mapping says it should, with the types this mapping says it should? Implemented as a GE Expectation Suite generated directly from `config/<table>.yaml`'s confirmed-matching and known-type-diff lists (see [`ge_validator/schema_suite.py`](GE_Validation/ge_validator/schema_suite.py)).
2. **Row-level reconciliation** — sample rows via the same `TABLESAMPLE` + sampled-bit-flag contract `bcv_analyzer.py` already uses (reused, not reimplemented — see [`ge_validator/reconciliation.py`](GE_Validation/ge_validator/reconciliation.py)), normalize known-equivalent values, then assert column-pair equality per matched column via GE. Known-issue columns are still checked and reported, but tagged separately from unexpected new failures — preserving the team's Y/N triage discipline instead of collapsing everything into a single pass/fail.

## Tables covered

| Table | Config | Join keys | Notable |
|---|---|---|---|
| `request` | `config/request.yaml` | `request__transaction_id` | 613-column bulk struct drops; timestamp timezone type diff; `batch_id`→`process_batch_id` open issue |
| `slot` | `config/slot.yaml` | `request__transaction_id`, `slot__index` *(int)* | 8 benign `avails` int→bigint widenings; the same `phase_metrics__value` narrowing bug; a real UTC-vs-local-time value bug on `request__timestamp`; dropped `visitor__identity_user_ids__*`; a `request__hashed_key_value` mismatch still under investigation |

`slot` is the sharpest illustration of why the Y/N triage matters: of its 92 unmatched fields (16.55% per `Slot fields analysis on BCV.md`), the large majority are the same benign `[]`-vs-`null` / `[None]`-vs-`null` semantics the equivalence groups absorb, while only four are genuine open bugs — the framework keeps those four visible instead of letting them drown in the noise.

## Extending to further tables

The same `[]`-vs-`null` / protobuf-default-vs-Avro-null root cause recurs across every table (confirmed in `ack`, `candidate`, `auction` — see inventory pass), so extending this framework means adding a new `config/<table>.yaml` with that table's confirmed-matching columns, known type diffs, and equivalence exceptions, then running `python run_validation.py --table <name>`. The code in `ge_validator/` is already table-agnostic — no code change is needed to onboard a new table, only a config and a citation trail.

---

# Part II — BCV Analyzer (reference CLI tool)

A command-line tool for analyzing schema differences between the **SRC** (source) tables and **BCV** (Backward Compatible View) tables in Presto/Trino, and generating backfill recommendations based on column usage data.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Interactive Mode](#interactive-mode)
  - [CLI Arguments](#cli-arguments)
  - [Environment Variables](#environment-variables)
- [Run Modes](#run-modes)
- [How It Works](#how-it-works)
  - [1. Schema Comparison](#1-schema-comparison)
  - [2. Column Size Lookup](#2-column-size-lookup)
  - [3. Column Exclusion](#3-column-exclusion)
  - [4. Usage Data Query](#4-usage-data-query)
  - [5. Analysis Summary](#5-analysis-summary)
- [Analysis Rules](#analysis-rules)
- [Output](#output)
  - [`<table>_result.csv`](#table_resultcsv)
  - [JSON Files](#json-files)
- [Matched Column Value Validation](#matched-column-value-validation)
  - [Triggering Validation](#triggering-validation)
  - [Network ID Filter](#network-id-filter)
  - [Per-Table Join Keys](#per-table-join-keys)
  - [Parent Structure Node Exclusion](#parent-structure-node-exclusion)
  - [Batching Strategy](#batching-strategy)
  - [Comparison Logic](#comparison-logic)
  - [Validation Summary Output](#validation-summary-output)
  - [Validation Output Files](#validation-output-files)
- [Supported Tables](#supported-tables)
- [Thresholds Reference](#thresholds-reference)

---

## Overview

BCV Analyzer compares the schema of a source table (`mrm_log_flat.default.<table>`) against its corresponding BCV table (`etl.public_test1.<table>`), identifies **DIFF** columns (columns present in SRC but missing in BCV), checks whether those columns are used by ETL or SOS, queries Presto for their historical usage data, and produces a prioritized backfill recommendation report.

```
SRC Table  ──┐
             ├──► Schema Comparison ──► MATCHED - TYPE DIFF columns ──► (magenta panel in summary)
BCV Table  ──┘         │
                       ▼
                  exclude.csv filter (removed from all further steps)
                       │
                       ▼
                  DIFF Columns ──► ETL / SOS Usage Check ──► Presto Usage Query ──► Analysis Summary + <table>_result.csv
                                                               (batch, 500/query)
                                                                       │
                                                                       ▼
                                          Value Validation (MATCHED + MATCHED - TYPE DIFF columns)
                                          ──► <table>_validation_report.md
                                          ──► <table>_result.csv  (validation column)
```

---

## Project Structure

```
BCV/
├── bcv_analyzer.py          # Main application
├── requirements.txt         # Python dependencies
├── etl_fields.json          # ETL-used fields, grouped by table name
├── sos_fields.csv           # SOS-used fields (columns: table, column)
├── exclude.csv              # Columns to skip entirely (columns: table, column)
├── field_size/              # Column size data (one .xlsx per table)
│   ├── request_raw_size_in_TiB.xlsx
│   ├── ad_raw_size_in_TiB.xlsx
│   ├── slot_raw_size_in_TiB.xlsx
│   ├── candidate_raw_size_in_TiB.xlsx
│   ├── auction_raw_size_in_TiB.xlsx
│   └── ack_raw_size_in_TiB.xlsx
├── output/                  # Generated output (auto-created)
│   ├── <table>_result.csv             # Main analysis result (+ validation column after validation)
│   ├── <table>_validation_report.md  # Detailed value validation report
│   ├── <table>.json                  # SRC column list
│   └── bcv_<table>.json              # BCV column list
└── tests/
    └── test_bcv_analyzer.py
```

---

## Requirements

- Python 3.11+
- Access to a Presto/Trino gateway
- Column size `.xlsx` files in the `field_size/` directory
- `etl_fields.json` in the project root for ETL usage lookup
- `sos_fields.csv` in the project root for SOS usage lookup
- `exclude.csv` in the project root to skip specific columns _(optional; create with `table,column` headers)_

---

## Installation

```bash
# Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> **Tip — Increase Terminal Scrollback Lines**
>
> The Analysis Summary output can be lengthy. It is recommended to increase your terminal's scrollback buffer to **30 000** lines so you can scroll back through the full results.
>
> **iTerm2 setup:**
> 1. Open iTerm2 → **Settings** → **Profiles** → select your profile → **Terminal** tab
> 2. Set **Scrollback lines** to `30000`

---

## Usage

### Recommended Execution

```bash
python bcv_analyzer.py \
  --host presto-gateway.presto.fw1.aws.fwmrm.net:8080 \
  --user yuwang \
  --auth-token cfeac6c3-db15-4e03-9bad-e0e96ae4932a
```

To get your own token follow the wiki guide:
https://freewheel.atlassian.net/wiki/spaces/DDEU2/pages/528557481/Presto+Gateway+Userguide#Geta-a-token-with-LDAP-account

> **Note:** You must be connected to VPN to reach the production Presto gateway.

### Interactive Mode

```bash
python bcv_analyzer.py
```

You will be prompted to:
1. **Select a table** — choose from the supported tables using ↑/↓ arrow keys
2. **Select a run mode** — Full Run or Validation Only (see [Run Modes](#run-modes))

### CLI Arguments

| Option              | Description                                      | Default                           |
|---------------------|--------------------------------------------------|-----------------------------------|
| `--host`            | Presto host                                      | `$PRESTO_HOST`                    |
| `--port`            | Presto port                                      | `$PRESTO_PORT` or `8080`          |
| `--user`            | Presto user                                      | `$PRESTO_USER`                    |
| `--request-timeout` | Request timeout (seconds)                        | `$PRESTO_REQUEST_TIMEOUT` or `5`  |
| `--auth-token`      | Auth token (`Authorization: Bearer ...`)         | `$PRESTO_AUTH_TOKEN`              |
| `--auth-header`     | Custom auth header name                          | `$PRESTO_AUTH_HEADER`             |
| `--table`           | Skip table selection prompt                      | _(interactive)_                   |
| `--help`            | Show help message                                |                                   |

### Environment Variables

```bash
PRESTO_HOST=presto.example.com PRESTO_USER=alice python bcv_analyzer.py --table request
```

---

## Run Modes

| Mode                | Description |
|---------------------|-------------|
| **Full Run**        | Queries Presto for **all** DIFF columns. |
| **Validation Only** | Skips schema comparison and usage analysis entirely. Reads the previously generated `output/<table>_result.csv` and proceeds directly to value validation. Requires a result CSV to already exist. |

---

## How It Works

### 1. Schema Comparison

The tool runs `DESCRIBE` on both the SRC and BCV tables, then assigns each column one of three statuses:

| Status | Condition |
|--------|-----------|
| `MATCHED` | Column exists in both tables with the **same** type |
| `MATCHED - TYPE DIFF` | Column exists in both tables but with **different** types |
| `DIFF` | Column is present in SRC but **missing** from BCV entirely |

`MATCHED - TYPE DIFF` columns are shown in a dedicated **magenta panel** in the Analysis Summary and are included in value validation. Columns present in BCV but not in SRC are recorded as `DIFF` (with an empty `src_field`) for informational purposes.

### 2. Column Size Lookup

For each SRC column, the tool looks up its raw data size (in TiB) from pre-generated `.xlsx` files in `field_size/`:

```
field_size/<table>_raw_size_in_TiB.xlsx
```

The file must contain at minimum two columns: `Field Name` and `Size (TiB)`.

### 3. Column Exclusion

Before any usage check or Presto query, columns listed in `exclude.csv` are removed from the analysis for the selected table.

**Format** (`table,column` headers, SRC column names use `__` notation):

```
table,column
request,request__some_deprecated_field
slot,slot__internal_only_field
```

Excluded columns are:
- Filtered out immediately after schema comparison
- **Not** included in ETL/SOS lookup or Presto usage queries
- **Not** written to `result.csv`
- **Not** validated during value validation
- Shown in a dedicated **white/grey panel** at the very top of the Analysis Summary (field name, status, SRC type, BCV type)

### 4. Usage Data Query

For each remaining DIFF column (SRC present, BCV missing), the tool checks two local reference files and then queries Presto:

**ETL usage** — `etl_fields.json`, keyed by table name with dot-separated field paths:

```json
{
  "request": ["request.context.distributor_asset_id"]
}
```

**SOS usage** — `sos_fields.csv`, with `table` and `column` headers and dot-separated field paths:

```
table,column
request,execution_networks.network_selection_info.candidate_ad_funnel_metrics.ad_creative_checking_metrics.auction_max_ad_duration
slot,partners.network_selection_info.candidate_ad_funnel_metrics.ad_filling_metrics.pod_position_targeting_check_failed
```

For both lookups the SRC column name is normalised by replacing `__` with `.` before matching (e.g. `request__context__distributor_asset_id` → `request.context.distributor_asset_id`).

**Presto usage query** — counts distinct queries per column broken down by user type:

| User Type  | Source     | Description |
|------------|------------|-------------|
| `ETL`      | local file | Column in `etl_fields.json` for the selected table — `Y` or empty |
| `SOS`      | local file | Column in `sos_fields.csv` for the selected table — `Y` or empty |
| `Insights` | Presto     | `sa-dataapp-insights`, `sa-dmo-aqs`, `sa-dataapp-yield`, and related accounts |
| `Arena`    | Presto     | Queries from Arena-based sources |
| `LQS`      | Presto     | Queries from LQS-based sources |
| `CP`       | Presto     | Custom Reports (`publisher` user) |
| `AF`       | Presto     | AF ETL (`sa-presto-af-etl` user) |
| `Others`   | Presto     | All other query sources |

**Batching:** 500 columns per Presto query (`USAGE_QUERY_BATCH_SIZE`).  
**Retry:** up to 3 attempts per batch (`USAGE_QUERY_MAX_RETRIES`).  
**Query scope:** `2026-01-01` onwards · `prd` environment · admin users and `presto-python-client` excluded.

### 5. Analysis Summary

The tool prints a color-coded **Analysis Summary** with up to five panels displayed in this order:

| # | Panel | Color | Contents |
|---|-------|-------|----------|
| 1 | **Excluded Columns** | ⚪ White/Grey | Columns from `exclude.csv` — skipped from all steps |
| 2 | **Recommended for Backfill** | 🔵 Cyan | DIFF columns where usage meets threshold AND size < 0.03 TiB |
| 3 | **Recommended Excluded** | 🟡 Yellow | DIFF columns where usage meets threshold AND size ≥ 0.03 TiB |
| 4 | **Recommended No Backfill** | 🔴 Red | DIFF columns where usage is below all thresholds |
| 5 | **Type Mismatch** | 🟣 Magenta | `MATCHED - TYPE DIFF` columns — field exists in both tables but types differ |

Panels 1 and 5 are only shown when they have entries. Panels 2–4 are always shown.

---

## Analysis Rules

Applied to `DIFF` rows where SRC has a value and the BCV column is missing:

| Panel | Color | Condition | `recommended_action` |
|-------|-------|-----------|----------------------|
| Recommended for Backfill | 🔵 Cyan | Usage meets threshold **AND** (size unknown **OR** < 0.03 TiB) | `Backfill` |
| Recommended Excluded | 🟡 Yellow | Usage meets threshold **AND** size ≥ 0.03 TiB | `Excluded - Size Too Large` |
| Recommended No Backfill | 🔴 Red | Usage **does not** meet any threshold | `No Backfill - Low Usage` |

**Usage threshold** — any one of the following must be met:

| Source   | Threshold |
|----------|-----------|
| ETL      | `Y`       |
| SOS      | `Y`       |
| Insights | > 0       |
| Arena    | > 0       |
| LQS      | ≥ 10      |
| CP       | > 0       |
| AF       | > 0       |
| Others   | ≥ 100     |

> `MATCHED - TYPE DIFF` columns do not receive a `recommended_action`; they are shown in the magenta panel only.  
> Columns in `exclude.csv` do not receive any recommendation and are not written to `result.csv`.

---

## Output

### `<table>_result.csv`

Written to `output/<table>_result.csv`. Excluded columns are **not** present in this file.

| Column | Description |
|--------|-------------|
| `status` | `MATCHED` · `MATCHED - TYPE DIFF` · `DIFF` |
| `src_field` | Column name in the SRC table |
| `src_type` | Column type in the SRC table |
| `bcv_field` | Column name in the BCV table (empty if missing) |
| `bcv_type` | Column type in the BCV table (empty if missing) |
| `size` | Raw column size in TiB (empty if not in size data) |
| `usage:ETL` | `Y` if used by ETL (`etl_fields.json`); otherwise empty |
| `usage:SOS` | `Y` if used by SOS (`sos_fields.csv`); otherwise empty |
| `usage:Insights` | Distinct Insights query count |
| `usage:Arena` | Distinct Arena query count |
| `usage:LQS` | Distinct LQS query count |
| `usage:CP` | Distinct Custom Reports query count |
| `usage:AF` | Distinct AF ETL query count |
| `usage:Others` | Distinct query count from all other sources |
| `recommended_action` | `Backfill` / `Excluded - Size Too Large` / `No Backfill - Low Usage` / _(empty for MATCHED and MATCHED - TYPE DIFF)_ |
| `validation` | Added after value validation: `Y` (match) · `N` (mismatch) · `-` (parent node, skipped) · _(empty for DIFF rows)_ |

### JSON Files

| File | Description |
|------|-------------|
| `output/<table>.json` | Full SRC column list from DESCRIBE |
| `output/bcv_<table>.json` | Full BCV column list from DESCRIBE |

---

## Matched Column Value Validation

Validates the actual data values of all `MATCHED` and `MATCHED - TYPE DIFF` columns by running live queries against both SRC and BCV and comparing row by row. Type-mismatched columns are included so the nature of any data difference can be observed directly.

### Triggering Validation

1. **After a Full Run** — once `result.csv` is written the tool prompts:
   > `Continue to validate values for MATCHED columns?`  
   Selecting `Yes` then asks:
   > `Select number of transactions to sample for validation: 10 / 100 / 1000`

2. **Validation Only mode** — select at startup to skip schema comparison entirely and jump straight to validation using a previously generated `result.csv`. The transaction-count prompt is shown at the start of the validation step.

### Per-Table Join Keys

| Table | Key Columns |
|-------|-------------|
| `request` | `request__transaction_id` |
| `slot` | `request__transaction_id`, `slot__index` _(int)_ |
| `ad` | `request__transaction_id`, `advertisement__ad_id`, `advertisement__ad_replica_id` _(int)_, `advertisement__ad_type` _(varchar)_ |

Tables without a configured key (`candidate`, `auction`, `ack`) skip validation with a warning. Integer key columns are written as unquoted integer literals in `IN (...)` clauses.

### Parent Structure Node Exclusion

A column is treated as a **parent structure node** and excluded from validation when **both** conditions hold:

1. `src_type` is one of: `varchar` · `array(varchar)` · `array(array(varchar))` · `array(array(array(varchar)))`
2. At least one child column `<field>__<suffix>` exists anywhere in the result CSV

Parent nodes are:
- Excluded from all validation queries (no SQL generated for them)
- Marked **`-`** in the `validation` column of `result.csv`
- Listed in a dedicated section of the validation report markdown

### Batching Strategy

Columns are split into batches of up to **500** (`VALUE_VALIDATION_BATCH_SIZE`). Key columns are automatically prepended to any batch that doesn't already include them.

**Batch 1 — TABLESAMPLE (anchors the key set):**

```sql
SELECT
    <key_columns>,
    <columns_batch_1>
FROM mrm_log_flat.default.<table> TABLESAMPLE BERNOULLI (1)
WHERE bitwise_and(request__bit_flags, 576460752303423488) > 0
  AND process_batch_id = '<batch_id>'
LIMIT <transaction_limit>
```

`batch_id` = current time − 24 h, rounded to the hour (`YYYYMMDDHHMMSS`). Shown in **green** in the terminal.  
`transaction_limit` = the value selected in the prompt (10 / 100 / 1000).

**Batch 2+ — SRC (targets the same rows):**

```sql
SELECT <key_columns>, <columns_batch_N>
FROM mrm_log_flat.default.<table>
WHERE process_batch_id = '<batch_id>'
  AND (<key_columns>) IN ((<v1>, <v2>), ...)
```

**BCV (all batches):**

```sql
SELECT <key_columns>, <columns_batch_N>
FROM etl.public_test1.<table>
WHERE batch_id = '<batch_id>'
  AND (<key_columns>) IN ((<v1>, <v2>), ...)
LIMIT <transaction_limit>
```

All batches run sequentially. Progress is shown with a live spinning indicator (refreshes every second). Results from all batches are merged in memory before the final comparison.

### Comparison Logic

1. Keys from batch 1 SRC rows establish the transaction universe.
2. Only rows present in **both** SRC and BCV (by key) are compared; unmatched keys are skipped.
3. Each non-key column is compared as a string.
4. A column is **matched** (`Y`) if all compared rows agree; otherwise **unmatched** (`N`).

### Validation Summary Output

```
[2026-06-25 10:31:00] Value validation summary:
[2026-06-25 10:31:00] Matched transactions:  10/10
[2026-06-25 10:31:00] Matched fields:       342/350  (97.71%)
[2026-06-25 10:31:00] Unmatched fields:       8/350   (2.29%)
```

Key counts are highlighted in color. Both output file paths are printed in **green**.

### Validation Output Files

| File | Description |
|------|-------------|
| `output/<table>_result.csv` | Patched with a `validation` column (`Y` / `N` / `-`) |
| `output/<table>_validation_report.md` | Detailed markdown report |

#### `<table>_validation_report.md` sections

| Section | Contents |
|---------|----------|
| **Summary** | Transaction counts, matched/unmatched field counts and percentages |
| **Excluded Parent Structure Nodes** | Fields skipped as parent nodes, with their types |
| **SQL Queries** | All SRC and BCV SQL for every batch as fenced code blocks |
| **Unmatched Field Details** | Per-column diff table: join key · SRC value · BCV value |

Example entry:

```markdown
### 1. `slot__environment`  _(3 diff(s))_

| Key | SRC | BCV |
|:---|:---|:---|
| `abc123 / 1` | `web` | `WEB`    |
| `def456 / 2` | `app` | *(null)* |
```

---

## Supported Tables

| Table | SRC Full Name | BCV Full Name | Validation Key Columns |
|-------|---------------|---------------|------------------------|
| `request` | `mrm_log_flat.default.request` | `etl.public_test1.request` | `request__transaction_id` |
| `ad` | `mrm_log_flat.default.ad` | `etl.public_test1.ad` | `request__transaction_id`, `advertisement__ad_id`, `advertisement__ad_replica_id` |
| `slot` | `mrm_log_flat.default.slot` | `etl.public_test1.slot` | `request__transaction_id`, `slot__index` |
| `candidate` | `mrm_log_flat.default.candidate` | `etl.public_test1.candidate` | _(not configured — validation skipped)_ |
| `auction` | `mrm_log_flat.default.auction` | `etl.public_test1.auction` | _(not configured — validation skipped)_ |
| `ack` | `mrm_log_flat.default.ack` | `etl.public_test1.ack` | _(not configured — validation skipped)_ |

---

## Thresholds Reference

| Constant | Value | Description |
|----------|-------|-------------|
| `USAGE_QUERY_BATCH_SIZE` | `500` | Columns per Presto usage batch query |
| `USAGE_QUERY_MAX_RETRIES` | `3` | Max retry attempts per usage batch on failure |
| `VALUE_VALIDATION_BATCH_SIZE` | `500` | Columns per value validation batch query |

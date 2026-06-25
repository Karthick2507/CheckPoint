# BCV Analyzer

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
  - [3. Usage Data Query](#3-usage-data-query)
  - [4. Analysis Summary](#4-analysis-summary)
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

BCV Analyzer compares the schema of a source table (`mrm_log_flat.default.<table>`) against its corresponding BCV table (`etl.public_test1.<table>`), identifies **DIFF** columns (columns present in SRC but missing in BCV), checks whether those columns are used by ETL, queries Presto for their historical usage data, and produces a prioritized backfill recommendation report.

```
SRC Table  ──┐
             ├──► Schema Comparison ──► DIFF Columns ──► ETL Usage Check ──► Presto Usage Query ──► Analysis Summary + <table>_result.csv
BCV Table  ──┘                                                                  (batch, 500/query)
                                                                                        │
                                                                                        ▼
                                                                           Value Validation (MATCHED columns)
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
> The Analysis Summary output can be lengthy. It is recommended to increase your terminal's scrollback buffer to **30000** lines so you can scroll back through the full results.
>
> **iTerm2 setup:**
> 1. Open iTerm2
> 2. Go to **iTerm2 → Settings**
> 3. Select **Profiles**
> 4. Select the profile you are using (e.g. `Default`)
> 5. Open the **Terminal** tab
> 6. Find **Scrollback lines** and set it to `30000`

---

## Usage

### Recommended Execution

The recommended way to run BCV Analyzer is to pass the Presto connection details directly via CLI flags:

```bash
python bcv_analyzer.py \
  --host presto-gateway.presto.fw1.aws.fwmrm.net:8080 \
  --user <your-username> \
  --auth-token <your-auth-token>
```

Example:

I don't mind at all if you use my username/token to submit presto queries like shown below. If you want to use your own username/token, please follow this wiki guide https://freewheel.atlassian.net/wiki/spaces/DDEU2/pages/528557481/Presto+Gateway+Userguide#Geta-a-token-with-LDAP-account to get a token. Please note token will be expired in 30 days, and you will have to re-apply it following the steps in the above link.

You need to connect to VPN in order to submit queries to production Presto server.

```bash
python bcv_analyzer.py \
  --host presto-gateway.presto.fw1.aws.fwmrm.net:8080 \
  --user yuwang \
  --auth-token cfeac6c3-db15-4e03-9bad-e0e96ae4932a
```

After launching, the interactive UI will prompt you to select a table and run mode.

### Interactive Mode

Simply run the script with no arguments to launch the interactive UI:

```bash
python bcv_analyzer.py
```

You will be prompted to:
1. **Select a table** — choose from the supported tables using ↑/↓ arrow keys
2. **Select a run mode** — Full Run or Validation Only (see [Run Modes](#run-modes))

### CLI Arguments

```bash
python bcv_analyzer.py [OPTIONS]
```

| Option               | Description                                      | Default                    |
|----------------------|--------------------------------------------------|----------------------------|
| `--host`             | Presto host                                      | `$PRESTO_HOST`             |
| `--port`             | Presto port                                      | `$PRESTO_PORT` or `8080`   |
| `--user`             | Presto user                                      | `$PRESTO_USER`             |
| `--request-timeout`  | Request timeout (seconds)                        | `$PRESTO_REQUEST_TIMEOUT` or `5` |
| `--auth-token`       | Auth token (sent as `Authorization: Bearer ...`) | `$PRESTO_AUTH_TOKEN`       |
| `--auth-header`      | Custom auth header name                          | `$PRESTO_AUTH_HEADER`      |
| `--table`            | Skip table selection prompt                      | _(interactive)_            |
| `--help`             | Show help message                                |                            |

Example:

```bash
python bcv_analyzer.py --host presto.example.com --user alice --table request
```

### Environment Variables

You can combine environment variables with CLI flags:

```bash
PRESTO_HOST=presto.example.com PRESTO_USER=alice python bcv_analyzer.py --table request
```

---

## Run Modes

When prompted, select one of two run modes:

| Mode                | Description |
|---------------------|-------------|
| **Full Run**        | Queries Presto for **all** DIFF columns. |
| **Validation Only** | Skips schema comparison and usage analysis entirely. Reads the previously generated `output/<table>_result.csv` and proceeds directly to [Matched Column Value Validation](#matched-column-value-validation). Requires a result CSV to already exist. |


---

## How It Works

### 1. Schema Comparison

The tool runs `DESCRIBE` on both the SRC and BCV tables, then compares column names and types:

- **MATCHED** — column exists in both tables with the same type
- **DIFF** — column is missing from BCV, or has a different type

Two sub-cases of DIFF are tracked:
- SRC has the column, BCV does not → candidate for backfill analysis
- BCV has a column that SRC does not → informational only

### 2. Column Size Lookup

For each SRC column, the tool looks up its raw data size (in TiB) from the pre-generated `.xlsx` files in `field_size/`. The file naming convention is:

```
field_size/<table>_raw_size_in_TiB.xlsx
```

The xlsx must contain at minimum two columns: `Field Name` and `Size (TiB)`.

### 3. Usage Data Query

For each DIFF column (SRC present, BCV missing), the tool first checks `etl_fields.json` to determine whether ETL uses the column. The file is organized by table name:

```json
{
  "request": [
    "request.context.distributor_asset_id"
  ]
}
```

When matching column names, the tool temporarily normalizes the SRC field name by replacing `__` with `.`. For example, `request__context__distributor_asset_id` matches `request.context.distributor_asset_id` in `etl_fields.json`.

The tool then queries the Presto internal usage tracking tables to find how many distinct queries accessed the column, broken down by user type:

| User Type  | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| `ETL`      | Column appears in `etl_fields.json` for the selected table                  |
| `Insights` | Queries from internal Insights service accounts (`sa-dataapp-insights`, etc.) |
| `Arena`    | Queries from Arena-based sources                                            |
| `LQS`      | Queries from LQS-based sources                                              |
| `CP`       | Queries from Custom Reports (`publisher` user)                              |
| `Others`   | All other query sources                                                     |

**Batching:** Columns are queried in batches of **500** per Presto query (configurable via `USAGE_QUERY_BATCH_SIZE`) to minimize query overhead.

**Retry:** Each batch query is retried up to **3 times** on failure (configurable via `USAGE_QUERY_MAX_RETRIES`).

**Query scope:**
- Date range: `2026-01-01` onwards
- Environment: `prd` only
- Excluded users: internal/admin accounts
- Excluded sources: `presto-python-client`

### 4. Analysis Summary

After querying usage data, the tool prints a color-coded **Analysis Summary** with three panels.

---

## Analysis Rules

The following rules are applied to all DIFF rows where **SRC has a value** and **BCV column is missing**:

| Panel | Color | Condition | `recommended_action` in CSV |
|-------|-------|-----------|------------------------------|
| **Recommended for Backfill** | 🔵 Cyan | Usage meets threshold **AND** (size unknown **OR** size < 0.03 TiB) | `Backfill` |
| **Recommended Excluded** | 🟡 Yellow | Usage meets threshold **AND** size ≥ 0.03 TiB | `Excluded - Size Too Large` |
| **Recommended No Backfill** | 🔴 Red | Usage **does not** meet any threshold | `No Backfill - Low Usage` |

**Usage threshold** (any one condition must be met):

| Source    | Threshold  |
|-----------|-----------|
| ETL       | `Y`       |
| Insights  | > 0       |
| Arena     | > 0       |
| LQS       | ≥ 10      |
| CP        | > 0       |
| Others    | ≥ 100     |

**Size threshold:** `< 0.03 TiB` (columns with unknown size are treated as small and included)

---

## Output

### `<table>_result.csv`

Written to `output/<table>_result.csv`. Contains one row per column comparison with the following fields:

| Column               | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `status`             | `MATCHED` or `DIFF`                                          |
| `src_field`          | Column name in the SRC table                                 |
| `src_type`           | Column type in the SRC table                                 |
| `bcv_field`          | Column name in the BCV table (empty if missing)              |
| `bcv_type`           | Column type in the BCV table (empty if missing)              |
| `size`               | Raw column size in TiB (empty if not found in size data)     |
| `usage:ETL`          | `Y` if the column is used by ETL according to `etl_fields.json`; otherwise empty |
| `usage:Insights`     | Number of distinct Insights service account queries using this column |
| `usage:Arena`        | Number of distinct Arena queries using this column           |
| `usage:LQS`          | Number of distinct LQS queries using this column             |
| `usage:CP`           | Number of distinct Custom Reports (`publisher`) queries using this column |
| `usage:Others`       | Number of distinct queries from other sources                |
| `recommended_action` | `Backfill` / `Excluded - Size Too Large` / `No Backfill - Low Usage` / _(empty)_ |
| `validation`         | Added after value validation: `Y` (values match), `N` (mismatch), `-` (parent structure node, skipped), or empty (not a MATCHED column) |

### JSON Files

Written to `output/`:

| File                   | Description                        |
|------------------------|------------------------------------|
| `<table>.json`         | Full SRC column list from DESCRIBE |
| `bcv_<table>.json`     | Full BCV column list from DESCRIBE |

---

## Matched Column Value Validation

After the schema comparison and usage analysis, the tool validates the **actual data values** of all MATCHED columns by running live queries against both SRC and BCV and comparing row by row.

### Triggering Validation

Validation is triggered in two ways:

1. **After a Full Run** — once `output/<table>_result.csv` is written, the tool prompts:
   > `Continue to validate values for MATCHED columns?`
   Selecting `Yes` starts validation immediately.

2. **Validation Only mode** — select this run mode at startup to skip schema comparison entirely and jump straight to validation using a previously generated result CSV.

### Network ID Filter

Both SRC and BCV queries include a fixed network ID filter to scope results to a known network:

```sql
AND request__context__video_cro_network_id = 169843
```

The value `169843` is an **integer** literal (not a quoted string). This filter is applied to every query in every validation batch.

### Per-Table Join Keys

SRC and BCV rows are joined on a set of key columns configured per table. Integer key columns are emitted as unquoted integer literals in `IN (...)` clauses.

| Table     | Key Columns                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|
| `request` | `request__transaction_id`                                                                     |
| `slot`    | `request__transaction_id`, `slot__index` _(int)_                                              |
| `ad`      | `request__transaction_id`, `advertisement__ad_id` _(int)_, `advertisement__ad_replica_id` _(int)_ |

Tables without a configured key (`candidate`, `auction`, `ack`) will skip value validation with a warning message.

### Parent Structure Node Exclusion

Certain MATCHED columns are structural containers rather than leaf values and are automatically excluded from comparison. A column is treated as a **parent structure node** when **both** of the following conditions hold simultaneously:

1. Its `src_type` is one of:
   - `varchar`
   - `array(varchar)`
   - `array(array(varchar))`
   - `array(array(array(varchar)))`

2. At least one child column named `<field>__<suffix>` exists anywhere in the result CSV.

   _Example: `visitor__postal_code_package` has type `array(varchar)` and a child column `visitor__postal_code_package__network_id` exists → it is a parent node._

Parent nodes are:
- **Excluded** from validation queries — no SQL is generated for them.
- Marked **`-`** in the `validation` column of `result.csv`.
- Listed in a dedicated **"Excluded Parent Structure Nodes"** section of the validation report markdown.

### Batching Strategy

Validation queries are split into batches of up to **500 columns** each (configurable via `VALUE_VALIDATION_BATCH_SIZE`). Key columns are automatically prepended to any batch that does not already include them.

**Batch 1 — anchor batch (TABLESAMPLE):**

```sql
SELECT
    <key_columns>,
    <matched_columns_batch_1>
FROM mrm_log_flat.default.<table> TABLESAMPLE BERNOULLI (1)
WHERE bitwise_and(request__bit_flags, 576460752303423488) > 0
  AND process_batch_id = '<batch_id>'
  AND request__context__video_cro_network_id = 169843
LIMIT 10
```

- `batch_id` = current time minus 24 hours, rounded to the hour (`YYYYMMDDHHMMSS`, e.g. `20260624140000`). Displayed in **green** in the terminal.
- Up to 10 rows are sampled. The key values from these rows are carried forward to all subsequent batches.

**Batch 2+ — key-targeted batches (SRC):**

```sql
SELECT
    <key_columns>,
    <matched_columns_batch_N>
FROM mrm_log_flat.default.<table>
WHERE process_batch_id = '<batch_id>'
  AND (<key_columns>) IN ((<v1>, <v2>), ...)
  AND request__context__video_cro_network_id = 169843
```

**BCV query (all batches):**

```sql
SELECT
    <key_columns>,
    <matched_columns_batch_N>
FROM etl.public_test1.<table>
WHERE batch_id = '<batch_id>'
  AND (<key_columns>) IN ((<v1>, <v2>), ...)
  AND request__context__video_cro_network_id = 169843
LIMIT 10
```

All batches are executed sequentially. Progress is shown with a live spinning indicator that refreshes every second:

```
[2026-06-25 10:30:05] Executing value validation batch 2/4 — SRC |
```

Results from all batches are merged in memory before the final comparison.

### Comparison Logic

1. SRC rows from batch 1 establish the universe of transaction keys.
2. Only rows whose key exists in **both** SRC and BCV are compared; unmatched keys are skipped.
3. For every compared row, each non-key column is compared as a string.
4. A column is **matched** (`Y`) if its value is identical across all compared rows; otherwise **unmatched** (`N`).

### Validation Summary Output

The terminal prints a summary with highlighted counts, e.g.:

```
[2026-06-25 10:31:00] Value validation summary:
[2026-06-25 10:31:00] Matched transactions:  10/10
[2026-06-25 10:31:00] Matched fields:       342/350  (97.71%)
[2026-06-25 10:31:00] Unmatched fields:       8/350   (2.29%)
```

### Validation Output Files

Two files are written/updated after validation. Both paths are printed in **green** in the terminal.

| File | Description |
|------|-------------|
| `output/<table>_result.csv` | Existing result CSV patched with a new `validation` column (`Y` / `N` / `-`) |
| `output/<table>_validation_report.md` | Detailed markdown report (see below) |

#### `<table>_validation_report.md`

| Section | Contents |
|---------|----------|
| **Summary** | Transaction counts and matched/unmatched field counts with percentages |
| **Excluded Parent Structure Nodes** | Fields skipped as parent nodes, with their types |
| **SQL Queries** | All SRC and BCV SQL for every batch, as fenced code blocks (for deep debugging) |
| **Unmatched Field Details** | Per-column diff table: join key, SRC value, BCV value for every differing row |

Example unmatched field entry in the report:

```markdown
### 1. `slot__environment`  _(3 diff(s))_

| Key | SRC | BCV |
|:---|:---|:---|
| `abc123 / 1` | `web`  | `WEB`    |
| `def456 / 2` | `app`  | *(null)* |
```

---

## Supported Tables

| Table       | SRC Full Name                        | BCV Full Name                     | Validation Key Columns |
|-------------|--------------------------------------|-----------------------------------|------------------------|
| `request`   | `mrm_log_flat.default.request`       | `etl.public_test1.request`        | `request__transaction_id` |
| `ad`        | `mrm_log_flat.default.ad`            | `etl.public_test1.ad`             | `request__transaction_id`, `advertisement__ad_id`, `advertisement__ad_replica_id` |
| `slot`      | `mrm_log_flat.default.slot`          | `etl.public_test1.slot`           | `request__transaction_id`, `slot__index` |
| `candidate` | `mrm_log_flat.default.candidate`     | `etl.public_test1.candidate`      | _(not configured — validation skipped)_ |
| `auction`   | `mrm_log_flat.default.auction`       | `etl.public_test1.auction`        | _(not configured — validation skipped)_ |
| `ack`       | `mrm_log_flat.default.ack`           | `etl.public_test1.ack`            | _(not configured — validation skipped)_ |

---

## Thresholds Reference

All thresholds are defined as constants at the top of `bcv_analyzer.py` for easy adjustment:

| Constant                        | Value    | Description                                         |
|---------------------------------|----------|-----------------------------------------------------|
| `USAGE_QUERY_BATCH_SIZE`        | `500`    | Columns per Presto usage batch query                |
| `USAGE_QUERY_MAX_RETRIES`       | `3`      | Max retry attempts per usage batch on failure       |
| `VALUE_VALIDATION_BATCH_SIZE`   | `500`    | Columns per value validation batch query            |
| `VALUE_VALIDATION_NETWORK_ID`   | `169843` | Network ID filter applied to all validation queries |

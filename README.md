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

BCV Analyzer compares the schema of a source table (`mrm_log_flat.default.<table>`) against its corresponding BCV table (`etl.public_test1.<table>`), identifies **DIFF** columns (columns present in SRC but missing in BCV), checks whether those columns are used by ETL or SOS, queries Presto for their historical usage data, and produces a prioritized backfill recommendation report.

```
SRC Table  ──┐
             ├──► Schema Comparison ──► MATCHED - TYPE DIFF columns ──► (magenta panel in summary)
BCV Table  ──┘         │
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
- `exclude.csv` in the project root to skip specific columns (optional; create with `table,column` headers)

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

| Status | Condition |
|--------|-----------|
| `MATCHED` | Column exists in both tables with the **same** type |
| `MATCHED - TYPE DIFF` | Column exists in both tables but with **different** types |
| `DIFF` | Column is present in SRC but **missing** from BCV entirely |

`MATCHED - TYPE DIFF` columns appear in a dedicated **magenta panel** in the Analysis Summary and are also included in value validation so the actual data difference can be observed.

Additionally, columns present in BCV but not in SRC are tracked separately for informational purposes.

### 2. Column Size Lookup

For each SRC column, the tool looks up its raw data size (in TiB) from the pre-generated `.xlsx` files in `field_size/`. The file naming convention is:

```
field_size/<table>_raw_size_in_TiB.xlsx
```

The xlsx must contain at minimum two columns: `Field Name` and `Size (TiB)`.

### 3. Usage Data Query

For each DIFF column (SRC present, BCV missing), the tool checks two local reference files before querying Presto:

**ETL usage** — checked against `etl_fields.json`, organized by table name:

```json
{
  "request": [
    "request.context.distributor_asset_id"
  ]
}
```

**SOS usage** — checked against `sos_fields.csv`, with `table` and `column` headers and dot-separated field names:

```
table,column
request,execution_networks.network_selection_info.candidate_ad_funnel_metrics.ad_creative_checking_metrics.auction_max_ad_duration
slot,partners.network_selection_info.candidate_ad_funnel_metrics.ad_filling_metrics.pod_position_targeting_check_failed
```

For both lookups, the SRC column name is normalized by replacing `__` with `.` before matching. For example, `request__context__distributor_asset_id` → `request.context.distributor_asset_id`.

**Column exclusion** — before any usage lookup or Presto query, columns listed in `exclude.csv` are removed from the analysis entirely. `exclude.csv` uses `__`-style SRC column names directly:

```
table,column
request,request__some_deprecated_field
slot,slot__internal_only_field
```

Excluded columns are:
- Removed from schema comparison analysis and backfill recommendations
- Not queried for Presto usage data
- Not included in `result.csv`
- Not validated during value validation
- Shown in a dedicated white/grey panel at the top of the Analysis Summary

The tool then queries the Presto internal usage tracking tables to find how many distinct queries accessed the column, broken down by user type:

| User Type  | Source | Description                                                                 |
|------------|--------|-----------------------------------------------------------------------------|
| `ETL`      | local file | Column appears in `etl_fields.json` for the selected table; value `Y` or empty |
| `SOS`      | local file | Column appears in `sos_fields.csv` for the selected table; value `Y` or empty  |
| `Insights` | Presto | Queries from internal Insights service accounts (`sa-dataapp-insights`, etc.) |
| `Arena`    | Presto | Queries from Arena-based sources                                            |
| `LQS`      | Presto | Queries from LQS-based sources                                              |
| `CP`       | Presto | Queries from Custom Reports (`publisher` user)                              |
| `AF`       | Presto | Queries from AF ETL (`sa-presto-af-etl` user)                              |
| `Others`   | Presto | All other query sources                                                     |

**Batching:** Columns are queried in batches of **500** per Presto query (configurable via `USAGE_QUERY_BATCH_SIZE`) to minimize query overhead.

**Retry:** Each batch query is retried up to **3 times** on failure (configurable via `USAGE_QUERY_MAX_RETRIES`).

**Query scope:**
- Date range: `2026-01-01` onwards
- Environment: `prd` only
- Excluded users: internal/admin accounts
- Excluded sources: `presto-python-client`

### 4. Analysis Summary

After querying usage data, the tool prints a color-coded **Analysis Summary** with up to five panels:

| Panel | Color | Contents |
|-------|-------|----------|
| Excluded Columns | ⚪ White/Grey | Columns listed in `exclude.csv` — skipped from all analysis and validation |
| Recommended for Backfill | 🔵 Cyan | DIFF columns where usage meets threshold AND size < 0.03 TiB |
| Recommended Excluded | 🟡 Yellow | DIFF columns where usage meets threshold AND size ≥ 0.03 TiB |
| Recommended No Backfill | 🔴 Red | DIFF columns where usage is below all thresholds |
| Type Mismatch | 🟣 Magenta | `MATCHED - TYPE DIFF` columns — exist in both tables but with different types |

The Excluded Columns panel is always shown first when `exclude.csv` contains entries for the selected table.

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
| SOS       | `Y`       |
| Insights  | > 0       |
| Arena     | > 0       |
| LQS       | ≥ 10      |
| CP        | > 0       |
| AF        | > 0       |
| Others    | ≥ 100     |

**Size threshold:** `< 0.03 TiB` (columns with unknown size are treated as small and included)

> **Note:** `MATCHED - TYPE DIFF` columns do not receive a `recommended_action` and are shown separately in the magenta panel.

---

## Output

### `<table>_result.csv`

Written to `output/<table>_result.csv`. Contains one row per column comparison with the following fields:

| Column               | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `status`             | `MATCHED` · `MATCHED - TYPE DIFF` · `DIFF`                  |
| `src_field`          | Column name in the SRC table                                 |
| `src_type`           | Column type in the SRC table                                 |
| `bcv_field`          | Column name in the BCV table (empty if missing)              |
| `bcv_type`           | Column type in the BCV table (empty if missing)              |
| `size`               | Raw column size in TiB (empty if not found in size data)     |
| `usage:ETL`          | `Y` if the column is used by ETL according to `etl_fields.json`; otherwise empty |
| `usage:SOS`          | `Y` if the column is used by SOS according to `sos_fields.csv`; otherwise empty  |
| `usage:Insights`     | Number of distinct Insights service account queries using this column |
| `usage:Arena`        | Number of distinct Arena queries using this column           |
| `usage:LQS`          | Number of distinct LQS queries using this column             |
| `usage:CP`           | Number of distinct Custom Reports (`publisher`) queries using this column |
| `usage:AF`           | Number of distinct AF ETL (`sa-presto-af-etl`) queries using this column |
| `usage:Others`       | Number of distinct queries from other sources                |
| `recommended_action` | `Backfill` / `Excluded - Size Too Large` / `No Backfill - Low Usage` / _(empty for MATCHED and MATCHED - TYPE DIFF)_ |
| `validation`         | Added after value validation: `Y` (values match), `N` (mismatch), `-` (parent structure node, skipped), or empty (DIFF rows are not validated) |

### JSON Files

Written to `output/`:

| File                   | Description                        |
|------------------------|------------------------------------|
| `<table>.json`         | Full SRC column list from DESCRIBE |
| `bcv_<table>.json`     | Full BCV column list from DESCRIBE |

---

## Matched Column Value Validation

After the schema comparison and usage analysis, the tool validates the **actual data values** of all `MATCHED` and `MATCHED - TYPE DIFF` columns by running live queries against both SRC and BCV and comparing row by row. This includes type-mismatched columns so that the nature of the data difference can be observed directly.

### Triggering Validation

Validation is triggered in two ways:

1. **After a Full Run** — once `output/<table>_result.csv` is written, the tool prompts:
   > `Continue to validate values for MATCHED columns?`
   Selecting `Yes` starts validation immediately.

2. **Validation Only mode** — select this run mode at

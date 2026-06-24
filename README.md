# BCV Analyzer

A command-line tool for analyzing schema differences between the **SRC** (source) tables and **BCV** (Backfill Column Value) tables in Presto/Trino, and generating backfill recommendations based on column usage data.

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
  - [result.csv](#resultcsv)
  - [JSON Files](#json-files)
- [Supported Tables](#supported-tables)
- [Thresholds Reference](#thresholds-reference)

---

## Overview

BCV Analyzer compares the schema of a source table (`mrm_log_flat.default.<table>`) against its corresponding BCV table (`etl.public_test1.<table>`), identifies **DIFF** columns (columns present in SRC but missing in BCV), queries Presto for their historical usage data, and produces a prioritized backfill recommendation report.

```
SRC Table  ──┐
             ├──► Schema Comparison ──► DIFF Columns ──► Presto Usage Query ──► Analysis Summary + result.csv
BCV Table  ──┘                                               (batch, 100/query)
```

---

## Project Structure

```
BCV/
├── bcv_analyzer.py          # Main application
├── requirements.txt         # Python dependencies
├── field_size/              # Column size data (one .xlsx per table)
│   ├── request_raw_size_in_TiB.xlsx
│   ├── ad_raw_size_in_TiB.xlsx
│   ├── slot_raw_size_in_TiB.xlsx
│   ├── candidate_raw_size_in_TiB.xlsx
│   ├── auction_raw_size_in_TiB.xlsx
│   └── ack_raw_size_in_TiB.xlsx
├── output/                  # Generated output (auto-created)
│   ├── result.csv           # Main analysis result
│   ├── <table>.json         # SRC column list
│   └── bcv_<table>.json     # BCV column list
└── tests/
    └── test_bcv_analyzer.py
```

---

## Requirements

- Python 3.11+
- Access to a Presto/Trino gateway
- Column size `.xlsx` files in the `field_size/` directory

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
2. **Select a run mode** — Trial or Full Run (see [Run Modes](#run-modes))

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

| Mode         | Description                                              |
|--------------|----------------------------------------------------------|
| **Trial**    | Queries Presto for the **first 10** DIFF columns only. Useful for quickly testing connectivity and validating results before a full run. |
| **Full Run** | Queries Presto for **all** DIFF columns. May take significantly longer depending on the number of missing columns. |

> **Note:** In Trial mode, columns beyond the first 10 will have no usage data and will show a blank `recommended_action` in the output CSV.

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

For each DIFF column (SRC present, BCV missing), the tool queries the Presto internal usage tracking tables to find how many distinct queries accessed the column, broken down by user type:

| User Type  | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| `Insights` | Queries from internal Insights service accounts (`sa-dataapp-insights`, etc.) |
| `Arena`    | Queries from Arena-based sources                                            |
| `LQS`      | Queries from LQS-based sources                                              |
| `Others`   | All other query sources                                                     |

**Batching:** Columns are queried in batches of **100** per Presto query (configurable via `USAGE_QUERY_BATCH_SIZE`) to minimize query overhead.

**Retry:** Each batch query is retried up to **3 times** on failure (configurable via `USAGE_QUERY_MAX_RETRIES`).

**Query scope:**
- Date range: `2026-01-01` onwards
- Environment: `prd` only
- Excluded users: internal/admin accounts
- Excluded sources: `presto-python-client`

### 4. Analysis Summary

After querying usage data, the tool prints a color-coded **Analysis Summary** with three panels:

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
| Insights  | > 0       |
| Arena     | > 0       |
| LQS       | ≥ 10      |
| Others    | ≥ 100     |

**Size threshold:** `< 0.03 TiB` (columns with unknown size are treated as small and included)

---

## Output

### result.csv

Written to `output/result.csv`. Contains one row per column comparison with the following fields:

| Column               | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `status`             | `MATCHED` or `DIFF`                                          |
| `src_field`          | Column name in the SRC table                                 |
| `src_type`           | Column type in the SRC table                                 |
| `bcv_field`          | Column name in the BCV table (empty if missing)              |
| `bcv_type`           | Column type in the BCV table (empty if missing)              |
| `size`               | Raw column size in TiB (empty if not found in size data)     |
| `usage:Insights`     | Number of distinct Insights service account queries using this column |
| `usage:Arena`        | Number of distinct Arena queries using this column           |
| `usage:LQS`          | Number of distinct LQS queries using this column             |
| `usage:Others`       | Number of distinct queries from other sources                |
| `recommended_action` | `Backfill` / `Excluded - Size Too Large` / `No Backfill - Low Usage` / _(empty)_ |

### JSON Files

Written to `output/`:

| File                   | Description                        |
|------------------------|------------------------------------|
| `<table>.json`         | Full SRC column list from DESCRIBE |
| `bcv_<table>.json`     | Full BCV column list from DESCRIBE |

---

## Supported Tables

| Table       | SRC Full Name                        | BCV Full Name                     |
|-------------|--------------------------------------|-----------------------------------|
| `request`   | `mrm_log_flat.default.request`       | `etl.public_test1.request`        |
| `ad`        | `mrm_log_flat.default.ad`            | `etl.public_test1.ad`             |
| `slot`      | `mrm_log_flat.default.slot`          | `etl.public_test1.slot`           |
| `candidate` | `mrm_log_flat.default.candidate`     | `etl.public_test1.candidate`      |
| `auction`   | `mrm_log_flat.default.auction`       | `etl.public_test1.auction`        |
| `ack`       | `mrm_log_flat.default.ack`           | `etl.public_test1.ack`            |

---

## Thresholds Reference

All thresholds are defined as constants at the top of `bcv_analyzer.py` for easy adjustment:

| Constant                  | Value  | Description                                     |
|---------------------------|--------|-------------------------------------------------|
| `USAGE_QUERY_LIMIT`       | `10`   | Number of columns queried in Trial mode         |
| `USAGE_QUERY_BATCH_SIZE`  | `100`  | Columns per Presto batch query                  |
| `USAGE_QUERY_MAX_RETRIES` | `3`    | Max retry attempts per batch on failure         |





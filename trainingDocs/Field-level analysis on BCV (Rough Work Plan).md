# Field\-level analysis on BCV \(Rough Work Plan\)

# Introduction

Engineers involved: GC, Ruonan, Daniel, Mani and Yu

## 1. Overall goal

For a given table (example with `slot`), build a **field-by-field matrix** with, for each column:

- Supported in BCV?
- Value exactly matched in BCV (per event-level validation)?
- Used in reporting ETL (Optimus/Jetfire)?
- Used in Arena ETL?
- Used in LQS?
- Data size (flag if share of table \> 0.1%)

We want a **clear, consistent method** so all 5 people can work in parallel.

## 2. General approach (everyone follows this flow)

### Step 0 – Define the field list and tracking template

1. **Choose the source table** (e.g. `mrm_log_flat.default.slot`).
2. Extract the **canonical column list** (from DDL or HooverEntityAnalysis/Confluence).
3. Create a tracking sheet (one row per column) with these columns:
    - `field_name`
    - `in_bcv` (Y/N)
    - `bcv_value_match` (Exact / Partial / Not\_checked / Not\_applicable)
    - `in_reporting_etl` (Y/N/Unknown)
    - `in_arena_etl` (Y/N)
    - `in_lqs` (Y/N)
    - `data_size_pct` (numeric, highlight if \>0.1%)
    - `notes` (e.g. “renamed in BCV”, “expected model diff”, “derived field”)

Everyone uses this same template for whatever fields they own.

### Step 1 – BCV presence (schema)

**Question:** “Is column X present in BCV slot?”  
Tables: `mrm_log_flat.default.slot` vs `etl.public_test1.slot`.

Process:

1. Get column list for **source** table (Hoover):
    - via DDL: `DESCRIBE mrm_log_flat.default.slot`
2. Get column list for **BCV** table:
    - `DESCRIBE etl.public_test1.slot`
3. For each `source_column`:
    - If column with same or clearly mapped name exists in BCV → `in_bcv = Y`
    - Else → `in_bcv = N` and add to `notes` (“not modelled in BCV”, “requires derived mapping”).

(For non-slot tables later, same pattern but different BCV views.)

### Step 2 – BCV value match (event-level validation)

**Questions:**

- “Was this column validated?”
- “Are values exactly matched?”

For slot, you have a specific validation page:

- `mrm_log_flat.default.slot vs etl.public_test1.slot` wiki.

Process:

1. Open the slot validation wiki.
2. For each field:
    - If it appears in the **comparison queries/results** and there were no residual issues → `bcv_value_match = Exact`.
    - If there were known, documented differences or partial coverage → `bcv_value_match = Partial` + note why.
    - If not included in validation → `bcv_value_match = Not_checked`.

You can repeat this per entity once you have equivalent wikis for other tables.

### Step 3 – Reporting ETL usage (Optimus / Jetfire / Vulcan)

**Question:** “Is this column used in reporting ETL?”

You already expect this to be handled by Vulcan. Treat this as a **dependency**:

1. Agree with Vulcan team on **their own field matrix**:
    - For each column: any references in Optimus/Jetfire jobs?
    - Mark Y/N and, if Y, the job name(s).
2. Import their answers into your sheet’s `in_reporting_etl` + `notes`.

From your side, the work is:

- Maintain the field list and mapping.
- Provide Vulcan with clear column names + table.
- Pull their results into the tracker; don’t duplicate their analysis.

### Step 4 – Arena ETL and LQS usage

**Question:** “Is this column used in Arena ETL or LQS?”

You already have an example LQS query link. The general approach:

1. In **LQS**, query query history / metadata for that datasource and table:
    - Filter by `column_name` in SQL text, or use whatever “column usage” view you have (similar to what was done for Transaction Field Usage).
2. For each field:
    - If it appears in **Arena ETL queries** (e.g. specific schema/db used by Arena) → `in_arena_etl = Y`.
    - If it appears in **any LQS queries** (across products) → `in_lqs = Y`.
    - Otherwise, mark `N` or `Unknown`.

Even if the provided LQS URL is only for slot, you can repeat the same search pattern for other entities later. ([https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260623183449\_176631&externalid=20260623\_183451\_00002\_954ki](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260623183449_176631&externalid=20260623_183451_00002_954ki))

### Step 5 – Data size (PQM / parquet metrics)

**Question:** “Does this column have data size share \> 0.1%?”

Use the PQM Grafana dashboard you linked:

- `hoover-parquet-field-size` with `metric_name=parquet_column_compressed_bytes`.

Process:

1. Set **DataSource** to the Hoover source.
2. Filter **table** to `slot` (and later, other tables).
3. For each column:
    - Either export the panel data or read the metric for that column.
    - Compute `column_bytes / table_total_bytes` over last 30d.
    - Record as `data_size_pct`, and in your view highlight those where `> 0.1%`.

This will help prioritize which non-used columns are still “expensive” to carry.

([https://pqm.fwmrm.net/d/be2w3etsuce0wf/hoover-parquet-field-size?orgId=1&from=now-30d&to=now&timezone=browser&var-DataSource=bVv7dduGk&var-Table=$\_\_all&var-TopK=20&var-metric\_name=parquet\_column\_compressed\_bytes](https://pqm.fwmrm.net/d/be2w3etsuce0wf/hoover-parquet-field-size?orgId=1&from=now-30d&to=now&timezone=browser&var-DataSource=bVv7dduGk&var-Table=$__all&var-TopK=20&var-metric_name=parquet_column_compressed_bytes))

## 3. Rough work allocation

Team: **Ruonan, Daniel, Yu, GC, Mani**

## 3. Work allocation (per table)

Everyone uses the same method; ownership is by table.

**Request – Yu**

- Owns request field list + template.
- Drives the Thursday walkthrough of the “analyze” flow for everyone:
    - Live example of: BCV presence, LQS usage, data size.
- Completes both **analyze** and **validation** columns for request.

**Slot – Ruonan**

- Owns slot fields.
- Analyze:
    - `in_bcv`, `in_reporting_etl`, `in_arena_etl`, `in_lqs`, `in_insights`, `data_size_pct`.
- Validation:
    - Use the existing slot vs BCV validation wiki to fill `bcv_value_match` + notes.

**Ad – Mani**

- Owns ad entity fields.
- Analyze:
    - Same 6 questions for ad columns (BCV, reporting ETL, Arena, LQS, Insights, size).
- Validation:
    - Use ad-level event validation wiki/queries to mark `bcv_value_match`.

**Ack – Daniel**

- Owns ack fields.
- Analyze:
    - Same pattern: ack presence in BCV, ETL usage, Arena/LQS/Insights, size.
- Validation:
    - Use ack-level validation results (e.g. defaultImpression, quartiles, etc.) to mark match/partial/not\_checked.

**Auction – GC**

- Owns auction fields.
- Analyze:
    - BCV presence + usage across reporting/Arena/LQS/Insights, data size.
- Validation:
    - Use auction validation results (counts, status, price fields) to fill `bcv_value_match`.

**Candidate – GC**

- Same as auction, but for candidate fields:
    - Deals, prices, DSP IDs, filter reasons, etc.


Previous field analysis (done by Beijing team)

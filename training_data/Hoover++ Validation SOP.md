# Hoover\+\+ Validation SOP

## 1. Purpose and Scope

This SOP documents how to run and maintain two Hoover++ validation flows:

1. L3 table-level validation between CONTROL (current Hoover model) and STAGE (Hoover++ model) tables.
2. Event-level validation between mrm\_log\_flat (current Hoover) and Hoover++ views (etl.public\_test1).

The goal is to ensure functional parity between the legacy Hoover model and Hoover++ before and after production rollout.

## 2. Pre-requisites

- Access to FW1 STG/PRD Databricks workspaces with permissions to view and manage the Hoover++ validation job(s).
- Ability to query LQS and Presto for Hoover model and Hoover++ model tables.
- Knowledge of the L3 / UBT table schemas you are validating (dimensions and metrics).
- Validation Python script available in your Databricks workspace or via GitHub:
    - validations.py: <https://github.freewheel.tv/data/hoover-model/blob/master/validation/scripts/validations.py>

## L3 Table-Level Validation SOP

### 3.1 High-Level Flow

1. Prepare CONTROL and STAGE tables with comparable hourly data.
2. Populate the validation config table with table metadata.
3. Configure and run the Databricks validation task.
4. Review results (email + logs) and perform follow-up analysis.

### 3.2 Data Preparation (L3)

#### 3.2.1 Create CONTROL and STAGE tables

FYI Only event\_hour 08 is LOADED (batch\_id 07,08,09).

- CONTROL table: clone of the existing L3 aggregation (e.g. f\_process\_request\_hourly\_sampling) in a sandbox schema.
- STAGE table: Hoover++ derived version of the same L3 aggregation, using the new model.

Example CONTROL table definition (f\_process\_request\_hourly):

```sql
CREATE TABLE fw1_prd.hoover_validations.f_process_request_hourly_hive (
  ...,
  event_date timestamp
);
```

Example STAGE table definition (f\_process\_request\_hourly):

```sql
CREATE TABLE fw1_prd.hoover_validations.f_process_request_hourly_hoover_plus (
  ...,
  event_date timestamp
);
```

Keep the schemas aligned between CONTROL and STAGE so that dimensions and metrics are comparable.

#### 3.2.2 Load hourly data

CONTROL load example:

```sql
INSERT INTO fw1_prd.hoover_validations.f_process_request_hourly_hive
SELECT *
FROM hive_data_prd_dwh_etl.aggregate.f_process_request_hourly_sampling
WHERE event_date = date_trunc('HOUR', CURRENT_TIMESTAMP()) - INTERVAL 4 HOURS;
```

STAGE load example (Hoover++ model):

- Convert the original Hoover SQL to Hoover++ / hoover\_pipeline\_compaction.
- Restrict using is\_first\_request = true where relevant.
- Add appropriate event\_hour boundaries to keep the data volume small and comparable.
- Insert into the STAGE table using the Hoover++ compaction query.

Once both tables have data for the same hour, proceed to config preparation.

### 3.3 Config Preparation (L3)

The validation job reads from a config table (default):

- fw1\_stg.kbhargava.validation\_config\_new

For each L3 table you want to validate, add a row specifying:

- control\_table: fully-qualified CONTROL table name.
- stage\_table: fully-qualified STAGE table name.
- validation\_table\_name: logical L3 / UBT table name (e.g. f\_process\_request\_hourly).
- dimensions: comma-separated list of dimension column names (STRING).
- metrics: comma-separated list of metric column names (STRING).

Example config row:

```sql
INSERT INTO fw1_prd.hoover_validations.validation_config
  (control_table, stage_table, validation_table_name, dimensions, metrics)
VALUES (
  'fw1_prd.hoover_validations.f_process_request_hourly_hive',
  'fw1_prd.hoover_validations.f_process_request_hourly_hoover_plus',
  'f_process_request_hourly',
  ''network_id', 'content_owner_id', ... , 'event_date'',
  ''ad_requests', 'total_ad_requests''
);
```

Repeat for each additional L3 table you want to validate.

### 3.4 Databricks Task Setup (L3)

You can use shared jobs (e.g. Hoover++ validations in STG/PRD) or create your own.

1. In Databricks, navigate to the Hoover++ validation job (or create one).
2. Under the Tasks tab, click "Add Task".
3. Configure:
    - Type: Python Script.
    - Source: Workspace (point to validations.py).
    - Compute: validation\_file\_cluster (or equivalent).
    - Depends on: none (tasks should be independent).
4. Parameters example:

```json
["--validation_config","fw1_stg.kbhargava.validation_config_new",
 "--validation_table","f_process_request_hourly"]
```

1. Save the task.

### 3.5 Running the L3 Validation

1. From the job page, trigger the task via "Run now".
2. The script computes start\_date and run\_hour internally and compares CONTROL vs STAGE using the config.
3. On completion:
    - If data matches within tolerance: no email is sent (success case).
    - If data mismatches: an email is sent to the configured recipients with:
        - Summary of mismatches.
        - Sample SQL to reproduce / investigate.

You can adjust the email recipients in the script (or comment out the Hoover channel address) to route notifications to yourself or the Hoover team.

### 3.6 Reviewing Results and Follow-up

1. Check the Databricks Run for task status and logs (errors, stack traces, configuration issues).
2. If an email was sent:
    - Review the attached SQL and sample mismatched data.
    - Use LQS/Presto to re-run the queries and inspect differences.
3. Typical mismatch causes:
    - Schema evolution differences between Hoover and Hoover++.
    - Missing or mis-mapped dimensions or metrics in the Hoover++ transformation.
    - Data filters (e.g. event\_hour, is\_first\_request) not aligned between CONTROL and STAGE.
4. Capture findings and raise PRs against hoover-model / Hoover++ transformations to close gaps.
5. Re-run the validation until mismatches are resolved.

---

## 4. Event-Level Validation SOP

### 4.1 High-Level Flow

1. Identify the entity / table to validate (request, slot, ad, candidate, ack, auction).
2. Build comparable queries in mrm\_log\_flat.default and Hoover++ views (etl.public\_test1.\*) on sampled data.
3. Compare key fields at event level using LQS.
4. Investigate and fix discrepancies.

### 4.2 Data Sources

- Current Hoover model tables (event-level):
    - mrm\_log\_flat.default.ack
    - mrm\_log\_flat.default.ad
    - mrm\_log\_flat.default.auction
    - mrm\_log\_flat.default.candidate
    - mrm\_log\_flat.default.request
    - mrm\_log\_flat.default.slot
- Hoover++ model views (backward-compatible):
    - etl.public\_test1.ack
    - etl.public\_test1.ad
    - etl.public\_test1.auction
    - etl.public\_test1.candidate
    - etl.public\_test1.request
    - etl.public\_test1.slot

Implementation SQL for the Hoover++ views lives in:

- [https://github.freewheel.tv/data/hoover-model/tree/master/views/lqs\_views](https://github.freewheel.tv/data/hoover-model/tree/master/views/lqs_views)

If you find issues in the Hoover++ SQL, fix them in this repo.

### 4.3 Sampling and Partitioning

To ensure you are comparing the same underlying data:

- Use the shared sampled data flag:

```
AND bitwise_and(request__bit_flags, 576460752303423488) > 0  -- 1 << 59 (sampled flag)
```

- Use appropriate partition keys:
    - mrm\_log\_flat.default: process\_batch\_id.
    - etl.public\_test1.request: event\_hour.

When comparing underlying Hoover++ batch tables directly, use hoover\_batch under hoover\_delta with the same event\_hour.

### 4.4 Running Event-Level Comparisons

1. Construct a baseline query against mrm\_log\_flat.default.\* for the entity you care about (e.g. request).
2. Construct a corresponding query against etl.public\_test1.\* using Hoover++ data.
3. Align filters:
    - Same date / hour partition.
    - Same sampling flag and any other necessary predicates.
4. Run both queries in LQS and compare:
    - Row counts.
    - Key field values.

Use existing LQS examples for reference when building queries for each entity.

### 4.5 Investigating Discrepancies

When key fields do not match between mrm\_log\_flat and Hoover++ views:

1. Confirm both queries are using the same sampled data and partitions.
2. Check whether the Hoover++ view logic in lqs\_views is aligned with the legacy Hoover derivation.
3. Identify whether differences are expected (e.g. deprecated fields, intentionally removed attributes) vs. regressions.
4. For regressions, open PRs against the Hoover++ view or upstream model.
5. Re-run event-level comparisons until parity is achieved or documented.

---

## 5. Operational Guidelines

- Document each new table or entity validation (L3 or event-level) with:
    - Purpose of the validation.
    - Control and stage sources.
    - Dimensions / metrics being compared.
    - Known intentional differences.
- Keep validation\_config\_new up to date as coverage grows.
- Use shared Databricks validation jobs where possible; clone tasks per table.
- Route validation emails to the appropriate Hoover / Hoover++ owners.
- Treat persistent mismatches as tracked work items (Jira/PRs) and revisit validations after fixes.

## 6. Contacts

- Primary owner: @Bhargava, Karan
- Hoover / Hoover++ team distribution lists and Slack channels as configured in the validation script.

# Hoover\+\+ Validation Tool Tech Design



## Background

Everyone knows what Hoover++ is (the next generation of data processing (and now modeling thanks to UBT) designed to efficiently cut out bloat currently present in the Hoover model. It is designed to collect, transform and analyze large-scale advertising data.

Hoover++ builds upon the foundation of Hoover by introducing enhanced scalability, modularity, and support for more complex data workflows

There is, however, a need for validating data between the current Hoover and Hoover++ models. Since Hoover++ redesigns how different entities are stored in the data model, we need to verify that these entities (and the underlying data) is still the SAME. 

This "tool" tries to solve the above ask. It is built to be able to validate a data between 2 sources; here in named as "stage" and "control"

For the purposes for this wiki, the control table(s) in our case is the current hoover model's output. And the stage table(s) in our case is the new Hoover++ model's output.

## Goal

The goal here is to have a mechanism to be able to validate between Hoover \<\> Hoover++ (and UBT) data sources and flag any inconsistencies and problems that may arise.

## Tech Design

The script is based on a PySpark notebook that we can use to compare 2 different datasets.

There are some pre-requisites required:

- Table dimensions and metrics
    - Need to add this to the validation table so the validation script can generate SQLs and run analysis as needed. 
- Compare query (using exceptAll between control data and stage data)
    - Before the compare query, we will generate an xxhash64 for each row.
        - If there are differences between dimensions/ metrics, we can easily flag them.
- The start date (the date we want to compare)
- The run hour (the hour we want to compare)

### Diagram


### Hoover \<\> Hoover++ Validations

#### Event Level Validations

For validating event level data, we need to first compact the current Hoover++ DLT. This is because the sheer volume of data is too much for a simple SQL warehouse to handle. 

Once the compaction is complete, we have a few ways we can do the comparisons.

- Create 1:1 COPY of current hoover table as a view but using Hoover++ SQL
    - This will also come in handy for downstream users to migrate their current jobs to new Hoover++
- Use request\_\_timestamp or request\_event\_date from both tables (MINUS 1 hour INTERVAL) to get event level data from both systems
    - The caveat here is that we'll have to wait a few hours for data to "settle". Proposal is we wait a maximum of 3 hours for ALL callbacks to return so we're comparing the FULL picture 

##### Why wait before comparing?

- In streaming pipelines (like Hoover++), data can arrive late due to network delays, retries, or out-of-order events.
- Batch pipelines (like Hoover) typically process all data for a time window at once, so late data is less of an issue.
- To ensure a fair (apple-to-apple) comparison, both systems must have received all relevant data for the time window being compared.

##### How to choose the waiting period?

- Analyze historical data to determine the typical delay for late-arriving events (e.g., callbacks).
- If most callbacks arrive within 1 hour, but a small percentage arrive later, a 3-hour buffer is a conservative choice to ensure completeness.
- This means: only compare data for a given request\_event\_date and hour after at least 3 hours have passed since that hour ended.

##### How to verify the approach?

- Track the count of records for a given hour over time. If the count stops changing after 3 hours, the window is stable.
- If counts continue to change, consider increasing the buffer or investigating sources of late data.

  

##### Aggregated Level Validations

For aggregated table validations between Hoover \<\> Hoover++ there are a few ways we can go about it. 

Since Optimus is going to be able to make sampled L3 tables accessible in DBX via Hive Metastore, we can easily validate the tables using the above approach.

- Since the current L3 tables ([Transformer L3 Tables](https://github.freewheel.tv/data/transformer/tree/2058615427262fa5b5ae750d36efd3e6a3130262/config/optimus/sql)) are built directly from current hoover model tables, the effort to transform them to Hoover++ SQL is not high
    - Such conversion is tracked here: <https://freewheel.atlassian.net/wiki/spaces/~kbhargava/pages/522256908/Hoover+Hoover+L3+Tables>
    - Most L3 tables can be converted to Hoover++ SQL with minimal changes, except for a few that use custom UDFs. These may require additional work to port or rewrite the UDFs for Hoover++.

Comparison approach:

- Use the documented SQLs to generate L3 tables from both Hoover and Hoover++ sources.
- Create views (materialized or not) in Databricks for both sets of L3 tables.
- Import current L3 table data into Databricks, so both versions are accessible in the same environment.
- Run comparisons between the two sets of tables within Databricks, leveraging Spark SQL for efficient analysis.

##### Outstanding questions:

- Should we build the new L3 tables from event level DLT and then compact? Or should be first compact the Hoover++ event level DLT and then build the new L3 tables?  
    - If we base L3 tables off compacted Hoover data:
        - Use the already-compacted (pre-aggregated) Hoover++ tables as your data source.
        - Write SQL queries that select and further aggregate as needed (e.g., by hour, by key).
        - This approach is efficient since the data is already deduplicated and possibly partitioned for fast access.
    - If we create event-level L3 table, then aggregate:
        - First, create a raw event-level L3 table in DBX using the SQL from step #1.
        - Store this table in the Hive metastore or as a Delta table.
        - Use a Databricks notebook or SQL Warehouse to run aggregation queries (e.g., GROUP BY hour, key) on this event-level table.
        - Write the results to a new, aggregated L3 table (e.g., hourly aggregates).
            - 2nd approach(event-level then aggregate) provides flexibility and allows for re-aggregation with different logic or time windows as needed.

### What happens when there is non-identical data?

We are expecting that there will be non-identical data between the 2 systems. Since things have moved around and are now potentially calculated different. There are few ways we can figure out differences:

1. We figure out rows that are not identical using row-hash and field-level comparisons (we can use the validation tool as mentioned above)
    1. Use row hashes to quickly identify which rows differ between datasets.
    2. Once differing rows are found, compare individual fields to pinpoint which columns are mismatched.
    3. This helps isolate whether the issue is with specific fields or entire rows.
2. Check for missing/ extra rows, mismatched values and late-arriving data
    1. Count rows in each dataset to detect missing or extra records.
    2. For mismatched values, compare key columns and metrics to see if differences are systematic or random.
    3. Investigate late-arriving data by checking timestamps or event dates; ensure both pipelines have processed all relevant data.
3. Compare intermediate aggregates (e.g. counts per key) to localize discrepancies
    1. Group data by key fields (e.g., networkId, event type) and compare counts or sums.
    2. This can reveal if discrepancies are concentrated in certain keys, helping to localize the problem.
4. Review schema and transformation differences between Hoover and Hoover++. (this is most likely the biggest culprit for differences)  
    1. Check for changes in field names, types, or nesting.
    2. Examine transformation logic (e.g., SQL, ETL steps) for differences in how data is processed or mapped.
    3. Schema mismatches or transformation bugs are common sources of data divergence.

#### Manual Comparisons (since there is differing data)

Since the validation tool provides an aggregated view of data mismatches, we will need to further dive deeper (transaction level compares) to see which column is different and why. 

The validation tool essentially does the following:

- Preliminary steps
    - Add row\_hash (xxhash64) and row\_id to read in data (monotonically\_increasing\_id)
        - Use exceptAll to check if data matches. If it does, GREAT! If not:
            - First layer check
                - Use the validate query (SELECT COUNT(DISTINCT \<dim\>), SUM(metric)) to see the gravity of differences.
            - Second layer check
                - Get rows with differences using the row\_hash 

  

```py
diff_control_rows = control_hashed_with_id.join(diff_control_hashes, on="row_hash", how="inner")
diff_stage_rows = control_hashed_with_id.join(diff_stage_hashes, on="row_hash", how="inner")

diff_control_rows.show(truncate=False, vertical=True)

# same with stage
```

This returns data like:

  

```
Control rows with differences:
-RECORD 0-----------------------------------------------------------------
 row_hash                                           | 2525618873662241769 
 date                                               | 2025-12-19          
 hour                                               | 05                  
 num_process_batch_id                               | 1                   
 num_network_id                                     | 24                  
 num_content_owner_id                               | 15                  
 num_distributor_id                                 | 16    


Stage rows with differences:
-RECORD 0-----------------------------------------------------------------
 row_hash                                           | -655023871983863922 
 date                                               | 2025-12-19          
 hour                                               | 05                  
 num_process_batch_id                               | 1                   
 num_network_id                                     | 28                  
 num_content_owner_id                               | 20    
```

  

The next steps after we've figured this out is to actually DIVE DEEP into the data to see why. Here we will NOT be using the aggregated table data (not the VALIDATE\_QUERY) but reading in the actual table(s) and generating the SQLs.

One additional step (that was recently added) was doing row-by-row analysis of the table to see which rows are present in 1 but not the other (limited to 1000 rows).

- Since we already have the dimensions and metrics available to us, we can compare ROW by ROW and see which rows are present in one DF and not in the other.

Additionally, there are a few more things we can do (this is part of the script and will be attached to the EMAIL as a SQL file):

1. Create a JOIN SQL to do:
    1. Full Outer Join on Key Columns Join the full tables on all USER\_DIMENSIONS (the key columns).
    2. Comparison Columns For each column in USER\_DIMENSIONS + USER\_METRICS, add a boolean column indicating if the values differ.
    3. Filter to Rows with Any Difference Add a WHERE clause to keep only rows where at least one comparison column is true.
2. Check for duplicates
    1. No duplicate rows in either table for the join keys. Duplicates can cause mismatches.
3. Null/Type Mismatches
    1. Compare schemas and check for type mismatches or unexpected NULLs in key columns
4. Unmatched keys
    1. Identify keys present in 1 table but not in the other (anti-join on keys)
5. Distribution Analysis
    1. Compare value distributions for key metrics (can define as many metrics as needed) and dimensions to spot outliers or skew
6. Sample problematic rows
    1. Randomly check rows with differences and inspect them for data issues
7. Truncation/ Precision Issues
    1. For decimal/ double type columns, check for rounding differences.
8. Export Differences
    1. Export to a diff table to run FURTHER analysis. 

  

  

---

## Scheduling

#### Databricks Job

The above script has been converted from PySpark to plain old python so it can run on a Databricks job cluster.

<https://freewheel-fw1-dev-e2.cloud.databricks.com/jobs/753910249184678?o=2929365364440953>

We can run this cluster either manually (for testing purposes) or we can automate it to run. 

The job does the following:

- Read in argument for the config table
- Read in argument for the table name we want to compare
- Read in argument for start date and run hour (pending todo)

It then runs a query to get all the information mentioned above (validation query and compare query)

It then runs the job via spark and outputs the results (via email for now).

##### DBX

In databricks, there's an easy way to schedule a job run using schedules and triggers; which is really handy. 

However, this might not work in our case. 

The python script is designed to read in parameters in the start 

```py
["--validation_table_name","fw1_stg.kbhargava.validation_config_table","--validation_table","f_order_selected_hourly"]
```

 Even if the config table name will not change, the name of the validation\_table will (since we won't just be validating 1 table.)

Possible workarounds:

- Select a handful of tables we want to validate, hard code them in the script and run them sequentially. (not preferred)
    - However, this would require a script update EVERY TIME we want to validate new tables that aren't currently being validated.
- Add multiple tasks to 1 job with different task parameters, then run them on a schedule. (preferred)

##### Airflow

The more tedious yet powerful option is using airflow to orchestrate running jobs. 

High level, it would look something like:

- Create job in Databricks (already created)
- Create and saveDAG in Airflow  
  

```py
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.utils.dates import days_ago

default_args = {
  'owner': 'airflow'
}

with DAG('databricks_dag',
  start_date = days_ago(1),
  schedule_interval = None,
  default_args = default_args
  ) as dag:

  opr_run_now = DatabricksRunNowOperator(
    task_id = 'run_now',
    databricks_conn_id = 'databricks_default',
    job_id = <JOB_ID>
  )
```

  

- Verify DAG creation in Airflow 

This approach, is doable, however adds another layer of complexity that we can avoid if we are okay with the workarounds mentioned above.

MWAA would become another technology we'd have to monitor.

  

---

## Current State

For testing purposes, there are some things that are hard coded in the job. We will do the below enhancements as needed.

The current job runs comparisons for 2025-12-19 hour 05 for the \`f\_order\_selected\_hourly\` table

We will enhance the job as noted below:

### Further Enhancements

Besides the pre-requisites, we WILL also enhance the tool to:

| Task | Completed | Comments |
| --- | --- | --- |
| Add more validation queries and compare queries for L3 Tables |  | We just need the dimensions and metrics for the table and validation\_script will generate on the fly. |
| Enhance validation script (see below) | COMPLETE |  |
| Orchestrate job via DBX or MWAA | COMPLETE |  |
| Record results somewhere (Email/ Slack) | COMPLETE | Code commented out for now., |
| Add f\_supply, f\_demand, and f\_programmatic tables for UBT |  |  |

##### Script Enhancements

Rather than storing the validate and compare query in the config table, what if we were to store the dimensions and columns instead?

This way, we can:

- Dynamically calculate start\_date and run\_hour (3 hours in past UTC)  
- Generate the validate and compare query on the fly (incorporate generation into 1 script)  
- If data does not match, do further analysis of what `dimensions` do not match.   
    - Email/ Slack notification includes the count differences but ALSO specifics into which dimensions are missing certain fields. 

## Child Pages (reference)

 

## References

<https://docs.databricks.com/aws/en/jobs/scheduled>

<https://docs.databricks.com/aws/en/jobs/how-to/use-airflow-with-jobs>

<https://medium.com/apache-airflow/running-databricks-jobs-on-apache-airflow-19619387aacf>

  

## Questions?

@Bhargava, Karan

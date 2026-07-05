# H\+\+ Validation Tech Design



## Background

Given that we've almost finished the development works from current Hoover ↔ Hoover++, we need to validate the data between both to see if there's any changes. Below are a few designs for such a tool so that we can do some automated validations.

## Tracker

All JIRA tickets are housed under the epic → 

| Ticket | Status | Comment |
| --- | --- | --- |
|  | IN PROGRESS |  |
|  |  |  |

  

## Design

There are a few ways we can go about this tool. Below are a few options and we can collectively decide which makes the most sense given ENG resources and timelines.

Whichever option we choose, the main idea would be:

For current hoover model → 

- Run DWH SQL 1 (from transformer code) to create a table used for comparisons.
- Load this data into databricks delta table 
- Read this newly create table's data in databricks

For new hoover model (H++ model) → 

- Run DWH SQL 2 (from transformer code, but converted to H++ model) to create a new table/ view 
- Read this new table/ view in databricks.

### Option 1


The idea here would be to:

For current hoover model → 

- Create new external table in LQS (output location of S3)
- Run DWH SQL 1 (from transformer code) on Arena to copy data into new external table
- Load this data into databricks delta table (AutoLoader job, more below)
- Read this newly create table's data in databricks

For new hoover model (H++ model) → 

- Run DWH SQL 2 (from transformer code, but converted to H++ model) to create a new table/ view 
- Read this data and run comparisons.

Once both the table(s)/ view(s) are created, read data; run comparison SQL (column by column)

- Send email with column counts between old and new model
    - For diff'ed columns, we'd need to run further analysis as to why (manual comparison on LQS for current model vs new model in databricks)

  

This would be the preferred way of doing things since we can easily build the same concept for UBT validations as well. Create a new table for each "stage" and run comparisons between new and old models.

  

### Option 2


Similar to option 1 but we'd need to create a script/ tool to read data from S3, since the current hoover model is hashed and the data is not "partitioned" directly in S3.

This would need some more design on the script/ tool to do so.

  

### Option 3


This is very similar to Option 2, however, we'd query the hidden field (`__path__`) from each table to:

- Get the location of each parquet file in S3.
- Load this data into databricks
- Run comparisons between this data and new H++ model.

  

## AutoLoader for DataBricks

A very simple databricks job to load data for the current hoover model from S3 into databricks so we have 1 tool to do validations between the CURRENT and H++ models. 

```py
cloud_path = "<path to S3>"
table_name = "<delta_table_name>"

df_read = spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "parquet")
        .option("cloudFiles.schemaLocation", f"{cloud_path}_schemas")
        .load(cloud_path)

df_read.writeStream
        .option("checkpointLocation", f"{cloud_path}_checkpoints")
        .trigger(processingTime='1 minute') # Or use .trigger(once=True) for batch processing
        .partitionBy("batch_id", "network_id") # we can partition by n number of columns
        .toTable(table_name))
```

  

## Comparisons

For comparisons, we'll use the validations done by Daniel for UBT and do the same for these. 

The main idea would be to either get a `count`  or `sum`  (depending on column type, either a dim or a metric) and do a `subtract` between columns and see if differences exist. 

Reference → <https://github.freewheel.tv/data/hoover-model/tree/test-ubt-poc/validation>

## Questions?

- Is there a way we can attach a trigger from Arena to run the databricks load job after a successful execution?
- How many hours of data should we compare? Odd hours? Daily?
    - Since there is a lot of auction data, hourly is preferred.
- When writing out to S3, possible to write it out to a path such as: `/<date>/hour/` ?
- When using the Arena job, how to add a partition?

  

- How to align the data between 2 streams?
    - Use request\_timestamp or event\_timestamp to get same data between 2 data sources (current Hoover and H++)

 

# Hoover\+\+ Validation

# Background

Hoover++ model has a completely different structure from the current flattened Hoover table; it is designed to run on Databricks output as delta table. We need to build a cross-validation tool to validate the correction of the Hoover++ by comparing aggregate tables from different inputs.


# Options

## Option 1

Use PRD hoover data to check with Hoover streaming, need to limit by the event\_timestamp to align the data from both side.

Need to fetch data from different platforms to check in local env.


## Option 2

Use the same input.

Check data by databricks engine.


  

# Previous Design

[\[KT\] Hoover Cross Validation Tool](https://freewheel.atlassian.net/wiki/display/Infrastructure/%5BKT%5D+Hoover+Cross+Validation+Tool)

<https://freewheel.atlassian.net/wiki/spaces/~bxiao/pages/213354086/New+Hoover+Cross+Validation>

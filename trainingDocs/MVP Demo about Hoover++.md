# MVP Demo about Hoover\+\+

## 

## Background

Our previous Hoover model is very bloated. There are massive duplication points (see image below). This duplication is particularly visible for context info like `request.context`  and `visitor`  entities which are duplicated in all of the 7 tables. 


Specifically for the `ack`  table, thousands of fields (5000+) are needed to link callbacks to different entities. There is also inefficiency in supporting metric calculations which leads to overly complicated SQL logic to calculate a metric. 

There are more reasons as highlighted in , so we won't be reiterating those. 

We will, instead, introduce the new Hoover ++ model.

## New Model (High Level)


The new model (please click into it to full screen it), is defined above. The idea here is to reduce duplication by having 1 table only; instead of 7, that would house every entity inside of it. Yes, this introduces some unnesting logic, but with the redesign of the DWH models as well, please reference here → , this makes things easier for both Hoover and downstream teams.

The main goals are to create 1 single pipeline for both AIM and TVP logs, provide low latency offer multiple SLA requirements for near realtime ETL (E2E latency of \< 30 minutes) and Analytics requirements (E2E latency of \> 30 minutes)  ~~through 1 pipeline~~ and save cost.

Additionally, analysis was completed to see what columns are actually queried. These were broken down into ETL usage, SoS usage, Arena usage, and LQS usage. If a column is used by the first 3, we included it in the new model. If it's not, we check if the LQS query is not by an `sa` (headless) accounts and is not queried a LOT. If it isn't, it's removed; otherwise it's included in the new pipeline.

The new pipeline would look something like this:

  


  

TL;DR: we will created an E2E 5 minute latent pipeline that will be "inaccurate" for the first 2 hours. After the 2 hours, there will be a optimization/ backfilling job that joins IVT data (IVT data is joined post), and provide the DWH a complete picture (see here → )

For more detailed design points and understanding, please see here →  and here → 

## Progress Updates

Since we've started design work in February, there have been a multitude of progress updates for both the model work and the pipeline work.

For Hoover pipeline:

Implementation of spark streaming pipeline to read kafka and sync data to delta table has been completed. Additionally, env setup has also been completed. CI&CD are currently in progress, alongside monitoring and performance tuning. 

For more details → 

For Hoover model:

New model repo has been initialized with designs under way for all entities: Ad, Candidate, Slot, Request, Visitor, Inventory, Auction, and Ack.

Additionally, code progress wise, many updates have happened:

- generate classes automatically using `classGenerator`  and JSON.
- some common classes have been defined
- entities in java are work in progress
- handlers are being committed day by day
- row generators have also been started.

For more details → 

## Timeline Updates

Design and Implementation for both the pipeline and model are already underway. Designs for both have already finished and the libraries for both are being designed/ implemented. 

Additionally, as mentioned above, CI/CD, monitoring and performance testing and tuning are already in progress for the pipeline. For hoover lib, design for all entities will soon be completed and communicated to downstream teams. Development is continuing alongside. 

IVT & Restatement work will start Mid-May for the pipeline and in June for Hoover model after the model is finalized.

Plan is to cutover to the new H++ model in November having completed Integration and Migration by October. This includes UT, PRD setup, tuning, testing and validations. 

For more details, see detailed diagram below:



## Key Functions

Key highlights for the new hoover model are as follows:

- Avoid duplication of data across multiple tables and have 1 merged hoover table instead of 7 (more details → )
- Get rid of conversion from Protobuf to Avro to Java; instead we convert directly from Protobuf to Java code making is an allowlist that we control.
- acks will be broken into 3 components
    - Ad Acks
    - Slot Acks
    - Request Acks
- There are 4 major categories of Hoover metrics (not all thing apply to above 3 entities) →  
    - Entity
    - Entity.Network
    - Entity.Ack
    - Entity.Ack.Network
- Networks are also broken down into 2 types (but this is only visible internally) → 
    - 
    - This is because the current `Partner`  definition has 300+ fields to support all 5 types of networks. We're breaking them apart to not have unnecessary fields.
- To deal with PII (personally identifiable information), we will add a new entity called `IVT`  in the model under `transaction` 
    - This will be made accessible to `IVT`  related jobs/ queries. 

## Questions?

 /  

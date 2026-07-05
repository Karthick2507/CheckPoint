# Hoover\+\+ with UBT Plan



# Background

The whole project goal is as follows -

  From  

> At a higher level, these are the major milestones and deliverables for the entire data team in 2026
> 
> **End of ~~April ~~May**
> 
> - Lo Beta release
> - Sampled Hoover++ with UBT
> - Socialize the new Hoover model to broader audiences so that people from other team could get prepared for the upcoming migration works.
> - Deprecate AIM ETL pipeline (migrating audience/segment related logics into both existing Hoover and Hoover++)
> 
>   
> **~~July/Auguest ~~Sep/Oct**
> 
> - Lo GA release
> - Full set data for Hoover++ with UBT
> - Migrate all reporting products into Hoover++ (V4 logs, ETL, billing, custom reports etc)
> - Deprecate legacy pipelines(SOS, Optimus, jetfire etc) and aggregate tables(L3, domain etc)
> 
>   
> **End of ~~Nov~~Dec**
> 
> - Finishes all other user migration works (LQS, Arena, Biz Monitor etc)
> - Deprecate existing Hoover pipeline and data.
> - Binlog optimization for cost savings
> - Consolidation of trouble-shooting workflow, pipelines and data models
> 
>   
> **~~End of Dec ~~2027**
> 
> - Data governance enhancements (data catalog, observability, lineage tracking, retention management, access control over PII fields etc)

When converted to the Hoover++ with the UBT part, the goal is

1. Before the end of ~~April ~~May,
    1. UBT
        1. Finish all the basic implementation/testing of
            1. Supply
            2. Demand
            3. Prog. 
            4. UBT view
        2. UBT Validation
            1. design ready
            2. Supply table ready
            3. Continue other tables
    2. Finish all Hoover++ work, including but not limited to 
        1. Finish View.
        2. Finish the validation work/tool.
        3. Finish adding Hoover++ troubleshooting fields
        4. Finish Hoover++ user migration guide
        5. Hoover++ Feature parity
2. Before Sep, before GA
    1. Finish UBT validation work.
    2. Finish the validation based on PRD data before GA for Hoover++ and UBT.
3. Before the end of Dec
    1. Support downstream migration

  

# TODO

1. Logic and modeling definition
    1. Summarize the UBT logic, including dimensions and metrics. 
        1. supply
        2. demand
        3. prog
        4. UBT view
    2. Review with the team about the common attributes, network dimension, metrics, and UBT views.
2. New member business catch-up
    1. ADS business training
    2. Data-specific training
    3. Hoover KT model training
    4. Review UBT logic wiki
3. UBT implementation
    1. Supply
    2. Demand
    3. Prog
4. UBT test
    1. UT
    2. Regression
5. UBT View
6. UBT validation
    1. Depends on Hoover++ validation process.
    2. Re-use Hoover++ validation tool
    3. By UBT view.
7. Dependency - Remaining work of Hoover++
    1. Troubleshooting part of the Hoover++ models has not been implemented yet
    2. Hoover++ views
        1. development
        2. validation
        3. performance tunning
    3. Hoover++ data validation
        1. Validation tools design and implementation
        2. Case validation.
    4. New feature catch-up
    5. User migration guide between the logical views and existing flattened tables.

# Detailed Plan

| # | Item | Description | Owner | Definition of Done | Start/End Date | Dependency | Status | Deliverable | Comment(risk/mitigation/...) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New memberbusiness catch-up | Catch up on business background and concepts to help better understand the data model |    | Finish 1. ADS business training 2. Data-specific training 3. Hoover KT model training 4. Review UBT wiki | -  | No | FINISHED |  |  |
| 2 | Summarize the UBT logic, including dimensions and metrics.  | 1. Supply 2. Demand 3. Prog ( The wiki is organized by 1. common attributes 2. dimensions 3. metrics ) |      | Wikis are finished for  1. Supply 2. Demand 3. Prog Ready to review. | -  | No | FINISHED |  |  |
| 3 | Summarize the UBT view logic | UBT View |    | Wikis are finishedLogic is finalizedReady to review | -   | depends on #2 | TODO |  |  |
| 4 | Review the UBT logic wiki | 1. Every team member reviews the wikis and comments on the questions 2. Group review - on sync meetings, owners help review the logic Materials  | All members | All the fields on the 3 UBT wiki are finalized.start from  1. network dimension 2. common attributes 3. network metrics Need to involve the DWH team |   | depends on #2 | IN PROGRESS |  |  |
| 5 | Review the UBT view wiki | Group view - on sync meetings, owners help review the logic | All members | All the fields on the 3 UBT view wiki are finalized. |  | depends on #3 | TODO |  |  |
| 6 | UBT implementation - Supply | Refer to the Supply category of the three wikis and complete all field implementations, unit testing, and regression testing.**We can utilize DWH f\_supply\_hourly to check the unclear logic, not implementing the f\_supply\_hourly** |    |  | -   | depends on #2, #4 | IN PROGRESS |  |  |
| 7 | UBT implementation - Demand | Refer to the Demand category of the three wikis and complete all field implementations, unit testing, and regression testing.**We can utilize DWH f\_demand\_hourly to check the unclear logic, not implementing the f\_demand\_hourly** |  |  | -  | depends on #2, #4 | IN PROGRESS |  |  |
| 8 | UBT implementation - Prog | Refer to the Programmatic category of the three wikis and complete all field implementations, unit testing, and regression testing.**We can utilize the DWH table** - **[f\_domain\_programmatic\_mkpl\_hourly.sql](https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f_domain_programmatic_mkpl_hourly.sql)** - **f\_domain\_programmatic\_ni\_hourly.sql** **to check the unclear logic, not implementing those tables** |  |  | -   | depends on #2, #4 | IN PROGRESS |  |  |
| 9 | UBT implementation - View | Implement the UBT View logicFinish the performance test |  |  | -  | depends on #3, #5 | TODO |  |  |
| 10 | UBT validation Design | Design ready |  | Start from Supply validation |   | depends on # 103 | TODO |  |  |
| 11 | UBT validation | Implementation and testing. |  |  |   | depends on #10, #103 | TODO |  |  |
|  |  |  |  |  |  |  |  |  |  |
| 101 | Hoover++ troubleshooting fields | Adding Hoover++ troubleshooting fieldsTODO: How to validate this?? |  |  |  |  |  |  |  |
| 102 | Hoover++ view  | 1. development 2. validation 3. performance tunning |  |  |  |  |  |  |  |
| 103 | Hoover++ data validation | 1. Validation tools design and implementation 2. Case validation. |  |  |  |  |  |  |  |
| 104 | New feature catch-up |  |  |  |  |  |  |  |  |
| 105 | User migration guide between the logical views and existing flattened tables. |  |  |  |  |  |  |  |  |

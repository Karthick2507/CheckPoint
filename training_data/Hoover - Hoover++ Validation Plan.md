# Hoover <\> Hoover\+\+ Validation Plan

## **Executive Summary**

This plan outlines the validation approach for comparing data between current Hoover and Hoover++ models before the June 2026 deadline. The validation will be conducted at two layers: **aggregated data** (L3 tables) and **event-level data** (raw Hoover tables) with more resources joining in to help.

## **1. General Approach**

### **1.1 Validation Strategy**

The validation will follow a **two-layer approach**:

1. **Aggregated Data Layer (L3 Tables)**
    - Validate sampled L3 tables in PRD using pre-written SQLs
    - Compare Hoover++ aggregated output against current Hoover L3 tables
    - Focus on tables: `f_sa_auction_hourly`  , `f_order_selected_hourly` , `f_order_sa_delivered_hourly` , `f_sa_bid_hourly`  , `f_process_request_hourly` 
2. **Event-Level Data Layer**
    - SQL-based manual validation using backwards-compatible views
    - Compare raw Hoover data with Hoover++ event-level data
    - Leverage sampled flag present in old model for apples-to-apples comparison

### **1.2 Data Sampling Approach**

- **Sampling Rate**: 1/1024 (approximately 0.1%)
- **Sampled Data Source**: Kafka topic with selected partitions (1 partition for 0.1% rate, 10 partitions for 1% rate, only partition #666 has data in the kafka topic 'pair\_sampling')
- **Sampled Tables Available**:
    - `f_sa_bid_hourly_sampling`
    - `f_sa_auction_hourly_sampling`
    - `f_process_request_hourly_sampling`
    - Additional tables to be enabled as needed (tracking JIRA → )

### **1.3 Validation Tool**

Based on existing validation frameworks at FreeWheel, the validation will utilize:

- **Validation tool** for comparing Delta table outputs
- **SQL-based comparison queries** for aggregated data
- **Row count and metric validation** for completeness

## **2. Task Breakdown**

### **Phase 1: Preparation & Setup**

**Target Release: 7.15.1 (Complete by mid-March 2026)**  
**Duration: 2 weeks (Early March)**

| Task | Owner | Duration | Target Date | Dependencies |
| --- | --- | --- | --- | --- |
| Set up validation environment in Databricks | Karan Bhargava | 3 days | Week 1 (Mar 3-5) | Access to PRD sampled data |
| Enable sampling for additional L3 tables | Aman Shankhdhar | 2 days | Week 1 (Mar 3-4) | TVP-65116 |
| Prepare validation SQLs for L3 tables | Hoover++ Team | 5 days | Week 1-2 (Mar 3-7) | SQL templates from Xinyu/Karan |
| Set up backwards-compatible views | Hoover++ Team | 3 days | Week 2 (Mar 10-12) | Hoover++ schema finalized |
| Configure validation tool and test framework | Karan Bhargava | 2 days | Week 2 (Mar 13-14) | Validation tool access |

**Deliverables for 7.15.1:**

- Databricks environment ready
- All sampled L3 tables accessible
- Validation SQL templates tested and committed
- Backwards-compatible views deployed
- Validation tool configured

### Phase 2: Aggregated Data Validation

**Target Release: 7.16 (Complete by mid-April 2026)**  
**Duration: 4 weeks (Mid-March to Mid-April)**

| Task | Owner | Duration | Target Date | Dependencies |
| --- | --- | --- | --- | --- |
| **Table 1: f\_sa\_auction\_hourly** |  |  |  |  |
| - Run validation SQL | Validator | 2 days | Week 3 (Mar 17-18) | Phase 1 complete |
| - Analyze discrepancies | Validator | 1 day | Week 3 (Mar 19) | Validation results |
| - Document findings | Validator | 1 day | Week 3 (Mar 20) | Analysis complete |
| **Table 2: f\_order\_selected\_hourly** |  |  |  |  |
| - Run validation SQL | Validator | 2 days | Week 3 (Mar 17-18) | Phase 1 complete |
| - Analyze discrepancies | Validator | 1 day | Week 3 (Mar 19) | Validation results |
| - Document findings | Validator | 1 day | Week 3 (Mar 20) | Analysis complete |
| **Table 3: f\_order\_sa\_delivered\_hourly** |  |  |  |  |
| - Run validation SQL | Validator | 2 days | Week 4 (Mar 24-25) | Table 1 complete |
| - Analyze discrepancies | Validator | 1 day | Week 4 (Mar 26) | Validation results |
| - Document findings | Validator | 1 day | Week 4 (Mar 27) | Analysis complete |
| **Table 4: f\_sa\_bid\_hourly** |  |  |  |  |
| - Run validation SQL | Validator | 2 days | Week 5 (Mar 31-Apr 1) | Table 2 complete |
| - Analyze discrepancies | Validator | 1 day | Week 5 (Apr 2) | Validation results |
| - Document findings | Validator | 1 day | Week 5 (Apr 3) | Analysis complete |
| **Table 5: f\_process\_request\_hourly** |  |  |  |  |
| - Run validation SQL | Validator | 2 days | Week 5 (Mar 31-Apr 1) | Table 2 complete |
| - Analyze discrepancies | Validator | 1 day | Week 5 (Apr 2) | Validation results |
| - Document findings | Validator | 1 day | Week 5 (Apr 3) | Analysis complete |

**Checkpoint: Mid-April 2026**

- All L3 tables validated
- Discrepancies documented
- Ready for event-level validation

### Phase 3: Event-Level Data Validation 

**Target Release: 7.16 (Complete by early May 2026)**  
**Duration: 4 weeks (Mid-April to Mid-May)**

| Task | Owner | Duration | Target Date | Dependencies |
| --- | --- | --- | --- | --- |
| Identify key event-level fields for validation | @Bhargava, Karan | 2 days | Week 7 (Apr 7-8) | Schema documentation |
| Write SQL queries for event-level comparison | Validator  | 5 days | Week 7-8 (Apr 9-15) | Backwards-compatible views |
| Execute event-level validation queries | Validator  | 5 days | Week 8-9 (Apr 16-22) | Queries tested |
| Analyze event-level discrepancies | ALL validations | 3 days | Week 9 (Apr 23-25) | Query results |
| Document event-level findings | @Bhargava, Karan  | 2 days | Week 10 (Apr 28-29) | Analysis complete |

**Checkpoint: End of April 2026**

- Event-level validation complete
- All discrepancies categorized
- Issue list finalized

### Phase 4A: Hoover Feature Catch-up

**Target Release: 7.16 (Complete by mid-May 2026)**  
**Duration: 2 weeks (Early-Mid May)**

This phase addresses **NOT STARTED** items from the Feature Catch-up wiki.

For up to date page: <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191811160/New+Feature+Catch+Up+New+Model>

### Complete Feature Catch-up List (7.10 - 7.16)

### 7.10 Features:

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-44245 | Implement Privacy Logic For Unified ADS/IDS Logging | Xuekui Bai | NOT STARTED | High | Week 11 (May 5-6) | PRs: /947, /948 |
| TVP-47886 | Integration Test for support remaining PT monetisation paths | Unknown User (bxiao) | NOT STARTED | Medium | Week 11 (May 7-8) | PR: /950 |
| TVP-48836 | Fix aim log processor remove logic | Unknown User (bxiao), Ruonan Li | NOT STARTED | Low | Week 11 (May 9) | PRs: /951, /953 |

### 7.11 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-51858 | Schema change of unconstrained\_opportunity\_in\_played\_slot + Support MPE: Average Inventory Floor Price | Ruonan Li | NOT STARTED | High | Week 11-12 (May 12-13) | PR: /956 |
| TVP-51853 | Remove fw\_ssp condition | Peng Gao | NOT STARTED | Medium | Week 12 (May 14) | PR: /959 |
| TVP-52894 | Add raw opportunity\_in\_played\_slot and avails\_in\_played\_slot + MPE Average Inventory Floor Price Implementation | Yu Wang, Ruonan Li | NOT STARTED | Low | Week 12 (May 15-16) | PRs: /960, /961, /965, /966 |
| **UNSURE** | Add supply chain node to transaction table | Peng Gao | UNSURE | TBD | TBD | PR: /957 - **Need decision: Do we need this?** |

### 7.12 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-55840 | Design and Implement for the AIM pb loading | Xuekui Bai | NOT STARTED | Medium | Week 12 (May 19) | PR: /972**Unsure. Needs more confirmation and understanding.** |
| TVP-55613 | Update schema for aim segment cost + Update logic for aim segment cost | Xuekui Bai | NOT STARTED | Medium | Week 13 (May 20-21) | PRs: /975, /977 |
| TVP-56500 | Fix the field name bug for aim metadata schema | Anran Li | NOT STARTED | Medium | Week 13 (May 22) | PR: /976 |

### 7.13 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-57722 | Add bit\_flag for audience extension usage | Xuekui Bai | NOT STARTED | Medium | Week 13 (May 23) | PR: /985 |
| TVP-58970 | Add openrtb\_ad\_traffic for Netflix integration | Ruonan Li | NOT STARTED | Medium | Week 14 (May 26) | PR: /986 |

### 7.14 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-62949 | Add aim\_audience\_targeting\_expression for phase 2 billing OR logic | Xuekui Bai | NOT STARTED | High | Week 14 (May 27) | PR: /998 |
| TVP-57289 | Log sampled info in Current Hoover for sample validation | Ruonan Li | NOT STARTED | Low | Week 14 (May 28) | PRs: /991, /992 - **Need decision: Do we need this?** |
| TVP-61530 | PB change to support PG | Anran Li | NOT STARTED | Medium | Week 14 (May 29) | PR: /994 |

### 7.15 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| ~~TVP-61908~~ | ~~Update private methods to public~~ | ~~Karan Bhargava~~ | ~~NOT STARTED~~ | ~~P2~~ | ~~Week 15 (Jun 2)~~ | ~~PRs: /995, /999 - **Maybe needed in redesign of v4 logs**~~ |
| TVP-62388 | Bug fix for only set raw\_inventory\_distinct\_avails\_in\_played\_slot only on ack | Ruonan Li | NOT STARTED | Medium | Week 15 (Jun 3) | PR: /996 |
| TVP-57689 | Write non tracked audience ids for all networks | Ruonan Li | NOT STARTED | Medium | Week 15 (Jun 4) | PR: /980 |
| TVP-62110 | Design and implementation of hoover max\_cpm metric logic phase II - OR logic between audiences | Xuekui Bai | NOT STARTED | High | Week 15 (Jun 5-6) | PRs: /1001, /1002 |

### 7.15.1 Features

| Ticket | Description | Owner | Status | Priority | Target Date | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| TVP-57689 | Write non tracked audience ids for all networks | Peng Gao | NOT STARTED | Medium | Week 15 (Jun 9) | PR: /1004 - **Duplicate of 7.15 item?** |
| TVP-65113 | Add schema for segment flags | Xuekui Bai | NOT STARTED | Medium | Week 15 (Jun 10) | PR: /1009 |

### Summary

| Release | Total Features | NOT STARTED | UNSURE | High | Medium | Low |
| --- | --- | --- | --- | --- | --- | --- |
| 7.10 | 3 | 3 | 0 | 0 | 2 | 1 |
| 7.11 | 4 | 3 | 1 | 2 | 1 | 0 |
| 7.12 | 3 | 3 | 0 | 0 | 2 | 1 |
| 7.13 | 2 | 2 | 0 | 0 | 2 | 0 |
| 7.14 | 3 | 3 | 0 | 1 | 1 | 1 |
| 7.15 | 4 | 4 | 0 | 1 | 2 | 1 |
| 7.15.1 | 2 | 2 | 0 | 0 | 2 | 0 |
| **TOTAL** | **21** | **20** | **1** | **4** | **12** | **4** |

**Note:** Items marked as **UNSURE** (e.g., supply chain node) should be discussed with the team to determine if they're needed.

### Phase 4B: Critical Data Issues & Re-validation 

**Target Release: 7.16 (Complete by late May 2026)**  
**Duration: 1 week (Late May)**

| Task | Owner | Duration | Target Date | Dependencies |
| --- | --- | --- | --- | --- |
| Triage and prioritize discrepancies | @Bhargava, Karan  | 1 day | Week 15 (Jun 2) | Phase 3 & 4A complete |
| Fix critical data issues (non-feature) | Hoover++ Team | 3 days | Week 15 (Jun 3-5) | Issue list finalized |
| Re-run validation for fixed issues | All Validators | 2 days | Week 15 (Jun 6-9) | Fixes deployed |
| Final validation report | @Bhargava, Karan  | 2 days | Week 16 (Jun 10-11) | Re-validation complete |

### Phase 5: Documentation & Handoff 

**Target Release: 7.16 (Complete by mid-June 2026)**  
**Duration: 1 week (Mid-June)**

| Task | Owner | Duration | Target Date | Dependencies |
| --- | --- | --- | --- | --- |
| Create validation summary wiki | @Bhargava, Karan  | 2 days | Week 16 (Jun 12-13) | All phases complete |
| Document known differences and workarounds | All Validations | 2 days | Week 16 (Jun 12-13) | Final report ready |
| Present findings to stakeholders | @Bhargava, Karan | 1 day | Week 17 (Jun 16) | Documentation complete |
| Handoff to downstream teams | @Bhargava, Karan | 2 days | Week 17 (Jun 17-18) | Presentation complete |

## **3. Validation Criteria**

### **3.1 Aggregated Data Validation**

**Count Validation:**

- Total row count match (within 0.01% tolerance)
- Row count by key dimensions (network\_id, event\_date, etc.)

**Metric Validation:**

- For **non-double fields**: Exact match required
- For **double fields**:
    - Absolute difference \< 0.01 (preferably \< 0.001)
    - Relative difference \< 0.1%
- Known logic differences: Document and exclude from validation

### **3.2 Event-Level Data Validation**

**Field-Level Comparison:**

- Compare key fields: transaction\_id, server\_id, timestamps
- Validate sampled flag consistency
- Check backwards-compatible view transformations

**Data Completeness:**

- Ensure all sampled records present in both models
- Identify Hoover-only or Hoover++-only records

## **4. Timeline**

```
Week 1-2:   ████████ Preparation & Setup
Week 3-6:   ████████████████ Aggregated Data Validation
Week 7-10:  ████████████████ Event-Level Data Validation
Week 11-14: ████████████ Issue Resolution & Re-validation
Week 15-16: ████████ Documentation & Handoff
```

**Total Duration**: 16 weeks (4 months)

## **5. Resource Allocation**

  

| Role | Responsibility | Time Commitment |
| --- | --- | --- |
| **Team Lead** | Overall coordination, setup, reporting | 50% (16 weeks) |
| **Validator 1** | L3 tables event-level validation | 100% (14 weeks) |
| **Validator 2** | L3 tables, event-level validation | 100% (14 weeks) |
| **Validator 3** | L3 Tables, event-level validation | 100% (14 weeks) |
| **Hoover++ Team** | Issue fixes, schema support | As needed |

## **6. Tools & Infrastructure**

### **6.1 Validation Environment**

- **Platform**: Databricks (PRD environment)
- **Data Source**: Sampled Hoover++ tables in `fw1_prd.hoover_pipeline_compaction.hoover_compaction`
- **Comparison Baseline**: Current Hoover L3 tables in `hive_data_prd_dwh_etl.aggregate.*`

### **6.2 Validation Tool Components**

- **Spark SQL** for query execution
- **DataFrame comparison** for row-level analysis
- **Git** for storing validation results

### **6.3 Monitoring & Reporting**

- **Validation Dashboard**: Track progress by table and phase
- **Issue Tracker**: JIRA tickets for discrepancies
- **Wiki Documentation**: Centralized validation results

## **7. Risk Mitigation**

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Sampled data not available for all tables | High | Enable sampling early (TVP-65116) |
| Validation queries too slow | Medium | Optimize queries, use partition pruning |
| Unknown schema differences | High | Review Hoover++ schema documentation early |
| Resource unavailability | Medium | Cross-train team members |
| Deadline pressure | High | Start early, prioritize critical tables |

## **8. Success Criteria**

✅ **All 5 L3 tables validated** with documented discrepancies  
✅ **Event-level validation complete** for key fields  
✅ **Critical issues resolved** and re-validated  
✅ **Validation report published** to wiki  
✅ **Stakeholder sign-off** obtained  
  

## **9. Key Contacts & References**

**Team Contacts:**

- Hoover++ Lead: @Wang, Yu 
- Validation Tool: Refer to validation tool wiki → <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191814598/Hoover+Validation+Tool+Tech+Design>
- Sampled Data: @Shankhdhar, Aman 

**Reference Documentation:**

- Hoover++ Execution Plan:  <https://freewheel.atlassian.net/wiki/spaces/~yuwang/pages/309628013/Execution+Plan+for+Hoover+UBT+2026+-+2027+WIP>
- Validation Framework: <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191814381/Hoover+Validation>
- Sampling Design: <https://freewheel.atlassian.net/wiki/spaces/DFV/pages/233105091/Pair+Sampling+Design+For+New+Hoover+Model>
- New Feature Catchup: <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191811160/New+Feature+Catch+Up+New+Model>

## **10. Next Steps**

1. **Week 1**: Kick-off meeting with team members
2. **Week 1**: Review validation tool wiki
3. **Week 1-2**: Set up Databricks environment and access
4. **Week 2**: Finalize validation SQL templates
5. **Week 3**: Begin Table 1 validation

  

### Questions?

@Bhargava, Karan 

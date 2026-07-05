# Hoover\+\+/UBT Weekly Updates

Please refer to  for Hoover++/UBT milestones and dates in 2026.

### Highlights:

- 1st version of H++(including UBT) data is made available on production for early access
- A new presto connector (for H++ and UBT) delta table is released onto production today by  's team ( ), which could allow a much easier access to H++/UBT data via LQS
- The initial version of Hoover pipeline monitoring dashboard is set up on STG for both pair and auction streams
- Risk still persists for H++/UBT development and validation due to the lack of resources. We may need more helps from CIEC team going forward in terms of those insights+ specific data capabilities and revisit/re-design works will be needed.

### Modeling

|  | Overall Status | Schema Review | Table Implementation | Unit/Regression Test | View Implementation | Cross-Validation | Documentation | Trainings | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++** | DELAYED | 100% | 75% | 75% | 10% | 5% | 0% | 0% | Allocated resource: 0  currently we don't have anyone working on Hoover++ models due to team resource constraints.  ,   |
| **UBT** | AT RISK | 90% | 60% | 60% | 20% | 10% | 0% | 0% | Allocated resource: 2schema review finished, all pending items (needs further discussion and research) are tracked at: .implementation:  240 out of 400 fieldsjust get started with the validation works and this is a bit slow than expected. This is because some distractions like: - Mani's paternity leave in March - Data restatement ( 2 new requests received from clients) - Biz feature development and discussion - Release planning |

  

---

### Pipeline

|  | Overall Status | Tech Design | Implementation | Performance Tuning | Integration Test | Monitoring/Alert | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++ Streaming** | ON TRACK | 100% | 80% | 60% | 60% | 70% | Allocated resource: 2 (including contractor)will give demo / update on below topics in the following weeks: 1. results of 2nd round of performance testing () 2. Hoover++ streaming monitoring dashboard |
| **Hoover++ Compaction** | ON TRACK | 70% | 35% | 0% | 0% | 0% | Allocated resource: 0.5 |
| **Post-bid IVT** | ON TRACK | 100% | 70% | 0% | 0% | 0% | Allocated resource: 0.5job orchestration part is done and started working on the pipeline build |
| **V4 logs** |  | 0% | 0% | 0% | 0% | 0% |  |
| **AF-DIP (forecasting)** |  | 0% | 0% | 0% | 0% | 0% |  |
| **SOS** | ON TRACK | 60% | 0% | 0% | 0% | 0% | Allocated resource: 0.5a full list of SOS rules are being reviewed at [here](https://freewheel.atlassian.net/wiki/display/DFV/%5BWIP%5D+Inventory+and+Classification+of+Existing+SOS+Rules) and the team is still working on the detailed tech design. |

### Modeling

|  | Overall Status | Schema Review | Table Implementation | Unit/Regression Test | View Implementation | Cross-Validation | Documentation | Trainings | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++** | DELAYED | 100% | 75% | 75% | 0% | 0% | 0% | 0% | Allocated resource: 0  currently we don't have anyone working on Hoover++ models due to team resource constraints.  ,   |
| **UBT** | AT RISK | 90% | 60% | 60% | 10% | 5% | 0% | 0% | Allocated resource: 2schema review finished, all pending items (needs further discussion and research) are tracked at: .implementation:  240 out of 400 fieldsjust get started with the validation works and this is a bit slow than expected. This is because some distractions like: - Mani's paternity leave in March - Data restatement ( 2 new requests received from clients) - Biz feature development and discussion - Release planning |

  

---

### Pipeline

|  | Overall Status | Tech Design | Implementation | Performance Tuning | Integration Test | Monitoring/Alert | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++ Streaming** | ON TRACK | 100% | 75% | 50% | 50% | 60% | Allocated resource: 2 (including contractor)will give demo / update on below topics in the following weeks: 1. results of 2nd round of performance testing () 2. Hoover++ streaming monitoring dashboard |
| **Hoover++ Compaction** | ON TRACK | 70% | 30% | 0% | 0% | 0% | Allocated resource: 0.5 |
| **Post-bid IVT** | ON TRACK | 100% | 70% | 0% | 0% | 0% | Allocated resource: 0.5job orchestration part is done and started working on the pipeline build |
| **V4 logs** |  | 0% | 0% | 0% | 0% | 0% |  |
| **AF-DIP (forecasting)** |  | 0% | 0% | 0% | 0% | 0% |  |
| **SOS** | ON TRACK | 50% | 0% | 0% | 0% | 0% | Allocated resource: 0.5a full list of SOS rules are being reviewed at [here](https://freewheel.atlassian.net/wiki/display/DFV/%5BWIP%5D+Inventory+and+Classification+of+Existing+SOS+Rules) and the team is still working on the detailed tech design. |

### Modeling

|  | Overall Status | Schema Review | Table Implementation | Unit/Regression Test | View Implementation | Cross-Validation | Documentation | Trainings | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++** | DELAYED | 100% | 75% | 75% | 0% | 0% | 0% | 0% | Allocated resource: 0  currently we don't have anyone working on Hoover++ models due to team resource constraints.  ,   |
| **UBT** | AT RISK | 90% | 60% | 60% | 0% | 0% | 0% | 0% | Allocated resource: 2schema review finished, all pending items (needs further discussion and research) are tracked at: .implementation:  240 out of 400 fieldsjust get started with the validation works and this is a bit slow than expected. This is because some distractions like: - Data restatement ( 2 new requests received from clients) - Biz feature development and discussion - Release planning |

  

---

### Pipeline

|  | Overall Status | Tech Design | Implementation | Performance Tuning | Integration Test | Monitoring/Alert | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++ Streaming** | ON TRACK | 100% | 75% | 40% | 40% | 40% | Allocated resource: 2.5 (including contractor)will give demo / update on below topics in the following weeks: 1. file publishing interface with downstream 2. result of 2nd round of streaming pipeline performance testing 3. streaming pipeline monitoring |
| **Hoover++ Compaction** |  | 70% | 25% | 0% | 0% | 0% | Allocated resource: 0 |
| **Post-bid IVT** | ON TRACK | 100% | 50% | 0% | 0% | 0% | Allocated resource: 0.5job orchestration part is done and started working on the pipeline build |
| **V4 logs** |  | 0% | 0% | 0% | 0% | 0% |  |
| **AF-DIP (forecasting)** |  | 0% | 0% | 0% | 0% | 0% |  |
| **SOS** | ON TRACK | 50% | 0% | 0% | 0% | 0% | Allocated resource: 0.5 a full list of SOS rules are being reviewed at [here](https://freewheel.atlassian.net/wiki/display/DFV/%5BWIP%5D+Inventory+and+Classification+of+Existing+SOS+Rules) and the team is still working on the detailed tech design. |

### Modeling

|  | Overall Status | Schema Review | Table Implementation | Unit/Regression Test | View Implementation | Cross-Validation | Documentation | Trainings | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++** | DELAYED | 100% | 75% | 75% | 0% | 0% | 0% | 0% | Allocated resource: 0  currently we don't have anyone working on Hoover++ models due to team resource constraints. Shall we consider handing over the build of cross-validation framework to other teams, so that we can at least have 0.5 engineer working on Hoover++ models. ,   |
| **UBT** | ON TRACK | 90% | 40% | 40% | 0% | 0% | 0% | 0% | Allocated resource: 2schema review: almost all of 400 fields(except the ones that under discussion)implementation: 163 out of 400 fields |

  

---

### Pipeline

|  | Overall Status | Tech Design | Implementation | Performance Tuning | Integration Test | Monitoring/Alert | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++ Streaming** | ON TRACK | 100% | 75% | 25% | 25% | 30% | Allocated resource: 2.5 (including contractor) |
| **Hoover++ Compaction** |  | 70% | 25% | 0% | 0% | 0% | Allocated resource: 0 |
| **Post-bid IVT** | ON TRACK | 100% | 50% | 0% | 0% | 0% | Allocated resource: 0.5 |
| **V4 logs** |  | 0% | 0% | 0% | 0% | 0% |  |
| **AF-DIP (forecasting)** |  | 0% | 0% | 0% | 0% | 0% |  |
| **SOS** | ON TRACK | 50% | 0% | 0% | 0% | 0% | Allocated resource: 0.5 |

### Modeling

|  | Overall Status | Schema Review | Table Implementation | Unit/Regression Test | View Implementation | Cross-Validation | Documentation | Trainings | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++** | DELAYED | 100% | 75% | 75% | 0% | 0% | 0% | 0% | Allocated resource: 0  currently we don't have anyone working on Hoover++ models due to team resource constraints. Shall we consider handing over the build of cross-validation framework to other teams, so that we can at least have 0.5 engineer working on Hoover++ models. ,   |
| **UBT** | ON TRACK | 75% | 37.5% | 37.5% | 0% | 0% | 0% | 0% | Allocated resource: 2schema review: 300 out of 400 fieldsimplementation: 150 out of 400 fields |

  

---

### Pipeline

|  | Overall Status | Tech Design | Implementation | Performance Tuning | Integration Test | Monitoring/Alert | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Hoover++ Streaming** | ON TRACK | 100% | 70% | 25% | 25% | 25% | Allocated resource: 2.5 (including contractor) |
| **Hoover++ Compaction** |  | 70% | 25% | 0% | 0% | 0% | Allocated resource: 0 |
| **Post-bid IVT** | ON TRACK | 100% | 50% | 0% | 0% | 0% | Allocated resource: 0.5 |
| **V4 logs** |  | 0% | 0% | 0% | 0% | 0% |  |
| **AF-DIP (forecasting)** |  | 0% | 0% | 0% | 0% | 0% |  |
| **SOS** | ON TRACK | 50% | 0% | 0% | 0% | 0% | Allocated resource: 0.5 |

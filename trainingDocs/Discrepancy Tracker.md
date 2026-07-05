# Discrepancy Tracker

Detailed Documentation: Hoover Validations Documentation Tracker

## Aggregated (L3 Tables):

|  | **Field Name** | **L3 Table Name** | **Expected?** | **Work/ Related PR** | **Status** |
| --- | --- | --- | --- | --- | --- |
| 1 | process\_batch\_id | ALL tables | YES | Since the split batching is different in old hoover vs new hoover++, the concept of `process_batch_id` is not equivalent. This dimension should be excluded. | IN PROGRESSevent\_hour exists in the compaction table. Similar concept but not the same. |
| 2 | traffic\_type | f\_process\_request\_hourlyf\_order\_selected\_hourly | Yes | If traffic\_type = 2 is missing, this is expected. Also attributed to the IVT Compaction pipeline.This dimension should be excluded.Reached out to  the diff comes from backend IVT, which is not consumed by the streaming pipeline, it will be used by the compaction pipeline. Also, considering the IVT detection algorithm, we can't compare the postbid IVT results by the sampled PRD data. It's a known issue. | IN PROGRESSIVT Compaction pipeline development in progress. |
| 3 | ivt\_indicator | f\_order\_selected\_hourly | Yes | Same as Traffic Typegenerated from traffic\_type | IN PROGRESSIVT Compaction pipeline development in progress. |
| 4 | bit\_flag: BIT\_FLAG\_NON\_MRC\_COMPLIANCE(11) | f\_order\_selected\_hourly | Yes | If enable IVT, rawReq.trafficCompliance.mrcComplianceFlag would be rewrite for COMPLIANCE\_FLAG\_INACTIVITY. | IN PROGRESSIVT Compaction pipeline development in progress. |
| 5 | bit\_flag: BIT\_FLAG\_HOUSEHOLD\_ID\_EXISTS (14) | f\_process\_request\_hourlyf\_order\_selected\_hourly | No | In hoover, we first **removeSensitiveData** and then set bit\_flags in **RequestHandler.setFields** In hoover++. we first set bit\_flags in **transactionCtx.setRequest **and then **setSensitiveDataFields**hoover++ set the flag when household\_id is null(househould\_is is removed due to privacy reasons)hoover does not set the flag when household\_id is removed. | IN PROGRESSTicket in PROGRESS. |
| 6 | bit\_flag:BIT\_FLAG\_FORECAST\_EXCLUDE(55) | ALL TABLES | Yes | Asset Chain and Site Section Chains bit flags are 0(by design)Request Table: [LQS](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260320220642_246867&externalid=20260320_220644_00536_iyf8z) Ack Table: [LQS](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260320220745_003106&externalid=20260320_220757_00540_iyf8z)Request Bit Flags missing sampled check<https://github.freewheel.tv/data/hoover-model/pull/262><https://github.freewheel.tv/data/hoover-model/pull/270>We sometimes do not set `1 << 55`  (forecast bit flag) because of the IVT pipeline. This causes differences between the 2 pipelines for bit flags.Definitely verify using the bit\_flag\_validator to decode the bits between control & stage | IN PROGRESSIVT Compaction Pipeline being developed |
| 7 | bit\_flag: BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED(57) | ALL TABLES | Yes | Not implemented in Hoover++<https://github.freewheel.tv/data/etl/pull/985> | IN PROGRESSPart of feature catchup. |
| 8 | airing\_id | f\_process\_request\_hourly | No | ID: 2 is missing which is INVALID\_ID\_WITHOUT\_TYPE<https://github.freewheel.tv/data/hoover-model/pull/262> | FIXED |
| 9 | client\_facing\_ivt\_reason\_flag | f\_process\_request\_hourly | Yes | There are certain flags that are not set yet and will be set by the IVT Compaction pipeline. One such flag value is: `1125899906842628` This dimension should be excluded.Reached out to  for the client facing `1 << 50`, it can come from prebid and postbid results, as I mentioned before, because no postbid ivt marked in the streaming pipeline, it's possible that we miss the value. | IN PROGRESSIVT Compaction pipeline development in progress. |
| 10 | slot\_ad\_unit\_ids | f\_process\_request\_hourly | No | Network ID check is inverted. Should be the other way around<https://github.freewheel.tv/data/hoover-model/pull/262> | FIXED |
| 11 | priority\_type | f\_order\_selected\_hourly | No | candidateInternalDealId is not unmask causing Programmatic prioirty\_type to be UNKNOWN. | <https://github.freewheel.tv/data/hoover-model/pull/320>Need to re-validate this after the code released.IN PROGRESS |
| 12 | postal\_code\_package\_id | f\_order\_selected\_hourly | No | Removing postal\_code\_package logic is not implemented in Hoover++ | IN PROGRESSTicket in progress. |
| 13 | bit\_flag\_aim\_product\_category(16) | f\_order\_selected\_hourly | Yes | Not implemented in Hoover++<https://github.freewheel.tv/data/etl/pull/985>  | LATERPart of feature catch-up |
| 14 | bit\_flag\_aim\_product\_category(32) | ALL TABLES | No | extra\_flags not in ad\_ctx.candidate.auction `if(partner.sales_channel = 4 and partner.supply_source != 4 and coalesce(auction.extra_flags, 0) & 4194304 > 0,     cast(32 as int), cast(0 as int)) ` | Part of feature catch-up |
| 15 | rendition\_id | f\_order\_sa\_delivered\_hourly |  | In hoover-etl pipeline, will unmask rendition id. But in hoover model,  export rendition id directly.Do we need to unmask it? `    public static final long fwMask = (1L << 48) - 1;      // unmask     public static long unmask(long id)     {         long unmasked = id & fwMask;         return (unmasked == fwMask) ? -1 : unmasked;     }` | LATERNeed to re-validate later |
| 16 | matched\_geo\_as\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | [ad\_ctx.ad](http://ad_ctx.ad).geo\_as\_audience\_segments\_id\_pks:  no such field in new hoover model. | LATER |
| 17 | matched\_include\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | network.audience\_partner\_segment\_infos:  no such field in new hoover model. | LATER |
| 18 | matched\_exclude\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | network.audience\_partner\_segment\_infos:  no such field in new hoover model. | LATER |
| 19 | priority\_type | f\_order\_sa\_delivered\_hourly | No | See above comment. | LATER |
| 20 | audience\_segment\_max\_cpm | f\_market\_delivered\_hourly | No | network.audience\_segment\_max\_cpm:  no such field in new hoover model. | LATER |
| 21 | avails\_event\_count |  | Yes | Pre-multiplied avails\_event\_count which contains ack.multiplier to new network structure. hence, avails\_event\_count can be removed from SQL wherever it is used for calculations. Found in f\_inventory\_sa\_delivered\_hourly and f\_inventory\_delivered\_hourly tables. | FIXED |

L3 (Aggregated) Tables

---

# Event Level (Backward Compatible Views)

| **#** | **Field Name** | **View Name** | **Expected?** | **Work/ Related PR** | **Status** |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
|  |  |  |  |  |  |

[https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views?atl\_f=PAGETREE](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views?atl_f=PAGETREE)

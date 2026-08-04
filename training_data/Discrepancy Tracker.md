# Discrepancy Tracker

Detailed Documentation: [Hoover Validations Documentation Tracker](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191887907/Hoover+Validations+Documentation+Tracker)

## Aggregated (L3 Tables):

|  | **Field Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | process\_batch\_id | YES | NO CHANGE PLANNED | Since the split batching is different in old hoover vs new hoover++, the concept of `process_batch_id` is not equivalent.  |
| 2 | traffic\_type | YES | IVT RELATED | Since postbid IVT is different between Hoover and Hoover++ pipeline, the traffic\_type differsTraffic\_type indicates IVT status (0: valid, 1: invalid-marked in prebid, 2: invalid-marked in postbid). The possible IVT diff comes from postbid ivt, because it is using different data between hoover and hoover++. So it means there may be some ivt traffic (traffic\_type=2) in the current hoover being marked as valid (traffic\_type=0) in Hoover++ or the other way round. |
| 3 | ivt\_indicator | YES | IVT RELATED | similar reason as above. Indicator is dependent on traffic\_type |
| 4 | client\_facing\_ivt\_reason\_flag | YES | IVT RELATED | similar reason as above. postbid IVT differences between Hoover \<\> Hoover++ |
| 5 | IVT BIT FLAGS`BIT_FLAG_NON_MRC_COMPLIANCE` | YES | IVT RELATED | similar reason as above. Bit flag is NOT set for some records correctly. |
| 6 | NORMAL BIT FLAGS`BIT_FLAG_FORECAST_EXCLUDE`(BIT 55) | NO | INVESTIGATION NEEDED | Sometimes the flag is NOT set in Hoover++ which we have not had TIME to check yet. Bit Flag is ONLY used by Forecasting (AF) team. |
| 7 | AIM related BIT FLAGS`BIT_FLAG_AIM_AUDIENCE_EXTENSION_USED``BIT_FLAG_AIM_PRODUCT_CATEGORY` (8, 16, 32 bits) | YES | AIM RELATED | AIM features have not been implemented in Hoover++ yet. Hence this is a KNOWN difference. |
| 8 | AIM related columns`MATCHED_GEO_AS_AUDIENCE_SEGMENT_IDS``MATCHED_INCLUDE_AUDIENCE_SEGMENT_IDS``MATCHED_EXCLUDE_AUDIENCE_SEGMENT_IDS``AUDIENCE_SEGMENT_MAX_CPM``AUDIENCE_SEGMENT_COST_USD` | YES | AIM RELATED | AIM features have not been implemented in Hoover++ yet. Hence this is a KNOWN difference. |
| 9 | avails\_event\_count | YES | NO CHANGE PLANNED | Hoover++ outputs the already multiplied avails metrics; hence DWH and other reporting products can take the value directly. |
| 10 | `*_in_played_slot` metrics | YES | NO CHANGE PLANNED | same as above |
| 11 | geo\_visibility | YES | NO CHANGE PLANNED | geo\_visibility is DEPRECATED |
| 12 | matched\_contextual\_segment\_ids | YES | NO CHANGE PLANNED | for f\_market\_selected\_hourly, the L3 table SQL is wrong. It selects from the advertisement record when it should be selecting from the ads\_in\_slot advertisement record. Hoover++ is correct here. |
| 13 | reseller\_network\_id | YES | NO CHANGE PLANNED | reseller\_network\_id is NOT present in inventory asset chain. This is because all values in Hoover are `null` and Hoover++ did not implement this. There is no need to implement `always null` fields. |
| 14 | metadata\_auditing\_flags | NO | INVESTIGATION NEEDED | Sometimes the metadata auditing flags are NOT set in Hoover++. This needs some further investigation as to why. |

For more detailed analysis please check each L3 table’s validation: [L3 (Aggregated) Tables](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605784711/L3+Aggregated+Tables)


|  | **Field Name** | **L3 Table Name** | **Expected?** | **Work/ Related PR** | **Status** |
| --- | --- | --- | --- | --- | --- |
| 1 | process\_batch\_id | ALL tables | YES | Since the split batching is different in old hoover vs new hoover++, the concept of `process_batch_id` is not equivalent. This dimension should be excluded. | DONEevent\_hour exists in the compaction table. Similar concept but not the same. |
| 2 | traffic\_type | f\_process\_request\_hourlyf\_order\_selected\_hourly | Yes | If traffic\_type = 2 is missing, this is expected. Also attributed to the IVT Compaction pipeline.This dimension should be excluded.Reached out to @Li, Ruonan the diff comes from backend IVT, which is not consumed by the streaming pipeline, it will be used by the compaction pipeline. Also, considering the IVT detection algorithm, we can't compare the postbid IVT results by the sampled PRD data. It's a known issue. | DONEPost bid IVT has been turned on for the compaction pipeline. |
| 3 | ivt\_indicator | f\_order\_selected\_hourly | Yes | Same as Traffic Typegenerated from traffic\_type | DONEPost bid IVT has been turned on for the compaction pipeline. |
| 4 | bit\_flag: BIT\_FLAG\_NON\_MRC\_COMPLIANCE(11) | f\_order\_selected\_hourly | Yes | If enable IVT, rawReq.trafficCompliance.mrcComplianceFlag would be rewrite for COMPLIANCE\_FLAG\_INACTIVITY. | DONEPost bid IVT has been turned on for the compaction pipeline. |
| 5 | bit\_flag: BIT\_FLAG\_HOUSEHOLD\_ID\_EXISTS (14) | f\_process\_request\_hourlyf\_order\_selected\_hourly | No | In hoover, we first **removeSensitiveData** and then set bit\_flags in **RequestHandler.setFields** In hoover++. we first set bit\_flags in **transactionCtx.setRequest **and then **setSensitiveDataFields**hoover++ set the flag when household\_id is null(househould\_is is removed due to privacy reasons)hoover does not set the flag when household\_id is removed. | DONEWe have a stripped proto and a non-stripped ivt proto in Hoover++ now. |
| 6 | bit\_flag:BIT\_FLAG\_FORECAST\_EXCLUDE(55) | ALL TABLES | Yes | Asset Chain and Site Section Chains bit flags are 0(by design)Request Table: [LQS](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260320220642_246867&externalid=20260320_220644_00536_iyf8z) Ack Table: [LQS](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260320220745_003106&externalid=20260320_220757_00540_iyf8z)Request Bit Flags missing sampled check<https://github.freewheel.tv/data/hoover-model/pull/262><https://github.freewheel.tv/data/hoover-model/pull/270>We sometimes do not set `1 << 55`  (forecast bit flag) because of the IVT pipeline. This causes differences between the 2 pipelines for bit flags.Definitely verify using the bit\_flag\_validator to decode the bits between control & stage | IN PROGRESSPost bid IVT has been turned on for the compaction pipeline.However, we still sometimes see an issue where BIT\_FLAG 55 is NOT set. Known diff for now (since only used by AF team but we will continue to figure this out) |
| 7 | bit\_flag: BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED(57) | ALL TABLES | Yes | Not implemented in Hoover++<https://github.freewheel.tv/data/etl/pull/985> | LATERAIM Feature; AIM integration not part of MVP |
| 8 | airing\_id | f\_process\_request\_hourly | No | ID: 2 is missing which is INVALID\_ID\_WITHOUT\_TYPE<https://github.freewheel.tv/data/hoover-model/pull/262> | FIXED |
| 9 | client\_facing\_ivt\_reason\_flag | f\_process\_request\_hourly | Yes | There are certain flags that are not set yet and will be set by the IVT Compaction pipeline. One such flag value is: `1125899906842628` This dimension should be excluded.Reached out to @Li, Ruonan for the client facing `1 << 50`, it can come from prebid and postbid results, as I mentioned before, because no postbid ivt marked in the streaming pipeline, it's possible that we miss the value. | DONEPost bid IVT has been turned on for the compaction pipeline. |
| 10 | slot\_ad\_unit\_ids | f\_process\_request\_hourly | No | Network ID check is inverted. Should be the other way around<https://github.freewheel.tv/data/hoover-model/pull/262> | FIXED |
| 11 | priority\_type | f\_order\_selected\_hourly | No | candidateInternalDealId is not unmask causing Programmatic prioirty\_type to be UNKNOWN. | <https://github.freewheel.tv/data/hoover-model/pull/320>Need to re-validate this after the code released.IN PROGRESS |
| 12 | postal\_code\_package\_id | f\_order\_selected\_hourly | No | Removing postal\_code\_package logic is not implemented in Hoover++ | DONE |
| 13 | bit\_flag\_aim\_product\_category(16) | f\_order\_selected\_hourly | Yes | Not implemented in Hoover++<https://github.freewheel.tv/data/etl/pull/985>  | LATERAIM Feature; AIM integration not part of MVP |
| 14 | bit\_flag\_aim\_product\_category(32) | ALL TABLES | No | extra\_flags not in ad\_ctx.candidate.auction `if(partner.sales_channel = 4 and partner.supply_source != 4 and coalesce(auction.extra_flags, 0) & 4194304 > 0,     cast(32 as int), cast(0 as int)) ` | AIM Feature; AIM integration not part of MVP |
| 15 | rendition\_id | f\_order\_sa\_delivered\_hourly |  | In hoover-etl pipeline, will unmask rendition id. But in hoover model,  export rendition id directly.Do we need to unmask it?  | DONEUnmasking was added; however a different issue for CPX events is being tracked separetely. |
| 16 | matched\_geo\_as\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | [ad\_ctx.ad](http://ad_ctx.ad).geo\_as\_audience\_segments\_id\_pks:  no such field in new hoover model. | LATERAIM Feature; AIM integration not part of MVP |
| 17 | matched\_include\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | network.audience\_partner\_segment\_infos:  no such field in new hoover model. | LATERAIM Feature; AIM integration not part of MVP |
| 18 | matched\_exclude\_audience\_segment\_ids | f\_order\_sa\_delivered\_hourly | No | network.audience\_partner\_segment\_infos:  no such field in new hoover model. | LATERAIM Feature; AIM integration not part of MVP |
| 19 | priority\_type | f\_order\_sa\_delivered\_hourly | No | See above comment. | ? |
| 20 | audience\_segment\_max\_cpm | f\_market\_delivered\_hourly | No | network.audience\_segment\_max\_cpm:  no such field in new hoover model. | LATERAIM Feature; AIM integration not part of MVP |
| 21 | avails\_event\_count |  | Yes | Pre-multiplied avails\_event\_count which contains ack.multiplier to new network structure. hence, avails\_event\_count can be removed from SQL wherever it is used for calculations. Found in f\_inventory\_sa\_delivered\_hourly and f\_inventory\_delivered\_hourly tables. | FIXED |

---

# Event Level (Backward Compatible Views)

|  | **Column Name** | **Expected** | **Table** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | request\_\_client\_facing\_reason\_code | IVT RELATED | ALL BCVs | Postbid ivt differences between Hoover \<\> Hoover++ |
| 2 | request\_\_mrc\_compliance\_label | IVT RELATED | ALL BCVs | Postbid ivt differences between Hoover \<\> Hoover++ |
| 3 | request\_\_traffic\_compliance\_\_mrc\_compliance\_flag | IVT RELATED | ALL BCVs | Postbid ivt differences between Hoover \<\> Hoover++ |
| 4 | request\_\_hashed\_key\_value | NO CHANGE PLANNED | ALL BCVs | Since privacyStripping is done in the beginning for Hoover++, the hashed key value is built on top of ALL kvs that are post GDPR/ CCPA privacy stripped. Since this field is mainly used by IVT this might be ok. |
| 5 | request\_\_bid\_request\_\_auction\_type | NO CHANGE PLANNED | ALL BCVs | Hoover++ is correct here; |
| 6 | geo\_visibility | NO CHANGE PLANNED | ALL BCVs | geo\_visibility is deprecated. |
| 7 | request\_\_flags | NO CHANGE PLANNED | ALL BCVs | `BIT_FLAG_PRIMARY_REQUEST` (1 \<\< 27) is NOT set in Hoover++. This flag is set by Matcher and since Hoover++ DOES NOT rely on matcher; this flag is not set. There is no downstream impact of this flag. |
| 8 | request\_\_bit\_flags | NEEDS FURTHER INVESTIGATION | All BCVs | Sometimes the bit\_flag `FORECAST_EXCLUDE`( 1 \<\< 55) is NOT set in Hoover++. This needs further investigation. |
| 9 | inventory\_\_site\_section\_chain\_\_tracked\_audience\_item\_ids | NEEDS FURTHER INVESTIGATION | Request | Needs further analysis as to why this is different between Hoover \<\> Hoover++ |
| 10 | audiences\_\_network\_id | NEEDS FURTHER INVESTIGATION | Request | Needs further analysis as to why this is different between Hoover \<\> Hoover++ |
| 11 | advertisement\_\_active\_aim\_audience\_idsadvertisement\_\_effective\_exclude\_aim\_audiencepartners\_\_audience\_partner\_segment\_infospartners\_\_audience\_segment\_max\_cpmpartners\_\_bit\_flags | AIM FEATURE | Ad | AIM features not implement in Hoover++. |
| 12 | candidate\_\_order\_id | NO | Ad | PR out to fix this already. Will be re-validated once released. |
| 13 | request\_\_ifa\_type | YES | Auction | Field requires RAW KV fields; and is not heavily used by downstream. Will be deprecated in Hoover++ |
| 14 | auction\_\_metadata\_auditing\_flags | NEEDS FURTHER INVESTIGATION | Auction | Needs to be investigated further as to why the metadata\_auditing\_flags are NOT set correctly in Hoover++ |
| 15 | partners\_\_avails\_category\_\_supply\_availspartners\_\_supply\_priority | NEEDS FURTHER INVESTIGATION | Slot | Needs to be investigated further. WIP by @Marino Johnson, Daniel |
| 16 |  |  |  |  |

[https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views?atl\_f=PAGETREE](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views?atl_f=PAGETREE)

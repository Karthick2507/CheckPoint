# f\_order\_selected\_hourly

# Results


**⚠️ \[STG\] VALIDATION FAILED - f\_order\_selected\_hourly**  
**Environment:** STG  |  **Date:** 2026-04-14  |  **Hour:** 16  
**Control table:** `fw1_stg.xkbai.f_order_selected_hourly_hive`  
**Stage table:** `fw1_stg.xkbai.f_order_selected_hourly_hoover_plus`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values
- Dimensions analyzed: 186 — differences found
- Metrics analyzed: 37 — ✓ pass
- Row count: Control 306,881 / Stage 306,881 — ✓ match
- Row hash diffs: 0 — ✓ match


---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*  

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **traffic\_type** \[EXPECTED\] | 2 | 0 | 2 | 0 |
| **bit\_flag** | 496 | 414 | 86 | 4 |
| **geo\_visibility** \[EXPECTED\] | 1 | 0 | 1 | 0 |
| **postal\_code\_package\_ids** (some values expected) | 11789 | 11794 | 0 | 5 |
| **ivt\_indicator** \[EXPECTED\] | 2 | 0 | 2 | 0 |
| **priority\_type** \[EXPECTED\] | 23 | 18 | 5 | 0 |
| **bit\_flag\_aim\_product\_category** \[EXPECTED\] | 6 | 7 | 2 | 3 |
| **process\_batch\_id** \[EXPECTED\] | 2 | 2 | 1 | 1 |



**Sample Values (first 5 dimensions with differences):**

**bit\_flag:**  
*Only in CONTROL (86 total):* 612559918071023616, 630574350940243968, 594546103672899584, 738665140073023520, 738942491847559168, 612560502192865280, 612559918066829312, 612490099080560640, 612562117090084864, 612564350473078784 ... (+ 76 more, see CSV)  
*Only in STAGE (4 total):* 576535519094376704, 594549952001361952, 576531121047865600, 576535519094376736

**postal\_code\_package\_ids:**  
*Only in STAGE (5 total):* \[ 1993 10801 10804 11157 11210 11221 11732\], \[ 1993 10801 10805 11148 11210 11732 12696\], \[ 1993 10801 11210 11532 11547 11734\], \[ 4195 9622 9623 10386 10451 10452 10580 11079 11186 11320 11379 11386 11394 11414 11415 11416 11477 11486 11550 11662 11733 11858 11876 12151 12280 12488 12684 12687 12688 12698 12699 12701 12702\], \[ 1993 10801 10806 11155 11210 11543\]

---

**📊 METRIC SUM DIFFERENCES**  

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **upstream\_bidding\_revenue\_in\_played\_slot** \[EXCLUDED — known diff\] | Not compared (acknowledged known difference) |  |  |  |



**✓ All row counts and hashes match!**

---

**📎 ATTACHMENTS:**  

1. **row\_differences.csv**: Complete row-level differences (up to 1000 rows each direction)
2. **dimension\_value\_differences.csv**: All actual different values for each dimension
3. **manual\_analysis.sql**: Additional SQL queries for deeper investigation

# Issues

| **Column** | **Expected?** | **Fixed?** | **Root Cause** |
| --- | --- | --- | --- |
| process\_batch\_id |   | - |  |
| traffic\_type |   |  | IVT |
| geo\_visibility |   | - | [geo\_visibility is DEPRECATED](https://github.freewheel.tv/kbharg432/hoover_plus_sqls/blob/main/L3%20SQL%20Conversions/Event%20Table/f_order_selected_hourly_h%2B%2B.sql#L22) |
| ivt\_indicator |   |  | IVT |
| postal\_code\_package\_ids |   |  | [postal\_code\_package is removed by GDPRHelper](https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/helper/GDPRHelper.java#L111)Removing postal\_code\_package logic is not implemented in Hoover++ |
| priority\_type |   | <https://github.freewheel.tv/data/hoover-model/pull/320> | candidateInternalDealId is not unmask |
| bit\_flag: BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED(57) |   |  | aim features are not implemented in hoover++ |
| bit\_flag:BIT\_FLAG\_FORECAST\_EXCLUDE(55) |   |  | IVT |
| bit\_flag: BIT\_FLAG\_HOUSEHOLD\_ID\_EXISTS (14) |   |  | In hoover, we first **removeSensitiveData** and then set bit\_flags in **RequestHandler.setFields** In hoover++. we first set bit\_flags in **transactionCtx.setRequest **and then **setSensitiveDataFields**hoover++ set the flag when household\_id is null(househould\_is is removed due to privacy reasons)hoover does not set the flag when household\_id is removed. |
| bit\_flag: BIT\_FLAG\_NON\_MRC\_COMPLIANCE(11) |   |  | IVT |
| bit\_flag\_aim\_product\_category(1) |   | - | Hoover use advertisement\_\_is\_rbpHoover++ use ads\_in\_slot\_\_advertisement\_\_is\_rbpIt seems hoover++ is correct. to fix L3 table |
| bit\_flag\_aim\_product\_category(8) |   | - | Hoover: use advertisement\_\_bit\_flags Hoover++: use ads\_in\_slot\_\_advertisement\_\_bit\_flagsIt seems hoover++ is correct. to fix L3 table |
| bit\_flag\_aim\_product\_category(16) |   |  | use partner.bit\_flags BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED(57)aim features not implemented in hoover++ |
| bit\_flag\_aim\_product\_category(32) |   |  | extra\_flags not in ad\_ctx.candidate.auction, can't add this value to hoover++ |
| upstream\_bidding\_revenue\_in\_played\_slot |   |  | no such field in Hoover++ |
| decision\_type |  |  <https://github.freewheel.tv/data/hoover-model/pull/315> | UDF`cal_decision_type miss supplySource == 1` |




# Validations

## Round 1

| **Dimension** | **Control Total** | **Stage Total** | **Only in Control** | **Only in Stage** | **Status** | **Root Cause** |
| --- | --- | --- | --- | --- | --- | --- |
| process\_batch\_id | 2 | 1 | 1 | 0 | `Expected` | `process_batch_id` differences can be attributed to how the batch splitting differs between matcher and hoover++ streaming. We should ignore this dimension |
| tv\_network\_id | 191 | 206 | 1 | 16 | Resolved | *~~Only in CONTROL (1 total):~~*~~ 748~~ Caused by for hoover\_plus, the event\_hour can be 20260414150000 when the ack\_\_timestamp is '2026-04-14 16:00:00'`select count(1) from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414160000'             AND event_hour < '20260414180000'             and request.context.tv_network_id = 748 result: 1``select request.transaction_id, slot_ack_ctx.ack.timestamp, slot_ack_ctx.ack.slot_id, slot_ack_ctx.ack.event_name, slot_ack_ctx.metrics.slot_impression, slot_ack_ctx.metrics.fire_event_slot_revenue_ratio, ad_ctx.ad.is_bumper, partner.network_is_extra_item_owner, partner.network_is_ad_owner, ad_ctx.ad.is_embedded_tracking from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414160000'             AND event_hour < '20260414180000'             and request.context.tv_network_id = 748  `It is slotEnd not slotImpression.In hoover, there's slotImpression[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260416200657\_057159&externalid=20260416\_200701\_00003\_6as4n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260416200657_057159&externalid=20260416_200701_00003_6as4n)Expand the event\_hour to 20260414150000, we can find the slotImpression. |

## Round 2

Load event\_hour = 20260414150000 into stage table.


| **Dimension** | **Control Total** | **Stage Total** | **Only in Control** | **Only in Stage** | **Status** | **Root Cause** |
| --- | --- | --- | --- | --- | --- | --- |
| ad\_id | 19488 | 19489 | 0 | 1 | Resolved | `select * from fw1_stg.xkbai.f_order_selected_hourly_hive where ad_id = 92782874; return 0 rows.``select * from fw1_stg.xkbai.f_order_selected_hourly_hoover_plus where ad_id = 92782874; return 1 rows.``select * from hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly_sampling where event_date = TIMESTAMP('2026-04-14 16:00:00') and ad_id = 92782874 return 0 rows``select request.transaction_id, slot_ack_ctx.ack.timestamp, slot_ack_ctx.ack.event_name, slot_ack_ctx.ack.slot_id, slot_ack_ctx.ack.flags, slot_ack_ctx.metrics.slot_impression, slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and ad_ctx.ad.ad_id = 92782874; returns 1 row   `transaction\_idtimestampevent\_nameslot\_idflagsslot\_impressionfire\_event\_slot\_revenue\_ratio17761858868060616471776185890slotImpression0`4194561`11In LQS, the slot\_impression is 0[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260417201849\_633305](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260417201849_633305)The flags include FILTERED(256)Based on Entity - SlotCtx#SlotAckMetricshoover plus plus slot\_impression not check FILTERED flag. |
| transaction\_id | timestamp | event\_name | slot\_id | flags | slot\_impression | fire\_event\_slot\_revenue\_ratio |
| 1776185886806061647 | 1776185890 | slotImpression | 0 | `4194561` | 1 | 1 |

## Round 3

add ack.flags filter when load stage table

```
  and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0
```


| **Dimension** | **Control Total** | **Stage Total** | **Only in Control** | **Only in Stage** | **Status** | **Root Cause** |
| --- | --- | --- | --- | --- | --- | --- |
| **traffic\_type**  | 2 | 0 | 2 | 0 | Expected | the diff comes from backend IVT, which is not consumed by the streaming pipeline, it will be used by the compaction pipeline. Also, considering the IVT detection algorithm, we can't compare the postbid IVT results by the sampled PRD data. It's a known issue. |
| **bit\_flag** | 496 | 414 | 86 | 4 |  | `with b as ( select bit_flag, sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hoover_plus group by 1 order by 1),  a as (  select bit_flag, sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hive group by 1 order by 1 ),  diff_result AS (   SELECT     a.bit_flag AS control_bit_flag,     b.bit_flag AS stage_bit_flag,     COALESCE(a.sum, 0) AS control_sum,     COALESCE(b.sum, 0) AS stage_sum   FROM a   FULL OUTER JOIN b     ON a.bit_flag = b.bit_flag   WHERE     a.bit_flag IS NULL     OR b.bit_flag IS NULL     OR COALESCE(a.sum, 0) <> COALESCE(b.sum, 0) ),  control_bits AS (   SELECT     bit_pos,     SUM(control_sum) AS control_sum   FROM diff_result   LATERAL VIEW explode(sequence(0, 62)) b AS bit_pos   WHERE control_bit_flag IS NOT NULL     AND ((control_bit_flag >> bit_pos) & 1) = 1   GROUP BY bit_pos ),  stage_bits AS (   SELECT     bit_pos,     SUM(stage_sum) AS stage_sum   FROM diff_result   LATERAL VIEW explode(sequence(0, 62)) b AS bit_pos   WHERE stage_bit_flag IS NOT NULL     AND ((stage_bit_flag >> bit_pos) & 1) = 1   GROUP BY bit_pos )  SELECT   COALESCE(c.bit_pos, s.bit_pos) AS bit_pos,   COALESCE(c.control_sum, 0) AS control_sum,   COALESCE(s.stage_sum, 0) AS stage_sum,   COALESCE(c.control_sum, 0) - COALESCE(s.stage_sum, 0) AS diff_sum FROM control_bits c FULL OUTER JOIN stage_bits s   ON c.bit_pos = s.bit_pos WHERE COALESCE(c.control_sum, 0) <> COALESCE(s.stage_sum, 0) ORDER BY ABS(diff_sum) DESC;`bit\_posnamecontrol\_sumstage\_sumdiff\_sumStatusdetail55BIT\_FLAG\_FORECAST\_EXCLUDE988567603125Expectedrequest.bit\_flagsSometimes the `isForecastExclude` flag is not set. This is because the FILTERED  flag is not set because the IVT Compaction pipeline has not run. 57BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED120801208Expectedpartner.bit\_flagsnot implemented in hoover++<https://github.freewheel.tv/data/etl/pull/985>14BIT\_FLAG\_HOUSEHOLD\_ID\_EXISTS2932329401-78 **ISSUE** request.bit\_flagshoover++ set the flag when  household\_id is null`select visitor.household_id is null, visitor.household_id = "", sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) *            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads -- request.transaction_id, -- slot_ack_ctx.ack.timestamp, -- slot_ack_ctx.ack.event_name, -- slot_ack_ctx.ack.slot_id, -- slot_ack_ctx.ack.flags, -- partner.network_id, -- partner.postal_code_package_ids, -- slot_ack_ctx.metrics.slot_impression, -- slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and (ad_ctx.ad.is_embedded_tracking = false    or (ad_ctx.ad.is_embedded_tracking   and (partner.network_is_ad_owner    or partner.network_is_extra_item_owner)))   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and request.bit_flags & shiftleft(CAST(1 AS BIGINT), 14) > 0   --  and visitor.household_id is null   group by 1,2` (visitor.household\_id IS NULL)(visitor.household\_id = "")selected\_primary\_adsFALSEFALSE43689TRUEnull78 `select request.transaction_id, sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) *            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads -- request.transaction_id, -- slot_ack_ctx.ack.timestamp, -- slot_ack_ctx.ack.event_name, -- slot_ack_ctx.ack.slot_id, -- slot_ack_ctx.ack.flags, -- partner.network_id, -- partner.postal_code_package_ids, -- slot_ack_ctx.metrics.slot_impression, -- slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and (ad_ctx.ad.is_embedded_tracking = false    or (ad_ctx.ad.is_embedded_tracking   and (partner.network_is_ad_owner    or partner.network_is_extra_item_owner)))   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and request.bit_flags & shiftleft(CAST(1 AS BIGINT), 14) > 0    and visitor.household_id is null   group by 1`No such case in hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260424180054\_021535&externalid=20260424\_180058\_00241\_ypz9x](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260424180054_021535&externalid=20260424_180058_00241_ypz9x)11BIT\_FLAG\_NON\_MRC\_COMPLIANCE24057524052352 **ISSUE**ad.bit\_flagsrequest\_\_mrc\_compliance\_label and request\_\_traffic\_compliance\_\_mrc\_compliance\_flag are null in hoover++ but not null in hoover. use this query to find one transaction`with b as (select deal_id as dimension,  sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hoover_plus where bit_flag & shiftleft(CAST(1 AS BIGINT), 11)  = 0 group by 1 ), a as (  select deal_id as dimension, sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hive where bit_flag & shiftleft(CAST(1 AS BIGINT), 11)  = 0 group by 1  )    SELECT     a.dimension AS control_dimension,     b.dimension AS stage_dimension,     COALESCE(a.sum, 0) AS control_sum,     COALESCE(b.sum, 0) AS stage_sum   FROM a   FULL OUTER JOIN b     ON a.dimension = b.dimension   WHERE     a.dimension IS NULL     OR b.dimension IS NULL     OR COALESCE(a.sum, 0) <> COALESCE(b.sum, 0)   `select deal\_id = 582951 `select request.transaction_id, coalesce(request.traffic_compliance.mrc_compliance_flag, 0) <= 0 and array_contains(request.mrc_compliance_label, "NOT_EXPLICIT_RENDERED") as c1,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) > 0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) = -1 or coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 2 > 0 as c2,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) > 0 and coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 1 >  0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) & 1 > 0 and slot_ctx.slot.time_position_class in ("preroll", "midroll", "postroll", "pause_midroll", "overlay") as c3,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 1 >  0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) & 2 > 0 and slot_ctx.slot.time_position_class in ("display", "in-player-display") as c4,  request.traffic_compliance.mrc_compliance_flag, request.mrc_compliance_label, request.traffic_compliance.mrc_non_compliance_type,  slot_ctx.slot.time_position_class  -- sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) * --            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' -- and (ad_ctx.ad.is_embedded_tracking = false --    or (ad_ctx.ad.is_embedded_tracking --   and (partner.network_is_ad_owner --    or partner.network_is_extra_item_owner))) --   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and ad_ctx.ad.bit_flags & shiftleft(CAST(1 AS BIGINT), 11) = 0    and if(partner.deal_awareability, coalesce(ad_ctx.candidate.internal_deal_id, cast(-1 as long)),           cast(-1 as long))    in (582951) --    and partner.network_id in (394492, -- 177562, -- 512166, -- 520177, -- 144750, -- 385316, -- 512167, -- 174057, -- 520311)   -- group by 1   -- order by 1`transaction\_id = '1776182099289346973'[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260421194948\_821617&externalid=20260421\_194953\_00117\_59kx3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260421194948_821617&externalid=20260421_194953_00117_59kx3)label and flag not samefieldhooverhoover++request\_\_mrc\_compliance\_label`[OTT_CONTINUOUS_PLAY]`nullrequest\_\_traffic\_compliance\_\_mrc\_compliance\_flag`2`0request\_\_mrc\_compliance\_label and request\_\_traffic\_compliance\_\_mrc\_compliance\_flag are null in hoover++ but not null in hoover.Hoover will set isInactivityTraffic flag. <https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/common/HooverConstants.java#L178C1-L179C1> |
| bit\_pos | name | control\_sum | stage\_sum | diff\_sum | Status | detail |
| 55 | BIT\_FLAG\_FORECAST\_EXCLUDE | 9885 | 6760 | 3125 | Expected | request.bit\_flagsSometimes the `isForecastExclude` flag is not set. This is because the FILTERED  flag is not set because the IVT Compaction pipeline has not run. |
| 57 | BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED | 1208 | 0 | 1208 | Expected | partner.bit\_flagsnot implemented in hoover++<https://github.freewheel.tv/data/etl/pull/985> |
| 14 | BIT\_FLAG\_HOUSEHOLD\_ID\_EXISTS | 29323 | 29401 | -78 |  **ISSUE** | request.bit\_flagshoover++ set the flag when  household\_id is null`select visitor.household_id is null, visitor.household_id = "", sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) *            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads -- request.transaction_id, -- slot_ack_ctx.ack.timestamp, -- slot_ack_ctx.ack.event_name, -- slot_ack_ctx.ack.slot_id, -- slot_ack_ctx.ack.flags, -- partner.network_id, -- partner.postal_code_package_ids, -- slot_ack_ctx.metrics.slot_impression, -- slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and (ad_ctx.ad.is_embedded_tracking = false    or (ad_ctx.ad.is_embedded_tracking   and (partner.network_is_ad_owner    or partner.network_is_extra_item_owner)))   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and request.bit_flags & shiftleft(CAST(1 AS BIGINT), 14) > 0   --  and visitor.household_id is null   group by 1,2` (visitor.household\_id IS NULL)(visitor.household\_id = "")selected\_primary\_adsFALSEFALSE43689TRUEnull78 `select request.transaction_id, sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) *            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads -- request.transaction_id, -- slot_ack_ctx.ack.timestamp, -- slot_ack_ctx.ack.event_name, -- slot_ack_ctx.ack.slot_id, -- slot_ack_ctx.ack.flags, -- partner.network_id, -- partner.postal_code_package_ids, -- slot_ack_ctx.metrics.slot_impression, -- slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and (ad_ctx.ad.is_embedded_tracking = false    or (ad_ctx.ad.is_embedded_tracking   and (partner.network_is_ad_owner    or partner.network_is_extra_item_owner)))   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and request.bit_flags & shiftleft(CAST(1 AS BIGINT), 14) > 0    and visitor.household_id is null   group by 1`No such case in hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260424180054\_021535&externalid=20260424\_180058\_00241\_ypz9x](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260424180054_021535&externalid=20260424_180058_00241_ypz9x) |
| (visitor.household\_id IS NULL) | (visitor.household\_id = "") | selected\_primary\_ads |  |  |  |  |
| FALSE | FALSE | 43689 |  |  |  |  |
| TRUE | null | 78 |  |  |  |  |
| 11 | BIT\_FLAG\_NON\_MRC\_COMPLIANCE | 240575 | 240523 | 52 |  **ISSUE** | ad.bit\_flagsrequest\_\_mrc\_compliance\_label and request\_\_traffic\_compliance\_\_mrc\_compliance\_flag are null in hoover++ but not null in hoover. use this query to find one transaction`with b as (select deal_id as dimension,  sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hoover_plus where bit_flag & shiftleft(CAST(1 AS BIGINT), 11)  = 0 group by 1 ), a as (  select deal_id as dimension, sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hive where bit_flag & shiftleft(CAST(1 AS BIGINT), 11)  = 0 group by 1  )    SELECT     a.dimension AS control_dimension,     b.dimension AS stage_dimension,     COALESCE(a.sum, 0) AS control_sum,     COALESCE(b.sum, 0) AS stage_sum   FROM a   FULL OUTER JOIN b     ON a.dimension = b.dimension   WHERE     a.dimension IS NULL     OR b.dimension IS NULL     OR COALESCE(a.sum, 0) <> COALESCE(b.sum, 0)   `select deal\_id = 582951 `select request.transaction_id, coalesce(request.traffic_compliance.mrc_compliance_flag, 0) <= 0 and array_contains(request.mrc_compliance_label, "NOT_EXPLICIT_RENDERED") as c1,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) > 0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) = -1 or coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 2 > 0 as c2,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) > 0 and coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 1 >  0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) & 1 > 0 and slot_ctx.slot.time_position_class in ("preroll", "midroll", "postroll", "pause_midroll", "overlay") as c3,  coalesce(request.traffic_compliance.mrc_compliance_flag, 0) & 1 >  0 and coalesce(request.traffic_compliance.mrc_non_compliance_type, -1) & 2 > 0 and slot_ctx.slot.time_position_class in ("display", "in-player-display") as c4,  request.traffic_compliance.mrc_compliance_flag, request.mrc_compliance_label, request.traffic_compliance.mrc_non_compliance_type,  slot_ctx.slot.time_position_class  -- sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) * --            coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' -- and (ad_ctx.ad.is_embedded_tracking = false --    or (ad_ctx.ad.is_embedded_tracking --   and (partner.network_is_ad_owner --    or partner.network_is_extra_item_owner))) --   and ad_ctx.ad.is_bumper = false   and (coalesce (slot_ack_ctx.metrics.slot_impression     , cast (0 as long)) != 0    or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio     , cast (0 as int)) != 0)   and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0    and ad_ctx.ad.bit_flags & shiftleft(CAST(1 AS BIGINT), 11) = 0    and if(partner.deal_awareability, coalesce(ad_ctx.candidate.internal_deal_id, cast(-1 as long)),           cast(-1 as long))    in (582951) --    and partner.network_id in (394492, -- 177562, -- 512166, -- 520177, -- 144750, -- 385316, -- 512167, -- 174057, -- 520311)   -- group by 1   -- order by 1`transaction\_id = '1776182099289346973'[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260421194948\_821617&externalid=20260421\_194953\_00117\_59kx3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260421194948_821617&externalid=20260421_194953_00117_59kx3)label and flag not samefieldhooverhoover++request\_\_mrc\_compliance\_label`[OTT_CONTINUOUS_PLAY]`nullrequest\_\_traffic\_compliance\_\_mrc\_compliance\_flag`2`0request\_\_mrc\_compliance\_label and request\_\_traffic\_compliance\_\_mrc\_compliance\_flag are null in hoover++ but not null in hoover.Hoover will set isInactivityTraffic flag. |
| field | hoover | hoover++ |  |  |  |  |
| request\_\_mrc\_compliance\_label | `[OTT_CONTINUOUS_PLAY]` | null |  |  |  |  |
| request\_\_traffic\_compliance\_\_mrc\_compliance\_flag | `2` | 0 |  |  |  |  |
| **geo\_visibility** | 1 | 0 | 1 | 0 | Expected  | [geo\_visibility is DEPRECATED](https://github.freewheel.tv/kbharg432/hoover_plus_sqls/blob/main/L3%20SQL%20Conversions/Event%20Table/f_order_selected_hourly_h%2B%2B.sql#L22) |
| **postal\_code\_package\_ids** | 11789 | 11794 | 0 | 5 |  | visitor\_\_postal\_code\_package\_\_postal\_code\_package\_id is null in Hoover, but not null in hoover++Find transaction\_id in hoover++`select request.transaction_id, slot_ack_ctx.ack.timestamp, slot_ack_ctx.ack.event_name, slot_ack_ctx.ack.slot_id, slot_ack_ctx.ack.flags, partner.network_id, partner.postal_code_package_ids, slot_ack_ctx.metrics.slot_impression, slot_ack_ctx.metrics.fire_event_slot_revenue_ratio from fw1_prd.hoover_pipeline_compaction.hoover_compaction          lateral view explode(slot_ctxes) as slot_ctx          lateral view explode(slot_ctx.ad_ctxes) as ad_ctx          lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx           lateral view explode(ad_ctx.networks) as partner where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00')             AND event_hour >= '20260414150000'             AND event_hour < '20260414170000' and partner.postal_code_package_ids in (   ARRAY(4195, 9622, 9623, 10386, 10451, 10452, 10580, 11079, 11186, 11320, 11379, 11386,       11394, 11414, 11415, 11416, 11477, 11486, 11550, 11662, 11733, 11858, 11876, 12151,       12280, 12488, 12684, 12687, 12688, 12698, 12699, 12701, 12702),  ARRAY(1993, 10801, 10806, 11155, 11210, 11543),  ARRAY(1993, 10801, 10804, 11157, 11210, 11221, 11732),  ARRAY(1993, 10801, 10805, 11148, 11210, 11732, 12696),  ARRAY(1993, 10801, 11210, 11532, 11547, 11734) );   `[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260421201222\_259883&externalid=20260421\_201403\_00002\_9jqsm](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260421201222_259883&externalid=20260421_201403_00002_9jqsm) |
| **ivt\_indicator** | 2 | 0 | 2 | 0 | Expected | same as traffic\_typethe diff comes from backend IVT, which is not consumed by the streaming pipeline, it will be used by the compaction pipeline. Also, considering the IVT detection algorithm, we can't compare the postbid IVT results by the sampled PRD data. It's a known issue. |
| **priority\_type** | 23 | 18 | 5 | 0 |  | When sales\_channel is PROGRAMMATIC, priority\_type is UNKNOWNcandidateInternalDealId is not unmask`if (candidateInternalDealId > 0) {     switch (candidateDealType) {         case HooverConstants.PROGRAMMATIC_GUARANTEED_TRADING_DESK_DEAL:             priorityType = HooverConstants.PROGRAMMATIC_GUARANTEED;             break;         case HooverConstants.BIDDABLE_GUARANTEED_DEAL:             priorityType = HooverConstants.BIDDABLE_GUARANTEED;             break;         case HooverConstants.FIRST_LOOK_DEAL:             priorityType = HooverConstants.FIRST_LOOK;             break;         default:             priorityType = candidateDealType;             break;     } } else {     if (Objects.equals(partnerRuleTypePriority, HooverConstants.ME_FIRST)) {         priorityType = HooverConstants.BACKFILL_ONLY;     } else {         priorityType = partnerRuleTypePriority;     } }`Only internal\_deal\_id in ad\_ctx.candidate but no deal\_type in ad\_ctx.candidate Find transaction id [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260421203238\_736964&externalid=20260421\_204002\_00140\_ee9mh](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260421203238_736964&externalid=20260421_204002_00140_ee9mh)andrequest.transaction\_idin ('1776181753693174087');[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260423\_155228\_00023\_wz9ek](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260423_155228_00023_wz9ek)priority\_type is PROGRAMMATIC\_GUARANTEED in hoover but is Unknown in hoover++ hooverhoover++network\_id 191701191701roleCROCROsales\_channel44supply\_source11**priority\_type****PROGRAMMATIC\_GUARANTEED****Unknown**internal\_deal\_id612244612244deal\_typePROGRAMMATIC\_GUARANTEED\_TRADING\_DESK\_DEALPROGRAMMATIC\_GUARANTEED\_TRADING\_DESK\_DEALFind the transaction in hoover++ table`select partner.network_id, partner.role, partner.priority_type, partner.sales_channel, partner.supply_source, request.transaction_id, slot_ack_ctx.ack.timestamp, slot_ack_ctx.ack.event_name, slot_ack_ctx.ack.slot_id, slot_ack_ctx.ack.flags, slot_ack_ctx.metrics.slot_impression, ad_ctx.candidate.internal_deal_id, candidate_ctx.candidate.deal_type from fw1_prd.hoover_pipeline_compaction.hoover_compaction lateral view explode(slot_ctxes) as slot_ctx lateral view explode(slot_ctx.ad_ctxes) as ad_ctx lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx lateral view explode(ad_ctx.networks) as partner lateral view explode(candidate_ctxes) as candidate_ctx where date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-14 16:00:00') AND event_hour >= '20260414150000' AND event_hour < '20260414170000' and candidate_ctx.candidate.internal_deal_id = ad_ctx.candidate.internal_deal_id and request.transaction_id in ( '1776181753693174087' -- , '1776184723584657439' ) and slot_ack_ctx.ack.slot_id = 20 -- and ( -- (slot_ack_ctx.ack.slot_id = 0 and partner.network_id in (512166,528776,530362) and ad_ctx.candidate.internal_deal_id in (233266, 550603)) or  -- (slot_ack_ctx.ack.slot_id = 20 and partner.network_id in (191701,505334,512167) and ad_ctx.candidate.internal_deal_id = 612244 ) -- )  ` |
|  | hoover | hoover++ |  |  |  |  |
| network\_id  | 191701 | 191701 |  |  |  |  |
| role | CRO | CRO |  |  |  |  |
| sales\_channel | 4 | 4 |  |  |  |  |
| supply\_source | 1 | 1 |  |  |  |  |
| **priority\_type** | **PROGRAMMATIC\_GUARANTEED** | **Unknown** |  |  |  |  |
| internal\_deal\_id | 612244 | 612244 |  |  |  |  |
| deal\_type | PROGRAMMATIC\_GUARANTEED\_TRADING\_DESK\_DEAL | PROGRAMMATIC\_GUARANTEED\_TRADING\_DESK\_DEAL |  |  |  |  |
| **bit\_flag\_aim\_product\_category** | 6 | 7 | 2 | 3 |  | logic change`         + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int), cast(0 as int))          + if(partner.sales_channel = 4 and partner.supply_source != 4 and coalesce(auction.extra_flags, 0) & 4194304 > 0,              cast(32 as int), cast(0 as int))                                                                                        as bit_flag_aim_product_category`extra\_flags not in ad\_ctx.candidate.auction can't add 32 to hoover++<https://github.freewheel.tv/data/transformer/commit/08514f6f4916ddecb3db1471ba3ed7cafe41384b#diff-f7d4c774797400b4c879c27592f85a25d6ed259b5eec6f17beb6a00ab69d772e>bitvaluecontrol\_sumstage\_sumdiff\_sumExpectedReason01` if(partner.network_is_ad_owner and !advertisement.is_bumper and !advertisement.is_external and advertisement.is_rbp, cast(1 as int), cast(0 as int)) `03301-3301YesHoover: use advertisement\_\_is\_bumper, advertisement\_\_is\_external, advertisement\_\_is\_rbp regardless of ads\_in\_slot\_\_advertisement\_\_is\_bumper, ads\_in\_slot\_\_advertisement\_\_is\_external, ads\_in\_slot\_\_advertisement\_\_is\_rbpit will never be true.Hoover++: useads\_in\_slot\_\_advertisement\_\_is\_bumper, ads\_in\_slot\_\_advertisement\_\_is\_external, ads\_in\_slot\_\_advertisement\_\_is\_rbp38`if(partner.network_is_extra_item_owner and (coalesce(advertisement.bit_flags, 0) &  		   shiftleft(cast(1 as long), 48)) > 0, cast(8 as int), cast(0 as int))  ` 06-6 Hoover: use advertisement\_\_bit\_flags Hoover++: use ads\_in\_slot\_\_advertisement\_\_bit\_flags416`if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int), cast(0 as int))` 120801208 Not implemented in hoover++ |
| bit | value | control\_sum | stage\_sum | diff\_sum | Expected | Reason |
| 0 | 1` if(partner.network_is_ad_owner and !advertisement.is_bumper and !advertisement.is_external and advertisement.is_rbp, cast(1 as int), cast(0 as int)) ` | 0 | 3301 | -3301 | Yes | Hoover: use advertisement\_\_is\_bumper, advertisement\_\_is\_external, advertisement\_\_is\_rbp regardless of ads\_in\_slot\_\_advertisement\_\_is\_bumper, ads\_in\_slot\_\_advertisement\_\_is\_external, ads\_in\_slot\_\_advertisement\_\_is\_rbpit will never be true.Hoover++: useads\_in\_slot\_\_advertisement\_\_is\_bumper, ads\_in\_slot\_\_advertisement\_\_is\_external, ads\_in\_slot\_\_advertisement\_\_is\_rbp |
| 3 | 8`if(partner.network_is_extra_item_owner and (coalesce(advertisement.bit_flags, 0) &  		   shiftleft(cast(1 as long), 48)) > 0, cast(8 as int), cast(0 as int))  ` | 0 | 6 | -6 |  | Hoover: use advertisement\_\_bit\_flags Hoover++: use ads\_in\_slot\_\_advertisement\_\_bit\_flags |
| 4 | 16`if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int), cast(0 as int))` | 1208 | 0 | 1208 |  | Not implemented in hoover++ |
| **process\_batch\_id** | 2 | 2 | 1 | 1 | Expected | `process_batch_id` differences can be attributed to how the batch splitting differs between matcher and hoover++ streaming. We should ignore this dimension |


## Round 4

add the following logic to bit\_flag\_aim\_product\_category

```
         + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int), cast(0 as int)) 
```


# Columns Level Diff

| **Column name** | **Diff** | **Reason** |  |  |
| --- | --- | --- | --- | --- |
| decision\_type | ‘Unknown' → 'Replacement Variant' \| 'Unknown' → 'Replacement Variant' \| 'Unknown' → 'Replacement Default'**control\_decision\_type****stage\_decision\_type****control\_sum****stage\_sum****diff**UnknownUnknown253780253366414N/AN/A32393288-49Replacement VariantReplacement Variant402576-174Replacement DefaultReplacement Default24402631-191 | <https://github.freewheel.tv/data/hoover-model/pull/315>UDF `cal_decision_type miss supplySource == 1``CREATE OR REPLACE FUNCTION fw1_stg.xkbai.cal_decision_type(bigFlag BIGINT, deliveryMethod STRING, supplySource INT) RETURNS STRING RETURN   CASE     WHEN (bigFlag & 32768) > 0 THEN       CASE         WHEN deliveryMethod = 'Static' AND (bigFlag & 536870912) > 0 THEN           CASE             WHEN (bigFlag & 67108864) > 0 THEN 'Replacement Default using Creative Variant'             ELSE 'Replacement Default' END WHEN deliveryMethod = 'Dynamic' AND (bigFlag & 131072) > 0 THEN 'Replacement Variant'         WHEN (bigFlag & 134217728) > 0 THEN 'Audience Targeted Creative Default'         WHEN (bigFlag & 268435456) > 0 THEN 'Audience Targeted Creative Variant'         WHEN deliveryMethod = 'Static' AND (bigFlag & 67108864) > 0 THEN 'Creative Variant'         ELSE 'N/A' END ELSE 'Unknown' END;        , cal_decision_type(coalesce(partner.bit_flags, cast(0 as long))                              + coalesce(ad_ctx.ad.bit_flags, cast(0 as long))                              + coalesce(request.bit_flags, cast(0 as long)),                          ad_ctx.ad.ad_delivery_method,                          coalesce(partner.supply_source, cast(-1 as int)))                                as decision_type   ``     , cal_decision_type(coalesce(partner.bit_flags, cast(0 as long))             + coalesce(ad_in_slot.advertisement.bit_flags, cast(0 as long))             + coalesce(request.bit_flags, cast(0 as long)),         ad_in_slot.advertisement.ad_delivery_method, coalesce(partner.supply_source, cast(-1 as int)))                               as decision_type``  val calDecisionType: UserDefinedFunction = udf((bigFlag: Long, deliveryMethod: String, supplySource: Long) => {     if(supplySource == 1 && (bigFlag & 32768) > 0) { // 32768:BIT_FLAG_HYLDA_REQUEST       if (deliveryMethod == "Static" && (bigFlag & 536870912) > 0) { // 536870912:BIT_FLAG_SCHEDULED_AD_REPLACEABLE         if ((bigFlag & 67108864) > 0) { // 67108864:BIT_FLAG_CREATIVE_AUTO_SELECT           "Replacement Default using Creative Variant"         } else {           "Replacement Default"         }       } else if (deliveryMethod == "Dynamic" && (bigFlag & 131072) > 0) { // 131072:BIT_FLAG_REPLACEMENT_AD         "Replacement Variant"       } else if ((bigFlag & 134217728) > 0) { // 134217728:BIT_FLAG_CREATIVE_AUDIENCE_TARGETING_DEFAULT         "Audience Targeted Creative Default"       } else if ((bigFlag & 268435456) > 0) { // 268435456:BIT_FLAG_CREATIVE_AUDIENCE_TARGETING_SUCCESS         "Audience Targeted Creative Variant"       } else if (deliveryMethod == "Static" && (bigFlag & 67108864) > 0) { // 67108864:BIT_FLAG_CREATIVE_AUTO_SELECT         "Creative Variant"       } else {         "N/A"       }     } else {       "Unknown"     }   }``select decision_type, supply_source = 1, sum(selected_primary_ads) as sum from fw1_stg.xkbai.f_order_selected_hourly_hoover_plus  where decision_type in ('N/A', 'Replacement Variant', 'Replacement Default') group by 1,2 order by 1,2` |  |  |
| **control\_decision\_type** | **stage\_decision\_type** | **control\_sum** | **stage\_sum** | **diff** |
| Unknown | Unknown | 253780 | 253366 | 414 |
| N/A | N/A | 3239 | 3288 | -49 |
| Replacement Variant | Replacement Variant | 402 | 576 | -174 |
| Replacement Default | Replacement Default | 2440 | 2631 | -191 |


# Query

```sql


truncate table fw1_stg.xkbai.f_order_selected_hourly_hoover_plus;

CREATE
OR REPLACE FUNCTION fw1_stg.xkbai.cal_decision_type(bigFlag BIGINT, deliveryMethod STRING, supplySource INT)
RETURNS STRING
RETURN
  CASE
    WHEN supplySource = 1 AND (bigFlag & 32768) > 0 THEN
      CASE
        WHEN deliveryMethod = 'Static' AND (bigFlag & 536870912) > 0 THEN
          CASE
            WHEN (bigFlag & 67108864) > 0 THEN 'Replacement Default using Creative Variant'
            ELSE 'Replacement Default'
END
WHEN deliveryMethod = 'Dynamic' AND (bigFlag & 131072) > 0 THEN 'Replacement Variant'
        WHEN (bigFlag & 134217728) > 0 THEN 'Audience Targeted Creative Default'
        WHEN (bigFlag & 268435456) > 0 THEN 'Audience Targeted Creative Variant'
        WHEN deliveryMethod = 'Static' AND (bigFlag & 67108864) > 0 THEN 'Creative Variant'
        ELSE 'N/A'
END
ELSE 'Unknown'
END;



INSERT INTO fw1_stg.xkbai.f_order_selected_hourly_hoover_plus (
select event_hour                                                                                    as process_batch_id
     , coalesce(partner.network_id, cast(-1 as long))                                                     as network_id
     , coalesce(partner.content_owner_network_id, cast(-1 as long))                                       as content_owner_id
     , if(
        coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and coalesce(partner.role, "") = "CRO",
        cast(-3 as long),
        coalesce(partner.distributor_network_id, cast(-1 as long)))                                       as distributor_id
     , coalesce(partner.reseller_network_id, cast(-1 as long))                                            as reseller_id
     , coalesce(request.context.tv_network_id, cast(-1 as long))                                          as tv_network_id
     , coalesce(partner.role, "")                                                                         as transaction_type
     , NULL                                                                                               as traffic_type
     , coalesce(partner.bit_flags, cast(0 as long))
    + coalesce(ad_ctx.ad.bit_flags, cast(0 as long))
    +
       coalesce(request.bit_flags, cast(0 as long))                                                       as bit_flag
     , coalesce(partner.asset_id, cast(-1 as long))                                                       as asset_id
     , coalesce(partner.series_id, cast(-1 as long))                                                      as series_id
     , coalesce(partner.asset_group_ids, cast(array() as array<long>))                                    as asset_group_ids
     , coalesce(partner.site_section_id, cast(-1 as long))                                                as site_section_id
     , coalesce(partner.site_id, cast(-1 as long))                                                        as site_id
     , coalesce(partner.site_section_group_ids, cast(array() as array<long>))                             as site_section_group_ids
     , partner.airing_id                                                                                  as airing_id
     , partner.airing_channel_id                                                                          as channel_id
     , coalesce(partner.break_id, cast(-1 as long))                                                       as break_id
     , coalesce(slot_ctx.slot.time_position_class, "Unknown")                                             as time_position_class
     , coalesce(partner.inbound_rule_id, cast(-1 as long))                                                as inbound_mrm_rule_id
     , coalesce(partner.rule_id, cast(-1 as long))                                                        as mrm_rule_id
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.campaign_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as campaign_id
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.io_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as io_id
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.placement_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as placement_id
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.ad_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as ad_id
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.creative_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as creative_id
     , ad_ctx.ad.ad_delivery_method                                                                       as delivery_method
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.targeting_criteria_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as targeting_criteria_id
     , if(partner.network_is_extra_item_owner, coalesce(ad_ctx.ad.ad_unit_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as ad_unit_id
     , case
           when partner.sales_channel in (5, 6)
               then coalesce(partner.matched_audience_item_ids, cast(array() as array<long>))
           when partner.network_is_extra_item_owner then coalesce(ad_ctx.ad.matched_audience_item_ids,
                                                                  cast(array() as array<long>))
           else cast(array() as array<long>)
    end                                                                                                   as matched_audience_item_ids
     , case
           when partner.sales_channel in (5, 6)
               then coalesce(partner.matched_key_value_ids, cast(array() as array<long>))
           when partner.network_is_extra_item_owner
               then coalesce(ad_ctx.ad.matched_key_value_ids, cast(array() as array<long>))
           else cast(array() as array<long>)
    end                                                                                                   as matched_keyvalue_item_ids
     , case
           when partner.sales_channel in (5, 6) then coalesce(partner.matched_daypart, false)
           when partner.network_is_extra_item_owner then coalesce(ad_ctx.ad.matched_daypart, false)
           else false
    end                                                                                                   as matched_daypart
     , "Unknown"                                                                                          as placement_type_priority
     , coalesce(visitor.platform_group, "-1")                                                             as platform_group
     , NULL                                                                                               as geo_visibility
     , coalesce(partner.user_agent_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as user_agent_visibility
     , coalesce(visitor.postal_code, "-1")                                                                as postal_code
     , coalesce(partner.postal_code_package_id, cast(array() as array<int>))                              as postal_code_package_ids
     , coalesce(visitor.city_id, cast(-1 as int))                                                         as user_city_id
     , coalesce(visitor.state_id, cast(-1 as int))                                                        as user_state_id
     , coalesce(visitor.dma_code, cast(-1 as int))                                                        as user_dma_code
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                       as user_country_id
     , coalesce(visitor.platform_browser_id, cast(-1 as long))                                            as delivered_platform_browser_id
     , coalesce(visitor.platform_device_id, cast(-1 as long))                                             as delivered_platform_device_id
     , coalesce(visitor.platform_os_id, cast(-1 as long))                                                 as delivered_platform_os_id
     , coalesce(visitor.operator_zone_id, cast(-1 as long))                                               as operator_zone_id
     , coalesce(request.delivery_method, "MRMADS")                                                        as integration_delivery_method
     , cast(-1 as long)                                                                                   as scenario_id
     , cast(-1 as long)                                                                                   as audience_extension_deal_id
     , coalesce(partner.tracked_audience_item_ids, cast(array() as array<long>))                          as tracked_audience_item_ids
     , coalesce(partner.geo_state_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as geo_state_visibility
     , coalesce(partner.geo_dma_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as geo_dma_visibility
     , coalesce(partner.geo_city_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as geo_city_visibility
     , coalesce(partner.geo_zip_code_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as geo_zipcode_visibility
     , coalesce(partner.key_value_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as key_value_visibility
     , coalesce(slot_ctx.slot.avail_type, "")                                                             as slot_avail_type
     , if(partner.role = 'CRO', coalesce(ad_ctx.ad.linear_decision_type, "Not Applicable"),
          "Not Applicable")                                                                               as linear_decision_type
     , if(visitor.standard_device_type_child_id is null,
          cast(array() as array<int>),
          array(visitor.standard_device_type_child_id))                                                   as standard_device_type_ids
     , coalesce(visitor.standard_environment_id, cast(-1 as int))                                         as standard_environment_id
     , coalesce(visitor.standard_os_id, cast(-1 as int))                                                  as standard_os_id
     , if(partner.standard_brand_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_brand_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_brand_id
     , if(partner.standard_channel_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_channel_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_channel_id
     , if(partner.standard_genre_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_genre_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                    as standard_genre_ids
     , if(partner.content_form_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.content_form_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as content_form_id
     , if(partner.content_rating_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.content_rating_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as content_rating_id
     , if(partner.standard_language_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_language_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                    as standard_language_ids
     , coalesce(request.context.stream_mode_id, cast(-1 as int))                                          as stream_mode_id
     , coalesce(request.context.inventory_location_id, cast(-1 as int))                                   as inventory_location_id
     , "Unknown"                                                                                          as mrm_rule_type_priority
     , cast(array() as array<long>)                                                                       as listing_ids
     , coalesce(partner.inbound_order_id, cast(-1 as long))                                               as inbound_order_id
     , coalesce(partner.inbound_listing_ids, cast(array() as array<long>))                                as inbound_listing_ids
     , coalesce(partner.outbound_order_id, cast(-1 as long))                                              as outbound_order_id
     , coalesce(partner.outbound_listing_id, cast(array() as array<long>))                               as outbound_listing_ids
     , sum(if(ad_ctx.ad.is_undeliverable = false and !ad_ctx.ad.is_fallback, 1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_primary_ads
     , sum(if(ad_ctx.ad.is_undeliverable = false and ad_ctx.ad.is_fallback, 1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_fallback_ads
     , cast(0 as double)                                                                                  as selected_margin
     , cast(0 as double)                                                                                  as selected_bidding_revenue
     , cast(0 as double)                                                                                  as co_selected_bidding_revenue
     , cast(0 as double)                                                                                  as d_selected_bidding_revenue
     , cast(0 as double)                                                                                  as r_selected_bidding_revenue
     , cast(0 as double)                                                                                  as selected_fallback_margin
     , cast(0 as double)                                                                                  as selected_fallback_bidding_revenue
     , cast(0 as double)                                                                                  as co_selected_fallback_bidding_revenue
     , cast(0 as double)                                                                                  as d_selected_fallback_bidding_revenue
     , cast(0 as double)                                                                                  as r_selected_fallback_bidding_revenue
     , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                  as ip_enabled_audience_id
     , if(partner.standard_programmer_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_programmer_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_programmer_id
     , coalesce(partner.geo_country_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as geo_country_visibility
     , coalesce(partner.standard_brand_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_brand_visibility
     , coalesce(partner.standard_genre_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_genre_visibility
     , coalesce(partner.content_rating_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as content_rating_visibility
     , if(partner.standard_endpoint_owner_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_endpoint_owner_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_endpoint_owner_id
     , if(partner.standard_endpoint_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_endpoint_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_endpoint_id
     , coalesce(partner.outbound_exchange_order_id, cast(-1 as long))                                     as outbound_exchange_order_id
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.internal_deal_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as deal_id
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.buyer_group_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as buyer_group_id
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.dsp_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as dsp_id
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.advertiser_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as programmatic_advertiser_id
     , coalesce(partner.supply_source, cast(-1 as int))                                                   as supply_source
     , coalesce(partner.sales_channel, cast(-1 as int))                                                   as sales_channel
     , coalesce(partner.standard_endpoint_owner_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_endpoint_owner_visibility
     , coalesce(partner.standard_endpoint_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_endpoint_visibility
     , coalesce(partner.inbound_order_auction_type, "UNKNOWN")                                            as inbound_order_auction_type
     , sum(if(ad_ctx.ad.is_undeliverable = false and coalesce(request.is_ssp_bidder_request, false) = true and
              ((coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or
               (coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as ssp_bids
     , sum(if(ad_ctx.ad.is_undeliverable = false and coalesce(request.is_ssp_bidder_request, false) = true and
              ((coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or
               (coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    * coalesce(partner.metrics.content_owner_bidding_revenue, cast(0 as double))
    *
           coalesce(slot_ack_ctx.metrics.fire_event_slot_revenue_ratio,
                    cast(0 as int)))                                                                      as ssp_co_bidding_revenue
     , if(partner.standard_content_daypart_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_content_daypart_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_content_daypart_id
     , coalesce(request.bid_request.publisher_id, "Unknown")                                              as ssp_external_publisher_id
     , if(coalesce(partner.role, "") in ("CRO", "R"),
          coalesce(ad_ctx.ad.global_advertiser_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as global_advertiser_ids
     , if(coalesce(partner.role, "") in ("CRO", "R"),
          coalesce(ad_ctx.ad.global_brand_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as global_brand_ids
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.ad.market_ad_id,
                                                    coalesce(ad_ctx.candidate.market_ad_id, cast(-1 as long))),
          cast(-1 as long))                                                                               as market_ad_id
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.trading_desk_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as trading_desk_id
     , coalesce(visitor.dma_code_id, cast(-1 as int))                                                     as user_dma_code_id
     , if(partner.demand_dim_awareability or partner.network_is_ad_owner,
          coalesce(ad_ctx.ad.global_industry_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as global_industry_ids
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.buyer_platform_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as buyer_platform_id
     , coalesce(partner.standard_programmer_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_programmer_visibility
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.bidding_seat_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as bidding_seat_id
     , if(
        coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and coalesce(partner.role, "") = "CRO",
        cast(-3 as long),
        if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.rendition_id, cast(-1 as long)),
           cast(-1 as long)))                                                                             as rendition_id
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.bidding_buyer_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as bidding_buyer_id
     , if(partner.demand_dim_awareability,
          coalesce(ad_ctx.candidate.global_agency_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as global_agency_ids
     , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                  as standard_publisher_id
     , coalesce(partner.bidder_seat_id, cast(-1 as long))                                                 as bidder_seat_id
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.auction.application_type, ''),
          '')                                                                                             as application_type
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.auction.app_bundle, ''),
          '')                                                                                             as app_bundle
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.auction.site_domain, ''),
          '')                                                                                             as site_domain
     , coalesce(request.global_currency_version, '')                                                      as global_currency_version
     , coalesce(partner.global_currency_id, cast(-1 as long))                                             as global_currency_id
     , coalesce(request.context.standard_app_id, cast(-1 as long))                                        as standard_app_id
     , if(
        coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and coalesce(partner.role, "") = "CRO",
        cast(-3 as long),
        coalesce(request.context.profile_id, cast(-1 as long)))                                           as profile_id
     , coalesce(request.context.profile_type, 'UNKNOWN')                                                  as profile_type
     , if(partner.standard_content_series_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_content_series_id, cast(-1 as int)),
          cast(-1 as int))                                                                                as standard_content_series_id
     , if(partner.standard_content_subscription_model_visibility.report_aggregate is not null or
          partner.supply_source != 3,
          coalesce(request.context.standard_content_subscription_model_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                             as standard_content_subscription_model_id
     , coalesce(request.context.standard_ssp_channel_id,
                cast(-1 as long))                                                                         as standard_ssp_channel_id
     , coalesce(request.context.standard_site_domain_id,
                cast(-1 as long))                                                                         as standard_site_domain_id
     , case
           when partner.sales_channel in (5, 6) then coalesce(partner.matched_inventory_package_ids,
                                                              cast(array() as array<long>))
           when partner.network_is_extra_item_owner then coalesce(ad_ctx.ad.matched_inventory_package_ids,
                                                                  cast(array() as array<long>))
           else cast(array() as array<long>)
    end                                                                                                   as matched_inventory_package_ids
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.dsp_currency_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as dsp_currency_id
     , coalesce(visitor.standard_operator_id, cast(-1 as long))                                           as standard_operator_id
     , coalesce(request.context.standard_iab_category_ids,
                cast(array() as array<long>))                                                             as standard_iab_category_ids
     , coalesce(partner.upstream_inbound_order_id, cast(-1 as long))                                      as upstream_inbound_order_id
     , coalesce(partner.upstream_global_currency_id, cast(-1 as long))                                    as upstream_global_currency_id
     , if(partner.standard_content_territory_visibility.report_aggregate is not null or partner.supply_source != 3,
          coalesce(request.context.standard_content_territory_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                             as standard_content_territory_id
     , coalesce(partner.standard_content_series_visibility.report_aggregate,
                'FULL_VISIBILITY')                                                                        as standard_content_series_visibility
     , if(partner.standard_content_credential_status_visibility.report_aggregate is not null or
          partner.supply_source != 3,
          coalesce(request.context.standard_content_credential_status_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                             as standard_content_credential_status_id
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.external_seat_id, 'Unknown'),
          'Unknown')                                                                                      as external_seat_id
     , if(partner.network_is_extra_item_owner,
          coalesce(ad_ctx.ad.matched_contextual_segment_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as matched_contextual_segment_ids
     , cast(array() as array<long>)                                                                       as inventory_package_ids
     , coalesce(partner.selected_yield_optimization_ids,
                cast(array() as array<long>))                                                             as selected_yield_optimization_ids
     , coalesce(ad_ctx.candidate.auction.publisher_id, '')                                                as outbound_publisher_id
     , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                           as standard_retailer_id
     , coalesce(partner.standard_content_subscription_model_visibility.report_aggregate,
                'FULL_VISIBILITY')                                                                        as standard_content_subscription_model_visibility
     , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                       as standard_manufacturer_id
     , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                 as standard_app_bundle_id
     , "FULL_VISIBILITY"                                                                                  as content_owner_visibility
     , if(partner.sales_channel = 4, "NO_VISIBILITY", "FULL_VISIBILITY")                                  as reseller_visibility
     , 'Removed'                                                                                          as slot_user_drop_off
     , case
           when coalesce(partner.sales_channel, cast(-1 as int)) = 3
               then if(partner.network_is_ad_owner, cast(5 as int), cast(3 as int)) --  5 for Reseller Sold - Reseller Tag and 3 for MRM Partner
           when coalesce(partner.sales_channel, cast(-1 as int)) in (5, 6) then cast(3 as int)
           else coalesce(partner.sales_channel, cast(-1 as int))
    end                                                                                                   as sales_strategy
     , NULL                                                                                               as ivt_indicator
     , case
           when coalesce(request.flags, cast(0 as long)) & 32 > 0 then 'No Selection'
           when coalesce(request.advertisement_delivered_count, request.advertisement_count, cast(0 as long)) = 0
               then 'Empty'
           else 'Filled'
    end                                                                                                   as request_fill_status
     , case
           when slot_ctx.slot.time_position_class = 'overlay' then
               case
                   when slot_ctx.slot.num_ads = 0 and slot_ctx.slot.max_ads > 0 then 'Empty - Slots with Avails'
                   when slot_ctx.slot.num_ads = 0 and slot_ctx.slot.max_ads = 0 then 'Empty - Slots without Avails'
                   when slot_ctx.slot.num_ads > 0 and slot_ctx.slot.num_ads < slot_ctx.slot.max_ads
                       then 'Partially Filled'
                   when slot_ctx.slot.num_ads > 0 and slot_ctx.slot.num_ads = slot_ctx.slot.max_ads then 'Fully Filled'
                   when slot_ctx.slot.num_ads is null or slot_ctx.slot.max_ads is null then 'Unknown'
                   else 'Unknown'
                   end
           else
               case
                   when slot_ctx.slot.num_ads = 0 and slot_ctx.slot.unfilled_avails > 0 then 'Empty - Slots with Avails'
                   when slot_ctx.slot.num_ads = 0 and slot_ctx.slot.unfilled_avails = 0
                       then 'Empty - Slots without Avails'
                   when slot_ctx.slot.num_ads > 0 and slot_ctx.slot.unfilled_avails > 0 then 'Partially Filled'
                   when slot_ctx.slot.num_ads > 0 and slot_ctx.slot.unfilled_avails = 0 then 'Fully Filled'
                   when slot_ctx.slot.num_ads is null or slot_ctx.slot.unfilled_avails is null then 'Unknown'
                   else 'Unknown'
                   end
    end                                                                                                   as slot_fill_status
     , case
           when slot_ctx.slot.sequence is null then 'Null'
           when slot_ctx.slot.sequence > 5 then '5+'
           else cast(slot_ctx.slot.sequence as string)
    end                                                                                                   as slot_sequence_normalized
     , if(
        coalesce(slot_ctx.slot.ad_unit_network_id, cast(-1 as long)) = coalesce(partner.network_id, cast(-1 as long)) or
        coalesce(slot_ctx.slot.normalized_ad_unit_id, cast(-1 as long)) in (1, 2, 3, 4, 5, 6),
        coalesce(slot_ctx.slot.normalized_ad_unit_id, cast(-1 as long)),
        cast(-1 as long))                                                                                 as slot_ad_unit_id
     , if(coalesce(slot_ctx.slot.flags, cast(0 as long)) & 8 > 0, 'Yes', 'No')                            as slot_removed_by_ux_indicator
     , if(coalesce(request.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 9) > 0, true, false)  as live_linear_indicator
     , if(coalesce(request.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 34) > 0, true, false) as ssp_bidder_indicator
     , if(coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50) > 0, true, false) as ssp_bidder_buyer_indicator
     , if(coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 40) > 0, true, false) as partner_tag_indicator
     , if(partner.sales_channel = 2,
          if(coalesce(ad_ctx.ad.entity_flags, cast(0 as long)) & shiftleft(cast(1 as long), 2) > 0, 'Yes', 'No'),
          'Not Applicable')                                                                               as promo_ad_indicator
     , if(partner.sales_channel = 2,
          if(coalesce(ad_ctx.ad.entity_flags, cast(0 as long)) & shiftleft(cast(1 as long), 35) > 0, 'Yes', 'No'),
          'Not Applicable')                                                                               as evergreen_ad_indicator
     , if(ad_ctx.ad.is_fallback = false or
          (coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 25) > 0 and ad_ctx.ad.is_undeliverable = false),
          'Primary',
          'Fallback')                                                                                     as primary_ad_indicator
     , if(coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 9) > 0, 'Ad With Fallback',
          'Ad Without Fallback')                                                                          as ad_with_fallback_indicator
     , coalesce(partner.priority_tier, 'UNKNOWN')                                                         as priority_tier
     , coalesce(partner.priority_type, 'UNKNOWN')                                                         as priority_type
     , coalesce(partner.priority_value, cast(0 as int))                                                   as priority_value
     , if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.advertiser_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as local_advertiser_id
     , if(ad_ctx.ad.is_undeliverable = true, coalesce(ad_ctx.candidate.error, ad_ctx.ad.error, ''),
          '')                                                                                             as failed_ad_error_code
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_fallback = false and ad_ctx.ad.is_sstf_fallback = false,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as placed_ads_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_fallback = false and ad_ctx.ad.is_sstf_fallback = false and
              coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 9) > 0,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as placed_ads_has_fallback_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and (ad_ctx.ad.is_fallback = true or ad_ctx.ad.is_sstf_fallback = true),
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as placed_fallback_ads_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and
              (coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 25) > 0 or ad_ctx.ad.is_fallback = false),
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as filled_ads_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and
              (coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 25) > 0 or ad_ctx.ad.is_fallback = false),
              coalesce(ad_ctx.ad.duration, cast(0 as long)), cast(0 as long)) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as filled_ads_duration_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and
              coalesce(ad_ctx.ad.flags, cast(0 as long)) & shiftleft(cast(1 as long), 25) > 0,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as filled_ads_sstf_fallback_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = true,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as failed_ads_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_ads_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and ad_ctx.ad.is_fallback = false,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_ads_in_played_slot_primary
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and ad_ctx.ad.is_fallback = true,
              1, 0) *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as selected_ads_in_played_slot_fallback
     , cast(0 as long)                                                                                    as placed_ads_in_all_slot
     , cast(0 as long)                                                                                    as placed_ads_has_fallback_in_all_slot
     , cast(0 as long)                                                                                    as placed_fallback_ads_in_all_slot
     , cast(0 as long)                                                                                    as filled_ads_in_all_slot
     , cast(0 as long)                                                                                    as filled_ads_duration_in_all_slot
     , cast(0 as long)                                                                                    as filled_ads_sstf_fallback_in_all_slot
     , cast(0 as long)                                                                                    as failed_ads_in_all_slot
     , cast(0 as long)                                                                                    as selected_ads_in_all_slot
     , cast(0 as long)                                                                                    as selected_ads_in_all_slot_primary
     , cast(0 as long)                                                                                    as selected_ads_in_all_slot_fallback
     , fw1_stg.xkbai.cal_decision_type(coalesce(partner.bit_flags, cast(0 as long))
                             + coalesce(ad_ctx.ad.bit_flags, cast(0 as long))
                             + coalesce(request.bit_flags, cast(0 as long)),
                         ad_ctx.ad.ad_delivery_method,
                         coalesce(partner.supply_source, cast(-1 as int)))                                as decision_type
     , if(coalesce(slot_ctx.slot.avail_type, "") = '', 'Unknown'
    , if((coalesce(request.bit_flags, cast(0 as long)) & 512) = 512 --is live_linear
              , CASE
                    WHEN coalesce(slot_ctx.slot.avail_type, "") = 'NON_ADDRESSABLE' THEN 'Non-Addressable'
                    WHEN coalesce(slot_ctx.slot.avail_type, "") = 'ADDRESSABLE_FULL_AVAIL' THEN 'Full Avail'
                    WHEN coalesce(slot_ctx.slot.avail_type, "") = 'ADDRESSABLE_SPLIT_AVAIL' THEN 'Split Avail'
                    ELSE 'Not Applicable' END
              ,
         'Not Applicable'))                                                                               as linear_avail_type
     , if((coalesce(request.bit_flags, cast(0 as long)) & 32768) = 0 and
          (coalesce(request.bit_flags, cast(0 as long)) & 512) > 0,
          partner.airing_channel_id,
          cast(-1 as long))                                                                               as station_id
     , if((coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 51)) > 0, true,
          false)                                                                                          as ad_in_passback_indicator
     , if(coalesce(partner.bit_flags, cast(0 as long)) & 2 > 0, true, false)                              as loop_indicator
     , coalesce(ad_ctx.candidate.auction.device_type, 'Unknown')                                          as programmatic_device_type
     , coalesce(visitor.standard_device_type_child_id, cast(-1 as int))                                   as standard_device_type_id
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and
              coalesce(request.is_ssp_bidder_request, false) = true and
              ((coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or
               (coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    *
           coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                               as outbound_bids_in_played_slot
     , sum(if(partner.role in ('CRO', 'R') and ad_ctx.ad.is_undeliverable = false and
              coalesce(request.is_ssp_bidder_request, false) = true and
              ((coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or
               (coalesce(partner.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    * coalesce(partner.metrics.content_owner_bidding_revenue, cast(0 as double))
    * coalesce(slot_ack_ctx.metrics.fire_event_slot_revenue_ratio,
               cast(0 as int)))                                                                           as outbound_bidding_revenue_in_played_slot
     , coalesce(partner.selected_yield_optimization_info_ids,
                cast(array() as array<array<bigint>>))                                                    as selected_yield_optimization_info_ids
     , coalesce(partner.standard_channel_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as standard_channel_visibility
     , coalesce(partner.content_form_visibility.report_aggregate,
                "FULL_VISIBILITY")                                                                        as content_form_visibility
     , if(partner.network_is_ad_owner and !ad_ctx.ad.is_bumper and !ad_ctx.ad.is_external and ad_ctx.ad.is_rbp,
          cast(1 as int), cast(0 as int))
    + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 53)) > 0, cast(2 as int), cast(0 as int))
    + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 54)) > 0, cast(4 as int), cast(0 as int))
    + if(partner.network_is_extra_item_owner and (coalesce(ad_ctx.ad.bit_flags, 0) &
             shiftleft(cast(1 as long), 48)) > 0, cast(8 as int), cast(0 as int))
    + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int), cast(0 as int)) as bit_flag_aim_product_category
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.media_buyer_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as media_buyer_id
     , if(partner.deal_awareability, coalesce(ad_ctx.candidate.post_auction_discount_id, cast(-1 as long)),
          cast(-1 as long))                                                                               as post_auction_discount_id
     , coalesce(partner.selected_yo_volume_cap_ids, cast(array() as array<long>))                         as selected_yo_volume_cap_ids
     , coalesce(partner.selected_yo_distribution_id, cast(-1 as long))                                    as selected_yo_distribution_id
     , coalesce(partner.selected_yo_distribution_nip_id, cast(-1 as long))                                as selected_yo_distribution_nip_id
     , coalesce(partner.selected_yo_inventory_prioritization_id,
                cast(-1 as long))                                                                         as selected_yo_inventory_prioritization_id
     , coalesce(partner.selected_yo_inventory_prioritization_nip_id,
                cast(-1 as long))                                                                         as selected_yo_inventory_prioritization_nip_id
     , coalesce(partner.selected_yo_margin_id, cast(-1 as long))                                          as selected_yo_margin_id
     , if(partner.demand_dim_awareability, coalesce(ad_ctx.candidate.integration_type, ''),
          '')                                                                                             as integration_type
     , if(partner.supply_source != 3,
          coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
          cast(array() as array<bigint>))                                                                 as standard_content_viewership_profile_ids
     , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                  as standard_privacy_id
     , coalesce(request.context.standard_addressability_ids,
                cast(array() as array<bigint>))                                                           as standard_addressability_ids
     , if(partner.supply_source != 3,
          coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                   as standard_sport_entity_ids
     , 0                                                                                                  as upstream_bidding_revenue_in_played_slot
     , date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp))                                  as event_date
from fw1_prd.hoover_batch.transaction
         lateral view explode(slot_ctxes) as slot_ctx
         lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
         lateral view explode(ad_ctx.networks) as partner
where
    (ad_ctx.ad.is_embedded_tracking = false
   or (ad_ctx.ad.is_embedded_tracking
  and (partner.network_is_ad_owner
   or partner.network_is_extra_item_owner)))
  and ad_ctx.ad.is_bumper = false
  and (coalesce (slot_ack_ctx.metrics.slot_impression
    , cast (0 as long)) != 0
   or coalesce (slot_ack_ctx.metrics.fire_event_slot_revenue_ratio
    , cast (0 as int)) != 0)
  and coalesce(slot_ack_ctx.ack.flags, cast(0 as long)) & 256 = 0
            and date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)) = TIMESTAMP('2026-04-29 16:00:00')
            AND event_hour >= '20260429150000'
            AND event_hour < '20260429180000'
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 196, 197, 198, 199, 200, 201, 202, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 223
)
```



```


INSERT INTO fw1_stg.xkbai.f_order_selected_hourly_hive
SELECT
  process_batch_id,
  network_id,
  content_owner_id,
  distributor_id,
  reseller_id,
  tv_network_id,
  transaction_type,
  traffic_type,
  bit_flag,
  asset_id,
  series_id,
  asset_group_ids,
  site_section_id,
  site_id,
  site_section_group_ids,
  airing_id,
  channel_id,
  break_id,
  time_position_class,
  inbound_mrm_rule_id,
  mrm_rule_id,
  campaign_id,
  io_id,
  placement_id,
  ad_id,
  creative_id,
  delivery_method,
  targeting_criteria_id,
  ad_unit_id,
  matched_audience_item_ids,
  matched_keyvalue_item_ids,
  matched_daypart,
  placement_type_priority,
  platform_group,
  geo_visibility,
  user_agent_visibility,
  postal_code,
  postal_code_package_ids,
  user_city_id,
  user_state_id,
  user_dma_code,
  user_country_id,
  delivered_platform_browser_id,
  delivered_platform_device_id,
  delivered_platform_os_id,
  operator_zone_id,
  integration_delivery_method,
  scenario_id,
  audience_extension_deal_id,
  tracked_audience_item_ids,
  geo_state_visibility,
  geo_dma_visibility,
  geo_city_visibility,
  geo_zipcode_visibility,
  key_value_visibility,
  slot_avail_type,
  linear_decision_type,
  standard_device_type_ids,
  standard_environment_id,
  standard_os_id,
  standard_brand_id,
  standard_channel_id,
  standard_genre_ids,
  content_form_id,
  content_rating_id,
  standard_language_ids,
  stream_mode_id,
  inventory_location_id,
  mrm_rule_type_priority,
  listing_ids,
  inbound_order_id,
  inbound_listing_ids,
  outbound_order_id,
  outbound_listing_ids,
  SUM(selected_primary_ads) AS selected_primary_ads,
  SUM(selected_fallback_ads) AS selected_fallback_ads,
  SUM(selected_margin) AS selected_margin,
  SUM(selected_bidding_revenue) AS selected_bidding_revenue,
  SUM(co_selected_bidding_revenue) AS co_selected_bidding_revenue,
  SUM(d_selected_bidding_revenue) AS d_selected_bidding_revenue,
  SUM(r_selected_bidding_revenue) AS r_selected_bidding_revenue,
  SUM(selected_fallback_margin) AS selected_fallback_margin,
  SUM(selected_fallback_bidding_revenue) AS selected_fallback_bidding_revenue,
  SUM(co_selected_fallback_bidding_revenue) AS co_selected_fallback_bidding_revenue,
  SUM(d_selected_fallback_bidding_revenue) AS d_selected_fallback_bidding_revenue,
  SUM(r_selected_fallback_bidding_revenue) AS r_selected_fallback_bidding_revenue,
  ip_enabled_audience_id,
  standard_programmer_id,
  geo_country_visibility,
  standard_brand_visibility,
  standard_genre_visibility,
  content_rating_visibility,
  standard_endpoint_owner_id,
  standard_endpoint_id,
  outbound_exchange_order_id,
  deal_id,
  buyer_group_id,
  dsp_id,
  programmatic_advertiser_id,
  supply_source,
  sales_channel,
  standard_endpoint_owner_visibility,
  standard_endpoint_visibility,
  inbound_order_auction_type,
  SUM(ssp_bids) AS ssp_bids,
  SUM(ssp_co_bidding_revenue) AS ssp_co_bidding_revenue,
  standard_content_daypart_id,
  ssp_external_publisher_id,
  global_advertiser_ids,
  global_brand_ids,
  market_ad_id,
  trading_desk_id,
  user_dma_code_id,
  global_industry_ids,
  buyer_platform_id,
  standard_programmer_visibility,
  bidding_seat_id,
  rendition_id,
  bidding_buyer_id,
  global_agency_ids,
  standard_publisher_id,
  bidder_seat_id,
  application_type,
  app_bundle,
  site_domain,
  global_currency_version,
  global_currency_id,
  standard_app_id,
  profile_id,
  profile_type,
  standard_content_series_id,
  standard_content_subscription_model_id,
  standard_ssp_channel_id,
  standard_site_domain_id,
  matched_inventory_package_ids,
  dsp_currency_id,
  standard_operator_id,
  standard_iab_category_ids,
  upstream_inbound_order_id,
  upstream_global_currency_id,
  standard_content_territory_id,
  standard_content_series_visibility,
  standard_content_credential_status_id,
  external_seat_id,
  matched_contextual_segment_ids,
  inventory_package_ids,
  selected_yield_optimization_ids,
  outbound_publisher_id,
  standard_retailer_id,
  standard_content_subscription_model_visibility,
  standard_manufacturer_id,
  standard_app_bundle_id,
  content_owner_visibility,
  reseller_visibility,
  slot_user_drop_off,
  sales_strategy,
  ivt_indicator,
  request_fill_status,
  slot_fill_status,
  slot_sequence_normalized,
  slot_ad_unit_id,
  slot_removed_by_ux_indicator,
  live_linear_indicator,
  ssp_bidder_indicator,
  ssp_bidder_buyer_indicator,
  partner_tag_indicator,
  promo_ad_indicator,
  evergreen_ad_indicator,
  primary_ad_indicator,
  ad_with_fallback_indicator,
  priority_tier,
  priority_type,
  priority_value,
  local_advertiser_id,
  failed_ad_error_code,
  SUM(placed_ads_in_played_slot) AS placed_ads_in_played_slot,
  SUM(placed_ads_has_fallback_in_played_slot) AS placed_ads_has_fallback_in_played_slot,
  SUM(placed_fallback_ads_in_played_slot) AS placed_fallback_ads_in_played_slot,
  SUM(filled_ads_in_played_slot) AS filled_ads_in_played_slot,
  SUM(filled_ads_duration_in_played_slot) AS filled_ads_duration_in_played_slot,
  SUM(filled_ads_sstf_fallback_in_played_slot) AS filled_ads_sstf_fallback_in_played_slot,
  SUM(failed_ads_in_played_slot) AS failed_ads_in_played_slot,
  SUM(selected_ads_in_played_slot) AS selected_ads_in_played_slot,
  SUM(selected_ads_in_played_slot_primary) AS selected_ads_in_played_slot_primary,
  SUM(selected_ads_in_played_slot_fallback) AS selected_ads_in_played_slot_fallback,
  SUM(placed_ads_in_all_slot) AS placed_ads_in_all_slot,
  SUM(placed_ads_has_fallback_in_all_slot) AS placed_ads_has_fallback_in_all_slot,
  SUM(placed_fallback_ads_in_all_slot) AS placed_fallback_ads_in_all_slot,
  SUM(filled_ads_in_all_slot) AS filled_ads_in_all_slot,
  SUM(filled_ads_duration_in_all_slot) AS filled_ads_duration_in_all_slot,
  SUM(filled_ads_sstf_fallback_in_all_slot) AS filled_ads_sstf_fallback_in_all_slot,
  SUM(failed_ads_in_all_slot) AS failed_ads_in_all_slot,
  SUM(selected_ads_in_all_slot) AS selected_ads_in_all_slot,
  SUM(selected_ads_in_all_slot_primary) AS selected_ads_in_all_slot_primary,
  SUM(selected_ads_in_all_slot_fallback) AS selected_ads_in_all_slot_fallback,
  decision_type,
  linear_avail_type,
  station_id,
  ad_in_passback_indicator,
  loop_indicator,
  programmatic_device_type,
  standard_device_type_id,
  SUM(outbound_bids_in_played_slot) AS outbound_bids_in_played_slot,
  SUM(outbound_bidding_revenue_in_played_slot) AS outbound_bidding_revenue_in_played_slot,
  selected_yield_optimization_info_ids,
  standard_channel_visibility,
  content_form_visibility,
  bit_flag_aim_product_category,
  media_buyer_id,
  post_auction_discount_id,
  selected_yo_volume_cap_ids,
  selected_yo_distribution_id,
  selected_yo_distribution_nip_id,
  selected_yo_inventory_prioritization_id,
  selected_yo_inventory_prioritization_nip_id,
  selected_yo_margin_id,
  integration_type,
  standard_content_viewership_profile_ids,
  standard_privacy_id,
  standard_addressability_ids,
  standard_sport_entity_ids,
  SUM(upstream_bidding_revenue_in_played_slot) AS upstream_bidding_revenue_in_played_slot,
  event_date
FROM hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly_sampling
WHERE event_date = TIMESTAMP('2026-04-29 16:00:00')
and process_batch_id >= '20260429150000'
and process_batch_id <= '20260429180000'
GROUP BY
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
  21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
  31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
  41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
  51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
  61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
  71, 72, 73, 74,
  87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
  97, 98, 99, 100, 101, 102, 103, 104,
  107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
  117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
  127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
  137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
  147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
  157, 158, 159, 160, 161, 162, 163, 164, 165, 166,
  167, 168, 169, 170, 171, 172, 173, 174, 175,
  196, 197, 198, 199, 200, 201, 202,
  205, 206, 207, 208, 209, 210, 211, 212, 213, 214,
  215, 216, 217, 218, 219, 220, 221,
  223
```


```
select * from fw1_stg.xkbai.validation_config_new ;

CREATE TABLE fw1_stg.xkbai.validation_config_new
AS SELECT * FROM fw1_stg.kbhargava.validation_config_new WHERE 1=0;



INSERT INTO fw1_stg.xkbai.validation_config_new 
(
    control_table, 
    stage_table, 
    validation_table_name, 
    dimensions, 
    metrics
) 
VALUES 
(
    "fw1_stg.xkbai.f_order_selected_hourly_hive", 
    "fw1_stg.xkbai.f_order_selected_hourly_hoover_plus", 
    "f_order_selected_hourly", 

    "'process_batch_id', 'network_id', 'content_owner_id', 'distributor_id', 'reseller_id', 'tv_network_id', 'transaction_type', 'traffic_type', 'bit_flag', 'asset_id', 'series_id', 'asset_group_ids', 'site_section_id', 'site_id', 'site_section_group_ids', 'airing_id', 'channel_id', 'break_id', 'time_position_class', 'inbound_mrm_rule_id', 'mrm_rule_id', 'campaign_id', 'io_id', 'placement_id', 'ad_id', 'creative_id', 'delivery_method', 'targeting_criteria_id', 'ad_unit_id', 'matched_audience_item_ids', 'matched_keyvalue_item_ids', 'matched_daypart', 'placement_type_priority', 'platform_group', 'geo_visibility', 'user_agent_visibility', 'postal_code', 'postal_code_package_ids', 'user_city_id', 'user_state_id', 'user_dma_code', 'user_country_id', 'delivered_platform_browser_id', 'delivered_platform_device_id', 'delivered_platform_os_id', 'operator_zone_id', 'integration_delivery_method', 'scenario_id', 'audience_extension_deal_id', 'tracked_audience_item_ids', 'geo_state_visibility', 'geo_dma_visibility', 'geo_city_visibility', 'geo_zipcode_visibility', 'key_value_visibility', 'slot_avail_type', 'linear_decision_type', 'standard_device_type_ids', 'standard_environment_id', 'standard_os_id', 'standard_brand_id', 'standard_channel_id', 'standard_genre_ids', 'content_form_id', 'content_rating_id', 'standard_language_ids', 'stream_mode_id', 'inventory_location_id', 'mrm_rule_type_priority', 'listing_ids', 'inbound_order_id', 'inbound_listing_ids', 'outbound_order_id', 'outbound_listing_ids', 'ip_enabled_audience_id', 'standard_programmer_id', 'geo_country_visibility', 'standard_brand_visibility', 'standard_genre_visibility', 'content_rating_visibility', 'standard_endpoint_owner_id', 'standard_endpoint_id', 'outbound_exchange_order_id', 'deal_id', 'buyer_group_id', 'dsp_id', 'programmatic_advertiser_id', 'supply_source', 'sales_channel', 'standard_endpoint_owner_visibility', 'standard_endpoint_visibility', 'inbound_order_auction_type', 'standard_content_daypart_id', 'ssp_external_publisher_id', 'global_advertiser_ids', 'global_brand_ids', 'market_ad_id', 'trading_desk_id', 'user_dma_code_id', 'global_industry_ids', 'buyer_platform_id', 'standard_programmer_visibility', 'bidding_seat_id', 'rendition_id', 'bidding_buyer_id', 'global_agency_ids', 'standard_publisher_id', 'bidder_seat_id', 'application_type', 'app_bundle', 'site_domain', 'global_currency_version', 'global_currency_id', 'standard_app_id', 'profile_id', 'profile_type', 'standard_content_series_id', 'standard_content_subscription_model_id', 'standard_ssp_channel_id', 'standard_site_domain_id', 'matched_inventory_package_ids', 'dsp_currency_id', 'standard_operator_id', 'standard_iab_category_ids', 'upstream_inbound_order_id', 'upstream_global_currency_id', 'standard_content_territory_id', 'standard_content_series_visibility', 'standard_content_credential_status_id', 'external_seat_id', 'matched_contextual_segment_ids', 'inventory_package_ids', 'selected_yield_optimization_ids', 'outbound_publisher_id', 'standard_retailer_id', 'standard_content_subscription_model_visibility', 'standard_manufacturer_id', 'standard_app_bundle_id', 'content_owner_visibility', 'reseller_visibility', 'slot_user_drop_off', 'sales_strategy', 'ivt_indicator', 'request_fill_status', 'slot_fill_status', 'slot_sequence_normalized', 'slot_ad_unit_id', 'slot_removed_by_ux_indicator', 'live_linear_indicator', 'ssp_bidder_indicator', 'ssp_bidder_buyer_indicator', 'partner_tag_indicator', 'promo_ad_indicator', 'evergreen_ad_indicator', 'primary_ad_indicator', 'ad_with_fallback_indicator', 'priority_tier', 'priority_type', 'priority_value', 'local_advertiser_id', 'failed_ad_error_code', 'decision_type', 'linear_avail_type', 'station_id', 'ad_in_passback_indicator', 'loop_indicator', 'programmatic_device_type', 'standard_device_type_id', 'standard_channel_visibility', 'content_form_visibility', 'bit_flag_aim_product_category', 'media_buyer_id', 'post_auction_discount_id', 'selected_yo_volume_cap_ids', 'selected_yo_distribution_id', 'selected_yo_distribution_nip_id', 'selected_yo_inventory_prioritization_id', 'selected_yo_inventory_prioritization_nip_id', 'selected_yo_margin_id', 'integration_type', 'standard_content_viewership_profile_ids', 'standard_privacy_id', 'standard_addressability_ids', 'standard_sport_entity_ids', 'selected_yield_optimization_info_ids', 'event_date'", 

    "'selected_primary_ads', 'selected_fallback_ads', 'selected_margin', 'selected_bidding_revenue', 'co_selected_bidding_revenue', 'd_selected_bidding_revenue', 'r_selected_bidding_revenue', 'selected_fallback_margin', 'selected_fallback_bidding_revenue', 'co_selected_fallback_bidding_revenue', 'd_selected_fallback_bidding_revenue', 'r_selected_fallback_bidding_revenue', 'ssp_bids', 'ssp_co_bidding_revenue', 'placed_ads_in_played_slot', 'placed_ads_has_fallback_in_played_slot', 'placed_fallback_ads_in_played_slot', 'filled_ads_in_played_slot', 'filled_ads_duration_in_played_slot', 'filled_ads_sstf_fallback_in_played_slot', 'failed_ads_in_played_slot', 'selected_ads_in_played_slot', 'selected_ads_in_played_slot_primary', 'selected_ads_in_played_slot_fallback', 'placed_ads_in_all_slot', 'placed_ads_has_fallback_in_all_slot', 'placed_fallback_ads_in_all_slot', 'filled_ads_in_all_slot', 'filled_ads_duration_in_all_slot', 'filled_ads_sstf_fallback_in_all_slot', 'failed_ads_in_all_slot', 'selected_ads_in_all_slot', 'selected_ads_in_all_slot_primary', 'selected_ads_in_all_slot_fallback', 'outbound_bids_in_played_slot', 'outbound_bidding_revenue_in_played_slot', 'upstream_bidding_revenue_in_played_slot'"
);
```


```
INSERT INTO fw1_stg.xkbai.f_order_selected_hourly_hive
SELECT
  process_batch_id,
  network_id,
  content_owner_id,
  distributor_id,
  reseller_id,
  tv_network_id,
  transaction_type,
  traffic_type,
  bit_flag,
  asset_id,
  series_id,
  asset_group_ids,
  site_section_id,
  site_id,
  site_section_group_ids,
  airing_id,
  channel_id,
  break_id,
  time_position_class,
  inbound_mrm_rule_id,
  mrm_rule_id,
  campaign_id,
  io_id,
  placement_id,
  ad_id,
  creative_id,
  delivery_method,
  targeting_criteria_id,
  ad_unit_id,
  matched_audience_item_ids,
  matched_keyvalue_item_ids,
  matched_daypart,
  placement_type_priority,
  platform_group,
  geo_visibility,
  user_agent_visibility,
  postal_code,
  postal_code_package_ids,
  user_city_id,
  user_state_id,
  user_dma_code,
  user_country_id,
  delivered_platform_browser_id,
  delivered_platform_device_id,
  delivered_platform_os_id,
  operator_zone_id,
  integration_delivery_method,
  scenario_id,
  audience_extension_deal_id,
  tracked_audience_item_ids,
  geo_state_visibility,
  geo_dma_visibility,
  geo_city_visibility,
  geo_zipcode_visibility,
  key_value_visibility,
  slot_avail_type,
  linear_decision_type,
  standard_device_type_ids,
  standard_environment_id,
  standard_os_id,
  standard_brand_id,
  standard_channel_id,
  standard_genre_ids,
  content_form_id,
  content_rating_id,
  standard_language_ids,
  stream_mode_id,
  inventory_location_id,
  mrm_rule_type_priority,
  listing_ids,
  inbound_order_id,
  inbound_listing_ids,
  outbound_order_id,
  outbound_listing_ids,
  selected_primary_ads,
  selected_fallback_ads,
  selected_margin,
  selected_bidding_revenue,
  co_selected_bidding_revenue,
  d_selected_bidding_revenue,
  r_selected_bidding_revenue,
  selected_fallback_margin,
  selected_fallback_bidding_revenue,
  co_selected_fallback_bidding_revenue,
  d_selected_fallback_bidding_revenue,
  r_selected_fallback_bidding_revenue,
  ip_enabled_audience_id,
  standard_programmer_id,
  geo_country_visibility,
  standard_brand_visibility,
  standard_genre_visibility,
  content_rating_visibility,
  standard_endpoint_owner_id,
  standard_endpoint_id,
  outbound_exchange_order_id,
  deal_id,
  buyer_group_id,
  dsp_id,
  programmatic_advertiser_id,
  supply_source,
  sales_channel,
  standard_endpoint_owner_visibility,
  standard_endpoint_visibility,
  inbound_order_auction_type,
  ssp_bids,
  ssp_co_bidding_revenue,
  standard_content_daypart_id,
  ssp_external_publisher_id,
  global_advertiser_ids,
  global_brand_ids,
  market_ad_id,
  trading_desk_id,
  user_dma_code_id,
  global_industry_ids,
  buyer_platform_id,
  standard_programmer_visibility,
  bidding_seat_id,
  rendition_id,
  bidding_buyer_id,
  global_agency_ids,
  standard_publisher_id,
  bidder_seat_id,
  application_type,
  app_bundle,
  site_domain,
  global_currency_version,
  global_currency_id,
  standard_app_id,
  profile_id,
  profile_type,
  standard_content_series_id,
  standard_content_subscription_model_id,
  standard_ssp_channel_id,
  standard_site_domain_id,
  matched_inventory_package_ids,
  dsp_currency_id,
  standard_operator_id,
  standard_iab_category_ids,
  upstream_inbound_order_id,
  upstream_global_currency_id,
  standard_content_territory_id,
  standard_content_series_visibility,
  standard_content_credential_status_id,
  external_seat_id,
  matched_contextual_segment_ids,
  inventory_package_ids,
  selected_yield_optimization_ids,
  outbound_publisher_id,
  standard_retailer_id,
  standard_content_subscription_model_visibility,
  standard_manufacturer_id,
  standard_app_bundle_id,
  content_owner_visibility,
  reseller_visibility,
  slot_user_drop_off,
  sales_strategy,
  ivt_indicator,
  request_fill_status,
  slot_fill_status,
  slot_sequence_normalized,
  slot_ad_unit_id,
  slot_removed_by_ux_indicator,
  live_linear_indicator,
  ssp_bidder_indicator,
  ssp_bidder_buyer_indicator,
  partner_tag_indicator,
  promo_ad_indicator,
  evergreen_ad_indicator,
  primary_ad_indicator,
  ad_with_fallback_indicator,
  priority_tier,
  priority_type,
  priority_value,
  local_advertiser_id,
  failed_ad_error_code,
  placed_ads_in_played_slot,
  placed_ads_has_fallback_in_played_slot,
  placed_fallback_ads_in_played_slot,
  filled_ads_in_played_slot,
  filled_ads_duration_in_played_slot,
  filled_ads_sstf_fallback_in_played_slot,
  failed_ads_in_played_slot,
  selected_ads_in_played_slot,
  selected_ads_in_played_slot_primary,
  selected_ads_in_played_slot_fallback,
  placed_ads_in_all_slot,
  placed_ads_has_fallback_in_all_slot,
  placed_fallback_ads_in_all_slot,
  filled_ads_in_all_slot,
  filled_ads_duration_in_all_slot,
  filled_ads_sstf_fallback_in_all_slot,
  failed_ads_in_all_slot,
  selected_ads_in_all_slot,
  selected_ads_in_all_slot_primary,
  selected_ads_in_all_slot_fallback,
  decision_type,
  linear_avail_type,
  station_id,
  ad_in_passback_indicator,
  loop_indicator,
  programmatic_device_type,
  standard_device_type_id,
  outbound_bids_in_played_slot,
  outbound_bidding_revenue_in_played_slot,
  selected_yield_optimization_info_ids,
  standard_channel_visibility,
  content_form_visibility,
  bit_flag_aim_product_category,
  media_buyer_id,
  post_auction_discount_id,
  selected_yo_volume_cap_ids,
  selected_yo_distribution_id,
  selected_yo_distribution_nip_id,
  selected_yo_inventory_prioritization_id,
  selected_yo_inventory_prioritization_nip_id,
  selected_yo_margin_id,
  integration_type,
  standard_content_viewership_profile_ids,
  standard_privacy_id,
  standard_addressability_ids,
  standard_sport_entity_ids,
  upstream_bidding_revenue_in_played_slot,
  event_date
FROM hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly_sampling
WHERE event_date = TIMESTAMP('2026-04-14 16:00:00');
```


```



CREATE TABLE fw1_stg.xkbai.f_order_selected_hourly_hive
AS SELECT * FROM hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly_sampling WHERE 1=0;

TRUNCATE TABLE fw1_stg.xkbai.f_order_selected_hourly_hoover_plus;



DROP TABLE IF EXISTS fw1_stg.xkbai.f_order_selected_hourly_hoover_plus;
CREATE TABLE fw1_stg.xkbai.f_order_selected_hourly_hoover_plus
(
    process_batch_id                               string,
    network_id                                     bigint,
    content_owner_id                               bigint,
    distributor_id                                 bigint,
    reseller_id                                    bigint,
    tv_network_id                                  bigint,
    transaction_type                               string,
    traffic_type                                   bigint,
    bit_flag                                       bigint,
    asset_id                                       bigint,
    series_id                                      bigint,
    asset_group_ids                                array<bigint>,
    site_section_id                                bigint,
    site_id                                        bigint,
    site_section_group_ids                         array<bigint>,
    airing_id                                      bigint,
    channel_id                                     bigint,
    break_id                                       bigint,
    time_position_class                            string,
    inbound_mrm_rule_id                            bigint,
    mrm_rule_id                                    bigint,
    campaign_id                                    bigint,
    io_id                                          bigint,
    placement_id                                   bigint,
    ad_id                                          bigint,
    creative_id                                    bigint,
    delivery_method                                string,
    targeting_criteria_id                          bigint,
    ad_unit_id                                     bigint,
    matched_audience_item_ids                      array<bigint>,
    matched_keyvalue_item_ids                      array<bigint>,
    matched_daypart                                boolean,
    placement_type_priority                        string,
    platform_group                                 string,
    geo_visibility                                 string,
    user_agent_visibility                          string,
    postal_code                                    string,
    postal_code_package_ids                        array<integer>,
    user_city_id                                   integer,
    user_state_id                                  integer,
    user_dma_code                                  integer,
    user_country_id                                bigint,
    delivered_platform_browser_id                  bigint,
    delivered_platform_device_id                   bigint,
    delivered_platform_os_id                       bigint,
    operator_zone_id                               bigint,
    integration_delivery_method                    string,
    scenario_id                                    bigint,
    audience_extension_deal_id                     bigint,
    tracked_audience_item_ids                      array<bigint>,
    geo_state_visibility                           string,
    geo_dma_visibility                             string,
    geo_city_visibility                            string,
    geo_zipcode_visibility                         string,
    key_value_visibility                           string,
    slot_avail_type                                string,
    linear_decision_type                           string,
    standard_device_type_ids                       array<integer>,
    standard_environment_id                        integer,
    standard_os_id                                 integer,
    standard_brand_id                              integer,
    standard_channel_id                            integer,
    standard_genre_ids                             array<integer>,
    content_form_id                                integer,
    content_rating_id                              integer,
    standard_language_ids                          array<integer>,
    stream_mode_id                                 integer,
    inventory_location_id                          integer,
    mrm_rule_type_priority                         string,
    listing_ids                                    array<bigint>,
    inbound_order_id                               bigint,
    inbound_listing_ids                            array<bigint>,
    outbound_order_id                              bigint,
    outbound_listing_ids                           array<bigint>,
    selected_primary_ads                           bigint,
    selected_fallback_ads                          bigint,
    selected_margin double,
    selected_bidding_revenue double,
    co_selected_bidding_revenue double,
    d_selected_bidding_revenue double,
    r_selected_bidding_revenue double,
    selected_fallback_margin double,
    selected_fallback_bidding_revenue double,
    co_selected_fallback_bidding_revenue double,
    d_selected_fallback_bidding_revenue double,
    r_selected_fallback_bidding_revenue double,
    ip_enabled_audience_id                         integer,
    standard_programmer_id                         integer,
    geo_country_visibility                         string,
    standard_brand_visibility                      string,
    standard_genre_visibility                      string,
    content_rating_visibility                      string,
    standard_endpoint_owner_id                     integer,
    standard_endpoint_id                           integer,
    outbound_exchange_order_id                     bigint,
    deal_id                                        bigint,
    buyer_group_id                                 bigint,
    dsp_id                                         bigint,
    programmatic_advertiser_id                     bigint,
    supply_source                                  integer,
    sales_channel                                  integer,
    standard_endpoint_owner_visibility             string,
    standard_endpoint_visibility                   string,
    inbound_order_auction_type                     string,
    ssp_bids                                       bigint,
    ssp_co_bidding_revenue double,
    standard_content_daypart_id                    integer,
    ssp_external_publisher_id                      string,
    global_advertiser_ids                          array<bigint>,
    global_brand_ids                               array<bigint>,
    market_ad_id                                   bigint,
    trading_desk_id                                bigint,
    user_dma_code_id                               integer,
    global_industry_ids                            array<bigint>,
    buyer_platform_id                              bigint,
    standard_programmer_visibility                 string,
    bidding_seat_id                                bigint,
    rendition_id                                   bigint,
    bidding_buyer_id                               bigint,
    global_agency_ids                              array<bigint>,
    standard_publisher_id                          bigint,
    bidder_seat_id                                 bigint,
    application_type                               string,
    app_bundle                                     string,
    site_domain                                    string,
    global_currency_version                        string,
    global_currency_id                             bigint,
    standard_app_id                                bigint,
    profile_id                                     bigint,
    profile_type                                   string,
    standard_content_series_id                     integer,
    standard_content_subscription_model_id         bigint,
    standard_ssp_channel_id                        bigint,
    standard_site_domain_id                        bigint,
    matched_inventory_package_ids                  array<bigint>,
    dsp_currency_id                                bigint,
    standard_operator_id                           bigint,
    standard_iab_category_ids                      array<bigint>,
    upstream_inbound_order_id                      bigint,
    upstream_global_currency_id                    bigint,
    standard_content_territory_id                  bigint,
    standard_content_series_visibility             string,
    standard_content_credential_status_id          bigint,
    external_seat_id                               string,
    matched_contextual_segment_ids                 array<bigint>,
    inventory_package_ids                          array<bigint>,
    selected_yield_optimization_ids                array<bigint>,
    outbound_publisher_id                          string,
    standard_retailer_id                           bigint,
    standard_content_subscription_model_visibility string,
    standard_manufacturer_id                       bigint,
    standard_app_bundle_id                         bigint,
    content_owner_visibility                       string,
    reseller_visibility                            string,
    slot_user_drop_off                             string,
    sales_strategy                                 integer,
    ivt_indicator                                  boolean,
    request_fill_status                            string,
    slot_fill_status                               string,
    slot_sequence_normalized                       string,
    slot_ad_unit_id                                bigint,
    slot_removed_by_ux_indicator                   string,
    live_linear_indicator                          boolean,
    ssp_bidder_indicator                           boolean,
    ssp_bidder_buyer_indicator                     boolean,
    partner_tag_indicator                          boolean,
    promo_ad_indicator                             string,
    evergreen_ad_indicator                         string,
    primary_ad_indicator                           string,
    ad_with_fallback_indicator                     string,
    priority_tier                                  string,
    priority_type                                  string,
    priority_value                                 integer,
    local_advertiser_id                            bigint,
    failed_ad_error_code                           string,
    placed_ads_in_played_slot                      bigint,
    placed_ads_has_fallback_in_played_slot         bigint,
    placed_fallback_ads_in_played_slot             bigint,
    filled_ads_in_played_slot                      bigint,
    filled_ads_duration_in_played_slot             bigint,
    filled_ads_sstf_fallback_in_played_slot        bigint,
    failed_ads_in_played_slot                      bigint,
    selected_ads_in_played_slot                    bigint,
    selected_ads_in_played_slot_primary            bigint,
    selected_ads_in_played_slot_fallback           bigint,
    placed_ads_in_all_slot                         bigint,
    placed_ads_has_fallback_in_all_slot            bigint,
    placed_fallback_ads_in_all_slot                bigint,
    filled_ads_in_all_slot                         bigint,
    filled_ads_duration_in_all_slot                bigint,
    filled_ads_sstf_fallback_in_all_slot           bigint,
    failed_ads_in_all_slot                         bigint,
    selected_ads_in_all_slot                       bigint,
    selected_ads_in_all_slot_primary               bigint,
    selected_ads_in_all_slot_fallback              bigint,
    decision_type                                  string,
    linear_avail_type                              string,
    station_id                                     bigint,
    ad_in_passback_indicator                       boolean,
    loop_indicator                                 boolean,
    programmatic_device_type                       string,
    standard_device_type_id                        integer,
    outbound_bids_in_played_slot                   bigint,
    outbound_bidding_revenue_in_played_slot double,
    selected_yield_optimization_info_ids           array<array<bigint>>,
    standard_channel_visibility                    string,
    content_form_visibility                        string,
    bit_flag_aim_product_category                  integer,
    media_buyer_id                                 bigint,
    post_auction_discount_id                       bigint,
    selected_yo_volume_cap_ids                     array<bigint>,
    selected_yo_distribution_id                    bigint,
    selected_yo_distribution_nip_id                bigint,
    selected_yo_inventory_prioritization_id        bigint,
    selected_yo_inventory_prioritization_nip_id    bigint,
    selected_yo_margin_id                          bigint,
    integration_type                               string,
    standard_content_viewership_profile_ids        array<bigint>,
    standard_privacy_id                            bigint,
    standard_addressability_ids                    array<bigint>,
    standard_sport_entity_ids                      array<bigint>,
    upstream_bidding_revenue_in_played_slot double,
    event_date                                     timestamp
)

320054


INSERT INTO fw1_stg.xkbai.f_order_selected_hourly_hive(
     SELECT * FROM hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly_sampling
     where event_date = date_trunc('HOUR', CURRENT_TIMESTAMP()) - INTERVAL 4 hours
);
309466


select distinct event_date from fw1_stg.xkbai.f_order_selected_hourly_hive limit 10;

2026-04-14T16:00:00.000+00:00

```



# Reference

transformer code: [https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f\_order\_selected\_hourly.sql](https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f_order_selected_hourly.sql)

new hoover design: New Hoover Model Design

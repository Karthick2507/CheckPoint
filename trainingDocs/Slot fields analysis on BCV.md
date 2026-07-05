# Slot fields analysis on BCV

# Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

# Columns Recommended for Backfill

| **Column Name** | **Type** | **Backfill?** | **Comment** |
| --- | --- | --- | --- |
| slot\_\_original\_max\_ads | integer | YES | Used in LQS(26) |
| slot\_\_raw\_max\_duration | integer | YES | Used in LQS(41) |
| slot\_\_raw\_max\_ads | integer | YES | Used in LQS(55) |
| slot\_\_carriage\_listing\_split\_unit\_id | bigint | YES | Used in SOS, LQS(48) and Custom Report(5856) |
| partners\_\_content\_owner\_bidding\_revenue | array(double) | YES | Used in SOS, Insights(4053) and LQS(5) |
| partners\_\_network\_is\_ad\_owner | array(boolean) | YES | Used in SOS, Insights(4053) and LQS(5) |
| process\_batch\_id | varchar | YES | rename the column batch\_id to process\_batch\_id in H++ views |
| slot\_\_outbound\_order\_\_order\_id | array(bigint) | YES | Size 0.04THowever, ADS team uses it.like: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260616172444\_042824](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260616172444_042824) |
| partners\_\_avails\_category\_\_supply\_avails | array(bigint) | YES | Size 0.03THowever, it’s a new metric that was implemented in 7.17; we need to add it back to BCV. |

# Columns with Mismatched

Summary:  
Matched transactions: 997/1000  
Matched fields: 464/556 (83.45%)  
Unmatched fields: 92/556 (16.55%)

## Columns with Mismatched Types

| **Column Name** | **SRC Type** | **BCV Type** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| partners\_\_avails\_category\_\_avails | array(integer) | array(bigint) | NO | Some avails in PB are int32, some are int64, to unify it, we use bigint for all avails-related fields |
| partners\_\_avails\_category\_\_unfilled\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_unconstrained\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_market\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_ssp\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_total\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_total\_unfilled\_avails | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_avails\_category\_\_opportunity | array(integer) | array(bigint) | NO | Same as above |
| partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | array(array(array(bigint))) | array(array(array(integer))) | YES | It seems like a typo in H++, the fields are defined as uint32[https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log\_Record.proto#L666](https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log_Record.proto#L666) |

## Columns with Mismatched Values

| **Column Name** | **SRC Values** | **BCV Values** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| request\_\_timestamp | `2026-06-30 14:07:20` | `2026-06-30 10:07:20` | YES | It looks like the BCV uses the local timezone |
| request\_\_flags | `136892929` | `136892993` | NO | Due to post-bid IVT diff |
| `request__context__profile_concrete_event_id request__context__ab_test_item__collection_id request__context__ab_test_item__bucket_id request__context__standard_genre_ids request__context__standard_language_ids request__context__standard_iab_category_ids request__context__standard_content_viewership_profile_ids request__context__standard_sport_entity_ids request__context__video_cro_selected_yield_optimization_infos__sub_yo_id request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids request__scores__network_id request__scores__flag request__scores__score request__candidates request__soft_guaranteed_ad__ad_id request__soft_guaranteed_ad__num_competing_ads request__soft_guaranteed_ad__network_id request__soft_guaranteed_ad__entity_type request__soft_guaranteed_ad__entity_id request__guaranteed_deal_avail__internal_deal_id request__guaranteed_deal_avail__buyer_id request__decision_info__external_bridge__slot_index request__decision_info__external_bridge__status request__decision_info__inventory_protections__level request__decision_info__inventory_protections__scope request__decision_info__inventory_protections__separation request__linear_capnedit__device_id request__linear_capnedit__active_state request__linear_capnedit__tune_time request__linear_capnedit__last_activity_time request__linear_capnedit__is_dvr request__linear_capnedit__mode request__mpe_matcher_filters__bucket_id request__yield_optimization_ids__demand_id request__yield_optimization_ids__optimization_ids request__mpe_matcher_filters__id request__mpe_matcher_filters__bucket_id request__mpe_matcher_filters__weight visitor__tracked_term visitor__postal_code_id visitor__postal_code_package__network_id visitor__postal_code_package__postal_code_package_id visitor__user_segments_lookup_key visitor__standard_device_type_ids visitor__universal_iids slot__listing_id` | \[\] | (null) | NO | \[\] vs null issue:See Request fields analysis on BCV |
| request\_\_mrc\_compliance\_label | \[\]`['OTT_CONTINUOUS_PLAY']` | (null)(null) | NO | 1. Same \[\] vs null issue 2. Due to post-bid IVT diff |
| request\_\_traffic\_compliance\_\_mrc\_compliance\_flag | 3 | 1 | NO | Due to post-bid IVT diff |
| request\_\_traffic\_type | 0 | 2 | NO | Due to post-bid IVT diff |
| request\_\_backend\_filtration\_reason | 0(null) | (null)64 | CHECKING | 1. Need CHECK 2. Due to post-bid IVT diff |
| request\_\_hashed\_key\_value | `2ed5debad79058490e5c83661d8fc086` | `cab385a440e95103f658246a3cfa06ab` | CHECKING |  |
| `request__bid_request__app_id request__bid_request__app_name` | (null) | (null) | NO | Not an issue, this is due to NULL != NULL |
| request\_\_bid\_request\_\_auction\_type | (null) | `FIRST_PRICE` | NO | According to Request fields analysis on BCVH++ is correct |
| request\_\_client\_facing\_ivt\_reason\_flag | (null)(null) | 0`1125899906842628` | NO | 1. null vs 0:     1. Checking the code, the diff is introduced by h++ implementation. Checking transformer code, they will convert the null values by `coalesce(request.client_facing_ivt_reason_flag, cast(0 as long))`, so no impact on the L3 tables. 2. Due to post-bid IVT diff |
| visitor\_\_filtration\_reason | (null) | 1001 | NO | Due to post-bid IVT diff |
| visitor\_\_identity\_user\_ids\_\_namespace\_id | `[6]` | (null) | YES | Same issue in Request fields analysis on BCV |
| visitor\_\_identity\_user\_ids\_\_id | `['d4b972f0-3385-54df-8987-c18061f0402b']` | (null) | YES | Same as above |
| visitor\_\_identity\_user\_ids\_\_authorized\_network\_id | `[[], [], []]``[[]]``[[]]` | `[None, None, None]``[None]`*(null)* | NOCHECKING | 1. \[\[\]\] vs \[None\]     1. See Request fields analysis on BCV 2. \[\[\]\] vs null |
| `partners__avails_category__avails_in_played_slot partners__avails_category__unfilled_avails_in_played_slot partners__avails_category__unconstrained_avails_in_played_slot partners__avails_category__raw_total_avails_in_played_slot partners__avails_category__market_avails_in_played_slot partners__avails_category__ssp_avails_in_played_slot partners__avails_category__total_avails_in_played_slot partners__avails_category__total_unfilled_avails_in_played_slot partners__avails_category__opportunity_in_played_slot partners__avails_category__raw_opportunity_in_played_slot partners__avails_category__slot_opp_avails_in_played_slot partners__avails_category__remaining_avails partners__avails_category__raw_inventory_distinct_avails_in_played_slot` | `[None, None, None, None, None, None]` | *(null)* | CHECKING | \[None\] vs null |
| `partners__eligible_outbound_orders__down_network_id partners__eligible_outbound_orders__order_id partners__eligible_outbound_orders__exchange_order_id partners__eligible_outbound_orders__listing_id partners__eligible_outbound_orders__matched_inventory_package_ids partners__eligible_outbound_orders__bit_flags partners__eligible_outbound_orders__sales_channel partners__eligible_outbound_orders__ad_filling_status__filled_ad_num partners__eligible_outbound_orders__ad_filling_status__unified_unfilled_opp partners__marketplace_audience_extension_deal_ids partners__eligible_outbound_orders__order_type partners__eligible_outbound_orders__order_transaction_type partners__eligible_outbound_orders__order_priority` | `[[523319, 384777, 524565, 372496, 543363], [], [], [], [], []]``[['EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER'], [], [], [], [], []]` | `[[523319, 384777, 524565, 372496, 543363], [], None, None, None, None]``[['EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER', 'EXCHANGE_ORDER'], [], None, None, None, None]` | NO | Array, both \[\] and None exist, diff is \[\] vs NoneSee Request fields analysis on BCV |
| `partners__eligible_carriage_listing_split_unit_ids partners__inventory_package_ids partners__listing_id` | `[[6202], [], [], [], [], [], []]``[[266206], [108491, 108495, 108502, 108505, 111425, 112564, 112571, 112576, 112616, 112618, 113229, 113237, 113244, 113247, 113249, 115225, 115226, 120538, 120543, 125008, 125032, 139004, 139918, 152727, 158660, 203123, 205333, 205508, 210770, 210772, 286951, 442092, 620273, 670073], [], [388539, 424654, 450425, 450429, 672825, 690304, 694894], [], []]` | `[[6202], None, None, None, None, None, None]``[[266206], [108491, 108495, 108502, 108505, 111425, 112564, 112571, 112576, 112616, 112618, 113229, 113237, 113244, 113247, 113249, 115225, 115226, 120538, 120543, 125008, 125032, 139004, 139918, 152727, 158660, 203123, 205333, 205508, 210770, 210772, 286951, 442092, 620273, 670073], None, [388539, 424654, 450425, 450429, 672825, 690304, 694894], None, None]` | NO | Array, diff is \[\] vs NoneSee Request fields analysis on BCV |

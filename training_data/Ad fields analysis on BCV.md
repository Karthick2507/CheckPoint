# Ad fields analysis on BCV

## Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

## Columns Recommended for Backfill

| **Column Name** | **Type** | **Backfill?** | **Comment** |
| --- | --- | --- | --- |
| advertisement\_\_net\_price | Double | YES | Used only in LQS(31). No other references found.   On LQS query usage analysis, found multiple adhoc queries using this field. Recommend to include this column.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709110211\_509154&externalid=20260709\_110212\_00000\_xey8e](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709110211_509154&externalid=20260709_110212_00000_xey8e) |
| advertisement\_\_active\_aim\_audience\_ids | array(integer) |  YES | Used in LQS(24). No other references found.   On LQS query usage analysis, found multiple adhoc queries using this field. Recommend to include this column.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709110211\_509154&externalid=20260709\_110212\_00000\_xey8e](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709110211_509154&externalid=20260709_110212_00000_xey8e) |
| advertisement\_\_effective\_exclude\_aim\_audience\_ids | array(integer) |  YES | Used in LQS(17). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I guess.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709111818\_890627&externalid=20260709\_111819\_00212\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709111818_890627&externalid=20260709_111819_00212_4cxzk) |
| auction\_\_index | Integer |  NO | Used in LQS(17). No other references foundOn LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I guess.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709111818\_890627&externalid=20260709\_111819\_00212\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709111818_890627&externalid=20260709_111819_00212_4cxzk) |
| auction\_\_error | varchar |  NO | Used in LQS(20). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I guess. [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709113733\_239032&externalid=20260709\_113734\_00216\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709113733_239032&externalid=20260709_113734_00216_4cxzk) |
| auction\_\_bid\_to\_eur\_exchange\_rate | Double |  NO | Used in LQS(10). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I guess.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709114107\_727805&externalid=20260709\_114108\_00218\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709114107_727805&externalid=20260709_114108_00218_4cxzk) |
| candidate\_\_duration | Integer | NO | Used in LQS(20). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I think.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709115531\_134222&externalid=20260709\_115532\_00223\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709115531_134222&externalid=20260709_115532_00223_4cxzk) |
| candidate\_\_bid\_replica\_id | Integer | NO | Used in LQS(14). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Most of it were related to Event Level Validation I think.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260709\_120030\_00225\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260709_120030_00225_4cxzk) |
| candidate\_\_order\_id | bigint | YES | Used in LQS(21). No other references found  On LQS query usage analysis, found multiple adhoc queries using this field. Recommend to include this column.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709120510\_764276&externalid=20260709\_120511\_00227\_4cxzk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709120510_764276&externalid=20260709_120511_00227_4cxzk) |
| partners\_\_internal\_deal\_ids | array(array(bigint))) | NO | Used in LQS(1), Arena(1) and Insights(62). No other references found. Only two adhoc queries [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713062600\_897164&externalid=20260713\_062601\_00018\_pwixy](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713062600_897164&externalid=20260713_062601_00018_pwixy) |
| partners\_\_inbound\_listing\_ids | array(array(bigint))) | NO | Used in LQS(12). No other references found  As per Karan’s comment this field returns null every time  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708151003\_295055&externalid=20260708\_151005\_00037\_qycab](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708151003_295055&externalid=20260708_151005_00037_qycab) |
| partners\_\_audience\_segment\_max\_cpm | array(double) | YES | Used in LQS(49) and Insights(2183). Used in Arena job etl.arena2.arena\_batch\_28120064\_8298, svc-ciec-sct  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713114200\_641584](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713114200_641584) |
| partners\_\_audience\_partner\_segment\_infos | array(array(varchar))) | NO | Used in LQS(23). No other references found. Adhoc Queries.  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713115136\_055139](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713115136_055139) |
| partners\_\_geo\_visibility\_\_report\_aggregate | array(varchar)) | YES | Used in LQS(31).  No other references found.   This field is getting deprecated. |
| process\_batch\_id | varchar | YES | rename the column batch\_id to process\_batch\_id in H++ views |
| request\_\_identifier\_\_source | varchar | NO | use kafka\_msg\_key as needed. |

## Columns with Mismatched Values

### Summary

\[2026-06-28 18:39:19\] Matched transactions: 98/100  
\[2026-06-28 18:39:19\] Matched fields: 563/690 (81.60%)  
\[2026-06-28 18:39:19\] Unmatched fields: 127/690 (18.4%)


### Major Categories of Diff


1. **Timestamp Format/Timezone Differences **(1 fields)  
Timestamp representation differs between SRC and BCV (format/timezone normalization).
2. **\[\] VS. NULL / Nested Array-NULL Handling** (81 fields)  
Repeated/nested id fields show array-vs-NULL and ordering differences (e.g., \[\] vs null, \[\[...\]\] vs \[None\]).
3. **Postbid IVT / Compliance **(3 fields)  
Fields related to postbid IVT/compliance logic are mismatched and should be reviewed end-to-end.  
  

### Detailed List



| **Column Name** | **SRC Values** | **BCV Values** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| request\_\_timestamp | `2026-06-30 14:07:20` | `2026-06-30 10:07:20` | YES | BCV uses the local timezone |
| 105 fields:`request__context__profile_concrete_event_id request__context__standard_genre_ids request__context__standard_language_ids request__context__standard_iab_category_ids request__context__standard_content_viewership_profile_ids request__context__standard_sport_entity_ids request__context__video_cro_selected_yield_optimization_infos__sub_yo_id request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids request__scores__network_id request__scores__flag request__scores__score request__candidates request__soft_guaranteed_ad__ad_id request__soft_guaranteed_ad__num_competing_ads request__soft_guaranteed_ad__network_id request__soft_guaranteed_ad__entity_type request__soft_guaranteed_ad__entity_id request__guaranteed_deal_avail__internal_deal_id request__guaranteed_deal_avail__buyer_id request__decision_info__external_bridge__slot_index request__decision_info__external_bridge__status request__decision_info__inventory_protections__level request__decision_info__inventory_protections__scope request__decision_info__inventory_protections__separation request__linear_capnedit__device_id request__linear_capnedit__active_state request__linear_capnedit__tune_time request__linear_capnedit__last_activity_time request__linear_capnedit__is_dvr request__linear_capnedit__mode request__yield_optimization_ids__demand_type request__yield_optimization_ids__demand_id request__yield_optimization_ids__optimization_ids request__mpe_matcher_filters__id request__mpe_matcher_filters__bucket_id request__mpe_matcher_filters__weight` `visitor__tracked_term visitor__postal_code_id visitor__postal_code_package__network_id visitor__postal_code_package__postal_code_package_id visitor__user_segments_lookup_key` `visitor__standard_device_type_ids` `visitor__universal_iids`   `advertisement__rules__network_id` `advertisement__rules__opp_rule_id` `advertisement__rules__win_rule_id` `advertisement__measurable_concrete_event_id` `advertisement__global_advertiser_ids` `advertisement__global_brand_ids` `advertisement__variant_creative_ids` `advertisement__variant_rendition_ids` `advertisement__global_industry_ids` `advertisement__contextual_billings__segment_id` `advertisement__contextual_billings__cpm` `advertisement__ad_opportunity_rules__network_id` `advertisement__ad_opportunity_rules__rule_id` `advertisement__ad_opportunity_rules__total_opp`   `auction__impression__index` `auction__impression__slot_index` `auction__impression__equivalent_opportunity_number` `auction__impression__max_duration` `auction__impression__bid_floor` `auction__impression__bid_floor_uplift` `auction__impression__deals__impression_index` `auction__impression__deals__slot_index` `auction__impression__deals__internal_deal_id` `auction__impression__deals__auction_type` `auction__impression__deals__network_execution_ctx_index` `auction__impression__deals__reseller_index_in_slot` `auction__impression__deals__outbound_order_index` `auction__impression__deals__order_id` `auction__impression__deals__order_type` `auction__impression__deals__order_buyer_network_id` `auction__impression__deals__buyer_group_id` `auction__impression__deals__is_auction_rule` `auction__impression__deals__listing_id` `auction__impression__deals__buyers__buyer_id` `auction__impression__deals__buyers__internal_seat_id` `auction__impression__deals__bid_floor` `auction__impression__deals__bid_floor_uplift` `auction__impression__matched_inventory_package_ids`   `auction__mkpl_partner_tags__network_execution_ctx_index` `auction__mkpl_partner_tags__strategy`   `auction__bid_throttling_info__model_info__model_id` `auction__bid_throttling_info__model_info__model_flags`   `candidate__filter_reason__error` `candidate__filter_reason__slot_index` `candidate__filter_reason__error_category` `candidate__global_advertiser_ids` `candidate__global_brand_ids` `candidate__global_industry_ids` `candidate__global_agency_ids` `candidate__ortb_fwpartners__idtype` `candidate__ortb_fwpartners__idvalue` | `[]` | *(null)* | NO |  |
| `request__mrc_compliance_label` | `['OTT_CONTINUOUS_PLAY']` | *(null)* | NO | due to lacking of postbid IVT |
| `request__traffic_compliance__mrc_compliance_flag` | 3 | 1 | NO | due to lacking of postbid IVT - |
| `request__bit_flags` | `576531121047863296` | `2882374130261557248` |  | forecasting flag diff, which is also IVT related |
| `request__flags` | `136888833` | `136888897` | NO | bit-64 is different, due to lacking of postbid IVT |
| `request__is_filtered``request__traffic_type``request__backend_filtration_reason``request__client_facing_ivt_reason_flag``visitor__filtration_reason` | `True``0``16``1125899906842632``1001` | `False``2``NULL``0``NULL` | NO | postbid IVT differences. |
| `request__backend_filtration_reason` | NULL | 64 |  | Is this part of Postbid IVT? |
| `request__bid_request__auction_type` | *(null)* | `FIRST_PRICE` | NO | H++ is correct |
| `request__client_facing_ivt_reason_flag` | *(null)**(null)* | 0`1125899906842628` | NO | default to 0L in H++ |
| `visitor__filtration_reason` | *(null)* | `1001` | NO | due to lacking of postbid IVT |
| `visitor__identity_user_ids__namespace_id` | `[6]` | *(null)* | YES | Privacy Stripping related(Covered in Request) |
| `visitor__identity_user_ids__id` | `['500763:optout-6B05D281-B504-44A5-918C-8C01F5DA5472']` | *(null)* | YES | same as above |
| `visitor__identity_user_ids__authorized_network_id` `auction__impression__deals__media_buyer_id` `auction__impression__deals__trading_desk_id` `auction__impression__deals__matched_inventory_package_ids` `partners__eligible_carriage_listing_split_unit_ids` `partners__selected_yield_optimization_info_ids` `partners__selected_yo_volume_cap_ids` | `[[]]` | `[None]` | NO | Known behavior difference |
| `advertisement__has_candidate` | (null) | False | NO | H++ Default to false |
| `auction__impression__error` | `'IMPRESSION_NO_BIDS'` | \[None\] | YES | Will be fixed as part of <https://github.freewheel.tv/data/hoover-model/pull/401/files#diff-280ff11953f7efb303c6d19c47fd0a08f1ae9e3c39312936e53e49e46c76d452> |
| `auction__invite_deal_size` | `(null)` | 0 | NO | H++ Default to 0 |
| `candidate__advertisement_index` | `1` | null(for all rows) | YES | @Bhargava, Karan I see you have fixed this bug inetl.public\_test1.candidate. |
| `partners__outbound_listing_id` | `[[473273], [], None]` | `[[473273], None, None]` | NO | Can be ignore since \[\] to None conversion is acceptable |
| `partners__programmatic_exchange_rate_to_usd` | `[0.0, 1.0, 1.0]` | `[None, 1.0, 1.0]` | NO | 0.0 vs null |
| `partners__programmatic_exchange_rate_to_eur` | `[0.0, 0.874393, 0.874393]` | `[None, 0.874393, 0.874393]` | NO | Same as above |
| `partners__inventory_package_ids` | `[[461126, 464961, 516715], [], None]` | `[[461126, 464961, 516715], None, None]` | NO | \[\[\]\] to None |
| `request__hashed_key_value` | `` `2e818f634460f30a226b1e9c61719239` `` | `` `dc4e9c317c2f0f78f90c5da434ddcad2` `` | YES | @Bhargava, Karan I am still getting this issue in latest run |
| `partners__bit_flags` | `[162129586585337856, 0]` | `[18014398509481984, 0]` | YES | known difference because the FLAG is not used/ set by Hoover++ yet for adPartners. |

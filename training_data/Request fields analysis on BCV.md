# Request fields analysis on BCV

## Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

## Columns Recommended for Backfill

| **Column Name** | **Type** | **Backfill?** | **Comment** | **Status** |
| --- | --- | --- | --- | --- |
| request | varchar | YES | this field is available in H++ transaction table as a **virtual column**. just need to get it added into the request view | FIXED |
| request\_\_request\_throttling\_info\_\_model\_info\_\_model\_id | array(integer) | YES | only used in LQS for the troubleshooting of traffic shaping. better to add the entire binlog struct **request\_throttling\_info **([https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log\_Record.proto#L2127](https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log_Record.proto#L2127)) | FIXED |
| request\_\_client\_facing\_reason\_code | array(varchar) | NO | used in LQS and ETL (f\_compliance\_hourly)  this is a duplicate field to **request\_\_client\_facing\_ivt\_reason\_flag(bigint)**, will not be added back. ETL table:f\_compliance\_hourly is mainly used by IVT team, and we will change the SQL to make use of the new field instead. | - |
| request\_\_bid\_request\_\_site\_domain | varchar | YES | used in LQS(40) - this is for inbound bid request (Bidding\_Context.Bid\_Request), not the outbound, outbound bid request is stored in RTB\_Auction  source field in binlog: raw.request.bidding\_context.bid\_request.site.domain | FIXED |
| visitor\_\_user\_agent\_device\_id | bigint | NO | used in LQS(13) this binlog field is explicitly marked as not used [https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log\_Record.proto#L1299](https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log_Record.proto#L1299) | - |
| inventory\_\_asset\_chain\_\_reseller\_network\_id | array(bigint) | NO | used in LQS(7) and ETLThe ETL SQL([https://github.freewheel.tv/data/transformer/blob/d37c4d5d9ee2eb35c08a75f42ac5bf85c5814c4d/config/optimus/sql/f\_inventory\_delivered\_hourly.sql#L1246](https://github.freewheel.tv/data/transformer/blob/d37c4d5d9ee2eb35c08a75f42ac5bf85c5814c4d/config/optimus/sql/f_inventory_delivered_hourly.sql#L1246)) is not correct because there isn’t any reseller nodes in the asset/site\_section chains. In existing Hoover, different types of network chain (inventory chain, ad chain, reseller chain) are all using the same struct and that is why the columns is there even though it doesn’t really make sense on inventory. The below LQS query shows this field is always set as NULL in the inventory chain: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260628231315\_576834&externalid=20260628\_231321\_00003\_cp9gu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260628231315_576834&externalid=20260628_231321_00003_cp9gu)  In Hoover++, the struct of chains differ according to its types. This is one of the major improvements in H++ and will make the schema semantically more clear. | - |
| execution\_networks\_\_reseller\_network\_id | array(bigint) | NO | Used in Insights and LQSSimilar as above, execution\_network is also using the shared parent class for network struct in exiting Hoover, and this field has never been set any value: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260628234845\_480009&externalid=20260628\_234847\_00004\_cp9gu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260628234845_480009&externalid=20260628_234847_00004_cp9gu)Insights query should be modified | - |
| execution\_networks\_\_revenue | array(double) | NO | Used in Insights and LQSsame as above | - |
| execution\_networks\_\_content\_owner\_bidding\_revenue | array(double) | NO | Used in Insights and LQSsame as above | - |
| execution\_networks\_\_network\_is\_ad\_owner | array(boolean) | NO | Used in Insights and LQSsame as above | - |
| execution\_networks\_\_supply\_acquisition\_cost | array(double) | NO | Used in Insights and LQSsame as above | - |
| execution\_networks\_\_supply\_distribution\_cost | array(double) | NO | Used in Insights and LQSsame as above | - |
| process\_batch\_id | varchar | YES | rename the column batch\_id to process\_batch\_id in H++ views | FIXED |


## Columns with Mismatched Types

| **Column Name** | **SRC Type** | **BCV Type** | **Changes?** | **Comment** | **Staus** |
| --- | --- | --- | --- | --- | --- |
| request\_\_timestamp | timestamp(3) | timestamp(3) with time zone | YES | all timestamp in the logs are assumed to be in UTC and thus we should convert the bigint timestamp to timestamp(3) without zone infoBCV change is requiredwhen converting timestamp with timezone to timestamp(3) we should explicitly specify UTC otherwise the conversion will be based on session’s default timezone. | @Bhargava, Karan |
| execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | array(array(array(bigint))) | array(array(array(integer))) | NO | is this a typo in creating the views?  the field is defined as uint32 in protobuf ([https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log\_Record.proto#L739](https://github.freewheel.tv/core/common/blob/master/src/server/protobuf/Log_Record.proto#L739))  so should be defined as bigint instead of int (H++ schema change) | - |

## Columns with Mismatched Values

### Summary

\[2026-06-28 18:39:19\] Matched transactions: 95/100  
\[2026-06-28 18:39:19\] Matched fields: 607/668 (90.87%)  
\[2026-06-28 18:39:19\] Unmatched fields: 61/668 (9.13%)

### Major Categories of Diff

#### 1. \[\] VS. NULL

If a repeated field in protobuf is not set, it is stored as an empty array in existing hoover tables while the field is set as NULL in H++. The implementation details between Hoover and Hoover++ are highlighted as below:

Existing Hoover:

proto → avro object

  // this looks like a bug, it doesn't check if the PB field is set or not

```
List<Long> profile_concrete_event_id_list =
    new ArrayList<>(protobuf.getProfileConcreteEventIdList());
context.setProfileConcreteEventId(profile_concrete_event_id_list); 
```


raw transaction → hoover 

 // we do check it here, but this condition would always return TRUE, because it already default to \[\] from the above step

```
if (raw.getProfileConcreteEventId() != null) {
    List<Long> list = new ArrayList<>();
    raw.getProfileConcreteEventId().forEach(x -> list.add(unmask(x)));
    context.setProfileConcreteEventId(list); 
}
```


Hoover++:

```
if (!rawRequest.getProfileConcreteEventIdList().isEmpty()) {
    List<java.lang.Long> profile_concrete_event_id_list = new ArrayList<>();
    rawRequest
            .getProfileConcreteEventIdList()
            .forEach(x -> profile_concrete_event_id_list.add(Utils.unmask(x)));
    context.setProfile_concrete_event_id(profile_concrete_event_id_list);
}
```


In my opinion the existing Hoover implementation is flawed where a NULL field in PB is mistakenly converted into array\[\]. However I am open to hearing more thoughts.

#### 2. \[\[\]\] VS. \[None\]

For example:  
`[[], None, None, [23217786], None]` // SRC

`[None, None, None, [23217786], None]` // BCV

Actually the root cause for this case is exactly the same as above. The additional complexity here is we are handling the NULL values of a repeated column in a Struct, like array(array(bigint)).

If looking at the SRC(existing hoover) result, obviously it is not following a consistent way to handle NULL values and this looks like a bug. It is checking the existence of outer object to determine if the whole record of the Struct should be populated

```
if (protobuf.hasInventory()) {                    // if inventory sub-message doesn't exist
    network_execution_context.setInventory(...);  // then the whole inventory record will be null, not array[]
}         
```

 But when setting value to inner object, there isn’t a check for the existence of the field and always initiated as an array\[\]

```
// always execute, no existence check
List<Long> mapped_site_section_ids_list =
    new ArrayList<>(protobuf.getMappedSiteSectionIdsList());
inventory.setMappedSiteSectionIds(mapped_site_section_ids_list);
```

As a result of this inconsistency of logics, we see None when the outer object (the whole record) doesn’t exist while we also see \[\] being used when the outer object exist but the field itself is not set in PB.

- The whole record exist && the repeated field is populated =\> normal array with values, e.g., `[23217786]`
- The whole record exist && the repeated field is not populated =\> \[\]
- The whole record doesn’t exist =\> None

This is definitely something looks problematic and very confusing and thus I recommend we just consistently use NULL/None in H++.

#### 3. Postbid IVT

- `request__client_facing_ivt_reason_flag`
- `request__flags`
- `request__mrc_compliance_label`
- `visitor__filtration_reason`
- `request__traffic_type`


### Detailed List

| **Column Name** | **SRC Values** | **BCV Values** | **Changes?** | **Comment** | **Status** |
| --- | --- | --- | --- | --- | --- |
| `request__timestamp` | `2026-06-27 18:39:52` | `2026-06-27 14:39:52-04:00` | YES | change to use timestamp(3) in BCV | @Bhargava, Karan |
| 45 fields:`request__context__profile_concrete_event_id request__context__standard_genre_ids request__context__standard_language_ids request__context__standard_iab_category_ids request__context__standard_content_viewership_profile_ids request__context__standard_sport_entity_ids request__context__video_cro_selected_yield_optimization_infos__sub_yo_id request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids request__scores__network_id request__scores__flag request__scores__score request__candidates request__soft_guaranteed_ad__ad_id request__soft_guaranteed_ad__num_competing_ads request__soft_guaranteed_ad__network_id request__soft_guaranteed_ad__entity_type request__soft_guaranteed_ad__entity_id request__guaranteed_deal_avail__internal_deal_id request__guaranteed_deal_avail__buyer_id request__decision_info__external_bridge__slot_index request__decision_info__external_bridge__status request__decision_info__inventory_protections__level request__decision_info__inventory_protections__scope request__decision_info__inventory_protections__separation request__linear_capnedit__device_id request__linear_capnedit__active_state request__linear_capnedit__tune_time request__linear_capnedit__last_activity_time request__linear_capnedit__is_dvr request__linear_capnedit__mode request__yield_optimization_ids__demand_type request__yield_optimization_ids__demand_id request__yield_optimization_ids__optimization_ids request__mpe_matcher_filters__id request__mpe_matcher_filters__bucket_id request__mpe_matcher_filters__weight visitor__tracked_term visitor__postal_code_id visitor__postal_code_package__network_id visitor__postal_code_package__postal_code_package_id visitor__user_segments_lookup_key visitor__universal_iids visitor__standard_device_type_ids request_info__raw_brands request_info__raw_channels request__context__ab_test_item__collection_id request__context__ab_test_item__bucket_id` | `[]` | *(null)* | NO | see <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV#%5B%5D-VS.-NULL> | - |
| `request__bid_request__app_bundle` | *(null)* | *(null)* | NO | not an issue, this is due to NULL != NULL | - |
| `request__bid_request__auction_type` | *(null)* | `FIRST_PRICE` | NO | H++ is correct | - |
| `request__client_facing_ivt_reason_flag` | *(null)**(null)* | 0`1125899906842628` | NO | default to 0L in H++ @Li, Ruonan  - is this expected? | - |
| `visitor__identity_user_ids__namespace_id` | `[6]` | *(null)* | YES | @Bhargava, Karan , can you check the implementation of `applyPrivacyStripping`()? | @Bhargava, Karan |
| `visitor__identity_user_ids__id` | `['4f34587bc35290f1ea1be0874bf9ed8db97a50d2']` | *(null)* | YES | same as above | @Bhargava, Karan |
| `inventory__site_section_chain__tracked_audience_item_ids` | `[[598055, 1150753, 1154115]]` | `[None]` | YES | logic diff, need to be checked and fixed | @Wang, Yu |
| `audiences__kv_term_ids` | `[[], [], [], [], [], [645657], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [645657], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [645657, 1164335], [], [], [], [], [], [], [], [], [645657, 1164335]]` | `[[645657], [], [], [], [], [645657], [], [645657, 1164335], [645657, 1164335]]` | NO | Hoover:initiate the Audience entity for every rows in Network\_AttributesHoover++: initiate the Audience entity only when either audience\_item\_ids or kv\_term\_ids is NOT NULL, this will help to avoid the empty entities being created.`if (transactionCtx.getNetworkAttributes() != null) {     for (Map.Entry<Long, NetworkAttribute> entry :             transactionCtx.getNetworkAttributes().entrySet()) {         Long networkId = entry.getKey();         NetworkAttribute networkAttribute = entry.getValue();         if (networkAttribute.getTrackedAudienceItemIds().isEmpty()                 && networkAttribute.getNonTrackedAudienceItemIds().isEmpty()                 && networkAttribute.getKvTermIds().isEmpty()) {             continue;         }         Audience audience = new Audience();         audience.setNetwork_id(networkId);         List<Long> audienceItemIds = new ArrayList<>();         audienceItemIds.addAll(networkAttribute.getTrackedAudienceItemIds());         audienceItemIds.addAll(networkAttribute.getNonTrackedAudienceItemIds());         audience.setAudience_item_ids(audienceItemIds);         // to get non-tracked AI position         audience.setNon_tracked_start_position(networkAttribute.getTrackedAudienceItemIds().size());         audience.setFlags(networkAttribute.getAudienceFlags());         audience.setKv_term_ids(networkAttribute.getKvTermIds());         audiences.add(audience);     } }` | - |
| `audiences__audience_item_ids` | - | - | NO | same as above - only populate when there is a audience\_item\_ids or kv\_term\_ids populated | - |
| `audiences__network_id``inventory__site_section_chain__tracked_audience_item_ids` | - | - | YES | Needs further investigation as to why it’s not matching. | - |
| `execution_networks__mapped_asset_ids``execution_networks__mapped_site_section_ids``execution_networks__inventory_package_ids``inventory__site_section_chain__inventory_package_ids``inventory__asset_chain__inventory_package_ids``visitor__identity_user_ids__authorized_network_id` | `[[]]` | `[None]` | NO | see <https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV#%5B%5B%5D%5D-VS.-%5BNone%5D> | - |
| `request__flags` | `136892929` | `136892993` | NO | bit-64 is different, due to lacking of postbid IVT | - |
| `request__context__distributor_video_asset_id` | 0 | *(null)* | NO | H++ has a check `hasAssetId()` before reading the PB field, which is better | - |
| `request__mrc_compliance_label` | `['OTT_CONTINUOUS_PLAY']` | *(null)* | NO | due to lacking of postbid IVT - @Li, Ruonan | - |
| `request__traffic_compliance__mrc_compliance_flag` | 3 | 1 | NO | due to lacking of postbid IVT - @Li, Ruonan | - |
| `visitor__filtration_reason` | *(null)* | `1001` | NO | due to lacking of postbid IVT - @Li, Ruonan | - |
| `request__traffic_type` | 0 | 2 | NO | due to lacking of postbid IVT - @Li, Ruonan | @Li, Ruonan |
| `request__is_filtered` | True | False | NO | due to lacking of postbid IVT - @Li, Ruonan | - |
| `request__bit_flags` | `576531121047863296` | `2882374130261557248` |  | forecasting flag diff, which is also IVT related |  |
| `request__backend_filtration_reason` | NULL | 64 |  |  | @Li, Ruonan |
| `request__hashed_key_value` | `684245d8a7b7163fceac09b6cfa59074` | `86fccaed1b853da74651e10551a5fceb` |  | is this also due to privacy handling? | @Bhargava, Karan |

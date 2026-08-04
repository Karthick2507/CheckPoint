# Re\-Check Ack Table \- 7/21/2026

# Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

# Columns Recommended for Backfill

| **Column Name** | **Type** | **Backfill?** | **Comment** | **Status** |
| --- | --- | --- | --- | --- |
| request\_\_context\_\_extracted\_key\_value | varchar | NO | FULL key\_value list is stored in Hoover. No need to store the extracted one. |  |
| request\_\_context\_\_extracted\_key\_value\_\_\_fw\_dbp | varchar | NO | FULL key\_value list is stored in Hoover. No need to store the extracted one. |  |
| request\_\_context\_\_extracted\_key\_value\_\_\_fw\_lto | varchar | NO | FULL key\_value list is stored in Hoover. No need to store the extracted one. |  |
| request\_\_identifier\_\_source | varchar | NO | binlog + kafka thing. I don’t think needed. Reconfirm with @Wang, YuUsed in `Arena`Update → `this one, and also the similar field on ack should not be included. kafka_msg_key should have sufficient info for debugging` | `fw_ads_binary_log#650#1784623728526592475-e33b5-1784623728580-3382-10c3303e#20260721-080000` |
| request\_\_client\_facing\_reason\_code | array(varchar) | NO | used in LQS and ETL (f\_compliance\_hourly)this is a duplicate field to **request\_\_client\_facing\_ivt\_reason\_flag(bigint)**, will not be added back. ETL table:f\_compliance\_hourly is mainly used by IVT team, and we will change the SQL to make use of the new field instead. |  |
| request\_\_bid\_request\_\_impression\_\_deal\_\_floor | array(array(real)) | YES | Real → Double | \<insert PR from TVP-75307 here\> |
| inventory\_\_asset\_chain\_\_reseller\_network\_id | array(bigint) | NO | All values NULL[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021731\_260302&externalid=20260722\_021736\_00046\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021731_260302&externalid=20260722_021736_00046_ptdgd) |  |
| inventory\_\_asset\_chain\_\_supply\_source | array(integer) | NO | All values 0/ null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021809\_416192&externalid=20260722\_021813\_00047\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021809_416192&externalid=20260722_021813_00047_ptdgd) |  |
| inventory\_\_asset\_chain\_\_sales\_channel | array(integer) | NO | All values 0/ null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021832\_696973&externalid=20260722\_021836\_00048\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021832_696973&externalid=20260722_021836_00048_ptdgd) |  |
| inventory\_\_asset\_chain\_\_floor\_price | array(double) | NO | All values 0/ null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021847\_343734&externalid=20260722\_021851\_00049\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021847_343734&externalid=20260722_021851_00049_ptdgd) |  |
| inventory\_\_asset\_chain\_\_geo\_visibility\_\_report\_aggregate | array(varchar) | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021919\_295641&externalid=20260722\_021924\_00050\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021919_295641&externalid=20260722_021924_00050_ptdgd) |  |
| inventory\_\_site\_section\_chain\_\_site\_group\_id | array(bigint) | YES | Maybe same as site\_section\_group\_id?[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722021920\_269637&externalid=20260722\_021925\_00051\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722021920_269637&externalid=20260722_021925_00051_ptdgd)@Wang, Yu can you help confirm? | \<insert PR from TVP-75307 here\> |
| inventory\_\_site\_section\_chain\_\_floor\_price | array(double) | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722022656\_258973&externalid=20260722\_022700\_00053\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722022656_258973&externalid=20260722_022700_00053_ptdgd) |  |
| ack\_\_ad\_unit\_id | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722022736\_831713&externalid=20260722\_022740\_00054\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722022736_831713&externalid=20260722_022740_00054_ptdgd) |  |
| ack\_\_identifier\_\_source | varchar | NO | Similar as request\_\_indentifier\_source. Needed?`this one, and also the similar field on ack should not be included. kafka_msg_key should have sufficient info for debugging` |  |
| ack\_\_metrics | varchar | NO | Virtual column.Not all acks have same schema; unable to UNION |  |
| ack\_\_metrics\_\_avails\_event\_count | bigint | NO | All metrics in Hoover++ already have this multiplied. Should we still add?@Wang, YuUsed by Insights & ETL heavily though |  |
| ack\_\_metrics\_\_ad\_net\_avail | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722022938\_350381](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722022938_350381) |  |
| ack\_\_metrics\_\_ad\_gross\_avail | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023004\_776114&externalid=20260722\_023008\_00057\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023004_776114&externalid=20260722_023008_00057_ptdgd) |  |
| ack\_\_metrics\_\_ad\_unconstrained\_gross\_avail | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023100\_244634&externalid=20260722\_023104\_00058\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023100_244634&externalid=20260722_023104_00058_ptdgd) |  |
| advertisement\_\_fill\_rate | double | YES | Only 17 LQS queries.Add value. | \<insert PR from TVP-75307 here\> |
| advertisement\_\_billable\_rate\_denominator\_event\_id | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023146\_992572&externalid=20260722\_023150\_00059\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023146_992572&externalid=20260722_023150_00059_ptdgd) |  |
| advertisement\_\_provider\_measured\_event\_id | bigint | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023240\_802440&externalid=20260722\_023243\_00061\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023240_802440&externalid=20260722_023243_00061_ptdgd) |  |
| advertisement\_\_original\_bidding\_price | double | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023244\_318738&externalid=20260722\_023247\_00062\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023244_318738&externalid=20260722_023247_00062_ptdgd) |  |
| advertisement\_\_data\_provider\_id | array(bigint) | YES |  | \<insert PR from TVP-75307 here\> |
| advertisement\_\_net\_price | double | YES |  | \<insert PR from TVP-75307 here\> |
| advertisement\_\_active\_aim\_audience\_ids | array(integer) | NO | AIM audience feature; later phase. |  |
| advertisement\_\_effective\_exclude\_aim\_audience\_ids | array(integer) | NO | AIM audience feature; later phase. |  |
| advertisement\_\_geo\_as\_audience\_segments\_id\_pks | array(integer) | YES | Used by Vulcan team. | \<insert PR from TVP-75307 here\> |
| advertisement\_\_matched\_geo\_ids | array(bigint) | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023523\_354339&externalid=20260722\_023526\_00066\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023523_354339&externalid=20260722_023526_00066_ptdgd) |  |
| advertisement\_\_matched\_postal\_code\_ids | array(bigint) | YES |  | \<insert PR from TVP-75307 here\> |
| advertisement\_\_matched\_postal\_code\_package\_ids | array(bigint) | YES |  | \<insert PR from TVP-75307 here\> |
| advertisement\_\_matched\_region\_ids | array(bigint) | YES |  | \<insert PR from TVP-75307 here\> |
| advertisement\_\_candidate\_index | integer | YES |  | \<insert PR from TVP-75307 here\> |
| slot\_\_carriage\_listing\_split\_unit\_id | bigint | YES | Already present in Hoover++; update BCVs | \<insert PR from TVP-75307 here\> |
| partners | array(varchar) | NO | Virtual column.Not all partners have same schema; unable to UNION |  |
| partners\_\_inbound\_listing\_ids | array(array(bigint)) | NO | All values NULL[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722023842\_371144&externalid=20260722\_023845\_00072\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722023842_371144&externalid=20260722_023845_00072_ptdgd) |  |
| partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_flags | array(array(array(bigint))) | LATER | AIM feature; later phase. |  |
| partners\_\_supply\_priority | array(integer) | YES | Already present in Hoover++; update BCVs | \<insert PR from TVP-75307 here\> |
| partners\_\_acquired\_supply\_type | array(integer) | YES | Already present in Hoover++; update BCVs | \<insert PR from TVP-75307 here\> |
| candidate\_\_duration | integer | YES |  | \<insert PR from TVP-75307 here\> |
| candidate\_\_cch\_key | varchar | YES |  | \<insert PR from TVP-75307 here\> |
| candidate\_\_trust\_id | varchar | NO | All values null[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722024110\_677308&externalid=20260722\_024114\_00076\_ptdgd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722024110_677308&externalid=20260722_024114_00076_ptdgd) |  |
| auction\_\_index | integer | YES |  | \<insert PR from TVP-75307 here\> |
| auction\_\_ifa\_type | varchar | YES |  | \<insert PR from TVP-75307 here\> |
| auction\_\_buyer\_platform\_url\_id | bigint | YES | Already present in Hoover++;update BCVs | \<insert PR from TVP-75307 here\> |
| auction\_\_market\_integration\_type | varchar | YES |  | \<insert PR from TVP-75307 here\> |
| auction\_\_dynamic\_floor\_price\_algorithm | varchar | YES |  | \<insert PR from TVP-75307 here\> |
| auction\_\_third\_party\_identifier\_ids | array(integer) | YES |  | \<insert PR from TVP-75307 here\> |
| auction\_\_device\_ip | varchar | YES |  | \<insert PR from TVP-75307 here\> |
| ads\_in\_slot\_\_advertisement\_\_geo\_as\_audience\_segments\_id\_pks | array(array(integer)) | YES |  | \<insert PR from TVP-75307 here\> |
| ads\_in\_slot\_\_auction\_\_ifa\_type | array(varchar) | YES |  | \<insert PR from TVP-75307 here\> |
| ads\_in\_slot\_\_auction\_\_third\_party\_identifier\_ids | array(array(integer)) | YES |  | \<insert PR from TVP-75307 here\> |
| ads\_in\_slot\_\_candidate | array(varchar) | NO | Virtual column; UNION doesn’t work otherwise. |  |
| ads\_in\_slot\_\_candidate\_\_duration | array(integer) | YES |  | \<insert PR from TVP-75307 here\> |
| ads\_in\_slot\_\_partners | array(array(varchar)) | NO | Virtual column; UNION doesn’t work otherwise. |  |
| ads\_in\_slot\_\_partners\_\_bidding\_up\_revenue | array(array(double)) | YES |  |  |
| ads\_in\_slot\_\_partners\_\_internal\_deal\_ids | array(array(array(bigint))) | NO | NULL values only (only set for Auctions)[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260723045609\_343312&externalid=20260723\_045613\_00078\_7q5va](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260723045609_343312&externalid=20260723_045613_00078_7q5va) |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos | array(array(array(varchar))) | LATER | AIM feature; later phase |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | array(array(array(array(integer)))) | LATER | AIM feature; later phase |  |
| ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_aggregate | array(array(varchar)) | NO | geo\_visiblity deprecated[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260723045713\_198053&externalid=20260723\_045716\_00079\_7q5va](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260723045713_198053&externalid=20260723_045716_00079_7q5va)Values are `null` anyways. |  |


# Recommend Excluded

| **Column Name** | **Size (TiB)** | **Usage: ETL** | **usage: SOS** | **Usage: Insights** | **Usage: Arena** | **Usage: LQS** | **Usage: CP** | **Usage: AF** | **Usage: Others** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| request\_\_identifier\_\_source | 0.53 |  |  |  |  | 48 |  |  |  |
| ack\_\_identifier\_\_source | 0.73 |  |  |  | 1 | 17 |  |  |  |

# Columns with Mismatched

Summary:  
Matched transactions: 100/100  
Matched fields: 1102/1567 (70.32%)  (440 (exact) + 662 (global equivalent null)  
Globally Equivalent Fields: 662 (42.2%)  
Unmatched fields: 465 (29.7%)

## Columns with Mismatches

| **Column Name** | **SRC Values** | **BCV Values** | **Changes?** | **Comment** | **Status** |
| --- | --- | --- | --- | --- | --- |
| ### `request__flags` | `1214529537` | `1080311809` | NO | SRC values include PRIMARY\_REQUEST flag; this is a known diff as it’s set by Matcher and is not used for any downstream querying. |  |
| ### `request__bid_request__auction_type` | NULL | `FIRST_PRICE` | NO | Hoover++ is correct |  |
| ### `inventory__asset_chain__network_id` | NULL | `[535263]` | ENHANCED DATA CAPABILITY | Shared entity of inventory across all tables; Hoover++ correct. | @Wang, Yu thoughts? |
| ### `inventory__asset_chain__role` | NULL | `[CRO]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__entity_source` | NULL | `[inventory]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__bit_flags` | NULL | `[0]` | NO | null vs 0. No changes required. |  |
| ### `inventory__asset_chain__content_owner_network_id` | NULL | `[535263]` | ENHANCED DATA CAPABILITY | Shared entity of inventory across all tables; Hoover++ correct. |  |
| ### `inventory__asset_chain__distributor_network_id` | NULL | `[535082]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__asset_id` | NULL | `[475146354, 475162482]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__site_section_id` | NULL | `[24047742, 1779684]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__series_id` | NULL | `1663131150, 1663272435]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__site_id` | NULL | `[1270876]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__asset_group_id` | NULL | `[1309893976]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__asset_group_ids` | NULL | `[[1309893976]]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__site_section_group_ids` | NULL | `[[672272, 764545, 764546, 764547, 771583, 771584, 771585, 771586], [675481]]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__airing_channel_id` | NULL | `[-1, -1]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__airing_id` | NULL | `[-1, -1]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__postal_code_package_id` | NULL | `[[13071], None]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__visible_concrete_event_id` | NULL | `[[47]]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__tracked_audience_item_ids` | NULL | `[[1448180], None]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__network_execution_ctx_index` | NULL | `[0, 35]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__inventory_package_ids` | NULL | `[[536658, 672163, 694899, 694900]]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_state_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_state_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_state_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_city_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_city_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_city_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_zip_code_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_zip_code_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_zip_code_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_dma_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_dma_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__geo_dma_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__user_agent_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__user_agent_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__user_agent_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__visitor_custom_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__visitor_custom_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__visitor_custom_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__device_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__device_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__device_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__ip_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__ip_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__ip_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__third_party_user_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__third_party_user_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__third_party_user_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__key_value_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__key_value_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__asset_chain__key_value_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__site_section_chain__network_id` | NULL | `[535263]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__entity_source` | NULL | `[inventory]` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `inventory__site_section_chain__role` | NULL | `[CRO]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__bit_flags` | NULL | `[0]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__content_owner_network_id` | NULL | `[535263]`\` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__distributor_network_id` | NULL | `[535263]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__asset_id` | NULL | `[475160425]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__site_section_id` | NULL | `[1779684]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__series_id` | NULL | `[1604282921]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__site_id` | NULL | `[614655]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__asset_group_id` | NULL | `[1288627473]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__asset_group_ids` | NULL | `[[1309893976]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__site_section_group_ids` | NULL | `[[1257658]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__airing_channel_id` | NULL | `[-1]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__airing_id` | NULL | `[-1]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__postal_code_package_id` | NULL | `[[2844, 2864, 2886, 4262, 5732, 6261]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__visible_concrete_event_id` | NULL | `[[47]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__tracked_audience_item_ids` | NULL | `[[1279323, 1311489, 1311490, 1311491, 1311492, 1311493, 1311494, 1311495, 1311496, 1406353, 1407012, 1407147, 1407149, 1407155, 1407157, 1407158, 1407159, 1407160, 1407161, 1407162, 1407164, 1407165, 1407166, 1407168, 1407169, 1407172, 1407173, 1407174, 1407207, 1407211, 1407212, 1407213, 1407214, 1407215, 1407901, 1407904, 1407907, 1407908, 1407909, 1407910, 1407911, 1407934, 1407935, 1407936, 1408293, 1408295, 1408296, 1408298, 1408301, 1408303, 1408311, 1408312, 1408364, 1408365, 1408369, 1408374, 1408375, 1408378, 1408380, 1408382, 1408436, 1408437, 1408438, 1408441, 1408442, 1408445, 1416220, 1421373, 1457798, 1476776, 1476777, 1476778, 1480746, 1480754, 1482135, 1484750, 1485299, 1485357, 1486117, 1486118, 1486527, 1492870]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__network_execution_ctx_index` | NULL | `[0]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__inventory_package_ids` | NULL | `[[536658, 672163, 694899, 694900]]` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_state_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_state_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_state_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_city_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_city_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_city_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_zip_code_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_zip_code_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_zip_code_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_dma_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_dma_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__geo_dma_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__user_agent_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__user_agent_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__user_agent_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__visitor_custom_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__visitor_custom_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__visitor_custom_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__device_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__device_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__device_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__ip_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__ip_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__ip_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__third_party_user_id_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__third_party_user_id_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__third_party_user_id_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__key_value_visibility__targetable` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__key_value_visibility__report_aggregate` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| `inventory__site_section_chain__key_value_visibility__report_event` | NULL | `['NO_VISIBILITY', 'FULL_VISIBILITY']` | ENHANCED DATA CAPABILITY | same as above |  |
| ### `ack__metrics__cpx_revenue_ratio` | `1.0` | `2.0` | CONFUSED | Double check why it’s double for this transaction`1783677906120276394`Code logic seems same; marking as `KNOWN DIFF` to come back to later. |  |
| ### `ack__cpx_derived_abstract_event_id` | `10268` | `-5692549928996296676` | YES | Needs to be unmasked\<insert PR from TVP-75307 here\> |  |
| ### `ack__cpx_derived_concrete_event_id` | `47` | `-5764607523034234833` | YES | Needs to be unmasked\<insert PR from TVP-75307 here\> |  |
| ### `advertisement__rules__opp_rule_id` | NULL | `[[]]` | NO | NULL vs \[\] diff |  |
| ### `advertisement__rules__win_rule_id` | NULL | `[[]]` | NO | NULL vs \[\] diff |  |
| ### `slot__original_max_ads` | `1` | `NULL` | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__raw_max_duration` | `30` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__raw_max_ads` | `1` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__down_reseller_index` | `[23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, None, None, None, None, None, None, None, None, None, None, None, None, None, 22]` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__order_id` | `[342859, 296108, 375042, 390706, 392357, 402969, 407545, 381771, 465189, 630401, 392451]` | `[None, None, None, None, None, None, None, None, None, None, None]` | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__listing_id` | `[[240516], [340183], [631410], [708238], [168215], [219324], [689973], [348687], [280469], [327307], [348691], [685824], [521953], [328966], [427216], [685825], [700480], [169201], [171089], [178747], [230561], [406928], [225408], [], [], [], [], [], [], [], [], [], [], [], [], [], [605799]]` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__order_type` | `['MARKETPLACE_ORDER']` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__order_transaction_type` | `[GUARANTEED]` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__order_priority` | \[`'PRIORITY_ABOVE_GUARANTEED'`\] | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__unified_priority__priority_tier` | `'TIER_1', 'TIER_1'` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__unified_priority__sub_priority_value` | `[25, 25, 25]` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__active_aim_audience_ids` | `[], [], [],` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__effective_exclude_aim_audience_ids` | `[], [], [], [],` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `slot__outbound_order__aim_audience_targeting_expression` | `['1182293']` | NULL | YES | Needs to be set for ad ack level.\<insert PR from TVP-75307 here\> |  |
| ### `partners__rule_ext_id` | `[-1, -1]` | NULL | NO | All values are just -1. What does this even solve?@Wang, Yu[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722214408\_584776&externalid=20260722\_214411\_00313\_pw3w5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722214408_584776&externalid=20260722_214411_00313_pw3w5) |  |
| ### `partners__listing_id` | `[[165051, 168215, 169201, 171089, 178747, 219324, 225408, 230561, 232969, 240516, 280469, 296510, 327307, 328966, 340183, 348687, 348691, 406928, 427216, 521953, 605799, 616875, 631410, 685824, 685825, 689973, 700480, 708238, 232125, 326983, 346751, 372537, 416295, 699818], None]` | NULL | YES | \<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__avails` | `[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]` | `[1]` | YES | \<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__unfilled_avails` | `[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | `[1]` | YES | \<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__avails_in_played_slot` | `[4]``[1, 1]` | `[0]``[100, 100]` | YES | Slot Impression 0 causes 0 as a value.In played slot metrics in Hoover++ already have magnifier applied. |  |
| ### `partners__avails_category__unfilled_avails_in_played_slot` | `[1, 0]` | `[100, 0]` | NO | In played slot metrics in Hoover++ already have magnifier applied. |  |
| ### `partners__avails_category__unconstrained_avails_in_played_slot` | `[1, 0]` | `[100, 0]` | NO | In played slot metrics in Hoover++ already have magnifier applied. |  |
| ### `partners__avails_category__raw_total_avails_in_played_slot` | `[1, 1]` | `[100, 100]` | NO | In played slot metrics in Hoover++ already have magnifier applied. |  |
| ### `partners__avails_category__total_avails_in_played_slot` | `[4]` | `[0]` | YES | Double check why value is diff. |  |
| ### `partners__avails_category__total_unfilled_avails_in_played_slot` | `[1, 0]` | `[100, 0]` | NO | In played slot metrics in Hoover++ already have magnifier applied. |  |
| ### `partners__avails_category__opportunity_in_played_slot` | `[2]` | `[0]` | YES | Double check why value is diff. - no slotImpression makes value 0 \<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__raw_opportunity_in_played_slot` | `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]` | `[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]` | YES | Missing setter\<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__slot_opp_avails_in_played_slot` | `[1]` | `[0]` | YES | Why is the value diff?; same as `opportunity_in_played_slot`\<insert PR from TVP-75307 here\> |  |
| ### `partners__avails_category__vod_programmer_total_avails` | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | *(null)* | NO | Values are always 0. Do we even need to set?@Wang, Yu`NULL is fine here.` |  |
| ### `partners__avails_category__supply_avails` | `[1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]` | `[1, None, None, None, None, None, None, None, 1, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]` | YES |  | @Marino Johnson, Daniel some more diffs with new avails metrics |
| ### `partners__eligible_outbound_orders__avails_category__unconstrained_avails` | `[[0, 0, 0, 0, 1, 0, 0], [1], [1], [], [], [], [], [], [0, 1, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__market_avails` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__ssp_avails` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__unfilled_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__unconstrained_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__raw_total_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__market_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__ssp_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__total_avails` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__total_unfilled_avails` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__total_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__total_unfilled_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__opportunity_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__raw_opportunity_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__slot_opp_avails_in_played_slot` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__avails_category__remaining_avails` | `[[None, None, None, None, None, None, None, None, None, None, None], [], [], [], [], [], [], [], [None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None], [None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [None], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]` | NULL | NO | All values are `None`. Should we even add?@Wang, Yu |  |
| ### `partners__eligible_outbound_orders__avails_category__vod_programmer_total_avails` | `[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [], [], [], [], [], [], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [], [], [], [], [], [], [0], [0, 0, 0, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]` | NULL | NO | Values are all `0`. Should we even add?@Wang, Yu`let’s leave it as is since I think this won’t cause any diff in reporting result on avails` |  |
| ### `partners__eligible_outbound_orders__avails_category__distinct_inventory_avails` | `[[None, None, None, None, None, None, None, None, None, None, None], [], [], [], [], [], [], [], [None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None], [None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [None], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]` | NULL | NO | Values are all `None`. Should we add? @Wang, Yu |  |
| ### `partners__eligible_outbound_orders__avails_category__inventory_avails` | `[[None, None, None, None, None, None, None], [None], [None], [], [], [], [], [], [None, None, None, None], [], [], [], [], []]` | NULL | NO | Values are all `None`. Should we add? @Wang, Yu |  |
| ### `partners__eligible_outbound_orders__avails_category__raw_inventory_distinct_avails_in_played_slot` | `[[None, None, None, None, None, None, None], [None], [None], [], [], [], [], [], [None, None, None, None], [], [], [], [], []]` | NULL | NO | Values are all `None`. Should we add? @Wang, Yu |  |
| ### `partners__eligible_outbound_orders__count_true_avails_as_booked` | `[[False, False, False, False, False, False, False, False, False, False, False], [], [], [], [], [], [], [], [False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False], [False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [False], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]` | NULL | YES | @Bhargava, Karan to add in. |  |
| ### `partners__eligible_outbound_orders__ad_filling_status__available_duration` | `[[120, 120, 120, 120, 120, 120, 120], [120], [120], [], [], [], [], [], [120, 120, 120, 120], [], [], [], [], []]` | NULL | YES |  |  |
| ### `partners__eligible_outbound_orders__ad_filling_status__filled_duration` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | NULL | NO |  |  |
| ### `partners__eligible_outbound_orders__ad_filling_status__default_unfilled_opp` | `[[None, None, None, None, None, None, None], [None], [None], [], [], [], [], [], [None, None, None, None], [], [], [], [], []]` | NULL | YES | @Bhargava, Karan to add in. |  |
| ### `partners__eligible_outbound_orders__ad_filling_status__initial_filled_ad_num` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | *(null)* | YES | @Bhargava, Karan to add in. |  |
| ### `partners__eligible_outbound_orders__ad_filling_status__initial_filled_duration` | `[[0, 0, 0, 0, 0, 0, 0], [0], [0], [], [], [], [], [], [0, 0, 0, 0], [], [], [], [], []]` | *(null)* | YES | @Bhargava, Karan to add in. |  |
| ### `partners__network_execution_ctx_index` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]` | NULL | YES | BCV doesn’t have value set. Fix |  |
| ### `partners__network_is_ad_owner` | `[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]` | NULL | NO | Slot level; this is an ad level metric. |  |
| ### `partners__network_is_extra_item_owner` | `[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]` | NULL | NO | same as above |  |
| ### `partners__deal_awareability` | `[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]` | NULL | MAYBE | same as above |  |
| ### `partners__demand_dim_awareability` | `[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]` | NULL | MAYBE | same as above |  |
| ### `partners__sales_channel` | `0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` | *(null)* | MAYBE | same as above |  |
| ### `partners__programmatic_exchange_rate_to_usd` | `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]` | *(null)* | MAYBE | same as above |  |
| ### `partners__programmatic_exchange_rate_to_eur` | `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]` | *(null)* | MAYBE | same as above |  |
| ### `partners__outbound_exchange_order_ids` | `[None, None, None]` | `[4211, None, None]` | YES | There are 2 fieldsexchange\_order\_id → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722230828\_430952&externalid=20260722\_230832\_00359\_pw3w5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722230828_430952&externalid=20260722_230832_00359_pw3w5)exchange\_order\_ids → all values NULL[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260722230845\_415084&externalid=20260722\_230849\_00360\_pw3w5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260722230845_415084&externalid=20260722_230849_00360_pw3w5)Align with outbound\_exchange\_order\_ids; i.e NULL |  |
| ### `partners__audience_segment_max_cpm` | `[2.5, None]` | *(null)* | LATER | AIM feature most likely |  |
| ### `partners__audience_partner_segment_infos__audience_partner_id` | `[[512025], None]` | *(null)* | LATER | AIM feature most likely |  |
| ### `partners__audience_partner_segment_infos__max_cpm` | `[[2.5], None]` | *(null)* | LATER | AIM feature most likely |  |
| ### `partners__audience_partner_segment_infos__matched_segments__id` | `[[[135484492]], None]` | *(null)* | LATER | AIM feature most likely |  |
| ### `partners__audience_partner_segment_infos__matched_segments__cpm` | `[[[2.5]], None]` | *(null)* | LATER | AIM feature most likely |  |
| ### `candidate__order_id` | `283420` | *(null)* | YES | This is the same bug as the Ad BCV. Should be fixed in both together. |  |
| ### `auction__ab_test_items__collection_id` | `[42, 90, 174, 3282740]` | *(null)* | YES | Ad Candidate Auction does not set this field. Needs to be fixed. |  |
| ### `auction__ab_test_items__bucket_id` | `[119, 298, 496, 3282962]` | *(null)* | YES | Ad Candidate Auction does not set this field. Needs to be fixed. |  |
| `ads_in_slot_*` | `NULL` | \<populated\> | YES | On ad ack level, this should be `NULL` Need to update BCV |  |
|  |  |  |  |  |  |

# Reference

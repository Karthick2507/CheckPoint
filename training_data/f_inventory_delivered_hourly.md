# f\_inventory\_delivered\_hourly

## New Diffs

|  | **Column Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | network\_id | NO | SQL CHECK + REVALIDATION | since all the diffs are \> in stage than in control a recheck of the SQL + re-validation is needed. Alongside this, if there are still diffs, we need to investigate why. |
| 2 | asset\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 3 | series\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 4 | asset\_group\_ids | NO | SQL CHECK + REVALIDATION | same as above |
| 5 | site\_section\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 6 | site\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 7 | site\_section\_group\_ids | NO | SQL CHECK + REVALIDATION | same as above |
| 8 | airing\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 9 | channel\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 10 | break\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 11 | ad\_unit\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 12 | tracked\_audience\_item\_ids | NO | SQL CHECK + REVALIDATION | same as above |
| 13 | postal\_code | NO | SQL CHECK + REVALIDATION | same as above |
| 14 | postal\_code\_package\_ids | NO | SQL CHECK + REVALIDATION | same as above |
| 15 | user\_city\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 16 | user\_dma\_code | NO | SQL CHECK + REVALIDATION | same as above |
| 17 | standard\_brand\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 18 | inbound\_order\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 19 | outbound\_order\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 20 | outbound\_listing\_ids | NO | SQL CHECK + REVALIDATION | same as above |
| 21 | profile\_id | NO | SQL CHECK + REVALIDATION | same as above |
| 22 | **video\_starts** | NO | SQL CHECK + REVALIDATION | same as above |
| 23 | **break\_starts** | NO | SQL CHECK + REVALIDATION | same as above |
| 24 | **avails** | NO | SQL CHECK + REVALIDATION | same as above |
| 25 | **unconstrained\_avails** | NO | SQL CHECK + REVALIDATION | same as above |
| 26 | **ad\_views** | NO | SQL CHECK + REVALIDATION | same as above |
| 27 | **no\_ad\_views** | NO | SQL CHECK + REVALIDATION | same as above |
| 28 | **no\_clicks** | NO | SQL CHECK + REVALIDATION | same as above |
| 29 | **first\_quartile** | NO | SQL CHECK + REVALIDATION | same as above |
| 30 | **middle\_quartile** | NO | SQL CHECK + REVALIDATION | same as above |
| 31 | **third\_quartile** | NO | SQL CHECK + REVALIDATION | same as above |
| 32 | **complete\_quartile** | NO | SQL CHECK + REVALIDATION | same as above |
| 33 | **can\_quartile** | NO | SQL CHECK + REVALIDATION | same as above |
| 34 | **ad\_mute** | NO | SQL CHECK + REVALIDATION | same as above |
| 35 | **ad\_unmute** | NO | SQL CHECK + REVALIDATION | same as above |
| 36 | **ad\_pause** | NO | SQL CHECK + REVALIDATION | same as above |
| 37 | **total\_avails** | NO | SQL CHECK + REVALIDATION | same as above |
| 38 | **total\_unfilled\_avails** | NO | SQL CHECK + REVALIDATION | same as above |
| 39 | **opportunity** | NO | SQL CHECK + REVALIDATION | same as above |
| 40 | **outbound\_avails** | NO | SQL CHECK + REVALIDATION | removed slot\_impression multiplied to the outbound\_opportunity and could able to match |
| 41 | **outbound\_opportunity** | NO | SQL CHECK + REVALIDATION | removed slot\_impression multiplied to the outbound\_opportunity and could able to match |
| 42 | **request\_count** | NO | SQL CHECK + REVALIDATION | added idx filter and able to match |

---


## Validation findings

- Removed reseller\_id, geo\_visibility since it’s not available in h++
- Removed process\_batch\_id, bit\_flag as the known issue
- added ‘idx' filter to request\_count and resolved
- updated ack\_entity\_type and most of the dimensions and few metrics got matched
- removed slot\_impression multiplier and could able to match outbound metrics
- updated `*.ack.flags & 256 = 0` and matched video\_starts and other metrics like **\*\_quartile **but revenue metrics have mismatch when adding the flags(eg. result below)

**sql with \*ack.flags & 256 = 0, idx filter, ack\_entity\_type**

```sql
%sql
CREATE TABLE IF NOT EXISTS fw1_stg.spandian.f_inventory_delivered_hourly_stage AS
select 
cast(date_format(date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id,
coalesce(partner.network_id, -1) as network_id,
coalesce(partner.content_owner_network_id,-1) as content_owner_id,
coalesce(partner.distributor_network_id, -1) as distributor_id,
--coalesce(partner.reseller_network_id,-1) as reseller_id,
cast(-1 as bigint)  as reseller_id,
coalesce(request.context.tv_network_id,-1) as tv_network_id,
coalesce(partner.role,"") as  transaction_type,
coalesce(ad_ack_ctx.ack.traffic_type,0) as traffic_type,
coalesce(partner.bit_flags, cast(0 as bigint))+ coalesce(ad_ctx.ad.bit_flags, cast(0 as bigint))+ coalesce(request.bit_flags, cast(0 as bigint))+ coalesce(ad_ack_ctx.ack.bit_flags, cast(0 as bigint))                    as bit_flag,
coalesce(partner.asset_id,-1) as asset_id,
coalesce(partner.series_id,-1) as series_id,
coalesce(partner.asset_group_ids, array())  as asset_group_ids,
coalesce(partner.site_section_id, -1)  as site_section_id,
coalesce(partner.site_id, -1)                    as site_id,
coalesce(partner.site_section_group_ids, array())  as site_section_group_ids,
coalesce(partner.airing_id, -1)                   as airing_id,
coalesce(partner.airing_channel_id, -1)           as channel_id,
coalesce(partner.break_id, -1)                    as break_id,
coalesce(slot_ctx.slot.time_position_class, "Unknown") as time_position_class,
ad_ctx.ad.ad_delivery_method as delivery_method,
IF(partner.network_is_extra_item_owner, coalesce(ad_ctx.ad.ad_unit_id, -1), -1) as ad_unit_id,
coalesce(visitor.platform_group, "-1")                                      as platform_group,
--coalesce(partner.geo_visibility.report_aggregate, "FULL_VISIBILITY")         as geo_visibility,
"" as geo_visibility,
coalesce(partner.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility,
coalesce(partner.tracked_audience_item_ids, array()) as tracked_audience_item_ids,
coalesce(visitor.postal_code, "-1") as postal_code,
coalesce(partner.postal_code_package_id, array()) as postal_code_package_ids,
coalesce(visitor.city_id, -1)                          as user_city_id,
coalesce(visitor.state_id, -1)                       as user_state_id,
coalesce(visitor.dma_code, -1)                       as user_dma_code,
coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint)) as user_country_id,
coalesce(visitor.platform_browser_id, cast(-1 as bigint))        as delivered_platform_browser_id,
coalesce(visitor.platform_device_id, cast(-1 as bigint))         as delivered_platform_device_id,
coalesce(visitor.platform_os_id, cast(-1 as bigint))             as delivered_platform_os_id,
coalesce(visitor.operator_zone_id, cast(-1 as bigint))           as operator_zone_id,
coalesce(request.delivery_method, "MRMADS")          as integration_delivery_method,
coalesce(partner.scenario_id, cast(-1 as bigint))  as scenario_id,
cast(0 as bigint) as video_starts,
cast(0 as bigint) as slot_imp,
cast(0 as bigint) as break_starts,
cast(0 as bigint) as avails,
cast(0 as bigint) as unconstrained_avails,
cast(0 as bigint) as unfilled_avails,
cast(0 as bigint) as market_avails,
cast(0 as bigint) as ssp_avails,
sum(coalesce(ad_ack_ctx.metrics.ad_impression, 0)) as ad_views,
sum(IF(partner.network_is_ad_owner, coalesce(ad_ack_ctx.metrics.no_ad_impression, 0), 0)) as no_ad_views,
sum(coalesce(ad_ack_ctx.metrics.raw_ad_impression, 0)) as gross_ad_views,
sum(coalesce(ad_ack_ctx.metrics.click, 0)) as clicks,
sum(coalesce(ad_ack_ctx.metrics.no_click, 0)) as no_clicks,
sum(coalesce(ad_ack_ctx.networks[partner.index].revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as revenue,
sum(coalesce(ad_ack_ctx.networks[partner.index].content_owner_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as co_revenue,
sum(coalesce(ad_ack_ctx.networks[partner.index].distributor_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as d_revenue,
sum(coalesce(ad_ack_ctx.networks[partner.index].reseller_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as r_revenue,
sum(coalesce(partner.metrics.margin, 0.0) * coalesce(ad_ack_ctx.metrics.fire_margin_ratio, 0)) as margin,
sum(coalesce(partner.metrics.bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as bidding_revenue,
sum(coalesce(partner.metrics.content_owner_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as co_bidding_revenue,
sum(coalesce(partner.metrics.distributor_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as d_bidding_revenue,
sum(coalesce(partner.metrics.reseller_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0)) as r_bidding_revenue,
sum(coalesce(ad_ack_ctx.metrics.first_quartile, 0)) as first_quartile,
sum(coalesce(ad_ack_ctx.metrics.middle_quartile, 0))    as middle_quartile,
sum(coalesce(ad_ack_ctx.metrics.third_quartile, 0))   as third_quartile,
sum(coalesce(ad_ack_ctx.metrics.complete_quartile, 0)) as complete_quartile,
sum(coalesce(ad_ack_ctx.metrics.can_quartile, 0))     as can_quartile,
sum(coalesce(ad_ack_ctx.metrics.ad_expand, 0))                                          as ad_expand
, sum(coalesce(ad_ack_ctx.metrics.ad_collapse, 0))                                      as ad_collapse
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_expand_collapse_impression, 0))          as measurable_ad_expand_collapse_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_mute, 0))                                          as ad_mute
, sum(coalesce(ad_ack_ctx.metrics.ad_unmute, 0))                                        as ad_unmute
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_mute_unmute_impression, 0))              as measurable_ad_mute_unmute_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_rewind, 0))                                        as ad_rewind
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_rewind_impression, 0))                   as measurable_ad_rewind_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_pause, 0))                                         as ad_pause
, sum(coalesce(ad_ack_ctx.metrics.ad_resume, 0))                                        as ad_resume
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_pause_resume_impression, 0))             as measurable_ad_pause_resume_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_close, 0))                                         as ad_close
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_close_impression, 0))                    as measurable_ad_close_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_accept_invitation, 0))                              as ad_accept_invitation
, sum(coalesce(ad_ack_ctx.metrics.ad_minimize, 0))                                       as ad_minimize
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_accept_invitation_minimize_impression, 0)) as measurable_ad_accept_invitation_minimize_impression
, sum(if(coalesce(request.extra_flags, cast(0 as bigint)) & 1073741824 = 1073741824 and coalesce(partner.role, "") = "CRO" and coalesce(request.extra_flags, cast(0 as bigint)) & 16384 = 16384, cast(0 as bigint), coalesce(ad_ack_ctx.metrics.ad_insertion, 0)))
  as ad_insertion
, sum(if(coalesce(request.is_ssp_bidder_request, false) = true and ((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 49)) > 0 or (coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 50)) > 0), 1, 0)
      * coalesce(ad_ack_ctx.metrics.ad_bid_won, 0))
  as ad_bid_won
, sum(coalesce(partner.metrics.margin, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))                              as bid_won_margin
, sum(coalesce(ad_ack_ctx.networks[partner.index].revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))           as bid_won_revenue
, sum(coalesce(ad_ack_ctx.networks[partner.index].content_owner_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0)) as co_bid_won_revenue
, sum(coalesce(ad_ack_ctx.networks[partner.index].distributor_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))   as d_bid_won_revenue
, sum(coalesce(ad_ack_ctx.networks[partner.index].reseller_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))      as r_bid_won_revenue
, sum(coalesce(partner.metrics.bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))                          as bid_won_bidding_revenue
, sum(coalesce(partner.metrics.content_owner_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))            as co_bid_won_bidding_revenue
, sum(coalesce(partner.metrics.distributor_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))              as d_bid_won_bidding_revenue
, sum(coalesce(partner.metrics.reseller_bidding_revenue, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_bid_revenue_ratio, 0))                 as r_bid_won_bidding_revenue
, sum(if(coalesce(partner.role, "") = "CRO", coalesce(ad_ack_ctx.metrics.hylda_replacement_impression_gains, 0), 0))
  as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, if(partner.network_is_ad_owner, coalesce(ad_ctx.ad.placement_type_priority, "Unknown"), "Unknown") as placement_type_priority
, coalesce(partner.marketplace_audience_extension_deal_ids, array())          as audience_extension_deal_ids
-- geo visibility fields
, coalesce(partner.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(partner.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(partner.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(partner.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
-- slot / ad context fields
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, if(partner.role = 'CRO', coalesce(ad_ctx.ad.linear_decision_type, "Not Applicable"), "Not Applicable") as linear_decision_type
-- visitor / device fields
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
-- conditional visibility fields
, if(partner.standard_brand_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_brand_id, cast(-1 as int)), cast(-1 as int)) as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, if(partner.standard_genre_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_genre_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_genre_ids
, if(partner.content_form_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.content_form_id, cast(-1 as int)), cast(-1 as int)) as content_form_id
, if(partner.content_rating_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.content_rating_id, cast(-1 as int)), cast(-1 as int)) as content_rating_id
, if(partner.standard_language_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_language_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_language_ids
-- request context fields
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
-- order / listing fields
, cast(array() as array<bigint>)                                              as listing_ids
, coalesce(partner.inbound_order_id, cast(-1 as bigint))                      as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, coalesce(partner.outbound_order_id, cast(-1 as bigint))                     as outbound_order_id
, coalesce(partner.outbound_listing_id, cast(array() as array<bigint>))       as outbound_listing_ids
-- static zero fields
, cast(0 as bigint) as total_avails
, cast(0 as bigint) as total_unfilled_avails
, cast(0 as bigint) as opportunity
, cast(0 as bigint) as outbound_avails
, cast(0 as bigint) as outbound_unfilled_avails
, cast(0 as bigint) as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, if(partner.standard_programmer_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_programmer_id, cast(-1 as int)), cast(-1 as int)) as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(partner.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(partner.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(partner.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(partner.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, coalesce(partner.supply_source, cast(-1 as int))                            as supply_source
, coalesce(partner.sales_channel, cast(-1 as int))                            as sales_channel
, coalesce(partner.inbound_order_auction_type, "UNKNOWN")                     as inbound_order_auction_type
, sum(if(coalesce(request.is_ssp_bidder_request, false) = true and ((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 49)) > 0 or (coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 50)) > 0), 1, 0)
      * coalesce(ad_ack_ctx.networks[partner.index].ssp_clearing_revenue, 0.0)
      * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0))             as ssp_clearing_revenue
, coalesce(request.bid_request.publisher_id, "Unknown")                       as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(partner.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, coalesce(partner.bidder_seat_id, cast(-1 as bigint))                        as bidder_seat_id
, coalesce(request.global_currency_version, '')                               as global_currency_version
, coalesce(partner.global_currency_id, cast(-1 as bigint))                    as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, sum(if(coalesce(partner.role, "") in ('CRO'), coalesce(partner.metrics.supply_acquisition_cost, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0), 0.0)) as supply_acquisition_cost
, sum(if(coalesce(partner.role, "") in ('CRO'), coalesce(partner.metrics.supply_distribution_cost, 0.0) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, 0), 0.0)) as supply_distribution_cost
, coalesce(partner.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, if(partner.network_is_ad_owner and not ad_ctx.ad.is_bumper and not ad_ctx.ad.is_external and ad_ctx.ad.is_rbp, cast(1 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 53)) > 0, cast(2 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 54)) > 0, cast(4 as int), cast(0 as int))
  + if(partner.network_is_extra_item_owner and (coalesce(ad_ctx.ad.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 48)) > 0, cast(8 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 57)) > 0, cast(16 as int), cast(0 as int))
  + if(partner.sales_channel = 4 and partner.supply_source != 4 and coalesce(ad_ctx.candidate.auction.extra_flags, cast(0 as bigint)) & 4194304 > 0, cast(32 as int), cast(0 as int))
                                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))            as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(ad_ctx.networks) as partner
lateral view explode(ad_ctx.ack_ctxes) as ad_ack_ctx
where ad_ack_ctx.ack.ack_entity_type = 'ad' 
and ad_ack_ctx.ack.flags & 256 = 0
and ad_ctx.ad.is_bumper = false
and (!ad_ack_ctx.ack.is_private_impression or partner.network_is_ad_owner or partner.network_is_extra_item_owner)
and date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all 

select
cast(date_format(date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(ad_ctx.ad.replaced_ad_network_id, cast(-1 as bigint))              as network_id
, coalesce(partner.content_owner_network_id, cast(-1 as bigint))              as content_owner_id
, coalesce(partner.distributor_network_id, cast(-1 as bigint))                as distributor_id
--, coalesce(ad_ctx.ad.replaced_ad_network_id, cast(-1 as bigint))             as reseller_id
, cast(-1 as bigint)  
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                as tv_network_id
, coalesce(partner.role, "")                                                  as transaction_type
, coalesce(ad_ack_ctx.ack.traffic_type, cast(0 as bigint))                   as traffic_type
, coalesce(partner.bit_flags, cast(0 as bigint))+ coalesce(ad_ctx.ad.replaced_ad_bit_flags, cast(0 as bigint))+ coalesce(request.bit_flags, cast(0 as bigint))+ coalesce(ad_ack_ctx.ack.bit_flags, cast(0 as bigint))                    as bit_flag
, cast(-1 as bigint)                                                          as asset_id
, cast(-1 as bigint)                                                          as series_id
, cast(array() as array<bigint>)                                              as asset_group_ids
, cast(-1 as bigint)                                                          as site_section_id
, cast(-1 as bigint)                                                          as site_id
, cast(array() as array<bigint>)                                              as site_section_group_ids
, cast(-1 as bigint)                                                          as airing_id
, cast(-1 as bigint)                                                          as channel_id
, cast(-1 as bigint)                                                          as break_id
, coalesce(slot_ctx.slot.time_position_class, "Unknown")                      as time_position_class
, ad_ctx.ad.ad_delivery_method                                                as delivery_method
, coalesce(ad_ctx.ad.replaced_ad_unit_id, cast(-1 as bigint))                as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, "FULL_VISIBILITY"                                                           as geo_visibility
, "" as geo_visibility
, "FULL_VISIBILITY"                                                           as user_agent_visibility
, cast(array() as array<bigint>)                                              as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, cast(array() as array<int>)                                                 as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, cast(-1 as bigint)                                                          as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, sum(coalesce(ad_ack_ctx.metrics.ad_impression, 0))                          as ad_views
, sum(if(partner.network_is_ad_owner, coalesce(ad_ack_ctx.metrics.no_ad_impression, 0), 0)) as no_ad_views
, sum(coalesce(ad_ack_ctx.metrics.raw_ad_impression, 0))                      as gross_ad_views
, sum(coalesce(ad_ack_ctx.metrics.click, 0))                                  as clicks
, sum(coalesce(ad_ack_ctx.metrics.no_click, 0))                               as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, sum(coalesce(ad_ack_ctx.metrics.first_quartile, 0))                         as first_quartile
, sum(coalesce(ad_ack_ctx.metrics.middle_quartile, 0))                        as middle_quartile
, sum(coalesce(ad_ack_ctx.metrics.third_quartile, 0))                         as third_quartile
, sum(coalesce(ad_ack_ctx.metrics.complete_quartile, 0))                      as complete_quartile
, sum(coalesce(ad_ack_ctx.metrics.can_quartile, 0))                           as can_quartile
, sum(coalesce(ad_ack_ctx.metrics.ad_expand, 0))                              as ad_expand
, sum(coalesce(ad_ack_ctx.metrics.ad_collapse, 0))                            as ad_collapse
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_expand_collapse_impression, 0)) as measurable_ad_expand_collapse_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_mute, 0))                                as ad_mute
, sum(coalesce(ad_ack_ctx.metrics.ad_unmute, 0))                              as ad_unmute
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_mute_unmute_impression, 0))   as measurable_ad_mute_unmute_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_rewind, 0))                              as ad_rewind
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_rewind_impression, 0))        as measurable_ad_rewind_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_pause, 0))                               as ad_pause
, sum(coalesce(ad_ack_ctx.metrics.ad_resume, 0))                              as ad_resume
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_pause_resume_impression, 0))  as measurable_ad_pause_resume_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_close, 0))                               as ad_close
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_close_impression, 0))         as measurable_ad_close_impression
, sum(coalesce(ad_ack_ctx.metrics.ad_accept_invitation, 0))                   as ad_accept_invitation
, sum(coalesce(ad_ack_ctx.metrics.ad_minimize, 0))                            as ad_minimize
, sum(coalesce(ad_ack_ctx.metrics.measurable_ad_accept_invitation_minimize_impression, 0)) as measurable_ad_accept_invitation_minimize_impression
, sum(if(coalesce(request.extra_flags, cast(0 as bigint)) & 1073741824 = 1073741824 and coalesce(partner.role, "") = "CRO" and coalesce(request.extra_flags, cast(0 as bigint)) & 16384 = 16384, cast(0 as bigint), coalesce(ad_ack_ctx.metrics.ad_insertion, 0)))
  as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, cast(array() as array<bigint>)                                              as audience_extension_deal_ids
, "FULL_VISIBILITY"                                                           as geo_state_visibility
, "FULL_VISIBILITY"                                                           as geo_dma_visibility
, "FULL_VISIBILITY"                                                           as geo_city_visibility
, "FULL_VISIBILITY"                                                           as geo_zipcode_visibility
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, if(partner.role = 'CRO', coalesce(ad_ctx.ad.linear_decision_type, "Not Applicable"), "Not Applicable") as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, cast(-1 as int) as standard_brand_id
, cast(-1 as int) as standard_channel_id
, cast(array() as array<int>) as standard_genre_ids
, cast(-1 as int) as content_form_id
, cast(-1 as int) as content_rating_id
, cast(array() as array<int>) as standard_language_ids
, cast(-1 as int) as stream_mode_id
, cast(-1 as int) as inventory_location_id
, cast(array() as array<bigint>) as listing_ids
, cast(-1 as bigint) as inbound_order_id
, cast(array() as array<bigint>) as inbound_listing_ids
, cast(-1 as bigint) as outbound_order_id
, cast(array() as array<bigint>) as outbound_listing_ids
, cast(0 as bigint) as total_avails
, cast(0 as bigint) as total_unfilled_avails
, cast(0 as bigint) as opportunity
, cast(0 as bigint) as outbound_avails
, cast(0 as bigint) as outbound_unfilled_avails
, cast(0 as bigint) as outbound_opportunity
, cast(-1 as int) as ip_enabled_audience_id
, cast(-1 as int) as standard_programmer_id
, cast(0 as bigint) as request_count
, "FULL_VISIBILITY" as geo_country_visibility
, "FULL_VISIBILITY" as standard_brand_visibility
, "FULL_VISIBILITY" as standard_genre_visibility
, "FULL_VISIBILITY" as content_rating_visibility
, cast(0 as int) as supply_source
, cast(2 as int) as sales_channel
, "UNKNOWN" as inbound_order_auction_type
, cast(0 as double) as ssp_clearing_revenue
, "Unknown" as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, "FULL_VISIBILITY" as standard_programmer_visibility
, cast(-1 as bigint) as bidder_seat_id
, '' as global_currency_version
, cast(-1 as bigint) as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>) as inventory_package_ids
, cast(0 as double) as supply_acquisition_cost
, cast(0 as double) as supply_distribution_cost
, "FULL_VISIBILITY" as content_form_visibility
, cast(0 as int)                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))            as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(ad_ctx.networks) as partner
lateral view explode(ad_ctx.ack_ctxes) as ad_ack_ctx
where ad_ack_ctx.ack.ack_entity_type = 'ad'
and ad_ack_ctx.ack.flags & 256 = 0
and coalesce(partner.role, "") in ("CRO")
and partner.network_is_ad_owner = true
and ad_ctx.ad.is_bumper = false
and ad_ctx.ad.is_ax = true
and date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all 

select
cast(date_format(date_trunc('HOUR', cast(req_ack.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(partner.network_id, cast(-1 as bigint))                             as network_id
, coalesce(partner.content_owner_network_id, cast(-1 as bigint))              as content_owner_id
, coalesce(partner.distributor_network_id, cast(-1 as bigint))                as distributor_id
--, coalesce(partner.reseller_network_id, cast(-1 as bigint))                   as reseller_id
, cast(-1 as bigint)                                                         as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, if(partner.role is null, "", concat(partner.role, "V"))                      as transaction_type
, coalesce(req_ack.ack.traffic_type, cast(0 as bigint))                    as traffic_type
, coalesce(partner.bit_flags, cast(0 as bigint)) + coalesce(request.bit_flags, cast(0 as bigint)) as bit_flag
, coalesce(partner.asset_id, cast(-1 as bigint))                              as asset_id
, coalesce(partner.series_id, cast(-1 as bigint))                             as series_id
, coalesce(partner.asset_group_ids, array())                                  as asset_group_ids
, coalesce(partner.site_section_id, cast(-1 as bigint))                       as site_section_id
, coalesce(partner.site_id, cast(-1 as bigint))                               as site_id
, coalesce(partner.site_section_group_ids, array())                           as site_section_group_ids
, partner.airing_id                                                           as airing_id
, partner.airing_channel_id                                                   as channel_id
, cast(-1 as bigint)                                                          as break_id
, "Unknown"                                                                   as time_position_class
, ""                                                                          as delivery_method
, cast(-1 as bigint)                                                          as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, coalesce(partner.geo_visibility.report_aggregate, "FULL_VISIBILITY")         as geo_visibility
,""                                                                           as geo_visibility
, coalesce(partner.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
, coalesce(partner.tracked_audience_item_ids, array())                        as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, coalesce(partner.postal_code_package_id, array())                           as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, coalesce(partner.scenario_id, cast(-1 as bigint))                           as scenario_id
, sum(coalesce(req_ack.metrics.video_view, 0))                                as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, cast(array() as array<bigint>)                                              as audience_extension_deal_ids
, coalesce(partner.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(partner.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(partner.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(partner.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
, ""                                                                          as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, if(partner.standard_brand_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_brand_id, cast(-1 as int)), cast(-1 as int)) as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, if(partner.standard_genre_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_genre_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_genre_ids
, if(partner.content_form_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.content_form_id, cast(-1 as int)), cast(-1 as int)) as content_form_id
, if(partner.content_rating_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.content_rating_id, cast(-1 as int)), cast(-1 as int)) as content_rating_id
, if(partner.standard_language_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_language_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_language_ids
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, cast(-1 as bigint)                                                          as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, cast(-1 as bigint)                                                          as outbound_order_id
, cast(array() as array<bigint>)                                              as outbound_listing_ids
, cast(0 as bigint) as total_avails
, cast(0 as bigint) as total_unfilled_avails
, cast(0 as bigint) as opportunity
, cast(0 as bigint) as outbound_avails
, cast(0 as bigint) as outbound_unfilled_avails
, cast(0 as bigint) as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, if(partner.standard_programmer_visibility.report_aggregate is not null or partner.supply_source != 3, coalesce(request.context.standard_programmer_id, cast(-1 as int)), cast(-1 as int)) as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(partner.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(partner.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(partner.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(partner.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, cast(0 as int)                                                              as supply_source
, cast(0 as int)                                                              as sales_channel
, "UNKNOWN"                                                                   as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, "Unknown"                                                                   as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(partner.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, cast(-1 as bigint)                                                          as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, coalesce(partner.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, if(coalesce(request.extra_flags3, cast(0 as bigint)) & 16 > 0, cast(32 as int), cast(0 as int)) as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(req_ack.ack.timestamp))             as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(inventory.asset_chain) as partner
    LATERAL VIEW EXPLODE(request.acks) AS req_ack
where
 req_ack.ack.ack_entity_type = 'video'
 and req_ack.ack.flags & 256 = 0
and coalesce(req_ack.metrics.video_view, 0) != 0
and date_trunc("HOUR", from_unixtime(req_ack.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all

select
cast(date_format(date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(slot_network.network_id, cast(-1 as bigint))                        as network_id
, coalesce(slot_network.content_owner_network_id, cast(-1 as bigint))         as content_owner_id
, coalesce(slot_network.distributor_network_id, cast(-1 as bigint))           as distributor_id
--, coalesce(slot_network.reseller_network_id, cast(-1 as bigint))               as reseller_id
,cast(-1 as bigint)               as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, if(slot_network.role is null, "", concat(slot_network.role, "V"))            as transaction_type
, coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as bigint))                  as traffic_type
, coalesce(slot_network.bit_flags, cast(0 as bigint)) + coalesce(request.bit_flags, cast(0 as bigint)) as bit_flag
, coalesce(slot_network.asset_id, cast(-1 as bigint))                         as asset_id
, coalesce(slot_network.series_id, cast(-1 as bigint))                        as series_id
, coalesce(slot_network.asset_group_ids, array())                             as asset_group_ids
, coalesce(slot_network.site_section_id, cast(-1 as bigint))                  as site_section_id
, coalesce(slot_network.site_id, cast(-1 as bigint))                          as site_id
, coalesce(slot_network.site_section_group_ids, array())                      as site_section_group_ids
, slot_network.airing_id                                                      as airing_id
, slot_network.airing_channel_id                                              as channel_id
, coalesce(slot_network.break_id, cast(-1 as bigint))                         as break_id
, coalesce(slot_ctx.slot.time_position_class, "Unknown")                      as time_position_class
, ""                                                                          as delivery_method
, if(slot_network.network_is_ad_unit_owner, coalesce(cast(slot_ctx.slot.ad_unit_id as bigint), cast(-1 as bigint)), cast(-1 as bigint)) as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, coalesce(slot_network.geo_visibility.report_aggregate, "FULL_VISIBILITY")      as geo_visibility
,"" as geo_visibility
, coalesce(slot_network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
, coalesce(slot_network.tracked_audience_item_ids, array())                   as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, coalesce(slot_network.postal_code_package_id, array())                      as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, coalesce(slot_network.scenario_id, cast(-1 as bigint))                      as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].avails_in_played_slot, cast(0 as bigint)))                as avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].unconstrained_avails_in_played_slot, cast(0 as bigint))) as unconstrained_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].unfilled_avails_in_played_slot, cast(0 as bigint)))      as unfilled_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].market_avails_in_played_slot, cast(0 as bigint)))        as market_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].ssp_avails_in_played_slot, cast(0 as bigint)))           as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, coalesce(slot_network.marketplace_audience_extension_deal_ids, array())     as audience_extension_deal_ids
, coalesce(slot_network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(slot_network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(slot_network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(slot_network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, if(slot_network.standard_brand_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_brand_id, cast(-1 as int)), cast(-1 as int)) as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, if(slot_network.standard_genre_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_genre_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_genre_ids
, if(slot_network.content_form_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.content_form_id, cast(-1 as int)), cast(-1 as int)) as content_form_id
, if(slot_network.content_rating_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.content_rating_id, cast(-1 as int)), cast(-1 as int)) as content_rating_id
, if(slot_network.standard_language_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_language_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_language_ids
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, coalesce(slot_network.inbound_order_id, cast(-1 as bigint))                 as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, cast(-1 as bigint)                                                          as outbound_order_id
, cast(array() as array<bigint>)                                              as outbound_listing_ids
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].total_avails_in_played_slot, cast(0 as bigint))) as total_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].total_unfilled_avails_in_played_slot, cast(0 as bigint))) as total_unfilled_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].opportunity_in_played_slot, cast(0 as bigint))) as opportunity
, cast(0 as bigint)                                                           as outbound_avails
, cast(0 as bigint)                                                           as outbound_unfilled_avails
, cast(0 as bigint)                                                           as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, if(slot_network.standard_programmer_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_programmer_id, cast(-1 as int)), cast(-1 as int)) as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(slot_network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(slot_network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(slot_network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(slot_network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, coalesce(slot_network.supply_source, cast(-1 as int))                       as supply_source
, cast(0 as int)                                                              as sales_channel
, coalesce(slot_network.inbound_order_auction_type, "UNKNOWN")                as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, coalesce(request.bid_request.publisher_id, "Unknown")                       as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(slot_network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, coalesce(slot_network.bidder_seat_id, cast(-1 as bigint))                   as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, coalesce(slot_network.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, cast(0 as int)                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))           as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.networks) as slot_network
    lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
where slot_ack_ctx.ack.flags & 256 = 0 and slot_ack_ctx.ack.ack_entity_type = 'slot'
  and coalesce(slot_ctx.slot.flags, cast(0 as bigint)) & 64 = 0
  and (
    (
      --coalesce(slot_ack_ctx.metrics.avails_event_count, 0) != 0
      --and 
      (
        coalesce(slot_ack_ctx.networks[slot_network.index].avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].unconstrained_avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].unfilled_avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].market_avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].ssp_avails_in_played_slot, 0) != 0
      )
    )
    or (
      coalesce(slot_ack_ctx.metrics.slot_impression, 0) != 0
      and (
        coalesce(slot_ack_ctx.networks[slot_network.index].total_avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].total_unfilled_avails_in_played_slot, 0) != 0
        or coalesce(slot_ack_ctx.networks[slot_network.index].opportunity_in_played_slot, 0) != 0
      )
    )
  )
  and date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all

select
cast(date_format(date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(slot_network.network_id, cast(-1 as bigint))                        as network_id
, coalesce(slot_network.content_owner_network_id, cast(-1 as bigint))         as content_owner_id
, coalesce(slot_network.distributor_network_id, cast(-1 as bigint))           as distributor_id
--, coalesce(outbound.down_network_id, cast(-1 as bigint))                      as reseller_id
, cast(-1 as bigint)                                                         as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, if(slot_network.role is null, "", concat(slot_network.role, "V"))            as transaction_type
, coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as bigint))                  as traffic_type
, coalesce(slot_network.bit_flags, cast(0 as bigint))+ coalesce(request.bit_flags, cast(0 as bigint))+ coalesce(outbound.bit_flags, cast(0 as bigint))                           as bit_flag
, coalesce(slot_network.asset_id, cast(-1 as bigint))                         as asset_id
, coalesce(slot_network.series_id, cast(-1 as bigint))                        as series_id
, coalesce(slot_network.asset_group_ids, array())                             as asset_group_ids
, coalesce(slot_network.site_section_id, cast(-1 as bigint))                  as site_section_id
, coalesce(slot_network.site_id, cast(-1 as bigint))                          as site_id
, coalesce(slot_network.site_section_group_ids, array())                      as site_section_group_ids
, slot_network.airing_id                                                      as airing_id
, slot_network.airing_channel_id                                              as channel_id
, coalesce(slot_network.break_id, cast(-1 as bigint))                         as break_id
, coalesce(slot_ctx.slot.time_position_class, "Unknown")                      as time_position_class
, ""                                                                          as delivery_method
, if(slot_network.network_is_ad_unit_owner, coalesce(cast(slot_ctx.slot.ad_unit_id as bigint), cast(-1 as bigint)), cast(-1 as bigint)) as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, coalesce(slot_network.geo_visibility.report_aggregate, "FULL_VISIBILITY")      as geo_visibility
,"" as geo_visibility
, coalesce(slot_network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
, coalesce(slot_network.tracked_audience_item_ids, array())                   as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, coalesce(slot_network.postal_code_package_id, array())                      as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, coalesce(slot_network.scenario_id, cast(-1 as bigint))                      as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, coalesce(slot_network.marketplace_audience_extension_deal_ids, array())     as audience_extension_deal_ids
, coalesce(slot_network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(slot_network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(slot_network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(slot_network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, if(slot_network.standard_brand_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_brand_id, cast(-1 as int)), cast(-1 as int)) as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, if(slot_network.standard_genre_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_genre_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_genre_ids
, if(slot_network.content_form_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.content_form_id, cast(-1 as int)), cast(-1 as int)) as content_form_id
, if(slot_network.content_rating_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.content_rating_id, cast(-1 as int)), cast(-1 as int)) as content_rating_id
, if(slot_network.standard_language_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_language_ids, cast(array() as array<int>)), cast(array() as array<int>)) as standard_language_ids
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, coalesce(slot_network.inbound_order_id, cast(-1 as bigint))                 as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, coalesce(outbound.order_id, cast(-1 as bigint))                             as outbound_order_id
, coalesce(outbound.listing_id, cast(array() as array<bigint>))               as outbound_listing_ids
, cast(0 as bigint)                                                           as total_avails
, cast(0 as bigint)                                                           as total_unfilled_avails
, cast(0 as bigint)                                                           as opportunity
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].total_avails_in_played_slot, cast(0 as bigint))) as outbound_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].total_unfilled_avails_in_played_slot, cast(0 as bigint))) as outbound_unfilled_avails
, sum(coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].opportunity_in_played_slot, cast(0 as bigint))) as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, if(slot_network.standard_programmer_visibility.report_aggregate is not null or slot_network.supply_source != 3, coalesce(request.context.standard_programmer_id, cast(-1 as int)), cast(-1 as int)) as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(slot_network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(slot_network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(slot_network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(slot_network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, coalesce(slot_network.supply_source, cast(-1 as int))                       as supply_source
, coalesce(outbound.sales_channel, cast(-1 as int))                           as sales_channel
, coalesce(slot_network.inbound_order_auction_type, "UNKNOWN")                as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, coalesce(request.bid_request.publisher_id, "Unknown")                       as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(slot_network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, coalesce(slot_network.bidder_seat_id, cast(-1 as bigint))                   as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, coalesce(slot_network.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, cast(0 as int)                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))           as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.networks) as slot_network
    lateral view explode(slot_network.eligible_outbound_orders) as outbound
    lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
where slot_ack_ctx.ack.ack_entity_type = 'slot'
  and coalesce(slot_ctx.slot.flags, cast(0 as bigint)) & 64 = 0
  and coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as bigint)) != 0
  and (
    coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].total_avails_in_played_slot, 0) != 0
    or coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].total_unfilled_avails_in_played_slot, 0) != 0
    or coalesce(slot_ack_ctx.networks[slot_network.index].eligible_outbound_orders[outbound.index].opportunity_in_played_slot, 0) != 0
  )
  and date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all 

select
cast(date_format(date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(slot_network.network_id, cast(-1 as bigint))                        as network_id
, coalesce(slot_network.content_owner_network_id, cast(-1 as bigint))         as content_owner_id
, coalesce(slot_network.distributor_network_id, cast(-1 as bigint))           as distributor_id
, cast(-1 as bigint)                                                          as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, "CROB"                                                                      as transaction_type
, coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as bigint))                  as traffic_type
, coalesce(slot_network.bit_flags, cast(0 as bigint)) + coalesce(request.bit_flags, cast(0 as bigint)) as bit_flag
, coalesce(slot_network.asset_id, cast(-1 as bigint))                         as asset_id
, coalesce(slot_network.series_id, cast(-1 as bigint))                        as series_id
, coalesce(slot_network.asset_group_ids, array())                             as asset_group_ids
, coalesce(slot_network.site_section_id, cast(-1 as bigint))                  as site_section_id
, coalesce(slot_network.site_id, cast(-1 as bigint))                          as site_id
, coalesce(slot_network.site_section_group_ids, array())                      as site_section_group_ids
, slot_network.airing_id                                                      as airing_id
, slot_network.airing_channel_id                                              as channel_id
, coalesce(slot_network.break_id, cast(-1 as bigint))                         as break_id
, "Unknown"                                                                   as time_position_class
, ""                                                                          as delivery_method
, cast(-1 as bigint)                                                          as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, coalesce(slot_network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY") as geo_visibility
,"" as geo_visibility
, coalesce(slot_network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
, cast(array() as array<bigint>)                                              as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, coalesce(slot_network.postal_code_package_id, array())                      as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, coalesce(slot_network.scenario_id, cast(-1 as bigint))                      as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, sum(coalesce(slot_ack_ctx.metrics.break_starts, cast(0 as bigint)))          as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, cast(array() as array<bigint>)                                              as audience_extension_deal_ids
, coalesce(slot_network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(slot_network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(slot_network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(slot_network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, coalesce(request.context.standard_brand_id, cast(-1 as int))                as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, coalesce(request.context.standard_genre_ids, cast(array() as array<int>))   as standard_genre_ids
, coalesce(request.context.content_form_id, cast(-1 as int))                  as content_form_id
, coalesce(request.context.content_rating_id, cast(-1 as int))                as content_rating_id
, coalesce(request.context.standard_language_ids, cast(array() as array<int>)) as standard_language_ids
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, cast(-1 as bigint)                                                          as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, cast(-1 as bigint)                                                          as outbound_order_id
, cast(array() as array<bigint>)                                              as outbound_listing_ids
, cast(0 as bigint)                                                           as total_avails
, cast(0 as bigint)                                                           as total_unfilled_avails
, cast(0 as bigint)                                                           as opportunity
, cast(0 as bigint)                                                           as outbound_avails
, cast(0 as bigint)                                                           as outbound_unfilled_avails
, cast(0 as bigint)                                                           as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, coalesce(request.context.standard_programmer_id, cast(-1 as int))           as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(slot_network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(slot_network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(slot_network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(slot_network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, cast(0 as int)                                                              as supply_source
, cast(0 as int)                                                              as sales_channel
, "UNKNOWN"                                                                   as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, "Unknown"                                                                   as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(slot_network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, cast(-1 as bigint)                                                          as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, coalesce(slot_network.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, cast(0 as int) as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))           as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.networks) as slot_network
    lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
where slot_ack_ctx.ack.ack_entity_type = 'slot'
  and slot_ack_ctx.ack.flags & 256 = 0 
  and coalesce(slot_network.role, "") = "CRO"
  and coalesce(slot_ctx.slot.environment, "") = "VIDEO"
  and coalesce(slot_ctx.slot.time_position_class, "Unknown") != "overlay"
  and coalesce(slot_ctx.slot.flags, cast(0 as bigint)) & 32 = 0
  and coalesce(request.bit_flags, cast(0 as bigint)) & 32768 != 0
  and coalesce(slot_ack_ctx.metrics.break_starts, cast(0 as bigint)) != 0
  and date_trunc("HOUR", from_unixtime(slot_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all 

select
cast(date_format(date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(partner.network_id, cast(-1 as bigint))                             as network_id
, coalesce(partner.content_owner_network_id, cast(-1 as bigint))              as content_owner_id
, coalesce(partner.distributor_network_id, cast(-1 as bigint))                as distributor_id
--, coalesce(partner.reseller_network_id, cast(-1 as bigint))                   as reseller_id
, cast(-1 as bigint)                                                          as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, coalesce(partner.role, "")                                                  as transaction_type
, coalesce(ad_ack_ctx.ack.traffic_type, cast(0 as bigint))                    as traffic_type
, coalesce(partner.bit_flags, cast(0 as bigint)) + coalesce(request.bit_flags, cast(0 as bigint)) as bit_flag
, coalesce(partner.asset_id, cast(-1 as bigint))                              as asset_id
, coalesce(partner.series_id, cast(-1 as bigint))                             as series_id
, coalesce(partner.asset_group_ids, array())                                  as asset_group_ids
, coalesce(partner.site_section_id, cast(-1 as bigint))                       as site_section_id
, coalesce(partner.site_id, cast(-1 as bigint))                               as site_id
, coalesce(partner.site_section_group_ids, array())                           as site_section_group_ids
, partner.airing_id                                                           as airing_id
, partner.airing_channel_id                                                   as channel_id
, coalesce(partner.break_id, cast(-1 as bigint))                              as break_id
, coalesce(slot_ctx.slot.time_position_class, "Unknown")                      as time_position_class
, "Static"                                                                    as delivery_method
, coalesce(ad_ctx.ad.replaced_ad_unit_id, cast(-1 as bigint))                 as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, coalesce(partner.geo_visibility.report_aggregate, "FULL_VISIBILITY")         as geo_visibility
,"" as geo_visibility
, coalesce(partner.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
, cast(array() as array<bigint>)                                              as tracked_audience_item_ids
, coalesce(visitor.postal_code, "-1")                                         as postal_code
, coalesce(partner.postal_code_package_id, array())                           as postal_code_package_ids
, coalesce(visitor.city_id, cast(-1 as int))                                  as user_city_id
, coalesce(visitor.state_id, cast(-1 as int))                                 as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, coalesce(visitor.platform_browser_id, cast(-1 as bigint))                   as delivered_platform_browser_id
, coalesce(visitor.platform_device_id, cast(-1 as bigint))                    as delivered_platform_device_id
, coalesce(visitor.platform_os_id, cast(-1 as bigint))                        as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, coalesce(request.delivery_method, "MRMADS")                                 as integration_delivery_method
, coalesce(partner.scenario_id, cast(-1 as bigint))                           as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, sum(coalesce(ad_ack_ctx.metrics.hylda_replacement_impression_forfeits, cast(0 as bigint))) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, cast(array() as array<bigint>)                                              as audience_extension_deal_ids
, coalesce(partner.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")  as geo_state_visibility
, coalesce(partner.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, coalesce(partner.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")   as geo_city_visibility
, coalesce(partner.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
, coalesce(slot_ctx.slot.avail_type, "")                                      as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, if(visitor.standard_device_type_child_id is null, cast(array() as array<int>), array(visitor.standard_device_type_child_id)) as standard_device_type_ids
, coalesce(visitor.standard_environment_id, cast(-1 as int))                  as standard_environment_id
, coalesce(visitor.standard_os_id, cast(-1 as int))                           as standard_os_id
, coalesce(request.context.standard_brand_id, cast(-1 as int))                as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, coalesce(request.context.standard_genre_ids, cast(array() as array<int>))   as standard_genre_ids
, coalesce(request.context.content_form_id, cast(-1 as int))                  as content_form_id
, coalesce(request.context.content_rating_id, cast(-1 as int))                as content_rating_id
, coalesce(request.context.standard_language_ids, cast(array() as array<int>)) as standard_language_ids
, coalesce(request.context.stream_mode_id, cast(-1 as int))                   as stream_mode_id
, coalesce(request.context.inventory_location_id, cast(-1 as int))            as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, cast(-1 as bigint)                                                          as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, cast(-1 as bigint)                                                          as outbound_order_id
, cast(array() as array<bigint>)                                              as outbound_listing_ids
, cast(0 as bigint)                                                           as total_avails
, cast(0 as bigint)                                                           as total_unfilled_avails
, cast(0 as bigint)                                                           as opportunity
, cast(0 as bigint)                                                           as outbound_avails
, cast(0 as bigint)                                                           as outbound_unfilled_avails
, cast(0 as bigint)                                                           as outbound_opportunity
, coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))           as ip_enabled_audience_id
, coalesce(request.context.standard_programmer_id, cast(-1 as int))           as standard_programmer_id
, cast(0 as bigint)                                                           as request_count
, coalesce(partner.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, coalesce(partner.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
, coalesce(partner.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY") as standard_genre_visibility
, coalesce(partner.content_rating_visibility.report_aggregate, "FULL_VISIBILITY") as content_rating_visibility
, cast(1 as int)                                                              as supply_source
, cast(2 as int)                                                              as sales_channel
, "UNKNOWN"                                                                   as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, "Unknown"                                                                   as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, coalesce(partner.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
, cast(-1 as bigint)                                                          as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, coalesce(partner.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
, if(partner.network_is_ad_owner and not ad_ctx.ad.is_bumper and not ad_ctx.ad.is_external and ad_ctx.ad.is_rbp, cast(1 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 53)) > 0, cast(2 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 54)) > 0, cast(4 as int), cast(0 as int))
  + if(partner.network_is_extra_item_owner and (coalesce(ad_ctx.ad.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 48)) > 0, cast(8 as int), cast(0 as int))
  + if((coalesce(partner.bit_flags, cast(0 as bigint)) & shiftleft(cast(1 as bigint), 57)) > 0, cast(16 as int), cast(0 as int))
  + if(partner.sales_channel = 4 and partner.supply_source != 4 and coalesce(ad_ctx.candidate.auction.extra_flags, cast(0 as bigint)) & 4194304 > 0, cast(32 as int), cast(0 as int))
                                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))             as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(ad_ctx.networks) as partner
lateral view explode(ad_ctx.ack_ctxes) as ad_ack_ctx
where ad_ack_ctx.ack.ack_entity_type = 'ad'
  and coalesce(partner.role, "") = "CRO"
  and ad_ctx.ad.is_bumper = false
  and ad_ctx.ad.is_replacement = true
  and coalesce(ad_ack_ctx.metrics.hylda_replacement_impression_forfeits, cast(0 as bigint)) != 0
  and date_trunc("HOUR", from_unixtime(ad_ack_ctx.ack.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148

union all 

select
cast(date_format(date_trunc('HOUR', cast(request.timestamp as timestamp)), 'yyyyMMddHHmmss') as bigint) as process_batch_id
, coalesce(network.network_id, cast(-1 as bigint))                             as network_id
, coalesce(network.content_owner_network_id, cast(-1 as bigint))              as content_owner_id
, coalesce(network.distributor_network_id, cast(-1 as bigint))                as distributor_id
--, coalesce(network.reseller_network_id, cast(-1 as bigint))                   as reseller_id
, cast(-1 as bigint) as reseller_id
, coalesce(request.context.tv_network_id, cast(-1 as bigint))                 as tv_network_id
, "CROR"                                                                      as transaction_type
, coalesce(request.traffic_type, cast(0 as bigint))                           as traffic_type
, coalesce(network.bit_flags, cast(0 as bigint)) + coalesce(request.bit_flags, cast(0 as bigint)) as bit_flag
, cast(-1 as bigint)                                                          as asset_id
, cast(-1 as bigint)                                                          as series_id
, cast(array() as array<bigint>)                                              as asset_group_ids
, coalesce(network.site_section_id, cast(-1 as bigint))                       as site_section_id
, coalesce(network.site_id, cast(-1 as bigint))                               as site_id
, cast(array() as array<bigint>)                                              as site_section_group_ids
, cast(-1 as bigint)                                                          as airing_id
, network.airing_channel_id                                                   as channel_id
, cast(-1 as bigint)                                                          as break_id
, "Unknown"                                                                   as time_position_class
, ""                                                                          as delivery_method
, cast(-1 as bigint)                                                          as ad_unit_id
, coalesce(visitor.platform_group, "-1")                                      as platform_group
--, "FULL_VISIBILITY"                                                           as geo_visibility
, "" as geo_visibility
, "FULL_VISIBILITY"                                                           as user_agent_visibility
, cast(array() as array<bigint>)                                              as tracked_audience_item_ids
, "-1"                                                                        as postal_code
, cast(array() as array<int>)                                                 as postal_code_package_ids
, cast(-1 as int)                                                             as user_city_id
, cast(-1 as int)                                                             as user_state_id
, coalesce(visitor.dma_code, cast(-1 as int))                                 as user_dma_code
, coalesce(cast(visitor.country_id as bigint), cast(-1 as bigint))            as user_country_id
, cast(-1 as bigint)                                                          as delivered_platform_browser_id
, cast(-1 as bigint)                                                          as delivered_platform_device_id
, cast(-1 as bigint)                                                          as delivered_platform_os_id
, coalesce(visitor.operator_zone_id, cast(-1 as bigint))                      as operator_zone_id
, ""                                                                          as integration_delivery_method
, cast(-1 as bigint)                                                          as scenario_id
, cast(0 as bigint) as video_starts
, cast(0 as bigint) as slot_imp
, cast(0 as bigint) as break_starts
, cast(0 as bigint) as avails
, cast(0 as bigint) as unconstrained_avails
, cast(0 as bigint) as unfilled_avails
, cast(0 as bigint) as market_avails
, cast(0 as bigint) as ssp_avails
, cast(0 as bigint) as ad_views
, cast(0 as bigint) as no_ad_views
, cast(0 as bigint) as gross_ad_views
, cast(0 as bigint) as clicks
, cast(0 as bigint) as no_clicks
, cast(0 as double) as revenue
, cast(0 as double) as co_revenue
, cast(0 as double) as d_revenue
, cast(0 as double) as r_revenue
, cast(0 as double) as margin
, cast(0 as double) as bidding_revenue
, cast(0 as double) as co_bidding_revenue
, cast(0 as double) as d_bidding_revenue
, cast(0 as double) as r_bidding_revenue
, cast(0 as bigint) as first_quartile
, cast(0 as bigint) as middle_quartile
, cast(0 as bigint) as third_quartile
, cast(0 as bigint) as complete_quartile
, cast(0 as bigint) as can_quartile
, cast(0 as bigint) as ad_expand
, cast(0 as bigint) as ad_collapse
, cast(0 as bigint) as measurable_ad_expand_collapse_impression
, cast(0 as bigint) as ad_mute
, cast(0 as bigint) as ad_unmute
, cast(0 as bigint) as measurable_ad_mute_unmute_impression
, cast(0 as bigint) as ad_rewind
, cast(0 as bigint) as measurable_ad_rewind_impression
, cast(0 as bigint) as ad_pause
, cast(0 as bigint) as ad_resume
, cast(0 as bigint) as measurable_ad_pause_resume_impression
, cast(0 as bigint) as ad_close
, cast(0 as bigint) as measurable_ad_close_impression
, cast(0 as bigint) as ad_accept_invitation
, cast(0 as bigint) as ad_minimize
, cast(0 as bigint) as measurable_ad_accept_invitation_minimize_impression
, cast(0 as bigint) as ad_insertion
, cast(0 as bigint) as ad_bid_won
, cast(0 as double) as bid_won_margin
, cast(0 as double) as bid_won_revenue
, cast(0 as double) as co_bid_won_revenue
, cast(0 as double) as d_bid_won_revenue
, cast(0 as double) as r_bid_won_revenue
, cast(0 as double) as bid_won_bidding_revenue
, cast(0 as double) as co_bid_won_bidding_revenue
, cast(0 as double) as d_bid_won_bidding_revenue
, cast(0 as double) as r_bid_won_bidding_revenue
, cast(0 as bigint) as hylda_replacement_impression_gains
, cast(0 as bigint) as hylda_replacement_impression_forfeits
, "Unknown"                                                                   as placement_type_priority
, cast(array() as array<bigint>)                                              as audience_extension_deal_ids
, "FULL_VISIBILITY"                                                           as geo_state_visibility
, coalesce(network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")    as geo_dma_visibility
, "FULL_VISIBILITY"                                                           as geo_city_visibility
, "FULL_VISIBILITY"                                                           as geo_zipcode_visibility
, ""                                                                          as slot_avail_type
, "Not Applicable"                                                            as linear_decision_type
, cast(array() as array<int>)                                                 as standard_device_type_ids
, cast(-1 as int)                                                             as standard_environment_id
, cast(-1 as int)                                                             as standard_os_id
, cast(-1 as int)                                                             as standard_brand_id
, cast(-1 as int)                                                             as standard_channel_id
, cast(array() as array<int>)                                                 as standard_genre_ids
, cast(-1 as int)                                                             as content_form_id
, cast(-1 as int)                                                             as content_rating_id
, cast(array() as array<int>)                                                 as standard_language_ids
, cast(-1 as int)                                                             as stream_mode_id
, cast(-1 as int)                                                             as inventory_location_id
, cast(array() as array<bigint>)                                              as listing_ids
, cast(-1 as bigint)                                                          as inbound_order_id
, cast(array() as array<bigint>)                                              as inbound_listing_ids
, cast(-1 as bigint)                                                          as outbound_order_id
, cast(array() as array<bigint>)                                              as outbound_listing_ids
, cast(0 as bigint)                                                           as total_avails
, cast(0 as bigint)                                                           as total_unfilled_avails
, cast(0 as bigint)                                                           as opportunity
, cast(0 as bigint)                                                           as outbound_avails
, cast(0 as bigint)                                                           as outbound_unfilled_avails
, cast(0 as bigint)                                                           as outbound_opportunity
, cast(-1 as int)                                                             as ip_enabled_audience_id
, cast(-1 as int)                                                             as standard_programmer_id
--, sum(coalesce(cast(request.log_sampling.magnifier as bigint), cast(1 as bigint))) as request_count
, sum(if(idx.is_first_request =true, coalesce(cast(request.log_sampling.magnifier as bigint), cast(1 as bigint)), cast(0 as bigint))) as request_count
, coalesce(network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
, "FULL_VISIBILITY"                                                           as standard_brand_visibility
, "FULL_VISIBILITY"                                                           as standard_genre_visibility
, "FULL_VISIBILITY"                                                           as content_rating_visibility
, cast(0 as int)                                                              as supply_source
, cast(0 as int)                                                              as sales_channel
, "UNKNOWN"                                                                   as inbound_order_auction_type
, cast(0 as double)                                                           as ssp_clearing_revenue
, "Unknown"                                                                   as ssp_external_publisher_id
, coalesce(visitor.dma_code_id, cast(-1 as int))                              as user_dma_code_id
, "FULL_VISIBILITY"                                                           as standard_programmer_visibility
, cast(-1 as bigint)                                                          as bidder_seat_id
, ''                                                                          as global_currency_version
, cast(-1 as bigint)                                                          as global_currency_id
, coalesce(request.context.profile_id, cast(-1 as bigint))                    as profile_id
, coalesce(request.context.profile_type, 'UNKNOWN')                           as profile_type
, cast(array() as array<bigint>)                                              as inventory_package_ids
, cast(0 as double)                                                           as supply_acquisition_cost
, cast(0 as double)                                                           as supply_distribution_cost
, "FULL_VISIBILITY"                                                           as content_form_visibility
, cast(0 as int)                                                               as bit_flag_aim_product_category
, date_trunc("HOUR", from_unixtime(request.timestamp))                    as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(inventory.asset_chain) as network
where coalesce(request.extra_flags, cast(0 as bigint)) & 1024 = 1024
  and coalesce(network.role, "") = "CRO"
  and coalesce(network.network_id, cast(-1 as bigint)) = coalesce(request.context.video_cro_network_id, cast(-1 as bigint))
  and not (coalesce(request.extra_flags, cast(0 as bigint)) & 1073741824 = 1073741824 and coalesce(network.role, "") = "CRO" and coalesce(request.extra_flags, cast(0 as bigint)) & 16384 = 16384)
  and date_trunc("HOUR", from_unixtime(request.timestamp))  = to_timestamp("20260722080000", 'yyyyMMddHHmmss')
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 94, 95, 96, 97, 98, 99, 100, 101, 102,
    103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148
```

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **site\_section\_id** | 10729 | 10730 | **0** | **1** |
| **channel\_id** | 6350 | 6343 | **7** | **0** |
| **postal\_code** | 42355 | 42356 | **0** | **1** |

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **avails** | 16,545,098.00 | 16,562,442.00 | **+17,344.00** | +0.10% |
| **unconstrained\_avails** | 16,546,915.00 | 16,564,259.00 | **+17,344.00** | +0.10% |
| **gross\_ad\_views** | 138,884.00 | 124,885.00 | **-13,999.00** | -10.08% |
| **revenue** | 1,412.98 | 1,412.88 | **-0.10** | -0.01% |
| **r\_revenue** | 1,606.12 | 1,606.01 | **-0.10** | -0.01% |
| **bidding\_revenue** | 1,412.27 | 1,412.17 | **-0.10** | -0.01% |
| **r\_bidding\_revenue** | 1,467.58 | 1,467.47 | **-0.10** | -0.01% |
| **ad\_close** | 53.00 | 54.00 | **+1.00** | +1.89% |
| **total\_avails** | 16,126,073.00 | 16,256,101.00 | **+130,028.00** | +0.81% |
| **total\_unfilled\_avails** | 4,275,266.00 | 4,404,803.00 | **+129,537.00** | +3.03% |
| **opportunity** | 28,104,891.00 | 28,250,209.00 | **+145,318.00** | +0.52% |

- After applying is\_filtered (result below) almost all the dimensions and metrics are not matching

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **network\_id** | 587 | 229 | 358 | 0 |
| **content\_owner\_id** | 289 | 235 | 54 | 0 |
| **distributor\_id** | 272 | 234 | 38 | 0 |
| **transaction\_type** | 10 | 7 | 3 | 0 |
| **asset\_id** | 9715 | 4796 | 4919 | 0 |
| **series\_id** | 4178 | 2446 | 1732 | 0 |
| **asset\_group\_ids** | 8789 | 4733 | 4065 | 9 |
| **site\_section\_id** | 10729 | 7015 | 3715 | 1 |
| **site\_id** | 3089 | 1943 | 1146 | 0 |
| **site\_section\_group\_ids** | 7591 | 5020 | 2571 | 0 |
| **airing\_id** | 81 | 19 | 62 | 0 |
| **channel\_id** | 6350 | 6342 | 56 | 48 |
| **break\_id** | 123 | 25 | 98 | 0 |
| **delivery\_method** | 3 | 2 | 1 | 0 |
| **ad\_unit\_id** | 755 | 185 | 570 | 0 |
| **tracked\_audience\_item\_ids** | 18822 | 3522 | 15300 | 0 |
| **postal\_code** | 42355 | 37569 | 4789 | 3 |
| **postal\_code\_package\_ids** | 42901 | 11441 | 31463 | 3 |
| **user\_city\_id** | 28452 | 24097 | 4357 | 2 |
| **user\_state\_id** | 1726 | 1631 | 95 | 0 |
| **user\_dma\_code** | 1089 | 797 | 292 | 0 |
| **user\_country\_id** | 180 | 173 | 7 | 0 |
| **delivered\_platform\_browser\_id** | 8 | 7 | 1 | 0 |
| **operator\_zone\_id** | 908 | 907 | 1 | 0 |
| **placement\_type\_priority** | 6 | 4 | 2 | 0 |
| **linear\_decision\_type** | 5 | 4 | 1 | 0 |
| **standard\_device\_type\_ids** | 59 | 58 | 1 | 0 |
| **standard\_brand\_id** | 999 | 875 | 124 | 0 |
| **standard\_genre\_ids** | 7308 | 6493 | 815 | 0 |
| **standard\_language\_ids** | 40 | 38 | 2 | 0 |
| **inbound\_order\_id** | 2924 | 367 | 2557 | 0 |
| **outbound\_order\_id** | 2873 | 2852 | 21 | 0 |
| **outbound\_listing\_ids** | 3423 | 3397 | 26 | 0 |
| **standard\_programmer\_id** | 432 | 390 | 42 | 0 |
| **supply\_source** | 5 | 3 | 2 | 0 |
| **sales\_channel** | 6 | 5 | 1 | 0 |
| **inbound\_order\_auction\_type** | 3 | 1 | 2 | 0 |
| **ssp\_external\_publisher\_id** | 1358 | 1350 | 8 | 0 |
| **global\_currency\_version** | 7 | 2 | 5 | 0 |
| **global\_currency\_id** | 11 | 2 | 9 | 0 |
| **profile\_id** | 1333 | 923 | 410 | 0 |


| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **video\_starts** | 92,056.00 | 207.00 | -91,849.00 | -99.78% |
| **break\_starts** | 1,289.00 | 279.00 | -1,010.00 | -78.36% |
| **avails** | 16,545,098.00 | 148,435.00 | -16,396,663.00 | -99.10% |
| **unconstrained\_avails** | 16,546,915.00 | 148,435.00 | -16,398,480.00 | -99.10% |
| **unfilled\_avails** | 4,504,556.00 | 1,655.00 | -4,502,901.00 | -99.96% |
| **ad\_views** | 124,885.00 | 13,999.00 | -110,886.00 | -88.79% |
| **no\_ad\_views** | 8.00 | 10.00 | +2.00 | +25.00% |
| **gross\_ad\_views** | 138,884.00 | 13,999.00 | -124,885.00 | -89.92% |
| **clicks** | 64.00 | 0.00 | -64.00 | -100.00% |
| **no\_clicks** | 79,349.00 | 12,450.00 | -66,899.00 | -84.31% |
| **revenue** | 1,412.98 | 0.10 | -1,412.88 | -99.99% |
| **co\_revenue** | 450.84 | 0.00 | -450.84 | -100.00% |
| **d\_revenue** | 2.89 | 0.00 | -2.89 | -100.00% |
| **r\_revenue** | 1,606.12 | 0.10 | -1,606.01 | -99.99% |
| **bidding\_revenue** | 1,412.27 | 0.10 | -1,412.17 | -99.99% |
| **co\_bidding\_revenue** | 451.95 | 0.00 | -451.95 | -100.00% |
| **r\_bidding\_revenue** | 1,467.58 | 0.10 | -1,467.47 | -99.99% |
| **first\_quartile** | 121,497.00 | 13,913.00 | -107,584.00 | -88.55% |
| **middle\_quartile** | 120,985.00 | 13,907.00 | -107,078.00 | -88.51% |
| **third\_quartile** | 120,617.00 | 13,900.00 | -106,717.00 | -88.48% |
| **complete\_quartile** | 120,607.00 | 13,896.00 | -106,711.00 | -88.48% |
| **can\_quartile** | 122,354.00 | 12,900.00 | -109,454.00 | -89.46% |
| **ad\_expand** | 190.00 | 0.00 | -190.00 | -100.00% |
| **ad\_collapse** | 5.00 | 0.00 | -5.00 | -100.00% |
| **measurable\_ad\_expand\_collapse\_impression** | 28,008.00 | 0.00 | -28,008.00 | -100.00% |
| **ad\_mute** | 719.00 | 0.00 | -719.00 | -100.00% |
| **ad\_unmute** | 43.00 | 0.00 | -43.00 | -100.00% |
| **measurable\_ad\_mute\_unmute\_impression** | 41,115.00 | 0.00 | -41,115.00 | -100.00% |
| **ad\_rewind** | 6.00 | 0.00 | -6.00 | -100.00% |
| **measurable\_ad\_rewind\_impression** | 26,559.00 | 0.00 | -26,559.00 | -100.00% |
| **ad\_pause** | 922.00 | 0.00 | -922.00 | -100.00% |
| **ad\_resume** | 896.00 | 0.00 | -896.00 | -100.00% |
| **measurable\_ad\_pause\_resume\_impression** | 45,285.00 | 0.00 | -45,285.00 | -100.00% |
| **ad\_close** | 53.00 | 0.00 | -53.00 | -100.00% |
| **measurable\_ad\_close\_impression** | 13,707.00 | 0.00 | -13,707.00 | -100.00% |
| **ad\_accept\_invitation** | 3.00 | 0.00 | -3.00 | -100.00% |
| **measurable\_ad\_accept\_invitation\_minimize\_impression** | 20,348.00 | 0.00 | -20,348.00 | -100.00% |
| **ad\_insertion** | 344.00 | 0.00 | -344.00 | -100.00% |
| **ad\_bid\_won** | 4.00 | 0.00 | -4.00 | -100.00% |
| **bid\_won\_revenue** | 0.10 | 0.00 | -0.10 | -100.00% |
| **co\_bid\_won\_revenue** | 0.04 | 0.00 | -0.04 | -100.00% |
| **r\_bid\_won\_revenue** | 0.12 | 0.00 | -0.12 | -100.00% |
| **bid\_won\_bidding\_revenue** | 0.10 | 0.00 | -0.10 | -100.00% |
| **co\_bid\_won\_bidding\_revenue** | 0.04 | 0.00 | -0.04 | -100.00% |
| **r\_bid\_won\_bidding\_revenue** | 0.12 | 0.00 | -0.12 | -100.00% |
| **hylda\_replacement\_impression\_gains** | 1,498.00 | 0.00 | -1,498.00 | -100.00% |
| **hylda\_replacement\_impression\_forfeits** | 1,380.00 | 0.00 | -1,380.00 | -100.00% |
| **total\_avails** | 16,126,073.00 | 130,028.00 | -15,996,045.00 | -99.19% |
| **total\_unfilled\_avails** | 4,275,266.00 | 129,537.00 | -4,145,729.00 | -96.97% |
| **opportunity** | 28,104,891.00 | 145,318.00 | -27,959,573.00 | -99.48% |
| **ssp\_clearing\_revenue** | 0.09 | 0.00 | -0.09 | -100.00% |
| **supply\_acquisition\_cost** | 3.32 | 0.00 | -3.32 | -100.00% |
| **supply\_distribution\_cost** | 8.29 | 0.00 | -8.29 | -100.00% |

##  -------------------------------------------------------------------------------------------------------------------------------------------------------

## **Actual SUMMARY**

- **Failed checks:** Dimension values, Metric sums, Row-level hash
- Dimensions analyzed: 77 — differences found
- Metrics analyzed: 66 — differences found
- Row count: Control 6,280,666 / Stage 6,334,011 — mismatch
- Row hash diffs: 232,649 — mismatch

---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*  

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **asset\_group\_ids** | 8789 | 8798 | 0 | 9 |
| **site\_section\_id** | 10729 | 10730 | 0 | 1 |
| **channel\_id** | 6350 | 6398 | 0 | 48 |
| **postal\_code** | 42355 | 42358 | 0 | 3 |
| **postal\_code\_package\_ids** | 42901 | 42904 | 0 | 3 |
| **user\_city\_id** | 28452 | 28454 | 0 | 2 |



**Sample Values (first 5 dimensions with differences):**

**asset\_group\_ids:**  
*Only in STAGE (9 total):* \[900661102\], \[1522123705\], \[900661054\], \[900661034\], \[900649684\], \[900661081\], \[334565447\], \[1911274203\], \[897176384\]

**site\_section\_id:**  
*Only in STAGE (1 total):* 23880911

**channel\_id:**  
*Only in STAGE (48 total):* 900661054, 877418757, 114551291, 1841874622, 877423976, 877409190, 877476823, 877432687, 877429134, 877328818 ... (+ 38 more, see CSV)

**postal\_code:**  
*Only in STAGE (3 total):* EC1A, 46068, 05155

**postal\_code\_package\_ids:**  
*Only in STAGE (3 total):* \[1647 2535 4616 7997\], \[1347 1469 1674 1736 2016 2087 2096 2128 2341 4620\], \[1760 2562 2563 4731 7912\]

*... and 1 more dimensions with differences (see CSV attachment for complete list)*

---

**📊 METRIC SUM DIFFERENCES**  

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **video\_starts** | 92,056.00 | 92,263.00 | +207.00 | +0.22% |
| **break\_starts** | 1,289.00 | 1,568.00 | +279.00 | +21.64% |
| **avails** | 16,545,098.00 | 16,562,442.00 | +17,344.00 | +0.10% |
| **unconstrained\_avails** | 16,546,915.00 | 16,564,259.00 | +17,344.00 | +0.10% |
| **ad\_views** | 124,885.00 | 138,884.00 | +13,999.00 | +11.21% |
| **no\_ad\_views** | 8.00 | 18.00 | +10.00 | +125.00% |
| **no\_clicks** | 79,349.00 | 91,799.00 | +12,450.00 | +15.69% |
| **first\_quartile** | 121,497.00 | 135,410.00 | +13,913.00 | +11.45% |
| **middle\_quartile** | 120,985.00 | 134,892.00 | +13,907.00 | +11.49% |
| **third\_quartile** | 120,617.00 | 134,517.00 | +13,900.00 | +11.52% |
| **complete\_quartile** | 120,607.00 | 134,503.00 | +13,896.00 | +11.52% |
| **can\_quartile** | 122,354.00 | 135,254.00 | +12,900.00 | +10.54% |
| **ad\_close** | 53.00 | 54.00 | +1.00 | +1.89% |
| **total\_avails** | 16,126,073.00 | 16,256,101.00 | +130,028.00 | +0.81% |
| **total\_unfilled\_avails** | 4,275,266.00 | 4,404,803.00 | +129,537.00 | +3.03% |
| **opportunity** | 28,104,891.00 | 28,250,209.00 | +145,318.00 | +0.52% |



---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**  

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 6,280,666, Stage: 6,334,011, Diff: +53,345) |
| **Row Hash** | **MISMATCH** (Only in Control: 89,652, Only in Stage: 142,997) |



---

**🔬 COLUMN-LEVEL DIFF — 72,207 combos with metric diffs**  

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-07-22, hour=08, network_id=536418, content_owner_id=536418, distributor_id=536418...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=546491, content_owner_id=190200, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=529669, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=8.0000, stg=1.0000, -7.0000 **unconstrained\_avails\_sum**: ctrl=8.0000, stg=1.0000, -7.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=520311, distributor_id=-1...` | **avails\_sum**: ctrl=8.0000, stg=1.0000, -7.0000 **unconstrained\_avails\_sum**: ctrl=8.0000, stg=1.0000, -7.0000 |
| `date=2026-07-22, hour=08, network_id=536174, content_owner_id=536174, distributor_id=536174...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=534988, content_owner_id=534988, distributor_id=534988...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=531516, content_owner_id=500763, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=529826, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=529846, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=6.0000, stg=1.0000, -5.0000 **unconstrained\_avails\_sum**: ctrl=6.0000, stg=1.0000, -5.0000 |
| `date=2026-07-22, hour=08, network_id=534790, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 **unconstrained\_avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-07-22, hour=08, network_id=376521, content_owner_id=520024, distributor_id=-1...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 **unconstrained\_avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-07-22, hour=08, network_id=528947, content_owner_id=531516, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=545360, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 **unconstrained\_avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 |
| `date=2026-07-22, hour=08, network_id=545360, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 **unconstrained\_avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-07-22, hour=08, network_id=510839, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=520024, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 **unconstrained\_avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 |
| `date=2026-07-22, hour=08, network_id=545450, content_owner_id=520040, distributor_id=-1...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 **unconstrained\_avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-07-22, hour=08, network_id=515189, content_owner_id=516283, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=384777, content_owner_id=384777, distributor_id=384777...` | **ad\_views\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **no\_clicks\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **first\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **middle\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **third\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **complete\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **can\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=384777, content_owner_id=384777, distributor_id=384777...` | **ad\_views\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **no\_clicks\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **first\_quartile\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **middle\_quartile\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **third\_quartile\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **complete\_quartile\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **can\_quartile\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 |
| `date=2026-07-22, hour=08, network_id=384777, content_owner_id=520040, distributor_id=384777...` | **ad\_views\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **no\_clicks\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **first\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **middle\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **third\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **complete\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **can\_quartile\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=535082, content_owner_id=535082, distributor_id=535082...` | **total\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **opportunity\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 |
| `date=2026-07-22, hour=08, network_id=531516, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=536075, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=7.0000, stg=1.0000, -6.0000 **unconstrained\_avails\_sum**: ctrl=7.0000, stg=1.0000, -6.0000 |
| `date=2026-07-22, hour=08, network_id=534988, content_owner_id=534988, distributor_id=534988...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=516283, distributor_id=-1...` | **avails\_sum**: ctrl=6.0000, stg=1.0000, -5.0000 **unconstrained\_avails\_sum**: ctrl=6.0000, stg=1.0000, -5.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=523319, content_owner_id=520040, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=529041, content_owner_id=524972, distributor_id=-1...` | **avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 **unconstrained\_avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=536815, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=535367, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=523319, content_owner_id=520040, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=535261, content_owner_id=535261, distributor_id=535261...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=524565, content_owner_id=384777, distributor_id=-1...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **unconstrained\_avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-22, hour=08, network_id=534991, content_owner_id=534991, distributor_id=534991...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=534988, content_owner_id=534988, distributor_id=534988...` | **total\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **opportunity\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-07-22, hour=08, network_id=512029, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 **unconstrained\_avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 |
| `date=2026-07-22, hour=08, network_id=535082, content_owner_id=535082, distributor_id=535082...` | **total\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **opportunity\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 **unconstrained\_avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-07-22, hour=08, network_id=539674, content_owner_id=512116, distributor_id=-1...` | **avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 **unconstrained\_avails\_sum**: ctrl=5.0000, stg=1.0000, -4.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=169843, distributor_id=-1...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 **unconstrained\_avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-07-22, hour=08, network_id=535260, content_owner_id=535260, distributor_id=535260...` | **total\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **total\_unfilled\_avails\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 **opportunity\_sum**: ctrl=0.0000, stg=100.0000, +100.0000 |
| `date=2026-07-22, hour=08, network_id=537323, content_owner_id=169843, distributor_id=-1...` | **avails\_sum**: ctrl=7.0000, stg=1.0000, -6.0000 **unconstrained\_avails\_sum**: ctrl=7.0000, stg=1.0000, -6.0000 |
| `date=2026-07-22, hour=08, network_id=535029, content_owner_id=169843, distributor_id=-1...` | **avails\_sum**: ctrl=12.0000, stg=1.0000, -11.0000 **unconstrained\_avails\_sum**: ctrl=12.0000, stg=1.0000, -11.0000 |

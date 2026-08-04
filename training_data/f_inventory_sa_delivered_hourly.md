# f\_inventory\_sa\_delivered\_hourly

## New Diffs

Below list is all diffs that need further investigation (unknown diffs)

|  |  **Column Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | `opportunity``_in_played_slot` metrics | NO | NEEDS INVESTIGATION | The value seems way higher in Hoover++ than in Hoover. Needs to be investigated as to why. |
| 2 | `ssp_floor_revenue_in_request` | NO | NEEDS INVESTIGATION | same as above |
| 3 |  |  |  |  |

@Jerry, Edwin V TO UPDATE THE SECTION BELOW.

## New Diffs ( as on 3-Aug-2026)

- Removed reseller\_id, geo\_visibility since it’s not available in h++
- Removed process\_batch\_id, bit\_flag as the known issue
- updated `*.ack.flags & 256 = 0` and able to match many metrics and adding the final SQL below

```sql
CREATE TABLE IF NOT EXISTS fw1_stg.edwin.f_inventory_sa_delivered_hourly_stage AS 
    select batch_id                                                                                           as process_batch_id
     , coalesce(network.network_id, cast(-1 as long))                                                                   as network_id
     , coalesce(network.content_owner_network_id, cast(-1 as long))                                                     as content_owner_id
     , coalesce(network.distributor_network_id, cast(-1 as long))                                                     as distributor_id
     , coalesce(network.reseller_network_id, cast(-1 as long))                                                          as reseller_id
     , coalesce(network.role, "")                                                                                       as transaction_type
     , coalesce(ad_ack_ctx.ack.traffic_type, cast(0 as long))                                                                      as traffic_type
     , coalesce(network.bit_flags, cast(0 as long))
    + coalesce(ad_ctx.ad.bit_flags, cast(0 as long))
    + coalesce(request.bit_flags, cast(0 as long))
    + coalesce(ad_ack_ctx.ack.bit_flags, cast(0 as long))                                                                     as bit_flag
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                                     as user_country_id
     , coalesce(visitor.state_id, cast(-1 as int))                                                                      as user_state_id
     , coalesce(visitor.city_id, cast(-1 as int))                                                                       as user_city_id
     , coalesce(visitor.operator_zone_id, cast(-1 as long))                                                             as operator_zone_id
     , coalesce(visitor.postal_code, "-1")                                                                              as postal_code
     , coalesce(visitor.dma_code, cast(-1 as int))                                                                      as user_dma_code
     , coalesce(network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY")                                     as geo_country_visibility
     ,  "FULL_VISIBILITY"                                             as geo_visibility
     , coalesce(network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")                                       as geo_state_visibility
     , coalesce(network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")                                        as geo_city_visibility
     , coalesce(network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY")                                    as geo_zipcode_visibility
     , coalesce(network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")                                         as geo_dma_visibility
     , if(visitor.standard_device_type_child_id is null,
          cast(array() as array<int>),
          array(visitor.standard_device_type_child_id))                                                                  as standard_device_type_ids
     , coalesce(visitor.standard_environment_id, cast(-1 as int))                                                       as standard_environment_id
     , coalesce(visitor.standard_os_id, cast(-1 as int))                                                                as standard_os_id
     , coalesce(request.context.tv_network_id, cast(-1 as long))                                                        as tv_network_id
     , if(network.standard_brand_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_brand_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_brand_id
     , if(network.standard_programmer_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_programmer_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_programmer_id
     , if(network.standard_genre_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_genre_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                                   as standard_genre_ids
     , if(network.content_form_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.content_form_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as content_form_id
     , if(network.content_rating_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.content_rating_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as content_rating_id
     , if(network.standard_language_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_language_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                                   as standard_language_ids
     , coalesce(request.context.stream_mode_id, cast(-1 as int))                                                        as stream_mode_id
     , coalesce(request.context.inventory_location_id, cast(-1 as int))                                                 as inventory_location_id
     , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                                as ip_enabled_audience_id
     , coalesce(network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_brand_visibility
     , coalesce(network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_genre_visibility
     , coalesce(network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY")                                  as content_rating_visibility
     , cast(array() as array<long>)                                                                                     as listing_ids
     , coalesce(network.inbound_order_id, cast(-1 as long))                                                             as inbound_order_id
     , coalesce(network.inbound_listing_id, cast(array() as array<long>))                                               as inbound_listing_ids
     , coalesce(network.outbound_order_id, cast(-1 as long))                                                            as outbound_order_id
     , coalesce(network.outbound_listing_id, cast(array() as array<long>))                                              as outbound_listing_ids
     , coalesce(slot_ctx.slot.time_position_class, "Unknown")                                                                    as time_position_class
     , if(network.network_is_ad_owner, coalesce(ad_ctx.ad.placement_type_priority, "Unknown"), "Unknown")           as placement_type_priority
     , sum(coalesce(ad_ack_ctx.metrics.ad_impression, cast(0 as long)))                                                        as ad_views
     , sum(if(network.network_is_ad_owner, coalesce(ad_ack_ctx.metrics.no_ad_impression, cast(0 as long)), cast(0 as long)))   as no_ad_views
     , sum(coalesce(ad_ack_ctx.metrics.raw_ad_impression, cast(0 as long)))                                                    as gross_ad_views
     , sum(coalesce(ad_ack_ctx.metrics.click, cast(0 as long)))                                                                as clicks
     , sum(coalesce(ad_ack_ctx.metrics.no_click, cast(0 as long)))                                                             as no_clicks
     , sum(coalesce(ad_ack_ctx.networks[network.index].revenue, cast(0 as double)) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)))                                    as revenue
     , sum(coalesce(ad_ack_ctx.networks[network.index].content_owner_revenue, cast(0 as double)) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)))                      as co_revenue
     , sum(coalesce(ad_ack_ctx.networks[network.index].distributor_revenue, cast(0 as double)) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)))                        as d_revenue
     , sum(coalesce(ad_ack_ctx.networks[network.index].reseller_revenue, cast(0 as double)) * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)))                           as r_revenue
     , sum(coalesce(ad_ack_ctx.metrics.first_quartile, cast(0 as long)))                                                       as first_quartile
     , sum(coalesce(ad_ack_ctx.metrics.middle_quartile, cast(0 as long)))                                                      as middle_quartile
     , sum(coalesce(ad_ack_ctx.metrics.third_quartile, cast(0 as long)))                                                       as third_quartile
     , sum(coalesce(ad_ack_ctx.metrics.complete_quartile, cast(0 as long)))                                                    as complete_quartile
     , sum(coalesce(ad_ack_ctx.metrics.can_quartile, cast(0 as long)))                                                         as can_quartile
     , sum(coalesce(ad_ack_ctx.metrics.ad_expand, cast(0 as long)))                                                            as ad_expand
     , sum(coalesce(ad_ack_ctx.metrics.ad_collapse, cast(0 as long)))                                                          as ad_collapse
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_expand_collapse_impression, cast(0 as long)))                             as measurable_ad_expand_collapse_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_mute, cast(0 as long)))                                                              as ad_mute
     , sum(coalesce(ad_ack_ctx.metrics.ad_unmute, cast(0 as long)))                                                            as ad_unmute
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_mute_unmute_impression, cast(0 as long)))                                 as measurable_ad_mute_unmute_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_rewind, cast(0 as long)))                                                            as ad_rewind
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_rewind_impression, cast(0 as long)))                                      as measurable_ad_rewind_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_pause, cast(0 as long)))                                                             as ad_pause
     , sum(coalesce(ad_ack_ctx.metrics.ad_resume, cast(0 as long)))                                                            as ad_resume
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_pause_resume_impression, cast(0 as long)))                                as measurable_ad_pause_resume_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_close, cast(0 as long)))                                                             as ad_close
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_close_impression, cast(0 as long)))                                       as measurable_ad_close_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_accept_invitation, cast(0 as long)))                                                 as ad_accept_invitation
     , sum(coalesce(ad_ack_ctx.metrics.ad_minimize, cast(0 as long)))                                                          as ad_minimize
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_accept_invitation_minimize_impression, cast(0 as long)))                  as measurable_ad_accept_invitation_minimize_impression
     , sum(if(coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and coalesce(network.role, "") = "CRO" and coalesce(request.extra_flags, cast(0 as long)) & 16384 = 16384, cast(0 as long), coalesce(ad_ack_ctx.metrics.ad_insertion, cast(0 as long))))
    as ad_insertion
     , cast(0 as long)                                                                                                  as total_avails
     , cast(0 as long)                                                                                                  as total_unfilled_avails
     , cast(0 as long)                                                                                                  as opportunity
     , cast(0 as long)                                                                                                  as outbound_avails
     , cast(0 as long)                                                                                                  as outbound_unfilled_avails
     , cast(0 as long)                                                                                                  as outbound_opportunity
     , coalesce(network.carriage_inventory_owner_id, cast(-1 as long))                                                  as carriage_inventory_owner_id
     , if(network.standard_endpoint_owner_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_owner_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_endpoint_owner_id
     , if(network.standard_endpoint_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_endpoint_id
     , coalesce(network.outbound_exchange_order_id, cast(-1 as long))                                                   as outbound_exchange_order_id
     , coalesce(network.supply_source, cast(-1 as int))                                                                 as supply_source
     , coalesce(network.sales_channel, cast(-1 as int))                                                                 as sales_channel
     , coalesce(network.standard_endpoint_owner_visibility.report_aggregate, "FULL_VISIBILITY")                         as standard_endpoint_owner_visibility
     , coalesce(network.standard_endpoint_visibility.report_aggregate, "FULL_VISIBILITY")                               as standard_endpoint_visibility
     , coalesce(network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY")                                      as user_agent_visibility
     , coalesce(network.inbound_order_auction_type, "UNKNOWN")                                                          as inbound_order_auction_type
     , sum(if(coalesce(request.is_ssp_bidder_request, false) = true and ((coalesce(network.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or (coalesce(network.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    * coalesce(ad_ack_ctx.networks[network.index].ssp_clearing_revenue, cast(0 as double))
    * coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)))                                            as ssp_clearing_revenue
     , sum(if(coalesce(request.is_ssp_bidder_request, false) = true and ((coalesce(network.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 49)) > 0 or (coalesce(network.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 50)) > 0), 1, 0)
    * coalesce(ad_ack_ctx.metrics.ad_bid_won, cast(0 as long)))                                                         as ad_bid_won
     , if(network.standard_channel_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_channel_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_channel_id
     , if(network.standard_content_daypart_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_daypart_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_content_daypart_id
     , coalesce(request.bid_request.publisher_id, "Unknown")                                                            as ssp_external_publisher_id
     , coalesce(network.tracked_audience_item_ids, cast(array() as array<long>))                                        as tracked_audience_item_ids
     , coalesce(visitor.dma_code_id, cast(-1 as int))                                                                   as user_dma_code_id
     , coalesce(network.asset_id, cast(-1 as long))                                                                     as asset_id
     , coalesce(network.series_id, cast(-1 as long))                                                                    as series_id
     , coalesce(network.asset_group_ids, cast(array() as array<long>))                                                  as asset_group_ids
     , coalesce(network.site_section_id, cast(-1 as long))                                                              as site_section_id
     , coalesce(network.site_id, cast(-1 as long))                                                                      as site_id
     , coalesce(network.site_section_group_ids, cast(array() as array<long>))                                           as site_section_group_ids
     , coalesce(network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY")                             as standard_programmer_visibility
     , if(network.network_is_extra_item_owner, coalesce(ad_ctx.ad.ad_unit_id, cast(-1 as long)), cast(-1 as long))  as ad_unit_id
     , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                                as standard_publisher_id
     , coalesce(network.bidder_seat_id, cast(-1 as long))                                                               as bidder_seat_id
     , coalesce(request.global_currency_version, '')                                                                    as global_currency_version
     , coalesce(network.global_currency_id, cast(-1 as long))                                                           as global_currency_id
     , coalesce(request.context.standard_app_id, cast(-1 as long))                                                      as standard_app_id
     , coalesce(request.context.profile_id, cast(-1 as long))                                                         as profile_id
     , coalesce(request.context.profile_type, 'UNKNOWN')                                                                as profile_type
     , if(network.standard_content_series_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_series_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_content_series_id
     , if(network.standard_content_subscription_model_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_subscription_model_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_subscription_model_id
     , coalesce(request.context.standard_ssp_channel_id, cast(-1 as long))                                              as standard_ssp_channel_id
     , coalesce(request.context.standard_site_domain_id, cast(-1 as long))                                              as standard_site_domain_id
     , coalesce(visitor.standard_operator_id, cast(-1 as long))                                                         as standard_operator_id
     , coalesce(request.context.standard_iab_category_ids, cast(array() as array<long>))                                as standard_iab_category_ids
     , case
           when network.network_is_extra_item_owner then coalesce(ad_ctx.ad.matched_inventory_package_ids, cast(array() as array<long>))
           when network.sales_channel in (5,6) then coalesce(network.matched_inventory_package_ids, cast(array() as array<long>))
           else cast(array() as array<long>)
    end                                                                                                              as matched_inventory_package_ids
     , if(network.standard_content_territory_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_territory_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_territory_id
     , coalesce(visitor.platform_group, "-1")                                                                           as platform_group
     , coalesce(network.standard_content_series_visibility.report_aggregate, 'FULL_VISIBILITY')                         as standard_content_series_visibility
     , if(network.standard_content_credential_status_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_credential_status_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_credential_status_id
     , coalesce(visitor.platform_device_id, cast(-1 as long))                                                           as delivered_platform_device_id
     , coalesce(visitor.platform_browser_id, cast(-1 as long))                                                          as delivered_platform_browser_id
     , coalesce(visitor.platform_os_id, cast(-1 as long))                                                               as delivered_platform_os_id
     , cast(array() as array<long>)                                                                                     as inventory_package_ids
     , cast(0 as double)                                                                                                as ssp_floor_revenue_in_request
     , network.airing_id                                                                                                as airing_id
     , network.airing_channel_id                                                                                        as channel_id
     , coalesce(network.break_id, cast(-1 as long))                                                                     as break_id
     , ad_ctx.ad.ad_delivery_method                                                                                 as delivery_method
     , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                                         as standard_retailer_id
     , coalesce(network.standard_content_subscription_model_visibility.report_aggregate, 'FULL_VISIBILITY')             as standard_content_subscription_model_visibility
     , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                                     as standard_manufacturer_id
     , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                               as standard_app_bundle_id
     , sum(if(coalesce(network.role, "") in ('CRO'), coalesce(network.metrics.supply_acquisition_cost, cast(0 as double))*
                                                     coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)), cast(0 as double)))                           as supply_acquisition_cost
     , sum(if(coalesce(network.role, "") in ('CRO'), coalesce(network.metrics.supply_distribution_cost, cast(0 as double))*
                                                     coalesce(ad_ack_ctx.metrics.fire_event_revenue_ratio, cast(0 as int)), cast(0 as double)))                           as supply_distribution_cost
     , coalesce(network.standard_channel_visibility.report_aggregate, "FULL_VISIBILITY")                                as standard_channel_visibility
     , coalesce(network.content_form_visibility.report_aggregate, "FULL_VISIBILITY")                                    as content_form_visibility
     , if(network.supply_source != 3,
          coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
          cast(array() as array<bigint>))                                                                               as standard_content_viewership_profile_ids
     , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                                as standard_privacy_id
     , coalesce(request.context.standard_addressability_ids, cast(array() as array<bigint>))                            as standard_addressability_ids
     , cast(0 as long)                                                                                                  as avails
     , cast(0 as long)                                                                                                  as unconstrained_avails
     , cast(0 as long)                                                                                                  as unfilled_avails
     , cast(0 as long)                                                                                                  as constrained_inventory_opportunities_in_played_slot
     , cast(0 as double)                                                                                                as inbound_floor_revenue
     , if(network.supply_source != 3,
          coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                                  as standard_sport_entity_ids
     , coalesce(slot_ctx.slot.avail_type, "")                                                                                    as slot_avail_type
     , if(network.role = 'CRO', coalesce(ad_ctx.ad.linear_decision_type, "Not Applicable"), "Not Applicable")       as linear_decision_type
     , cast(0 as long)                                                                                                  as break_starts
     , date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as timestamp))                                                             as event_date
FROM fw1_hoover_prd.hoover_batch.transaction
         lateral view explode(slot_ctxes) as slot_ctx
         lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(ad_ctx.networks) as network
         lateral view explode(ad_ctx.ack_ctxes) as ad_ack_ctx
where ad_ack_ctx.ack.ack_entity_type = "ad"
  and ad_ack_ctx.ack.flags & 256 = 0
  and ad_ctx.ad.is_bumper = false
  and (!ad_ack_ctx.ack.is_private_impression or network.network_is_ad_owner or network.network_is_extra_item_owner)
  and date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as TIMESTAMP)) = date_trunc('HOUR', to_timestamp("20260722080000", 'yyyyMMddHHmmss'))
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
    109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135, 136, 139, 140,
    141, 142, 143, 149, 150, 151, 153
-- -- count = 88826
--
union all
-- -- ax on lsa
select batch_id                                                                                               as process_batch_id
     , coalesce(ad_ctx.ad.replaced_ad_network_id, cast(-1 as long))                                           as network_id
     , coalesce(network.content_owner_network_id, cast(-1 as long))                                           as content_owner_id
     , coalesce(network.distributor_network_id, cast(-1 as long))                                             as distributor_id
     , coalesce(ad_ctx.ad.replaced_ad_network_id, cast(-1 as long))                                           as reseller_id
     , coalesce(network.role, "")                                                                             as transaction_type
     , coalesce(ad_ack_ctx.ack.traffic_type, cast(0 as long))                                                 as traffic_type
     , coalesce(network.bit_flags, cast(0 as long))
    + coalesce(ad_ctx.ad.replaced_ad_bit_flags, cast(0 as long))
    + coalesce(request.bit_flags, cast(0 as long))
    +
       coalesce(ad_ack_ctx.ack.bit_flags, cast(0 as long))                                                    as bit_flag
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                           as user_country_id
     , coalesce(visitor.state_id, cast(-1 as int))                                                            as user_state_id
     , coalesce(visitor.city_id, cast(-1 as int))                                                             as user_city_id
     , coalesce(visitor.operator_zone_id, cast(-1 as long))                                                   as operator_zone_id
     , coalesce(visitor.postal_code, "-1")                                                                    as postal_code
     , coalesce(visitor.dma_code, cast(-1 as int))                                                            as user_dma_code
     , "FULL_VISIBILITY"                                                                                      as geo_country_visibility
     , "FULL_VISIBILITY"                                                                                      as geo_visibility
     , "FULL_VISIBILITY"                                                                                      as geo_state_visibility
     , "FULL_VISIBILITY"                                                                                      as geo_city_visibility
     , "FULL_VISIBILITY"                                                                                      as geo_zipcode_visibility
     , "FULL_VISIBILITY"                                                                                      as geo_dma_visibility
     , if(visitor.standard_device_type_child_id is null,
          cast(array() as array<int>),
          array(visitor.standard_device_type_child_id))                                                       as standard_device_type_ids
     , coalesce(visitor.standard_environment_id, cast(-1 as int))                                             as standard_environment_id
     , coalesce(visitor.standard_os_id, cast(-1 as int))                                                      as standard_os_id
     , coalesce(request.context.tv_network_id, cast(-1 as long))                                              as tv_network_id
     -- since network.networkIsCRO = true in where clause, no need add content sa limitation
     , coalesce(request.context.standard_brand_id, cast(-1 as int))                                           as standard_brand_id
     , coalesce(request.context.standard_programmer_id, cast(-1 as int))                                      as standard_programmer_id
     , coalesce(request.context.standard_genre_ids,
                cast(array() as array<int>))                                                                  as standard_genre_ids
     , coalesce(request.context.content_form_id, cast(-1 as int))                                             as content_form_id
     , coalesce(request.context.content_rating_id, cast(-1 as int))                                           as content_rating_id
     , coalesce(request.context.standard_language_ids,
                cast(array() as array<int>))                                                                  as standard_language_ids
     , coalesce(request.context.stream_mode_id, cast(-1 as int))                                              as stream_mode_id
     , coalesce(request.context.inventory_location_id, cast(-1 as int))                                       as inventory_location_id
     , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                      as ip_enabled_audience_id
     , "FULL_VISIBILITY"                                                                                      as standard_brand_visibility
     , "FULL_VISIBILITY"                                                                                      as standard_genre_visibility
     , "FULL_VISIBILITY"                                                                                      as content_rating_visibility
     , cast(array() as array<long >)                                                                          as listing_ids
     , cast(-1 as long)                                                                                       as inbound_order_id
     , cast(array() as array<long >)                                                                          as inbound_listing_ids
     , cast(-1 as long)                                                                                       as outbound_order_id
     , cast(array() as array<long >)                                                                          as outbound_listing_ids
     , coalesce(slot_ctx.slot.time_position_class, "Unknown")                                                 as time_position_class
     , "Unknown"                                                                                              as placement_type_priority
     , sum(coalesce(ad_ack_ctx.metrics.ad_impression, cast(0 as long)))                                       as ad_views
     , sum(if(network.network_is_ad_owner, coalesce(ad_ack_ctx.metrics.no_ad_impression, cast(0 as long)),
              cast(0 as long)))                                                                               as no_ad_views
     , sum(coalesce(ad_ack_ctx.metrics.raw_ad_impression, cast(0 as long)))                                   as gross_ad_views
     , sum(coalesce(ad_ack_ctx.metrics.click, cast(0 as long)))                                               as clicks
     , sum(coalesce(ad_ack_ctx.metrics.no_click, cast(0 as long)))                                            as no_clicks
     , cast(0 as double)                                                                                      as revenue
     , cast(0 as double)                                                                                      as co_revenue
     , cast(0 as double)                                                                                      as d_revenue
     , cast(0 as double)                                                                                      as r_revenue
     , sum(coalesce(ad_ack_ctx.metrics.first_quartile, cast(0 as long)))                                      as first_quartile
     , sum(coalesce(ad_ack_ctx.metrics.middle_quartile, cast(0 as long)))                                     as middle_quartile
     , sum(coalesce(ad_ack_ctx.metrics.third_quartile, cast(0 as long)))                                      as third_quartile
     , sum(coalesce(ad_ack_ctx.metrics.complete_quartile, cast(0 as long)))                                   as complete_quartile
     , sum(coalesce(ad_ack_ctx.metrics.can_quartile, cast(0 as long)))                                        as can_quartile
     , sum(coalesce(ad_ack_ctx.metrics.ad_expand, cast(0 as long)))                                           as ad_expand
     , sum(coalesce(ad_ack_ctx.metrics.ad_collapse, cast(0 as long)))                                         as ad_collapse
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_expand_collapse_impression,
                    cast(0 as long)))                                                                         as measurable_ad_expand_collapse_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_mute, cast(0 as long)))                                             as ad_mute
     , sum(coalesce(ad_ack_ctx.metrics.ad_unmute, cast(0 as long)))                                           as ad_unmute
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_mute_unmute_impression,
                    cast(0 as long)))                                                                         as measurable_ad_mute_unmute_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_rewind, cast(0 as long)))                                           as ad_rewind
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_rewind_impression,
                    cast(0 as long)))                                                                         as measurable_ad_rewind_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_pause, cast(0 as long)))                                            as ad_pause
     , sum(coalesce(ad_ack_ctx.metrics.ad_resume, cast(0 as long)))                                           as ad_resume
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_pause_resume_impression,
                    cast(0 as long)))                                                                         as measurable_ad_pause_resume_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_close, cast(0 as long)))                                            as ad_close
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_close_impression,
                    cast(0 as long)))                                                                         as measurable_ad_close_impression
     , sum(coalesce(ad_ack_ctx.metrics.ad_accept_invitation, cast(0 as long)))                                as ad_accept_invitation
     , sum(coalesce(ad_ack_ctx.metrics.ad_minimize, cast(0 as long)))                                         as ad_minimize
     , sum(coalesce(ad_ack_ctx.metrics.measurable_ad_accept_invitation_minimize_impression,
                    cast(0 as long)))                                                                         as measurable_ad_accept_invitation_minimize_impression
     , sum(if(coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and
              coalesce(network.role, "") = "CRO" and coalesce(request.extra_flags, cast(0 as long)) & 16384 = 16384,
              cast(0 as long), coalesce(ad_ack_ctx.metrics.ad_insertion, cast(0 as long))))
                                                                                                              as ad_insertion
     , cast(0 as long)                                                                                        as total_avails
     , cast(0 as long)                                                                                        as total_unfilled_avails
     , cast(0 as long)                                                                                        as opportunity
     , cast(0 as long)                                                                                        as outbound_avails
     , cast(0 as long)                                                                                        as outbound_unfilled_avails
     , cast(0 as long)                                                                                        as outbound_opportunity
     , cast(-1 as long)                                                                                       as carriage_inventory_owner_id
     , coalesce(request.context.standard_endpoint_owner_id,
                cast(-1 as int))                                                                              as standard_endpoint_owner_id
     , coalesce(request.context.standard_endpoint_id, cast(-1 as int))                                        as standard_endpoint_id
     , cast(-1 as long)                                                                                       as outbound_exchange_order_id
     , cast(0 as int)                                                                                         as supply_source
     , cast(2 as int)                                                                                         as sales_channel
     , "FULL_VISIBILITY"                                                                                      as standard_endpoint_owner_visibility
     , "FULL_VISIBILITY"                                                                                      as standard_endpoint_visibility
     , "FULL_VISIBILITY"                                                                                      as user_agent_visibility
     , "UNKNOWN"                                                                                              as inbound_order_auction_type
     , cast(0 as double)                                                                                      as ssp_clearing_revenue
     , cast(0 as long)                                                                                        as ad_bid_won
     , coalesce(request.context.standard_channel_id, cast(-1 as int))                                         as standard_channel_id
     , coalesce(request.context.standard_content_daypart_id,
                cast(-1 as int))                                                                              as standard_content_daypart_id
     , "Unknown"                                                                                              as ssp_external_publisher_id
     , cast(array() as array<long >)                                                                          as tracked_audience_item_ids
     , coalesce(visitor.dma_code_id, cast(-1 as int))                                                         as user_dma_code_id
     , cast(-1 as long)                                                                                       as asset_id
     , cast(-1 as long)                                                                                       as series_id
     , cast(array() as array<long >)                                                                          as asset_group_ids
     , cast(-1 as long)                                                                                       as site_section_id
     , cast(-1 as long)                                                                                       as site_id
     , cast(array() as array<long >)                                                                          as site_section_group_ids
     , "FULL_VISIBILITY"                                                                                      as standard_programmer_visibility
     , coalesce(ad_ctx.ad.replaced_ad_unit_id, cast(-1 as long))                                              as ad_unit_id
     , cast(-1 as long)                                                                                       as standard_publisher_id
     , cast(-1 as long)                                                                                       as bidder_seat_id
     , ''                                                                                                     as global_currency_version
     , cast(-1 as long)                                                                                       as global_currency_id
     , cast(-1 as long)                                                                                       as standard_app_id
     , coalesce(request.context.profile_id, cast(-1 as long))                                                 as profile_id
     , coalesce(request.context.profile_type, 'UNKNOWN')                                                      as profile_type
     , coalesce(request.context.standard_content_series_id,
                cast(-1 as int))                                                                              as standard_content_series_id
     , coalesce(request.context.standard_content_subscription_model_id,
                cast(-1 as bigint))                                                                           as standard_content_subscription_model_id
     , cast(-1 as long)                                                                                       as standard_ssp_channel_id
     , cast(-1 as long)                                                                                       as standard_site_domain_id
     , coalesce(visitor.standard_operator_id, cast(-1 as long))                                               as standard_operator_id
     , cast(array() as array<long >)                                                                          as standard_iab_category_ids
     , cast(array() as array<long >)                                                                          as matched_inventory_package_ids
     , coalesce(request.context.standard_content_territory_id,
                cast(-1 as bigint))                                                                           as standard_content_territory_id
     , coalesce(visitor.platform_group, "-1")                                                                 as platform_group
     , "FULL_VISIBILITY"                                                                                      as standard_content_series_visibility
     , coalesce(request.context.standard_content_credential_status_id,
                cast(-1 as bigint))                                                                           as standard_content_credential_status_id
     , coalesce(visitor.platform_device_id, cast(-1 as long))                                                 as delivered_platform_device_id
     , coalesce(visitor.platform_browser_id, cast(-1 as long))                                                as delivered_platform_browser_id
     , coalesce(visitor.platform_os_id, cast(-1 as long))                                                     as delivered_platform_os_id
     , cast(array() as array<long >)                                                                          as inventory_package_ids
     , cast(0 as double)                                                                                      as ssp_floor_revenue_in_request
     , cast(-1 as long)                                                                                       as airing_id
     , cast(-1 as long)                                                                                       as channel_id
     , cast(-1 as long)                                                                                       as break_id
     , ad_ctx.ad.ad_delivery_method                                                                           as delivery_method
     , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                               as standard_retailer_id
     , "FULL_VISIBILITY"                                                                                      as standard_content_subscription_model_visibility
     , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                           as standard_manufacturer_id
     , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                     as standard_app_bundle_id
     , cast(0 as double)                                                                                      as supply_acquisition_cost
     , cast(0 as double)                                                                                      as supply_distribution_cost
     , "FULL_VISIBILITY"                                                                                      as standard_channel_visibility
     , "FULL_VISIBILITY"                                                                                      as content_form_visibility
     , if(network.supply_source != 3,
          coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
          cast(array() as array<bigint>))                                                                     as standard_content_viewership_profile_ids
     , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                      as standard_privacy_id
     , coalesce(request.context.standard_addressability_ids,
                cast(array() as array<bigint>))                                                               as standard_addressability_ids
     , cast(0 as long)                                                                                        as avails
     , cast(0 as long)                                                                                        as unconstrained_avails
     , cast(0 as long)                                                                                        as unfilled_avails
     , cast(0 as long)                                                                                        as constrained_inventory_opportunities_in_played_slot
     , cast(0 as double)                                                                                      as inbound_floor_revenue
     , if(network.supply_source != 3,
          coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long >)),
          cast(array() as array<long >))                                                                      as standard_sport_entity_ids
     , coalesce(slot_ctx.slot.avail_type, "")                                                                 as slot_avail_type
     , if(network.role = 'CRO', coalesce(ad_ctx.ad.linear_decision_type, "Not Applicable"),
          "Not Applicable")                                                                                   as linear_decision_type
     , cast(0 as long)                                                                                        as break_starts
     , date_trunc('HOUR', cast(ad_ack_ctx.ack.timestamp as timestamp))                                        as event_date
FROM fw1_hoover_prd.hoover_batch.transaction
         lateral view explode(slot_ctxes) as slot_ctx
         lateral view explode(slot_ctx.ad_ctxes) as ad_ctx
         lateral view explode(ad_ctx.networks) as network
         lateral view explode(ad_ctx.ack_ctxes) as ad_ack_ctx
         lateral view explode(ad_ack_ctx.networks) as ad_ack_networks
where ad_ack_ctx.ack.ack_entity_type = "ad"
  and ad_ack_ctx.ack.flags & 256 = 0
  and ad_ctx.ad.is_bumper = false
  and network.network_is_ad_owner = true
  and ad_ctx.ad.is_ax = true -- ad is ax ad
  and coalesce(network.role
    , "") = "CRO"
  and date_trunc('HOUR'
    , cast (ad_ack_ctx.ack.timestamp as TIMESTAMP)) = date_trunc('HOUR'
    , to_timestamp("20260722080000"
    , 'yyyyMMddHHmmss'))
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
    106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135,
    136, 139, 140, 141, 142, 143, 149, 150, 151, 153
-- count = 746

UNION ALL

-- inbound avails/opportunity
select batch_id                                                                                          as process_batch_id
        , coalesce(network.network_id, cast(-1 as long))                                                                   as network_id
        , coalesce(network.content_owner_network_id, cast(-1 as long))                                                     as content_owner_id
        , coalesce(network.distributor_network_id, cast(-1 as long))                                                     as distributor_id
        , coalesce(null, cast(-1 as long))                                                          as reseller_id -- only an ad network level field
        , if(network.role is null, "", concat(network.role, "V"))                                                          as transaction_type
        , coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as long))                                                                      as traffic_type
        , coalesce(network.bit_flags, cast(0 as long)) + coalesce(request.bit_flags, cast(0 as long))                      as bit_flag
        , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                                     as user_country_id
        , coalesce(visitor.state_id, cast(-1 as int))                                                                      as user_state_id
        , coalesce(visitor.city_id, cast(-1 as int))                                                                       as user_city_id
        , coalesce(visitor.operator_zone_id, cast(-1 as long))                                                             as operator_zone_id
        , coalesce(visitor.postal_code, "-1")                                                                              as postal_code
        , coalesce(visitor.dma_code, cast(-1 as int))                                                                      as user_dma_code
        , coalesce(network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY")                                     as geo_country_visibility
        ,"FULL_VISIBILITY"                                             as geo_visibility
        , coalesce(network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")                                       as geo_state_visibility
        , coalesce(network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")                                        as geo_city_visibility
        , coalesce(network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY")                                    as geo_zipcode_visibility
        , coalesce(network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")                                         as geo_dma_visibility
        , if(visitor.standard_device_type_child_id is null,
    cast(array() as array<int>),
    array(visitor.standard_device_type_child_id))                                                                  as standard_device_type_ids
        , coalesce(visitor.standard_environment_id, cast(-1 as int))                                                       as standard_environment_id
        , coalesce(visitor.standard_os_id, cast(-1 as int))                                                                as standard_os_id
        , coalesce(request.context.tv_network_id, cast(-1 as long))                                                        as tv_network_id
        , if(network.standard_brand_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_brand_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_brand_id
        , if(network.standard_programmer_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_programmer_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_programmer_id
        , if(network.standard_genre_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_genre_ids, cast(array() as array<int>)),
    cast(array() as array<int>))                                                                                   as standard_genre_ids
        , if(network.content_form_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.content_form_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as content_form_id
        , if(network.content_rating_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.content_rating_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as content_rating_id
        , if(network.standard_language_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_language_ids, cast(array() as array<int>)),
    cast(array() as array<int>))                                                                                   as standard_language_ids
        , coalesce(request.context.stream_mode_id, cast(-1 as int))                                                        as stream_mode_id
        , coalesce(request.context.inventory_location_id, cast(-1 as int))                                                 as inventory_location_id
        , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                                as ip_enabled_audience_id
        , coalesce(network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_brand_visibility
        , coalesce(network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_genre_visibility
        , coalesce(network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY")                                  as content_rating_visibility
        , cast(array() as array<long>)                                                                                     as listing_ids
        , coalesce(network.inbound_order_id, cast(-1 as long))                                                             as inbound_order_id
        , coalesce(network.inbound_listing_id, cast(array() as array<long>))                                               as inbound_listing_ids
        , cast(-1 as long)                                                                                                 as outbound_order_id
        , cast(array() as array<long>)                                                                                     as outbound_listing_ids
        , coalesce(slot_ctx.slot.time_position_class, "Unknown")                                                                    as time_position_class
        , "Unknown"                                                                                                        as placement_type_priority
        , cast(0 as long)                                                                                                  as ad_views
        , cast(0 as long)                                                                                                  as no_ad_views
        , cast(0 as long)                                                                                                  as gross_ad_views
        , cast(0 as long)                                                                                                  as clicks
        , cast(0 as long)                                                                                                  as no_clicks
        , cast(0 as double)                                                                                                as revenue
        , cast(0 as double)                                                                                                as co_revenue
        , cast(0 as double)                                                                                                as d_revenue
        , cast(0 as double)                                                                                                as r_revenue
        , cast(0 as long)                                                                                                  as first_quartile
        , cast(0 as long)                                                                                                  as middle_quartile
        , cast(0 as long)                                                                                                  as third_quartile
        , cast(0 as long)                                                                                                  as complete_quartile
        , cast(0 as long)                                                                                                  as can_quartile
        , cast(0 as long)                                                                                                  as ad_expand
        , cast(0 as long)                                                                                                  as ad_collapse
        , cast(0 as long)                                                                                                  as measurable_ad_expand_collapse_impression
        , cast(0 as long)                                                                                                  as ad_mute
        , cast(0 as long)                                                                                                  as ad_unmute
        , cast(0 as long)                                                                                                  as measurable_ad_mute_unmute_impression
        , cast(0 as long)                                                                                                  as ad_rewind
        , cast(0 as long)                                                                                                  as measurable_ad_rewind_impression
        , cast(0 as long)                                                                                                  as ad_pause
        , cast(0 as long)                                                                                                  as ad_resume
        , cast(0 as long)                                                                                                  as measurable_ad_pause_resume_impression
        , cast(0 as long)                                                                                                  as ad_close
        , cast(0 as long)                                                                                                  as measurable_ad_close_impression
        , cast(0 as long)                                                                                                  as ad_accept_invitation
        , cast(0 as long)                                                                                                  as ad_minimize
        , cast(0 as long)                                                                                                  as measurable_ad_accept_invitation_minimize_impression
        , cast(0 as long)                                                                                                  as ad_insertion
        , sum(coalesce(slot_ack_network.total_avails_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))             as total_avails
        , sum(coalesce(slot_ack_network.total_unfilled_avails_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))    as total_unfilled_avails
        , sum(coalesce(slot_ack_network.opportunity_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))              as opportunity
        , cast(0 as long)                                                                                                  as outbound_avails
        , cast(0 as long)                                                                                                  as outbound_unfilled_avails
        , cast(0 as long)                                                                                                  as outbound_opportunity
        , coalesce(network.carriage_inventory_owner_id, cast(-1 as long))                                                  as carriage_inventory_owner_id
        , if(network.standard_endpoint_owner_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_endpoint_owner_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_endpoint_owner_id
        , if(network.standard_endpoint_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_endpoint_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_endpoint_id
        , cast(-1 as long)                                                                                                 as outbound_exchange_order_id
        , coalesce(network.supply_source, cast(-1 as int))                                                                 as supply_source
        , cast(0 as int)                                                                                                   as sales_channel
        , coalesce(network.standard_endpoint_owner_visibility.report_aggregate, "FULL_VISIBILITY")                         as standard_endpoint_owner_visibility
        , coalesce(network.standard_endpoint_visibility.report_aggregate, "FULL_VISIBILITY")                               as standard_endpoint_visibility
        , coalesce(network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY")                                      as user_agent_visibility
        , coalesce(network.inbound_order_auction_type, "UNKNOWN")                                                          as inbound_order_auction_type
        , cast(0 as double)                                                                                                as ssp_clearing_revenue
        , cast(0 as long)                                                                                                  as ad_bid_won
        , if(network.standard_channel_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_channel_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_channel_id
        , if(network.standard_content_daypart_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_content_daypart_id, cast(-1 as int)),
    cast(-1 as int))                                                                                               as standard_content_daypart_id
        , coalesce(request.bid_request.publisher_id, "Unknown")                                                            as ssp_external_publisher_id
        , coalesce(network.tracked_audience_item_ids, cast(array() as array<long>))                                        as tracked_audience_item_ids
        , coalesce(visitor.dma_code_id, cast(-1 as int))                                                                   as user_dma_code_id
        , coalesce(network.asset_id, cast(-1 as long))                                                                     as asset_id
        , coalesce(network.series_id, cast(-1 as long))                                                                    as series_id
        , coalesce(network.asset_group_ids, cast(array() as array<long>))                                                  as asset_group_ids
        , coalesce(network.site_section_id, cast(-1 as long))                                                              as site_section_id
        , coalesce(network.site_id, cast(-1 as long))                                                                      as site_id
        , coalesce(network.site_section_group_ids, cast(array() as array<long>))                                           as site_section_group_ids
        , coalesce(network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY")                             as standard_programmer_visibility
        , if(network.network_is_ad_unit_owner, coalesce(slot_ctx.slot.ad_unit_id, cast(-1 as long)), cast(-1 as long))              as ad_unit_id
        , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                                as standard_publisher_id
        , coalesce(network.bidder_seat_id, cast(-1 as long))                                                               as bidder_seat_id
        , ''                                                                                                               as global_currency_version
        , cast(-1 as long)                                                                                                 as global_currency_id
        , coalesce(request.context.standard_app_id, cast(-1 as long))                                                      as standard_app_id
        , coalesce(request.context.profile_id, cast(-1 as long))                                                         as profile_id
        , coalesce(request.context.profile_type, 'UNKNOWN')                                                                as profile_type
        , if(network.standard_content_series_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_content_series_id, cast(-1 as int)),
    cast(-1 as int))                                                                                              as standard_content_series_id
        , if(network.standard_content_subscription_model_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_content_subscription_model_id, cast(-1 as bigint)),
    cast(-1 as bigint))                                                                                           as standard_content_subscription_model_id
        , coalesce(request.context.standard_ssp_channel_id, cast(-1 as long))                                              as standard_ssp_channel_id
        , coalesce(request.context.standard_site_domain_id, cast(-1 as long))                                              as standard_site_domain_id
        , coalesce(visitor.standard_operator_id, cast(-1 as long))                                                         as standard_operator_id
        , coalesce(request.context.standard_iab_category_ids, cast(array() as array<long>))                                as standard_iab_category_ids
        , cast(array() as array<long>)                                                                                     as matched_inventory_package_ids
        , if(network.standard_content_territory_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_content_territory_id, cast(-1 as bigint)),
    cast(-1 as bigint))                                                                                           as standard_content_territory_id
        , coalesce(visitor.platform_group, "-1")                                                                           as platform_group
        , coalesce(network.standard_content_series_visibility.report_aggregate, 'FULL_VISIBILITY')                         as standard_content_series_visibility
        , if(network.standard_content_credential_status_visibility.report_aggregate is not null or network.supply_source != 3,
    coalesce(request.context.standard_content_credential_status_id, cast(-1 as bigint)),
    cast(-1 as bigint))                                                                                           as standard_content_credential_status_id
        , coalesce(visitor.platform_device_id, cast(-1 as long))                                                           as delivered_platform_device_id
        , coalesce(visitor.platform_browser_id, cast(-1 as long))                                                          as delivered_platform_browser_id
        , coalesce(visitor.platform_os_id, cast(-1 as long))                                                               as delivered_platform_os_id
        , cast(array() as array<long>)                                                                                     as inventory_package_ids
        , sum(if(coalesce(request.is_ssp_bidder_request, false) = true, 1, 0)
    * coalesce(network.floor_price, cast(0 as double))
    * coalesce(slot_ack_network.opportunity_in_played_slot, cast(0 as int))
    * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)) / 1000)                                             as ssp_floor_revenue_in_request
        , network.airing_id                                                                                                as airing_id
        , network.airing_channel_id                                                                                        as channel_id
        , coalesce(network.break_id, cast(-1 as long))                                                                     as break_id
        , ""                                                                                                               as delivery_method
        , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                                         as standard_retailer_id
        , coalesce(network.standard_content_subscription_model_visibility.report_aggregate, 'FULL_VISIBILITY')             as standard_content_subscription_model_visibility
        , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                                     as standard_manufacturer_id
        , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                               as standard_app_bundle_id
        , cast(0 as double)                                                                                                as supply_acquisition_cost
        , cast(0 as double)                                                                                                as supply_distribution_cost
        , coalesce(network.standard_channel_visibility.report_aggregate, "FULL_VISIBILITY")                                as standard_channel_visibility
        , coalesce(network.content_form_visibility.report_aggregate, "FULL_VISIBILITY")                                    as content_form_visibility
        , if(network.supply_source != 3,
    coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
    cast(array() as array<bigint>))                                                                               as standard_content_viewership_profile_ids
        , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                                as standard_privacy_id
        , coalesce(request.context.standard_addressability_ids, cast(array() as array<bigint>))                            as standard_addressability_ids
        , sum(coalesce(slot_ack_network.avails_in_played_slot, cast(0 as int)) * coalesce(1, cast(0 as int)))                          as avails
        , sum(coalesce(slot_ack_network.unconstrained_avails_in_played_slot, cast(0 as int)) * coalesce(1, cast(0 as int)))            as unconstrained_avails
        , sum(coalesce(slot_ack_network.unfilled_avails_in_played_slot, cast(0 as int)) * coalesce(1, cast(0 as int)))                 as unfilled_avails
        , sum(if(not((coalesce(slot_ctx.slot.flags, 0) & 8 > 0 or coalesce(slot_ctx.slot.flags, 0) & 1 > 0 or coalesce(slot_ctx.slot.flags, 0) & 2 > 0) and coalesce(slot_ctx.slot.num_ads, 0) = 0), 1, 0)
    * cast(
    case
    when coalesce(slot_ctx.slot.flags, 0) & 64 != 0
    then 0
    when coalesce(slot_ctx.slot.flags, 0) & 8 = 0 and (coalesce(slot_ctx.slot.flags, 0) & 1 > 0 or coalesce(slot_ctx.slot.flags, 0) & 2 > 0) and coalesce(slot_ctx.slot.num_ads, 0) = 0
    then 0
    when (coalesce(request.extra_flags2, cast(0 as long)) & 8) = 8
    then coalesce(slot_ack_network.raw_opportunity_in_played_slot, 0) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when slot_ctx.slot.time_position_class in ('display', 'in-player-display')
    then if(coalesce(slot_ctx.slot.num_ads, 0) = 0, 1, slot_ctx.slot.num_ads) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 1 or (network.supply_source = 5 and coalesce(network.inbound_order_type, '') = 'CARRIAGE_ORDER')
    then (coalesce(slot_ctx.slot.num_ads, 0) + coalesce(slot_ctx.slot.unfilled_avails, greatest(coalesce(slot_ctx.slot.max_ads, 0) - coalesce(slot_ctx.slot.num_ads, 0), 0)))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 3
    then if(coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0) < coalesce(slot_ctx.slot.num_ads, 0)
        , coalesce(slot_ctx.slot.num_ads, 0)
        , coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0)
    ) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 5 and coalesce(network.inbound_order_type, '') = 'MARKETPLACE_ORDER' and coalesce(network.inbound_order_transaction_type, '') = 'GUARANTEED'
    then (coalesce(network.ad_filling_status.initial_filled_ad_num, 0) + coalesce(network.ad_filling_status.unified_unfilled_opp, 0))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source in (5,6)
    then (coalesce(network.ad_filling_status.filled_ad_num, 0)+ coalesce(slot_ctx.slot.unfilled_avails, greatest(coalesce(slot_ctx.slot.max_ads, 0) - coalesce(slot_ctx.slot.num_ads, 0), 0)))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    else
    array_max(array(
    coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0),
    coalesce(slot_ack_network.raw_opportunity_in_played_slot,0),
    coalesce(network.ad_filling_status.filled_ad_num, 0)
    )) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    end as long))                                                                                              as constrained_inventory_opportunities_in_played_slot
        , sum(if(network.supply_source in (1, 3), 0, 1)
    * coalesce(network.floor_price, cast(0 as double))
    * if(not((coalesce(slot_ctx.slot.flags, 0) & 8 > 0 or coalesce(slot_ctx.slot.flags, 0) & 1 > 0 or coalesce(slot_ctx.slot.flags, 0) & 2 > 0) and coalesce(slot_ctx.slot.num_ads, 0) = 0), 1, 0)
    * cast(
    case
    when coalesce(slot_ctx.slot.flags, 0) & 64 != 0
    then 0
    when coalesce(slot_ctx.slot.flags, 0) & 8 = 0 and (coalesce(slot_ctx.slot.flags, 0) & 1 > 0 or coalesce(slot_ctx.slot.flags, 0) & 2 > 0) and coalesce(slot_ctx.slot.num_ads, 0) = 0
    then 0
    when (coalesce(request.extra_flags2, cast(0 as long)) & 8) = 8
    then coalesce(slot_ack_network.raw_opportunity_in_played_slot, 0) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when slot_ctx.slot.time_position_class in ('display', 'in-player-display')
    then if(coalesce(slot_ctx.slot.num_ads, 0) = 0, 1, slot_ctx.slot.num_ads) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 1 or (network.supply_source = 5 and coalesce(network.inbound_order_type, '') = 'CARRIAGE_ORDER')
    then (coalesce(slot_ctx.slot.num_ads, 0) + coalesce(slot_ctx.slot.unfilled_avails, greatest(coalesce(slot_ctx.slot.max_ads, 0) - coalesce(slot_ctx.slot.num_ads, 0), 0)))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 3
    then if(coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0) < coalesce(slot_ctx.slot.num_ads, 0)
        , coalesce(slot_ctx.slot.num_ads, 0)
        , coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0)
    ) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source = 5 and coalesce(network.inbound_order_type, '') = 'MARKETPLACE_ORDER' and coalesce(network.inbound_order_transaction_type, '') = 'GUARANTEED'
    then (coalesce(network.ad_filling_status.initial_filled_ad_num, 0) + coalesce(network.ad_filling_status.unified_unfilled_opp, 0))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    when network.supply_source in (5,6)
    then (coalesce(network.ad_filling_status.filled_ad_num, 0)+ coalesce(slot_ctx.slot.unfilled_avails, greatest(coalesce(slot_ctx.slot.max_ads, 0) - coalesce(slot_ctx.slot.num_ads, 0), 0)))
    * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    else
    array_max(array(
    coalesce(slot_ack_network.raw_total_avails_in_played_slot, 0),
    coalesce(slot_ack_network.raw_opportunity_in_played_slot,0),
    coalesce(network.ad_filling_status.filled_ad_num, 0)
    )) * coalesce(slot_ack_ctx.metrics.slot_impression, 0)
    end as long)
    / 1000)                                                                                                        as inbound_floor_revenue
        , if(network.supply_source != 3,
    coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long>)),
    cast(array() as array<long>))                                                                                  as standard_sport_entity_ids
        , coalesce(slot_ctx.slot.avail_type, "")                                                                                    as slot_avail_type
        , "Not Applicable"                                                                                                 as linear_decision_type
        , cast(0 as long)                                                                                                  as break_starts
        , date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp))                                                             as event_date
from fw1_hoover_prd.hoover_batch.transaction
    lateral view explode(slot_ctxes) as slot_ctx
    lateral view explode(slot_ctx.networks) as network
    lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
    lateral view explode(slot_ack_ctx.networks) as slot_ack_network
where slot_ack_ctx.ack.ack_entity_type = "slot"
  and slot_ack_ctx.ack.flags & 256 = 0
  and coalesce(slot_ctx.slot.flags, cast(0 as long)) & 64 = 0 -- not parent slot
-- remove zero rows
  and ((
    coalesce(0, cast(0 as int)) != 0
  and (
    coalesce(slot_ack_network.avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(slot_ack_network.unconstrained_avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(slot_ack_network.unfilled_avails_in_played_slot, cast(0 as int)) != 0
    )
    ) or (
    coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)) != 0
  and (
    coalesce(slot_ack_network.total_avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(slot_ack_network.total_unfilled_avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(slot_ack_network.opportunity_in_played_slot, cast(0 as int)) != 0
    )
    ))
    and date_trunc('HOUR', cast (slot_ack_ctx.ack.timestamp as TIMESTAMP)) = date_trunc('HOUR', to_timestamp("20260722080000", 'yyyyMMddHHmmss'))

group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
35, 36, 37, 38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135, 136,
 139, 140, 141, 142, 143, 149, 150, 151, 153
-- 3734240
UNION ALL

-- outbound avails/opportunity
select batch_id                                                                                          as process_batch_id
     , coalesce(network.network_id, cast(-1 as long))                                                                   as network_id
     , coalesce(network.content_owner_network_id, cast(-1 as long))                                                     as content_owner_id
     , coalesce(network.distributor_network_id, cast(-1 as long))                                                     as distributor_id
     , coalesce(outbound.down_network_id, cast(-1 as long))                                                             as reseller_id
     , if(network.role is null, "", concat(network.role, "V"))                                                          as transaction_type
     , coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as long))                                                                      as traffic_type
     , coalesce(network.bit_flags, cast(0 as long))
    + coalesce(request.bit_flags, cast(0 as long))
    + coalesce(outbound.bit_flags, cast(0 as long))                                                                as bit_flag
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                                     as user_country_id
     , coalesce(visitor.state_id, cast(-1 as int))                                                                      as user_state_id
     , coalesce(visitor.city_id, cast(-1 as int))                                                                       as user_city_id
     , coalesce(visitor.operator_zone_id, cast(-1 as long))                                                             as operator_zone_id
     , coalesce(visitor.postal_code, "-1")                                                                              as postal_code
     , coalesce(visitor.dma_code, cast(-1 as int))                                                                      as user_dma_code
     , coalesce(network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY")                                     as geo_country_visibility
     , "FULL_VISIBILITY"                                             as geo_visibility
     , coalesce(network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")                                       as geo_state_visibility
     , coalesce(network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")                                        as geo_city_visibility
     , coalesce(network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY")                                    as geo_zipcode_visibility
     , coalesce(network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")                                         as geo_dma_visibility
     , if(visitor.standard_device_type_child_id is null,
          cast(array() as array<int>),
          array(visitor.standard_device_type_child_id))                                                                  as standard_device_type_ids
     , coalesce(visitor.standard_environment_id, cast(-1 as int))                                                       as standard_environment_id
     , coalesce(visitor.standard_os_id, cast(-1 as int))                                                                as standard_os_id
     , coalesce(request.context.tv_network_id, cast(-1 as long))                                                        as tv_network_id
     , if(network.standard_brand_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_brand_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_brand_id
     , if(network.standard_programmer_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_programmer_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_programmer_id
     , if(network.standard_genre_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_genre_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                                   as standard_genre_ids
     , if(network.content_form_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.content_form_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as content_form_id
     , if(network.content_rating_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.content_rating_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as content_rating_id
     , if(network.standard_language_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_language_ids, cast(array() as array<int>)),
          cast(array() as array<int>))                                                                                   as standard_language_ids
     , coalesce(request.context.stream_mode_id, cast(-1 as int))                                                        as stream_mode_id
     , coalesce(request.context.inventory_location_id, cast(-1 as int))                                                 as inventory_location_id
     , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                                as ip_enabled_audience_id
     , coalesce(network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_brand_visibility
     , coalesce(network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_genre_visibility
     , coalesce(network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY")                                  as content_rating_visibility
     , cast(array() as array<long>)                                                                                     as listing_ids
     , coalesce(network.inbound_order_id, cast(-1 as long))                                                             as inbound_order_id
     , coalesce(network.inbound_listing_id, cast(array() as array<long>))                                               as inbound_listing_ids
     , coalesce(outbound.order_id, cast(-1 as long))                                                                    as outbound_order_id
     , coalesce(outbound.listing_id, cast(array() as array<long>))                                                      as outbound_listing_ids
     , coalesce(slot_ctx.slot.time_position_class, "Unknown")                                                                    as time_position_class
     , "Unknown"                                                                                                        as placement_type_priority
     , cast(0 as long)                                                                                                  as ad_views
     , cast(0 as long)                                                                                                  as no_ad_views
     , cast(0 as long)                                                                                                  as gross_ad_views
     , cast(0 as long)                                                                                                  as clicks
     , cast(0 as long)                                                                                                  as no_clicks
     , cast(0 as double)                                                                                                as revenue
     , cast(0 as double)                                                                                                as co_revenue
     , cast(0 as double)                                                                                                as d_revenue
     , cast(0 as double)                                                                                                as r_revenue
     , cast(0 as long)                                                                                                  as first_quartile
     , cast(0 as long)                                                                                                  as middle_quartile
     , cast(0 as long)                                                                                                  as third_quartile
     , cast(0 as long)                                                                                                  as complete_quartile
     , cast(0 as long)                                                                                                  as can_quartile
     , cast(0 as long)                                                                                                  as ad_expand
     , cast(0 as long)                                                                                                  as ad_collapse
     , cast(0 as long)                                                                                                  as measurable_ad_expand_collapse_impression
     , cast(0 as long)                                                                                                  as ad_mute
     , cast(0 as long)                                                                                                  as ad_unmute
     , cast(0 as long)                                                                                                  as measurable_ad_mute_unmute_impression
     , cast(0 as long)                                                                                                  as ad_rewind
     , cast(0 as long)                                                                                                  as measurable_ad_rewind_impression
     , cast(0 as long)                                                                                                  as ad_pause
     , cast(0 as long)                                                                                                  as ad_resume
     , cast(0 as long)                                                                                                  as measurable_ad_pause_resume_impression
     , cast(0 as long)                                                                                                  as ad_close
     , cast(0 as long)                                                                                                  as measurable_ad_close_impression
     , cast(0 as long)                                                                                                  as ad_accept_invitation
     , cast(0 as long)                                                                                                  as ad_minimize
     , cast(0 as long)                                                                                                  as measurable_ad_accept_invitation_minimize_impression
     , cast(0 as long)                                                                                                  as ad_insertion
     , cast(0 as long)                                                                                                  as total_avails
     , cast(0 as long)                                                                                                  as total_unfilled_avails
     , cast(0 as long)                                                                                                  as opportunity
     , sum(coalesce(outbound_ack.total_avails_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))               as outbound_avails
     , sum(coalesce(outbound_ack.total_unfilled_avails_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))      as outbound_unfilled_avails
     , sum(coalesce(outbound_ack.opportunity_in_played_slot, cast(0 as int)) * coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)))                as outbound_opportunity
     , coalesce(network.carriage_inventory_owner_id, cast(-1 as long))                                                  as carriage_inventory_owner_id
     , if(network.standard_endpoint_owner_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_owner_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_endpoint_owner_id
     , if(network.standard_endpoint_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_endpoint_id
     , coalesce(outbound.exchange_order_id, cast(-1 as long))                                                           as outbound_exchange_order_id
     , coalesce(network.supply_source, cast(-1 as int))                                                                 as supply_source
     , coalesce(outbound.sales_channel, cast(-1 as int))                                                                as sales_channel
     , coalesce(network.standard_endpoint_owner_visibility.report_aggregate, "FULL_VISIBILITY")                         as standard_endpoint_owner_visibility
     , coalesce(network.standard_endpoint_visibility.report_aggregate, "FULL_VISIBILITY")                               as standard_endpoint_visibility
     , coalesce(network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY")                                      as user_agent_visibility
     , coalesce(network.inbound_order_auction_type, "UNKNOWN")                                                          as inbound_order_auction_type
     , cast(0 as double)                                                                                                as ssp_clearing_revenue
     , cast(0 as long)                                                                                                  as ad_bid_won
     , if(network.standard_channel_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_channel_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_channel_id
     , if(network.standard_content_daypart_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_daypart_id, cast(-1 as int)),
          cast(-1 as int))                                                                                               as standard_content_daypart_id
     , coalesce(request.bid_request.publisher_id, "Unknown")                                                            as ssp_external_publisher_id
     , coalesce(network.tracked_audience_item_ids, cast(array() as array<long>))                                        as tracked_audience_item_ids
     , coalesce(visitor.dma_code_id, cast(-1 as int))                                                                   as user_dma_code_id
     , coalesce(network.asset_id, cast(-1 as long))                                                                     as asset_id
     , coalesce(network.series_id, cast(-1 as long))                                                                    as series_id
     , coalesce(network.asset_group_ids, cast(array() as array<long>))                                                  as asset_group_ids
     , coalesce(network.site_section_id, cast(-1 as long))                                                              as site_section_id
     , coalesce(network.site_id, cast(-1 as long))                                                                      as site_id
     , coalesce(network.site_section_group_ids, cast(array() as array<long>))                                           as site_section_group_ids
     , coalesce(network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY")                             as standard_programmer_visibility
     , if(network.network_is_ad_unit_owner, coalesce(slot_ctx.slot.ad_unit_id, cast(-1 as long)), cast(-1 as long))              as ad_unit_id
     , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                                as standard_publisher_id
     , coalesce(network.bidder_seat_id, cast(-1 as long))                                                               as bidder_seat_id
     , ''                                                                                                               as global_currency_version
     , cast(-1 as long)                                                                                                 as global_currency_id
     , coalesce(request.context.standard_app_id, cast(-1 as long))                                                      as standard_app_id
     , coalesce(request.context.profile_id, cast(-1 as long))                                                         as profile_id
     , coalesce(request.context.profile_type, 'UNKNOWN')                                                                as profile_type
     , if(network.standard_content_series_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_series_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_content_series_id
     , if(network.standard_content_subscription_model_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_subscription_model_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_subscription_model_id
     , coalesce(request.context.standard_ssp_channel_id, cast(-1 as long))                                              as standard_ssp_channel_id
     , coalesce(request.context.standard_site_domain_id, cast(-1 as long))                                              as standard_site_domain_id
     , coalesce(visitor.standard_operator_id, cast(-1 as long))                                                         as standard_operator_id
     , coalesce(request.context.standard_iab_category_ids, cast(array() as array<long>))                                as standard_iab_category_ids
     , if(outbound.sales_channel in (5,6),
          coalesce(outbound.matched_inventory_package_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                                 as matched_inventory_package_ids
     , if(network.standard_content_territory_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_territory_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_territory_id
     , coalesce(visitor.platform_group, "-1")                                                                           as platform_group
     , coalesce(network.standard_content_series_visibility.report_aggregate, 'FULL_VISIBILITY')                         as standard_content_series_visibility
     , if(network.standard_content_credential_status_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_credential_status_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_credential_status_id
     , coalesce(visitor.platform_device_id, cast(-1 as long))                                                           as delivered_platform_device_id
     , coalesce(visitor.platform_browser_id, cast(-1 as long))                                                          as delivered_platform_browser_id
     , coalesce(visitor.platform_os_id, cast(-1 as long))                                                               as delivered_platform_os_id
     , cast(array() as array<long>)                                                                                     as inventory_package_ids
     , cast(0 as double)                                                                                                as ssp_floor_revenue_in_request
     , network.airing_id                                                                                                as airing_id
     , network.airing_channel_id                                                                                        as channel_id
     , coalesce(network.break_id, cast(-1 as long))                                                                     as break_id
     , ""                                                                                                               as delivery_method
     , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                                         as standard_retailer_id
     , coalesce(network.standard_content_subscription_model_visibility.report_aggregate, 'FULL_VISIBILITY')             as standard_content_subscription_model_visibility
     , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                                     as standard_manufacturer_id
     , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                               as standard_app_bundle_id
     , cast(0 as double)                                                                                                as supply_acquisition_cost
     , cast(0 as double)                                                                                                as supply_distribution_cost
     , coalesce(network.standard_channel_visibility.report_aggregate, "FULL_VISIBILITY")                                as standard_channel_visibility
     , coalesce(network.content_form_visibility.report_aggregate, "FULL_VISIBILITY")                                    as content_form_visibility
     , if(network.supply_source != 3,
          coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
          cast(array() as array<bigint>))                                                                               as standard_content_viewership_profile_ids
     , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                                as standard_privacy_id
     , coalesce(request.context.standard_addressability_ids, cast(array() as array<bigint>))                            as standard_addressability_ids
     , cast(0 as long)                                                                                                  as avails
     , cast(0 as long)                                                                                                  as unconstrained_avails
     , cast(0 as long)                                                                                                  as unfilled_avails
     , cast(0 as long)                                                                                                  as constrained_inventory_opportunities_in_played_slot
     , cast(0 as double)                                                                                                as inbound_floor_revenue
     , if(network.supply_source != 3,
          coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                                  as standard_sport_entity_ids
     , coalesce(slot_ctx.slot.avail_type, "")                                                                                    as slot_avail_type
     , "Not Applicable"                                                                                                 as linear_decision_type
     , cast(0 as long)                                                                                                  as break_starts
     , date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp))                                                             as event_date
from fw1_hoover_prd.hoover_batch.transaction
         lateral view explode(slot_ctxes) as slot_ctx
        lateral view explode(slot_ctx.networks) as network
         lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
         lateral view explode(slot_ack_ctx.networks) as slot_ack_network
    lateral view explode(network.eligible_outbound_orders) as outbound
lateral view explode(slot_ack_network.eligible_outbound_orders) as outbound_ack
where slot_ack_ctx.ack.ack_entity_type = "slot"
  and slot_ack_ctx.ack.flags & 256 = 0
  and coalesce(slot_ctx.slot.flags, cast(0 as long)) & 64 = 0 -- not parent slot
-- remove zero rows
  and coalesce(slot_ack_ctx.metrics.slot_impression, cast(0 as long)) != 0
  and (
    coalesce(outbound_ack.total_avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(outbound_ack.total_unfilled_avails_in_played_slot, cast(0 as int)) != 0
   or coalesce(outbound_ack.opportunity_in_played_slot, cast(0 as int)) != 0
    )
  and date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as TIMESTAMP)) = date_trunc('HOUR', to_timestamp("20260722080000", 'yyyyMMddHHmmss'))
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 135, 136, 139, 140, 141, 142, 143,
    149, 150, 151, 153
-- 3182404

UNION ALL

-- break starts
select batch_id                                                                                          as process_batch_id
     , coalesce(network.network_id, cast(-1 as long))                                                                   as network_id
     , coalesce(network.content_owner_network_id, cast(-1 as long))                                                     as content_owner_id
     , coalesce(network.distributor_network_id, cast(-1 as long))                                                   as distributor_id
     , coalesce(null, cast(-1 as long))                                                          as reseller_id -- only an ad network field
     , "CROB"                                                                                                           as transaction_type
     , coalesce(slot_ack_ctx.ack.traffic_type, cast(0 as long))                                                                      as traffic_type
     , coalesce(network.bit_flags, cast(0 as long)) + coalesce(request.bit_flags, cast(0 as long))                      as bit_flag
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                                     as user_country_id
     , coalesce(visitor.state_id, cast(-1 as int))                                                                      as user_state_id
     , coalesce(visitor.city_id, cast(-1 as int))                                                                       as user_city_id
     , coalesce(visitor.operator_zone_id, cast(-1 as long))                                                             as operator_zone_id
     , coalesce(visitor.postal_code, "-1")                                                                              as postal_code
     , coalesce(visitor.dma_code, cast(-1 as int))                                                                      as user_dma_code
     , coalesce(network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY")                                     as geo_country_visibility
     , "FULL_VISIBILITY"                                             as geo_visibility
     , coalesce(network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY")                                       as geo_state_visibility
     , coalesce(network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY")                                        as geo_city_visibility
     , coalesce(network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY")                                    as geo_zipcode_visibility
     , coalesce(network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY")                                         as geo_dma_visibility
     , if(visitor.standard_device_type_child_id is null,
          cast(array() as array<int>),
          array(visitor.standard_device_type_child_id))                                                                 as standard_device_type_ids
     , coalesce(visitor.standard_environment_id, cast(-1 as int))                                                       as standard_environment_id
     , coalesce(visitor.standard_os_id, cast(-1 as int))                                                                as standard_os_id
     , coalesce(request.context.tv_network_id, cast(-1 as long))                                                        as tv_network_id
     , coalesce(request.context.standard_brand_id, cast(-1 as int))                                                     as standard_brand_id
     , coalesce(request.context.standard_programmer_id, cast(-1 as int))                                                as standard_programmer_id
     , coalesce(request.context.standard_genre_ids, cast(array() as array<int>))                                        as standard_genre_ids
     , coalesce(request.context.content_form_id, cast(-1 as int))                                                       as content_form_id
     , coalesce(request.context.content_rating_id, cast(-1 as int))                                                     as content_rating_id
     , coalesce(request.context.standard_language_ids, cast(array() as array<int>))                                     as standard_language_ids
     , coalesce(request.context.stream_mode_id, cast(-1 as int))                                                        as stream_mode_id
     , coalesce(request.context.inventory_location_id, cast(-1 as int))                                                 as inventory_location_id
     , coalesce(request.context.ip_enabled_audience_id, cast(-1 as int))                                                as ip_enabled_audience_id
     , coalesce(network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_brand_visibility
     , coalesce(network.standard_genre_visibility.report_aggregate, "FULL_VISIBILITY")                                  as standard_genre_visibility
     , coalesce(network.content_rating_visibility.report_aggregate, "FULL_VISIBILITY")                                  as content_rating_visibility
     , cast(array() as array<long>)                                                                                     as listing_ids
     , cast(-1 as long)                                                                                                 as inbound_order_id
     , cast(array() as array<long>)                                                                                     as inbound_listing_ids
     , cast(-1 as long)                                                                                                 as outbound_order_id
     , cast(array() as array<long>)                                                                                     as outbound_listing_ids
     , "Unknown"                                                                                                        as time_position_class
     , "Unknown"                                                                                                        as placement_type_priority
     , cast(0 as long)                                                                                                  as ad_views
     , cast(0 as long)                                                                                                  as no_ad_views
     , cast(0 as long)                                                                                                  as gross_ad_views
     , cast(0 as long)                                                                                                  as clicks
     , cast(0 as long)                                                                                                  as no_clicks
     , cast(0 as double)                                                                                                as revenue
     , cast(0 as double)                                                                                                as co_revenue
     , cast(0 as double)                                                                                                as d_revenue
     , cast(0 as double)                                                                                                as r_revenue
     , cast(0 as long)                                                                                                  as first_quartile
     , cast(0 as long)                                                                                                  as middle_quartile
     , cast(0 as long)                                                                                                  as third_quartile
     , cast(0 as long)                                                                                                  as complete_quartile
     , cast(0 as long)                                                                                                  as can_quartile
     , cast(0 as long)                                                                                                  as ad_expand
     , cast(0 as long)                                                                                                  as ad_collapse
     , cast(0 as long)                                                                                                  as measurable_ad_expand_collapse_impression
     , cast(0 as long)                                                                                                  as ad_mute
     , cast(0 as long)                                                                                                  as ad_unmute
     , cast(0 as long)                                                                                                  as measurable_ad_mute_unmute_impression
     , cast(0 as long)                                                                                                  as ad_rewind
     , cast(0 as long)                                                                                                  as measurable_ad_rewind_impression
     , cast(0 as long)                                                                                                  as ad_pause
     , cast(0 as long)                                                                                                  as ad_resume
     , cast(0 as long)                                                                                                  as measurable_ad_pause_resume_impression
     , cast(0 as long)                                                                                                  as ad_close
     , cast(0 as long)                                                                                                  as measurable_ad_close_impression
     , cast(0 as long)                                                                                                  as ad_accept_invitation
     , cast(0 as long)                                                                                                  as ad_minimize
     , cast(0 as long)                                                                                                  as measurable_ad_accept_invitation_minimize_impression
     , cast(0 as long)                                                                                                  as ad_insertion
     , cast(0 as long)                                                                                                  as total_avails
     , cast(0 as long)                                                                                                  as total_unfilled_avails
     , cast(0 as long)                                                                                                  as opportunity
     , cast(0 as long)                                                                                                  as outbound_avails
     , cast(0 as long)                                                                                                  as outbound_unfilled_avails
     , cast(0 as long)                                                                                                  as outbound_opportunity
     , coalesce(network.carriage_inventory_owner_id, cast(-1 as long))                                                  as carriage_inventory_owner_id
     , if(network.standard_endpoint_owner_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_owner_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_endpoint_owner_id
     , if(network.standard_endpoint_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_endpoint_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_endpoint_id
     , cast(-1 as long)                                                                                                 as outbound_exchange_order_id
     , cast(0 as int)                                                                                                   as supply_source
     , cast(0 as int)                                                                                                   as sales_channel
     , coalesce(network.standard_endpoint_owner_visibility.report_aggregate, "FULL_VISIBILITY")                         as standard_endpoint_owner_visibility
     , coalesce(network.standard_endpoint_visibility.report_aggregate, "FULL_VISIBILITY")                               as standard_endpoint_visibility
     , coalesce(network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY")                                      as user_agent_visibility
     , "UNKNOWN"                                                                                                        as inbound_order_auction_type
     , cast(0 as double)                                                                                                as ssp_clearing_revenue
     , cast(0 as long)                                                                                                  as ad_bid_won
     , if(network.standard_channel_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_channel_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_channel_id
     , if(network.standard_content_daypart_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_daypart_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_content_daypart_id
     , "Unknown"                                                                                                        as ssp_external_publisher_id
     , cast(array() as array<long>)                                                                                     as tracked_audience_item_ids
     , coalesce(visitor.dma_code_id, cast(-1 as int))                                                                   as user_dma_code_id
     , coalesce(network.asset_id, cast(-1 as long))                                                                     as asset_id
     , coalesce(network.series_id, cast(-1 as long))                                                                    as series_id
     , coalesce(network.asset_group_ids, cast(array() as array<long>))                                                  as asset_group_ids
     , coalesce(network.site_section_id, cast(-1 as long))                                                              as site_section_id
     , coalesce(network.site_id, cast(-1 as long))                                                                      as site_id
     , coalesce(network.site_section_group_ids, cast(array() as array<long>))                                           as site_section_group_ids
     , coalesce(network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY")                             as standard_programmer_visibility
     , cast(-1 as long)                                                                                                 as ad_unit_id
     , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                                as standard_publisher_id
     , cast(-1 as long)                                                                                                 as bidder_seat_id
     , ''                                                                                                               as global_currency_version
     , cast(-1 as long)                                                                                                 as global_currency_id
     , coalesce(request.context.standard_app_id, cast(-1 as long))                                                      as standard_app_id
     , coalesce(request.context.profile_id, cast(-1 as long))                                                         as profile_id
     , coalesce(request.context.profile_type, 'UNKNOWN')                                                                as profile_type
     , if(network.standard_content_series_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_series_id, cast(-1 as int)),
          cast(-1 as int))                                                                                              as standard_content_series_id
     , if(network.standard_content_subscription_model_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_subscription_model_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_subscription_model_id
     , coalesce(request.context.standard_ssp_channel_id, cast(-1 as long))                                              as standard_ssp_channel_id
     , coalesce(request.context.standard_site_domain_id, cast(-1 as long))                                              as standard_site_domain_id
     , coalesce(visitor.standard_operator_id, cast(-1 as long))                                                         as standard_operator_id
     , coalesce(request.context.standard_iab_category_ids, cast(array() as array<long>))                                as standard_iab_category_ids
--      , case
--            when network.network_is_extra_item_owner then coalesce(ad_ctx.ad.matched_inventory_package_ids, cast(array() as array<long>)) -- network is extra item owner is an ad network only dimension
--            when network.sales_channel in (5,6) then coalesce(network.matched_inventory_package_ids, cast(array() as array<long>)) -- same for sales channel
--            else cast(array() as array<long>)
--     end
    , cast(array() as array<long>) as matched_inventory_package_ids
     , if(network.standard_content_territory_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_territory_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_territory_id
     , coalesce(visitor.platform_group, "-1")                                                                           as platform_group
     , coalesce(network.standard_content_series_visibility.report_aggregate, 'FULL_VISIBILITY')                         as standard_content_series_visibility
     , if(network.standard_content_credential_status_visibility.report_aggregate is not null or network.supply_source != 3,
          coalesce(request.context.standard_content_credential_status_id, cast(-1 as bigint)),
          cast(-1 as bigint))                                                                                           as standard_content_credential_status_id
     , coalesce(visitor.platform_device_id, cast(-1 as long))                                                           as delivered_platform_device_id
     , coalesce(visitor.platform_browser_id, cast(-1 as long))                                                          as delivered_platform_browser_id
     , coalesce(visitor.platform_os_id, cast(-1 as long))                                                               as delivered_platform_os_id
     , cast(array() as array<long>)                                                                                     as inventory_package_ids
     , cast(0 as double)                                                                                                as ssp_floor_revenue_in_request
     , network.airing_id                                                                                                as airing_id
     , network.airing_channel_id                                                                                        as channel_id
     , coalesce(network.break_id, cast(-1 as long))                                                                     as break_id
     , ""                                                                                                               as delivery_method
     , coalesce(visitor.standard_retailer_id, cast(-1 as long))                                                         as standard_retailer_id
     , coalesce(network.standard_content_subscription_model_visibility.report_aggregate, 'FULL_VISIBILITY')             as standard_content_subscription_model_visibility
     , coalesce(visitor.standard_manufacturer_id, cast(-1 as long))                                                     as standard_manufacturer_id
     , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                               as standard_app_bundle_id
     , cast(0 as double)                                                                                                as supply_acquisition_cost
     , cast(0 as double)                                                                                                as supply_distribution_cost
     , coalesce(network.standard_channel_visibility.report_aggregate, "FULL_VISIBILITY")                                as standard_channel_visibility
     , coalesce(network.content_form_visibility.report_aggregate, "FULL_VISIBILITY")                                    as content_form_visibility
     , if(network.supply_source != 3,
          coalesce(request.context.standard_content_viewership_profile_ids, cast(array() as array<bigint>)),
          cast(array() as array<bigint>))                                                                               as standard_content_viewership_profile_ids
     , coalesce(request.context.standard_privacy_id, cast(-1 as bigint))                                                as standard_privacy_id
     , coalesce(request.context.standard_addressability_ids, cast(array() as array<bigint>))                            as standard_addressability_ids
     , cast(0 as long)                                                                                                  as avails
     , cast(0 as long)                                                                                                  as unconstrained_avails
     , cast(0 as long)                                                                                                  as unfilled_avails
     , cast(0 as long)                                                                                                  as constrained_inventory_opportunities_in_played_slot
     , cast(0 as double)                                                                                                as inbound_floor_revenue
     , if(network.supply_source != 3,
          coalesce(request.context.standard_sport_entity_ids, cast(array() as array<long>)),
          cast(array() as array<long>))                                                                                  as standard_sport_entity_ids
     , coalesce(slot_ctx.slot.avail_type, "")                                                                                    as slot_avail_type
     , "Not Applicable"                                                                                                 as linear_decision_type
     , sum(coalesce(slot_ack_ctx.metrics.break_starts, cast(0 as long)))                                                         as break_starts
     , date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as timestamp))                                                             as event_date
from fw1_hoover_prd.hoover_batch.transaction
         lateral view explode(slot_ctxes) as slot_ctx
         lateral view explode(slot_ctx.networks) as network
         lateral view explode(slot_ctx.ack_ctxes) as slot_ack_ctx
where slot_ack_ctx.ack.ack_entity_type = "slot"
  and slot_ack_ctx.ack.flags & 256 = 0
  and coalesce(network.role, "") = "CRO"
  and coalesce(slot_ctx.slot.environment, "") = "VIDEO"
  and coalesce(slot_ctx.slot.time_position_class, "Unknown") != "overlay"
  and coalesce(slot_ctx.slot.flags, cast(0 as long)) & 32 == 0 -- not sub-slot
  and coalesce(request.bit_flags, cast(0 as long)) & 32768 != 0 -- is HyLDA request
  and coalesce(slot_ack_ctx.metrics.break_starts, cast(0 as long)) != 0  -- remove zero rows
  and  date_trunc('HOUR', cast(slot_ack_ctx.ack.timestamp as TIMESTAMP)) = date_trunc('HOUR', to_timestamp("20260722080000", 'yyyyMMddHHmmss'))
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
35, 36, 37, 38, 39, 40, 41, 42, 43, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 129, 130, 131, 132, 133,
134, 135, 136, 139, 140, 141, 142, 143, 149, 150, 151, 153
```

Inferences:

- Adding `*.ack.flags & 256 = 0` matches revenue metrics but with a slight difference of 0.10

**SUMMARY:**

- **Failed checks:** Dimension values, Metric sums, Row-level hash
- Dimensions analyzed: 102 — differences found
- Metrics analyzed: 48 — differences found
- Row count: Control 6,854,871 / Stage 6,946,438 — mismatch
- Row hash diffs: 13,433,041 — mismatch

| **Dimension** | **Control Total** | **Stage Total** | **Only in Control** | **Only in Stage** | **Comments** |
| --- | --- | --- | --- | --- | --- |
| **content\_owner\_id** | 277 | 276 | 1 | 0 |  |
| **distributor\_id** | 264 | 263 | 1 | 0 |  |
| **traffic\_type** | 3 | 2 | 1 | 0 |  |
| **user\_state\_id** | 1702 | 1695 | 7 | 0 |  |
| **user\_city\_id** | 26213 | 25840 | 373 | 0 |  |
| **operator\_zone\_id** | 884 | 687 | 197 | 0 |  |
| **postal\_code** | 39773 | 39284 | 489 | 0 |  |
| **user\_dma\_code** | 1010 | 1005 | 5 | 0 |  |
| **tv\_network\_id** | 175 | 149 | 26 | 0 |  |
| **standard\_brand\_id** | 959 | 950 | 9 | 0 |  |
| **standard\_programmer\_id** | 417 | 413 | 4 | 0 |  |
| **standard\_genre\_ids** | 6778 | 6629 | 149 | 0 |  |
| **standard\_language\_ids** | 40 | 39 | 1 | 0 |  |
| **inbound\_order\_id** | 2924 | 2985 | 1 | 62 |  |
| **inbound\_listing\_ids** | 3449 | 3520 | 1 | 72 |  |
| **outbound\_order\_id** | 2873 | 2928 | 0 | 55 |  |
| **outbound\_listing\_ids** | 3423 | 3487 | 0 | 64 |  |
| **carriage\_inventory\_owner\_id** | 105 | 104 | 1 | 0 |  |
| **standard\_endpoint\_owner\_id** | 151 | 150 | 1 | 0 |  |
| **standard\_endpoint\_id** | 256 | 254 | 2 | 0 |  |
| **standard\_channel\_id** | 832 | 831 | 1 | 0 |  |
| **ssp\_external\_publisher\_id** | 1358 | 1297 | 61 | 0 |  |
| **tracked\_audience\_item\_ids** | 4859 | 4832 | 31 | 4 |  |
| **asset\_id** | 7759 | 7600 | 160 | 1 |  |
| **series\_id** | 3574 | 3499 | 76 | 1 |  |
| **asset\_group\_ids** | 7419 | 6695 | 725 | 1 |  |
| **site\_section\_id** | 9519 | 9490 | 100 | 71 |  |
| **site\_id** | 2678 | 2644 | 36 | 2 |  |
| **site\_section\_group\_ids** | 6685 | 6671 | 65 | 51 |  |
| **ad\_unit\_id** | 755 | 723 | 32 | 0 |  |
| **standard\_app\_id** | 1583 | 1259 | 324 | 0 |  |
| **profile\_id** | 1201 | 1188 | 13 | 0 |  |
| **standard\_content\_series\_id** | 1215 | 1177 | 38 | 0 |  |
| **standard\_site\_domain\_id** | 1526 | 1468 | 58 | 0 |  |
| **standard\_iab\_category\_ids** | 1810 | 1783 | 27 | 0 |  |
| **matched\_inventory\_package\_ids** | 1568 | 1579 | 0 | 11 |  |
| **standard\_content\_territory\_id** | 37 | 34 | 3 | 0 |  |
| **airing\_id** | 81 | 80 | 1 | 0 |  |
| **channel\_id** | 5963 | 1588 | 4375 | 0 |  |
| **break\_id** | 123 | 122 | 1 | 0 |  |
| **standard\_app\_bundle\_id** | 2726 | 2275 | 451 | 0 |  |
| **standard\_content\_viewership\_profile\_ids** | 118 | 115 | 3 | 0 |  |
| **standard\_addressability\_ids** | 209 | 208 | 1 | 0 |  |
| **standard\_sport\_entity\_ids** | 15 | 14 | 1 | 0 |  |
| **network\_id** | 570 | 570 | 1 | 1 |  |

| **Metric** | **Control Sum** | **Stage Sum** | **Difference** | **% Diff** | **Comments** |
| --- | --- | --- | --- | --- | --- |
| **gross\_ad\_views** | 138,884.00 | 124,885.00 | -13,999.00 | -10.08% |  |
| **revenue** | 1,412.98 | 1,412.88 | -0.10 | -0.01% |  |
| **r\_revenue** | 1,606.12 | 1,606.01 | -0.10 | -0.01% |  |
| **ad\_close** | 53.00 | 54.00 | +1.00 | +1.89% |  |
| **total\_avails** | 16,126,073.00 | 18,548,537,953.00 | +18,532,411,880.00 | +114922.04% |  |
| **total\_unfilled\_avails** | 4,275,266.00 | 2,035,960,017.00 | +2,031,684,751.00 | +47521.83% |  |
| **opportunity** | 28,104,891.00 | 30,274,034,767.00 | +30,245,929,876.00 | +107618.03% |  |
| **outbound\_avails** | 11,807,898.00 | 15,707,886,993.00 | +15,696,079,095.00 | +132928.65% |  |
| **outbound\_unfilled\_avails** | 3,268.00 | 123,112.00 | +119,844.00 | +3667.20% |  |
| **outbound\_opportunity** | 23,784,311.00 | 26,524,028,280.00 | +26,500,243,969.00 | +111419.01% |  |
| **ssp\_floor\_revenue\_in\_request** | 97.61 | 12,489.88 | +12,392.27 | +12695.15% |  |
| **avails** | 16,545,098.00 | 333,657,089.00 | +317,111,991.00 | +1916.65% |  |
| **unconstrained\_avails** | 16,546,915.00 | 333,657,089.00 | +317,110,174.00 | +1916.43% |  |
| **unfilled\_avails** | 4,504,556.00 | 27,328,547.00 | +22,823,991.00 | +506.69% |  |
| **constrained\_inventory\_opportunities\_in\_played\_slot** | 27,787,895.00 | 485,039,063.00 | +457,251,168.00 | +1645.50% |  |
| **inbound\_floor\_revenue** | 146,607.10 | 2,143,779.42 | +1,997,172.32 | +1362.26% |  |

---

**Additional filters to match the Control and Stage Tables:**

1. Added `ad_ack_ctx.ack.flags & 256 = 0` to align the columns like first\_quartile and other metrics.
2. Adding `ad_ack_ctx.ack.flags & 256 = 0`is aligning few columns like first\_quartile, but it shows minor of 0.10 for revenue metrics.


## Diffs (27-Jul-2026)

**SUMMARY**

- **Failed checks:** Dimension values, Metric sums, Row-level hash
- Dimensions analyzed: 104 — differences found
- Metrics analyzed: 48 — differences found
- Row count: Control 8,854,168 / Stage 4,980,462 — mismatch
- Row hash diffs: 13,739,512 — mismatch


1. **DIMENSION VALUE DIFFERENCES (Actual Values)**

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **process\_batch\_id** | 2 | 1 | 1 | 0 |
| **network\_id** | 542 | 530 | 15 | 3 |
| **content\_owner\_id** | 279 | 268 | 11 | 0 |
| **distributor\_id** | 267 | 257 | 10 | 0 |
| **reseller\_id** | 337 | 338 | 1 | 2 |
| **bit\_flag** | 718 | 640 | 93 | 15 |
| **user\_country\_id** | 175 | 174 | 1 | 0 |
| **user\_state\_id** | 1775 | 1752 | 23 | 0 |
| **user\_city\_id** | 26450 | 25249 | 1217 | 16 |
| **postal\_code** | 37542 | 36085 | 1485 | 28 |
| **user\_dma\_code** | 980 | 968 | 15 | 3 |
| **standard\_device\_type\_ids** | 58 | 59 | 0 | 1 |
| **tv\_network\_id** | 162 | 163 | 1 | 2 |
| **standard\_brand\_id** | 951 | 920 | 31 | 0 |
| **standard\_programmer\_id** | 411 | 402 | 9 | 0 |
| **standard\_genre\_ids** | 6277 | 6038 | 242 | 3 |
| **inbound\_order\_id** | 2819 | 2559 | 333 | 73 |
| **inbound\_listing\_ids** | 3381 | 2996 | 474 | 89 |
| **outbound\_order\_id** | 2801 | 2849 | 8 | 56 |
| **outbound\_listing\_ids** | 3362 | 3426 | 8 | 72 |
| **carriage\_inventory\_owner\_id** | 107 | 104 | 3 | 0 |
| **standard\_endpoint\_owner\_id** | 142 | 141 | 1 | 0 |
| **standard\_endpoint\_id** | 254 | 242 | 13 | 1 |
| **standard\_channel\_id** | 818 | 789 | 35 | 6 |
| **ssp\_external\_publisher\_id** | 1255 | 1204 | 51 | 0 |
| **tracked\_audience\_item\_ids** | 5461 | 5165 | 360 | 64 |
| **asset\_id** | 7679 | 6974 | 760 | 55 |
| **series\_id** | 3471 | 3199 | 300 | 28 |
| **asset\_group\_ids** | 7340 | 6779 | 602 | 41 |
| **site\_section\_id** | 9396 | 9016 | 520 | 140 |
| **site\_id** | 2667 | 2555 | 119 | 7 |
| **site\_section\_group\_ids** | 6760 | 6526 | 334 | 100 |
| **ad\_unit\_id** | 765 | 657 | 119 | 11 |
| **global\_currency\_version** | 12 | 2 | 10 | 0 |
| **standard\_app\_id** | 1972 | 1499 | 473 | 0 |
| **profile\_id** | 1186 | 1122 | 65 | 1 |
| **standard\_content\_series\_id** | 1184 | 1115 | 72 | 3 |
| **standard\_site\_domain\_id** | 1509 | 1419 | 90 | 0 |
| **standard\_iab\_category\_ids** | 1519 | 1459 | 60 | 0 |
| **matched\_inventory\_package\_ids** | 1373 | 1294 | 92 | 13 |
| **standard\_content\_territory\_id** | 38 | 35 | 3 | 0 |
| **airing\_id** | 93 | 71 | 22 | 0 |
| **channel\_id** | 5888 | 5875 | 34 | 21 |
| **break\_id** | 132 | 97 | 35 | 0 |
| **standard\_app\_bundle\_id** | 3308 | 2611 | 697 | 0 |
| **standard\_content\_viewership\_profile\_ids** | 119 | 117 | 3 | 1 |
| **standard\_addressability\_ids** | 208 | 204 | 4 | 0 |

1. **METRIC SUM DIFFERENCES**

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **ad\_views** | 127,151.00 | 224,321.00 | +97,170.00 | +76.42% |
| **no\_ad\_views** | 7.00 | 54.00 | +47.00 | +671.43% |
| **gross\_ad\_views** | 141,024.00 | 224,321.00 | +83,297.00 | +59.07% |
| **clicks** | 39.00 | 49.00 | +10.00 | +25.64% |
| **no\_clicks** | 77,988.00 | 138,829.00 | +60,841.00 | +78.01% |
| **revenue** | 1,515.58 | 2,339.80 | +824.22 | +54.38% |
| **co\_revenue** | 481.33 | 916.67 | +435.34 | +90.45% |
| **d\_revenue** | 2.04 | 5.33 | +3.29 | +161.02% |
| **r\_revenue** | 1,679.93 | 2,752.81 | +1,072.88 | +63.86% |
| **first\_quartile** | 123,636.00 | 218,590.00 | +94,954.00 | +76.80% |
| **middle\_quartile** | 122,973.00 | 217,045.00 | +94,072.00 | +76.50% |
| **third\_quartile** | 122,370.00 | 215,637.00 | +93,267.00 | +76.22% |
| **complete\_quartile** | 122,250.00 | 215,071.00 | +92,821.00 | +75.93% |
| **can\_quartile** | 124,660.00 | 220,914.00 | +96,254.00 | +77.21% |
| **ad\_expand** | 202.00 | 217.00 | +15.00 | +7.43% |
| **ad\_collapse** | 6.00 | 14.00 | +8.00 | +133.33% |
| **measurable\_ad\_expand\_collapse\_impression** | 31,389.00 | 57,400.00 | +26,011.00 | +82.87% |
| **ad\_mute** | 944.00 | 2,327.00 | +1,383.00 | +146.50% |
| **ad\_unmute** | 42.00 | 90.00 | +48.00 | +114.29% |
| **measurable\_ad\_mute\_unmute\_impression** | 44,840.00 | 81,669.00 | +36,829.00 | +82.13% |
| **ad\_rewind** | 3.00 | 9.00 | +6.00 | +200.00% |
| **measurable\_ad\_rewind\_impression** | 30,208.00 | 56,132.00 | +25,924.00 | +85.82% |
| **ad\_pause** | 1,006.00 | 1,722.00 | +716.00 | +71.17% |
| **ad\_resume** | 1,159.00 | 2,153.00 | +994.00 | +85.76% |
| **measurable\_ad\_pause\_resume\_impression** | 48,795.00 | 89,236.00 | +40,441.00 | +82.88% |
| **ad\_close** | 42.00 | 68.00 | +26.00 | +61.90% |
| **measurable\_ad\_close\_impression** | 14,822.00 | 19,790.00 | +4,968.00 | +33.52% |
| **measurable\_ad\_accept\_invitation\_minimize\_impression** | 21,289.00 | 28,397.00 | +7,108.00 | +33.39% |
| **ad\_insertion** | 349.00 | 384.00 | +35.00 | +10.03% |
| **total\_avails** | 15,328,716.00 | 853,830,237.00 | +838,501,521.00 | +5470.14% |
| **total\_unfilled\_avails** | 3,786,767.00 | 9,043,564.00 | +5,256,797.00 | +138.82% |
| **opportunity** | 31,529,047.00 | 899,522,084.00 | +867,993,037.00 | +2752.99% |
| **outbound\_avails** | 11,497,869.00 | 5,891,548,614.00 | +5,880,050,745.00 | +51140.35% |
| **outbound\_unfilled\_avails** | 3,052.00 | 124,561.00 | +121,509.00 | +3981.29% |
| **outbound\_opportunity** | 27,695,789.00 | 21,600,162,041.00 | +21,572,466,252.00 | +77890.78% |
| **ssp\_clearing\_revenue** | 0.55 | 0.69 | +0.14 | +25.70% |
| **ad\_bid\_won** | 26.00 | 32.00 | +6.00 | +23.08% |
| **ssp\_floor\_revenue\_in\_request** | 106.07 | 0.92 | -105.14 | -99.13% |
| **supply\_acquisition\_cost** | 3.07 | 4.79 | +1.72 | +55.90% |
| **supply\_distribution\_cost** | 8.76 | 13.73 | +4.97 | +56.73% |
| **avails** | 15,789,563.00 | 726,253,307.00 | +710,463,744.00 | +4499.58% |
| **unconstrained\_avails** | 15,791,367.00 | 726,253,307.00 | +710,461,940.00 | +4499.05% |
| **unfilled\_avails** | 4,048,156.00 | 4,485,385.00 | +437,229.00 | +10.80% |
| **constrained\_inventory\_opportunities\_in\_played\_slot** | 32,310,414.00 | 583,766,488.00 | +551,456,074.00 | +1706.74% |
| **inbound\_floor\_revenue** | 220,911.32 | 3,016,120.65 | +2,795,209.33 | +1265.31% |
| **break\_starts** | 1,249.00 | 144.00 | -1,105.00 | -88.47% |

**network\_id:**

Control Total: 542  
Stage Total: 532

Hoover Query: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710095825\_353666&externalid=20260710\_095853\_00000\_5ukap](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710095825_353666&externalid=20260710_095853_00000_5ukap)

count - 1776 rows

Hoover++ Query: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710144419\_608888&externalid=20260710\_145857\_00063\_arm92](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710144419_608888&externalid=20260710_145857_00063_arm92)

count - 1277 rows

| **Sub Query** | **Hoover Presto Link** | **Hoover (Control)** | **Hoover++ Presto Link** | **Hoover++** |
| --- | --- | --- | --- | --- |
| 1 | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710101233\_511257&externalid=20260710\_101243\_00012\_qs5aw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710101233_511257&externalid=20260710_101243_00012_qs5aw) | 634 rows | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710152746\_503976&externalid=20260710\_153223\_00005\_ptajh](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710152746_503976&externalid=20260710_153223_00005_ptajh) | 371 rows |
| 2 | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710101652\_619884&externalid=20260710\_101707\_00000\_m8cz5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710101652_619884&externalid=20260710_101707_00000_m8cz5) | 2 rows | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710151202\_702686&externalid=20260710\_151352\_00017\_zyjge](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710151202_702686&externalid=20260710_151352_00017_zyjge) | 2 rows |
| 3 | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710102002\_290628&externalid=20260710\_102014\_00002\_bs648](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710102002_290628&externalid=20260710_102014_00002_bs648) | 563 rows | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710151227\_997652&externalid=20260710\_151528\_00029\_dvpw5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710151227_997652&externalid=20260710_151528_00029_dvpw5) | 447 rows |
| 4 | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710143040\_505753&externalid=20260710\_143120\_00033\_6r48n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710143040_505753&externalid=20260710_143120_00033_6r48n) | 563 rows | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710151300\_954228&externalid=20260710\_151445\_00007\_v42uk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710151300_954228&externalid=20260710_151445_00007_v42uk) | 447 rows |
| 5 | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710145948\_053638&externalid=20260710\_150000\_00005\_syy5j](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710145948_053638&externalid=20260710_150000_00005_syy5j) | 14 rows | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710151914\_627835&externalid=20260710\_152237\_00041\_nxf5d](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710151914_627835&externalid=20260710_152237_00041_nxf5d) | 10 rows |

**network\_id**: `529893`

**request\_\_transaction\_id**: `1782807674138432405`, `1782807541790279954`


hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713171738\_618040&externalid=20260713\_171742\_00261\_pwixy](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713171738_618040&externalid=20260713_171742_00261_pwixy)

hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713173001\_353130&externalid=20260713\_173544\_00147\_gmh8c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713173001_353130&externalid=20260713_173544_00147_gmh8c)


`531840` - `1782807976810874547`

hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713174112\_497446&externalid=20260713\_174116\_00279\_pwixy](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713174112_497446&externalid=20260713_174116_00279_pwixy)

hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713174255\_125501&externalid=20260713\_175322\_00001\_6xehh](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713174255_125501&externalid=20260713_175322_00001_6xehh)

### Dimension Validation:

*Only in CONTROL (15 total):* 529893, 539746, 536326, 525813, 538936, 519663, 394701, 191700, 542451, 537406 ... (+ 5 more, see CSV)  

**Present in stage and not in control: **

network\_id: *Only in STAGE (3 total):* 510938, 536723, 531840

content\_owner\_id: *Only in CONTROL (11 total):* 536326, 525813, 519663, 191700, 542451, 391249, 545332, 531692, 543709, 535131 ... (+ 1 more, see CSV)

| **Dimension** | **Issue** | **Hoover (Control)** | **Hoover++ (Stage)** | **Hoover++ Transaction** | **Reason** |
| --- | --- | --- | --- | --- | --- |
| network\_id | Present in stage and not in control | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714082508\_455990&externalid=20260714\_082519\_00029\_p7kyc](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714082508_455990&externalid=20260714_082519_00029_p7kyc) | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714065730\_393160&externalid=20260714\_070246\_00002\_a5y2p](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714065730_393160&externalid=20260714_070246_00002_a5y2p) |  | Checked the networks (`510938`, `536723, 531840`) and we don’t see any entries for this networks in hoover for this timeframe **20260630080000.** |
| network\_id | Present in control and not in stage | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714085317\_126787&externalid=20260714\_085401\_00000\_5pqq3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714085317_126787&externalid=20260714_085401_00000_5pqq3) |  |  |  |
| content\_owner\_id | Present in control and not in stage | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714084826\_285687&externalid=20260714\_084831\_00078\_v7pgw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714084826_285687&externalid=20260714_084831_00078_v7pgw) |  |  |  |
| distributor\_id | Present in control and not in stage | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715063119\_642629&externalid=20260715\_063144\_00005\_s8pzq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715063119_642629&externalid=20260715_063144_00005_s8pzq) |  |  |  |
| **reseller\_id** | Present in stage and not in control |  |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715093903\_283246&externalid=20260715\_094101\_00115\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715093903_283246&externalid=20260715_094101_00115_a6c4k) |  |
| **reseller\_id** |  |  |  |  |  |
| bit\_flag |  |  |  |  |  |
| **user\_state\_id** | Present in control and not in stage |  |  |  |  |
| **user\_city\_id** | Present in control and not in stage |  |  |  |  |
| **user\_city\_id** | Present in stage and not in control |  |  |  |  |
| **postal\_code** | Present in control and not in stage |  |  |  |  |
| **postal\_code** | Present in stage and not in control |  |  |  |  |
| **site\_section\_id** | Present in stage and not in control | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260716061704\_981658&externalid=20260716\_061715\_00081\_vxphg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260716061704_981658&externalid=20260716_061715_00081_vxphg) | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715111721\_363395](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715111721_363395) | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715111103\_259207&externalid=20260715\_111238\_00014\_4r26f](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715111103_259207&externalid=20260715_111238_00014_4r26f) | checked site\_section\_ids (23406989,     17841788,     23416870,     23991505,     23392678,     23601527) and we don’t see any entries for this networks in hoover for this timeframe **20260630080000.** |

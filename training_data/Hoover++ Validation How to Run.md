# Hoover\+\+ Validation How to Run

## Introduction

There are few steps needed to run the validation tool between the STAGE and CONTROL environments. 

#### Concrete example → [Hoover++ Validation (Concrete Example)](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191814982/Hoover+Validation+Concrete+Example)

## Steps

### Data Preparation

We want to compare apples to apples between our "stage" and "control" tables. So we need to prepare the data for it.

P.S. `start_date`  and `run_hour`  are automatically calculated in the validation script. So, we will need to setup a continuous job to load data into the "tables"

Additionally, the event\_date is rounded to the hour so we need to make sure we're using the `event_date`  in the where clause correctly.

Example for a "control" table:

```
select * from hive_data_prd_dwh_etl.aggregate.f_order_selected_hourly where event_date = date_trunc('HOUR', CURRENT_TIMESTAMP()) - INTERVAL 3 hours;
```



Example for a "stage" table:

There are a few more things needed to get data from the H++ model.

We first, need to convert the SQL from the current hoover model to the new hoover model (most of these are already completed)

```sql
select stream_batch_id                                                                                    as process_batch_id
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
     , coalesce(partner.postal_code_package_ids, cast(array() as array<int>))                             as postal_code_package_ids
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
     , coalesce(partner.outbound_listing_ids, cast(array() as array<long>))                               as outbound_listing_ids
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
     , cal_decision_type(coalesce(partner.bit_flags, cast(0 as long))
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
    + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int),
         cast(0 as int))                                                                                  as bit_flag_aim_product_category
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
from fw1_stg.hoover_pipeline_streaming.hoover_stream
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
  and cast (request.timestamp as timestamp) >= from_unixtime(request.timestamp) - interval 1 hour
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 196, 197, 198, 199, 200, 201, 202, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 223
```


Once we have the SQL, we can update it to use the compacted data in a similar fashion as above. 

We can either create a "view" or a "table" for this new Hoover++ table and insert data in it as needed.

```
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
     , coalesce(partner.postal_code_package_ids, cast(array() as array<int>))                             as postal_code_package_ids
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
     , coalesce(partner.outbound_listing_ids, cast(array() as array<long>))                               as outbound_listing_ids
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
     , cal_decision_type(coalesce(partner.bit_flags, cast(0 as long))
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
    + if((coalesce(partner.bit_flags, 0) & shiftleft(cast(1 as long), 57)) > 0, cast(16 as int),
         cast(0 as int))                                                                                  as bit_flag_aim_product_category
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
from fw1_prd.hoover_pipeline_compaction.hoover_compaction
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
and to_timestamp(event_hour, 'yyyyMMddHHmmss') = TIMESTAMP('2026-02-23 15:00:00') - interval 3 hour
--   and cast(ack.timestamp as TIMESTAMP) >= to_timestamp(event_hour, 'yyyyMMddHHmmss') - interval 3 hour
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 196, 197, 198, 199, 200, 201, 202, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 223;
```


Now that we have the data prepared, we can move on to the next step.

### Config Preparation

The validation job reads from the config table \`fw1\_stg.kbhargava.validation\_config\_new\`

This can be specified in the task config (see-below) or can be omitted. 

There are a few things that need to be added to this table:

- the control table name (from above)
- the stage table name (from above)
- validation\_table\_name (which L3 or UBT table we're validating)
- The dimensions (of the table we're validating) → COMMA SEPARATED LIST (STRING TYPE)
- The metrics (of the table we're validating) → COMMA SEPARATED LIST (STRING TYPE)

Example:

```
insert into fw1_stg.kbhargava.validation_config_new (control_table, stage_table, validation_table_name, dimensions, metrics)
VALUES (
   "fw1_stg.kbhargava.f_order_selected_hourly_hoover_plus_control", "fw1_stg.kbhargava.f_order_selected_hourly_hoover_plus_stage_diff", 
    "f_order_selected_hourly", "'process_batch_id','network_id', 'content_owner_id', 'distributor_id', 'reseller_id', 'tv_network_id', 'transaction_type',
    'traffic_type', 'bit_flag', 'asset_id', 'series_id', 'asset_group_ids', 'site_section_id', 'site_id',
    'site_section_group_ids', 'airing_id', 'channel_id', 'break_id', 'time_position_class', 'inbound_mrm_rule_id',
    'mrm_rule_id', 'campaign_id', 'io_id', 'placement_id', 'ad_id', 'creative_id', 'delivery_method',
    'targeting_criteria_id', 'ad_unit_id', 'matched_audience_item_ids', 'matched_keyvalue_item_ids',
    'matched_daypart', 'placement_type_priority', 'platform_group', 'geo_visibility', 'user_agent_visibility',
    'postal_code', 'postal_code_package_ids', 'user_city_id', 'user_state_id', 'user_dma_code', 'user_country_id',
    'delivered_platform_browser_id', 'delivered_platform_device_id', 'delivered_platform_os_id', 'operator_zone_id',
    'integration_delivery_method', 'scenario_id', 'audience_extension_deal_id', 'tracked_audience_item_ids',
    'geo_state_visibility', 'geo_dma_visibility', 'geo_city_visibility', 'geo_zipcode_visibility',
    'key_value_visibility', 'slot_avail_type', 'linear_decision_type', 'standard_device_type_ids',
    'standard_environment_id', 'standard_os_id', 'standard_brand_id', 'standard_channel_id', 'standard_genre_ids',
    'content_form_id', 'content_rating_id', 'standard_language_ids', 'stream_mode_id', 'inventory_location_id',
    'mrm_rule_type_priority', 'listing_ids', 'inbound_order_id', 'inbound_listing_ids', 'outbound_order_id',
    'outbound_listing_ids', 'ip_enabled_audience_id', 'standard_programmer_id', 'geo_country_visibility',
    'standard_brand_visibility', 'standard_genre_visibility', 'content_rating_visibility', 'standard_endpoint_owner_id',
    'standard_endpoint_id', 'outbound_exchange_order_id', 'deal_id', 'buyer_group_id', 'dsp_id',
    'programmatic_advertiser_id', 'supply_source', 'sales_channel', 'standard_endpoint_owner_visibility',
    'standard_endpoint_visibility', 'inbound_order_auction_type', 'standard_content_daypart_id',
    'ssp_external_publisher_id', 'global_advertiser_ids', 'global_brand_ids', 'market_ad_id', 'trading_desk_id',
    'user_dma_code_id', 'global_industry_ids', 'buyer_platform_id', 'standard_programmer_visibility',
    'bidding_seat_id', 'rendition_id', 'bidding_buyer_id', 'global_agency_ids', 'standard_publisher_id',
    'bidder_seat_id', 'application_type', 'app_bundle', 'site_domain', 'global_currency_version', 'global_currency_id',
    'standard_app_id', 'profile_id', 'profile_type', 'standard_content_series_id', 'standard_content_subscription_model_id',
    'standard_ssp_channel_id', 'standard_site_domain_id', 'matched_inventory_package_ids', 'dsp_currency_id',
    'standard_operator_id', 'standard_iab_category_ids', 'upstream_inbound_order_id', 'upstream_global_currency_id',
    'standard_content_territory_id', 'standard_content_series_visibility', 'standard_content_credential_status_id',
    'external_seat_id', 'matched_contextual_segment_ids', 'inventory_package_ids', 'selected_yield_optimization_ids',
    'outbound_publisher_id', 'standard_retailer_id', 'standard_content_subscription_model_visibility',
    'standard_manufacturer_id', 'standard_app_bundle_id', 'content_owner_visibility', 'reseller_visibility',
    'slot_user_drop_off', 'sales_strategy', 'ivt_indicator', 'request_fill_status', 'slot_fill_status',
    'slot_sequence_normalized', 'slot_ad_unit_id', 'slot_removed_by_ux_indicator', 'live_linear_indicator',
    'ssp_bidder_indicator', 'ssp_bidder_buyer_indicator', 'partner_tag_indicator', 'promo_ad_indicator',
    'evergreen_ad_indicator', 'primary_ad_indicator', 'ad_with_fallback_indicator', 'priority_tier', 'priority_type',
    'priority_value', 'local_advertiser_id', 'failed_ad_error_code', 'decision_type', 'linear_avail_type',
    'station_id', 'ad_in_passback_indicator', 'loop_indicator', 'programmatic_device_type', 'standard_device_type_id',
    'standard_channel_visibility', 'content_form_visibility', 'bit_flag_aim_product_category', 'media_buyer_id',
    'post_auction_discount_id', 'selected_yo_volume_cap_ids', 'selected_yo_distribution_id', 'selected_yo_distribution_nip_id',
    'selected_yo_inventory_prioritization_id', 'selected_yo_inventory_prioritization_nip_id', 'selected_yo_margin_id',
    'integration_type', 'standard_content_viewership_profile_ids', 'standard_privacy_id', 'standard_addressability_ids',
    'standard_sport_entity_ids', 'selected_yield_optimization_info_ids', 'event_date'", "'selected_primary_ads', 'selected_fallback_ads', 'selected_margin', 'selected_bidding_revenue',
    'co_selected_bidding_revenue', 'd_selected_bidding_revenue', 'r_selected_bidding_revenue',
    'selected_fallback_margin', 'selected_fallback_bidding_revenue', 'co_selected_fallback_bidding_revenue',
    'd_selected_fallback_bidding_revenue', 'r_selected_fallback_bidding_revenue', 'ssp_bids',
    'ssp_co_bidding_revenue', 'placed_ads_in_played_slot', 'placed_ads_has_fallback_in_played_slot',
    'placed_fallback_ads_in_played_slot', 'filled_ads_in_played_slot', 'filled_ads_duration_in_played_slot',
    'filled_ads_sstf_fallback_in_played_slot', 'failed_ads_in_played_slot', 'selected_ads_in_played_slot',
    'selected_ads_in_played_slot_primary', 'selected_ads_in_played_slot_fallback', 'placed_ads_in_all_slot',
    'placed_ads_has_fallback_in_all_slot', 'placed_fallback_ads_in_all_slot', 'filled_ads_in_all_slot',
    'filled_ads_duration_in_all_slot', 'filled_ads_sstf_fallback_in_all_slot', 'failed_ads_in_all_slot',
    'selected_ads_in_all_slot', 'selected_ads_in_all_slot_primary', 'selected_ads_in_all_slot_fallback',
    'outbound_bids_in_played_slot', 'outbound_bidding_revenue_in_played_slot', 'upstream_bidding_revenue_in_played_slot'"
)
```


### Task Preparation

Now that we're prepared the data and the config, we need to prepare the databricks job (or task) to run this

We can create a SHARED validation job (shared with a few keys users (however, for the purpose of this example, we have a job already created (<https://freewheel-fw1-dev-e2.cloud.databricks.com/jobs/753910249184678?o=2929365364440953>)

Once a shared job is created, the steps below would become as easy as cloning a task and adding more validation tables.

- Head over to the tasks tab

- Click `Add Task` 

- Specify `Python Script`  (as the validation job is a python job)

- For specifying options:
    - Task name → whatever you want
        - Would be best to name it to the table that is validating
    - Type
        - Python Script
    - Source
        - Workspace
            - Assuming the validation script is uploaded to your workspace (if not, it's available in the Git link below)
    - Compute
        - validation\_file\_cluster 
    - Depends on
        - Empty (all tasks should be independent)
    - Parameters
        - \["--validation\_config","fw1\_stg.kbhargava.validation\_config\_new","–validation\_table","f\_order\_selected\_hourly"\]
- Once things are specified (the location of the validation python script, 

- You can hit Save Task and then run it!

- Click `Run Now`  to run

- Voila! Done
- Once the run is finished, if it errors, you can see it under `Runs`  or if it succeeds there are 2 paths
    - DATA MATCHED → no email; this is SUCCESS case
    - DATA MISMATCHED → see attachment below

### Mismatched Data Sample Email




### Next Steps

Now that we know that there are mismatches. The next steps are to figure out why the differences exist and how we can mitigate them. 

Most likely the mismatches arise from schema evolution changes between Hoover \<\> Hoover++ but there are also potentially bugs that were introduced. 

Using the SQLs from the email (sample email attached), we can investigate further and keep a check on things.

### Github for validation script

<https://github.freewheel.tv/data/hoover-model/blob/master/validation/scripts/validations.py>



## Questions?

@Bhargava, Karan 

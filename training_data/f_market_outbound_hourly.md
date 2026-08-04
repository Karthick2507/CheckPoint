# f\_market\_outbound\_hourly



### New Diffs

There are no diffs found. Query results match Hoover results.

---

**✅ \[STG\] VALIDATION PASSED - f\_market\_outbound\_hourly**  
**Environment:** STG  |  **Date:** 2026-06-30  |  **Hour:** 08  
**Control table:** `fw1_stg.edwin.f_market_outbound_hourly_control`  
**Stage table:** `fw1_stg.edwin.f_market_outbound_hourly_stage`

---

**📋 SUMMARY**

- Dimensions analyzed: 30 — ✓ pass
- Metrics analyzed: 4 — ✓ pass
- Row count: Control 386,571 / Stage 386,571 — ✓ match
- Row hashes — ✓ all match


**Hoover++ Query:**

```sql
CREATE TABLE IF NOT EXISTS fw1_stg.edwin.f_market_outbound_hourly_stage AS 
select network_id                         as network_id
     , asset_id                           as asset_id
     , series_id                          as series_id
     , site_id                            as site_id
     , site_section_id                    as site_section_id
     , country_id                         as country_id
     , time_position_class                as time_position_class
     , device_type                        as device_type
     , dsp_id                             as dsp_id
     , deal_id                            as deal_id
     , array(cast(-1 as long))            as buyer_id --deprecated. Set array(-1) as default value. Even if downstream unnest it, buyer_id can have -1 returned.
     , buyer_group_id                     as buyer_group_id
     , integration_type                   as integration_type
     , error_code                         as error_code
     , asset_group_ids                    as asset_group_ids
     , site_section_group_ids             as site_section_group_ids
     , sum(outbound_request)              as outbound_request
     , sum(outbound_request_user_matched) as outbound_request_user_matched
     , cast(0 as long)                    as outbound_opportunity --deprecated
     , process_batch_id                   as process_batch_id
     , buyer_platform_id                  as buyer_platform_id
     , array(cast(-1 as long))            as seat_ids --deprecated. Set array(-1) as default value. Even if downstream unnest it, seat_id can have -1 returned.
     , cast(0 as long)                    as imp_no_bids --deprecated
     , auction_status                     as auction_status
     , application_type                   as application_type
     , app_bundle                         as app_bundle
     , site_domain                        as site_domain
     , sum(pre_filtered_requests)         as pre_filtered_requests
     , supply_source                      as supply_source
     , content_owner_id                   as content_owner_id
     , sum(opportunities_in_bid_request)  as opportunities_in_bid_request
     , matched_inventory_package_ids      as matched_inventory_package_ids
     , geo_country_visibility             as geo_country_visibility
     , inventory_package_ids              as inventory_package_ids
     , event_date                         as event_date
from (
  select
    coalesce(auction_ctx.auction.network_id , cast(-1 as long))                                     as network_id
    , coalesce(auction_ctx.auction.asset_id, cast(-1 as long))                                      as asset_id
    , coalesce(auction_ctx.auction.series_id, cast(-1 as long))                                     as series_id
    , coalesce(auction_ctx.auction.site_id, cast(-1 as long))                                       as site_id
    , coalesce(auction_ctx.auction.site_section_id, cast(-1 as long))                               as site_section_id
    , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                  as country_id
    , coalesce(auction_ctx.auction.time_position_class, 'Unknown')                                as time_position_class
    , coalesce(auction_ctx.auction.device_type, 'Unknown')                                          as device_type
    , coalesce(auction_ctx.auction.dsp_id, cast(-1 as long))                                        as dsp_id
    , coalesce(partners.internal_deal_ids, cast(array() as array<long>))                             as deal_id
    , coalesce(auction_ctx.auction.buyer_group_id, cast(-1 as long))                                as buyer_group_id
    , coalesce(auction_ctx.auction.integration_type, '')                                            as integration_type
    , coalesce(auction_ctx.auction.error, '')                                                       as error_code
    , cast(array() as array<long>)                                                                  as asset_group_ids
    , cast(array() as array<long>)                                                             as site_section_group_ids
    , cast(1 as long) * coalesce(request.log_sampling.magnifier , cast(1 as long))
                   * coalesce(auction_ctx.auction.auction_sampling.magnifier , cast(1 as long))      as outbound_request
    , if((coalesce(auction_ctx.auction.flags, 0) & 1) > 0, 
        cast(1 as long),
        cast(0 as long)) * coalesce(request.log_sampling.magnifier , cast(1 as long))
                     * coalesce(auction_ctx.auction.auction_sampling.magnifier , cast(1 as long))                         as outbound_request_user_matched
    , date_format(date_trunc('HOUR', cast(request.timestamp as timestamp)), 'yyyyMMddHHmmss')       as process_batch_id
    , coalesce(auction_ctx.auction.buyer_platform_id, cast(-1 as long))                             as buyer_platform_id
    , coalesce(auction_ctx.auction.auction_status, cast(0 as long))                                 as auction_status
    , coalesce(auction_ctx.auction.application_type, '')                                            as application_type
    , coalesce(auction_ctx.auction.app_bundle, '')                                                  as app_bundle
    , coalesce(auction_ctx.auction.site_domain, '')                                                 as site_domain
    , if((coalesce(auction_ctx.auction.flags, 0) & 262144) > 0,
            cast(1 as long),
             if((coalesce(auction_ctx.auction.auction_status, cast(0 as long)) & 1 ) > 0 and
                coalesce(auction_ctx.auction.error, '') in ('LAT_UNSUPPORTED', 'GDPR_UNSUPPORTED','COPPA_UNSUPPORTED', 'CCPA_UNSUPPORTED', 'ATTS_UNSUPPORTED', 'GPP_UNSUPPORTED'),
                cast(1 as long), 
                cast(0 as long))) 
                * coalesce(request.log_sampling.magnifier, cast(1 as long))
                * coalesce(auction_ctx.auction.auction_sampling.magnifier , cast(1 as long))        as pre_filtered_requests
    , coalesce(partners.supply_source, cast(-1 as int))                                             as supply_source
    , coalesce(partners.content_owner_network_id, cast(-1 as long))                                 as content_owner_id
    , cast(0 as long)                                                                        as opportunities_in_bid_request
    , coalesce(partners.matched_inventory_package_ids, cast(array() as array<long>))        as matched_inventory_package_ids
    , coalesce(partners.geo_country_visibility.report_aggregate, 'FULL_VISIBILITY')                as geo_country_visibility
    , cast(array() as array<long>)                                                                 as inventory_package_ids
    , date_trunc('HOUR', cast(request.timestamp as timestamp))                                     as event_date
    from fw1_hoover_prd.hoover_batch.auction AS original
    lateral view explode(auction_ctxes) AS auction_ctx
    lateral view explode(auction_ctx.networks) AS partners
    where coalesce(auction_ctx.auction.integration_type, '') in ('NORMAL', 'PG_TD')
    AND partners.entity_source = 'auction'
    AND auction_ctx.auction.is_faked_auction = false
    AND date_trunc('HOUR', cast(request.timestamp as TIMESTAMP))='2026-06-30T08:00:00.000+00:00'

UNION all

select
     coalesce(auction_ctx.auction.network_id , cast(-1 as long))                                     as network_id
     , coalesce(auction_ctx.auction.asset_id, cast(-1 as long))                                      as asset_id
     , coalesce(auction_ctx.auction.series_id, cast(-1 as long))                                     as series_id
     , coalesce(auction_ctx.auction.site_id, cast(-1 as long))                                       as site_id
     , coalesce(auction_ctx.auction.site_section_id, cast(-1 as long))                               as site_section_id
     , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                  as country_id
     , coalesce(auction_ctx.auction.time_position_class, 'Unknown')                                  as time_position_class
     , coalesce(auction_ctx.auction.device_type, 'Unknown')                                          as device_type
     , coalesce(auction_ctx.auction.dsp_id, cast(-1 as long))                                        as dsp_id
     , coalesce(SORT_ARRAY(filter(imp.deals.internal_deal_id, deal_id -> deal_id IS NOT NULL))
        , cast(array() as array<long>))                                                              as deal_ids -- sort array ascend, as network.internal_deal_ids. So more rows can merge with the first union part
     , coalesce(auction_ctx.auction.buyer_group_id, cast(-1 as long))                                as buyer_group_id
     , coalesce(auction_ctx.auction.integration_type, '')                                            as integration_type
     , coalesce(auction_ctx.auction.error, '')                                                       as error_code
     , cast(array() as array<long>)                                                                  as asset_group_ids
     , cast(array() as array<long>)                                                                as site_section_group_ids
     , cast(0 as long)                                                                               as outbound_request
     , cast(0 as long)                                                                      as outbound_request_user_matched
     , date_format(date_trunc('HOUR', cast(request.timestamp as timestamp)), 'yyyyMMddHHmmss')       as process_batch_id
     , coalesce(auction_ctx.auction.buyer_platform_id, cast(-1 as long))                             as buyer_platform_id
     , coalesce(auction_ctx.auction.auction_status, cast(0 as long))                                 as auction_status
     , coalesce(auction_ctx.auction.application_type, '')                                            as application_type
     , coalesce(auction_ctx.auction.app_bundle, '')                                                  as app_bundle
     , coalesce(auction_ctx.auction.site_domain, '')                                                 as site_domain
     , cast(0 as long)                                                                              as pre_filtered_requests
     , coalesce(partners.supply_source, cast(-1 as int))                                              as supply_source
     , coalesce(partners.content_owner_network_id, cast(-1 as long))                                  as content_owner_id
     , coalesce(imp.equivalent_opportunity_number, cast(1 as long)) * 
                 coalesce(request.log_sampling.magnifier, cast(1 as long)) *
                 coalesce(auction_ctx.auction.auction_sampling.magnifier , cast(1 as long))                      as opportunities_in_bid_request
     , coalesce(imp.matched_inventory_package_ids, cast(array() as array<long>))                     as matched_inventory_package_ids
     , coalesce(partners.geo_country_visibility.report_aggregate, 'FULL_VISIBILITY')               as geo_country_visibility
     , cast(array() as array<long>)                                                                as inventory_package_ids
     , date_trunc('HOUR', cast(request.timestamp as timestamp))                                    as event_date
    from fw1_hoover_prd.hoover_batch.auction AS original
    lateral view explode(auction_ctxes) AS auction_ctx
    lateral view explode(auction_ctx.networks) AS partners
         lateral view explode(auction_ctx.auction.impression) as imp
    where coalesce(auction_ctx.auction.integration_type, '') in ('NORMAL', 'PG_TD')
    AND partners.entity_source = 'auction'
    AND auction_ctx.auction.is_faked_auction = false
    AND date_trunc('HOUR', cast(request.timestamp as TIMESTAMP))='2026-06-30T08:00:00.000+00:00'
)
group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,21,22,23,24,25,26,27,29,30,32,33,34,35
```

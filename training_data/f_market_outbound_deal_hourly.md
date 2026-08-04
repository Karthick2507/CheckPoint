# f\_market\_outbound\_deal\_hourly

### New Diffs

There are no diffs found. Query results match Hoover results.

---

**✅ \[STG\] VALIDATION PASSED - f\_market\_outbound\_deal\_hourly**  
**Environment:** STG  |  **Date:** 2026-06-30  |  **Hour:** 08  
**Control table:** `fw1_stg.edwin.f_market_outbound_deal_hourly_control`  
**Stage table:** `fw1_stg.edwin.f_market_outbound_deal_hourly_stage`

---

**📋 SUMMARY**

- Dimensions analyzed: 24 — ✓ pass
- Metrics analyzed: 6 — ✓ pass
- Row count: Control 5,053,668 / Stage 5,053,668 — ✓ match
- Row hashes — ✓ all match

**Hoover++ Query:**

```sql
select coalesce(inner_table.network_id, cast(-1 as long))                                        as network_id
     , coalesce(inner_table.asset_id, cast(-1 as long))                                          as asset_id
     , coalesce(inner_table.series_id, cast(-1 as long))                                         as series_id
     , coalesce(inner_table.site_id, cast(-1 as long))                                           as site_id
     , coalesce(inner_table.site_section_id, cast(-1 as long))                                   as site_section_id
     , coalesce(cast(inner_table.country_id as long), cast(-1 as long))                          as country_id
     , coalesce(inner_table.time_position_class, 'Unknown')                                      as time_position_class
     , coalesce(inner_table.device_type, 'Unknown')                                              as device_type
     , coalesce(inner_table.dsp_id, cast(-1 as long))                                            as dsp_id
     , coalesce(deal_id, cast(-1 as long))                                                       as deal_id
     , array(cast(-1 as long))                                                                   as buyer_id
     , cast(-1 as long)                                                                          as buyer_group_id
     , coalesce(inner_table.integration_type, '')                                                as integration_type
     , coalesce(inner_table.error_code, '')                                                      as error_code
     , cast(array() as array<long >)                                                             as asset_group_ids
     , cast(array() as array<long >)                                                             as site_section_group_ids
     , sum(cast(1 as long) * coalesce(inner_table.request_log_sampling_magnifier , cast(1 as long))
              *  coalesce(inner_table.auction_sampling_magnifier , cast(1 as long)))             as outbound_request
     , sum(if((coalesce(inner_table.flags, 0) & 1) > 0, 
                  cast(1 as long),
                  cast(0 as long)) * coalesce(inner_table.request_log_sampling_magnifier , cast(1 as long))
                  * coalesce(inner_table.auction_sampling_magnifier , cast(1 as long)))          as outbound_request_user_matched
     , cast(0 as long)                                                                           as outbound_opportunity
     , date_format(date_trunc('HOUR', cast(inner_table.request_timestamp as timestamp)), 'yyyyMMddHHmmss') as process_batch_id
     , coalesce(inner_table.buyer_platform_id, cast(-1 as long))                                 as buyer_platform_id
     , array(cast(-1 as long))                                                                   as seat_ids
     , cast(0 as long)                                                                           as imp_no_bids
     , coalesce(inner_table.auction_status, cast(0 as long))                                     as auction_status
     , coalesce(inner_table.application_type, '')                                                as application_type
     , coalesce(inner_table.app_bundle, '')                                                      as app_bundle
     , coalesce(inner_table.site_domain, '')                                                     as site_domain
     , sum(if((coalesce(inner_table.flags, 0) & 262144) > 0, cast(1 as long),
              if((coalesce(inner_table.auction_status, cast(0 as long)) & 1) > 0 and
                 coalesce(inner_table.error_code, '') in
                 ('LAT_UNSUPPORTED', 'GDPR_UNSUPPORTED', 'COPPA_UNSUPPORTED', 'CCPA_UNSUPPORTED', 'ATTS_UNSUPPORTED',
                  'GPP_UNSUPPORTED'), cast(1 as long), cast(0 as long)))
                  * coalesce(inner_table.request_log_sampling_magnifier, cast(1 as long))
                  * coalesce(inner_table.auction_sampling_magnifier , cast(1 as long)))          as pre_filtered_requests
     , sum(inner_table.internal_bids[idx]
            * coalesce(inner_table.request_log_sampling_magnifier , cast(1 as long))
            * coalesce(inner_table.auction_sampling_magnifier , cast(1 as long)))                as opportunities_in_bid_request
     , coalesce(inner_table.geo_country_visibility, 'FULL_VISIBILITY')                           as geo_country_visibility
     , date_trunc('HOUR', cast(inner_table.request_timestamp as timestamp))                      as event_date
from (select auction_ctx.auction.network_id                                                             as network_id,
             auction_ctx.auction.asset_id                                                               as asset_id,
             auction_ctx.auction.series_id                                                              as series_id,
             auction_ctx.auction.site_id                                                                as site_id,
             auction_ctx.auction.site_section_id                                                        as site_section_id,
             visitor.country_id                                                                      as country_id,
             auction_ctx.auction.time_position_class                                                 as time_position_class,
             auction_ctx.auction.device_type                                                            as device_type,
             auction_ctx.auction.dsp_id                                                                 as dsp_id,
             filter(partners.internal_deal_ids, id -> coalesce(id, cast(-1 as long)) > 0)    as internal_deal_ids,
             transform(filter(partners.internal_deal_ids, id -> coalesce(id, cast(-1 as long)) > 0),
                       id -> (aggregate(transform(auction_ctx.auction.impression,
                                                  x -> if(array_contains(x.deals.internal_deal_id, id),
                                                          coalesce(x.equivalent_opportunity_number, cast(1 as long)),
                                                          cast(0 as long))),
                                        cast(0 as long), (acc, element) -> acc + element))) as internal_bids,
             auction_ctx.auction.integration_type                                                       as integration_type,
             auction_ctx.auction.error                                                                  as error_code,
             auction_ctx.auction.flags                                                                  as flags,
             auction_ctx.auction.buyer_platform_id                                                      as buyer_platform_id,
             auction_ctx.auction.auction_status                                                         as auction_status,
             auction_ctx.auction.application_type                                                       as application_type,
             auction_ctx.auction.app_bundle                                                             as app_bundle,
             auction_ctx.auction.site_domain                                                            as site_domain,
             partners.geo_country_visibility.report_aggregate                                as geo_country_visibility,
             request.log_sampling.magnifier                                               as request_log_sampling_magnifier,
             auction_ctx.auction.auction_sampling.magnifier                                   as auction_sampling_magnifier,
             request.timestamp                                                              as request_timestamp
    from fw1_hoover_prd.hoover_batch.auction AS original
    lateral view explode(auction_ctxes) AS auction_ctx
    lateral view explode(auction_ctx.networks) AS partners
    where
            coalesce(auction_ctx.auction.integration_type, '') in ('NORMAL', 'PG_TD')
            and partners.entity_source = 'auction'
            and auction_ctx.auction.is_faked_auction = false
            and date_trunc('HOUR', cast(request.timestamp as TIMESTAMP))='2026-06-30T08:00:00.000+00:00'
      ) inner_table
      lateral view posexplode(inner_table.internal_deal_ids) as idx,deal_id
group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22, 24, 25, 26, 27, 30, 31
```

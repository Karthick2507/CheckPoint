# Hoover\+\+ Validation \(Concrete Example\)

### Data Preparation

The below guide is for validating `f_process_request_hourly_sampling`  (other tables can be validated in a similar fashion)

I've been manually playing around with validating 1 hour (once we have it in a "good" spot, we can make it a continuous validation by constantly loading data in and comparing)

We want to compare apples to apples between our "stage" and "control" tables. So we need to prepare the data for it.

#### Steps

##### Create table(s) 

**CONTROL:**

```
CREATE TABLE fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive
(
    process_batch_id                   string,
    network_id                         bigint,
    content_owner_id                   bigint,
    distributor_id                     bigint,
    tv_network_id                      bigint,
    transaction_type                   string,
    traffic_type                       bigint,
    bit_flag                           bigint,
    asset_id                           bigint,
    series_id                          bigint,
    asset_group_ids                    array<bigint>,
    site_section_id                    bigint,
    site_id                            bigint,
    site_section_group_ids             array<bigint>,
    airing_id                          bigint,
    channel_id                         bigint,
    platform_group                     string,
    postal_code                        string,
    postal_code_package_ids            array<integer>,
    user_city_id                       integer,
    user_state_id                      integer,
    user_dma_code_id                   integer,
    user_country_id                    bigint,
    operator_zone_id                   bigint,
    geo_country_visibility             string,
    geo_state_visibility               string,
    geo_dma_visibility                 string,
    geo_city_visibility                string,
    geo_zipcode_visibility             string,
    privacy_jurisdiction_ids           array<integer>,
    privacy_choice_ids                 array<integer>,
    ad_requests                        bigint,
    profile_id                         bigint,
    profile_type                       string,
    client_facing_ivt_reason_flag      bigint,
    total_ad_requests                  bigint,
    standard_endpoint_id               integer,
    standard_device_type_id            integer,
    standard_endpoint_visibility       string,
    user_agent_visibility              string,
    inventory_package_ids              array<bigint>,
    standard_os_id                     integer,
    delivered_platform_browser_id      bigint,
    request_chain_type                 string,
    video_cro_network_id               bigint,
    request_context_network_id         bigint,
    ivt_indicator                      boolean,
    live_linear_indicator              boolean,
    ssp_bidder_indicator               boolean,
    standard_publisher_id              bigint,
    standard_app_id                    bigint,
    standard_brand_id                  integer,
    standard_brand_visibility          string,
    standard_programmer_id             integer,
    standard_programmer_visibility     string,
    content_form_id                    integer,
    stream_mode_id                     integer,
    standard_endpoint_owner_id         integer,
    standard_endpoint_owner_visibility string,
    standard_environment_id            integer,
    request_fill_status                string,
    time_position_classes              array<string>,
    slot_ad_unit_ids                   array<bigint>,
    content_form_visibility            string,
    standard_app_bundle_id             bigint,
    standard_site_domain_id            bigint,
    event_date                         timestamp
);
```

  

**STAGE:**

```
CREATE TABLE fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus
(
    process_batch_id                   string,
    network_id                         bigint,
    content_owner_id                   bigint,
    distributor_id                     bigint,
    tv_network_id                      bigint,
    transaction_type                   string,
    traffic_type                       bigint,
    bit_flag                           bigint,
    asset_id                           bigint,
    series_id                          bigint,
    asset_group_ids                    array<bigint>,
    site_section_id                    bigint,
    site_id                            bigint,
    site_section_group_ids             array<bigint>,
    airing_id                          bigint,
    channel_id                         bigint,
    platform_group                     string,
    postal_code                        string,
    postal_code_package_ids            array<integer>,
    user_city_id                       integer,
    user_state_id                      integer,
    user_dma_code_id                   integer,
    user_country_id                    bigint,
    operator_zone_id                   bigint,
    geo_country_visibility             string,
    geo_state_visibility               string,
    geo_dma_visibility                 string,
    geo_city_visibility                string,
    geo_zipcode_visibility             string,
    privacy_jurisdiction_ids           array<integer>,
    privacy_choice_ids                 array<integer>,
    ad_requests                        bigint,
    profile_id                         bigint,
    profile_type                       string,
    client_facing_ivt_reason_flag      bigint,
    total_ad_requests                  bigint,
    standard_endpoint_id               integer,
    standard_device_type_id            integer,
    standard_endpoint_visibility       string,
    user_agent_visibility              string,
    inventory_package_ids              array<bigint>,
    standard_os_id                     integer,
    delivered_platform_browser_id      bigint,
    request_chain_type                 string,
    video_cro_network_id               bigint,
    request_context_network_id         bigint,
    ivt_indicator                      boolean,
    live_linear_indicator              boolean,
    ssp_bidder_indicator               boolean,
    standard_publisher_id              bigint,
    standard_app_id                    bigint,
    standard_brand_id                  integer,
    standard_brand_visibility          string,
    standard_programmer_id             integer,
    standard_programmer_visibility     string,
    content_form_id                    integer,
    stream_mode_id                     integer,
    standard_endpoint_owner_id         integer,
    standard_endpoint_owner_visibility string,
    standard_environment_id            integer,
    request_fill_status                string,
    time_position_classes              array<string>,
    slot_ad_unit_ids                   array<bigint>,
    content_form_visibility            string,
    standard_app_bundle_id             bigint,
    standard_site_domain_id            bigint,
    event_date                         timestamp
);
```

  

##### Load data in said tables:

**CONTROL:**

```
INSERT INTO fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive(
     SELECT * FROM hive_data_prd_dwh_etl.aggregate.f_process_request_hourly_sampling
     where event_date = date_trunc('HOUR', CURRENT_TIMESTAMP()) - INTERVAL 4 hours
);
```

  

  

**STAGE:**

There are a few caveats here. 

1. If your original query is from ANY table (that is not the `ack`  table)  Hoover table, be sure to add `is_first_request=true`  in your where clause.
2. Make sure to add `event_hour`  boundaries (this helps prune data from the compaction table and makes the load quick)

  

```
INSERT INTO fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus(

    select process_batch_id                   as process_batch_id
         , network_id                         as network_id
         , content_owner_id                   as content_owner_id
         , distributor_id                     as distributor_id
         , tv_network_id                      as tv_network_id
         , transaction_type                   as transaction_type
         , traffic_type                       as traffic_type
         , bit_flag                           as bit_flag
         , asset_id                           as asset_id
         , series_id                          as series_id
         , asset_group_ids                    as asset_group_ids
         , site_section_id                    as site_section_id
         , site_id                            as site_id
         , site_section_group_ids             as site_section_group_ids
         , airing_id                          as airing_id
         , channel_id                         as channel_id
         , platform_group                     as platform_group
         , postal_code                        as postal_code
         , postal_code_package_ids            as postal_code_package_ids
         , user_city_id                       as user_city_id
         , user_state_id                      as user_state_id
         , user_dma_code_id                   as user_dma_code_id
         , user_country_id                    as user_country_id
         , operator_zone_id                   as operator_zone_id
         , geo_country_visibility             as geo_country_visibility
         , geo_state_visibility               as geo_state_visibility
         , geo_dma_visibility                 as geo_dma_visibility
         , geo_city_visibility                as geo_city_visibility
         , geo_zipcode_visibility             as geo_zipcode_visibility
         , privacy_jurisdiction_ids           as privacy_jurisdiction_ids
         , privacy_choice_ids                 as privacy_choice_ids
         , sum(ad_requests)                   as ad_requests
         , profile_id                         as profile_id
         , profile_type                       as profile_type
         , client_facing_ivt_reason_flag      as client_facing_ivt_reason_flag
         , sum(total_ad_requests)             as total_ad_requests
         , standard_endpoint_id               as standard_endpoint_id
         , standard_device_type_id            as standard_device_type_id
         , standard_endpoint_visibility       as standard_endpoint_visibility
         , user_agent_visibility              as user_agent_visibility
         , inventory_package_ids              as inventory_package_ids
         , standard_os_id                     as standard_os_id
         , delivered_platform_browser_id      as delivered_platform_browser_id
         , request_chain_type                 as request_chain_type
         , video_cro_network_id               as video_cro_network_id
         , request_context_network_id         as request_context_network_id
         , ivt_indicator                      as ivt_indicator
         , live_linear_indicator              as live_linear_indicator
         , ssp_bidder_indicator               as ssp_bidder_indicator
         , standard_publisher_id              as standard_publisher_id
         , standard_app_id                    as standard_app_id
         , standard_brand_id                  as standard_brand_id
         , standard_brand_visibility          as standard_brand_visibility
         , standard_programmer_id             as standard_programmer_id
         , standard_programmer_visibility     as standard_programmer_visibility
         , content_form_id                    as content_form_id
         , stream_mode_id                     as stream_mode_id
         , standard_endpoint_owner_id         as standard_endpoint_owner_id
         , standard_endpoint_owner_visibility as standard_endpoint_owner_visibility
         , standard_environment_id            as standard_environment_id
         , request_fill_status                as request_fill_status
         , time_position_classes              as time_position_classes
         , slot_ad_unit_ids                   as slot_ad_unit_ids
         , content_form_visibility            as content_form_visibility
         , standard_app_bundle_id             as standard_app_bundle_id
         , standard_site_domain_id            as standard_site_domain_id
         , event_date                         as event_date
    from (select event_hour                                                                                    as process_batch_id
               , coalesce(network.network_id, cast(-1 as long))                                                     as network_id
               , coalesce(network.content_owner_network_id, cast(-1 as long))                                       as content_owner_id
               , if(coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and
                    coalesce(network.role, "") = "CRO", cast(-3 as long),
                    coalesce(network.distributor_network_id, cast(-1 as long)))                                     as distributor_id
               , coalesce(request.context.tv_network_id, cast(-1 as long))                                          as tv_network_id
               , coalesce(network.role, "")                                                                         as transaction_type
               , coalesce(request.traffic_type, cast(0 as long))                                                    as traffic_type
               , coalesce(network.bit_flags, cast(0 as long)) +
                 coalesce(request.bit_flags, cast(0 as long))                                                       as bit_flag
               , coalesce(network.asset_id, cast(-1 as long))                                                       as asset_id
               , coalesce(network.series_id, cast(-1 as long))                                                      as series_id
               , coalesce(network.asset_group_ids, cast(array() as array<long >))                                   as asset_group_ids
               , coalesce(network.site_section_id, cast(-1 as long))                                                as site_section_id
               , coalesce(network.site_id, cast(-1 as long))                                                        as site_id
               , coalesce(network.site_section_group_ids,
                          cast(array() as array<long >))                                                            as site_section_group_ids
               , network.airing_id                                                                                  as airing_id
               , network.airing_channel_id                                                                          as channel_id
               , coalesce(visitor.platform_group, "-1")                                                             as platform_group
               , coalesce(visitor.postal_code, "-1")                                                                as postal_code
               , coalesce(network.postal_code_package_ids,
                          cast(array() as array<int>))                                                              as postal_code_package_ids
               , coalesce(visitor.city_id, cast(-1 as int))                                                         as user_city_id
               , coalesce(visitor.state_id, cast(-1 as int))                                                        as user_state_id
               , coalesce(visitor.dma_code_id, cast(-1 as int))                                                     as user_dma_code_id
               , coalesce(cast(visitor.country_id as long), cast(-1 as long))                                       as user_country_id
               , coalesce(visitor.operator_zone_id, cast(-1 as long))                                               as operator_zone_id
               , coalesce(network.geo_country_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as geo_country_visibility
               , coalesce(network.geo_state_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as geo_state_visibility
               , coalesce(network.geo_dma_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as geo_dma_visibility
               , coalesce(network.geo_city_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as geo_city_visibility
               , coalesce(network.geo_zip_code_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as geo_zipcode_visibility
               , coalesce(request.privacy_jurisdiction_ids,
                          cast(array() as array<int>))                                                              as privacy_jurisdiction_ids
               , coalesce(request.privacy_choice_ids, cast(array() as array<int>))                                  as privacy_choice_ids
               , cast(1 as long) * coalesce(request.multiplier, cast(1 as long)) *
                 coalesce(request.magnifier, cast(1 as long)) *
                 coalesce(request.log_sampling.magnifier, cast(1 as long))                                          as ad_requests
               , if(coalesce(request.extra_flags, cast(0 as long)) & 1073741824 = 1073741824 and
                    coalesce(network.role, "") = "CRO", cast(-3 as long),
                    coalesce(request.context.profile_id, cast(-1 as long)))                                         as profile_id
               , coalesce(request.context.profile_type, 'UNKNOWN')                                                  as profile_type
               , coalesce(request.client_facing_ivt_reason_flag, cast(0 as long))                                   as client_facing_ivt_reason_flag
               , cast(0 as long)                                                                                    as total_ad_requests
               , coalesce(request.context.standard_endpoint_id, cast(-1 as int))                                    as standard_endpoint_id
               , coalesce(visitor.standard_device_type_child_id, cast(-1 as int))                                   as standard_device_type_id
               , coalesce(network.standard_endpoint_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as standard_endpoint_visibility
               , coalesce(network.user_agent_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as user_agent_visibility
               , cast(array() as array<long>)                                                                       as inventory_package_ids
               , coalesce(visitor.standard_os_id, cast(-1 as int))                                                  as standard_os_id
               , coalesce(visitor.platform_browser_id, cast(-1 as long))                                            as delivered_platform_browser_id
               , 'ASSET'                                                                                            as request_chain_type
               , coalesce(request.context.video_cro_network_id, cast(-1 as long))                                   as video_cro_network_id
               , coalesce(request.context.network_id, cast(-1 as long))                                             as request_context_network_id
               , if(coalesce(request.traffic_type, cast(0 as long)) != 0, true, false)                              as ivt_indicator
               , if(coalesce(request.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 9) > 0, true, false)  as live_linear_indicator
               , if(coalesce(request.bit_flags, cast(0 as long)) & shiftleft(cast(1 as long), 34) > 0, true, false) as ssp_bidder_indicator
               , coalesce(request.context.standard_publisher_id, cast(-1 as long))                                  as standard_publisher_id
               , coalesce(request.context.standard_app_id, cast(-1 as long))                                        as standard_app_id
               , coalesce(request.context.standard_brand_id, cast(-1 as int))                                       as standard_brand_id
               , coalesce(network.standard_brand_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as standard_brand_visibility
               , coalesce(request.context.standard_programmer_id, cast(-1 as int))                                  as standard_programmer_id
               , coalesce(network.standard_programmer_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as standard_programmer_visibility
               , coalesce(request.context.content_form_id, cast(-1 as int))                                         as content_form_id
               , coalesce(request.context.stream_mode_id, cast(-1 as int))                                          as stream_mode_id
               , coalesce(request.context.standard_endpoint_owner_id,
                          cast(-1 as int))                                                                          as standard_endpoint_owner_id
               , coalesce(network.standard_endpoint_owner_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as standard_endpoint_owner_visibility
               , coalesce(visitor.standard_environment_id, cast(-1 as int))                                         as standard_environment_id
               , case
                     when coalesce(request.flags, cast(0 as long)) & 32 > 0 then 'No Selection'
                     when coalesce(request.advertisement_delivered_count, request.advertisement_count, cast(0 as long)) = 0
                         then 'Empty'
                     else 'Filled'
            end                                                                                                     as request_fill_status
               , coalesce(request_info.slot_time_position_classes,
                          cast(array() as array<string>))                                                           as time_position_classes
               , coalesce(request_info.slot_video_cro_ad_unit_ids,
                          cast(array() as array<long>))                                                             as slot_ad_unit_ids
               , coalesce(network.content_form_visibility.report_aggregate,
                          "FULL_VISIBILITY")                                                                        as content_form_visibility
               , coalesce(request.context.standard_app_bundle_id, cast(-1 as long))                                 as standard_app_bundle_id
               , coalesce(request.context.standard_site_domain_id,
                          cast(-1 as long))                                                                         as standard_site_domain_id
               , date_trunc('HOUR', cast(request.timestamp as timestamp))                                           as event_date
          from fw1_prd.hoover_pipeline_compaction.hoover_compaction lateral view explode(inventory.asset_chains) as network
          where coalesce (network.role
              , "") in ("CRO"
              , "D")                -- only report for cro and d
            and cast (request.timestamp as TIMESTAMP) >= to_timestamp(event_hour, 'yyyyMMddHHmmss') - interval '4' hours
            AND event_hour >= date_format(date_trunc('hour', current_timestamp) - interval 4 hour, 'yyyyMMddHH000')
            AND event_hour < date_format(date_trunc('hour', current_timestamp) - interval 3 hour, 'yyyyMMddHH000')
            and not (coalesce (network.role
              , "") = "D"
            and coalesce (network.network_id
              , cast (-1 as long)) = coalesce (network.content_owner_network_id
              , cast (-1 as long))) -- remove the D when D is the same as CRO
          and idx.is_first_request = true


          union all
          --no asset chain, check the site_section_chain
          select event_hour as process_batch_id
                  , coalesce (network.network_id, cast (-1 as long)) as network_id
                  , coalesce (network.content_owner_network_id, cast (-1 as long)) as content_owner_id
                  , if(coalesce (request.extra_flags, cast (0 as long)) & 1073741824 = 1073741824 and
              coalesce (network.role, "") = "CRO", cast (-3 as long), coalesce (network.distributor_network_id, cast (-1 as long))) as distributor_id
                  , coalesce (request.context.tv_network_id, cast (-1 as long)) as tv_network_id
                  , coalesce (network.role, "") as transaction_type
                  , coalesce (request.traffic_type, cast (0 as long)) as traffic_type
                  , coalesce (network.bit_flags, cast (0 as long)) + coalesce (request.bit_flags, cast (0 as long)) as bit_flag
                  , coalesce (network.asset_id, cast (-1 as long)) as asset_id
                  , coalesce (network.series_id, cast (-1 as long)) as series_id
                  , coalesce (network.asset_group_ids, cast (array() as array<long >)) as asset_group_ids
                  , coalesce (network.site_section_id, cast (-1 as long)) as site_section_id
                  , coalesce (network.site_id, cast (-1 as long)) as site_id
                  , coalesce (network.site_section_group_ids, cast (array() as array<long >)) as site_section_group_ids
                  , network.airing_id as airing_id
                  , network.airing_channel_id as channel_id
                  , coalesce (visitor.platform_group, "-1") as platform_group
                  , coalesce (visitor.postal_code, "-1") as postal_code
                  , coalesce (network.postal_code_package_ids, cast (array() as array< int >)) as postal_code_package_ids
                  , coalesce (visitor.city_id, cast (-1 as int)) as user_city_id
                  , coalesce (visitor.state_id, cast (-1 as int)) as user_state_id
                  , coalesce (visitor.dma_code_id, cast (-1 as int)) as user_dma_code_id
                  , coalesce (cast (visitor.country_id as long), cast (-1 as long)) as user_country_id
                  , coalesce (visitor.operator_zone_id, cast (-1 as long)) as operator_zone_id
                  , coalesce (network.geo_country_visibility.report_aggregate, "FULL_VISIBILITY") as geo_country_visibility
                  , coalesce (network.geo_state_visibility.report_aggregate, "FULL_VISIBILITY") as geo_state_visibility
                  , coalesce (network.geo_dma_visibility.report_aggregate, "FULL_VISIBILITY") as geo_dma_visibility
                  , coalesce (network.geo_city_visibility.report_aggregate, "FULL_VISIBILITY") as geo_city_visibility
                  , coalesce (network.geo_zip_code_visibility.report_aggregate, "FULL_VISIBILITY") as geo_zipcode_visibility
                  , coalesce (request.privacy_jurisdiction_ids, cast (array() as array< int >)) as privacy_jurisdiction_ids
                  , coalesce (request.privacy_choice_ids, cast (array() as array< int >)) as privacy_choice_ids
                  , cast (1 as long) * coalesce (request.multiplier, cast (1 as long)) *
              coalesce (request.magnifier, cast (1 as long)) *
              coalesce (request.log_sampling.magnifier, cast (1 as long)) as ad_requests
                  , if(coalesce (request.extra_flags, cast (0 as long)) & 1073741824 = 1073741824 and
              coalesce (network.role, "") = "CRO", cast (-3 as long), coalesce (request.context.profile_id, cast (-1 as long))) as profile_id
                  , coalesce (request.context.profile_type, 'UNKNOWN') as profile_type
                  , coalesce (request.client_facing_ivt_reason_flag, cast (0 as long)) as client_facing_ivt_reason_flag
                  , cast (0 as long) as total_ad_requests
                  , coalesce (request.context.standard_endpoint_id, cast (-1 as int)) as standard_endpoint_id
                  , coalesce (visitor.standard_device_type_child_id, cast (-1 as int)) as standard_device_type_id
                  , coalesce (network.standard_endpoint_visibility.report_aggregate, "FULL_VISIBILITY") as standard_endpoint_visibility
                  , coalesce (network.user_agent_visibility.report_aggregate, "FULL_VISIBILITY") as user_agent_visibility
                  , cast (array() as array<long>) as inventory_package_ids
                  , coalesce (visitor.standard_os_id, cast (-1 as int)) as standard_os_id
                  , coalesce (visitor.platform_browser_id, cast (-1 as long)) as delivered_platform_browser_id
                  , 'SITE' as request_chain_type
                  , coalesce (request.context.video_cro_network_id, cast (-1 as long)) as video_cro_network_id
                  , coalesce (request.context.network_id, cast (-1 as long)) as request_context_network_id
                  , if(coalesce (request.traffic_type, cast (0 as long)) != 0, true, false) as ivt_indicator
                  , if(coalesce (request.bit_flags, cast (0 as long)) & shiftleft(cast (1 as long), 9) > 0, true, false) as live_linear_indicator
                  , if(coalesce (request.bit_flags, cast (0 as long)) & shiftleft(cast (1 as long), 34) > 0, true, false) as ssp_bidder_indicator
                  , coalesce (request.context.standard_publisher_id, cast (-1 as long)) as standard_publisher_id
                  , coalesce (request.context.standard_app_id, cast (-1 as long)) as standard_app_id
                  , coalesce (request.context.standard_brand_id, cast (-1 as int)) as standard_brand_id
                  , coalesce (network.standard_brand_visibility.report_aggregate, "FULL_VISIBILITY") as standard_brand_visibility
                  , coalesce (request.context.standard_programmer_id, cast (-1 as int)) as standard_programmer_id
                  , coalesce (network.standard_programmer_visibility.report_aggregate, "FULL_VISIBILITY") as standard_programmer_visibility
                  , coalesce (request.context.content_form_id, cast (-1 as int)) as content_form_id
                  , coalesce (request.context.stream_mode_id, cast (-1 as int)) as stream_mode_id
                  , coalesce (request.context.standard_endpoint_owner_id, cast (-1 as int)) as standard_endpoint_owner_id
                  , coalesce (network.standard_endpoint_owner_visibility.report_aggregate, "FULL_VISIBILITY") as standard_endpoint_owner_visibility
                  , coalesce (visitor.standard_environment_id, cast (-1 as int)) as standard_environment_id
                  , case
              when coalesce (request.flags, cast (0 as long)) & 32 > 0 then 'No Selection'
              when coalesce (request.advertisement_delivered_count, request.advertisement_count, cast (0 as long)) = 0 then 'Empty'
              else 'Filled'
              end as request_fill_status
                  , coalesce (request_info.slot_time_position_classes, cast (array() as array<string>)) as time_position_classes
                  , cast (array() as array<long>) as slot_ad_unit_ids
                  , coalesce (network.content_form_visibility.report_aggregate, "FULL_VISIBILITY") as content_form_visibility
                  , coalesce (request.context.standard_app_bundle_id, cast (-1 as long)) as standard_app_bundle_id
                  , coalesce (request.context.standard_site_domain_id, cast (-1 as long)) as standard_site_domain_id
                  , date_trunc('HOUR', cast (request.timestamp as timestamp)) as event_date
          from fw1_prd.hoover_pipeline_compaction.hoover_compaction
              lateral view explode(inventory.site_section_chains) as network
          where coalesce (network.role
              , "") in ("CRO"
              , "D")                -- only report for cro and d
            and not (inventory.asset_chains is not null
            and size (inventory.asset_chains)
              > 0
            and array_contains(inventory.asset_chains.network_id
              , coalesce (network.network_id
              , cast (-1 as long))))
            and not (coalesce (network.role
              , "") = "D"
            and coalesce (network.network_id
              , cast (-1 as long)) = coalesce (network.content_owner_network_id
              , cast (-1 as long))) -- remove the D when D is the same as CRO
            and cast (request.timestamp as TIMESTAMP) >= to_timestamp(event_hour, 'yyyyMMddHHmmss') - interval '4' hours
            AND event_hour >= date_format(date_trunc('hour', current_timestamp) - interval 4 hour, 'yyyyMMddHH000')
            AND event_hour < date_format(date_trunc('hour', current_timestamp) - interval 3 hour, 'yyyyMMddHH000')
            and idx.is_first_request = true

          union all
          -- no asset_chain and no site_section_chain
          select event_hour as process_batch_id
                  , coalesce (request.context.network_id, cast (-1 as long)) as network_id
                  , coalesce (request.context.video_cro_network_id, cast (-1 as long)) as content_owner_id
                  , coalesce (request.context.network_id, cast (-1 as long)) as distributor_id
                  , coalesce (request.context.tv_network_id, cast (-1 as long)) as tv_network_id
                  , "D" as transaction_type
                  , coalesce (request.traffic_type, cast (0 as long)) as traffic_type
                  , coalesce (request.bit_flags, cast (0 as long)) as bit_flag
                  , cast (-1 as long) as asset_id
                  , cast (-1 as long) as series_id
                  , cast (array() as array<long >) as asset_group_ids
                  , cast (-1 as long) as site_section_id
                  , cast (-1 as long) as site_id
                  , cast (array() as array<long >) as site_section_group_ids
                  , cast (-1 as long) as airing_id
                  , cast (-1 as long) as channel_id
                  , coalesce (visitor.platform_group, "-1") as platform_group
                  , coalesce (visitor.postal_code, "-1") as postal_code
                  , cast (array() as array< int >) as postal_code_package_ids
                  , coalesce (visitor.city_id, cast (-1 as int)) as user_city_id
                  , coalesce (visitor.state_id, cast (-1 as int)) as user_state_id
                  , coalesce (visitor.dma_code_id, cast (-1 as int)) as user_dma_code_id
                  , coalesce (cast (visitor.country_id as long), cast (-1 as long)) as user_country_id
                  , coalesce (visitor.operator_zone_id, cast (-1 as long)) as operator_zone_id
                  , "FULL_VISIBILITY" as geo_country_visibility
                  , "FULL_VISIBILITY" as geo_state_visibility
                  , "FULL_VISIBILITY" as geo_dma_visibility
                  , "FULL_VISIBILITY" as geo_city_visibility
                  , "FULL_VISIBILITY" as geo_zipcode_visibility
                  , coalesce (request.privacy_jurisdiction_ids, cast (array() as array< int >)) as privacy_jurisdiction_ids
                  , coalesce (request.privacy_choice_ids, cast (array() as array< int >)) as privacy_choice_ids
                  , cast (1 as long) * coalesce (request.multiplier, cast (1 as long)) *
              coalesce (request.magnifier, cast (1 as long)) *
              coalesce (request.log_sampling.magnifier, cast (1 as long)) as ad_requests
                  , coalesce (request.context.profile_id, cast (-1 as long)) as profile_id
                  , coalesce (request.context.profile_type, 'UNKNOWN') as profile_type
                  , coalesce (request.client_facing_ivt_reason_flag, cast (0 as long)) as client_facing_ivt_reason_flag
                  , cast (0 as long) as total_ad_requests
                  , coalesce (request.context.standard_endpoint_id, cast (-1 as int)) as standard_endpoint_id
                  , coalesce (visitor.standard_device_type_child_id, cast (-1 as int)) as standard_device_type_id
                  , "FULL_VISIBILITY" as standard_endpoint_visibility
                  , "FULL_VISIBILITY" as user_agent_visibility
                  , cast (array() as array<long>) as inventory_package_ids
                  , coalesce (visitor.standard_os_id, cast (-1 as int)) as standard_os_id
                  , coalesce (visitor.platform_browser_id, cast (-1 as long)) as delivered_platform_browser_id
                  , 'UNKNOWN' as request_chain_type
                  , coalesce (request.context.video_cro_network_id, cast (-1 as long)) as video_cro_network_id
                  , coalesce (request.context.network_id, cast (-1 as long)) as request_context_network_id
                  , if(coalesce (request.traffic_type, cast (0 as long)) != 0, true, false) as ivt_indicator
                  , if(coalesce (request.bit_flags, cast (0 as long)) & shiftleft(cast (1 as long), 9) > 0, true, false) as live_linear_indicator
                  , if(coalesce (request.bit_flags, cast (0 as long)) & shiftleft(cast (1 as long), 34) > 0, true, false) as ssp_bidder_indicator
                  , coalesce (request.context.standard_publisher_id, cast (-1 as long)) as standard_publisher_id
                  , coalesce (request.context.standard_app_id, cast (-1 as long)) as standard_app_id
                  , cast (-1 as int) as standard_brand_id
                  , "FULL_VISIBILITY" as standard_brand_visibility
                  , cast (-1 as int) as standard_programmer_id
                  , "FULL_VISIBILITY" as standard_programmer_visibility
                  , cast (-1 as int) as content_form_id
                  , coalesce (request.context.stream_mode_id, cast (-1 as int)) as stream_mode_id
                  , coalesce (request.context.standard_endpoint_owner_id, cast (-1 as int)) as standard_endpoint_owner_id
                  , "FULL_VISIBILITY" as standard_endpoint_owner_visibility
                  , coalesce (visitor.standard_environment_id, cast (-1 as int)) as standard_environment_id
                  , case
              when coalesce (request.flags, cast (0 as long)) & 32 > 0 then 'No Selection'
              when coalesce (request.advertisement_delivered_count, request.advertisement_count, cast (0 as long)) = 0 then 'Empty'
              else 'Filled'
              end as request_fill_status
                  , coalesce (request_info.slot_time_position_classes, cast (array() as array<string>)) as time_position_classes
                  , cast (array() as array<long>) as slot_ad_unit_ids
                  , "FULL_VISIBILITY" as content_form_visibility
                  , coalesce (request.context.standard_app_bundle_id, cast (-1 as long)) as standard_app_bundle_id
                  , coalesce (request.context.standard_site_domain_id, cast (-1 as long)) as standard_site_domain_id
                  , date_trunc('HOUR', cast (request.timestamp as timestamp)) as event_date
          from fw1_prd.hoover_pipeline_compaction.hoover_compaction
          where (inventory.asset_chains is null
             or size (inventory.asset_chains) = 0)
            and (inventory.site_section_chains is null
             or size (inventory.site_section_chains) = 0)
            and cast (request.timestamp as TIMESTAMP) >= to_timestamp(event_hour, 'yyyyMMddHHmmss') - interval '4' hours
            AND event_hour >= date_format(date_trunc('hour', current_timestamp) - interval 4 hour, 'yyyyMMddHH000')
            AND event_hour < date_format(date_trunc('hour', current_timestamp) - interval 3 hour, 'yyyyMMddHH000')
            and idx.is_first_request = true)
    group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
             61, 62, 63, 64, 65, 66, 67
);
```

  

##### Setup Validation Config

Now that we have the data prepared, we need to setup the configuration table.

The job reads from table: `fw1_stg.kbhargava.validation_config_new` 

However, this can be overridden as needed. 

Things needed:

- Control table name (fw1\_stg.kbhargava\_prd\_test.f\_process\_request\_hourly\_hive)
- Stage table name (fw1\_stg.kbhargava\_prd\_test.f\_process\_request\_hourly\_hoover\_plus)
- Validation table name (f\_process\_request\_hourly)
- Dimensions (comma separated)
- Metrics (comma separated)

Example:

```
insert into fw1_stg.kbhargava.validation_config_new (control_table, stage_table, validation_table_name, dimensions, metrics)
VALUES("fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive", "fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus", "f_process_request_hourly", "'network_id', 'content_owner_id', 'distributor_id', 'tv_network_id', 'transaction_type', 'traffic_type', 'bit_flag', 'asset_id', 'series_id', 'asset_group_ids', 'site_section_id', 'site_id', 'site_section_group_ids', 'airing_id', 'channel_id', 'platform_group', 'postal_code', 'postal_code_package_ids', 'user_city_id', 'user_state_id', 'user_dma_code_id', 'user_country_id', 'operator_zone_id', 'geo_country_visibility', 'geo_state_visibility', 'geo_dma_visibility', 'geo_city_visibility', 'geo_zipcode_visibility', 'privacy_jurisdiction_ids', 'privacy_choice_ids', 'profile_id', 'profile_type', 'client_facing_ivt_reason_flag', 'standard_endpoint_id', 'standard_device_type_id', 'standard_endpoint_visibility', 'user_agent_visibility', 'inventory_package_ids', 'standard_os_id', 'delivered_platform_browser_id', 'request_chain_type', 'video_cro_network_id', 'request_context_network_id', 'ivt_indicator', 'live_linear_indicator', 'ssp_bidder_indicator', 'standard_publisher_id', 'standard_app_id', 'standard_brand_id', 'standard_brand_visibility', 'standard_programmer_id', 'standard_programmer_visibility', 'content_form_id', 'stream_mode_id', 'standard_endpoint_owner_id', 'standard_endpoint_owner_visibility', 'standard_environment_id', 'request_fill_status', 'time_position_classes', 'slot_ad_unit_ids', 'content_form_visibility', 'standard_app_bundle_id', 'standard_site_domain_id', 'event_date'", "'ad_requests', 'total_ad_requests'" )
```

  

##### Setup Validation Job(s)

Job(s) are already setup.

STG: <https://freewheel-fw1-stg-e2.cloud.databricks.com/jobs/127321631350884/runs?o=310372727989026>

PRD: <https://freewheel-fw1-prd-e2.cloud.databricks.com/jobs/1026002533394894/runs?o=1013481471976618>

Add more task(s) as needed (see )

The group `hoover-team-stg`   has been given permissions to manage the job mentioned above. But you can also create your own as needed.

##### Run Validation Tool

After adding a task (or creating a new job as needed) now is the time to run the task.

Config example:

```
["--validation_config","fw1_stg.kbhargava.validation_config_new","--validation_table","f_process_request_hourly"]
```

  

  

##### View Results

The validation tool sends an email out (feel free to swap it to your email or comment out the #hoover-with-ubt channel email)


##### Further Analysis

There are probably going to be difference between current hoover and Hoover++ outputs. Next is some manual analysis (jumping off point can be the SQL attached in the email) and PRs to figure out why things don't match.

## Questions?

 

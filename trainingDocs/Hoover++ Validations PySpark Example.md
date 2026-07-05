# Hoover\+\+ Validations PySpark Example

## Pyspark Notebook

<https://freewheel-fw1-dev-e2.cloud.databricks.com/editor/notebooks/880907671281902?contextId=sql-editor&o=2929365364440953#command/5431567481884881>

```py
spark
```

```py
# Objective: This notebook file runs data comparisons between the "control" and "stage" datasets for the datasource.
#    Note that data cannot always align exactly the same, due to the minor differences in the stream dataflow.
#    That said, they should be very similar, being off by just a handful of counts
#
```

```py
#
# CONFIGURE these parameters before running the script
# 

start_date = "2025-12-19"
run_hour = "05"
```

```py
control_table = "fw1_stg.kbhargava.f_order_selected_hourly_hoover_plus"
df_control = spark.table(control_table)
```

```py
stage_table = "fw1_stg.kbhargava.f_order_selected_hourly_hoover_plus"
df_stage = spark.table(stage_table)
```

```py
df_control.createOrReplaceTempView("control_v")
df_stage.createOrReplaceTempView("stage_v")
```

```py
# Query counts and sums by date,hour
validate_query = "SELECT date(event_date) as date, date_format(event_date, \"HH\") as hour, COUNT (DISTINCT process_batch_id) as num_process_batch_id, COUNT (DISTINCT network_id) as num_network_id, COUNT (DISTINCT content_owner_id) as num_content_owner_id, COUNT (DISTINCT distributor_id) as num_distributor_id, COUNT (DISTINCT reseller_id) as num_reseller_id, COUNT (DISTINCT tv_network_id) as num_tv_network_id, COUNT (DISTINCT transaction_type) as num_transaction_type, COUNT (DISTINCT traffic_type) as num_traffic_type, COUNT (DISTINCT bit_flag) as num_bit_flag, COUNT (DISTINCT asset_id) as num_asset_id, COUNT (DISTINCT series_id) as num_series_id, COUNT (DISTINCT asset_group_ids) as num_asset_group_ids, COUNT (DISTINCT site_section_id) as num_site_section_id, COUNT (DISTINCT site_id) as num_site_id, COUNT (DISTINCT site_section_group_ids) as num_site_section_group_ids, COUNT (DISTINCT airing_id) as num_airing_id, COUNT (DISTINCT channel_id) as num_channel_id, COUNT (DISTINCT break_id) as num_break_id, COUNT (DISTINCT time_position_class) as num_time_position_class, COUNT (DISTINCT inbound_mrm_rule_id) as num_inbound_mrm_rule_id, COUNT (DISTINCT mrm_rule_id) as num_mrm_rule_id, COUNT (DISTINCT campaign_id) as num_campaign_id, COUNT (DISTINCT io_id) as num_io_id, COUNT (DISTINCT placement_id) as num_placement_id, COUNT (DISTINCT ad_id) as num_ad_id, COUNT (DISTINCT creative_id) as num_creative_id, COUNT (DISTINCT delivery_method) as num_delivery_method, COUNT (DISTINCT targeting_criteria_id) as num_targeting_criteria_id, COUNT (DISTINCT ad_unit_id) as num_ad_unit_id, COUNT (DISTINCT matched_audience_item_ids) as num_matched_audience_item_ids, COUNT (DISTINCT matched_keyvalue_item_ids) as num_matched_keyvalue_item_ids, COUNT (DISTINCT matched_daypart) as num_matched_daypart, COUNT (DISTINCT placement_type_priority) as num_placement_type_priority, COUNT (DISTINCT platform_group) as num_platform_group, COUNT (DISTINCT geo_visibility) as num_geo_visibility, COUNT (DISTINCT user_agent_visibility) as num_user_agent_visibility, COUNT (DISTINCT postal_code) as num_postal_code, COUNT (DISTINCT postal_code_package_ids) as num_postal_code_package_ids, COUNT (DISTINCT user_city_id) as num_user_city_id, COUNT (DISTINCT user_state_id) as num_user_state_id, COUNT (DISTINCT user_dma_code) as num_user_dma_code, COUNT (DISTINCT user_country_id) as num_user_country_id, COUNT (DISTINCT delivered_platform_browser_id) as num_delivered_platform_browser_id, COUNT (DISTINCT delivered_platform_device_id) as num_delivered_platform_device_id, COUNT (DISTINCT delivered_platform_os_id) as num_delivered_platform_os_id, COUNT (DISTINCT operator_zone_id) as num_operator_zone_id, COUNT (DISTINCT integration_delivery_method) as num_integration_delivery_method, COUNT (DISTINCT scenario_id) as num_scenario_id, COUNT (DISTINCT audience_extension_deal_id) as num_audience_extension_deal_id, COUNT (DISTINCT tracked_audience_item_ids) as num_tracked_audience_item_ids, COUNT (DISTINCT geo_state_visibility) as num_geo_state_visibility, COUNT (DISTINCT geo_dma_visibility) as num_geo_dma_visibility, COUNT (DISTINCT geo_city_visibility) as num_geo_city_visibility, COUNT (DISTINCT geo_zipcode_visibility) as num_geo_zipcode_visibility, COUNT (DISTINCT key_value_visibility) as num_key_value_visibility, COUNT (DISTINCT slot_avail_type) as num_slot_avail_type, COUNT (DISTINCT linear_decision_type) as num_linear_decision_type, COUNT (DISTINCT standard_device_type_ids) as num_standard_device_type_ids, COUNT (DISTINCT standard_environment_id) as num_standard_environment_id, COUNT (DISTINCT standard_os_id) as num_standard_os_id, COUNT (DISTINCT standard_brand_id) as num_standard_brand_id, COUNT (DISTINCT standard_channel_id) as num_standard_channel_id, COUNT (DISTINCT standard_genre_ids) as num_standard_genre_ids, COUNT (DISTINCT content_form_id) as num_content_form_id, COUNT (DISTINCT content_rating_id) as num_content_rating_id, COUNT (DISTINCT standard_language_ids) as num_standard_language_ids, COUNT (DISTINCT stream_mode_id) as num_stream_mode_id, COUNT (DISTINCT inventory_location_id) as num_inventory_location_id, COUNT (DISTINCT mrm_rule_type_priority) as num_mrm_rule_type_priority, COUNT (DISTINCT listing_ids) as num_listing_ids, COUNT (DISTINCT inbound_order_id) as num_inbound_order_id, COUNT (DISTINCT inbound_listing_ids) as num_inbound_listing_ids, COUNT (DISTINCT outbound_order_id) as num_outbound_order_id, COUNT (DISTINCT outbound_listing_ids) as num_outbound_listing_ids, SUM (selected_primary_ads) as selected_primary_ads_sum, SUM (selected_fallback_ads) as selected_fallback_ads_sum, COUNT (DISTINCT selected_margin) as num_selected_margin, COUNT (DISTINCT selected_bidding_revenue) as num_selected_bidding_revenue, COUNT (DISTINCT co_selected_bidding_revenue) as num_co_selected_bidding_revenue, COUNT (DISTINCT d_selected_bidding_revenue) as num_d_selected_bidding_revenue, COUNT (DISTINCT r_selected_bidding_revenue) as num_r_selected_bidding_revenue, COUNT (DISTINCT selected_fallback_margin) as num_selected_fallback_margin, COUNT (DISTINCT selected_fallback_bidding_revenue) as num_selected_fallback_bidding_revenue, COUNT (DISTINCT co_selected_fallback_bidding_revenue) as num_co_selected_fallback_bidding_revenue, COUNT (DISTINCT d_selected_fallback_bidding_revenue) as num_d_selected_fallback_bidding_revenue, COUNT (DISTINCT r_selected_fallback_bidding_revenue) as num_r_selected_fallback_bidding_revenue, COUNT (DISTINCT ip_enabled_audience_id) as num_ip_enabled_audience_id, COUNT (DISTINCT standard_programmer_id) as num_standard_programmer_id, COUNT (DISTINCT geo_country_visibility) as num_geo_country_visibility, COUNT (DISTINCT standard_brand_visibility) as num_standard_brand_visibility, COUNT (DISTINCT standard_genre_visibility) as num_standard_genre_visibility, COUNT (DISTINCT content_rating_visibility) as num_content_rating_visibility, COUNT (DISTINCT standard_endpoint_owner_id) as num_standard_endpoint_owner_id, COUNT (DISTINCT standard_endpoint_id) as num_standard_endpoint_id, COUNT (DISTINCT outbound_exchange_order_id) as num_outbound_exchange_order_id, COUNT (DISTINCT deal_id) as num_deal_id, COUNT (DISTINCT buyer_group_id) as num_buyer_group_id, COUNT (DISTINCT dsp_id) as num_dsp_id, COUNT (DISTINCT programmatic_advertiser_id) as num_programmatic_advertiser_id, COUNT (DISTINCT supply_source) as num_supply_source, COUNT (DISTINCT sales_channel) as num_sales_channel, COUNT (DISTINCT standard_endpoint_owner_visibility) as num_standard_endpoint_owner_visibility, COUNT (DISTINCT standard_endpoint_visibility) as num_standard_endpoint_visibility, COUNT (DISTINCT inbound_order_auction_type) as num_inbound_order_auction_type, SUM (ssp_bids) as ssp_bids_sum, SUM (ssp_co_bidding_revenue) as ssp_co_bidding_revenue_sum, COUNT (DISTINCT standard_content_daypart_id) as num_standard_content_daypart_id, COUNT (DISTINCT ssp_external_publisher_id) as num_ssp_external_publisher_id, COUNT (DISTINCT global_advertiser_ids) as num_global_advertiser_ids, COUNT (DISTINCT global_brand_ids) as num_global_brand_ids, COUNT (DISTINCT market_ad_id) as num_market_ad_id, COUNT (DISTINCT trading_desk_id) as num_trading_desk_id, COUNT (DISTINCT user_dma_code_id) as num_user_dma_code_id, COUNT (DISTINCT global_industry_ids) as num_global_industry_ids, COUNT (DISTINCT buyer_platform_id) as num_buyer_platform_id, COUNT (DISTINCT standard_programmer_visibility) as num_standard_programmer_visibility, COUNT (DISTINCT bidding_seat_id) as num_bidding_seat_id, COUNT (DISTINCT rendition_id) as num_rendition_id, COUNT (DISTINCT bidding_buyer_id) as num_bidding_buyer_id, COUNT (DISTINCT global_agency_ids) as num_global_agency_ids, COUNT (DISTINCT standard_publisher_id) as num_standard_publisher_id, COUNT (DISTINCT bidder_seat_id) as num_bidder_seat_id, COUNT (DISTINCT application_type) as num_application_type, COUNT (DISTINCT app_bundle) as num_app_bundle, COUNT (DISTINCT site_domain) as num_site_domain, COUNT (DISTINCT global_currency_version) as num_global_currency_version, COUNT (DISTINCT global_currency_id) as num_global_currency_id, COUNT (DISTINCT standard_app_id) as num_standard_app_id, COUNT (DISTINCT profile_id) as num_profile_id, COUNT (DISTINCT profile_type) as num_profile_type, COUNT (DISTINCT standard_content_series_id) as num_standard_content_series_id, COUNT (DISTINCT standard_content_subscription_model_id) as num_standard_content_subscription_model_id, COUNT (DISTINCT standard_ssp_channel_id) as num_standard_ssp_channel_id, COUNT (DISTINCT standard_site_domain_id) as num_standard_site_domain_id, COUNT (DISTINCT matched_inventory_package_ids) as num_matched_inventory_package_ids, COUNT (DISTINCT dsp_currency_id) as num_dsp_currency_id, COUNT (DISTINCT standard_operator_id) as num_standard_operator_id, COUNT (DISTINCT standard_iab_category_ids) as num_standard_iab_category_ids, COUNT (DISTINCT upstream_inbound_order_id) as num_upstream_inbound_order_id, COUNT (DISTINCT upstream_global_currency_id) as num_upstream_global_currency_id, COUNT (DISTINCT standard_content_territory_id) as num_standard_content_territory_id, COUNT (DISTINCT standard_content_series_visibility) as num_standard_content_series_visibility, COUNT (DISTINCT standard_content_credential_status_id) as num_standard_content_credential_status_id, COUNT (DISTINCT external_seat_id) as num_external_seat_id, COUNT (DISTINCT matched_contextual_segment_ids) as num_matched_contextual_segment_ids, COUNT (DISTINCT inventory_package_ids) as num_inventory_package_ids, COUNT (DISTINCT selected_yield_optimization_ids) as num_selected_yield_optimization_ids, COUNT (DISTINCT outbound_publisher_id) as num_outbound_publisher_id, COUNT (DISTINCT standard_retailer_id) as num_standard_retailer_id, COUNT (DISTINCT standard_content_subscription_model_visibility) as num_standard_content_subscription_model_visibility, COUNT (DISTINCT standard_manufacturer_id) as num_standard_manufacturer_id, COUNT (DISTINCT standard_app_bundle_id) as num_standard_app_bundle_id, COUNT (DISTINCT content_owner_visibility) as num_content_owner_visibility, COUNT (DISTINCT reseller_visibility) as num_reseller_visibility, COUNT (DISTINCT slot_user_drop_off) as num_slot_user_drop_off, COUNT (DISTINCT sales_strategy) as num_sales_strategy, COUNT (DISTINCT ivt_indicator) as num_ivt_indicator, COUNT (DISTINCT request_fill_status) as num_request_fill_status, COUNT (DISTINCT slot_fill_status) as num_slot_fill_status, COUNT (DISTINCT slot_sequence_normalized) as num_slot_sequence_normalized, COUNT (DISTINCT slot_ad_unit_id) as num_slot_ad_unit_id, COUNT (DISTINCT slot_removed_by_ux_indicator) as num_slot_removed_by_ux_indicator, COUNT (DISTINCT live_linear_indicator) as num_live_linear_indicator, COUNT (DISTINCT ssp_bidder_indicator) as num_ssp_bidder_indicator, COUNT (DISTINCT ssp_bidder_buyer_indicator) as num_ssp_bidder_buyer_indicator, COUNT (DISTINCT partner_tag_indicator) as num_partner_tag_indicator, COUNT (DISTINCT promo_ad_indicator) as num_promo_ad_indicator, COUNT (DISTINCT evergreen_ad_indicator) as num_evergreen_ad_indicator, COUNT (DISTINCT primary_ad_indicator) as num_primary_ad_indicator, COUNT (DISTINCT ad_with_fallback_indicator) as num_ad_with_fallback_indicator, COUNT (DISTINCT priority_tier) as num_priority_tier, COUNT (DISTINCT priority_type) as num_priority_type, COUNT (DISTINCT priority_value) as num_priority_value, COUNT (DISTINCT local_advertiser_id) as num_local_advertiser_id, COUNT (DISTINCT failed_ad_error_code) as num_failed_ad_error_code, SUM (placed_ads_in_played_slot) as placed_ads_in_played_slot_sum, SUM (placed_ads_has_fallback_in_played_slot) as placed_ads_has_fallback_in_played_slot_sum, SUM (placed_fallback_ads_in_played_slot) as placed_fallback_ads_in_played_slot_sum, SUM (filled_ads_in_played_slot) as filled_ads_in_played_slot_sum, SUM (filled_ads_duration_in_played_slot) as filled_ads_duration_in_played_slot_sum, SUM (filled_ads_sstf_fallback_in_played_slot) as filled_ads_sstf_fallback_in_played_slot_sum, SUM (failed_ads_in_played_slot) as failed_ads_in_played_slot_sum, SUM (selected_ads_in_played_slot) as selected_ads_in_played_slot_sum, SUM (selected_ads_in_played_slot_primary) as selected_ads_in_played_slot_primary_sum, SUM (selected_ads_in_played_slot_fallback) as selected_ads_in_played_slot_fallback_sum, COUNT (DISTINCT placed_ads_in_all_slot) as num_placed_ads_in_all_slot, COUNT (DISTINCT placed_ads_has_fallback_in_all_slot) as num_placed_ads_has_fallback_in_all_slot, COUNT (DISTINCT placed_fallback_ads_in_all_slot) as num_placed_fallback_ads_in_all_slot, COUNT (DISTINCT filled_ads_in_all_slot) as num_filled_ads_in_all_slot, COUNT (DISTINCT filled_ads_duration_in_all_slot) as num_filled_ads_duration_in_all_slot, COUNT (DISTINCT filled_ads_sstf_fallback_in_all_slot) as num_filled_ads_sstf_fallback_in_all_slot, COUNT (DISTINCT failed_ads_in_all_slot) as num_failed_ads_in_all_slot, COUNT (DISTINCT selected_ads_in_all_slot) as num_selected_ads_in_all_slot, COUNT (DISTINCT selected_ads_in_all_slot_primary) as num_selected_ads_in_all_slot_primary, COUNT (DISTINCT selected_ads_in_all_slot_fallback) as num_selected_ads_in_all_slot_fallback, COUNT (DISTINCT decision_type) as num_decision_type, COUNT (DISTINCT linear_avail_type) as num_linear_avail_type, COUNT (DISTINCT station_id) as num_station_id, COUNT (DISTINCT ad_in_passback_indicator) as num_ad_in_passback_indicator, COUNT (DISTINCT loop_indicator) as num_loop_indicator, COUNT (DISTINCT programmatic_device_type) as num_programmatic_device_type, COUNT (DISTINCT standard_device_type_id) as num_standard_device_type_id, SUM (outbound_bids_in_played_slot) as outbound_bids_in_played_slot_sum, SUM (outbound_bidding_revenue_in_played_slot) as outbound_bidding_revenue_in_played_slot_sum, COUNT (DISTINCT selected_yield_optimization_info_ids) as num_selected_yield_optimization_info_ids, COUNT (DISTINCT standard_channel_visibility) as num_standard_channel_visibility, COUNT (DISTINCT content_form_visibility) as num_content_form_visibility, COUNT (DISTINCT bit_flag_aim_product_category) as num_bit_flag_aim_product_category, COUNT (DISTINCT media_buyer_id) as num_media_buyer_id, COUNT (DISTINCT post_auction_discount_id) as num_post_auction_discount_id, COUNT (DISTINCT selected_yo_volume_cap_ids) as num_selected_yo_volume_cap_ids, COUNT (DISTINCT selected_yo_distribution_id) as num_selected_yo_distribution_id, COUNT (DISTINCT selected_yo_distribution_nip_id) as num_selected_yo_distribution_nip_id, COUNT (DISTINCT selected_yo_inventory_prioritization_id) as num_selected_yo_inventory_prioritization_id, COUNT (DISTINCT selected_yo_inventory_prioritization_nip_id) as num_selected_yo_inventory_prioritization_nip_id, COUNT (DISTINCT selected_yo_margin_id) as num_selected_yo_margin_id, COUNT (DISTINCT integration_type) as num_integration_type, COUNT (DISTINCT standard_content_viewership_profile_ids) as num_standard_content_viewership_profile_ids, COUNT (DISTINCT standard_privacy_id) as num_standard_privacy_id, COUNT (DISTINCT standard_addressability_ids) as num_standard_addressability_ids, COUNT (DISTINCT standard_sport_entity_ids) as num_standard_sport_entity_ids, COUNT (DISTINCT upstream_bidding_revenue_in_played_slot) as num_upstream_bidding_revenue_in_played_slot, COUNT (DISTINCT event_date) as num_event_date FROM VIEW_TABLE WHERE date(event_date) = CAST('START_DATE' AS DATE) AND date_format(event_date, \"HH\") = RUN_HOUR GROUP BY 1, 2 ORDER BY 1, 2"


control_query = validate_query.replace("VIEW_TABLE","control_v",1).replace("START_DATE", start_date).replace("RUN_HOUR",run_hour)
stage_query = validate_query.replace("VIEW_TABLE","stage_v",1).replace("START_DATE",start_date).replace("RUN_HOUR","06")
control_agg=spark.sql(control_query)
stage_agg=spark.sql(stage_query)
```

```py
# Verify the data results are non-empty before running comparisons
proceed = 1
if (df_control is None or df_control.isEmpty()): 
        proceed = 0
        print("Empty control data. Stopping here.")
elif ( df_stage is None or df_stage.isEmpty() ):
        proceed = 0
        print("Empty stage data. Stopping here.")
else:
        print("Found some aggregated data results.")
```

```py
# Compare control and stage dataframes by subtraction; this would yield an empty dataframe if they are identical
is_match = 0
if proceed == 1:
    # Add row_id and row_hash to each row
    control_hashed_with_id = control_agg.withColumn("row_id", f.monotonically_increasing_id()) \
                                        .withColumn("row_hash", f.xxhash64(*control_agg.columns))
    stage_hashed_with_id = stage_agg.withColumn("row_id", f.monotonically_increasing_id()) \
                                    .withColumn("row_hash", f.xxhash64(*stage_agg.columns))

    # Compare using exceptAll on row_hash
    diff_control_hashes = control_hashed_with_id.select("row_hash").exceptAll(stage_hashed_with_id.select("row_hash"))
    diff_stage_hashes = stage_hashed_with_id.select("row_hash").exceptAll(control_hashed_with_id.select("row_hash"))

    # Check if there are any differences
    if diff_control_hashes.isEmpty() and diff_stage_hashes.isEmpty():
        is_match = 1
        print("OK! Data matched.")
    else:
        is_match = 0
        print("UH-OH. Data did not match. Further diagnostics below...")
```

```py
#
# extra checks ...

#control_agg.show()
#stage_agg.show()
```

```py
# FIRST LAYER CHECK

### Determine which fields were different between control and stage aggregated data
run = 0
if is_match == 0:
    run = 1 

#   Build views of the aggregated data to run comparisons 
if run > 0:
    control_agg.createOrReplaceTempView("control_agg_v")
    stage_agg.createOrReplaceTempView("stage_agg_v")
else:
    print("Skipping since data matched.")

#   Determine the delta for each field
if run > 0:
    query_cmp = "SELECT (s.num_process_batch_id - c.num_process_batch_id) as diff_num_process_batch_id, (s.num_network_id - c.num_network_id) as diff_num_network_id, (s.num_content_owner_id - c.num_content_owner_id) as diff_num_content_owner_id, (s.num_distributor_id - c.num_distributor_id) as diff_num_distributor_id, (s.num_reseller_id - c.num_reseller_id) as diff_num_reseller_id, (s.num_tv_network_id - c.num_tv_network_id) as diff_num_tv_network_id, (s.num_transaction_type - c.num_transaction_type) as diff_num_transaction_type, (s.num_traffic_type - c.num_traffic_type) as diff_num_traffic_type, (s.num_bit_flag - c.num_bit_flag) as diff_num_bit_flag, (s.num_asset_id - c.num_asset_id) as diff_num_asset_id, (s.num_series_id - c.num_series_id) as diff_num_series_id, (s.num_asset_group_ids - c.num_asset_group_ids) as diff_num_asset_group_ids, (s.num_site_section_id - c.num_site_section_id) as diff_num_site_section_id, (s.num_site_id - c.num_site_id) as diff_num_site_id, (s.num_site_section_group_ids - c.num_site_section_group_ids) as diff_num_site_section_group_ids, (s.num_airing_id - c.num_airing_id) as diff_num_airing_id, (s.num_channel_id - c.num_channel_id) as diff_num_channel_id, (s.num_break_id - c.num_break_id) as diff_num_break_id, (s.num_time_position_class - c.num_time_position_class) as diff_num_time_position_class, (s.num_inbound_mrm_rule_id - c.num_inbound_mrm_rule_id) as diff_num_inbound_mrm_rule_id, (s.num_mrm_rule_id - c.num_mrm_rule_id) as diff_num_mrm_rule_id, (s.num_campaign_id - c.num_campaign_id) as diff_num_campaign_id, (s.num_io_id - c.num_io_id) as diff_num_io_id, (s.num_placement_id - c.num_placement_id) as diff_num_placement_id, (s.num_ad_id - c.num_ad_id) as diff_num_ad_id, (s.num_creative_id - c.num_creative_id) as diff_num_creative_id, (s.num_delivery_method - c.num_delivery_method) as diff_num_delivery_method, (s.num_targeting_criteria_id - c.num_targeting_criteria_id) as diff_num_targeting_criteria_id, (s.num_ad_unit_id - c.num_ad_unit_id) as diff_num_ad_unit_id, (s.num_matched_audience_item_ids - c.num_matched_audience_item_ids) as diff_num_matched_audience_item_ids, (s.num_matched_keyvalue_item_ids - c.num_matched_keyvalue_item_ids) as diff_num_matched_keyvalue_item_ids, (s.num_matched_daypart - c.num_matched_daypart) as diff_num_matched_daypart, (s.num_placement_type_priority - c.num_placement_type_priority) as diff_num_placement_type_priority, (s.num_platform_group - c.num_platform_group) as diff_num_platform_group, (s.num_geo_visibility - c.num_geo_visibility) as diff_num_geo_visibility, (s.num_user_agent_visibility - c.num_user_agent_visibility) as diff_num_user_agent_visibility, (s.num_postal_code - c.num_postal_code) as diff_num_postal_code, (s.num_postal_code_package_ids - c.num_postal_code_package_ids) as diff_num_postal_code_package_ids, (s.num_user_city_id - c.num_user_city_id) as diff_num_user_city_id, (s.num_user_state_id - c.num_user_state_id) as diff_num_user_state_id, (s.num_user_dma_code - c.num_user_dma_code) as diff_num_user_dma_code, (s.num_user_country_id - c.num_user_country_id) as diff_num_user_country_id, (s.num_delivered_platform_browser_id - c.num_delivered_platform_browser_id) as diff_num_delivered_platform_browser_id, (s.num_delivered_platform_device_id - c.num_delivered_platform_device_id) as diff_num_delivered_platform_device_id, (s.num_delivered_platform_os_id - c.num_delivered_platform_os_id) as diff_num_delivered_platform_os_id, (s.num_operator_zone_id - c.num_operator_zone_id) as diff_num_operator_zone_id, (s.num_integration_delivery_method - c.num_integration_delivery_method) as diff_num_integration_delivery_method, (s.num_scenario_id - c.num_scenario_id) as diff_num_scenario_id, (s.num_audience_extension_deal_id - c.num_audience_extension_deal_id) as diff_num_audience_extension_deal_id, (s.num_tracked_audience_item_ids - c.num_tracked_audience_item_ids) as diff_num_tracked_audience_item_ids, (s.num_geo_state_visibility - c.num_geo_state_visibility) as diff_num_geo_state_visibility, (s.num_geo_dma_visibility - c.num_geo_dma_visibility) as diff_num_geo_dma_visibility, (s.num_geo_city_visibility - c.num_geo_city_visibility) as diff_num_geo_city_visibility, (s.num_geo_zipcode_visibility - c.num_geo_zipcode_visibility) as diff_num_geo_zipcode_visibility, (s.num_key_value_visibility - c.num_key_value_visibility) as diff_num_key_value_visibility, (s.num_slot_avail_type - c.num_slot_avail_type) as diff_num_slot_avail_type, (s.num_linear_decision_type - c.num_linear_decision_type) as diff_num_linear_decision_type, (s.num_standard_device_type_ids - c.num_standard_device_type_ids) as diff_num_standard_device_type_ids, (s.num_standard_environment_id - c.num_standard_environment_id) as diff_num_standard_environment_id, (s.num_standard_os_id - c.num_standard_os_id) as diff_num_standard_os_id, (s.num_standard_brand_id - c.num_standard_brand_id)as diff_num_standard_brand_id, (s.num_standard_channel_id - c.num_standard_channel_id) as diff_num_standard_channel_id, (s.num_standard_genre_ids - c.num_standard_genre_ids) as diff_num_standard_genre_ids, (s.num_content_form_id - c.num_content_form_id) as diff_num_content_form_id, (s.num_content_rating_id - c.num_content_rating_id)as diff_num_content_rating_id, (s.num_standard_language_ids - c.num_standard_language_ids) as diff_num_standard_language_ids, (s.num_stream_mode_id - c.num_stream_mode_id) as diff_num_stream_mode_id, (s.num_inventory_location_id - c.num_inventory_location_id) as diff_num_inventory_location_id, (s.num_mrm_rule_type_priority - c.num_mrm_rule_type_priority) as diff_num_mrm_rule_type_priority, (s.num_listing_ids - c.num_listing_ids) as diff_num_listing_ids, (s.num_inbound_order_id - c.num_inbound_order_id) as diff_num_inbound_order_id, (s.num_inbound_listing_ids - c.num_inbound_listing_ids) as diff_num_inbound_listing_ids, (s.num_outbound_order_id - c.num_outbound_order_id)as diff_num_outbound_order_id, (s.num_outbound_listing_ids - c.num_outbound_listing_ids) as diff_num_outbound_listing_ids, (s.selected_primary_ads_sum - c.selected_primary_ads_sum) as diff_selected_primary_ads_sum, (s.selected_fallback_ads_sum - c.selected_fallback_ads_sum) as diff_selected_fallback_ads_sum, (s.num_selected_margin - c.num_selected_margin) as diff_num_selected_margin, (s.num_selected_bidding_revenue - c.num_selected_bidding_revenue) as diff_num_selected_bidding_revenue, (s.num_co_selected_bidding_revenue - c.num_co_selected_bidding_revenue) as diff_num_co_selected_bidding_revenue, (s.num_d_selected_bidding_revenue - c.num_d_selected_bidding_revenue) as diff_num_d_selected_bidding_revenue, (s.num_r_selected_bidding_revenue - c.num_r_selected_bidding_revenue) as diff_num_r_selected_bidding_revenue, (s.num_selected_fallback_margin - c.num_selected_fallback_margin) as diff_num_selected_fallback_margin, (s.num_selected_fallback_bidding_revenue - c.num_selected_fallback_bidding_revenue) as diff_num_selected_fallback_bidding_revenue, (s.num_co_selected_fallback_bidding_revenue - c.num_co_selected_fallback_bidding_revenue) as diff_num_co_selected_fallback_bidding_revenue, (s.num_d_selected_fallback_bidding_revenue - c.num_d_selected_fallback_bidding_revenue) as diff_num_d_selected_fallback_bidding_revenue, (s.num_r_selected_fallback_bidding_revenue - c.num_r_selected_fallback_bidding_revenue) as diff_num_r_selected_fallback_bidding_revenue, (s.num_ip_enabled_audience_id - c.num_ip_enabled_audience_id) as diff_num_ip_enabled_audience_id, (s.num_standard_programmer_id - c.num_standard_programmer_id) as diff_num_standard_programmer_id, (s.num_geo_country_visibility - c.num_geo_country_visibility) as diff_num_geo_country_visibility, (s.num_standard_brand_visibility - c.num_standard_brand_visibility) as diff_num_standard_brand_visibility, (s.num_standard_genre_visibility - c.num_standard_genre_visibility) as diff_num_standard_genre_visibility, (s.num_content_rating_visibility - c.num_content_rating_visibility) as diff_num_content_rating_visibility, (s.num_standard_endpoint_owner_id - c.num_standard_endpoint_owner_id) as diff_num_standard_endpoint_owner_id, (s.num_standard_endpoint_id - c.num_standard_endpoint_id) as diff_num_standard_endpoint_id, (s.num_outbound_exchange_order_id - c.num_outbound_exchange_order_id) as diff_num_outbound_exchange_order_id, (s.num_deal_id - c.num_deal_id) as diff_num_deal_id, (s.num_buyer_group_id - c.num_buyer_group_id) as diff_num_buyer_group_id, (s.num_dsp_id - c.num_dsp_id) as diff_num_dsp_id, (s.num_programmatic_advertiser_id - c.num_programmatic_advertiser_id) as diff_num_programmatic_advertiser_id, (s.num_supply_source - c.num_supply_source) as diff_num_supply_source, (s.num_sales_channel - c.num_sales_channel) as diff_num_sales_channel, (s.num_standard_endpoint_owner_visibility - c.num_standard_endpoint_owner_visibility) as diff_num_standard_endpoint_owner_visibility, (s.num_standard_endpoint_visibility - c.num_standard_endpoint_visibility) as diff_num_standard_endpoint_visibility, (s.num_inbound_order_auction_type - c.num_inbound_order_auction_type) as diff_num_inbound_order_auction_type, (s.ssp_bids_sum - c.ssp_bids_sum) as diff_ssp_bids_sum, (s.ssp_co_bidding_revenue_sum - c.ssp_co_bidding_revenue_sum) as diff_ssp_co_bidding_revenue_sum, (s.num_standard_content_daypart_id - c.num_standard_content_daypart_id) as diff_num_standard_content_daypart_id, (s.num_ssp_external_publisher_id - c.num_ssp_external_publisher_id) as diff_num_ssp_external_publisher_id, (s.num_global_advertiser_ids - c.num_global_advertiser_ids) as diff_num_global_advertiser_ids, (s.num_global_brand_ids - c.num_global_brand_ids) as diff_num_global_brand_ids, (s.num_market_ad_id - c.num_market_ad_id) as diff_num_market_ad_id, (s.num_trading_desk_id - c.num_trading_desk_id) as diff_num_trading_desk_id, (s.num_user_dma_code_id - c.num_user_dma_code_id) as diff_num_user_dma_code_id, (s.num_global_industry_ids - c.num_global_industry_ids) as diff_num_global_industry_ids, (s.num_buyer_platform_id - c.num_buyer_platform_id)as diff_num_buyer_platform_id, (s.num_standard_programmer_visibility - c.num_standard_programmer_visibility) as diff_num_standard_programmer_visibility, (s.num_bidding_seat_id - c.num_bidding_seat_id) as diff_num_bidding_seat_id, (s.num_rendition_id - c.num_rendition_id) as diff_num_rendition_id, (s.num_bidding_buyer_id - c.num_bidding_buyer_id) as diff_num_bidding_buyer_id, (s.num_global_agency_ids - c.num_global_agency_ids)as diff_num_global_agency_ids, (s.num_standard_publisher_id - c.num_standard_publisher_id) as diff_num_standard_publisher_id, (s.num_bidder_seat_id - c.num_bidder_seat_id) as diff_num_bidder_seat_id, (s.num_application_type - c.num_application_type) as diff_num_application_type, (s.num_app_bundle - c.num_app_bundle) as diff_num_app_bundle, (s.num_site_domain - c.num_site_domain) as diff_num_site_domain, (s.num_global_currency_version - c.num_global_currency_version) as diff_num_global_currency_version, (s.num_global_currency_id - c.num_global_currency_id) as diff_num_global_currency_id, (s.num_standard_app_id - c.num_standard_app_id) as diff_num_standard_app_id, (s.num_profile_id - c.num_profile_id) as diff_num_profile_id, (s.num_profile_type - c.num_profile_type) as diff_num_profile_type, (s.num_standard_content_series_id - c.num_standard_content_series_id) as diff_num_standard_content_series_id, (s.num_standard_content_subscription_model_id - c.num_standard_content_subscription_model_id) as diff_num_standard_content_subscription_model_id, (s.num_standard_ssp_channel_id - c.num_standard_ssp_channel_id) as diff_num_standard_ssp_channel_id, (s.num_standard_site_domain_id - c.num_standard_site_domain_id) as diff_num_standard_site_domain_id, (s.num_matched_inventory_package_ids - c.num_matched_inventory_package_ids) as diff_num_matched_inventory_package_ids, (s.num_dsp_currency_id - c.num_dsp_currency_id) as diff_num_dsp_currency_id, (s.num_standard_operator_id - c.num_standard_operator_id) as diff_num_standard_operator_id, (s.num_standard_iab_category_ids - c.num_standard_iab_category_ids) as diff_num_standard_iab_category_ids, (s.num_upstream_inbound_order_id - c.num_upstream_inbound_order_id) as diff_num_upstream_inbound_order_id, (s.num_upstream_global_currency_id - c.num_upstream_global_currency_id) as diff_num_upstream_global_currency_id, (s.num_standard_content_territory_id - c.num_standard_content_territory_id) as diff_num_standard_content_territory_id, (s.num_standard_content_series_visibility - c.num_standard_content_series_visibility) as diff_num_standard_content_series_visibility, (s.num_standard_content_credential_status_id - c.num_standard_content_credential_status_id) as diff_num_standard_content_credential_status_id, (s.num_external_seat_id - c.num_external_seat_id) as diff_num_external_seat_id, (s.num_matched_contextual_segment_ids - c.num_matched_contextual_segment_ids) as diff_num_matched_contextual_segment_ids, (s.num_inventory_package_ids - c.num_inventory_package_ids) as diff_num_inventory_package_ids, (s.num_selected_yield_optimization_ids - c.num_selected_yield_optimization_ids) as diff_num_selected_yield_optimization_ids, (s.num_outbound_publisher_id - c.num_outbound_publisher_id) as diff_num_outbound_publisher_id, (s.num_standard_retailer_id - c.num_standard_retailer_id) as diff_num_standard_retailer_id, (s.num_standard_content_subscription_model_visibility - c.num_standard_content_subscription_model_visibility) as diff_num_standard_content_subscription_model_visibility, (s.num_standard_manufacturer_id - c.num_standard_manufacturer_id) as diff_num_standard_manufacturer_id, (s.num_standard_app_bundle_id - c.num_standard_app_bundle_id) as diff_num_standard_app_bundle_id, (s.num_content_owner_visibility - c.num_content_owner_visibility) as diff_num_content_owner_visibility, (s.num_reseller_visibility - c.num_reseller_visibility) as diff_num_reseller_visibility, (s.num_slot_user_drop_off - c.num_slot_user_drop_off) as diff_num_slot_user_drop_off, (s.num_sales_strategy - c.num_sales_strategy) as diff_num_sales_strategy, (s.num_ivt_indicator - c.num_ivt_indicator) as diff_num_ivt_indicator, (s.num_request_fill_status - c.num_request_fill_status) as diff_num_request_fill_status, (s.num_slot_fill_status - c.num_slot_fill_status) as diff_num_slot_fill_status, (s.num_slot_sequence_normalized - c.num_slot_sequence_normalized) as diff_num_slot_sequence_normalized, (s.num_slot_ad_unit_id - c.num_slot_ad_unit_id) as diff_num_slot_ad_unit_id, (s.num_slot_removed_by_ux_indicator - c.num_slot_removed_by_ux_indicator) as diff_num_slot_removed_by_ux_indicator, (s.num_live_linear_indicator - c.num_live_linear_indicator) as diff_num_live_linear_indicator, (s.num_ssp_bidder_indicator - c.num_ssp_bidder_indicator) as diff_num_ssp_bidder_indicator, (s.num_ssp_bidder_buyer_indicator - c.num_ssp_bidder_buyer_indicator) as diff_num_ssp_bidder_buyer_indicator, (s.num_partner_tag_indicator - c.num_partner_tag_indicator) as diff_num_partner_tag_indicator, (s.num_promo_ad_indicator - c.num_promo_ad_indicator) as diff_num_promo_ad_indicator, (s.num_evergreen_ad_indicator - c.num_evergreen_ad_indicator) as diff_num_evergreen_ad_indicator, (s.num_primary_ad_indicator - c.num_primary_ad_indicator) as diff_num_primary_ad_indicator, (s.num_ad_with_fallback_indicator - c.num_ad_with_fallback_indicator) as diff_num_ad_with_fallback_indicator, (s.num_priority_tier - c.num_priority_tier) as diff_num_priority_tier, (s.num_priority_type - c.num_priority_type) as diff_num_priority_type, (s.num_priority_value - c.num_priority_value) as diff_num_priority_value, (s.num_local_advertiser_id - c.num_local_advertiser_id) as diff_num_local_advertiser_id, (s.num_failed_ad_error_code - c.num_failed_ad_error_code) as diff_num_failed_ad_error_code, (s.placed_ads_in_played_slot_sum - c.placed_ads_in_played_slot_sum) as diff_placed_ads_in_played_slot_sum, (s.placed_ads_has_fallback_in_played_slot_sum - c.placed_ads_has_fallback_in_played_slot_sum) as diff_placed_ads_has_fallback_in_played_slot_sum, (s.placed_fallback_ads_in_played_slot_sum - c.placed_fallback_ads_in_played_slot_sum) as diff_placed_fallback_ads_in_played_slot_sum, (s.filled_ads_in_played_slot_sum - c.filled_ads_in_played_slot_sum) as diff_filled_ads_in_played_slot_sum, (s.filled_ads_duration_in_played_slot_sum - c.filled_ads_duration_in_played_slot_sum) as diff_filled_ads_duration_in_played_slot_sum, (s.filled_ads_sstf_fallback_in_played_slot_sum - c.filled_ads_sstf_fallback_in_played_slot_sum) as diff_filled_ads_sstf_fallback_in_played_slot_sum, (s.failed_ads_in_played_slot_sum - c.failed_ads_in_played_slot_sum) as diff_failed_ads_in_played_slot_sum, (s.selected_ads_in_played_slot_sum - c.selected_ads_in_played_slot_sum) as diff_selected_ads_in_played_slot_sum, (s.selected_ads_in_played_slot_primary_sum - c.selected_ads_in_played_slot_primary_sum) as diff_selected_ads_in_played_slot_primary_sum, (s.selected_ads_in_played_slot_fallback_sum - c.selected_ads_in_played_slot_fallback_sum) as diff_selected_ads_in_played_slot_fallback_sum, (s.num_placed_ads_in_all_slot - c.num_placed_ads_in_all_slot) as diff_num_placed_ads_in_all_slot, (s.num_placed_ads_has_fallback_in_all_slot - c.num_placed_ads_has_fallback_in_all_slot) as diff_num_placed_ads_has_fallback_in_all_slot, (s.num_placed_fallback_ads_in_all_slot - c.num_placed_fallback_ads_in_all_slot) as diff_num_placed_fallback_ads_in_all_slot, (s.num_filled_ads_in_all_slot - c.num_filled_ads_in_all_slot) as diff_num_filled_ads_in_all_slot, (s.num_filled_ads_duration_in_all_slot - c.num_filled_ads_duration_in_all_slot) as diff_num_filled_ads_duration_in_all_slot, (s.num_filled_ads_sstf_fallback_in_all_slot - c.num_filled_ads_sstf_fallback_in_all_slot) as diff_num_filled_ads_sstf_fallback_in_all_slot, (s.num_failed_ads_in_all_slot - c.num_failed_ads_in_all_slot) as diff_num_failed_ads_in_all_slot, (s.num_selected_ads_in_all_slot - c.num_selected_ads_in_all_slot) as diff_num_selected_ads_in_all_slot, (s.num_selected_ads_in_all_slot_primary - c.num_selected_ads_in_all_slot_primary) as diff_num_selected_ads_in_all_slot_primary, (s.num_selected_ads_in_all_slot_fallback - c.num_selected_ads_in_all_slot_fallback) as diff_num_selected_ads_in_all_slot_fallback, (s.num_decision_type - c.num_decision_type) as diff_num_decision_type, (s.num_linear_avail_type - c.num_linear_avail_type)as diff_num_linear_avail_type, (s.num_station_id - c.num_station_id) as diff_num_station_id, (s.num_ad_in_passback_indicator - c.num_ad_in_passback_indicator) as diff_num_ad_in_passback_indicator, (s.num_loop_indicator - c.num_loop_indicator) as diff_num_loop_indicator, (s.num_programmatic_device_type - c.num_programmatic_device_type) as diff_num_programmatic_device_type, (s.num_standard_device_type_id - c.num_standard_device_type_id) as diff_num_standard_device_type_id, (s.outbound_bids_in_played_slot_sum - c.outbound_bids_in_played_slot_sum) as diff_outbound_bids_in_played_slot_sum, (s.outbound_bidding_revenue_in_played_slot_sum - c.outbound_bidding_revenue_in_played_slot_sum) as diff_outbound_bidding_revenue_in_played_slot_sum, (s.num_selected_yield_optimization_info_ids - c.num_selected_yield_optimization_info_ids) as diff_num_selected_yield_optimization_info_ids, (s.num_standard_channel_visibility - c.num_standard_channel_visibility) as diff_num_standard_channel_visibility, (s.num_content_form_visibility - c.num_content_form_visibility) as diff_num_content_form_visibility, (s.num_bit_flag_aim_product_category - c.num_bit_flag_aim_product_category) as diff_num_bit_flag_aim_product_category, (s.num_media_buyer_id - c.num_media_buyer_id) as diff_num_media_buyer_id, (s.num_post_auction_discount_id - c.num_post_auction_discount_id) as diff_num_post_auction_discount_id, (s.num_selected_yo_volume_cap_ids - c.num_selected_yo_volume_cap_ids) as diff_num_selected_yo_volume_cap_ids, (s.num_selected_yo_distribution_id - c.num_selected_yo_distribution_id) as diff_num_selected_yo_distribution_id, (s.num_selected_yo_distribution_nip_id - c.num_selected_yo_distribution_nip_id) as diff_num_selected_yo_distribution_nip_id, (s.num_selected_yo_inventory_prioritization_id - c.num_selected_yo_inventory_prioritization_id) as diff_num_selected_yo_inventory_prioritization_id, (s.num_selected_yo_inventory_prioritization_nip_id - c.num_selected_yo_inventory_prioritization_nip_id) as diff_num_selected_yo_inventory_prioritization_nip_id, (s.num_selected_yo_margin_id - c.num_selected_yo_margin_id) as diff_num_selected_yo_margin_id, (s.num_integration_type - c.num_integration_type) as diff_num_integration_type, (s.num_standard_content_viewership_profile_ids - c.num_standard_content_viewership_profile_ids) as diff_num_standard_content_viewership_profile_ids, (s.num_standard_privacy_id - c.num_standard_privacy_id) as diff_num_standard_privacy_id, (s.num_standard_addressability_ids - c.num_standard_addressability_ids) as diff_num_standard_addressability_ids, (s.num_standard_sport_entity_ids - c.num_standard_sport_entity_ids) as diff_num_standard_sport_entity_ids, (s.num_upstream_bidding_revenue_in_played_slot - c.num_upstream_bidding_revenue_in_played_slot) as diff_num_upstream_bidding_revenue_in_played_slot, (s.num_event_date - c.num_event_date) as diff_num_event_date FROM stage_agg_v as s FULL OUTER JOIN control_agg_v as c ON s.date = c.date AND s.hour = c.hour"

    cmp_results = spark.sql(query_cmp)
    cmp_results.show(vertical=True,truncate=False)

### How to interpret the comparisons
#   0 = no difference
#   > 0 = stage has a higher count / sum than control
#   < 0 = control has a higher count / sum than stage
```

```py
# Get rows with differences (2nd layer check with COUNT DISTINCT dims)
if run > 0:
    diff_control_rows = control_hashed_with_id.join(diff_control_hashes, on="row_hash", how="inner")
    diff_stage_rows = stage_hashed_with_id.join(diff_stage_hashes, on="row_hash", how="inner")


    print("Control rows with differences:")
    diff_control_rows.show(truncate=False, vertical=True)

    print("Stage rows with differences:")
    diff_stage_rows.show(truncate=False, vertical=True)
```

```py
## MANUAL TROUBLESHOOTING (since there are differences)
```

```py
USER_DIMENSIONS = [
    'process_batch_id','network_id', 'content_owner_id', 'distributor_id', 'reseller_id', 'tv_network_id', 'transaction_type',
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
    'standard_sport_entity_ids', 'selected_yield_optimization_info_ids', 'event_date'
]

USER_METRICS = [
    'selected_primary_ads', 'selected_fallback_ads', 'selected_margin', 'selected_bidding_revenue',
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
    'outbound_bids_in_played_slot', 'outbound_bidding_revenue_in_played_slot', 'upstream_bidding_revenue_in_played_slot'
]
```

```py
#### SELECT ALL (GROUP BY DIMENSIONS)
```

```py
select_all_query = "SELECT date(event_date) as date, date_format(event_date, \"HH\") as hour, process_batch_id, network_id, content_owner_id, distributor_id, reseller_id, tv_network_id, transaction_type, traffic_type, bit_flag, asset_id, series_id, asset_group_ids, site_section_id, site_id, site_section_group_ids, airing_id, channel_id, break_id, time_position_class, inbound_mrm_rule_id, mrm_rule_id, campaign_id, io_id, placement_id, ad_id, creative_id, delivery_method, targeting_criteria_id, ad_unit_id, matched_audience_item_ids, matched_keyvalue_item_ids, matched_daypart, placement_type_priority, platform_group, geo_visibility, user_agent_visibility, postal_code, postal_code_package_ids, user_city_id, user_state_id, user_dma_code, user_country_id, delivered_platform_browser_id, delivered_platform_device_id, delivered_platform_os_id, operator_zone_id, integration_delivery_method, scenario_id, audience_extension_deal_id, tracked_audience_item_ids, geo_state_visibility, geo_dma_visibility, geo_city_visibility, geo_zipcode_visibility, key_value_visibility, slot_avail_type, linear_decision_type, standard_device_type_ids, standard_environment_id, standard_os_id, standard_brand_id, standard_channel_id, standard_genre_ids, content_form_id, content_rating_id, standard_language_ids, stream_mode_id, inventory_location_id, mrm_rule_type_priority, listing_ids, inbound_order_id, inbound_listing_ids, outbound_order_id, outbound_listing_ids, ip_enabled_audience_id, standard_programmer_id, geo_country_visibility, standard_brand_visibility, standard_genre_visibility, content_rating_visibility, standard_endpoint_owner_id, standard_endpoint_id, outbound_exchange_order_id, deal_id, buyer_group_id, dsp_id, programmatic_advertiser_id, supply_source, sales_channel, standard_endpoint_owner_visibility, standard_endpoint_visibility, inbound_order_auction_type, standard_content_daypart_id, ssp_external_publisher_id, global_advertiser_ids, global_brand_ids, market_ad_id, trading_desk_id, user_dma_code_id, global_industry_ids, buyer_platform_id, standard_programmer_visibility, bidding_seat_id, rendition_id, bidding_buyer_id, global_agency_ids, standard_publisher_id, bidder_seat_id, application_type, app_bundle, site_domain, global_currency_version, global_currency_id, standard_app_id, profile_id, profile_type, standard_content_series_id, standard_content_subscription_model_id, standard_ssp_channel_id, standard_site_domain_id, matched_inventory_package_ids, dsp_currency_id, standard_operator_id, standard_iab_category_ids, upstream_inbound_order_id, upstream_global_currency_id, standard_content_territory_id, standard_content_series_visibility, standard_content_credential_status_id, external_seat_id, matched_contextual_segment_ids, inventory_package_ids, selected_yield_optimization_ids, outbound_publisher_id, standard_retailer_id, standard_content_subscription_model_visibility, standard_manufacturer_id, standard_app_bundle_id, content_owner_visibility, reseller_visibility, slot_user_drop_off, sales_strategy, ivt_indicator, request_fill_status, slot_fill_status, slot_sequence_normalized, slot_ad_unit_id, slot_removed_by_ux_indicator, live_linear_indicator, ssp_bidder_indicator, ssp_bidder_buyer_indicator, partner_tag_indicator, promo_ad_indicator, evergreen_ad_indicator, primary_ad_indicator, ad_with_fallback_indicator, priority_tier, priority_type, priority_value, local_advertiser_id, failed_ad_error_code, decision_type, linear_avail_type, station_id, ad_in_passback_indicator, loop_indicator, programmatic_device_type, standard_device_type_id, standard_channel_visibility, content_form_visibility, bit_flag_aim_product_category, media_buyer_id, post_auction_discount_id, selected_yo_volume_cap_ids, selected_yo_distribution_id, selected_yo_distribution_nip_id, selected_yo_inventory_prioritization_id, selected_yo_inventory_prioritization_nip_id, selected_yo_margin_id, integration_type, standard_content_viewership_profile_ids, standard_privacy_id, standard_addressability_ids, standard_sport_entity_ids, selected_yield_optimization_info_ids, event_date, SUM(selected_primary_ads) as selected_primary_ads_sum, SUM(selected_fallback_ads) as selected_fallback_ads_sum, SUM(selected_margin) as selected_margin_sum, SUM(selected_bidding_revenue) as selected_bidding_revenue_sum, SUM(co_selected_bidding_revenue) as co_selected_bidding_revenue_sum, SUM(d_selected_bidding_revenue) as d_selected_bidding_revenue_sum, SUM(r_selected_bidding_revenue) as r_selected_bidding_revenue_sum, SUM(selected_fallback_margin) as selected_fallback_margin_sum, SUM(selected_fallback_bidding_revenue) as selected_fallback_bidding_revenue_sum, SUM(co_selected_fallback_bidding_revenue) as co_selected_fallback_bidding_revenue_sum, SUM(d_selected_fallback_bidding_revenue) as d_selected_fallback_bidding_revenue_sum, SUM(r_selected_fallback_bidding_revenue) as r_selected_fallback_bidding_revenue_sum, SUM(ssp_bids) as ssp_bids_sum, SUM(ssp_co_bidding_revenue) as ssp_co_bidding_revenue_sum, SUM(placed_ads_in_played_slot) as placed_ads_in_played_slot_sum, SUM(placed_ads_has_fallback_in_played_slot) as placed_ads_has_fallback_in_played_slot_sum, SUM(placed_fallback_ads_in_played_slot) as placed_fallback_ads_in_played_slot_sum, SUM(filled_ads_in_played_slot) as filled_ads_in_played_slot_sum, SUM(filled_ads_duration_in_played_slot) as filled_ads_duration_in_played_slot_sum, SUM(filled_ads_sstf_fallback_in_played_slot) as filled_ads_sstf_fallback_in_played_slot_sum, SUM(failed_ads_in_played_slot) as failed_ads_in_played_slot_sum, SUM(selected_ads_in_played_slot) as selected_ads_in_played_slot_sum, SUM(selected_ads_in_played_slot_primary) as selected_ads_in_played_slot_primary_sum, SUM(selected_ads_in_played_slot_fallback) as selected_ads_in_played_slot_fallback_sum, SUM(placed_ads_in_all_slot) as placed_ads_in_all_slot_sum, SUM(placed_ads_has_fallback_in_all_slot) as placed_ads_has_fallback_in_all_slot_sum, SUM(placed_fallback_ads_in_all_slot) as placed_fallback_ads_in_all_slot_sum, SUM(filled_ads_in_all_slot) as filled_ads_in_all_slot_sum, SUM(filled_ads_duration_in_all_slot) as filled_ads_duration_in_all_slot_sum, SUM(filled_ads_sstf_fallback_in_all_slot) as filled_ads_sstf_fallback_in_all_slot_sum, SUM(failed_ads_in_all_slot) as failed_ads_in_all_slot_sum, SUM(selected_ads_in_all_slot) as selected_ads_in_all_slot_sum, SUM(selected_ads_in_all_slot_primary) as selected_ads_in_all_slot_primary_sum, SUM(selected_ads_in_all_slot_fallback) as selected_ads_in_all_slot_fallback_sum, SUM(outbound_bids_in_played_slot) as outbound_bids_in_played_slot_sum, SUM(outbound_bidding_revenue_in_played_slot) as outbound_bidding_revenue_in_played_slot_sum, SUM(upstream_bidding_revenue_in_played_slot) as upstream_bidding_revenue_in_played_slot_sum FROM VIEW_TABLE WHERE date(event_date) = CAST('START_DATE' AS DATE) AND date_format(event_date, \"HH\") = RUN_HOUR GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188 ORDER BY 1, 2"
```

```py
control_select_all_query = select_all_query.replace("VIEW_TABLE","control_v",1).replace("START_DATE", start_date).replace("RUN_HOUR",run_hour)
stage_select_all_query = select_all_query.replace("VIEW_TABLE","stage_v",1).replace("START_DATE",start_date).replace("RUN_HOUR",run_hour)
control_select_all_agg=spark.sql(control_select_all_query)
stage_select_all_agg=spark.sql(stage_select_all_query)

# Verify the data results are non-empty before running comparisons
proceed = 1
if (control_select_all_agg is None or control_select_all_agg.isEmpty()): 
        proceed = 0
        print("Empty control data. Stopping here.")
elif ( stage_select_all_agg is None or stage_select_all_agg.isEmpty() ):
        proceed = 0
        print("Empty stage data. Stopping here.")
else:
        print("Found some aggregated data results.")


is_match = 0
if proceed == 1:
    # Add row_id to identify rows
    control_with_id = control_select_all_agg.withColumn("row_id", f.monotonically_increasing_id())
    stage_with_id = stage_select_all_agg.withColumn("row_id", f.monotonically_increasing_id())
    
    # Create hash for each row
    control_hashed = control_with_id.withColumn("row_hash", f.xxhash64(*control_select_all_agg.columns))
    stage_hashed = stage_with_id.withColumn("row_hash", f.xxhash64(*stage_select_all_agg.columns))
    
    # Find rows that don't match by hash
    diff_control_hashes = control_hashed.select("row_hash", "row_id").exceptAll(stage_hashed.select("row_hash", "row_id"))
    diff_stage_hashes = stage_hashed.select("row_hash", "row_id").exceptAll(control_hashed.select("row_hash", "row_id"))
    
    if diff_control_hashes.isEmpty() and diff_stage_hashes.isEmpty():
        is_match = 1
        print("OK! Data matched.")
    else:
        is_match = 0
        print("UH-OH. Data did not match. Further diagnostics below...")
        
        # Get full rows for mismatched hashes in control
        if not diff_control_hashes.isEmpty():
            control_mismatches = control_hashed.join(
                diff_control_hashes.select("row_id"),
                on="row_id",
                how="inner"
            ).drop("row_id")
            print(f"\nRows in CONTROL but not in STAGE (or different): {control_mismatches.count()}")
            control_mismatches.show(100, truncate=False, vertical=True)
        
        # Get full rows for mismatched hashes in stage
        if not diff_stage_hashes.isEmpty():
            stage_mismatches = stage_hashed.join(
                diff_stage_hashes.select("row_id"),
                on="row_id",
                how="inner"
            ).drop("row_id")
            print(f"\nRows in STAGE but not in CONTROL (or different): {stage_mismatches.count()}")
            stage_mismatches.show(100, truncate=False, vertical=True)
```

```py
%md
## OTHER TROUBLESHOOTING OPTIONS
#### GENERATE SQLs
```

```py
# Read full tables for the relevant date/hour
filter_expr = f"date(event_date) = CAST('{start_date}' AS DATE) AND date_format(event_date, 'HH') = '{run_hour}'"
full_control = df_control.filter(filter_expr).withColumn("row_id", f.monotonically_increasing_id())
full_stage = df_stage.filter(filter_expr).withColumn("row_id", f.monotonically_increasing_id())

full_control.createOrReplaceTempView("full_control_v")
full_stage.createOrReplaceTempView("full_stage_v")

# Build join keys and diff expressions
join_keys = USER_DIMENSIONS
select_exprs = []
diff_exprs = []
for col in USER_DIMENSIONS + USER_METRICS:
    select_exprs.append(f"c.{col} as control_{col}")
    select_exprs.append(f"s.{col} as stage_{col}")
    diff_exprs.append(
        f"(c.{col} <> s.{col} OR (c.{col} IS NULL AND s.{col} IS NOT NULL) OR (c.{col} IS NOT NULL AND s.{col} IS NULL)) as diff_{col}"
    )

join_cond = " AND ".join([f"c.{k} <=> s.{k}" for k in join_keys])  # null-safe equality

full_diff_query = f"""
SELECT
    {', '.join(select_exprs)},
    {', '.join(diff_exprs)}
FROM full_control_v c
FULL OUTER JOIN full_stage_v s
      ON {join_cond}
"""

print("FULL DIFF QUERY:")
print(full_diff_query)

# diff_df = spark.sql(full_diff_query)
# print(diff_df.count())
# diff_df.show(5)
```

```py
# 1. Check for Duplicates
dup_keys = ", ".join(USER_DIMENSIONS)
sql_duplicates_control = f"""
SELECT {dup_keys}, COUNT(*) as cnt
FROM {control_table}
GROUP BY {dup_keys}
HAVING cnt > 1
LIMIT 100
"""
sql_duplicates_stage = f"""
SELECT {dup_keys}, COUNT(*) as cnt
FROM {stage_table}
GROUP BY {dup_keys}
HAVING cnt > 1
LIMIT 100
"""

# 2. Null/Type Mismatches (Nulls in key columns)
null_checks = " OR ".join([f"{col} IS NULL" for col in USER_DIMENSIONS])
sql_nulls_control = f"SELECT * FROM control_v WHERE {null_checks} LIMIT 100"
sql_nulls_stage = f"SELECT * FROM stage_v WHERE {null_checks} LIMIT 100"

# 3. Unmatched Keys (Anti-join)
join_cond = " AND ".join([f"c.{k} <=> s.{k}" for k in USER_DIMENSIONS])
key_cols = ", ".join([f"c.{k}" for k in USER_DIMENSIONS])
sql_keys_in_control_not_stage = f"""
SELECT {key_cols}
FROM {control_table} c
LEFT ANTI JOIN stage_v s
  ON {join_cond}
LIMIT 100
"""
sql_keys_in_stage_not_control = f"""
SELECT {key_cols.replace('c.', 's.')}
FROM {stage_table} s
LEFT ANTI JOIN control_v c
  ON {join_cond}
LIMIT 100
"""

# 4. Distribution/Histogram Analysis (one metric example)
metric = USER_METRICS[0] if USER_METRICS else 'some_metric'
sql_histogram_control = f"""
SELECT {metric}, COUNT(*) as cnt
FROM {control_table}
GROUP BY {metric}
ORDER BY cnt DESC
LIMIT 20
"""
sql_histogram_stage = f"""
SELECT {metric}, COUNT(*) as cnt
FROM {stage_table}
GROUP BY {metric}
ORDER BY cnt DESC
LIMIT 20
"""

# 5. Sample Problematic Rows (rows with any difference)
select_exprs = []
diff_exprs = []
for col in USER_DIMENSIONS + USER_METRICS:
    select_exprs.append(f"c.{col} as control_{col}")
    select_exprs.append(f"s.{col} as stage_{col}")
    diff_exprs.append(
        f"(c.{col} <> s.{col} OR (c.{col} IS NULL AND s.{col} IS NOT NULL) OR (c.{col} IS NOT NULL AND s.{col} IS NULL)) as diff_{col}"
    )
any_diff_expr = " OR ".join([f"diff_{col}" for col in USER_DIMENSIONS + USER_METRICS])
sql_problematic_rows = f"""
SELECT
  {', '.join(select_exprs)},
  {', '.join(diff_exprs)}
FROM {control_table} c
FULL OUTER JOIN {stage_table} s
  ON {join_cond}
WHERE {any_diff_expr}
LIMIT 100
"""

# 6. Truncation/Precision Issues (example for float/decimal columns)
float_metric = next((m for m in USER_METRICS if 'revenue' in m or 'margin' in m), USER_METRICS[0])
sql_precision_diff = f"""
SELECT c.{float_metric} as control_val, s.{float_metric} as stage_val,
       ABS(c.{float_metric} - s.{float_metric}) as abs_diff
FROM {control_table} c
INNER JOIN {stage_table} s
  ON {join_cond}
WHERE ABS(c.{float_metric} - s.{float_metric}) > 0.01
LIMIT 100
"""

# 7. Log/Export Differences (write to table)
# Generate diff expressions
select_exprs = []
diff_exprs = []
diff_conditions = []
for col in USER_DIMENSIONS + USER_METRICS:
    select_exprs.append(f"c.{col} as control_{col}")
    select_exprs.append(f"s.{col} as stage_{col}")
    diff_expr = f"(c.{col} <> s.{col} OR (c.{col} IS NULL AND s.{col} IS NOT NULL) OR (c.{col} IS NOT NULL AND s.{col} IS NULL)) as diff_{col}"
    diff_exprs.append(diff_expr)
    diff_conditions.append(f"(c.{col} <> s.{col} OR (c.{col} IS NULL AND s.{col} IS NOT NULL) OR (c.{col} IS NOT NULL AND s.{col} IS NULL))")

any_diff_expr = " OR ".join(diff_conditions)

sql_export_diff = f"""
CREATE OR REPLACE TABLE fw1_stg.kbhargava.diff_results AS
SELECT
  {', '.join(select_exprs)},
  {', '.join(diff_exprs)}
FROM {control_table} c
FULL OUTER JOIN {stage_table} s
  ON {" AND ".join([f"c.{k} <=> s.{k}" for k in USER_DIMENSIONS])}
WHERE {any_diff_expr}
"""

# Print all SQLs
print("1. Duplicates in control:\n", sql_duplicates_control)
print("1. Duplicates in stage:\n", sql_duplicates_stage)
print("2. Nulls in control:\n", sql_nulls_control)
print("2. Nulls in stage:\n", sql_nulls_stage)
print("3. Keys in control not in stage:\n", sql_keys_in_control_not_stage)
print("3. Keys in stage not in control:\n", sql_keys_in_stage_not_control)
print("4. Histogram in control:\n", sql_histogram_control)
print("4. Histogram in stage:\n", sql_histogram_stage)
print("5. Problematic rows:\n", sql_problematic_rows)
print("6. Precision issues:\n", sql_precision_diff)
print("7. Export differences:\n", sql_export_diff)

```

```py
%md
## DEBUG (EXTRA CODE MAYBE NOT NEEDED)
```

```py
validate_query_new = "SELECT date(event_date) as date, date_format(event_date, \"HH\") as hour,  process_batch_id as process_batch_id,  network_id as network_id,  content_owner_id as content_owner_id,  distributor_id as distributor_id,  reseller_id as reseller_id,  tv_network_id as tv_network_id,  transaction_type as transaction_type,  traffic_type as traffic_type,  bit_flag as bit_flag,  asset_id as asset_id,  series_id as series_id,  asset_group_ids as asset_group_ids,  site_section_id as site_section_id,  site_id as site_id,  site_section_group_ids as site_section_group_ids,  airing_id as airing_id,  channel_id as channel_id,  break_id as break_id,  time_position_class as time_position_class,  inbound_mrm_rule_id as inbound_mrm_rule_id,  mrm_rule_id as mrm_rule_id,  campaign_id as campaign_id,  io_id as io_id,  placement_id as placement_id,  ad_id as ad_id,  creative_id as creative_id,  delivery_method as delivery_method,  targeting_criteria_id as targeting_criteria_id,  ad_unit_id as ad_unit_id,  matched_audience_item_ids as matched_audience_item_ids,  matched_keyvalue_item_ids as matched_keyvalue_item_ids,  matched_daypart as matched_daypart,  placement_type_priority as placement_type_priority,  platform_group as platform_group,  geo_visibility as geo_visibility,  user_agent_visibility as user_agent_visibility,  postal_code as postal_code,  postal_code_package_ids as postal_code_package_ids,  user_city_id as user_city_id,  user_state_id as user_state_id,  user_dma_code as user_dma_code,  user_country_id as user_country_id,  delivered_platform_browser_id as delivered_platform_browser_id,  delivered_platform_device_id as delivered_platform_device_id,  delivered_platform_os_id as delivered_platform_os_id,  operator_zone_id as operator_zone_id,  integration_delivery_method as integration_delivery_method,  scenario_id as scenario_id,  audience_extension_deal_id as audience_extension_deal_id,  tracked_audience_item_ids as tracked_audience_item_ids,  geo_state_visibility as geo_state_visibility,  geo_dma_visibility as geo_dma_visibility,  geo_city_visibility as geo_city_visibility,  geo_zipcode_visibility as geo_zipcode_visibility,  key_value_visibility as key_value_visibility,  slot_avail_type as slot_avail_type,  linear_decision_type as linear_decision_type,  standard_device_type_ids as standard_device_type_ids,  standard_environment_id as standard_environment_id,  standard_os_id as standard_os_id,  standard_brand_id as standard_brand_id,  standard_channel_id as standard_channel_id,  standard_genre_ids as standard_genre_ids,  content_form_id as content_form_id,  content_rating_id as content_rating_id,  standard_language_ids as standard_language_ids,  stream_mode_id as stream_mode_id,  inventory_location_id as inventory_location_id,  mrm_rule_type_priority as mrm_rule_type_priority,  listing_ids as listing_ids,  inbound_order_id as inbound_order_id,  inbound_listing_ids as inbound_listing_ids,  outbound_order_id as outbound_order_id,  outbound_listing_ids as outbound_listing_ids,  ip_enabled_audience_id as ip_enabled_audience_id,  standard_programmer_id as standard_programmer_id,  geo_country_visibility as geo_country_visibility,  standard_brand_visibility as standard_brand_visibility,  standard_genre_visibility as standard_genre_visibility,  content_rating_visibility as content_rating_visibility,  standard_endpoint_owner_id as standard_endpoint_owner_id,  standard_endpoint_id as standard_endpoint_id,  outbound_exchange_order_id as outbound_exchange_order_id,  deal_id as deal_id,  buyer_group_id as buyer_group_id,  dsp_id as dsp_id,  programmatic_advertiser_id as programmatic_advertiser_id,  supply_source as supply_source,  sales_channel as sales_channel,  standard_endpoint_owner_visibility as standard_endpoint_owner_visibility,  standard_endpoint_visibility as standard_endpoint_visibility,  inbound_order_auction_type as inbound_order_auction_type,  standard_content_daypart_id as standard_content_daypart_id,  ssp_external_publisher_id as ssp_external_publisher_id,  global_advertiser_ids as global_advertiser_ids,  global_brand_ids as global_brand_ids,  market_ad_id as market_ad_id,  trading_desk_id as trading_desk_id,  user_dma_code_id as user_dma_code_id,  global_industry_ids as global_industry_ids,  buyer_platform_id as buyer_platform_id,  standard_programmer_visibility as standard_programmer_visibility,  bidding_seat_id as bidding_seat_id,  rendition_id as rendition_id,  bidding_buyer_id as bidding_buyer_id,  global_agency_ids as global_agency_ids,  standard_publisher_id as standard_publisher_id,  bidder_seat_id as bidder_seat_id,  application_type as application_type,  app_bundle as app_bundle,  site_domain as site_domain,  global_currency_version as global_currency_version,  global_currency_id as global_currency_id,  standard_app_id as standard_app_id,  profile_id as profile_id,  profile_type as profile_type,  standard_content_series_id as standard_content_series_id,  standard_content_subscription_model_id as standard_content_subscription_model_id,  standard_ssp_channel_id as standard_ssp_channel_id,  standard_site_domain_id as standard_site_domain_id,  matched_inventory_package_ids as matched_inventory_package_ids,  dsp_currency_id as dsp_currency_id,  standard_operator_id as standard_operator_id,  standard_iab_category_ids as standard_iab_category_ids,  upstream_inbound_order_id as upstream_inbound_order_id,  upstream_global_currency_id as upstream_global_currency_id,  standard_content_territory_id as standard_content_territory_id,  standard_content_series_visibility as standard_content_series_visibility,  standard_content_credential_status_id as standard_content_credential_status_id,  external_seat_id as external_seat_id,  matched_contextual_segment_ids as matched_contextual_segment_ids,  inventory_package_ids as inventory_package_ids,  selected_yield_optimization_ids as selected_yield_optimization_ids,  outbound_publisher_id as outbound_publisher_id,  standard_retailer_id as standard_retailer_id,  standard_content_subscription_model_visibility as standard_content_subscription_model_visibility,  standard_manufacturer_id as standard_manufacturer_id,  standard_app_bundle_id as standard_app_bundle_id,  content_owner_visibility as content_owner_visibility,  reseller_visibility as reseller_visibility,  slot_user_drop_off as slot_user_drop_off,  sales_strategy as sales_strategy,  ivt_indicator as ivt_indicator,  request_fill_status as request_fill_status,  slot_fill_status as slot_fill_status,  slot_sequence_normalized as slot_sequence_normalized,  slot_ad_unit_id as slot_ad_unit_id,  slot_removed_by_ux_indicator as slot_removed_by_ux_indicator,  live_linear_indicator as live_linear_indicator,  ssp_bidder_indicator as ssp_bidder_indicator,  ssp_bidder_buyer_indicator as ssp_bidder_buyer_indicator,  partner_tag_indicator as partner_tag_indicator,  promo_ad_indicator as promo_ad_indicator,  evergreen_ad_indicator as evergreen_ad_indicator,  primary_ad_indicator as primary_ad_indicator,  ad_with_fallback_indicator as ad_with_fallback_indicator,  priority_tier as priority_tier,  priority_type as priority_type,  priority_value as priority_value,  local_advertiser_id as local_advertiser_id,  failed_ad_error_code as failed_ad_error_code,  decision_type as decision_type,  linear_avail_type as linear_avail_type,  station_id as station_id,  ad_in_passback_indicator as ad_in_passback_indicator,  loop_indicator as loop_indicator,  programmatic_device_type as programmatic_device_type,  standard_device_type_id as standard_device_type_id,  standard_channel_visibility as standard_channel_visibility,  content_form_visibility as content_form_visibility,  bit_flag_aim_product_category as bit_flag_aim_product_category,  media_buyer_id as media_buyer_id,  post_auction_discount_id as post_auction_discount_id,  selected_yo_volume_cap_ids as selected_yo_volume_cap_ids,  selected_yo_distribution_id as selected_yo_distribution_id,  selected_yo_distribution_nip_id as selected_yo_distribution_nip_id,  selected_yo_inventory_prioritization_id as selected_yo_inventory_prioritization_id,  selected_yo_inventory_prioritization_nip_id as selected_yo_inventory_prioritization_nip_id,  selected_yo_margin_id as selected_yo_margin_id,  integration_type as integration_type,  standard_content_viewership_profile_ids as standard_content_viewership_profile_ids,  standard_privacy_id as standard_privacy_id,  standard_addressability_ids as standard_addressability_ids,  standard_sport_entity_ids as standard_sport_entity_ids,  selected_yield_optimization_info_ids as selected_yield_optimization_info_ids,  event_date as event_date, SUM(selected_primary_ads) as selected_primary_ads_sum, SUM(selected_fallback_ads) as selected_fallback_ads_sum, SUM(selected_margin) as selected_margin_sum, SUM(selected_bidding_revenue) as selected_bidding_revenue_sum, SUM(co_selected_bidding_revenue) as co_selected_bidding_revenue_sum, SUM(d_selected_bidding_revenue) as d_selected_bidding_revenue_sum, SUM(r_selected_bidding_revenue) as r_selected_bidding_revenue_sum, SUM(selected_fallback_margin) as selected_fallback_margin_sum, SUM(selected_fallback_bidding_revenue) as selected_fallback_bidding_revenue_sum, SUM(co_selected_fallback_bidding_revenue) as co_selected_fallback_bidding_revenue_sum, SUM(d_selected_fallback_bidding_revenue) as d_selected_fallback_bidding_revenue_sum, SUM(r_selected_fallback_bidding_revenue) as r_selected_fallback_bidding_revenue_sum, SUM(ssp_bids) as ssp_bids_sum, SUM(ssp_co_bidding_revenue) as ssp_co_bidding_revenue_sum, SUM(placed_ads_in_played_slot) as placed_ads_in_played_slot_sum, SUM(placed_ads_has_fallback_in_played_slot) as placed_ads_has_fallback_in_played_slot_sum, SUM(placed_fallback_ads_in_played_slot) as placed_fallback_ads_in_played_slot_sum, SUM(filled_ads_in_played_slot) as filled_ads_in_played_slot_sum, SUM(filled_ads_duration_in_played_slot) as filled_ads_duration_in_played_slot_sum, SUM(filled_ads_sstf_fallback_in_played_slot) as filled_ads_sstf_fallback_in_played_slot_sum, SUM(failed_ads_in_played_slot) as failed_ads_in_played_slot_sum, SUM(selected_ads_in_played_slot) as selected_ads_in_played_slot_sum, SUM(selected_ads_in_played_slot_primary) as selected_ads_in_played_slot_primary_sum, SUM(selected_ads_in_played_slot_fallback) as selected_ads_in_played_slot_fallback_sum, SUM(placed_ads_in_all_slot) as placed_ads_in_all_slot_sum, SUM(placed_ads_has_fallback_in_all_slot) as placed_ads_has_fallback_in_all_slot_sum, SUM(placed_fallback_ads_in_all_slot) as placed_fallback_ads_in_all_slot_sum, SUM(filled_ads_in_all_slot) as filled_ads_in_all_slot_sum, SUM(filled_ads_duration_in_all_slot) as filled_ads_duration_in_all_slot_sum, SUM(filled_ads_sstf_fallback_in_all_slot) as filled_ads_sstf_fallback_in_all_slot_sum, SUM(failed_ads_in_all_slot) as failed_ads_in_all_slot_sum, SUM(selected_ads_in_all_slot) as selected_ads_in_all_slot_sum, SUM(selected_ads_in_all_slot_primary) as selected_ads_in_all_slot_primary_sum, SUM(selected_ads_in_all_slot_fallback) as selected_ads_in_all_slot_fallback_sum, SUM(outbound_bids_in_played_slot) as outbound_bids_in_played_slot_sum, SUM(outbound_bidding_revenue_in_played_slot) as outbound_bidding_revenue_in_played_slot_sum, SUM(upstream_bidding_revenue_in_played_slot) as upstream_bidding_revenue_in_played_slot_sum FROM VIEW_TABLE WHERE date(event_date) = CAST('START_DATE' AS DATE) AND date_format(event_date, \"HH\") = RUN_HOUR GROUP BY process_batch_id, network_id, content_owner_id, distributor_id, reseller_id, tv_network_id, transaction_type, traffic_type, bit_flag, asset_id, series_id, asset_group_ids, site_section_id, site_id, site_section_group_ids, airing_id, channel_id, break_id, time_position_class, inbound_mrm_rule_id, mrm_rule_id, campaign_id, io_id, placement_id, ad_id, creative_id, delivery_method, targeting_criteria_id, ad_unit_id, matched_audience_item_ids, matched_keyvalue_item_ids, matched_daypart, placement_type_priority, platform_group, geo_visibility, user_agent_visibility, postal_code, postal_code_package_ids, user_city_id, user_state_id, user_dma_code, user_country_id, delivered_platform_browser_id, delivered_platform_device_id, delivered_platform_os_id, operator_zone_id, integration_delivery_method, scenario_id, audience_extension_deal_id, tracked_audience_item_ids, geo_state_visibility, geo_dma_visibility, geo_city_visibility, geo_zipcode_visibility, key_value_visibility, slot_avail_type, linear_decision_type, standard_device_type_ids, standard_environment_id, standard_os_id, standard_brand_id, standard_channel_id, standard_genre_ids, content_form_id, content_rating_id, standard_language_ids, stream_mode_id, inventory_location_id, mrm_rule_type_priority, listing_ids, inbound_order_id, inbound_listing_ids, outbound_order_id, outbound_listing_ids, ip_enabled_audience_id, standard_programmer_id, geo_country_visibility, standard_brand_visibility, standard_genre_visibility, content_rating_visibility, standard_endpoint_owner_id, standard_endpoint_id, outbound_exchange_order_id, deal_id, buyer_group_id, dsp_id, programmatic_advertiser_id, supply_source, sales_channel, standard_endpoint_owner_visibility, standard_endpoint_visibility, inbound_order_auction_type, standard_content_daypart_id, ssp_external_publisher_id, global_advertiser_ids, global_brand_ids, market_ad_id, trading_desk_id, user_dma_code_id, global_industry_ids, buyer_platform_id, standard_programmer_visibility, bidding_seat_id, rendition_id, bidding_buyer_id, global_agency_ids, standard_publisher_id, bidder_seat_id, application_type, app_bundle, site_domain, global_currency_version, global_currency_id, standard_app_id, profile_id, profile_type, standard_content_series_id, standard_content_subscription_model_id, standard_ssp_channel_id, standard_site_domain_id, matched_inventory_package_ids, dsp_currency_id, standard_operator_id, standard_iab_category_ids, upstream_inbound_order_id, upstream_global_currency_id, standard_content_territory_id, standard_content_series_visibility, standard_content_credential_status_id, external_seat_id, matched_contextual_segment_ids, inventory_package_ids, selected_yield_optimization_ids, outbound_publisher_id, standard_retailer_id, standard_content_subscription_model_visibility, standard_manufacturer_id, standard_app_bundle_id, content_owner_visibility, reseller_visibility, slot_user_drop_off, sales_strategy, ivt_indicator, request_fill_status, slot_fill_status, slot_sequence_normalized, slot_ad_unit_id, slot_removed_by_ux_indicator, live_linear_indicator, ssp_bidder_indicator, ssp_bidder_buyer_indicator, partner_tag_indicator, promo_ad_indicator, evergreen_ad_indicator, primary_ad_indicator, ad_with_fallback_indicator, priority_tier, priority_type, priority_value, local_advertiser_id, failed_ad_error_code, decision_type, linear_avail_type, station_id, ad_in_passback_indicator, loop_indicator, programmatic_device_type, standard_device_type_id, standard_channel_visibility, content_form_visibility, bit_flag_aim_product_category, media_buyer_id, post_auction_discount_id, selected_yo_volume_cap_ids, selected_yo_distribution_id, selected_yo_distribution_nip_id, selected_yo_inventory_prioritization_id, selected_yo_inventory_prioritization_nip_id, selected_yo_margin_id, integration_type, standard_content_viewership_profile_ids, standard_privacy_id, standard_addressability_ids, standard_sport_entity_ids, selected_yield_optimization_info_ids, event_date ORDER BY 1, 2"
```

```py
control_troubleshooting_query = validate_query_new.replace("VIEW_TABLE","control_v",1).replace("START_DATE", start_date).replace("RUN_HOUR",run_hour)
stage_troubleshooting_query = validate_query_new.replace("VIEW_TABLE","stage_v",1).replace("START_DATE",start_date).replace("RUN_HOUR",run_hour)
print("-----CONTROL------")
control_troubleshooting_agg=spark.sql(control_troubleshooting_query).show(truncate=False, vertical=True)
```

```py
print("------STAGE------")
stage__troubleshooting_agg=spark.sql(stage_troubleshooting_query).show(truncate=False, vertical=True)
```

```py
## IF DATA IS NOT IN TABLE, WE CAN READ IT IN AND SPECIFY THE SCHEMA (FROM S3 OR WHEREVER)
```

```py
'process_batch_id', 'network_id', 'content_owner_id', 'distributor_id', 'reseller_id', 'tv_network_id', 'transaction_type', 'traffic_type', 'bit_flag', 'asset_id', 'series_id', 'asset_group_ids', 'site_section_id', 'site_id', 'site_section_group_ids', 'airing_id', 'channel_id', 'break_id', 'time_position_class', 'inbound_mrm_rule_id', 'mrm_rule_id', 'campaign_id', 'io_id', 'placement_id', 'ad_id', 'creative_id', 'delivery_method', 'targeting_criteria_id', 'ad_unit_id', 'matched_audience_item_ids', 'matched_keyvalue_item_ids', 'matched_daypart', 'placement_type_priority', 'platform_group', 'geo_visibility', 'user_agent_visibility', 'postal_code', 'postal_code_package_ids', 'user_city_id', 'user_state_id', 'user_dma_code', 'user_country_id', 'delivered_platform_browser_id', 'delivered_platform_device_id', 'delivered_platform_os_id', 'operator_zone_id', 'integration_delivery_method', 'scenario_id', 'audience_extension_deal_id', 'tracked_audience_item_ids', 'geo_state_visibility', 'geo_dma_visibility', 'geo_city_visibility', 'geo_zipcode_visibility', 'key_value_visibility', 'slot_avail_type', 'linear_decision_type', 'standard_device_type_ids', 'standard_environment_id', 'standard_os_id', 'standard_brand_id', 'standard_channel_id', 'standard_genre_ids', 'content_form_id', 'content_rating_id', 'standard_language_ids', 'stream_mode_id', 'inventory_location_id', 'mrm_rule_type_priority', 'listing_ids', 'inbound_order_id', 'inbound_listing_ids', 'outbound_order_id', 'outbound_listing_ids', 'selected_primary_ads', 'selected_fallback_ads', 'selected_margin', 'selected_bidding_revenue', 'co_selected_bidding_revenue', 'd_selected_bidding_revenue', 'r_selected_bidding_revenue', 'selected_fallback_margin', 'selected_fallback_bidding_revenue', 'co_selected_fallback_bidding_revenue', 'd_selected_fallback_bidding_revenue', 'r_selected_fallback_bidding_revenue', 'ip_enabled_audience_id', 'standard_programmer_id', 'geo_country_visibility', 'standard_brand_visibility', 'standard_genre_visibility', 'content_rating_visibility', 'standard_endpoint_owner_id', 'standard_endpoint_id', 'outbound_exchange_order_id', 'deal_id', 'buyer_group_id', 'dsp_id', 'programmatic_advertiser_id', 'supply_source', 'sales_channel', 'standard_endpoint_owner_visibility', 'standard_endpoint_visibility', 'inbound_order_auction_type', 'ssp_bids', 'ssp_co_bidding_revenue', 'standard_content_daypart_id', 'ssp_external_publisher_id', 'global_advertiser_ids', 'global_brand_ids', 'market_ad_id', 'trading_desk_id', 'user_dma_code_id', 'global_industry_ids', 'buyer_platform_id', 'standard_programmer_visibility', 'bidding_seat_id', 'rendition_id', 'bidding_buyer_id', 'global_agency_ids', 'standard_publisher_id', 'bidder_seat_id', 'application_type', 'app_bundle', 'site_domain', 'global_currency_version', 'global_currency_id', 'standard_app_id', 'profile_id', 'profile_type', 'standard_content_series_id', 'standard_content_subscription_model_id', 'standard_ssp_channel_id', 'standard_site_domain_id', 'matched_inventory_package_ids', 'dsp_currency_id', 'standard_operator_id', 'standard_iab_category_ids', 'upstream_inbound_order_id', 'upstream_global_currency_id', 'standard_content_territory_id', 'standard_content_series_visibility', 'standard_content_credential_status_id', 'external_seat_id', 'matched_contextual_segment_ids', 'inventory_package_ids', 'selected_yield_optimization_ids', 'outbound_publisher_id', 'standard_retailer_id', 'standard_content_subscription_model_visibility', 'standard_manufacturer_id', 'standard_app_bundle_id', 'content_owner_visibility', 'reseller_visibility', 'slot_user_drop_off', 'sales_strategy', 'ivt_indicator', 'request_fill_status', 'slot_fill_status', 'slot_sequence_normalized', 'slot_ad_unit_id', 'slot_removed_by_ux_indicator', 'live_linear_indicator', 'ssp_bidder_indicator', 'ssp_bidder_buyer_indicator', 'partner_tag_indicator', 'promo_ad_indicator', 'evergreen_ad_indicator', 'primary_ad_indicator', 'ad_with_fallback_indicator', 'priority_tier', 'priority_type', 'priority_value', 'local_advertiser_id', 'failed_ad_error_code', 'placed_ads_in_played_slot', 'placed_ads_has_fallback_in_played_slot', 'placed_fallback_ads_in_played_slot', 'filled_ads_in_played_slot', 'filled_ads_duration_in_played_slot', 'filled_ads_sstf_fallback_in_played_slot', 'failed_ads_in_played_slot', 'selected_ads_in_played_slot', 'selected_ads_in_played_slot_primary', 'selected_ads_in_played_slot_fallback', 'placed_ads_in_all_slot', 'placed_ads_has_fallback_in_all_slot', 'placed_fallback_ads_in_all_slot', 'filled_ads_in_all_slot', 'filled_ads_duration_in_all_slot', 'filled_ads_sstf_fallback_in_all_slot', 'failed_ads_in_all_slot', 'selected_ads_in_all_slot', 'selected_ads_in_all_slot_primary', 'selected_ads_in_all_slot_fallback', 'decision_type', 'linear_avail_type', 'station_id', 'ad_in_passback_indicator', 'loop_indicator', 'programmatic_device_type', 'standard_device_type_id', 'outbound_bids_in_played_slot', 'outbound_bidding_revenue_in_played_slot', 'selected_yield_optimization_info_ids', 'standard_channel_visibility', 'content_form_visibility', 'bit_flag_aim_product_category', 'media_buyer_id', 'post_auction_discount_id', 'selected_yo_volume_cap_ids', 'selected_yo_distribution_id', 'selected_yo_distribution_nip_id', 'selected_yo_inventory_prioritization_id', 'selected_yo_inventory_prioritization_nip_id', 'selected_yo_margin_id', 'integration_type', 'standard_content_viewership_profile_ids', 'standard_privacy_id', 'standard_addressability_ids', 'standard_sport_entity_ids', 'upstream_bidding_revenue_in_played_slot', 'event_date'
```

```py
# DEBUG
```

```py
control_agg.show(vertical=True, truncate=False)
```

```py
stage_agg.show(vertical=True, truncate=False)
```

```py
spark.sql("SELECT (s.num_process_batch_id - c.num_process_batch_id) as diff_num_process_batch_id FROM stage_agg_v as s FULL OUTER JOIN control_agg_v as c ON s.date = c.date").show(vertical=True, truncate=False)
```

## Questions?

 

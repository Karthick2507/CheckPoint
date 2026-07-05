# f\_process\_request\_hourly

# Introduction

Below is validation results for `f_process_request_hourly` 

It compares data from current hoover model and the new H++ output of the same table.

# Problematic Dimensions Fixes

Please check the tracker here: 

Validations tracker → 

# 2026-04-16 → Hour 15

We're almost aligned between Hoover \<\> Hoover++. 

For this hour, we see 747,109 rows in control vs 746,925 rows in stage. 

The checks we did (and their status)

**Failed checks:**Row-level hash  
• Dimensions analyzed: 64 — ✓ pass  
• Metrics analyzed: 2 — ✓ pass  
• Row count: Control 747,109 / Stage 746,925 — mismatch  
• Row hash diffs: 84,832 — mismatch

There are a few dimensions (as tracked in the validations documentation tracker) that we KNOW are going to be mismatching because IVT compaction is needed.

- Traffic Type
- Bit Flag (specifically 1 \<\< 55 since there are some request\_flags that are set by the IVT Pipeline and thus the FORECAST bit is not set correctly)
- Client Facing IVT Reason Flag (similar to above; we're missing 1 bit flag from here that is set by the IVT pipeline)

The other remaining field that is mismatching, is `postal_code_package_ids` . We see a few postal code package ids MORE in Stage. This can be attributed to same root cause as above, NOT a separate issue.

When IVT compaction runs, it changes traffic\_type and bit\_flag for affected requests, shifting them to different dimension combos. This causes a small number of postal\_code\_package\_ids values to appear under different dimension combos in control vs. stage

**Metrics diff**

The other diff we see is ad\_requests. Even though the SUM of the ad\_requests is matching, when drilling down to the requests, we can see that:

Bit 55 (IVT flag) is being set in hoover\_compaction on some requests where the old request table did NOT set it, causing those rows to hash to a different bit\_flag dimension key. The same request appears in control with bit\_flag=X and in stage with bit\_flag=X+2^55, producing ±1 redistributions. Total sums are unaffected.

---

# 2026-04-07 → Hour 18

We know the both Bit Flag and Postal Code Package Ids are problematic and will be until the IVT Compaction Pipeline is up and running.

Let's see if the OTHER dimensions/ metrics are aligned.

  

  

---

# 2026-04-07 → Hour 14

## Discrepancies:

### Problematic Dimensions:

1. Bit Flag 
2. Postal Code Package Ids

### Problematic Metrics:

N/A

#### Dimensions deep dive:

##### Bit Flag:

Only in CONTROL (2 total): 612559922361794560, 612559918066827520

Double checking a specific transaction

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260408174529\_397842](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260408174529_397842)

We can see that in the old model, this transaction is FILTERED

However, in the new model:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260407201226\_470218](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260407201226_470218) (the flags are different)

The diff of the flags is 64

Talking to  , this is EXPECTED since the IVT Compaction pipeline is NOT running yet.

postbid ivt will also change request\_\_flags and add 64, could you check the corresponding records if the hoover request\_\_traffic\_type is 2

Since request\_traffic\_type is in fact 2, this is expected.

##### Postal Code Package IDs:

*Only in STAGE (4 total):* \[ 8932 11387 11395 11439 11463\], \[ 1993 10801 10804 11148 11210 11732\], \[ 4109 9623 9691 10386 10451 10452 11079 11170 11186 11212 11223 11320 11386 11394 11414 11415 11416 11427 11477 11486 11550 11608 11876 12080 12151 12280 12482 12488\], \[ 1993 10801 10803 11210 11845\]

Double checking one of the records:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260408182142\_246265&externalid=20260408\_183405\_00009\_uwku6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260408182142_246265&externalid=20260408_183405_00009_uwku6)

New model:

```
SELECT request.transaction_id, request, inventory.asset_chains, network.postal_code_package_ids
FROM fw1_prd.hoover_pipeline_streaming.hoover_stream
         lateral view explode(inventory.asset_chains) as network
WHERE date_trunc('hour', from_unixtime(request.timestamp)) = date_trunc('hour',  TIMESTAMP '2026-04-07 14:00:00')
  AND network.postal_code_package_ids = array(8932,11387,11395,11439,11463)
and coalesce (network.role, "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (network.role, "") = "D"
  and coalesce (network.network_id, cast (-1 as long)) = coalesce (network.content_owner_network_id , cast (-1 as long))) -- remove the D when D is the same as CRO
  and idx.is_first_request = true
AND stream_batch_id >= '20260407130000' and stream_batch_id < '20260407150000'
```

Returns:

  

We can see that the bit\_flag DIMENSION is different between the 2 records. Similar to above, BIT 55 (forecast) is NOT set.

We will re-evaluate this one when the IVT Compaction Pipeline is up and running.

  

  

  

---

# 2026-03-30 → Hour 17

## Discrepancies:

### Problematic Dimensions:

1. Bit Flag 
2. Postal Code Package Ids

### Problematic Metrics:

N/A

#### Dimensions deep dive:

##### Bit Flag:

*Only in CONTROL (2 total):* 612490099078463488, 612559918066827520

The missing bit\_flag is the forecast\_exclude bit flag. Let's rebuild the method and see.

##### Postal Code Package IDs:

Only in STAGE (3 total): 1993 10801 10804 10806 11155 11210\], \[ 4137 6613 9691 10386 10451 10452 10986 11079 11186 11212 11379 11386 11414 11415 11416 11427 11477 11486 11608 12080 12151 12280 12488 12583\], \[ 1993 10801 10803 11148 11210\]

STG is seeing more records because of unmasking. Let's remove unmasking and re-validate.

  

---

# 2026-03-20 → Hour 12

Given that the below discrepancies were caused by the splitting of the batches; I removed the `event_hour`  check from the compaction table and made the following SQL change to the hoover\_plus table to compare:

Change the sql:

  

```
and cast (request.timestamp as TIMESTAMP) >= to_timestamp(event_hour, 'yyyyMMddHHmmss') - interval '4' hours
AND event_hour >= date_format(date_trunc('hour', current_timestamp) - interval 4 hour, 'yyyyMMddHH000')
AND event_hour < date_format(date_trunc('hour', current_timestamp) - interval 3 hour, 'yyyyMMddHH000')
```

  

To this:

```
AND date_trunc('HOUR', cast(request.timestamp as timestamp)) = date_trunc('HOUR', current_timestamp) - interval '4' hours
```

  

Once changed, I re-ran the validation tool to see results and they look very promising.

## Discrepancies:

### Problematic Dimensions:

1. Traffic Type
2. Bit Flag (Inventory Network)
3. Airing ID
4. Client Facing IVT Reason Flag
5. Postal Code Package IDs
6. Slot Ad Unit IDs

### Problematic Metrics:

N/A

#### Dimensions deep dive:

##### Traffic Type (same as before):

ID: 2 is missing in Hoover++ while it is present in Hoover.

This is because `FILTER_BY_IVT_DETECTION`  check is missing in Hoover++.

<https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/RequestHandler.java#L290>

The above needs to be implemented in Hoover++.

##### Bit Flag (same as before):

We are missing the SAMPLED bit flag from request

Bit\_flags are NOT set for inventoryNetworks (in both old and new hoover)

##### Client Facing IVT Reason Flag (same as before):

Checked value: 1125899906842628

No results. Need to check with  or  if maybe a missing `bit_flag`  in `IVTHelper`

##### Airing ID (same as before):

This is a potential bug in `NetworkHandler` 

`INVALID_HYLDA_AIRING_ID`  is not being set

Need to check setFields method in NetworkHandler line 36

##### Postal Code Package IDs:

There are 3 missing values that are ONLY present in the stage table.

These can be attributed to different batching ways between current hoover and new Hoover++ model (details below)

##### Slot Ad Unit IDs:

Checked values: array(22201) and array(-1,1)

```

```

No results returned from streaming table. 

No results returned for values in control table either.

Potential bug in `RequestInfoHandler`  in `hoover-model` 

# Differences (in detail)

## Dimensions

###  Postal Code Package ID (3 Values Missing from CONTROL table)

Missing value:array(1993,10801,10804,11148,11157,11210,11221,11732)

```

```

#### Check the sampling table:

Event level table with a wider window of event\_date and process\_batch\_id

```
SELECT event_date, process_batch_id, postal_code_package_ids from hive_data_prd_dwh_etl.aggregate.f_process_request_hourly_sampling where event_date >= '2026-03-20 12:00:00' and event_date <= '2026-03-20 13:00:00' and process_batch_id >= 20260320120000 and process_batch_id <= 20260320130000 and postal_code_package_ids = array(1993,10801,10804,11148,11157,11210,11221,11732) group by 1,2,3;

--2026-03-20T13:00:00.000+00:00	20260320130000	[1993,10801,10804,11148,11157,11210,11221,11732]
```

  

We can see that this can be attributed to the split batch as well but the other way around this time. The current hoover model is splitting it to the next batch while our updated SQL is putting it in the previous batch.

### Slot Ad Unit ID (575 Values Missing)

#### Stage table missing values: (not present)

```
SELECT stream_batch_id,
    request_info.slot_video_cro_ad_unit_ids
from fw1_prd.hoover_pipeline_streaming.hoover_stream
where idx.is_first_request = true and
      stream_batch_id >= '20260320100000' and stream_batch_id < '20260320140000'
  and request_info.slot_video_cro_ad_unit_ids = array(22201)

-- no results
```

  

#### Control table missing values (not present)

```
SELECT event_date, process_batch_id, slot_ad_unit_ids from hive_data_prd_dwh_etl.aggregate.f_process_request_hourly_sampling where event_date >= '2026-03-20 11:00:00' and event_date <= '2026-03-20 13:00:00' and process_batch_id >= 20260320120000 and process_batch_id <= 20260320130000 and slot_ad_unit_ids = array(-1, 1) group by 1,2,3;

-- no results
```

  

  

Attachments

  

Validation email → 

Dimension value differences → 

Manual Analysis SQL → 

Row by Row differences → 

  

---

# 2026-03-17 → Hour 19

## Discrepancies:

### Problematic Dimensions:

1. Traffic Type
2. Bit Flag (Inventory Network)
3. Airing ID
4. Client Facing IVT Reason Flag
5. Slot Ad Unit IDs

### Problematic Metrics:

N/A

#### Dimensions deep dive:

Most of the dimension discrepancies can be attributed to how the batch splitting is working between old hoover and new hoover. 

Old hoover pipeline: In current logic, we put it into event\_hour 20260317190000, it seems correct, even though it’s different with the Flusher split batch.  can explain more.

New hoover pipeline → <https://github.freewheel.tv/data/hoover-pipeline/blob/master/hoover-pipeline-compaction/src/main/scala/tv/freewheel/reporting/compact/Compact.scala#L152C7-L154C33>

If you look at the `min`  and the `max`  stream\_batch\_id for a specific event\_hour:

```
select min(min_event_date) as start, max(max_event_date) as end from fw1_prd.hoover_pipeline_streaming.sub_batch_status where event_hour = '20260319200000'

-- 20260319200031	20260319210026
```

  

This means that anything BEFORE `20260319200031`  falls in event\_hour 19 and anything after `20260319210026`  falls in event\_hour 21

```
select distinct(event_hour) from fw1_prd.hoover_pipeline_streaming.sub_batch_status where min_event_date < '20260319200031'

-- 20260319180000
-- 20260319190000
```

  

Most of the below discrepancies can be explained by the above behavior. The splitting of the batches between the current hoover model and the new Hoover++ streaming mode is NOT the same. 

This leads to some records being in different "event hours" when looking at the output of the aggregated data for a given hour.

**In the below example if the `min`  was set to 20260317190027 and max was set to 20260317200103 we would capture similar data between the 2 models.**

##### Network ID:

ID 372464 is present in the batch: 20260317190027.

##### Content Owner ID:

ID 372464 is present in the batch: 20260317190027.

##### Distributor ID:

ID 372464 is present in the batch: 20260317190027.

##### Traffic Type:

ID: 2 is missing in Hoover++ while it is present in Hoover.

This is because `FILTER_BY_IVT_DETECTION`  check is missing in Hoover++.

<https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/RequestHandler.java#L290>

The above needs to be implemented in Hoover++.

##### Bit Flag:

We are missing the SAMPLED bit flag from request

Bit\_flags are NOT set for inventoryNetworks (in both old and new hoover)

##### Asset ID:

Checked asset IDs: 290420578, 409837636, 393341051, 391543446

Above checked values are available in the 20260317190038 batch.

##### Series ID:

Checked series IDs: 3154132, 1669357928, 1621963040

Above checked values are available in the 20260317200103 batch.

##### Asset Group IDs:

Checked asset group ID: \[363640063 363640075 363640103 363640132 363644622 363644626 363644632 363644979 363645005 363645018 363645032 363645675 363645771 363645889 363647181 363649942 363659455 363660058 363661108 363662623 363662724 363665810 363668392 389436091\]

Above checked value is available in the 20260317190027 batch.

##### Site ID:

Checked Site ID: 1266640

Above checked site\_id is available in the 20260317190027 batch.

##### Site Section Group IDs:

Checked site section group id: array(938841,938842,938850,938852,938853,938854,938856,938881,938898,1083443,1083444,1246063,1246065)

Above checked value is available in the 20260317200103 batch.

##### Airing ID:

This is a potential bug in `NetworkHandler` 

`INVALID_HYLDA_AIRING_ID`  is not being set

Need to check setFields method in NetworkHandler line 36

##### Channel ID:

Checked channel ID: 900632075

Above checked value is available in the 20260317190027 batch.

##### Postal Code:

Checked values: 38205, 1072 nx

Above checked values are available in the 20260317190038 batch

##### Postal Code Package IDs:

Checked postal code package id: array(6016,7064,8630,9790,11213,11412,11413,11621,11625,11769,11770,12182,12196,12345,12447,12576)

Above checked value available in the 20260317190038 batch.

##### User City ID:

Checked values: 57020

Above checked value is available in the 20260317190052 batch.

##### User State ID:

Checked values: 5354, 1169

Above checked values are available in the 20260317190038 batch.

##### User Country ID:

Checked value: 91

Above checked value is available in the 20260317190038 batch.

##### Profile ID:

Checked value: 9577

Above checked value is available in the 20260317190027 batch.

##### Client Facing IVT Reason Flag:

Checked value: 1125899906842628

No results. Need to check with  or  if maybe a missing `bit_flag`  in `IVTHelper`

##### Standard Endpoint ID:

Checked value: 1204

Above checked value is available in the 20260317190052 batch.

##### Video CRO Network ID:

Checked value: 372464

Above checked value is available in the 20260317190027 batch.

##### Request Context Network ID:

Checked value: 372464

Above checked value is available in the 20260317190027 batch.

##### Standard App ID:

Checked value: 8471

Above checked value is available in the 20260317190027 batch.

##### Standard Brand ID:

Checked values: 492, 10577

Above checked values are available in the 20260317190052 and 20260317190038 batches respectively.

##### Standard Programmer ID:

Checked values: 10576, 491

Above checked values are available in the 20260317190038 and 20260317190052 batches respectively.

##### Slot Ad Unit IDs:

Checked values: array(63789), array(1,52427)

No results returned from streaming table. Potential bug in `RequestInfoHandler`  in `hoover-model` 

##### Standard App Bundle ID:

Checked values: 25244, 90733

Above checked values are available in the 20260317190038 and 20260317190027 batches respectively.

##### Standard Site Domain ID:

Checked values: 1199407, 1134182

Above checked values are available in the 20260317190038 and 20260317200103 batches respectively.

#### Metrics (deep dive)

##### Ad Requests:

  

```
cast(1 as long) 
* coalesce(request.multiplier, cast(1 as long))
* coalesce(request.magnifier, cast(1 as long)) 
* coalesce(request.log_sampling.magnifier, cast(1 as long))                                          as ad_requests
```

In our control table: 1,576,224

In our stage table: 1,565,092

Difference: - 11,132 (-0.71%) negative means more in control.

These can also be attributed to the split batching difference between current Hoover and Hoover++ models.

# Differences (in detail)

## Dimensions

### Network ID (1 Value Missing)

Missing value: 372464

#### Control Table:

```
SELECT event_date, process_batch_id, network_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where network_id = 372464 group by 1,2,3;

--2026-03-17 19:00:00.000000000,20260317190000
```

  

#### Stage Table:

```
SELECT event_date, process_batch_id, network_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus where network_id = 372464 group by 1,2,3;

-- NO RESULTS
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.network_id as asset_chain_network
--      , site_section_chain_network.network_id as site_section_chain_network
--      , request.context.network_id as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317200000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.network_id = 372464

-- 20260317190027,372464
-- 20260317185346,372464
```

  

  

### Content Owner ID (1 Value Missing)

Missing value: 372464

#### Control Table:

```
SELECT event_date, process_batch_id, content_owner_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where content_owner_id = 372464 group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000
```

  

#### Stage Table:

```
SELECT event_date, process_batch_id, content_owner_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus where content_owner_id = 372464 group by 1,2,3;

-- NO RESULTS
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.content_owner_network_id as asset_chain_network
--      , site_section_chain_network.content_owner_network_id as site_section_chain_network
--      , request.context.content_owner_network_id as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317200000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.content_owner_network_id = 372464
 
-- 20260317190027,372464
-- 20260317185346,372464
```

  

  

### Distributor ID (1 Value Missing)

Missing value: 372464

#### Control Table:

```
SELECT event_date, process_batch_id, distributor_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where distributor_id = 372464 group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000
```

  

#### Stage Table:

```
SELECT event_date, process_batch_id, distributor_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hoover_plus where distributor_id = 372464 group by 1,2,3;

-- NO RESULTS
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.distributor_network_id as asset_chain_network
--      , site_section_chain_network.distributor_network_id as site_section_chain_network
--      , request.context.distributor_network_id as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317200000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.distributor_network_id = 372464
 
-- 20260317190027,372464
-- 20260317185346,372464
```

  

### Traffic Type (1 Value Missing)

Missing value: 2

Explanation below. Seems to be missing from Hoover++ code

### Bit Flag (All NETWORK values missing)

Missing Value(s): ALL

We are missing the SAMPLED bit flag from request

Bit\_flags are NOT set for inventoryNetworks (in both old and new hoover)

```
SELECT stream_batch_id, asset_chain_network.bit_flags as asset_chain_network
     , site_section_chain_network.bit_flags as site_section_chain_network
     , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317200000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO

-- site_section_chain
    and coalesce (site_section_chain_network.role, "") in ("CRO", "D")                -- only report for cro and d
  and not (inventory.asset_chains is not null and size (inventory.asset_chains) > 0
  and array_contains(inventory.asset_chains.network_id , coalesce (site_section_chain_network.network_id, cast (-1 as long))))
  and not (coalesce (site_section_chain_network.role  , "") = "D"
  and coalesce (site_section_chain_network.network_id  , cast (-1 as long)) = coalesce (site_section_chain_network.content_owner_network_id , cast (-1 as long))) -- remove the D when D is the same as CRO


-- 20260317195841,0,0,36046389205058048
-- 20260317195841,0,0,36046389205058048
```

  

### Asset ID (112 Value Missing)

Missing values (spot check): 290420578, 409837636, 393341051, 391543446

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.asset_id as asset_chain_network
--      , site_section_chain_network.asset_id as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317200000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.asset_id IN (290420578, 409837636, 393341051, 391543446)

 returns:
20260317182233,393341051
20260317190038,290420578
20260317190038,391543446
20260317190038,393341051
```

  

### Series ID (40 Value Missing)

Missing values (Spot Check): 3154132, 1669357928, 1621963040

#### Control Table:

```
SELECT event_date, process_batch_id, series_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where series_id IN (3154132, 1669357928, 1621963040) group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317200000,1621963040
-- 2026-03-17 19:00:00.000000000,20260317200000,3154132
-- 2026-03-17 19:00:00.000000000,20260317200000,1669357928
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.series_id as asset_chain_network
     , site_section_chain_network.asset_id as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.series_id IN (3154132, 1669357928, 1621963040)

-- 20260317200103,1669357928,463840805
-- 20260317200103,3154132,137217419
-- 20260317200103,3154132,203977784
-- 20260317200103,1621963040,459482340
-- 20260317180148,1669357928,462645169
-- 20260317203438,1669357928,462119902
```

  

### Asset Group IDs (75 Value Missing)

Missing value (spot check): \[363640063 363640075 363640103 363640132 363644622 363644626 363644632 363644979 363645005 363645018 363645032 363645675 363645771 363645889 363647181 363649942 363659455 363660058 363661108 363662623 363662724 363665810 363668392 389436091\]

#### Control Table:

```
SELECT event_date, process_batch_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where asset_group_ids = (array(363640063, 363640075, 363640103, 363640132, 363644622, 363644626, 363644632,363644979, 363645005, 363645018, 363645032, 363645675, 363645771, 363645889,363647181, 363649942, 363659455, 363660058, 363661108, 363662623, 363662724,363665810, 363668392, 389436091)) group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.asset_group_ids as asset_chain_network
--      , site_section_chain_network.asset_group_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.asset_group_ids = (array(363640063, 363640075, 363640103, 363640132, 363644622, 363644626, 363644632,
    363644979, 363645005, 363645018, 363645032, 363645675, 363645771, 363645889,
    363647181, 363649942, 363659455, 363660058, 363661108, 363662623, 363662724,
    363665810, 363668392, 389436091))

returns:
-- 20260317190027
```

  

### Site ID (10 Values Missing)

Missing value (spot check): 1266640

#### Control Table:

```
SELECT event_date, process_batch_id, site_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where site_id = 1266640 group by 1,2,3;

--2026-03-17 19:00:00.000000000,20260317190000,1266640
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.site_id as asset_chain_network
--      , site_section_chain_network.asset_group_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.site_id = 1266640

-- 20260317190027,1266640
```

  

### Site Section Group IDs (35 Value Missing)

Missing value (spot check): (938841,938842,938850,938852,938853,938854,938856,938881,938898,1083443,1083444,1246063,1246065)

#### Control Table:

```
SELECT event_date, process_batch_id, site_section_group_ids from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where site_section_group_ids = (array(938841,938842,938850,938852,938853,938854,938856,938881,938898,1083443,1083444,1246063,1246065)) group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317200000
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id, asset_chain_network.site_section_group_ids as asset_chain_network
--      , site_section_chain_network.asset_group_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

-- asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.site_section_group_ids = (array(938841,938842,938850,938852,938853,938854,938856,938881,938898,1083443,1083444,1246063,1246065))

20260317183040
20260317200103
20260317204808
20260317205448
20260317205113
20260317205518
```

  

### Airing ID (1 Value Missing)

Missing value: -2

Potential bug in `NetworkHandler`  for hoover-model.

<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/NetworkHandler.java#L438>

Need to check the `setFields`  method in NetworkHandler to see why `INVALID_HYLDA_AIRING_ID`  is not being set correctly.

### Channel ID (8 Values Missing)

Missing value (spot check): 900632075

#### Control Table:

```
SELECT event_date, process_batch_id, channel_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where channel_id = 900632075 group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000,900632075
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT
    stream_batch_id
     , asset_chain_network.airing_channel_id as asset_chain_network
--      , site_section_chain_network.airing_id as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

--asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.airing_channel_id = 900632075

-- 20260317190027,900632075
-- 20260317182317,900632075
```

  

### Postal Code (133 Values Missing)

Missing value(s) spot check: '38205', and '1072 nx'

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT
    stream_batch_id
, visitor.postal_code
--      , asset_chain_network.airing_channel_id as asset_chain_network
--      , site_section_chain_network.airing_id as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
    and visitor.postal_code = '38205'

-- 20260317181308,38205
-- 20260317190038,38205
-- 20260317203305,38205

SELECT
    stream_batch_id
, visitor.postal_code
--      , asset_chain_network.airing_channel_id as asset_chain_network
--      , site_section_chain_network.airing_id as site_section_chain_network
--      , request.bit_flags as request_context_network
from fw1_prd.hoover_pipeline_streaming.hoover_stream
lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
where idx.is_first_request = true
and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
    and visitor.postal_code = "1072 nx"

-- 20260317190038,1072 nx
```

  

### Postal Code Package IDs (86 Values Missing)

Missing values (spot check): array(6016,7064,8630,9790,11213,11412,11413,11621,11625,11769,11770,12182,12196,12345,12447,12576)

#### Control Table:

```
SELECT event_date, process_batch_id, postal_code_package_ids from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where postal_code_package_ids = array(6016,7064,8630,9790,11213,11412,11413,11621,11625,11769,11770,12182,12196,12345,12447,12576) group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
--      , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'

--asset_chain
and coalesce (asset_chain_network.role , "") in ("CRO", "D")                -- only report for cro and d
  and not (coalesce (asset_chain_network.role, "") = "D"
  and coalesce (asset_chain_network.network_id, cast (-1 as long)) = coalesce (asset_chain_network.content_owner_network_id, cast (-1 as long))) -- remove the D when D is the same as CRO
    and asset_chain_network.postal_code_package_ids =  array(6016,7064,8630,9790,11213,11412,11413,11621,11625,11769,11770,12182,12196,12345,12447,12576)

-- 20260317190038
```

  

### User City ID (74 Values Missing)

Missing value (spot check): 57020

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, visitor.city_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and visitor.city_id IN (57020)

-- 20260317184115
-- 20260317190052
```

  

### User State ID (2 Values Missing)

Missing value: 5354, 1169

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, visitor.state_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317190000' and stream_batch_id < '20260317200000'
                                           and visitor.state_id IN (5354,1169)


-- 20260317190038
-- 20260317190038
```

  

### User Country ID (1 Value Missing)

Missing value: 91:

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, visitor.country_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and visitor.country_id IN (91)

-- 20260317180842
-- 20260317190038
```

  

### Profile ID (5 Values Missing)

Missing value (spot check): 9577

#### Control Table:

#### Stage Table:

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.profile_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.profile_id IN (9577)

-- 20260317190027
```

  

### Client Facing IVT Reason Flag (1 Value Missing)

Missing value: 1125899906842628

#### Not present in streaming table.

Check with Rounan/ Anran on this. Maybe a missing bit\_flag in `IVTHelper` ?

### Standard Endpoint ID (1 Value Missing)

Missing value: 1204

#### Control Table:

```
SELECT event_date, process_batch_id, standard_endpoint_id from fw1_stg.kbhargava_prd_test.f_process_request_hourly_hive where standard_endpoint_id = 1204 group by 1,2,3;

-- 2026-03-17 19:00:00.000000000,20260317190000,1204
```

  

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_endpoint_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_endpoint_id IN (1204)

-- 20260317204349,1204
-- 20260317190052,1204
```

  

### Video CRO Network ID (1 Value Missing)

Missing value: 372464

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.video_cro_network_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.video_cro_network_id IN (372464)
-- 20260317185346,372464
-- 20260317190027,372464
 
```

  

### Request Context Network ID (1 Value Missing)

Missing value: 372464

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.network_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.network_id IN (372464)
-- 20260317185346,372464
-- 20260317190027,372464
```

  

### Standard App ID (4 Values Missing)

Missing value (spot check): 8471

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_app_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_app_id IN (8471)

-- 20260317190027, 8471
```

  

### Standard Brand ID (2 Values Missing)

Missing value: 492, 10577

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_brand_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_brand_id IN (492, 10577)
-- 20260317190038,10577
-- 20260317190052,492
-- 20260317203517,10577
-- 20260317203653,10577
```

  

### Standard Programmer ID (2 Values Missing)

Missing value: 491, 10576

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_programmer_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_programmer_id IN (491, 10576)
-- 20260317182637,491
-- 20260317184257,491
-- 20260317190038,10576
-- 20260317190052,491
-- 20260317201039,491
-- 20260317203517,10576
-- 20260317203653,10576
-- 20260317205327,491
```

  

### Slot Ad Unit IDs (653 Values Missing)

Missing value (spot check): array(63789), array(1,52427)

#### No results (in streaming table)

Potential bug with `request_info` ?

<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/RequestInfoHandler.java>

### Standard App Bundle ID (5 Values Missing)

Missing value (spot check): 25244, 90733

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_app_bundle_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_app_bundle_id IN (25244, 90733)

-- 20260317190027,90733
-- 20260317190038,25244
```

  

### Standard Site Domain ID (7 Value Missing)

Missing value(s) spot check: 1199407, 1134182

#### Check the non-compaction table:

Event level table with a wider window of `stream_batch_id` 

```
SELECT stream_batch_id
, request.context.standard_site_domain_id
--       , asset_chain_network.postal_code_package_ids as asset_chain_network
--      , site_section_chain_network.postal_code_package_ids as site_section_chain_network
--      , request.bit_flags as request_context_network
                                       from fw1_prd.hoover_pipeline_streaming.hoover_stream
                                                lateral view explode(inventory.asset_chains) as asset_chain_network
lateral view explode(inventory.site_section_chains) as site_section_chain_network
                                       where idx.is_first_request = true
                                         and stream_batch_id >= '20260317180000' and stream_batch_id < '20260317210000'
                                           and request.context.standard_site_domain_id IN (1199407, 1134182)

-- 20260317190038,1199407
-- 20260317200103,1134182
```

  

  

  

# Questions?

 

  

# Attachments

Validation email → 

Dimension differences → 

Manual Analysis SQL → 

Row by row differences → 

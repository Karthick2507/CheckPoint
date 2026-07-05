# f\_sa\_auction\_hourly

- Hoover sql: [https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f\_sa\_auction\_hourly.sql](https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f_sa_auction_hourly.sql)
- Hoover++ sql: [https://github.freewheel.tv/data/hoover-model/blob/master/validation\_sqls/transformer\_tables/hoover\_streaming\_src/f\_sa\_auction\_hourly\_h%2B%2B.sql](https://github.freewheel.tv/data/hoover-model/blob/master/validation_sqls/transformer_tables/hoover_streaming_src/f_sa_auction_hourly_h%2B%2B.sql)
- Please check the tracker here: [Discrepancy Tracker](https://freewheel.atlassian.net)
- Validations tracker → [Hoover Validations Documentation Tracker](https://freewheel.atlassian.net/wiki/pages/viewpage.action?spaceKey=Infrastructure&title=Hoover+Validations+Documentation+Tracker)

Below is validation results for f\_sa\_auction\_hourly, comparing data from current hoover model and the new H++ output of the same table.

  

---

# Validations

## Round 1

### 2026-04-23 → Hour 15

**📋 SUMMARY**  
• **Failed checks:**Dimension values, Row-level hash  
• Dimensions analyzed: 89 — differences found  
• Metrics analyzed: 3 — ✓ pass  
• Row count: Control 2,374,711 / Stage 2,374,734 — mismatch  
• Row hash diffs: 4,749,445 — mismatch

## Dimension diffs

3 dimensions have value-level mismatches.

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **bit\_flag** | 83 | 72 | 83 | 72 |
| **outbound\_order\_ids** | 1332 | 1335 | 4 | 7 |
| **reseller\_id** | 177 | 177 | 1 | 1 |

## Fixes

**Bit Flag**

Need to add SAMPLED bit flag for the auction pipeline as well.

**Outbound Order Ids**

Getting the value without the `has` check returns the default value of 0 for this field. All STAGE outbound\_order\_ids have an extra 0 as the initial values

**Reseller Id**

We're doing an unnecessary unmasking which is adding `-1` in the reseller\_id field. Otherwise, it should be `0`

**PR**

<https://github.freewheel.tv/data/hoover-model/pull/305>

  

## Questions?

 

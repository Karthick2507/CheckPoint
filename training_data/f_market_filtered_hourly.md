# f\_market\_filtered\_hourly

### New Diffs

There are no new diffs that exist that are not already known.

---

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_filtered\_hourly**

  
**Environment:** STG  |  **Date:** 2026-07-18  |  **Hour:** 08  
**Control table:** `fw1_stg.slogan313.f_market_filtered_hourly_control`  
**Stage table:** `fw1_stg.slogan313.f_market_filtered_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Row-level hash
- Dimensions analyzed: 39 — differences found
- Metrics analyzed: 1 — ✓ pass
- Row count: Control 155,714 / Stage 155,649 — mismatch
- Row hash diffs: 849 — mismatch

---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **bit\_flag** | 45 | 43 | 2 | 0 |

**Sample Values (first 5 dimensions with differences):**

**bit\_flag:**  
*Only in CONTROL (2 total):* 612490099078463488, 612489549322649600

**✓ All metric sums match!**

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 155,714, Stage: 155,649, Diff: -65) |
| **Row Hash** | **MISMATCH** (Only in Control: 457, Only in Stage: 392) |

---

**🔬 COLUMN-LEVEL DIFF — 65 combos with metric diffs**

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=119662702, series_id=914489941...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=2.0000, stg=4.0000, +2.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=8.0000, stg=11.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=8.0000, stg=11.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=476038887, series_id=957619711...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=21.0000, stg=22.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=4.0000, stg=7.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=3.0000, stg=7.0000, +4.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=8.0000, stg=11.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=1.0000, stg=3.0000, +2.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=8.0000, stg=11.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=4.0000, stg=7.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=20.0000, stg=21.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=2.0000, stg=5.0000, +3.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=2.0000, stg=4.0000, +2.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=4.0000, stg=5.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=2.0000, stg=6.0000, +4.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=119662702, series_id=914489941...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=3.0000, stg=4.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=21.0000, stg=22.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=19.0000, stg=20.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=19.0000, stg=20.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=475647965, series_id=31228274...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=506334, asset_id=115190714, series_id=11209193...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=4.0000, stg=5.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=3.0000, stg=7.0000, +4.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=3.0000, stg=7.0000, +4.0000 |
| `date=2026-07-18, hour=08, network_id=144750, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=507282, asset_id=-1, series_id=-1...` | **filter\_bid\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |

### Hoover

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715072102\_379104&externalid=GATEWAY\_PENDING\_386801686](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715072102_379104&externalid=GATEWAY_PENDING_386801686)

### Hoover++ (View)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715083310\_369018](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715083310_369018)

### Hoover++ (Transaction)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715081757\_160832&externalid=20260715\_082103\_00084\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715081757_160832&externalid=20260715_082103_00084_a6c4k)

Note: I have included the idx\_\_is\_first\_request which reduced the % diff. The summary was taken without the idx\_\_is\_first\_request. Will update the summary with first\_request.

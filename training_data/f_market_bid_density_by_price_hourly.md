# f\_market\_bid\_density\_by\_price\_hourly

## New Diffs

Below list is all diffs that need further investigation (unknown diffs)

|  |  **Column Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | `_in_played_slot`metrics | YES | IVT RELATED | As shown below, the traffic\_type is different hence the overcount in Hoover++. This is an expected diff. |

---

### Differences

#### Metrics Difference

| **Column Name** | **Differences** | **Reason** |
| --- | --- | --- |
| selected\_ads\_in\_played\_slot | Control : 46,233.00Stage : 46,235.00Diff: 2% Diff : 0.00 | Reason is due to ack traffic type. (Known Issue)In L3 query, we have a filter condition [ack traffic type = 0](https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f_market_bid_density_by_price_hourly.sql#L148) because of this filter some records are filtered in hoover but became available in h++Hoover :  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260723083934\_693552](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260723083934_693552)Hoover ++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260723085119\_442649](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260723085119_442649) |
| selected\_ads\_in\_played\_slot\_primary | Control : 46,233.00Stage : 46,235.00Diff: 2% Diff : 0.00 | Same as the above |
|  |  |  |

### Report

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_bid\_density\_by\_price\_hourly**  
**Environment:** STG  |  **Date:** 2026-07-22  |  **Hour:** 08  
**Control table:**`fw1_stg.ns319.f_market_bid_density_by_price_hourly_control`  
**Stage table:**`fw1_stg.ns319.f_market_bid_density_by_price_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Metric sums, Row-level hash
- Dimensions analyzed: 18 — ✓ pass
- Metrics analyzed: 20 — differences found
- Row count: Control 110,273 / Stage 110,273 — ✓ match
- Row hash diffs: 2 — mismatch


**✓ All dimension values match!**

---

**📊 METRIC SUM DIFFERENCES**  

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **selected\_ads\_in\_played\_slot** | 46,233.00 | 46,235.00 | +2.00 | +0.00% |
| **selected\_ads\_in\_played\_slot\_primary** | 44,556.00 | 44,558.00 | +2.00 | +0.00% |



---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**  

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | ✓ Match (110,273 rows) |
| **Row Hash** | **MISMATCH** (Only in Control: 1, Only in Stage: 1) |



---

**🔬 COLUMN-LEVEL DIFF — 1 combos with metric diffs**  

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-07-22, hour=08, network_id=520040, integration_type=OPENRTB_NORMAL, site_section_id=16519712...` | **selected\_ads\_in\_played\_slot\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 **selected\_ads\_in\_played\_slot\_primary\_sum**: ctrl=0.0000, stg=2.0000, +2.0000 |

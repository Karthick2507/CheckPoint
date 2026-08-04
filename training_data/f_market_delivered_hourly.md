# f\_market\_delivered\_hourly



### New Diffs

There are no new diffs that exist that are not already known.

---

### Differences

#### Dimension 

| **Column Name** | **Differences** | **Reason** |
| --- | --- | --- |
| bit\_flag | *Only in CONTROL (17 total):* 738665140073023520, 576465150383753248, 738665140039452704, 738665140039450656, 738665140039469088, 630579298738372640, 738665140073007136, 612564316147435552, 612564316113356832, 576536068884267040 ... (+ 7 more, see CSV) *Only in STAGE (20 total):* 2900392961211369504, 2882378528309643296, 2900392961210861600, 2882379078063882272, 2882378528308070432, 2882378528308594720, 2918407325327034400, 2882308159597447200, 594549952001345568, 2882378528341641248 ... (+ 10 more, see CSV) | Its known issue.BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED is not set for partners in hoover++Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710155401\_096082&externalid=20260710\_155405\_00052\_nxf5d](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710155401_096082&externalid=20260710_155405_00052_nxf5d) Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710160619\_105286&externalid=20260710\_161536\_00063\_nxf5d](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710160619_105286&externalid=20260710_161536_00063_nxf5d) |
| postal\_code\_package\_id | *Only in STAGE (4 total):* \[3842 6329 6586\], \[3818 5644 6339 6580 6586 7054 8207 9324\], \[3859 5644 6336 6580\], \[3841 6339 6580\] | It’s known issue. Hoover → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260706111554\_140481&externalid=20260706\_111606\_00000\_t6rqw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260706111554_140481&externalid=20260706_111606_00000_t6rqw) Hoover++ → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260706155209\_047895&externalid=20260706\_155819\_00000\_nwau7](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260706155209_047895&externalid=20260706_155819_00000_nwau7)Karan has ticket to fix this issue |
| bit\_flag\_aim\_product\_category | *Only in CONTROL (1 total):* 20 | Its known issue.BIT\_FLAG\_AIM\_AUDIENCE\_EXTENSION\_USED is not set for partners in hoover++Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710155401\_096082&externalid=20260710\_155405\_00052\_nxf5d](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710155401_096082&externalid=20260710_155405_00052_nxf5d) Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710160619\_105286&externalid=20260710\_161536\_00063\_nxf5d](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710160619_105286&externalid=20260710_161536_00063_nxf5d) |

#### Metrics

Overall sum is matching for all the metrics 

Column level Metric Difference 

| **Metric Difference** | **Reason** |
| --- | --- |
| **impression\_primary\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **vtr\_0\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **vtr\_25\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **vtr\_50\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **vtr\_75\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 **vtr\_100\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 **measured\_revenue\_ssp\_sum**: ctrl=0.0000, stg=0.0077, +0.0077 **measured\_revenue\_dsp\_sum**: ctrl=0.0000, stg=0.0088, +0.0088 **measured\_revenue\_corp\_usd\_sum**: ctrl=0.0000, stg=0.0088, +0.0088 **measured\_revenue\_corp\_eur\_sum**: ctrl=0.0000, stg=0.0077, +0.0077 **raw\_revenue\_ssp\_sum**: ctrl=0.0000, stg=0.0077, +0.0077 **run\_revenue\_usd\_discounted\_sum**: ctrl=0.0000, stg=0.0088, +0.0088 | It’s known issue. (Profile id bug)Hoover → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710065849\_181970&externalid=20260710\_065858\_00000\_wdsuh](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710065849_181970&externalid=20260710_065858_00000_wdsuh)Hoover++ → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713065118\_938299](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713065118_938299) |

### Report

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_delivered\_hourly**  
**Environment:** STG  |  **Date:** 2026-07-12  |  **Hour:** 08  
**Control table:** `fw1_stg.ns319.f_market_delivered_hourly_control`  
**Stage table:** `fw1_stg.ns319.f_market_delivered_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Row-level hash
- Dimensions analyzed: 81 — differences found
- Metrics analyzed: 22 — ✓ pass
- Row count: Control 28,039 / Stage 28,039 — ✓ match
- Row hash diffs: 534 — mismatch


---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*  

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **bit\_flag** | 126 | 111 | 18 | 3 |
| **bit\_flag\_aim\_product\_category** | 3 | 2 | 1 | 0 |



**Sample Values (first 5 dimensions with differences):**

**bit\_flag:**  
*Only in CONTROL (18 total):* 738665140073023520, 612564316118059040, 738665140039452704, 630578748982560800, 1026895516224735264, 612493947369162784, 738665140039469088, 738665140073007136, 774623568347808288, 612494497124974624 ... (+ 8 more, see CSV)  
*Only in STAGE (3 total):* 630508380271952416, 594549952001345568, 576535519094376736

**bit\_flag\_aim\_product\_category:**  
*Only in CONTROL (1 total):* 20

**✓ All metric sums match!**

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**  

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | ✓ Match (28,039 rows) |
| **Row Hash** | **MISMATCH** (Only in Control: 267, Only in Stage: 267) |

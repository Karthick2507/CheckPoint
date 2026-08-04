# f\_market\_selected\_hourly

### New Diffs

No such list exists; all diffs are known diffs.

---

**From: **<notifier.ecs@freewheel.tv> \<<notifier.ecs@freewheel.tv>\>  
**Date: **Sunday, 12 July 2026 at 9:47 AM  
**To: **Murugesan, Sureshpandiyan \<<SureshpandiyanM@freewheel.com>\>  
**Subject: **⚠️ \[STG\] VALIDATION FAILED - f\_market\_selected\_hourly - 2026-07-01 @ 08:00

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_selected\_hourly**  
**Environment:** STG  |  **Date:** 2026-07-01  |  **Hour:** 08  
**Control table:** `fw1_stg.suresh.f_market_selected_hourly_control`  
**Stage table:** `fw1_stg.suresh.f_market_selected_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Row-level hash
- Dimensions analyzed: 61 — differences found
- Metrics analyzed: 15 — ✓ pass
- Row count: Control 197,128 / Stage 197,358 — mismatch
- Row hash diffs: 31,598 — mismatch

---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **bit\_flag** | 196 | 214 | **21** | **39** |
| **bit\_flag\_aim\_product\_category** | 5 | 4 | **1** | **0** |
| **matched\_contextual\_segment\_ids** | 1 | 15 | **0** | **14** |



**Sample Values (first 5 dimensions with differences):**

**bit\_flag: --Know difference**  
*Only in CONTROL (21 total):* 738665140073023520, 576465150383753248, 738665140039452704, 738665140039450656, 738665140039469088, 630579298738372640, 612559918100922368, 594549951997691936, 738665140073007136, 612559918066843648 ... (+ 11 more, see CSV)  
*Only in STAGE (39 total):* 2900392961211369504, 2882378528309643296, 2900392961177307168, 2882374680051449856, 2882374130262097920, 2882303761551458304, 2900392961210861600, 2882374130261557248, 2882308159564417056, 2882303761550934016 ... (+ 29 more, see CSV)  
--Expected Mismatches

**bit\_flag\_aim\_product\_category:**  
*Only in CONTROL (1 total):* 20 --Expected mismatches

**matched\_contextual\_segment\_ids:**  
*Only in STAGE (14 total):* \[25240\], \[25228\], \[25222\], \[25242\], \[25309\], \[25240 25241\], \[25319\], \[25258\], \[25227\], \[25256\] ... (+ 4 more, see CSV)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713085947\_639053&externalid=20260713\_085953\_00046\_pwixy](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713085947_639053&externalid=20260713_085953_00046_pwixy)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260713115409\_434640&externalid=20260713\_115641\_00082\_pwixy](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260713115409_434640&externalid=20260713_115641_00082_pwixy)

**✓ All metric sums match!**

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 197,128, Stage: 197,358, Diff: +230) |
| **Row Hash** | **MISMATCH** (Only in Control: 15,684, Only in Stage: 15,914) |


---

**🔬 COLUMN-LEVEL DIFF — 163 combos with metric diffs**

BitFlag Difference: – Know Difference

Hoover:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714120604\_431208&externalid=20260714\_120606\_00006\_5btys](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714120604_431208&externalid=20260714_120606_00006_5btys)

Hoover++:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714114422\_558097](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714114422_558097)

Traffic Type Difference: – Know Difference

`asset_id=410523752`:

Hoover:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715081734\_677989&externalid=20260715\_081736\_00083\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715081734_677989&externalid=20260715_081736_00083_a6c4k)

Hoover++:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715091810\_699959&externalid=20260715\_092119\_00109\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715091810_699959&externalid=20260715_092119_00109_a6c4k)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715091803\_320856&externalid=20260715\_092119\_00110\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715091803_320856&externalid=20260715_092119_00110_a6c4k)

`asset_id=180011665`:

Hoover:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260716054144\_987227&externalid=20260716\_054146\_00061\_v3dm3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260716054144_987227&externalid=20260716_054146_00061_v3dm3)

Hoover++:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260716054218\_028452&externalid=20260716\_054535\_00063\_v3dm3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260716054218_028452&externalid=20260716_054535_00063_v3dm3)

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=894.0000, stg=902.0000, +8.0000 **bid\_pre\_filtered\_sum**: ctrl=894.0000, stg=902.0000, +8.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 **bid\_pre\_filtered\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **received\_bid\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **resolved\_bid\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **total\_received\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **total\_resolved\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **demand\_total\_received\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=317.0000, stg=332.0000, +15.0000 **bid\_pre\_filtered\_sum**: ctrl=317.0000, stg=332.0000, +15.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=470611144, series_id=-1...` | **error\_frequency\_sum**: ctrl=19.0000, stg=21.0000, +2.0000 **bid\_pre\_filtered\_sum**: ctrl=19.0000, stg=21.0000, +2.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=894.0000, stg=902.0000, +8.0000 **bid\_pre\_filtered\_sum**: ctrl=894.0000, stg=902.0000, +8.0000 |
| `date=2026-07-01, hour=08, network_id=523319, asset_id=-1, series_id=-1...` | **error\_frequency\_sum**: ctrl=90.0000, stg=92.0000, +2.0000 **received\_bid\_sum**: ctrl=90.0000, stg=92.0000, +2.0000 **resolved\_bid\_sum**: ctrl=90.0000, stg=92.0000, +2.0000 **total\_received\_bid\_price\_sum**: ctrl=13.0356, stg=13.0856, +0.0500 **total\_resolved\_bid\_price\_sum**: ctrl=13.0356, stg=13.0856, +0.0500 **demand\_total\_received\_bid\_price\_sum**: ctrl=13.0356, stg=13.0856, +0.0500 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=13.0356, stg=13.0856, +0.0500 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473964680, series_id=25140647...` | **error\_frequency\_sum**: ctrl=9.0000, stg=8.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=9.0000, stg=8.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=8.0000, stg=4.0000, -4.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=4.0000, -4.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=6.0000, stg=5.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=6.0000, stg=5.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=50.0000, stg=47.0000, -3.0000 **bid\_pre\_filtered\_sum**: ctrl=50.0000, stg=47.0000, -3.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960020, series_id=25140647...` | **error\_frequency\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473964680, series_id=25140647...` | **error\_frequency\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 **received\_bid\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 **resolved\_bid\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 **total\_received\_bid\_price\_sum**: ctrl=54.0000, stg=36.0000, -18.0000 **total\_resolved\_bid\_price\_sum**: ctrl=54.0000, stg=36.0000, -18.0000 **demand\_total\_received\_bid\_price\_sum**: ctrl=54.0000, stg=36.0000, -18.0000 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=54.0000, stg=36.0000, -18.0000 |
| `date=2026-07-01, hour=08, network_id=524918, asset_id=392917340, series_id=926999042...` | **error\_frequency\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 **bid\_pre\_filtered\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=35.0000, stg=33.0000, -2.0000 **bid\_pre\_filtered\_sum**: ctrl=35.0000, stg=33.0000, -2.0000 |
| `date=2026-07-01, hour=08, network_id=524918, asset_id=392917340, series_id=926999042...` | **error\_frequency\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473977609, series_id=18698782...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=35.0000, stg=33.0000, -2.0000 **bid\_pre\_filtered\_sum**: ctrl=35.0000, stg=33.0000, -2.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 **bid\_pre\_filtered\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473963676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=20.0000, stg=19.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=20.0000, stg=19.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=8.0000, stg=4.0000, -4.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=4.0000, -4.0000 |
| `date=2026-07-01, hour=08, network_id=524918, asset_id=473980870, series_id=1642291487...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **received\_bid\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **resolved\_bid\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **selected\_primary\_bid\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **total\_received\_bid\_price\_sum**: ctrl=91.3400, stg=45.6700, -45.6700 **total\_resolved\_bid\_price\_sum**: ctrl=91.3400, stg=45.6700, -45.6700 **total\_bid\_won\_price\_sum**: ctrl=91.3395, stg=45.6698, -45.6698 **demand\_total\_received\_bid\_price\_sum**: ctrl=9.4040, stg=4.7020, -4.7020 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=9.4040, stg=4.7020, -4.7020 **demand\_total\_bid\_won\_price\_sum**: ctrl=9.4040, stg=4.7020, -4.7020 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473977609, series_id=18698782...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 **bid\_pre\_filtered\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=317.0000, stg=332.0000, +15.0000 **bid\_pre\_filtered\_sum**: ctrl=317.0000, stg=332.0000, +15.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 **bid\_pre\_filtered\_sum**: ctrl=10.0000, stg=5.0000, -5.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473977609, series_id=18698782...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 **bid\_pre\_filtered\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=462293182, series_id=1652230728...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=405661393, series_id=1028175179...` | **error\_frequency\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 **bid\_pre\_filtered\_sum**: ctrl=15.0000, stg=16.0000, +1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960020, series_id=25140647...` | **error\_frequency\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **received\_bid\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **resolved\_bid\_sum**: ctrl=5.0000, stg=4.0000, -1.0000 **total\_received\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **total\_resolved\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **demand\_total\_received\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=90.0000, stg=72.0000, -18.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473977609, series_id=18698782...` | **error\_frequency\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=523319, asset_id=-1, series_id=-1...` | **selected\_bid\_in\_watched\_slot\_primary\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=524918, asset_id=392917340, series_id=926999042...` | **error\_frequency\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=3.0000, stg=2.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473960676, series_id=25140647...` | **error\_frequency\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=8.0000, stg=7.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=523319, asset_id=-1, series_id=-1...` | **error\_frequency\_sum**: ctrl=2.0000, stg=5.0000, +3.0000 **received\_bid\_sum**: ctrl=2.0000, stg=5.0000, +3.0000 **resolved\_bid\_sum**: ctrl=2.0000, stg=5.0000, +3.0000 **total\_received\_bid\_price\_sum**: ctrl=31.8645, stg=81.3645, +49.5000 **total\_resolved\_bid\_price\_sum**: ctrl=31.8645, stg=81.3645, +49.5000 **demand\_total\_received\_bid\_price\_sum**: ctrl=31.8645, stg=81.3645, +49.5000 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=31.8645, stg=81.3645, +49.5000 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=512116, asset_id=180011665, series_id=-1...` | **error\_frequency\_sum**: ctrl=11.0000, stg=9.0000, -2.0000 **received\_bid\_sum**: ctrl=11.0000, stg=9.0000, -2.0000 **resolved\_bid\_sum**: ctrl=11.0000, stg=9.0000, -2.0000 **selected\_primary\_bid\_sum**: ctrl=11.0000, stg=9.0000, -2.0000 **total\_received\_bid\_price\_sum**: ctrl=143.0010, stg=117.0008, -26.0002 **total\_resolved\_bid\_price\_sum**: ctrl=143.0010, stg=117.0008, -26.0002 **total\_bid\_won\_price\_sum**: ctrl=143.0000, stg=117.0000, -26.0000 **demand\_total\_received\_bid\_price\_sum**: ctrl=143.0010, stg=117.0008, -26.0002 **demand\_total\_resolved\_bid\_price\_sum**: ctrl=143.0010, stg=117.0008, -26.0002 **demand\_total\_bid\_won\_price\_sum**: ctrl=143.0010, stg=117.0008, -26.0002 |
| `date=2026-07-01, hour=08, network_id=520311, asset_id=410523752, series_id=1115082970...` | **error\_frequency\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-07-01, hour=08, network_id=516429, asset_id=473964680, series_id=25140647...` | **error\_frequency\_sum**: ctrl=9.0000, stg=8.0000, -1.0000 **bid\_pre\_filtered\_sum**: ctrl=9.0000, stg=8.0000, -1.0000 |


*Showing 50 of 163 — see CSV.*

---

**📎 ATTACHMENTS:**

1. **row\_differences.csv**: Complete row-level differences (up to 1000 rows each direction)
2. **dimension\_value\_differences.csv**: All actual different values for each dimension
3. **column\_level\_diff.csv**: Per-dimension-combo metric diffs (163 combos)
4. **manual\_analysis.sql**: Additional SQL queries for deeper investigation



# After Removing the bit\_Flag, bit\_flag\_aim\_product\_category, matched\_contextual\_segment\_ids, traffic\_type

**From: **<notifier.ecs@freewheel.tv> \<<notifier.ecs@freewheel.tv>\>  
**Date: **Thursday, 16 July 2026 at 12:50 PM  
**To: **Murugesan, Sureshpandiyan \<<SureshpandiyanM@freewheel.com>\>  
**Subject: **⚠️ \[STG\] VALIDATION FAILED - f\_market\_selected\_hourly - 2026-07-01 @ 08:00  

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_selected\_hourly**  
**Environment:** STG  |  **Date:** 2026-07-01  |  **Hour:** 08  
**Control table:** `fw1_stg.suresh.f_market_selected_hourly_control`  
**Stage table:** `fw1_stg.suresh.f_market_selected_hourly_stage`  

---

**📋 SUMMARY**

- **Failed checks:** Row-level hash
- Dimensions analyzed: 57 — ✓ pass
- Metrics analyzed: 15 — ✓ pass
- Row count: Control 192,997 / Stage 192,997 — ✓ match
- Row hash diffs: 2 — mismatch


**✓ All dimension values match!**

**✓ All metric sums match!**  

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | ✓ Match (192,997 rows) |
| **Row Hash** | **MISMATCH** (Only in Control: 1, Only in Stage: 1) |


---

**🔬 COLUMN-LEVEL DIFF — 1 combos with metric diffs**

| Dims | Metric Diffs |
| --- | --- |


---

**📎 ATTACHMENTS:**

1. **row\_differences.csv**: Complete row-level differences (up to 1000 rows each direction)
2. **dimension\_value\_differences.csv**: All actual different values for each dimension
3. **column\_level\_diff.csv**: Per-dimension-combo metric diffs (1 combos)
4. **manual\_analysis.sql**: Additional SQL queries for deeper investigation

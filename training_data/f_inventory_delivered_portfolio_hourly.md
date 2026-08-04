# f\_inventory\_delivered\_portfolio\_hourly






## New Diffs

Below list is all diffs that need further investigation (unknown diffs)

|  | **Column Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | channel\_id | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |
| 2 | postal\_code | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |
| 3 | postal\_code\_package\_ids | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |
| 4 | user\_city\_id | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |
| 5 | operator\_zone\_id | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |
| 6 | avails | YES | IVT RELATED | `traffic_type indicates ivt status (0: valid, 1:invalid-marked in prebid, 2:invalid-marked in postbid). the possible IVT diff comes from postbid ivt, because it is using different data between hoover and hoover++. so it means there may be some ivt traffic(traffic_type=2) in the current hoover being marked as valid(traffic_type=0) in h++ or the other way round. This may lead to differences in the ack table/ view for different dimensions/ metrics` |

---

 **⚠️ \[STG\] VALIDATION FAILED - f\_inventory\_delivered\_portfolio\_hourly**

  
**Environment:** STG  |  **Date:** 2026-07-24  |  **Hour:** 08  
**Control table:** `fw1_stg.slogan313.f_inventory_delivered_portfolio_hourly_control`  
**Stage table:** `fw1_stg.slogan313.f_inventory_delivered_portfolio_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Metric sums, Row-level hash
- Dimensions analyzed: 49 — differences found
- Metrics analyzed: 2 — differences found
- Row count: Control 2,744,841 / Stage 2,769,789 — mismatch
- Row hash diffs: 5,514,630 — mismatch

---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **bit\_flag** | 639 | 563 | 80 | 4 |
| **channel\_id** | 5824 | 5890 | 0 | 66 |
| **postal\_code** | 39448 | 39450 | 0 | 2 |
| **postal\_code\_package\_ids** | 37777 | 37778 | 0 | 1 |
| **user\_city\_id** | 25762 | 25765 | 0 | 3 |
| **operator\_zone\_id** | 857 | 858 | 0 | 1 |
| **geo\_visibility** | 1 | 1 | 1 | 1 |

**Sample Values (first 5 dimensions with differences):**

**bit\_flag:**  
*Only in CONTROL (80 total):* 738665140073023520, 1765481972437876736, 1765483621696929792, 612562117094279168, 738660741992955904, 900794692265052192, 1765484171452743680, 738599169341800448, 612562117090084864, 738665140039452704 ... (+ 70 more, see CSV)  
*Only in STAGE (4 total):* 612507691801149952, 612507691801166336, 576465150352295936, 596735781088018432

**channel\_id:**  
*Only in STAGE (66 total):* 16896383, 17070314, 17900458, 353245657, 16888358, 16888993, 16895389, 208529226, 16895320, 16886233 ... (+ 56 more, see CSV)

**postal\_code:**  
*Only in STAGE (2 total):* 22853, 19031

**postal\_code\_package\_ids:**  
*Only in STAGE (1 total):* \[1447 2056 2235 4669 8483\]

**user\_city\_id:**  
*Only in STAGE (3 total):* 77143, 77190, 81143

*... and 2 more dimensions with differences (see CSV attachment for complete list)*

---

**📊 METRIC SUM DIFFERENCES**

| Metric | Control Sum | Stage Sum | Difference | % Diff |
| --- | --- | --- | --- | --- |
| **avails** | 15,817,016.00 | 15,672,762.00 | -144,254.00 | -0.91% |

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**  

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 2,744,841, Stage: 2,769,789, Diff: +24,948) |
| **Row Hash** | **MISMATCH** (Only in Control: 2,744,841, Only in Stage: 2,769,789) |

---

**🔬 COLUMN-LEVEL DIFF — Dimension value FREQUENCY differences found**  
*These dimensions have different value distributions between control and stage, causing 0 rows to match when joining on all dimension keys.*

| Dimension | Values with Freq Diff | Sample Differences |
| --- | --- | --- |
| **network\_id** | 197 / 547 | val=`384777`: ctrl=85120, stg=86177 val=`532107`: ctrl=316, stg=334 val=`525804`: ctrl=416, stg=417 val=`524565`: ctrl=340294, stg=340995 val=`500763`: ctrl=300, stg=330 |
| **content\_owner\_id** | 63 / 277 | val=`539275`: ctrl=40, stg=46 val=`384777`: ctrl=79169, stg=80344 val=`525804`: ctrl=1099, stg=1101 val=`500763`: ctrl=1288, stg=1530 val=`171213`: ctrl=9811, stg=9952 |
| **distributor\_id** | 56 / 264 | val=`539275`: ctrl=10, stg=11 val=`384777`: ctrl=18821, stg=19119 val=`525804`: ctrl=225, stg=226 val=`500763`: ctrl=292, stg=320 val=`-1`: ctrl=2136621, stg=2160131 |
| **reseller\_id** | 13 / 242 | val=`384777`: ctrl=9789, stg=9938 val=`-1`: ctrl=2658021, stg=2682930 val=`171213`: ctrl=711, stg=709 val=`191701`: ctrl=3012, stg=2883 val=`520040`: ctrl=1259, stg=1274 |
| **tv\_network\_id** | 11 / 162 | val=`-1`: ctrl=2720256, stg=2745018 val=`3`: ctrl=501, stg=511 val=`601`: ctrl=40, stg=41 val=`41`: ctrl=183, stg=200 val=`55`: ctrl=215, stg=218 |
| **transaction\_type** | 6 / 6 | val=`D`: ctrl=3890, stg=3896 val=`C`: ctrl=626, stg=634 val=`CROV`: ctrl=549443, stg=550837 val=`R`: ctrl=28187, stg=28182 val=`CRO`: ctrl=54261, stg=54291 |
| **traffic\_type** | 3 / 3 | val=`0`: ctrl=2705980, stg=2704890 val=`1`: ctrl=38395, stg=38581 val=`2`: ctrl=466, stg=26318 |
| **bit\_flag** | 209 / 643 | val=`864761497199577088`: ctrl=142, stg=199.0 val=`612489549324748800`: ctrl=1, stg=nan val=`1765481972429488128`: ctrl=86, stg=nan val=`2053711798825385984`: ctrl=66, stg=nan val=`1765481972429492224`: ctrl=115, stg=nan |
| **asset\_id** | 1 / 1 | val=`-1`: ctrl=2744841, stg=2769789 |
| **series\_id** | 1 / 1 | val=`-1`: ctrl=2744841, stg=2769789 |

  

**Control table:** `fw1_stg.suresh.f_inventory_delivered_portfolio_hourly_control`  
**Stage table:** `fw1_stg.suresh.f_inventory_delivered_portfolio_hourly_stage`

| **Column\_name** | **Known** | **comment** |
| --- | --- | --- |
| total\_ad\_views | Yes | `If you really want to find something to align, then use traffic_type != 1 +ack__metrics__ad_impression (in H++), it should be = ack__metrics__ad_impression in current hoover` |
| avails | Yes | As per discussion with @Li, Ruonan and @Bhargava, Karan  The difference we are seeing is due to the below factor` traffic_type indicate ivt status(0: valid, 1:invalid-marked in prebid, 2:invalid-marked in postbid). the possible IVT diff comes from postbid ivt, because it is using different data between hoover and hoover++. so it means there may be some ivt traffic(traffic_type=2) in the current hoover being marked as valid(traffic_type=0) in h++ or the other way round. in your case, the avails in total are 292194, that's aligned in hoover and hoover++. when checking the diff, it comes from distribution of traffic_type 0 and 2, so it's expected.` |

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Metric sums, Row-level hash
- Dimensions analyzed: 50 — differences found
- Metrics analyzed: 2 — differences found
- Row count: Control 3,264,790 / Stage 3,301,265 — mismatch
- Row hash diffs: 688,951 — mismatch


---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **process\_batch\_id** | 2 | 1 | 1 | 0 |
| **network\_id** | 542 | 544 | 0 | 2 |
| **reseller\_id** | 240 | 241 | 0 | 1 |
| **tv\_network\_id** | 162 | 164 | 0 | 2 |
| **bit\_flag** | 646 | 609 | 41 | 4 |
| **site\_section\_id** | 9543 | 9582 | 0 | 39 |
| **site\_id** | 2676 | 2683 | 0 | 7 |
| **site\_section\_group\_ids** | 6878 | 6901 | 0 | 23 |
| **airing\_id** | 93 | 94 | 0 | 1 |
| **channel\_id** | 5888 | 5920 | 0 | 32 |
| **break\_id** | 132 | 133 | 0 | 1 |
| **ad\_unit\_id** | 773 | 775 | 0 | 2 |
| **geo\_visibility** | 1 | 2 | 0 | 1 |
| **postal\_code** | 37554 | 37583 | 0 | 29 |
| **postal\_code\_package\_ids** | 45618 | 45712 | 0 | 94 |
| **user\_city\_id** | 26465 | 26483 | 0 | 18 |
| **user\_dma\_code** | 981 | 984 | 0 | 3 |
| **tracked\_audience\_item\_ids** | 5407 | 5472 | 0 | 65 |

**DIMENSION DIFFERENCE SAMPLES:**

**network\_id**:  
**issue: Present in stage and not in control**  
**Samples:**

Hoover ++ Transaction : [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711063523\_205089&externalid=20260711\_063655\_00014\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711063523_205089&externalid=20260711_063655_00014_t2mj6)

Hoover ++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710024608\_364549&externalid=20260710\_025101\_00024\_7mazq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710024608_364549&externalid=20260710_025101_00024_7mazq)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710034249\_735596](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710034249_735596)

Reason: Checked the above networks (`510938`, `531840`) and we don’t see any entries for this networks in hoover for this timeframe **20260630080000. **


**bit\_flag**:  
**issue: Present in control and not in stage**  
**Samples:**

|  |
| --- |
| 738594771328829472 |
| 612559918071023616 |
| 630574350940243968 |
| 738665140073023520 |
| 612564350489856000 |

Took the first sample (**738594771328829472**) and analysed the Hoover tables  
Hoover:   
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711105400\_884265&externalid=20260711\_105410\_00014\_qwcrt](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711105400_884265&externalid=20260711_105410_00014_qwcrt)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711120051\_417915&externalid=20260711\_120116\_00000\_gpzgv](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711120051_417915&externalid=20260711_120116_00000_gpzgv)

Hoover++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711120615\_060177&externalid=20260711\_120925\_00002\_5ic43](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711120615_060177&externalid=20260711_120925_00002_5ic43)

Reason: It seems the network\_bit\_flag is different between Hoover and Hoover++ tables which is causing the issue when we calculate the bit-flag using logic **COALESCE(nw.bit\_flags, CAST(0 AS BIGINT)) + COALESCE(ad\_bit\_flag, CAST(0 AS BIGINT)) + COALESCE(request\_\_bit\_flags, CAST(0 AS BIGINT)) AS bit\_flag. **

**issue: Present in stage and not in control**  
**Samples:**

|  |
| --- |
| 594479583252973600 |
| 612507691801149952 |
| 594549952001345568 |
| 612507691801166336 |

Took the first sample (**594479583252973600**) and analysed the Hoover tables  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711125930\_844144&externalid=20260711\_125942\_00110\_zbk8j](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711125930_844144&externalid=20260711_125942_00110_zbk8j)  
Hoover++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711130128\_419244&externalid=20260711\_130427\_00004\_5ic43](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711130128_419244&externalid=20260711_130427_00004_5ic43)

Reason: Same as above issue where the network\_bit\_flag is different between Hoover and Hoover++ tables which is causing the issue when we calculate the bit-flag using logic **COALESCE(nw.bit\_flags, CAST(0 AS BIGINT)) + COALESCE(ad\_bit\_flag, CAST(0 AS BIGINT)) + COALESCE(request\_\_bit\_flags, CAST(0 AS BIGINT)) AS bit\_flag. **

**reseller\_network\_id**:  
**issue: Present in stage and not in control**  
**Samples:**

Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711064919\_671345&externalid=20260711\_065051\_00015\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711064919_671345&externalid=20260711_065051_00015_t2mj6)

Hoover ++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710060950\_485202&externalid=20260710\_061508\_00035\_7mazq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710060950_485202&externalid=20260710_061508_00035_7mazq)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710061953\_271822&externalid=20260710\_062005\_00001\_qmjd4](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710061953_271822&externalid=20260710_062005_00001_qmjd4)

Reason: Checked the above reseller\_network\_id (`531840`) and we don’t see any entries for this reseller\_network\_id in hoover for this timeframe **20260630080000.**


**tv\_network\_id**:  
**issue: Present in stage and not in control**  
**Samples:**

Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711070820\_954554&externalid=20260711\_071118\_00016\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711070820_954554&externalid=20260711_071118_00016_t2mj6)  
Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710062532\_900632&externalid=20260710\_063428\_00036\_7mazq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710062532_900632&externalid=20260710_063428_00036_7mazq)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710074222\_345266&externalid=20260710\_074232\_00005\_qcha3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710074222_345266&externalid=20260710_074232_00005_qcha3)

Reason: Checked the above tv\_network\_id (`32,249`) and we don’t see any entries for this tv\_network\_id in hoover for this timeframe **20260630080000.**

**site\_section\_id**:  
**issue: Present in stage and not in control**  
**Samples:**

Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711072312\_510613&externalid=20260711\_072445\_00017\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711072312_510613&externalid=20260711_072445_00017_t2mj6)  
Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710100022\_994811&externalid=20260710\_100543\_00054\_5nyyp](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710100022_994811&externalid=20260710_100543_00054_5nyyp)  
Hoover:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710132902\_074184&externalid=20260710\_132912\_00009\_rrahm](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710132902_074184&externalid=20260710_132912_00009_rrahm)

Reason: Checked the above site\_section\_ids (17841788,23604657,24385524,22771647,19710877) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**

**site\_id**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711072947\_281795&externalid=20260711\_073118\_00021\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711072947_281795&externalid=20260711_073118_00021_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710155443\_421648&externalid=20260710\_160026\_00039\_3jkcu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710155443_421648&externalid=20260710_160026_00039_3jkcu)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710161017\_849595&externalid=20260710\_161154\_00001\_dycaf](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710161017_849595&externalid=20260710_161154_00001_dycaf)

Reason: Checked the above site\_ids (1094422,678322,1273479,871747) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**


**airing\_id**:  
**issue: Present in stage and not in control**  
**Samples:**

Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711073550\_533825&externalid=20260711\_073722\_00024\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711073550_533825&externalid=20260711_073722_00024_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710161919\_572938&externalid=20260710\_162432\_00032\_8kk56](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710161919_572938&externalid=20260710_162432_00032_8kk56)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710162950\_230019&externalid=20260710\_162958\_00014\_e37bp](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710162950_230019&externalid=20260710_162958_00014_e37bp)

Reason: Checked the above airing\_id (`473830212`) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**

**channel\_id**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710163308\_637463&externalid=20260710\_163807\_00004\_3aks2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710163308_637463&externalid=20260710_163807_00004_3aks2)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710163308\_637463&externalid=20260710\_163807\_00004\_3aks2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710163308_637463&externalid=20260710_163807_00004_3aks2)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710164839\_439398&externalid=20260710\_164900\_00004\_mt5jg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710164839_439398&externalid=20260710_164900_00004_mt5jg)

Reason: 

Checked the above channel\_id (1147558203,1098148988,1130424993,150307126) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**  
For this channel\_id(`100504408`) the timeframe is falling 07 instead of 08 hour in hoover


**break\_id**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711074325\_956276&externalid=20260711\_074452\_00026\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711074325_956276&externalid=20260711_074452_00026_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710164943\_899075&externalid=20260710\_165442\_00019\_esznk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710164943_899075&externalid=20260710_165442_00019_esznk)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260710170136\_949738&externalid=20260710\_170252\_00000\_xixep](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260710170136_949738&externalid=20260710_170252_00000_xixep)

Reason: Checked the above break\_id (64228050) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**


**ad\_unit\_id**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711075756\_219519&externalid=20260711\_075926\_00027\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711075756_219519&externalid=20260711_075926_00027_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711080432\_972469&externalid=20260711\_080752\_00000\_e4fk3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711080432_972469&externalid=20260711_080752_00000_e4fk3)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711080717\_345613&externalid=20260711\_080756\_00002\_m56qs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711080717_345613&externalid=20260711_080756_00002_m56qs)

Reason: Checked the above ad\_unit\_id (68178,68177) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**


**postal\_code**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711083047\_684028&externalid=20260711\_083351\_00031\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711083047_684028&externalid=20260711_083351_00031_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711083735\_656664&externalid=20260711\_084636\_00093\_53ds7](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711083735_656664&externalid=20260711_084636_00093_53ds7)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711085101\_236037&externalid=20260711\_085114\_00002\_7sy6n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711085101_236037&externalid=20260711_085114_00002_7sy6n)

Reason: Checked the above postal\_code ('3875','8089','46446','16666') and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**

**user\_city\_id**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711085327\_718439&externalid=20260711\_085624\_00032\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711085327_718439&externalid=20260711_085624_00032_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711085402\_118205&externalid=20260711\_090258\_02007\_w8huf](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711085402_118205&externalid=20260711_090258_02007_w8huf)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711091223\_553331&externalid=20260711\_091232\_00007\_ic4bn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711091223_553331&externalid=20260711_091232_00007_ic4bn)

Reason: Checked the above user\_city\_id (344050,795603,77637,74242,710051) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**


**user\_dma\_code**:  
**issue: Present in stage and not in control**  
**Samples:**  
Hoover ++ Transaction: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711091453\_641572&externalid=20260711\_091754\_00033\_t2mj6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711091453_641572&externalid=20260711_091754_00033_t2mj6)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711091524\_789724&externalid=20260711\_092352\_00000\_j5b23](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711091524_789724&externalid=20260711_092352_00000_j5b23)  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260711093236\_051032&externalid=20260711\_093250\_00070\_k5ifh](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260711093236_051032&externalid=20260711_093250_00070_k5ifh)

Reason: Checked the above user\_dma\_code (752153,752175,752120) and we don’t see any entries for this  in hoover for this timeframe **20260630080000.**




---

**📊 METRIC SUM DIFFERENCES**

| Metric | Control Sum | Stage Sum | Difference | % Diff | **Know difference** |
| --- | --- | --- | --- | --- | --- |
| **avails** | 15,882,406.00 | 15,899,078.00 | +16,672.00 | +0.10% |  |
| **ad\_views** | 126,921.00 | 126,921.00 | 0 | 0 | - |

**METRIC SUM DIFFERENCES** **SAMPLES:**

For the below networks the metric values are coming in as higher values in the H++ but in Hoover it’s lower values

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| network\_id | total\_ad\_views\_stage | total\_ad\_views\_ctrl | ad\_views\_delta | total\_avails\_stage | total\_avails\_ctrl | avails\_delta |
| 384777 | 14010 | 3808 | 10202 | 1571993 | 1562073 | 9920 |
| 505334 | 1589 | 673 | 916 | 17958 | 16030 | 1928 |
| 515123 | 800 | 295 | 505 | 4136 | 884 | 3252 |
| 376521 | 3638 | 3321 | 317 | 76569 | 75163 | 1406 |
| 523208 | 367 | 76 | 291 | 0 | 0 | 0 |
| 520040 | 1553 | 1388 | 165 | 1265 | 1235 | 30 |
| 520311 | 21853 | 21727 | 126 | 72726 | 72590 | 136 |

### **ad\_views analysis :**  
  
For the above issue networks the `raw_ad_impression`  are matching between the Hoover++ and Hoover, but when it comes to `ad_impression`  Hoover is having less count for some cases where as hoover++ is filled with values same as `raw_ad_impression` Also the **ack\_\_event\_type is matching in both cases.**

Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708164045\_135470&externalid=20260708\_164051\_00055\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708164045_135470&externalid=20260708_164051_00055_xgsem)  
Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708164156\_991651&externalid=20260708\_164637\_00056\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708164156_991651&externalid=20260708_164637_00056_xgsem)

I also pulled few transaction where i see this issue happening at transaction level as well  
`1782808029762785596`  
`1782807041563740416`  
`1782808167023313334`  
`1782807110280054712`

LQS query pulled for one of the transaction id `1782808029762785596`  
Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708173652\_925195&externalid=20260708\_173656\_00087\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708173652_925195&externalid=20260708_173656_00087_xgsem)  
Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708173717\_147021&externalid=20260708\_174545\_00094\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708173717_147021&externalid=20260708_174545_00094_xgsem)

Adding `traffic_type` to the sum:  
hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708185241\_262941&externalid=20260708\_185246\_00004\_rg66a](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708185241_262941&externalid=20260708_185246_00004_rg66a)  
hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708185237\_500153&externalid=20260708\_185712\_00144\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708185237_500153&externalid=20260708_185712_00144_xgsem)

We see that `traffic_type = 0` and `traffic_type = 2` does not match.

diving deeper into that same transaction that you did  
hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708185139\_467040&externalid=20260708\_185144\_00003\_rg66a](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708185139_467040&externalid=20260708_185144_00003_rg66a)  
Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708190319\_803509&externalid=20260708\_191958\_00027\_zi245](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708190319_803509&externalid=20260708_191958_00027_zi245)

As per below event-level validation known difference. to tackle this issue we need to add the `traffic_type != 1` for the ad\_impression metric.

`If you really want to find something to align, then use traffic_type != 1 +ack__metrics__ad_impression (in H++), it should be = ack__metrics__ad_impression in current hoover`

###   
**Avails analysis:**

Also for the `avails` count as well we see the same pattern alike mismatch where we see the extra counts in the hoover++ but less count in hoover data. I have pulled few samples for the same

Hoover -\>[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708192021\_072587](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708192021_072587)  
Hoover++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708192036\_682893](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708192036_682893)  
Transaction level samples :  
In Hoover we are using this logic `SUM( COALESCE(avails_in_played_slot, 0) * COALESCE(ack__metrics__avails_event_count, 0) )`  and in the current case we see null as value for `ack__metrics__avails_event_count`  so the hoover avails count is zero where as hoover++ have count for the transactionid.  
sample transaction\_ids:

```
1782807946322668893
1782806758289191007
1782809936800274681
1782808031005479107
1782808167023313334
```

Lqs query pulled for transaction id `1782807946322668893`  
Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708191241\_603671&externalid=20260708\_191245\_00155\_xgsem](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708191241_603671&externalid=20260708_191245_00155_xgsem)  
Hoover ++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708191303\_370396](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708191303_370396)

**08/07**-\> Tried to apply the same filter on the `traffic_type != 1` to avails metric as well but seeing below mismatch  
difference came from `+0.10 %`  to `-0.74 %`  , so i dig deeper and noticed for few networks and the traffic\_type=1 values are summed on Hoover table metric but if we exclude it in the hoover++ then the metric value wont be matching.

Sample networks:  
`535082`  
`534465`  
`533473`  
`533471`  
`376521`

Hoover -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709153824\_453790&externalid=20260709\_153851\_00028\_ydaej](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709153824_453790&externalid=20260709_153851_00028_ydaej)  
Hoover ++ -\> [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260709153754\_912520&externalid=20260709\_154441\_00000\_r4bqd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260709153754_912520&externalid=20260709_154441_00000_r4bqd)

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 3,264,790, Stage: 3,301,265, Diff: +36,475) |
| **Row Hash** | **MISMATCH** (Only in Control: 326,238, Only in Stage: 362,713) |

---

**🔬 COLUMN-LEVEL DIFF — 57,549 combos with metric diffs**

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=536174, content_owner_id=536174...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=523319, content_owner_id=524972...` | **avails\_sum**: ctrl=6.0000, stg=3.0000, -3.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534790, content_owner_id=512116...` | **avails\_sum**: ctrl=9.0000, stg=3.0000, -6.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=510839, content_owner_id=520311...` | **avails\_sum**: ctrl=16.0000, stg=2.0000, -14.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=523319, content_owner_id=531516...` | **avails\_sum**: ctrl=4.0000, stg=2.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=529119, content_owner_id=512116...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=533596, content_owner_id=533596...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=533596, content_owner_id=533596...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=533600, content_owner_id=533600...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=523319, content_owner_id=524972...` | **avails\_sum**: ctrl=28.0000, stg=32.0000, +4.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=384777, content_owner_id=531516...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=523319, content_owner_id=531516...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535256, content_owner_id=535256...` | **avails\_sum**: ctrl=2.0000, stg=0.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535262, content_owner_id=535262...` | **avails\_sum**: ctrl=5.0000, stg=0.0000, -5.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=520311, content_owner_id=520311...` | **ad\_views\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=525290, content_owner_id=520040...` | **avails\_sum**: ctrl=12.0000, stg=3.0000, -9.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535395, content_owner_id=535395...` | **avails\_sum**: ctrl=8.0000, stg=4.0000, -4.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=537323, content_owner_id=516429...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535082, content_owner_id=535082...` | **avails\_sum**: ctrl=100.0000, stg=0.0000, -100.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=537323, content_owner_id=516429...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=529861, content_owner_id=512116...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=524565, content_owner_id=535354...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535646, content_owner_id=531516...` | **avails\_sum**: ctrl=0.0000, stg=1.0000, +1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=520040, content_owner_id=520040...` | **avails\_sum**: ctrl=2.0000, stg=1.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535262, content_owner_id=535262...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=531818, content_owner_id=512116...` | **avails\_sum**: ctrl=4.0000, stg=2.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535263, content_owner_id=535263...` | **avails\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=537142, content_owner_id=512116...` | **avails\_sum**: ctrl=6.0000, stg=3.0000, -3.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=384777, content_owner_id=520024...` | **avails\_sum**: ctrl=15.0000, stg=14.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=529062, content_owner_id=512116...` | **avails\_sum**: ctrl=4.0000, stg=1.0000, -3.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534790, content_owner_id=512116...` | **avails\_sum**: ctrl=9.0000, stg=3.0000, -6.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535262, content_owner_id=535262...` | **avails\_sum**: ctrl=5.0000, stg=0.0000, -5.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=536359, content_owner_id=536359...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=524565, content_owner_id=384777...` | **avails\_sum**: ctrl=20.0000, stg=10.0000, -10.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=529681, content_owner_id=512116...` | **avails\_sum**: ctrl=6.0000, stg=3.0000, -3.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534465, content_owner_id=534465...` | **avails\_sum**: ctrl=100.0000, stg=0.0000, -100.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=537323, content_owner_id=512116...` | **avails\_sum**: ctrl=3.0000, stg=1.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=384777, content_owner_id=520024...` | **avails\_sum**: ctrl=4.0000, stg=2.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=543065, content_owner_id=191701...` | **avails\_sum**: ctrl=12.0000, stg=6.0000, -6.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=535399, content_owner_id=535399...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=384777, content_owner_id=534465...` | **avails\_sum**: ctrl=8.0000, stg=2.0000, -6.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=510839, content_owner_id=535275...` | **avails\_sum**: ctrl=4.0000, stg=3.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=536359, content_owner_id=536359...` | **avails\_sum**: ctrl=1.0000, stg=0.0000, -1.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=534991, content_owner_id=534991...` | **avails\_sum**: ctrl=2.0000, stg=0.0000, -2.0000 |
| `date=2026-06-30, hour=08, process_batch_id=20260630080000, network_id=545336, content_owner_id=545336...` | **avails\_sum**: ctrl=1.0000, stg=2.0000, +1.0000 |

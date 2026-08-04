# f\_market\_metadata\_auditing\_hourly

### New Diffs

There are no new diffs that exist that are not already known.

---

**⚠️ \[STG\] VALIDATION FAILED - f\_market\_metadata\_auditing\_hourly**

  
**Environment:** STG  |  **Date:** 2026-07-18  |  **Hour:** 08  
**Control table:** `fw1_stg.slogan313.f_market_metadata_auditing_hourly_control`  
**Stage table:** `fw1_stg.slogan313.f_market_metadata_auditing_hourly_stage`

---

**📋 SUMMARY**

- **Failed checks:** Dimension values, Row-level hash
- Dimensions analyzed: 15 — differences found
- Metrics analyzed: 1 — ✓ pass
- Row count: Control 338,457 / Stage 336,473 — mismatch
- Row hash diffs: 65,826 — mismatch

---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **metadata\_auditing\_flags** | 26 | 2 | 24 | 0 |

**Sample Values (first 5 dimensions with differences):**

**metadata\_auditing\_flags:**  
*Only in CONTROL (24 total):* 34, 136, 144, 32, 98, 72, 146, 88, 96, 104 ... (+ 14 more, see CSV)

**✓ All metric sums match!**

---

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | **MISMATCH** (Control: 338,457, Stage: 336,473, Diff: -1,984) |
| **Row Hash** | **MISMATCH** (Only in Control: 33,905, Only in Stage: 31,921) |

---

**🔬 COLUMN-LEVEL DIFF — 1,541 combos with metric diffs**

| Dims | Metric Diffs |
| --- | --- |
| `date=2026-07-18, hour=08, network_id=169843, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2.0000, stg=102.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=537323, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=4,210.0000, stg=4,310.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=536452, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=200.0000, stg=300.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=510839, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=300.0000, stg=702.0000, +402.0000 |
| `date=2026-07-18, hour=08, network_id=512116, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=11,308.0000, stg=11,310.0000, +2.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=600.0000, stg=900.0000, +300.0000 |
| `date=2026-07-18, hour=08, network_id=520311, integration_type=NORMAL, auction_status=6...` | **outbound\_request\_sum**: ctrl=10.0000, stg=15.0000, +5.0000 |
| `date=2026-07-18, hour=08, network_id=510839, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2,306.0000, stg=2,506.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=6...` | **outbound\_request\_sum**: ctrl=6.0000, stg=12.0000, +6.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=603.0000, stg=604.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=500.0000, stg=900.0000, +400.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=300.0000, stg=500.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=300.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=533475, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=12,200.0000, stg=12,400.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=1,802.0000, stg=3,404.0000, +1,602.0000 |
| `date=2026-07-18, hour=08, network_id=535275, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=203.0000, stg=303.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=538726, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=207.0000, stg=313.0000, +106.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=200.0000, stg=2,000.0000, +1,800.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=6...` | **outbound\_request\_sum**: ctrl=163.0000, stg=169.0000, +6.0000 |
| `date=2026-07-18, hour=08, network_id=538726, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=537.0000, stg=543.0000, +6.0000 |
| `date=2026-07-18, hour=08, network_id=537432, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=5.0000, stg=6.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=200.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=401.0000, stg=2,005.0000, +1,604.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=60,858.0000, stg=66,864.0000, +6,006.0000 |
| `date=2026-07-18, hour=08, network_id=169843, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2,604.0000, stg=5,006.0000, +2,402.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=6...` | **outbound\_request\_sum**: ctrl=1.0000, stg=101.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=191701, integration_type=PG_TD, auction_status=2...` | **outbound\_request\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=3.0000, stg=406.0000, +403.0000 |
| `date=2026-07-18, hour=08, network_id=520311, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2.0000, stg=3.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=200.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=604.0000, stg=704.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=200.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2,647.0000, stg=2,651.0000, +4.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=14...` | **outbound\_request\_sum**: ctrl=8.0000, stg=9.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=534979, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=7.0000, stg=13.0000, +6.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=11.0000, stg=12.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=200.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=510839, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=302.0000, stg=702.0000, +400.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=1,108.0000, stg=1,308.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=524565, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=10.0000, stg=11.0000, +1.0000 |
| `date=2026-07-18, hour=08, network_id=376521, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=2,406.0000, stg=3,009.0000, +603.0000 |
| `date=2026-07-18, hour=08, network_id=535275, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=703.0000, stg=1,207.0000, +504.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=1.0000, stg=101.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=100.0000, stg=200.0000, +100.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=404.0000, stg=604.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=1,014.0000, stg=1,614.0000, +600.0000 |
| `date=2026-07-18, hour=08, network_id=520311, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=10.0000, stg=15.0000, +5.0000 |
| `date=2026-07-18, hour=08, network_id=384777, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=604.0000, stg=804.0000, +200.0000 |
| `date=2026-07-18, hour=08, network_id=523319, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=8,840.0000, stg=9,542.0000, +702.0000 |
| `date=2026-07-18, hour=08, network_id=510839, integration_type=NORMAL, auction_status=2...` | **outbound\_request\_sum**: ctrl=102.0000, stg=302.0000, +200.0000 |

### Hoover

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715175926\_566169&externalid=20260715\_175927\_00320\_z8gvm](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715175926_566169&externalid=20260715_175927_00320_z8gvm)

### Hoover++ (View)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715175921\_241631&externalid=20260715\_180118\_00325\_z8gvm](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715175921_241631&externalid=20260715_180118_00325_z8gvm)

### Hoover++ (Transaction)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715175923\_086624&externalid=20260715\_180117\_00324\_z8gvm](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715175923_086624&externalid=20260715_180117_00324_z8gvm)

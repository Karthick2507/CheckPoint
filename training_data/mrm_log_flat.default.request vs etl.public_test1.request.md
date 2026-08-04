# mrm\_log\_flat\.default\.request vs etl\.public\_test1\.request

## Introduction

Below is a list of all the `request` level entities that were validated. 

For columns that are SEMANTICALLY the same, i.e one more reports `null` while other reports an `[]` we can mark these as same. Event level validations script (built from validations.py) does this.

Top 5 networks (by record count for an hour) → 538917, 112214, 543709, 535275, 516429


## Known Difference:

| **View** | **Entity** | **Difference ** | **Comments** |
| --- | --- | --- | --- |
| Request | **Inventory** | Following Internal array columns are missing inside  **inventory\_\_site\_section\_chain** **Inventory\_\_asset\_chain **columns where as it was present in old hoover request table`network_is_ad_owner network_is_extra_item_owner deal_awareability demand_dim_awareability supply_source sales_channel programmatic_exchange_rate_to_usd programmatic_exchange_rate_to_eur` | As per discussion on 28/05/2026 Confirmed with @Bhargava, Karan  that this is know difference to not to include this columns under the inventory chains in the new views. |

## Entity

### Request

Checking network\_id 516429 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511230216\_167279&externalid=20260511\_230219\_00415\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511230216_167279&externalid=20260511_230219_00415_i8jpu)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511230225\_680799&externalid=20260511\_230257\_00416\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511230225_680799&externalid=20260511_230257_00416_i8jpu)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_2_txn.csv
  Source B : new_2_txn.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    request__yield_optimization_ids                              2 row(s)
    request__client_facing_ivt_reason_flag                       2 row(s)

  Detailed diffs:

  [row=2]
    request__yield_optimization_ids:
      old_2_txn.csv: '[]'
      new_2_txn.csv: '\\N'
    request__client_facing_ivt_reason_flag:
      old_2_txn.csv: '\\N'
      new_2_txn.csv: '0'

  [row=3]
    request__yield_optimization_ids:
      old_2_txn.csv: '[]'
      new_2_txn.csv: '\\N'
    request__client_facing_ivt_reason_flag:
      old_2_txn.csv: '\\N'
      new_2_txn.csv: '0'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

2 rows have differences. Looking at the differences for these 2 fields, we see that:

Client Facing IVT Reason Flag is `null` in Hoover vs `0` in Hoover++

Yield Optimization Ids is `[]`in Hoover vs `null` in Hoover++

---

Checking network id 538917 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511230510\_786281&externalid=20260511\_230512\_00420\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511230510_786281&externalid=20260511_230512_00420_i8jpu)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511230925\_690064&externalid=20260511\_230954\_00425\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511230925_690064&externalid=20260511_230954_00425_i8jpu)

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_538917.csv
  Source B : new_538917.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              5 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       5 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 112214 with specific transaction ids:

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511232405\_393478](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511232405_393478)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511232044\_299673](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511232044_299673)

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_112214.csv
  Source B : new_112214.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              5 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       5 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]
    request__backend_filtration_reason                           2 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 543709

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=history&queryid=presto\_20260511232405\_393478&externalid=20260511\_232407\_00434\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=history&queryid=presto_20260511232405_393478&externalid=20260511_232407_00434_i8jpu)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511232411\_968690&externalid=20260511\_232436\_00435\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511232411_968690&externalid=20260511_232436_00435_i8jpu)

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_543709.csv
  Source B : new_543709.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              5 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       4 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 535275

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511232915\_799468&externalid=20260511\_232917\_00439\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511232915_799468&externalid=20260511_232917_00439_i8jpu)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511232917\_307133&externalid=20260511\_232945\_00440\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511232917_307133&externalid=20260511_232945_00440_i8jpu)

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_535275.csv
  Source B : new_535275.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              5 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       5 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 516429

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511233109\_543521&externalid=20260511\_233111\_00442\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511233109_543521&externalid=20260511_233111_00442_i8jpu)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260511233137\_741019&externalid=20260511\_233154\_00443\_i8jpu](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511233137_741019&externalid=20260511_233154_00443_i8jpu)

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_516429.csv
  Source B : new_516429.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 50
  Columns B: 50

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (50 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              5 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       5 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]
    request__backend_filtration_reason                           1 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

### Request Info 

Checking network\_id 516429 with specific transaction ids:

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_516429.csv
  Source B : new_516429.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 538917 with specific transaction ids:

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_538917.csv
  Source B : new_538917.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 112214 with specific transaction ids:

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_538917.csv
  Source B : new_538917.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
❯ python event_validations.py old_112214.csv new_112214.csv
Reading old_112214.csv …
Reading new_112214.csv …
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_112214.csv
  Source B : new_112214.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 543709

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_543709.csv
  Source B : new_543709.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 535275

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_535275.csv
  Source B : new_535275.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 516429

```
Sorting both files by request__transaction_id …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_516429.csv
  Source B : new_516429.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 5
  Columns B: 5

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (5 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

### Aggregated Columns (deep dive)

#### request\_\_context\_\_network\_id

| **Network ID** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| 538917 | 187575 | 182335 | 5240 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511215823_756714&externalid=20260511_220022_00001_ehspj) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260511215606_155078&externalid=20260511_215644_00382_i8jpu) |
| 112214 | 73189 | 68710 | 4479 |  |
| 543709 | 62084 | 62360 | -276 |  |
| 516429 | 42622 | 40477 | 2145 |  |
| 535275 | 41132 | 40655 | 477 |  |

Why? ^ Need to look into the above → 

 

| **Network ID** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| 543709 | 61002 | 61002 | 0 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520210635_754406&externalid=20260520_210637_00465_fk2ih) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520210636_323776&externalid=20260520_210720_00466_fk2ih) |
| 538917 | 161500 | 161500 | 0 |  |
| 535275 | 35179 | 35179 | 0 |  |
| 516429 | 41852 | 41852 | 0 |  |
| 112214 | 66962 | 66962 | 0 |  |

Re-ran analysis; using the same query as the above.

No differences found. Assumption: data had NOT settled in previous model; hence discrepancy.

### Visitor Entity

Checking network\_id 516429 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515181543\_502720&externalid=20260515\_181545\_00372\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515181543_502720&externalid=20260515_181545_00372_bkccs)

New model LQS →[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515181528\_736194&externalid=20260515\_181607\_00373\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515181528_736194&externalid=20260515_181607_00373_bkccs)

```
Reading visitor_old_516429.csv …
Reading visitor_new_516429.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : visitor_old_516429.csv
  Source B : visitor_new_516429.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 538917 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515182308\_536645&externalid=20260515\_182311\_00382\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515182308_536645&externalid=20260515_182311_00382_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515182311\_894527&externalid=20260515\_182348\_00383\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515182311_894527&externalid=20260515_182348_00383_bkccs)

```
Reading old_538917.csv …
Reading new_538917.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_538917.csv
  Source B : new_538917.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      5 row(s)
    visitor__tracked_term                                        5 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 112214 with specific transaction ids:

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183225\_769563&externalid=20260515\_183228\_00396\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183225_769563&externalid=20260515_183228_00396_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260515\_183302\_00397\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260515_183302_00397_bkccs)

```
Reading old_112214.csv …
Reading new_112214.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_112214.csv
  Source B : new_112214.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__tracked_term                                        5 row(s)
    visitor__universal_iids                                      1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 543709

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515182811\_004720&externalid=20260515\_182813\_00390\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515182811_004720&externalid=20260515_182813_00390_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183147\_709673&externalid=20260515\_183225\_00395\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183147_709673&externalid=20260515_183225_00395_bkccs)

```
Reading old_543709.csv …
Reading new_543709.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_543709.csv
  Source B : new_543709.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      5 row(s)
    visitor__tracked_term                                        5 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 535275

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183703\_063243&externalid=20260515\_183706\_00399\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183703_063243&externalid=20260515_183706_00399_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183706\_067872&externalid=20260515\_183746\_00402\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183706_067872&externalid=20260515_183746_00402_bkccs)

```
Reading old_535275.csv …
Reading new_535275.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_535275.csv
  Source B : new_535275.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      5 row(s)
    visitor__tracked_term                                        5 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

---

Checking network id 516429

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183713\_457594&externalid=20260515\_183716\_00400\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183713_457594&externalid=20260515_183716_00400_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515183720\_128847&externalid=20260515\_183745\_00401\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515183720_128847&externalid=20260515_183745_00401_bkccs)

```
Reading old_516429_2.csv …
Reading new_516429_2.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_516429_2.csv
  Source B : new_516429_2.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 36
  Columns B: 36

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (36 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      2 row(s)
    visitor__tracked_term                                        2 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary:

No real diffs found 

### Visitor Aggregated Columns (deep dive)

#### **visitor\_\_country**

|  |  |  |  |
| --- | --- | --- | --- |
| **request\_\_context\_\_network\_id** | **visitor\_\_country** | **old\_count** [old\_query](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260522144901_914072&externalid=20260522_144903_00184_7ydkw) | **new\_count** [new\_query](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260522144901_914072&externalid=20260522_144903_00184_7ydkw) |
| 112214 | us | 85285 | 85285 |
| 112214 | mx | 637 | 637 |
| 112214 | do | 50 | 50 |
| 112214 | pr | 48 | 48 |
| 112214 | gt | 16 | 16 |
| 112214 | co | 8 | 8 |
| 112214 | cr | 8 | 8 |
| 112214 | hn | 7 | 7 |
| 112214 | null | 5 | 5 |
| 112214 | ve | 5 | 5 |
| 112214 | ar | 4 | 4 |
| 112214 | uy | 3 | 3 |
| 112214 | pe | 3 | 3 |
| 112214 | ec | 3 | 3 |
| 112214 | sv | 2 | 2 |
| 112214 | pa | 1 | 1 |
| 535354 | us | 38722 | 38722 |
| 535354 | za | 1532 | 1532 |
| 535354 | in | 1478 | 1478 |
| 535354 | es | 1210 | 1210 |
| 535354 | gb | 1011 | 1011 |
| 535354 | de | 853 | 853 |
| 535354 | fr | 611 | 611 |
| 535354 | it | 291 | 291 |
| 535354 | nl | 268 | 268 |
| 535354 | ch | 247 | 247 |
| 535354 | ca | 207 | 207 |
| 535354 | pl | 185 | 185 |
| 535354 | br | 140 | 140 |
| 535354 | id | 133 | 133 |
| 535354 | au | 124 | 124 |
| 535354 | tr | 122 | 122 |
| 535354 | mx | 118 | 118 |
| 535354 | cl | 87 | 87 |
| 535354 | at | 69 | 69 |
| 535354 | se | 67 | 67 |
| 535354 | hr | 51 | 51 |
| 535354 | co | 50 | 50 |
| 535354 | be | 27 | 27 |
| 535354 | ar | 26 | 26 |
| 535354 | pe | 24 | 24 |
| 535354 | ae | 22 | 22 |
| 535354 | ma | 19 | 19 |
| 535354 | eg | 19 | 19 |
| 535354 | pt | 15 | 15 |
| 535354 | gr | 14 | 14 |
| 535354 | vn | 14 | 14 |
| 535354 | dz | 13 | 13 |
| 535354 | tn | 10 | 10 |
| 535354 | dk | 7 | 7 |
| 535354 | fi | 6 | 6 |
| 535354 | no | 5 | 5 |
| 535354 | ke | 5 | 5 |
| 535354 | cz | 4 | 4 |
| 535354 | my | 4 | 4 |
| 535354 | nz | 4 | 4 |
| 535354 | pr | 4 | 4 |
| 535354 | gp | 3 | 3 |
| 535354 | ng | 2 | 2 |
| 535354 | ie | 2 | 2 |
| 535354 | cr | 2 | 2 |
| 535354 | qa | 2 | 2 |
| 535354 | sy | 1 | 1 |
| 535354 | pk | 1 | 1 |
| 535354 | gf | 1 | 1 |
| 535354 | gi | 1 | 1 |
| 535354 | sg | 1 | 1 |
| 535354 | ph | 1 | 1 |
| 536142 | us | 57240 | 57240 |
| 536142 | ca | 119 | 119 |
| 536142 | gb | 102 | 102 |
| 536142 | de | 50 | 50 |
| 536142 | it | 40 | 40 |
| 536142 | fr | 35 | 35 |
| 536142 | es | 25 | 25 |
| 536142 | ie | 16 | 16 |
| 536142 | se | 11 | 11 |
| 536142 | nl | 10 | 10 |
| 536142 | dk | 6 | 6 |
| 536142 | au | 6 | 6 |
| 536142 | ae | 4 | 4 |
| 536142 | br | 2 | 2 |
| 536142 | cl | 1 | 1 |
| 536142 | fi | 1 | 1 |
| 536142 | dz | 1 | 1 |
| 536142 | be | 1 | 1 |
| 538917 | us | 168928 | 168928 |
| 538917 | ca | 309 | 309 |
| 538917 | mx | 9 | 9 |
| 538917 | pr | 9 | 9 |
| 538917 | gu | 2 | 2 |
| 538917 | kr | 2 | 2 |
| 538917 | ar | 1 | 1 |
| 538917 | co | 1 | 1 |
| 538917 | sa | 1 | 1 |
| 538917 | cr | 1 | 1 |
| 538917 | ve | 1 | 1 |
| 538917 | aw | 1 | 1 |
| 538917 | null | 1 | 1 |
| 538917 | tc | 1 | 1 |
| 538917 | fr | 1 | 1 |
| 538917 | jm | 1 | 1 |
| 543709 | us | 61726 | 61726 |
| 543709 | jm | 2 | 2 |
| 543709 | bs | 1 | 1 |

  Counts matching

#### **visitor\_\_dma\_code\_id**  

|  |  |  |  |
| --- | --- | --- | --- |
| **request\_\_context\_\_network\_id** | **visitor\_\_dma\_code\_id** | **old\_count** [old\_query](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260522145446_951859&externalid=20260522_145448_00188_7ydkw) | **new\_count** [new\_query](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260522145500_749931&externalid=20260522_062056_00056_7ydkw) |
| 112214 | null | 25206 | 25206 |
| 112214 | 192 | 7092 | 7092 |
| 112214 | 2 | 4484 | 4484 |
| 112214 | 98 | 3254 | 3254 |
| 112214 | 101 | 3198 | 3198 |
| 112214 | 86 | 2852 | 2852 |
| 112214 | 170 | 1560 | 1560 |
| 112214 | 29 | 1484 | 1484 |
| 112214 | 25 | 1372 | 1372 |
| 112214 | 12 | 1361 | 1361 |
| 112214 | 194 | 1339 | 1339 |
| 112214 | 113 | 1306 | 1306 |
| 112214 | 118 | 1302 | 1302 |
| 112214 | 112 | 1165 | 1165 |
| 112214 | 40 | 1159 | 1159 |
| 112214 | 205 | 1107 | 1107 |
| 112214 | 35 | 1020 | 1020 |
| 112214 | 206 | 970 | 970 |
| 112214 | 5 | 962 | 962 |
| 112214 | 168 | 946 | 946 |
| 112214 | 180 | 824 | 824 |
| 112214 | 201 | 752 | 752 |
| 112214 | 7 | 728 | 728 |
| 112214 | 61 | 715 | 715 |
| 112214 | 203 | 682 | 682 |
| 112214 | 18 | 674 | 674 |
| 112214 | 198 | 623 | 623 |
| 112214 | 28 | 607 | 607 |
| 112214 | 130 | 587 | 587 |
| 112214 | 199 | 477 | 477 |
| 112214 | 49 | 471 | 471 |
| 112214 | 96 | 442 | 442 |
| 112214 | 187 | 437 | 437 |
| 112214 | 183 | 407 | 407 |
| 112214 | 124 | 402 | 402 |
| 112214 | 34 | 391 | 391 |
| 112214 | 167 | 384 | 384 |
| 112214 | 70 | 360 | 360 |
| 112214 | 139 | 350 | 350 |
| 112214 | 13 | 345 | 345 |
| 112214 | 95 | 339 | 339 |
| 112214 | 97 | 335 | 335 |
| 112214 | 19 | 291 | 291 |
| 112214 | 100 | 283 | 283 |
| 112214 | 6 | 274 | 274 |
| 112214 | 189 | 266 | 266 |
| 112214 | 184 | 265 | 265 |
| 112214 | 195 | 257 | 257 |
| 112214 | 110 | 246 | 246 |
| 112214 | 186 | 244 | 244 |
| 112214 | 107 | 235 | 235 |
| 112214 | 117 | 225 | 225 |
| 112214 | 62 | 225 | 225 |
| 112214 | 193 | 222 | 222 |
| 112214 | 202 | 209 | 209 |
| 112214 | 91 | 209 | 209 |
| 112214 | 22 | 208 | 208 |
| 112214 | 196 | 203 | 203 |
| 112214 | 126 | 200 | 200 |
| 112214 | 36 | 195 | 195 |
| 112214 | 67 | 195 | 195 |
| 112214 | 103 | 188 | 188 |
| 112214 | 85 | 186 | 186 |
| 112214 | 57 | 182 | 182 |
| 112214 | 30 | 177 | 177 |
| 112214 | 111 | 176 | 176 |
| 112214 | 45 | 166 | 166 |
| 112214 | 150 | 161 | 161 |
| 112214 | 16 | 159 | 159 |
| 112214 | 73 | 144 | 144 |
| 112214 | 204 | 144 | 144 |
| 112214 | 58 | 143 | 143 |
| 112214 | 146 | 140 | 140 |
| 112214 | 11 | 138 | 138 |
| 112214 | 174 | 136 | 136 |
| 112214 | 125 | 132 | 132 |
| 112214 | 135 | 128 | 128 |
| 112214 | 140 | 127 | 127 |
| 112214 | 63 | 125 | 125 |
| 112214 | 47 | 121 | 121 |
| 112214 | 66 | 113 | 113 |
| 112214 | 208 | 110 | 110 |
| 112214 | 134 | 109 | 109 |
| 112214 | 144 | 103 | 103 |
| 112214 | 69 | 102 | 102 |
| 112214 | 80 | 101 | 101 |
| 112214 | 39 | 99 | 99 |
| 112214 | 20 | 95 | 95 |
| 112214 | 92 | 91 | 91 |
| 112214 | 71 | 91 | 91 |
| 112214 | 75 | 90 | 90 |
| 112214 | 145 | 90 | 90 |
| 112214 | 46 | 88 | 88 |
| 112214 | 156 | 85 | 85 |
| 112214 | 94 | 82 | 82 |
| 112214 | 8 | 82 | 82 |
| 112214 | 142 | 82 | 82 |
| 112214 | 129 | 81 | 81 |
| 112214 | 169 | 77 | 77 |
| 112214 | 33 | 76 | 76 |
| 112214 | 9 | 74 | 74 |
| 112214 | 21 | 73 | 73 |
| 112214 | 74 | 72 | 72 |
| 112214 | 207 | 71 | 71 |
| 112214 | 153 | 68 | 68 |
| 112214 | 42 | 67 | 67 |
| 112214 | 133 | 66 | 66 |
| 112214 | 44 | 62 | 62 |
| 112214 | 15 | 59 | 59 |
| 112214 | 10 | 55 | 55 |
| 112214 | 102 | 52 | 52 |
| 112214 | 158 | 52 | 52 |
| 112214 | 43 | 52 | 52 |
| 112214 | 131 | 51 | 51 |
| 112214 | 51 | 51 | 51 |
| 112214 | 147 | 50 | 50 |
| 112214 | 89 | 49 | 49 |
| 112214 | 23 | 48 | 48 |
| 112214 | 155 | 46 | 46 |
| 112214 | 132 | 45 | 45 |
| 112214 | 56 | 40 | 40 |
| 112214 | 119 | 40 | 40 |
| 112214 | 48 | 39 | 39 |
| 112214 | 128 | 37 | 37 |
| 112214 | 109 | 37 | 37 |
| 112214 | 4 | 36 | 36 |
| 112214 | 197 | 36 | 36 |
| 112214 | 177 | 34 | 34 |
| 112214 | 31 | 33 | 33 |
| 112214 | 141 | 33 | 33 |
| 112214 | 137 | 33 | 33 |
| 112214 | 185 | 32 | 32 |
| 112214 | 105 | 31 | 31 |
| 112214 | 68 | 29 | 29 |
| 112214 | 32 | 29 | 29 |
| 112214 | 164 | 29 | 29 |
| 112214 | 99 | 28 | 28 |
| 112214 | 151 | 25 | 25 |
| 112214 | 106 | 24 | 24 |
| 112214 | 52 | 24 | 24 |
| 112214 | 190 | 24 | 24 |
| 112214 | 26 | 24 | 24 |
| 112214 | 122 | 23 | 23 |
| 112214 | 104 | 21 | 21 |
| 112214 | 114 | 21 | 21 |
| 112214 | 81 | 20 | 20 |
| 112214 | 27 | 20 | 20 |
| 112214 | 152 | 20 | 20 |
| 112214 | 143 | 17 | 17 |
| 112214 | 123 | 17 | 17 |
| 112214 | 116 | 16 | 16 |
| 112214 | 176 | 16 | 16 |
| 112214 | 93 | 15 | 15 |
| 112214 | 77 | 15 | 15 |
| 112214 | 76 | 15 | 15 |
| 112214 | 87 | 15 | 15 |
| 112214 | 127 | 15 | 15 |
| 112214 | 160 | 15 | 15 |
| 112214 | 149 | 14 | 14 |
| 112214 | 175 | 14 | 14 |
| 112214 | 148 | 13 | 13 |
| 112214 | 166 | 12 | 12 |
| 112214 | 163 | 12 | 12 |
| 112214 | 88 | 12 | 12 |
| 112214 | 191 | 11 | 11 |
| 112214 | 79 | 11 | 11 |
| 112214 | 37 | 10 | 10 |
| 112214 | 136 | 10 | 10 |
| 112214 | 24 | 10 | 10 |
| 112214 | 1 | 9 | 9 |
| 112214 | 157 | 9 | 9 |
| 112214 | 120 | 9 | 9 |
| 112214 | 14 | 9 | 9 |
| 112214 | 200 | 8 | 8 |
| 112214 | 64 | 8 | 8 |
| 112214 | 17 | 7 | 7 |
| 112214 | 3 | 7 | 7 |
| 112214 | 159 | 7 | 7 |
| 112214 | 121 | 7 | 7 |
| 112214 | 115 | 7 | 7 |
| 112214 | 179 | 7 | 7 |
| 112214 | 72 | 6 | 6 |
| 112214 | 209 | 6 | 6 |
| 112214 | 108 | 6 | 6 |
| 112214 | 90 | 5 | 5 |
| 112214 | 50 | 5 | 5 |
| 112214 | 161 | 5 | 5 |
| 112214 | 181 | 4 | 4 |
| 112214 | 59 | 4 | 4 |
| 112214 | 171 | 4 | 4 |
| 112214 | 55 | 4 | 4 |
| 112214 | 41 | 3 | 3 |
| 112214 | 82 | 3 | 3 |
| 112214 | 65 | 3 | 3 |
| 112214 | 210 | 3 | 3 |
| 112214 | 138 | 3 | 3 |
| 112214 | 165 | 3 | 3 |
| 112214 | 53 | 3 | 3 |
| 112214 | 162 | 2 | 2 |
| 112214 | 60 | 2 | 2 |
| 112214 | 182 | 1 | 1 |
| 112214 | 154 | 1 | 1 |
| 112214 | 173 | 1 | 1 |
| 112214 | 38 | 1 | 1 |
| 535354 | null | 9667 | 9667 |
| 535354 | 101 | 1925 | 1925 |
| 535354 | 2 | 1511 | 1511 |
| 535354 | 170 | 1244 | 1244 |
| 535354 | 98 | 1137 | 1137 |
| 535354 | 25 | 1131 | 1131 |
| 535354 | 86 | 1129 | 1129 |
| 535354 | 168 | 839 | 839 |
| 535354 | 192 | 838 | 838 |
| 535354 | 40 | 820 | 820 |
| 535354 | 112 | 777 | 777 |
| 535354 | 5 | 757 | 757 |
| 535354 | 35 | 740 | 740 |
| 535354 | 12 | 699 | 699 |
| 535354 | 118 | 686 | 686 |
| 535354 | 29 | 643 | 643 |
| 535354 | 6 | 594 | 594 |
| 535354 | 11 | 490 | 490 |
| 535354 | 61 | 489 | 489 |
| 535354 | 7 | 474 | 474 |
| 535354 | 18 | 459 | 459 |
| 535354 | 95 | 457 | 457 |
| 535354 | 198 | 450 | 450 |
| 535354 | 28 | 439 | 439 |
| 535354 | 96 | 438 | 438 |
| 535354 | 183 | 424 | 424 |
| 535354 | 199 | 403 | 403 |
| 535354 | 16 | 376 | 376 |
| 535354 | 91 | 364 | 364 |
| 535354 | 203 | 362 | 362 |
| 535354 | 130 | 347 | 347 |
| 535354 | 49 | 319 | 319 |
| 535354 | 36 | 318 | 318 |
| 535354 | 100 | 289 | 289 |
| 535354 | 63 | 288 | 288 |
| 535354 | 194 | 278 | 278 |
| 535354 | 124 | 277 | 277 |
| 535354 | 30 | 274 | 274 |
| 535354 | 97 | 257 | 257 |
| 535354 | 205 | 255 | 255 |
| 535354 | 103 | 253 | 253 |
| 535354 | 67 | 248 | 248 |
| 535354 | 13 | 242 | 242 |
| 535354 | 62 | 231 | 231 |
| 535354 | 45 | 220 | 220 |
| 535354 | 187 | 212 | 212 |
| 535354 | 174 | 209 | 209 |
| 535354 | 19 | 206 | 206 |
| 535354 | 113 | 204 | 204 |
| 535354 | 135 | 200 | 200 |
| 535354 | 34 | 194 | 194 |
| 535354 | 142 | 181 | 181 |
| 535354 | 111 | 180 | 180 |
| 535354 | 150 | 177 | 177 |
| 535354 | 139 | 176 | 176 |
| 535354 | 43 | 174 | 174 |
| 535354 | 9 | 172 | 172 |
| 535354 | 201 | 171 | 171 |
| 535354 | 70 | 171 | 171 |
| 535354 | 107 | 170 | 170 |
| 535354 | 186 | 167 | 167 |
| 535354 | 126 | 166 | 166 |
| 535354 | 14 | 165 | 165 |
| 535354 | 99 | 164 | 164 |
| 535354 | 58 | 162 | 162 |
| 535354 | 125 | 156 | 156 |
| 535354 | 48 | 155 | 155 |
| 535354 | 57 | 152 | 152 |
| 535354 | 94 | 152 | 152 |
| 535354 | 169 | 150 | 150 |
| 535354 | 47 | 149 | 149 |
| 535354 | 42 | 149 | 149 |
| 535354 | 69 | 146 | 146 |
| 535354 | 153 | 145 | 145 |
| 535354 | 140 | 144 | 144 |
| 535354 | 141 | 142 | 142 |
| 535354 | 134 | 142 | 142 |
| 535354 | 22 | 134 | 134 |
| 535354 | 85 | 132 | 132 |
| 535354 | 158 | 129 | 129 |
| 535354 | 117 | 129 | 129 |
| 535354 | 129 | 128 | 128 |
| 535354 | 66 | 128 | 128 |
| 535354 | 114 | 127 | 127 |
| 535354 | 73 | 126 | 126 |
| 535354 | 144 | 124 | 124 |
| 535354 | 133 | 124 | 124 |
| 535354 | 208 | 124 | 124 |
| 535354 | 41 | 121 | 121 |
| 535354 | 1 | 119 | 119 |
| 535354 | 156 | 114 | 114 |
| 535354 | 180 | 114 | 114 |
| 535354 | 20 | 112 | 112 |
| 535354 | 64 | 108 | 108 |
| 535354 | 109 | 104 | 104 |
| 535354 | 46 | 102 | 102 |
| 535354 | 146 | 102 | 102 |
| 535354 | 52 | 101 | 101 |
| 535354 | 143 | 100 | 100 |
| 535354 | 15 | 99 | 99 |
| 535354 | 80 | 98 | 98 |
| 535354 | 122 | 97 | 97 |
| 535354 | 8 | 95 | 95 |
| 535354 | 75 | 95 | 95 |
| 535354 | 110 | 92 | 92 |
| 535354 | 10 | 90 | 90 |
| 535354 | 195 | 90 | 90 |
| 535354 | 155 | 89 | 89 |
| 535354 | 206 | 86 | 86 |
| 535354 | 21 | 86 | 86 |
| 535354 | 123 | 85 | 85 |
| 535354 | 157 | 85 | 85 |
| 535354 | 71 | 72 | 72 |
| 535354 | 196 | 72 | 72 |
| 535354 | 175 | 72 | 72 |
| 535354 | 88 | 71 | 71 |
| 535354 | 119 | 71 | 71 |
| 535354 | 32 | 70 | 70 |
| 535354 | 164 | 69 | 69 |
| 535354 | 137 | 68 | 68 |
| 535354 | 148 | 68 | 68 |
| 535354 | 31 | 67 | 67 |
| 535354 | 37 | 66 | 66 |
| 535354 | 147 | 65 | 65 |
| 535354 | 167 | 65 | 65 |
| 535354 | 33 | 64 | 64 |
| 535354 | 51 | 64 | 64 |
| 535354 | 4 | 63 | 63 |
| 535354 | 23 | 62 | 62 |
| 535354 | 149 | 62 | 62 |
| 535354 | 132 | 62 | 62 |
| 535354 | 173 | 61 | 61 |
| 535354 | 136 | 60 | 60 |
| 535354 | 145 | 60 | 60 |
| 535354 | 93 | 59 | 59 |
| 535354 | 39 | 59 | 59 |
| 535354 | 190 | 59 | 59 |
| 535354 | 128 | 58 | 58 |
| 535354 | 89 | 57 | 57 |
| 535354 | 138 | 53 | 53 |
| 535354 | 166 | 52 | 52 |
| 535354 | 105 | 50 | 50 |
| 535354 | 74 | 50 | 50 |
| 535354 | 56 | 49 | 49 |
| 535354 | 178 | 49 | 49 |
| 535354 | 179 | 47 | 47 |
| 535354 | 92 | 46 | 46 |
| 535354 | 76 | 46 | 46 |
| 535354 | 197 | 44 | 44 |
| 535354 | 24 | 44 | 44 |
| 535354 | 163 | 44 | 44 |
| 535354 | 160 | 43 | 43 |
| 535354 | 102 | 43 | 43 |
| 535354 | 72 | 43 | 43 |
| 535354 | 131 | 42 | 42 |
| 535354 | 172 | 41 | 41 |
| 535354 | 87 | 40 | 40 |
| 535354 | 207 | 39 | 39 |
| 535354 | 185 | 37 | 37 |
| 535354 | 182 | 37 | 37 |
| 535354 | 44 | 36 | 36 |
| 535354 | 26 | 36 | 36 |
| 535354 | 38 | 35 | 35 |
| 535354 | 127 | 35 | 35 |
| 535354 | 202 | 34 | 34 |
| 535354 | 120 | 34 | 34 |
| 535354 | 116 | 33 | 33 |
| 535354 | 184 | 33 | 33 |
| 535354 | 60 | 32 | 32 |
| 535354 | 151 | 32 | 32 |
| 535354 | 171 | 32 | 32 |
| 535354 | 154 | 31 | 31 |
| 535354 | 3 | 31 | 31 |
| 535354 | 193 | 31 | 31 |
| 535354 | 77 | 30 | 30 |
| 535354 | 81 | 29 | 29 |
| 535354 | 106 | 29 | 29 |
| 535354 | 83 | 28 | 28 |
| 535354 | 50 | 28 | 28 |
| 535354 | 54 | 27 | 27 |
| 535354 | 108 | 26 | 26 |
| 535354 | 204 | 26 | 26 |
| 535354 | 121 | 24 | 24 |
| 535354 | 189 | 24 | 24 |
| 535354 | 177 | 23 | 23 |
| 535354 | 84 | 22 | 22 |
| 535354 | 17 | 22 | 22 |
| 535354 | 159 | 21 | 21 |
| 535354 | 90 | 21 | 21 |
| 535354 | 152 | 20 | 20 |
| 535354 | 200 | 20 | 20 |
| 535354 | 68 | 19 | 19 |
| 535354 | 79 | 18 | 18 |
| 535354 | 55 | 18 | 18 |
| 535354 | 181 | 17 | 17 |
| 535354 | 176 | 17 | 17 |
| 535354 | 59 | 17 | 17 |
| 535354 | 161 | 16 | 16 |
| 535354 | 27 | 15 | 15 |
| 535354 | 65 | 13 | 13 |
| 535354 | 53 | 10 | 10 |
| 535354 | 191 | 9 | 9 |
| 535354 | 82 | 9 | 9 |
| 535354 | 104 | 9 | 9 |
| 535354 | 115 | 8 | 8 |
| 535354 | 78 | 6 | 6 |
| 535354 | 209 | 5 | 5 |
| 535354 | 162 | 4 | 4 |
| 535354 | 165 | 3 | 3 |
| 535354 | 188 | 1 | 1 |
| 535354 | 210 | 1 | 1 |
| 536142 | 101 | 2721 | 2721 |
| 536142 | 98 | 2655 | 2655 |
| 536142 | 2 | 2204 | 2204 |
| 536142 | 203 | 2018 | 2018 |
| 536142 | 192 | 1519 | 1519 |
| 536142 | 25 | 1503 | 1503 |
| 536142 | 6 | 1431 | 1431 |
| 536142 | null | 1429 | 1429 |
| 536142 | 198 | 1318 | 1318 |
| 536142 | 12 | 1254 | 1254 |
| 536142 | 86 | 1211 | 1211 |
| 536142 | 100 | 1119 | 1119 |
| 536142 | 5 | 1113 | 1113 |
| 536142 | 199 | 905 | 905 |
| 536142 | 35 | 862 | 862 |
| 536142 | 170 | 850 | 850 |
| 536142 | 40 | 846 | 846 |
| 536142 | 208 | 820 | 820 |
| 536142 | 18 | 738 | 738 |
| 536142 | 29 | 701 | 701 |
| 536142 | 7 | 681 | 681 |
| 536142 | 16 | 650 | 650 |
| 536142 | 96 | 636 | 636 |
| 536142 | 130 | 613 | 613 |
| 536142 | 144 | 603 | 603 |
| 536142 | 11 | 550 | 550 |
| 536142 | 118 | 548 | 548 |
| 536142 | 95 | 539 | 539 |
| 536142 | 153 | 514 | 514 |
| 536142 | 8 | 509 | 509 |
| 536142 | 28 | 505 | 505 |
| 536142 | 168 | 502 | 502 |
| 536142 | 91 | 496 | 496 |
| 536142 | 61 | 463 | 463 |
| 536142 | 62 | 449 | 449 |
| 536142 | 194 | 439 | 439 |
| 536142 | 117 | 437 | 437 |
| 536142 | 139 | 425 | 425 |
| 536142 | 205 | 421 | 421 |
| 536142 | 124 | 409 | 409 |
| 536142 | 36 | 400 | 400 |
| 536142 | 134 | 398 | 398 |
| 536142 | 9 | 377 | 377 |
| 536142 | 107 | 371 | 371 |
| 536142 | 13 | 357 | 357 |
| 536142 | 1 | 341 | 341 |
| 536142 | 45 | 341 | 341 |
| 536142 | 183 | 314 | 314 |
| 536142 | 97 | 305 | 305 |
| 536142 | 19 | 303 | 303 |
| 536142 | 112 | 302 | 302 |
| 536142 | 67 | 299 | 299 |
| 536142 | 30 | 298 | 298 |
| 536142 | 34 | 275 | 275 |
| 536142 | 142 | 275 | 275 |
| 536142 | 119 | 272 | 272 |
| 536142 | 187 | 271 | 271 |
| 536142 | 49 | 265 | 265 |
| 536142 | 178 | 248 | 248 |
| 536142 | 201 | 245 | 245 |
| 536142 | 57 | 244 | 244 |
| 536142 | 173 | 241 | 241 |
| 536142 | 174 | 240 | 240 |
| 536142 | 146 | 238 | 238 |
| 536142 | 126 | 237 | 237 |
| 536142 | 70 | 227 | 227 |
| 536142 | 63 | 219 | 219 |
| 536142 | 135 | 213 | 213 |
| 536142 | 64 | 211 | 211 |
| 536142 | 22 | 211 | 211 |
| 536142 | 58 | 209 | 209 |
| 536142 | 47 | 205 | 205 |
| 536142 | 42 | 197 | 197 |
| 536142 | 15 | 197 | 197 |
| 536142 | 155 | 187 | 187 |
| 536142 | 43 | 185 | 185 |
| 536142 | 172 | 184 | 184 |
| 536142 | 66 | 181 | 181 |
| 536142 | 75 | 180 | 180 |
| 536142 | 73 | 179 | 179 |
| 536142 | 69 | 177 | 177 |
| 536142 | 113 | 174 | 174 |
| 536142 | 206 | 170 | 170 |
| 536142 | 179 | 169 | 169 |
| 536142 | 33 | 164 | 164 |
| 536142 | 20 | 161 | 161 |
| 536142 | 103 | 153 | 153 |
| 536142 | 150 | 152 | 152 |
| 536142 | 140 | 150 | 150 |
| 536142 | 94 | 148 | 148 |
| 536142 | 14 | 148 | 148 |
| 536142 | 99 | 145 | 145 |
| 536142 | 171 | 136 | 136 |
| 536142 | 109 | 134 | 134 |
| 536142 | 186 | 134 | 134 |
| 536142 | 180 | 133 | 133 |
| 536142 | 129 | 131 | 131 |
| 536142 | 32 | 129 | 129 |
| 536142 | 46 | 129 | 129 |
| 536142 | 48 | 126 | 126 |
| 536142 | 122 | 126 | 126 |
| 536142 | 147 | 123 | 123 |
| 536142 | 71 | 123 | 123 |
| 536142 | 169 | 119 | 119 |
| 536142 | 158 | 113 | 113 |
| 536142 | 39 | 113 | 113 |
| 536142 | 80 | 111 | 111 |
| 536142 | 51 | 109 | 109 |
| 536142 | 136 | 109 | 109 |
| 536142 | 196 | 109 | 109 |
| 536142 | 31 | 107 | 107 |
| 536142 | 56 | 106 | 106 |
| 536142 | 137 | 106 | 106 |
| 536142 | 21 | 105 | 105 |
| 536142 | 123 | 105 | 105 |
| 536142 | 4 | 103 | 103 |
| 536142 | 164 | 102 | 102 |
| 536142 | 23 | 98 | 98 |
| 536142 | 176 | 95 | 95 |
| 536142 | 145 | 94 | 94 |
| 536142 | 163 | 93 | 93 |
| 536142 | 141 | 93 | 93 |
| 536142 | 200 | 93 | 93 |
| 536142 | 114 | 92 | 92 |
| 536142 | 195 | 91 | 91 |
| 536142 | 85 | 91 | 91 |
| 536142 | 24 | 91 | 91 |
| 536142 | 133 | 90 | 90 |
| 536142 | 127 | 88 | 88 |
| 536142 | 37 | 84 | 84 |
| 536142 | 10 | 84 | 84 |
| 536142 | 190 | 82 | 82 |
| 536142 | 26 | 80 | 80 |
| 536142 | 111 | 79 | 79 |
| 536142 | 52 | 78 | 78 |
| 536142 | 128 | 78 | 78 |
| 536142 | 143 | 78 | 78 |
| 536142 | 157 | 75 | 75 |
| 536142 | 151 | 74 | 74 |
| 536142 | 72 | 73 | 73 |
| 536142 | 74 | 72 | 72 |
| 536142 | 166 | 72 | 72 |
| 536142 | 110 | 72 | 72 |
| 536142 | 44 | 71 | 71 |
| 536142 | 87 | 70 | 70 |
| 536142 | 156 | 70 | 70 |
| 536142 | 41 | 69 | 69 |
| 536142 | 189 | 68 | 68 |
| 536142 | 102 | 67 | 67 |
| 536142 | 105 | 63 | 63 |
| 536142 | 120 | 62 | 62 |
| 536142 | 88 | 61 | 61 |
| 536142 | 106 | 59 | 59 |
| 536142 | 125 | 59 | 59 |
| 536142 | 148 | 58 | 58 |
| 536142 | 159 | 58 | 58 |
| 536142 | 175 | 54 | 54 |
| 536142 | 138 | 54 | 54 |
| 536142 | 38 | 54 | 54 |
| 536142 | 76 | 54 | 54 |
| 536142 | 149 | 52 | 52 |
| 536142 | 84 | 52 | 52 |
| 536142 | 3 | 51 | 51 |
| 536142 | 60 | 51 | 51 |
| 536142 | 181 | 50 | 50 |
| 536142 | 116 | 49 | 49 |
| 536142 | 197 | 48 | 48 |
| 536142 | 92 | 48 | 48 |
| 536142 | 89 | 47 | 47 |
| 536142 | 204 | 47 | 47 |
| 536142 | 193 | 47 | 47 |
| 536142 | 90 | 46 | 46 |
| 536142 | 132 | 43 | 43 |
| 536142 | 207 | 43 | 43 |
| 536142 | 154 | 43 | 43 |
| 536142 | 55 | 42 | 42 |
| 536142 | 17 | 40 | 40 |
| 536142 | 184 | 40 | 40 |
| 536142 | 93 | 40 | 40 |
| 536142 | 202 | 39 | 39 |
| 536142 | 121 | 35 | 35 |
| 536142 | 182 | 34 | 34 |
| 536142 | 65 | 33 | 33 |
| 536142 | 177 | 31 | 31 |
| 536142 | 152 | 31 | 31 |
| 536142 | 160 | 30 | 30 |
| 536142 | 50 | 29 | 29 |
| 536142 | 27 | 27 | 27 |
| 536142 | 59 | 27 | 27 |
| 536142 | 131 | 27 | 27 |
| 536142 | 185 | 25 | 25 |
| 536142 | 81 | 24 | 24 |
| 536142 | 79 | 24 | 24 |
| 536142 | 83 | 24 | 24 |
| 536142 | 54 | 22 | 22 |
| 536142 | 104 | 21 | 21 |
| 536142 | 82 | 19 | 19 |
| 536142 | 77 | 18 | 18 |
| 536142 | 68 | 18 | 18 |
| 536142 | 167 | 16 | 16 |
| 536142 | 115 | 15 | 15 |
| 536142 | 209 | 15 | 15 |
| 536142 | 161 | 13 | 13 |
| 536142 | 108 | 12 | 12 |
| 536142 | 53 | 10 | 10 |
| 536142 | 191 | 9 | 9 |
| 536142 | 165 | 8 | 8 |
| 536142 | 210 | 7 | 7 |
| 536142 | 188 | 3 | 3 |
| 536142 | 162 | 3 | 3 |
| 536142 | 78 | 1 | 1 |
| 538917 | 2 | 6570 | 6570 |
| 538917 | 192 | 5645 | 5645 |
| 538917 | 101 | 5477 | 5477 |
| 538917 | 25 | 4366 | 4366 |
| 538917 | 86 | 4124 | 4124 |
| 538917 | 98 | 3711 | 3711 |
| 538917 | 5 | 3585 | 3585 |
| 538917 | 40 | 3496 | 3496 |
| 538917 | 35 | 3297 | 3297 |
| 538917 | 12 | 2940 | 2940 |
| 538917 | 6 | 2854 | 2854 |
| 538917 | 170 | 2623 | 2623 |
| 538917 | 29 | 2599 | 2599 |
| 538917 | 7 | 2471 | 2471 |
| 538917 | 18 | 2425 | 2425 |
| 538917 | 28 | 2358 | 2358 |
| 538917 | 11 | 2301 | 2301 |
| 538917 | 61 | 2270 | 2270 |
| 538917 | 130 | 2180 | 2180 |
| 538917 | 198 | 2039 | 2039 |
| 538917 | 91 | 1949 | 1949 |
| 538917 | 95 | 1911 | 1911 |
| 538917 | 168 | 1842 | 1842 |
| 538917 | 67 | 1741 | 1741 |
| 538917 | 118 | 1692 | 1692 |
| 538917 | 194 | 1679 | 1679 |
| 538917 | 36 | 1633 | 1633 |
| 538917 | 9 | 1629 | 1629 |
| 538917 | 205 | 1626 | 1626 |
| 538917 | 96 | 1538 | 1538 |
| 538917 | 16 | 1489 | 1489 |
| 538917 | 107 | 1473 | 1473 |
| 538917 | 199 | 1458 | 1458 |
| 538917 | 62 | 1439 | 1439 |
| 538917 | 19 | 1437 | 1437 |
| 538917 | 117 | 1386 | 1386 |
| 538917 | 100 | 1372 | 1372 |
| 538917 | 30 | 1366 | 1366 |
| 538917 | 34 | 1299 | 1299 |
| 538917 | 13 | 1265 | 1265 |
| 538917 | 124 | 1230 | 1230 |
| 538917 | 203 | 1222 | 1222 |
| 538917 | 142 | 1200 | 1200 |
| 538917 | 49 | 1195 | 1195 |
| 538917 | 97 | 1174 | 1174 |
| 538917 | 112 | 1166 | 1166 |
| 538917 | 45 | 1146 | 1146 |
| 538917 | 58 | 1065 | 1065 |
| 538917 | 63 | 1021 | 1021 |
| 538917 | 64 | 965 | 965 |
| 538917 | 187 | 958 | 958 |
| 538917 | 201 | 943 | 943 |
| 538917 | 146 | 941 | 941 |
| 538917 | 144 | 938 | 938 |
| 538917 | 42 | 922 | 922 |
| 538917 | 183 | 902 | 902 |
| 538917 | 70 | 870 | 870 |
| 538917 | 135 | 859 | 859 |
| 538917 | 66 | 854 | 854 |
| 538917 | 69 | 834 | 834 |
| 538917 | 47 | 833 | 833 |
| 538917 | 43 | 830 | 830 |
| 538917 | 57 | 816 | 816 |
| 538917 | 33 | 808 | 808 |
| 538917 | 22 | 799 | 799 |
| 538917 | 20 | 782 | 782 |
| 538917 | 14 | 756 | 756 |
| 538917 | 73 | 739 | 739 |
| 538917 | 15 | 688 | 688 |
| 538917 | 139 | 686 | 686 |
| 538917 | 75 | 685 | 685 |
| 538917 | 99 | 665 | 665 |
| 538917 | 206 | 660 | 660 |
| 538917 | 71 | 657 | 657 |
| 538917 | 94 | 636 | 636 |
| 538917 | 113 | 635 | 635 |
| 538917 | 109 | 629 | 629 |
| 538917 | 103 | 629 | 629 |
| 538917 | 126 | 626 | 626 |
| 538917 | 1 | 624 | 624 |
| 538917 | 46 | 614 | 614 |
| 538917 | 32 | 613 | 613 |
| 538917 | 8 | 607 | 607 |
| 538917 | 153 | 601 | 601 |
| 538917 | 155 | 597 | 597 |
| 538917 | 48 | 596 | 596 |
| 538917 | 122 | 591 | 591 |
| 538917 | 186 | 589 | 589 |
| 538917 | 150 | 564 | 564 |
| 538917 | 208 | 564 | 564 |
| 538917 | 123 | 560 | 560 |
| 538917 | 140 | 550 | 550 |
| 538917 | 56 | 538 | 538 |
| 538917 | 147 | 515 | 515 |
| 538917 | 169 | 514 | 514 |
| 538917 | 180 | 501 | 501 |
| 538917 | 51 | 501 | 501 |
| 538917 | 80 | 500 | 500 |
| 538917 | 39 | 490 | 490 |
| 538917 | 4 | 474 | 474 |
| 538917 | 31 | 473 | 473 |
| 538917 | 37 | 470 | 470 |
| 538917 | 134 | 469 | 469 |
| 538917 | 21 | 466 | 466 |
| 538917 | 141 | 463 | 463 |
| 538917 | 85 | 454 | 454 |
| 538917 | 10 | 453 | 453 |
| 538917 | 129 | 445 | 445 |
| 538917 | 41 | 426 | 426 |
| 538917 | 133 | 424 | 424 |
| 538917 | 24 | 413 | 413 |
| 538917 | 196 | 409 | 409 |
| 538917 | 119 | 401 | 401 |
| 538917 | 174 | 398 | 398 |
| 538917 | 145 | 393 | 393 |
| 538917 | 136 | 388 | 388 |
| 538917 | 137 | 383 | 383 |
| 538917 | 195 | 380 | 380 |
| 538917 | 44 | 377 | 377 |
| 538917 | 158 | 376 | 376 |
| 538917 | 23 | 374 | 374 |
| 538917 | 114 | 367 | 367 |
| 538917 | null | 363 | 363 |
| 538917 | 52 | 362 | 362 |
| 538917 | 164 | 340 | 340 |
| 538917 | 127 | 338 | 338 |
| 538917 | 157 | 337 | 337 |
| 538917 | 111 | 327 | 327 |
| 538917 | 106 | 326 | 326 |
| 538917 | 156 | 315 | 315 |
| 538917 | 26 | 310 | 310 |
| 538917 | 72 | 303 | 303 |
| 538917 | 189 | 296 | 296 |
| 538917 | 166 | 289 | 289 |
| 538917 | 76 | 285 | 285 |
| 538917 | 88 | 283 | 283 |
| 538917 | 105 | 283 | 283 |
| 538917 | 190 | 279 | 279 |
| 538917 | 110 | 269 | 269 |
| 538917 | 125 | 264 | 264 |
| 538917 | 89 | 264 | 264 |
| 538917 | 74 | 260 | 260 |
| 538917 | 92 | 257 | 257 |
| 538917 | 128 | 250 | 250 |
| 538917 | 207 | 250 | 250 |
| 538917 | 148 | 241 | 241 |
| 538917 | 3 | 238 | 238 |
| 538917 | 132 | 233 | 233 |
| 538917 | 197 | 231 | 231 |
| 538917 | 138 | 229 | 229 |
| 538917 | 143 | 219 | 219 |
| 538917 | 173 | 216 | 216 |
| 538917 | 149 | 215 | 215 |
| 538917 | 120 | 212 | 212 |
| 538917 | 87 | 212 | 212 |
| 538917 | 81 | 211 | 211 |
| 538917 | 60 | 209 | 209 |
| 538917 | 193 | 207 | 207 |
| 538917 | 90 | 204 | 204 |
| 538917 | 38 | 203 | 203 |
| 538917 | 163 | 201 | 201 |
| 538917 | 102 | 199 | 199 |
| 538917 | 151 | 191 | 191 |
| 538917 | 184 | 180 | 180 |
| 538917 | 116 | 180 | 180 |
| 538917 | 93 | 173 | 173 |
| 538917 | 204 | 172 | 172 |
| 538917 | 179 | 171 | 171 |
| 538917 | 55 | 169 | 169 |
| 538917 | 160 | 167 | 167 |
| 538917 | 27 | 161 | 161 |
| 538917 | 17 | 156 | 156 |
| 538917 | 50 | 156 | 156 |
| 538917 | 202 | 154 | 154 |
| 538917 | 159 | 140 | 140 |
| 538917 | 178 | 138 | 138 |
| 538917 | 54 | 137 | 137 |
| 538917 | 68 | 132 | 132 |
| 538917 | 175 | 129 | 129 |
| 538917 | 84 | 128 | 128 |
| 538917 | 154 | 128 | 128 |
| 538917 | 209 | 126 | 126 |
| 538917 | 59 | 126 | 126 |
| 538917 | 79 | 125 | 125 |
| 538917 | 152 | 120 | 120 |
| 538917 | 83 | 120 | 120 |
| 538917 | 167 | 117 | 117 |
| 538917 | 121 | 117 | 117 |
| 538917 | 77 | 102 | 102 |
| 538917 | 82 | 101 | 101 |
| 538917 | 172 | 100 | 100 |
| 538917 | 185 | 99 | 99 |
| 538917 | 131 | 98 | 98 |
| 538917 | 65 | 93 | 93 |
| 538917 | 200 | 90 | 90 |
| 538917 | 182 | 89 | 89 |
| 538917 | 177 | 80 | 80 |
| 538917 | 115 | 79 | 79 |
| 538917 | 171 | 73 | 73 |
| 538917 | 176 | 72 | 72 |
| 538917 | 108 | 72 | 72 |
| 538917 | 104 | 60 | 60 |
| 538917 | 191 | 55 | 55 |
| 538917 | 161 | 54 | 54 |
| 538917 | 53 | 42 | 42 |
| 538917 | 210 | 32 | 32 |
| 538917 | 181 | 31 | 31 |
| 538917 | 78 | 30 | 30 |
| 538917 | 162 | 27 | 27 |
| 538917 | 165 | 22 | 22 |
| 538917 | 188 | 1 | 1 |
| 543709 | null | 2577 | 2577 |
| 543709 | 12 | 2533 | 2533 |
| 543709 | 101 | 2432 | 2432 |
| 543709 | 2 | 2256 | 2256 |
| 543709 | 25 | 2061 | 2061 |
| 543709 | 86 | 1936 | 1936 |
| 543709 | 36 | 1745 | 1745 |
| 543709 | 18 | 1698 | 1698 |
| 543709 | 5 | 1625 | 1625 |
| 543709 | 192 | 1492 | 1492 |
| 543709 | 6 | 1176 | 1176 |
| 543709 | 98 | 1145 | 1145 |
| 543709 | 170 | 1059 | 1059 |
| 543709 | 40 | 1019 | 1019 |
| 543709 | 28 | 963 | 963 |
| 543709 | 124 | 946 | 946 |
| 543709 | 35 | 940 | 940 |
| 543709 | 117 | 888 | 888 |
| 543709 | 11 | 875 | 875 |
| 543709 | 100 | 844 | 844 |
| 543709 | 96 | 825 | 825 |
| 543709 | 95 | 788 | 788 |
| 543709 | 29 | 777 | 777 |
| 543709 | 91 | 752 | 752 |
| 543709 | 130 | 736 | 736 |
| 543709 | 118 | 736 | 736 |
| 543709 | 107 | 693 | 693 |
| 543709 | 62 | 682 | 682 |
| 543709 | 61 | 661 | 661 |
| 543709 | 9 | 657 | 657 |
| 543709 | 203 | 610 | 610 |
| 543709 | 7 | 595 | 595 |
| 543709 | 45 | 593 | 593 |
| 543709 | 198 | 561 | 561 |
| 543709 | 19 | 548 | 548 |
| 543709 | 67 | 546 | 546 |
| 543709 | 97 | 498 | 498 |
| 543709 | 168 | 488 | 488 |
| 543709 | 30 | 476 | 476 |
| 543709 | 199 | 448 | 448 |
| 543709 | 146 | 416 | 416 |
| 543709 | 205 | 408 | 408 |
| 543709 | 194 | 388 | 388 |
| 543709 | 155 | 388 | 388 |
| 543709 | 73 | 387 | 387 |
| 543709 | 69 | 375 | 375 |
| 543709 | 43 | 369 | 369 |
| 543709 | 153 | 343 | 343 |
| 543709 | 47 | 338 | 338 |
| 543709 | 142 | 329 | 329 |
| 543709 | 42 | 328 | 328 |
| 543709 | 15 | 323 | 323 |
| 543709 | 187 | 323 | 323 |
| 543709 | 16 | 318 | 318 |
| 543709 | 22 | 313 | 313 |
| 543709 | 34 | 311 | 311 |
| 543709 | 64 | 306 | 306 |
| 543709 | 32 | 298 | 298 |
| 543709 | 112 | 285 | 285 |
| 543709 | 183 | 278 | 278 |
| 543709 | 33 | 255 | 255 |
| 543709 | 20 | 245 | 245 |
| 543709 | 58 | 235 | 235 |
| 543709 | 4 | 228 | 228 |
| 543709 | 63 | 228 | 228 |
| 543709 | 140 | 219 | 219 |
| 543709 | 13 | 218 | 218 |
| 543709 | 71 | 216 | 216 |
| 543709 | 46 | 213 | 213 |
| 543709 | 51 | 194 | 194 |
| 543709 | 114 | 191 | 191 |
| 543709 | 8 | 187 | 187 |
| 543709 | 141 | 185 | 185 |
| 543709 | 66 | 184 | 184 |
| 543709 | 144 | 178 | 178 |
| 543709 | 57 | 176 | 176 |
| 543709 | 147 | 164 | 164 |
| 543709 | 135 | 163 | 163 |
| 543709 | 31 | 161 | 161 |
| 543709 | 136 | 155 | 155 |
| 543709 | 49 | 153 | 153 |
| 543709 | 37 | 152 | 152 |
| 543709 | 23 | 148 | 148 |
| 543709 | 150 | 148 | 148 |
| 543709 | 39 | 146 | 146 |
| 543709 | 103 | 145 | 145 |
| 543709 | 99 | 145 | 145 |
| 543709 | 139 | 137 | 137 |
| 543709 | 208 | 137 | 137 |
| 543709 | 70 | 135 | 135 |
| 543709 | 122 | 131 | 131 |
| 543709 | 134 | 131 | 131 |
| 543709 | 94 | 128 | 128 |
| 543709 | 21 | 126 | 126 |
| 543709 | 1 | 122 | 122 |
| 543709 | 56 | 122 | 122 |
| 543709 | 126 | 118 | 118 |
| 543709 | 201 | 117 | 117 |
| 543709 | 129 | 110 | 110 |
| 543709 | 180 | 107 | 107 |
| 543709 | 14 | 106 | 106 |
| 543709 | 109 | 104 | 104 |
| 543709 | 159 | 103 | 103 |
| 543709 | 75 | 98 | 98 |
| 543709 | 123 | 97 | 97 |
| 543709 | 119 | 96 | 96 |
| 543709 | 80 | 96 | 96 |
| 543709 | 10 | 96 | 96 |
| 543709 | 206 | 95 | 95 |
| 543709 | 137 | 93 | 93 |
| 543709 | 48 | 89 | 89 |
| 543709 | 41 | 88 | 88 |
| 543709 | 156 | 88 | 88 |
| 543709 | 174 | 87 | 87 |
| 543709 | 24 | 86 | 86 |
| 543709 | 169 | 84 | 84 |
| 543709 | 163 | 84 | 84 |
| 543709 | 186 | 83 | 83 |
| 543709 | 195 | 82 | 82 |
| 543709 | 105 | 81 | 81 |
| 543709 | 132 | 80 | 80 |
| 543709 | 113 | 80 | 80 |
| 543709 | 85 | 79 | 79 |
| 543709 | 52 | 77 | 77 |
| 543709 | 127 | 76 | 76 |
| 543709 | 72 | 76 | 76 |
| 543709 | 26 | 72 | 72 |
| 543709 | 133 | 71 | 71 |
| 543709 | 166 | 68 | 68 |
| 543709 | 138 | 67 | 67 |
| 543709 | 93 | 67 | 67 |
| 543709 | 145 | 66 | 66 |
| 543709 | 74 | 65 | 65 |
| 543709 | 77 | 64 | 64 |
| 543709 | 196 | 62 | 62 |
| 543709 | 81 | 61 | 61 |
| 543709 | 116 | 60 | 60 |
| 543709 | 76 | 59 | 59 |
| 543709 | 176 | 59 | 59 |
| 543709 | 111 | 58 | 58 |
| 543709 | 158 | 58 | 58 |
| 543709 | 148 | 57 | 57 |
| 543709 | 17 | 56 | 56 |
| 543709 | 3 | 55 | 55 |
| 543709 | 164 | 54 | 54 |
| 543709 | 89 | 53 | 53 |
| 543709 | 149 | 53 | 53 |
| 543709 | 151 | 52 | 52 |
| 543709 | 157 | 51 | 51 |
| 543709 | 92 | 50 | 50 |
| 543709 | 209 | 50 | 50 |
| 543709 | 90 | 50 | 50 |
| 543709 | 60 | 50 | 50 |
| 543709 | 197 | 49 | 49 |
| 543709 | 88 | 48 | 48 |
| 543709 | 120 | 48 | 48 |
| 543709 | 106 | 47 | 47 |
| 543709 | 190 | 46 | 46 |
| 543709 | 87 | 45 | 45 |
| 543709 | 102 | 43 | 43 |
| 543709 | 125 | 42 | 42 |
| 543709 | 38 | 41 | 41 |
| 543709 | 121 | 41 | 41 |

  Counts matching

### Inventory (Asset chain)

### Columns Present in Hoover but not in Hoover++ view

| # | Column |
| --- | --- |
| 1 | `inventory__asset_chain__flags` |
| 2 | `inventory__asset_chain__reseller_network_id` |
| 3 | `inventory__asset_chain__revenue` |
| 4 | `inventory__asset_chain__content_owner_revenue` |
| 5 | `inventory__asset_chain__distributor_revenue` |
| 6 | `inventory__asset_chain__reseller_revenue` |
| 7 | `inventory__asset_chain__bidding_revenue` |
| 8 | `inventory__asset_chain__bidding_up_revenue` |
| 9 | `inventory__asset_chain__content_owner_bidding_revenue` |
| 10 | `inventory__asset_chain__content_owner_bidding_modified_revenue` |
| 11 | `inventory__asset_chain__content_owner_bidding_original_revenue` |
| 12 | `inventory__asset_chain__distributor_bidding_revenue` |
| 13 | `inventory__asset_chain__reseller_bidding_revenue` |
| 14 | `inventory__asset_chain__ssp_clearing_revenue` |
| 15 | `inventory__asset_chain__margin` |
| 16 | `inventory__asset_chain__competition_resellers` |
| 17 | `inventory__asset_chain__rule_id` |
| 18 | `inventory__asset_chain__rule_ext_id` |
| 19 | `inventory__asset_chain__rule_flags` |
| 20 | `inventory__asset_chain__rule_type_priority` |
| 21 | `inventory__asset_chain__unified_rule_priority` |
| 22 | `inventory__asset_chain__unified_rule_priority__priority_tier` |
| 23 | `inventory__asset_chain__unified_rule_priority__sub_priority_value` |
| 24 | `inventory__asset_chain__site_group_id` |
| 25 | `inventory__asset_chain__airing_channel_group_id` |
| 26 | `inventory__asset_chain__edge_postal_code_package_ids` |
| 27 | `inventory__asset_chain__inbound_rule_id` |
| 28 | `inventory__asset_chain__listing_id` |
| 29 | `inventory__asset_chain__inbound_listing_id` |
| 30 | `inventory__asset_chain__inbound_order_id` |
| 31 | `inventory__asset_chain__inbound_order_type` |
| 32 | `inventory__asset_chain__inbound_order_auction_type` |
| 33 | `inventory__asset_chain__inbound_order_transaction_type` |
| 34 | `inventory__asset_chain__upstream_inbound_order_id` |
| 35 | `inventory__asset_chain__upstream_global_currency_id` |
| 36 | `inventory__asset_chain__upstream_content_owner_revenue_in_up_currency` |
| 37 | `inventory__asset_chain__outbound_order_id` |
| 38 | `inventory__asset_chain__outbound_order_type` |
| 39 | `inventory__asset_chain__outbound_exchange_order_id` |
| 40 | `inventory__asset_chain__outbound_listing_id` |
| 41 | `inventory__asset_chain__unified_outbound_order_priority` |
| 42 | `inventory__asset_chain__unified_outbound_order_priority__priority_tier` |
| 43 | `inventory__asset_chain__unified_outbound_order_priority__sub_priority_value` |
| 44 | `inventory__asset_chain__outbound_order_transaction_type` |
| 45 | `inventory__asset_chain__outbound_order_priority_type` |
| 46 | `inventory__asset_chain__avails_category` |
| 47 | `inventory__asset_chain__avails_category__avails` |
| 48 | `inventory__asset_chain__avails_category__unfilled_avails` |
| 49 | `inventory__asset_chain__avails_category__unconstrained_avails` |
| 50 | `inventory__asset_chain__avails_category__market_avails` |
| 51 | `inventory__asset_chain__avails_category__ssp_avails` |
| 52 | `inventory__asset_chain__avails_category__avails_in_played_slot` |
| 53 | `inventory__asset_chain__avails_category__unfilled_avails_in_played_slot` |
| 54 | `inventory__asset_chain__avails_category__unconstrained_avails_in_played_slot` |
| 55 | `inventory__asset_chain__avails_category__raw_total_avails_in_played_slot` |
| 56 | `inventory__asset_chain__avails_category__market_avails_in_played_slot` |
| 57 | `inventory__asset_chain__avails_category__ssp_avails_in_played_slot` |
| 58 | `inventory__asset_chain__avails_category__total_avails` |
| 59 | `inventory__asset_chain__avails_category__total_unfilled_avails` |
| 60 | `inventory__asset_chain__avails_category__opportunity` |
| 61 | `inventory__asset_chain__avails_category__total_avails_in_played_slot` |
| 62 | `inventory__asset_chain__avails_category__total_unfilled_avails_in_played_slot` |
| 63 | `inventory__asset_chain__avails_category__opportunity_in_played_slot` |
| 64 | `inventory__asset_chain__avails_category__raw_opportunity_in_played_slot` |
| 65 | `inventory__asset_chain__avails_category__slot_opp_avails_in_played_slot` |
| 66 | `inventory__asset_chain__avails_category__remaining_avails` |
| 67 | `inventory__asset_chain__avails_category__vod_programmer_total_avails` |
| 68 | `inventory__asset_chain__avails_category__distinct_inventory_avails` |
| 69 | `inventory__asset_chain__avails_category__inventory_avails` |
| 70 | `inventory__asset_chain__avails_category__raw_inventory_distinct_avails_in_played_slot` |
| 71 | `inventory__asset_chain__outbound_rules` |
| 72 | `inventory__asset_chain__outbound_rules__rule_id` |
| 73 | `inventory__asset_chain__outbound_rules__total_opp` |
| 74 | `inventory__asset_chain__outbound_rules__win_opp` |
| 75 | `inventory__asset_chain__eligible_outbound_orders` |
| 76 | `inventory__asset_chain__eligible_outbound_orders__down_network_id` |
| 77 | `inventory__asset_chain__eligible_outbound_orders__order_id` |
| 78 | `inventory__asset_chain__eligible_outbound_orders__order_type` |
| 79 | `inventory__asset_chain__eligible_outbound_orders__exchange_order_id` |
| 80 | `inventory__asset_chain__eligible_outbound_orders__listing_id` |
| 81 | `inventory__asset_chain__eligible_outbound_orders__matched_inventory_package_ids` |
| 82 | `inventory__asset_chain__eligible_outbound_orders__bit_flags` |
| 83 | `inventory__asset_chain__eligible_outbound_orders__order_transaction_type` |
| 84 | `inventory__asset_chain__eligible_outbound_orders__order_priority` |
| 85 | `inventory__asset_chain__eligible_outbound_orders__sales_channel` |
| 86 | `inventory__asset_chain__eligible_outbound_orders__avails_category` |
| 87 | `inventory__asset_chain__eligible_outbound_orders__avails_category__avails` |
| 88 | `inventory__asset_chain__eligible_outbound_orders__avails_category__unfilled_avails` |
| 89 | `inventory__asset_chain__eligible_outbound_orders__avails_category__unconstrained_avails` |
| 90 | `inventory__asset_chain__eligible_outbound_orders__avails_category__market_avails` |
| 91 | `inventory__asset_chain__eligible_outbound_orders__avails_category__ssp_avails` |
| 92 | `inventory__asset_chain__eligible_outbound_orders__avails_category__avails_in_played_slot` |
| 93 | `inventory__asset_chain__eligible_outbound_orders__avails_category__unfilled_avails_in_played_slot` |
| 94 | `inventory__asset_chain__eligible_outbound_orders__avails_category__unconstrained_avails_in_played_slot` |
| 95 | `inventory__asset_chain__eligible_outbound_orders__avails_category__raw_total_avails_in_played_slot` |
| 96 | `inventory__asset_chain__eligible_outbound_orders__avails_category__market_avails_in_played_slot` |
| 97 | `inventory__asset_chain__eligible_outbound_orders__avails_category__ssp_avails_in_played_slot` |
| 98 | `inventory__asset_chain__eligible_outbound_orders__avails_category__total_avails` |
| 99 | `inventory__asset_chain__eligible_outbound_orders__avails_category__total_unfilled_avails` |
| 100 | `inventory__asset_chain__eligible_outbound_orders__avails_category__opportunity` |
| 101 | `inventory__asset_chain__eligible_outbound_orders__avails_category__total_avails_in_played_slot` |
| 102 | `inventory__asset_chain__eligible_outbound_orders__avails_category__total_unfilled_avails_in_played_slot` |
| 103 | `inventory__asset_chain__eligible_outbound_orders__avails_category__opportunity_in_played_slot` |
| 104 | `inventory__asset_chain__eligible_outbound_orders__avails_category__raw_opportunity_in_played_slot` |
| 105 | `inventory__asset_chain__eligible_outbound_orders__avails_category__slot_opp_avails_in_played_slot` |
| 106 | `inventory__asset_chain__eligible_outbound_orders__avails_category__remaining_avails` |
| 107 | `inventory__asset_chain__eligible_outbound_orders__avails_category__vod_programmer_total_avails` |
| 108 | `inventory__asset_chain__eligible_outbound_orders__avails_category__distinct_inventory_avails` |
| 109 | `inventory__asset_chain__eligible_outbound_orders__avails_category__inventory_avails` |
| 110 | `inventory__asset_chain__eligible_outbound_orders__avails_category__raw_inventory_distinct_avails_in_played_slot` |
| 111 | `inventory__asset_chain__eligible_outbound_orders__count_true_avails_as_booked` |
| 112 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status` |
| 113 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__available_duration` |
| 114 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__filled_ad_num` |
| 115 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__filled_duration` |
| 116 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__unified_unfilled_opp` |
| 117 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__default_unfilled_opp` |
| 118 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__initial_filled_ad_num` |
| 119 | `inventory__asset_chain__eligible_outbound_orders__ad_filling_status__initial_filled_duration` |
| 120 | `inventory__asset_chain__outbound_exchange_listings` |
| 121 | `inventory__asset_chain__outbound_exchange_listings__listing_ids` |
| 122 | `inventory__asset_chain__outbound_exchange_listings__avails_metrics` |
| 123 | `inventory__asset_chain__outbound_exchange_listings__avails_metrics__default_duration` |
| 124 | `inventory__asset_chain__outbound_exchange_listings__avails_metrics__opportunity` |
| 125 | `inventory__asset_chain__outbound_exchange_listings__avails_metrics__avails` |
| 126 | `inventory__asset_chain__outbound_exchange_listings__avails_metrics__unfilled_avails` |
| 127 | `inventory__asset_chain__non_tracked_audience_item_ids` |
| 128 | `inventory__asset_chain__marketplace_audience_extension_deal_ids` |
| 129 | `inventory__asset_chain__portfolio_ids` |
| 130 | `inventory__asset_chain__network_is_ad_owner` |
| 131 | `inventory__asset_chain__network_is_ad_unit_owner` |
| 132 | `inventory__asset_chain__network_is_extra_item_owner` |
| 133 | `inventory__asset_chain__network_is_vod_programmer` |
| 134 | `inventory__asset_chain__count_imp_as_booked` |
| 135 | `inventory__asset_chain__deal_awareability` |
| 136 | `inventory__asset_chain__demand_dim_awareability` |
| 137 | `inventory__asset_chain__carriage_inventory_owner_id` |
| 138 | `inventory__asset_chain__carriage_listing_split_unit_id` |
| 139 | `inventory__asset_chain__eligible_carriage_listing_split_unit_ids` |
| 140 | `inventory__asset_chain__ad_priority_bucket` |
| 141 | `inventory__asset_chain__supply_source` |
| 142 | `inventory__asset_chain__supply_source_type` |
| 143 | `inventory__asset_chain__sales_channel` |
| 144 | `inventory__asset_chain__programmatic_exchange_rate_to_usd` |
| 145 | `inventory__asset_chain__programmatic_exchange_rate_to_eur` |
| 146 | `inventory__asset_chain__bidder_seat_id` |
| 147 | `inventory__asset_chain__global_currency_id` |
| 148 | `inventory__asset_chain__floor_price` |
| 149 | `inventory__asset_chain__ad_unit_default_duration` |
| 150 | `inventory__asset_chain__ad_filling_status` |
| 151 | `inventory__asset_chain__ad_filling_status__available_duration` |
| 152 | `inventory__asset_chain__ad_filling_status__filled_ad_num` |
| 153 | `inventory__asset_chain__ad_filling_status__filled_duration` |
| 154 | `inventory__asset_chain__ad_filling_status__unified_unfilled_opp` |
| 155 | `inventory__asset_chain__ad_filling_status__default_unfilled_opp` |
| 156 | `inventory__asset_chain__ad_filling_status__initial_filled_ad_num` |
| 157 | `inventory__asset_chain__ad_filling_status__initial_filled_duration` |
| 158 | `inventory__asset_chain__priority_tier` |
| 159 | `inventory__asset_chain__priority_value` |
| 160 | `inventory__asset_chain__priority_type` |
| 161 | `inventory__asset_chain__supply_acquisition_cost` |
| 162 | `inventory__asset_chain__supply_distribution_cost` |
| 163 | `inventory__asset_chain__internal_deal_ids` |
| 164 | `inventory__asset_chain__inbound_order_ids` |
| 165 | `inventory__asset_chain__inbound_listing_ids` |
| 166 | `inventory__asset_chain__buyer_ids` |
| 167 | `inventory__asset_chain__internal_seat_ids` |
| 168 | `inventory__asset_chain__outbound_order_ids` |
| 169 | `inventory__asset_chain__outbound_exchange_order_ids` |
| 170 | `inventory__asset_chain__matched_yield_optimization_ids` |
| 171 | `inventory__asset_chain__selected_yield_optimization_ids` |
| 172 | `inventory__asset_chain__selected_yield_optimization_info_ids` |
| 173 | `inventory__asset_chain__matched_inventory_package_ids` |
| 174 | `inventory__asset_chain__matched_audience_item_ids` |
| 175 | `inventory__asset_chain__matched_key_value_ids` |
| 176 | `inventory__asset_chain__matched_daypart` |
| 177 | `inventory__asset_chain__network_selection_info` |
| 178 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics` |
| 179 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics` |
| 180 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__input_ad_number` |
| 181 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__output_ad_number` |
| 182 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__data_privacy` |
| 183 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__restriction` |
| 184 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__unmapped` |
| 185 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__undefined` |
| 186 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics` |
| 187 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__input_ad_number` |
| 188 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__output_ad_number` |
| 189 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_ad_domain` |
| 190 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_slot_assigned_through_mrm_rule` |
| 191 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__frequency_cap` |
| 192 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__cpx_check_failed` |
| 193 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_schedule` |
| 194 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__rbp_check_failed` |
| 195 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot` |
| 196 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__sponsorship_check_failed` |
| 197 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__exclusivity_check_failed` |
| 198 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_user_experience` |
| 199 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_no_external_rule` |
| 200 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_resellable` |
| 201 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_promo_only` |
| 202 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_compatible` |
| 203 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_budget` |
| 204 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_yield_optimization` |
| 205 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__unmapped` |
| 206 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__undefined` |
| 207 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__ad_truncation` |
| 208 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics` |
| 209 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__input_ad_number` |
| 210 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__output_ad_number` |
| 211 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__frequency_cap` |
| 212 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot` |
| 213 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__compliance_check_failed` |
| 214 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative` |
| 215 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_suitable_rule_path` |
| 216 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__profile_check_failed` |
| 217 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__floor_price_not_met` |
| 218 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__restriction` |
| 219 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__exclusivity` |
| 220 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__pg_deal_bid_throttling` |
| 221 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__auction_max_ad_duration` |
| 222 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__reseller_restriction` |
| 223 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__market_ad_not_approved` |
| 224 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__listing_creative_duration_check_failed` |
| 225 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_ad_asset_store_availability` |
| 226 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_bitrate_check_failed` |
| 227 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_creative_targeting_check_failed` |
| 228 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_date_range_check_failed` |
| 229 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_max_ad_duration_check_failed` |
| 230 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_compatible_dimension_check_failed` |
| 231 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inventory_source_restriction` |
| 232 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_not_compatible` |
| 233 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_excluded_by_sponsor` |
| 234 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__met_yield_optimization` |
| 235 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__mpe_listing_restriction` |
| 236 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__unmapped` |
| 237 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__undefined` |
| 238 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inbound_order_competition_failure` |
| 239 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__competition_failure_in_pick_many` |
| 240 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics` |
| 241 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__input_ad_number` |
| 242 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_ad_number` |
| 243 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_num_ads` |
| 244 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_duration` |
| 245 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__time_based_freq_cap` |
| 246 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__no_creative` |
| 247 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__companion_check_failed` |
| 248 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__pod_position_targeting_check_failed` |
| 249 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_exclusivity_check_failed` |
| 250 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_sponsorship_check_failed` |
| 251 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_filled_by_multi_ad` |
| 252 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_fallback_ad_number` |
| 253 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_not_found` |
| 254 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__do_not_repeat` |
| 255 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__unmapped` |
| 256 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__undefined` |
| 257 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__network_id` |
| 258 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__demand_type` |
| 259 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__order_id` |
| 260 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__listing_ids` |
| 261 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics` |
| 262 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__phase` |
| 263 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__name` |
| 264 | `inventory__asset_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__value` |
| 265 | `inventory__asset_chain__inventory_distribution_contexts` |
| 266 | `inventory__asset_chain__inventory_distribution_contexts__carriage_inventory_owner_id` |
| 267 | `inventory__asset_chain__inventory_distribution_contexts__carriage_listing_split_unit_id` |
| 268 | `inventory__asset_chain__mapped_asset_ids` |
| 269 | `inventory__asset_chain__mapped_site_section_ids` |
| 270 | `inventory__asset_chain__selected_yo_volume_cap_ids` |
| 271 | `inventory__asset_chain__selected_yo_distribution_id` |
| 272 | `inventory__asset_chain__selected_yo_distribution_nip_id` |
| 273 | `inventory__asset_chain__selected_yo_inventory_prioritization_id` |
| 274 | `inventory__asset_chain__selected_yo_inventory_prioritization_nip_id` |
| 275 | `inventory__asset_chain__selected_yo_margin_id` |
| 276 | `inventory__asset_chain__audience_segment_max_cpm` |
| 277 | `inventory__asset_chain__audience_partner_segment_infos` |
| 278 | `inventory__asset_chain__audience_partner_segment_infos__audience_partner_id` |
| 279 | `inventory__asset_chain__audience_partner_segment_infos__max_cpm` |
| 280 | `inventory__asset_chain__audience_partner_segment_infos__matched_segments` |
| 281 | `inventory__asset_chain__audience_partner_segment_infos__matched_segments__id` |
| 282 | `inventory__asset_chain__audience_partner_segment_infos__matched_segments__cpm` |
| 283 | `inventory__asset_chain__audience_partner_segment_infos__matched_segments__flags` |
| 284 | `inventory__asset_chain__geo_visibility` |
| 285 | `inventory__asset_chain__geo_visibility__targetable` |
| 286 | `inventory__asset_chain__geo_visibility__report_aggregate` |
| 287 | `inventory__asset_chain__geo_visibility__report_event` |

Checking network\_id 516429 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514060105\_091785&externalid=20260514\_060123\_00000\_yrfhq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514060105_091785&externalid=20260514_060123_00000_yrfhq)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514060110\_659640&externalid=20260514\_060149\_00068\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514060110_659640&externalid=20260514_060149_00068_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 128
  Columns B: 128

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (128 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__asset_chain__asset_group_id                       2 row(s)
    inventory__asset_chain__break_id                             2 row(s)
    inventory__asset_chain__opportunity_id                       2 row(s)
    inventory__asset_chain__scenario_id                          2 row(s)
    inventory__asset_chain__custom_platform_ids                  2 row(s)
    inventory__asset_chain__region_ids                           2 row(s)
    inventory__asset_chain__network_execution_ctx_flags          2 row(s)
    inventory__asset_chain__geo_country_visibility               2 row(s)
    inventory__asset_chain__geo_country_visibility__targetable   2 row(s)
    inventory__asset_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__geo_country_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility         2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility   2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_brand_visibility            2 row(s)
    inventory__asset_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_genre_visibility            2 row(s)
    inventory__asset_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__asset_chain__content_rating_visibility            2 row(s)
    inventory__asset_chain__content_rating_visibility__targetable 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_programmer_visibility       2 row(s)
    inventory__asset_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__asset_chain__content_form_visibility              2 row(s)
    inventory__asset_chain__content_form_visibility__targetable  2 row(s)
    inventory__asset_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_form_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_language_visibility         2 row(s)
    inventory__asset_chain__standard_language_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_channel_visibility          2 row(s)
    inventory__asset_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility  2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_series_visibility   2 row(s)
    inventory__asset_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__asset_chain                                       2 row(s)

  Detailed diffs:

  [row=2]
    inventory__asset_chain:
      old.csv: '[{"network_id":516429,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":516429,"distributor_network_id":516429,"asset_id":413467098,"site_section_id":19715213,"series_id":1134473675,"site_id":1212768,"asset_group_ids":[1134439078,1539297779],"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"airing_channel_id":-1,"airing_id":-1,"postal_code_package_id":[8885,9385,11421,11423,11612,11636,11859,12059,12511],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46],"tracked_audience_item_ids":[1311495,1311496,1311497,1406353,1407149,1407151,1407154,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407163,1407164,1407166,1407167,1407168,1407169,1407172,1407173,1407215,1407901,1407906,1407911,1407934,1407935,1408295,1408296,1408297,1408370,1416220,1421323,1421373,1479033,1479034,1479035,1479037,1479038],"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[210565,279585,364094]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_ids":[1134439078,1539297779],"asset_id":413467098,"bit_flags":0,"content_owner_network_id":516429,"context_id":288230376171426957,"distributor_network_id":516429,"entity_source":"inventory","inventory_package_ids":[210565,279585,364094],"network_execution_ctx_index":0,"network_id":516429,"postal_code_package_id":[8885,9385,11421,11423,11612,11636,11859,12059,12511],"role":"CRO","series_id":1134473675,"site_id":1212768,"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"site_section_id":19715213,"tracked_audience_item_ids":[1311495,1311496,1311497,1406353,1407149,1407151,1407154,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407163,1407164,1407166,1407167,1407168,1407169,1407172,1407173,1407215,1407901,1407906,1407911,1407934,1407935,1408295,1408296,1408297,1408370,1416220,1421323,1421373,1479033,1479034,1479035,1479037,1479038],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46]}]'

  [row=3]
    inventory__asset_chain:
      old.csv: '[{"network_id":516429,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":516429,"distributor_network_id":516429,"asset_id":418691252,"site_section_id":19715213,"series_id":1162706512,"site_id":1212768,"asset_group_ids":[1547016268],"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"airing_channel_id":-1,"airing_id":-1,"postal_code_package_id":[11612,11635,11860,12058,12510],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46],"tracked_audience_item_ids":[1406353,1407012,1407147,1407149,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407164,1407169,1407174,1407207,1407208,1407210,1407211,1407212,1407213,1407214,1407215,1407216,1407217,1407904,1407910,1407911,1407913,1407934,1407936,1408293,1408298,1408301,1408303,1408304,1408313,1408364,1408365,1408367,1408370,1408371,1408440,1408442,1408443,1408516,1416220,1428419,1479033,1479034,1479035,1479037,1479038,1479039],"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[226273,279585]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_ids":[1547016268],"asset_id":418691252,"bit_flags":0,"content_owner_network_id":516429,"context_id":288230376171426957,"distributor_network_id":516429,"entity_source":"inventory","inventory_package_ids":[226273,279585],"network_execution_ctx_index":0,"network_id":516429,"postal_code_package_id":[11612,11635,11860,12058,12510],"role":"CRO","series_id":1162706512,"site_id":1212768,"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"site_section_id":19715213,"tracked_audience_item_ids":[1406353,1407012,1407147,1407149,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407164,1407169,1407174,1407207,1407208,1407210,1407211,1407212,1407213,1407214,1407215,1407216,1407217,1407904,1407910,1407911,1407913,1407934,1407936,1408293,1408298,1408301,1408303,1408304,1408313,1408364,1408365,1408367,1408370,1408371,1408440,1408442,1408443,1408516,1416220,1428419,1479033,1479034,1479035,1479037,1479038,1479039],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46]}]'

========================================================================
  END OF REPORT
========================================================================
```


Summary:

1. Expected difference on the **inventory\_\_asset\_chain **columns ordering. 
2. Schema difference

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |

---

Checking network id 538917

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514061735\_099767&externalid=20260514\_061738\_00080\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514061735_099767&externalid=20260514_061738_00080_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514061741\_310584&externalid=20260514\_061818\_00081\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514061741_310584&externalid=20260514_061818_00081_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 128
  Columns B: 128

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (128 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__asset_chain__asset_group_id                       2 row(s)
    inventory__asset_chain__break_id                             2 row(s)
    inventory__asset_chain__opportunity_id                       2 row(s)
    inventory__asset_chain__scenario_id                          2 row(s)
    inventory__asset_chain__custom_platform_ids                  2 row(s)
    inventory__asset_chain__region_ids                           2 row(s)
    inventory__asset_chain__network_execution_ctx_flags          2 row(s)
    inventory__asset_chain__inventory_package_ids                2 row(s)
    inventory__asset_chain__geo_country_visibility               2 row(s)
    inventory__asset_chain__geo_country_visibility__targetable   2 row(s)
    inventory__asset_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__geo_country_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility         2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility   2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_brand_visibility            2 row(s)
    inventory__asset_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_genre_visibility            2 row(s)
    inventory__asset_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__asset_chain__content_rating_visibility            2 row(s)
    inventory__asset_chain__content_rating_visibility__targetable 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_programmer_visibility       2 row(s)
    inventory__asset_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__asset_chain__content_form_visibility              2 row(s)
    inventory__asset_chain__content_form_visibility__targetable  2 row(s)
    inventory__asset_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_form_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_language_visibility         2 row(s)
    inventory__asset_chain__standard_language_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_channel_visibility          2 row(s)
    inventory__asset_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility  2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_series_visibility   2 row(s)
    inventory__asset_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__asset_chain                                       2 row(s)

  Detailed diffs:

  [row=2]
    inventory__asset_chain:
      old.csv: '[{"network_id":538917,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":538917,"distributor_network_id":538917,"asset_id":449733918,"site_section_id":24253642,"site_id":1274911,"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_id":449733918,"bit_flags":0,"content_owner_network_id":538917,"context_id":288230376175965386,"distributor_network_id":538917,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":538917,"role":"CRO","site_id":1274911,"site_section_id":24253642}]'

  [row=3]
    inventory__asset_chain:
      old.csv: '[{"network_id":538917,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":538917,"distributor_network_id":538917,"asset_id":449733918,"site_section_id":24253642,"site_id":1274911,"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_id":449733918,"bit_flags":0,"content_owner_network_id":538917,"context_id":288230376175965386,"distributor_network_id":538917,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":538917,"role":"CRO","site_id":1274911,"site_section_id":24253642}]'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

1. Expected difference on the **inventory\_\_asset\_chain **columns ordering. 
2. Schema difference 

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |

---

Checking network id 112214

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514062804\_008591&externalid=20260514\_062811\_00086\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514062804_008591&externalid=20260514_062811_00086_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514062753\_341546&externalid=20260514\_062904\_00087\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514062753_341546&externalid=20260514_062904_00087_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 128
  Columns B: 128

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (128 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__asset_chain__break_id                             2 row(s)
    inventory__asset_chain__opportunity_id                       2 row(s)
    inventory__asset_chain__scenario_id                          2 row(s)
    inventory__asset_chain__custom_platform_ids                  2 row(s)
    inventory__asset_chain__region_ids                           2 row(s)
    inventory__asset_chain__network_execution_ctx_flags          2 row(s)
    inventory__asset_chain__geo_country_visibility               2 row(s)
    inventory__asset_chain__geo_country_visibility__targetable   2 row(s)
    inventory__asset_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__geo_country_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility         2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility   2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_brand_visibility            2 row(s)
    inventory__asset_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_genre_visibility            2 row(s)
    inventory__asset_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__asset_chain__content_rating_visibility            2 row(s)
    inventory__asset_chain__content_rating_visibility__targetable 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_rating_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_programmer_visibility       2 row(s)
    inventory__asset_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__asset_chain__content_form_visibility              2 row(s)
    inventory__asset_chain__content_form_visibility__targetable  2 row(s)
    inventory__asset_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__content_form_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_language_visibility         2 row(s)
    inventory__asset_chain__standard_language_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_language_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_channel_visibility          2 row(s)
    inventory__asset_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility  2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_series_visibility   2 row(s)
    inventory__asset_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__asset_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__asset_chain                                       2 row(s)
    inventory__asset_chain__asset_group_id                       2 row(s)

  Detailed diffs:

  [row=2]
    inventory__asset_chain:
      old.csv: '[{"network_id":112214,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":112214,"distributor_network_id":112214,"asset_id":-1,"site_section_id":17513277,"site_id":1081628,"asset_group_id":540630,"asset_group_ids":[540630],"site_section_group_ids":[678119,1081570,1081571,1081572,1081573,1081575,1081576,1081579,1081583,1081586,1081592,1094547],"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[334228]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_id":540630,"asset_group_ids":[540630],"asset_id":-1,"bit_flags":0,"content_owner_network_id":112214,"context_id":288230376169225021,"distributor_network_id":112214,"entity_source":"inventory","inventory_package_ids":[334228],"network_execution_ctx_index":0,"network_id":112214,"role":"CRO","site_id":1081628,"site_section_group_ids":[678119,1081570,1081571,1081572,1081573,1081575,1081576,1081579,1081583,1081586,1081592,1094547],"site_section_id":17513277}]'
    inventory__asset_chain__asset_group_id:
      old.csv: '[540630]'
      new.csv: '\\N'

  [row=3]
    inventory__asset_chain:
      old.csv: '[{"network_id":112214,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":112214,"distributor_network_id":112214,"asset_id":-1,"site_section_id":17513277,"site_id":1081628,"asset_group_id":540630,"asset_group_ids":[540630],"site_section_group_ids":[678119,1081570,1081571,1081572,1081573,1081575,1081576,1081579,1081583,1081586,1081592,1094547],"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[334228]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_id":540630,"asset_group_ids":[540630],"asset_id":-1,"bit_flags":0,"content_owner_network_id":112214,"context_id":288230376169225021,"distributor_network_id":112214,"entity_source":"inventory","inventory_package_ids":[334228],"network_execution_ctx_index":0,"network_id":112214,"role":"CRO","site_id":1081628,"site_section_group_ids":[678119,1081570,1081571,1081572,1081573,1081575,1081576,1081579,1081583,1081586,1081592,1094547],"site_section_id":17513277}]'
    inventory__asset_chain__asset_group_id:
      old.csv: '[540630]'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

1. Expected difference on the **inventory\_\_asset\_chain **columns ordering. 
2. **inventory\_\_asset\_chain\_\_asset\_group\_id**is casted as NULL in view definition needs to be updated
3. Schema difference 

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |


---


### Inventory Aggregated Columns (deep dive)

#### **inventory\_\_asset\_chain\_\_network\_id**

| **inventory\_\_asset\_chain\_\_network\_id** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| `[538917]` | `151492` | `151492` | 0 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513090504_136131&externalid=20260513_090506_00077_7uxyb) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513090519_845056&externalid=20260513_090550_00078_7uxyb) |
| `[112214]` | `58942` | `58942` | 0 |  |
| `[516429]` | `57679` | `57679` | 0 |  |

#### **inventory\_\_asset\_chain\_\_role**

| **inventory\_\_asset\_chain\_\_role** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| `[CRO]` | `397558` | `397558` | 0 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515073318_836666&externalid=20260515_073320_00062_bkccs) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515073310_809087&externalid=20260515_073350_00063_bkccs) |
| `[]` | `3` | `3` | 0 |  |

  

### Inventory (Site\_Section chain)

### Columns Present in Hoover but not in Hoover++ view

##   
Columns NOT available in the ETL query (`etl.public_test1."request"`) but present in `mrm_log_flat.default.request`

| # | Column |
| --- | --- |
| 1 | `inventory__site_section_chain__flags` |
| 2 | `inventory__site_section_chain__reseller_network_id` |
| 3 | `inventory__site_section_chain__revenue` |
| 4 | `inventory__site_section_chain__content_owner_revenue` |
| 5 | `inventory__site_section_chain__distributor_revenue` |
| 6 | `inventory__site_section_chain__reseller_revenue` |
| 7 | `inventory__site_section_chain__bidding_revenue` |
| 8 | `inventory__site_section_chain__bidding_up_revenue` |
| 9 | `inventory__site_section_chain__content_owner_bidding_revenue` |
| 10 | `inventory__site_section_chain__content_owner_bidding_modified_revenue` |
| 11 | `inventory__site_section_chain__content_owner_bidding_original_revenue` |
| 12 | `inventory__site_section_chain__distributor_bidding_revenue` |
| 13 | `inventory__site_section_chain__reseller_bidding_revenue` |
| 14 | `inventory__site_section_chain__ssp_clearing_revenue` |
| 15 | `inventory__site_section_chain__margin` |
| 16 | `inventory__site_section_chain__competition_resellers` |
| 17 | `inventory__site_section_chain__rule_id` |
| 18 | `inventory__site_section_chain__rule_ext_id` |
| 19 | `inventory__site_section_chain__rule_flags` |
| 20 | `inventory__site_section_chain__rule_type_priority` |
| 21 | `inventory__site_section_chain__unified_rule_priority` |
| 22 | `inventory__site_section_chain__unified_rule_priority__priority_tier` |
| 23 | `inventory__site_section_chain__unified_rule_priority__sub_priority_value` |
| 24 | `inventory__site_section_chain__site_group_id` |
| 25 | `inventory__site_section_chain__airing_channel_group_id` |
| 26 | `inventory__site_section_chain__edge_postal_code_package_ids` |
| 27 | `inventory__site_section_chain__inbound_rule_id` |
| 28 | `inventory__site_section_chain__listing_id` |
| 29 | `inventory__site_section_chain__inbound_listing_id` |
| 30 | `inventory__site_section_chain__inbound_order_id` |
| 31 | `inventory__site_section_chain__inbound_order_type` |
| 32 | `inventory__site_section_chain__inbound_order_auction_type` |
| 33 | `inventory__site_section_chain__inbound_order_transaction_type` |
| 34 | `inventory__site_section_chain__upstream_inbound_order_id` |
| 35 | `inventory__site_section_chain__upstream_global_currency_id` |
| 36 | `inventory__site_section_chain__upstream_content_owner_revenue_in_up_currency` |
| 37 | `inventory__site_section_chain__outbound_order_id` |
| 38 | `inventory__site_section_chain__outbound_order_type` |
| 39 | `inventory__site_section_chain__outbound_exchange_order_id` |
| 40 | `inventory__site_section_chain__outbound_listing_id` |
| 41 | `inventory__site_section_chain__unified_outbound_order_priority` |
| 42 | `inventory__site_section_chain__unified_outbound_order_priority__priority_tier` |
| 43 | `inventory__site_section_chain__unified_outbound_order_priority__sub_priority_value` |
| 44 | `inventory__site_section_chain__outbound_order_transaction_type` |
| 45 | `inventory__site_section_chain__outbound_order_priority_type` |
| 46 | `inventory__site_section_chain__avails_category` |
| 47 | `inventory__site_section_chain__avails_category__avails` |
| 48 | `inventory__site_section_chain__avails_category__unfilled_avails` |
| 49 | `inventory__site_section_chain__avails_category__unconstrained_avails` |
| 50 | `inventory__site_section_chain__avails_category__market_avails` |
| 51 | `inventory__site_section_chain__avails_category__ssp_avails` |
| 52 | `inventory__site_section_chain__avails_category__avails_in_played_slot` |
| 53 | `inventory__site_section_chain__avails_category__unfilled_avails_in_played_slot` |
| 54 | `inventory__site_section_chain__avails_category__unconstrained_avails_in_played_slot` |
| 55 | `inventory__site_section_chain__avails_category__raw_total_avails_in_played_slot` |
| 56 | `inventory__site_section_chain__avails_category__market_avails_in_played_slot` |
| 57 | `inventory__site_section_chain__avails_category__ssp_avails_in_played_slot` |
| 58 | `inventory__site_section_chain__avails_category__total_avails` |
| 59 | `inventory__site_section_chain__avails_category__total_unfilled_avails` |
| 60 | `inventory__site_section_chain__avails_category__opportunity` |
| 61 | `inventory__site_section_chain__avails_category__total_avails_in_played_slot` |
| 62 | `inventory__site_section_chain__avails_category__total_unfilled_avails_in_played_slot` |
| 63 | `inventory__site_section_chain__avails_category__opportunity_in_played_slot` |
| 64 | `inventory__site_section_chain__avails_category__raw_opportunity_in_played_slot` |
| 65 | `inventory__site_section_chain__avails_category__slot_opp_avails_in_played_slot` |
| 66 | `inventory__site_section_chain__avails_category__remaining_avails` |
| 67 | `inventory__site_section_chain__avails_category__vod_programmer_total_avails` |
| 68 | `inventory__site_section_chain__avails_category__distinct_inventory_avails` |
| 69 | `inventory__site_section_chain__avails_category__inventory_avails` |
| 70 | `inventory__site_section_chain__avails_category__raw_inventory_distinct_avails_in_played_slot` |
| 71 | `inventory__site_section_chain__outbound_rules` |
| 72 | `inventory__site_section_chain__outbound_rules__rule_id` |
| 73 | `inventory__site_section_chain__outbound_rules__total_opp` |
| 74 | `inventory__site_section_chain__outbound_rules__win_opp` |
| 75 | `inventory__site_section_chain__eligible_outbound_orders` |
| 76 | `inventory__site_section_chain__eligible_outbound_orders__down_network_id` |
| 77 | `inventory__site_section_chain__eligible_outbound_orders__order_id` |
| 78 | `inventory__site_section_chain__eligible_outbound_orders__order_type` |
| 79 | `inventory__site_section_chain__eligible_outbound_orders__exchange_order_id` |
| 80 | `inventory__site_section_chain__eligible_outbound_orders__listing_id` |
| 81 | `inventory__site_section_chain__eligible_outbound_orders__matched_inventory_package_ids` |
| 82 | `inventory__site_section_chain__eligible_outbound_orders__bit_flags` |
| 83 | `inventory__site_section_chain__eligible_outbound_orders__order_transaction_type` |
| 84 | `inventory__site_section_chain__eligible_outbound_orders__order_priority` |
| 85 | `inventory__site_section_chain__eligible_outbound_orders__sales_channel` |
| 86 | `inventory__site_section_chain__eligible_outbound_orders__avails_category` |
| 87 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__avails` |
| 88 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__unfilled_avails` |
| 89 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__unconstrained_avails` |
| 90 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__market_avails` |
| 91 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__ssp_avails` |
| 92 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__avails_in_played_slot` |
| 93 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__unfilled_avails_in_played_slot` |
| 94 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__unconstrained_avails_in_played_slot` |
| 95 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__raw_total_avails_in_played_slot` |
| 96 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__market_avails_in_played_slot` |
| 97 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__ssp_avails_in_played_slot` |
| 98 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__total_avails` |
| 99 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__total_unfilled_avails` |
| 100 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__opportunity` |
| 101 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__total_avails_in_played_slot` |
| 102 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__total_unfilled_avails_in_played_slot` |
| 103 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__opportunity_in_played_slot` |
| 104 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__raw_opportunity_in_played_slot` |
| 105 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__slot_opp_avails_in_played_slot` |
| 106 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__remaining_avails` |
| 107 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__vod_programmer_total_avails` |
| 108 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__distinct_inventory_avails` |
| 109 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__inventory_avails` |
| 110 | `inventory__site_section_chain__eligible_outbound_orders__avails_category__raw_inventory_distinct_avails_in_played_slot` |
| 111 | `inventory__site_section_chain__eligible_outbound_orders__count_true_avails_as_booked` |
| 112 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status` |
| 113 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__available_duration` |
| 114 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__filled_ad_num` |
| 115 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__filled_duration` |
| 116 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__unified_unfilled_opp` |
| 117 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__default_unfilled_opp` |
| 118 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__initial_filled_ad_num` |
| 119 | `inventory__site_section_chain__eligible_outbound_orders__ad_filling_status__initial_filled_duration` |
| 120 | `inventory__site_section_chain__outbound_exchange_listings` |
| 121 | `inventory__site_section_chain__outbound_exchange_listings__listing_ids` |
| 122 | `inventory__site_section_chain__outbound_exchange_listings__avails_metrics` |
| 123 | `inventory__site_section_chain__outbound_exchange_listings__avails_metrics__default_duration` |
| 124 | `inventory__site_section_chain__outbound_exchange_listings__avails_metrics__opportunity` |
| 125 | `inventory__site_section_chain__outbound_exchange_listings__avails_metrics__avails` |
| 126 | `inventory__site_section_chain__outbound_exchange_listings__avails_metrics__unfilled_avails` |
| 127 | `inventory__site_section_chain__non_tracked_audience_item_ids` |
| 128 | `inventory__site_section_chain__marketplace_audience_extension_deal_ids` |
| 129 | `inventory__site_section_chain__network_is_ad_owner` |
| 130 | `inventory__site_section_chain__network_is_ad_unit_owner` |
| 131 | `inventory__site_section_chain__network_is_extra_item_owner` |
| 132 | `inventory__site_section_chain__network_is_vod_programmer` |
| 133 | `inventory__site_section_chain__count_imp_as_booked` |
| 134 | `inventory__site_section_chain__deal_awareability` |
| 135 | `inventory__site_section_chain__demand_dim_awareability` |
| 136 | `inventory__site_section_chain__carriage_inventory_owner_id` |
| 137 | `inventory__site_section_chain__carriage_listing_split_unit_id` |
| 138 | `inventory__site_section_chain__eligible_carriage_listing_split_unit_ids` |
| 139 | `inventory__site_section_chain__ad_priority_bucket` |
| 140 | `inventory__site_section_chain__supply_source` |
| 141 | `inventory__site_section_chain__supply_source_type` |
| 142 | `inventory__site_section_chain__sales_channel` |
| 143 | `inventory__site_section_chain__programmatic_exchange_rate_to_usd` |
| 144 | `inventory__site_section_chain__programmatic_exchange_rate_to_eur` |
| 145 | `inventory__site_section_chain__bidder_seat_id` |
| 146 | `inventory__site_section_chain__global_currency_id` |
| 147 | `inventory__site_section_chain__floor_price` |
| 148 | `inventory__site_section_chain__ad_unit_default_duration` |
| 149 | `inventory__site_section_chain__ad_filling_status` |
| 150 | `inventory__site_section_chain__ad_filling_status__available_duration` |
| 151 | `inventory__site_section_chain__ad_filling_status__filled_ad_num` |
| 152 | `inventory__site_section_chain__ad_filling_status__filled_duration` |
| 153 | `inventory__site_section_chain__ad_filling_status__unified_unfilled_opp` |
| 154 | `inventory__site_section_chain__ad_filling_status__default_unfilled_opp` |
| 155 | `inventory__site_section_chain__ad_filling_status__initial_filled_ad_num` |
| 156 | `inventory__site_section_chain__ad_filling_status__initial_filled_duration` |
| 157 | `inventory__site_section_chain__priority_tier` |
| 158 | `inventory__site_section_chain__priority_value` |
| 159 | `inventory__site_section_chain__priority_type` |
| 160 | `inventory__site_section_chain__supply_acquisition_cost` |
| 161 | `inventory__site_section_chain__supply_distribution_cost` |
| 162 | `inventory__site_section_chain__internal_deal_ids` |
| 163 | `inventory__site_section_chain__inbound_order_ids` |
| 164 | `inventory__site_section_chain__inbound_listing_ids` |
| 165 | `inventory__site_section_chain__buyer_ids` |
| 166 | `inventory__site_section_chain__internal_seat_ids` |
| 167 | `inventory__site_section_chain__outbound_order_ids` |
| 168 | `inventory__site_section_chain__outbound_exchange_order_ids` |
| 169 | `inventory__site_section_chain__matched_yield_optimization_ids` |
| 170 | `inventory__site_section_chain__selected_yield_optimization_ids` |
| 171 | `inventory__site_section_chain__selected_yield_optimization_info_ids` |
| 172 | `inventory__site_section_chain__matched_inventory_package_ids` |
| 173 | `inventory__site_section_chain__matched_audience_item_ids` |
| 174 | `inventory__site_section_chain__matched_key_value_ids` |
| 175 | `inventory__site_section_chain__matched_daypart` |
| 176 | `inventory__site_section_chain__network_selection_info` |
| 177 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics` |
| 178 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics` |
| 179 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__input_ad_number` |
| 180 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__output_ad_number` |
| 181 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__data_privacy` |
| 182 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__restriction` |
| 183 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__unmapped` |
| 184 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__undefined` |
| 185 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics` |
| 186 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__input_ad_number` |
| 187 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__output_ad_number` |
| 188 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_ad_domain` |
| 189 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_slot_assigned_through_mrm_rule` |
| 190 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__frequency_cap` |
| 191 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__cpx_check_failed` |
| 192 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_schedule` |
| 193 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__rbp_check_failed` |
| 194 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot` |
| 195 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__sponsorship_check_failed` |
| 196 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__exclusivity_check_failed` |
| 197 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_user_experience` |
| 198 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_no_external_rule` |
| 199 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_resellable` |
| 200 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_promo_only` |
| 201 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_compatible` |
| 202 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_budget` |
| 203 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_yield_optimization` |
| 204 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__unmapped` |
| 205 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__undefined` |
| 206 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__ad_truncation` |
| 207 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics` |
| 208 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__input_ad_number` |
| 209 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__output_ad_number` |
| 210 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__frequency_cap` |
| 211 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot` |
| 212 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__compliance_check_failed` |
| 213 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative` |
| 214 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_suitable_rule_path` |
| 215 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__profile_check_failed` |
| 216 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__floor_price_not_met` |
| 217 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__restriction` |
| 218 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__exclusivity` |
| 219 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__pg_deal_bid_throttling` |
| 220 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__auction_max_ad_duration` |
| 221 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__reseller_restriction` |
| 222 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__market_ad_not_approved` |
| 223 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__listing_creative_duration_check_failed` |
| 224 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_ad_asset_store_availability` |
| 225 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_bitrate_check_failed` |
| 226 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_creative_targeting_check_failed` |
| 227 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_date_range_check_failed` |
| 228 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_max_ad_duration_check_failed` |
| 229 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_compatible_dimension_check_failed` |
| 230 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inventory_source_restriction` |
| 231 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_not_compatible` |
| 232 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_excluded_by_sponsor` |
| 233 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__met_yield_optimization` |
| 234 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__mpe_listing_restriction` |
| 235 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__unmapped` |
| 236 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__undefined` |
| 237 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inbound_order_competition_failure` |
| 238 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__competition_failure_in_pick_many` |
| 239 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics` |
| 240 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__input_ad_number` |
| 241 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_ad_number` |
| 242 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_num_ads` |
| 243 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_duration` |
| 244 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__time_based_freq_cap` |
| 245 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__no_creative` |
| 246 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__companion_check_failed` |
| 247 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__pod_position_targeting_check_failed` |
| 248 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_exclusivity_check_failed` |
| 249 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_sponsorship_check_failed` |
| 250 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_filled_by_multi_ad` |
| 251 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_fallback_ad_number` |
| 252 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_not_found` |
| 253 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__do_not_repeat` |
| 254 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__unmapped` |
| 255 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__undefined` |
| 256 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__network_id` |
| 257 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__demand_type` |
| 258 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__order_id` |
| 259 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__listing_ids` |
| 260 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics` |
| 261 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__phase` |
| 262 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__name` |
| 263 | `inventory__site_section_chain__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__value` |
| 264 | `inventory__site_section_chain__inventory_distribution_contexts` |
| 265 | `inventory__site_section_chain__inventory_distribution_contexts__carriage_inventory_owner_id` |
| 266 | `inventory__site_section_chain__inventory_distribution_contexts__carriage_listing_split_unit_id` |
| 267 | `inventory__site_section_chain__mapped_asset_ids` |
| 268 | `inventory__site_section_chain__mapped_site_section_ids` |
| 269 | `inventory__site_section_chain__selected_yo_volume_cap_ids` |
| 270 | `inventory__site_section_chain__selected_yo_distribution_id` |
| 271 | `inventory__site_section_chain__selected_yo_distribution_nip_id` |
| 272 | `inventory__site_section_chain__selected_yo_inventory_prioritization_id` |
| 273 | `inventory__site_section_chain__selected_yo_inventory_prioritization_nip_id` |
| 274 | `inventory__site_section_chain__selected_yo_margin_id` |
| 275 | `inventory__site_section_chain__audience_segment_max_cpm` |
| 276 | `inventory__site_section_chain__audience_partner_segment_infos` |
| 277 | `inventory__site_section_chain__audience_partner_segment_infos__audience_partner_id` |
| 278 | `inventory__site_section_chain__audience_partner_segment_infos__max_cpm` |
| 279 | `inventory__site_section_chain__audience_partner_segment_infos__matched_segments` |
| 280 | `inventory__site_section_chain__audience_partner_segment_infos__matched_segments__id` |
| 281 | `inventory__site_section_chain__audience_partner_segment_infos__matched_segments__cpm` |
| 282 | `inventory__site_section_chain__audience_partner_segment_infos__matched_segments__flags` |
| 283 | `inventory__site_section_chain__geo_visibility` |
| 284 | `inventory__site_section_chain__geo_visibility__targetable` |
| 285 | `inventory__site_section_chain__geo_visibility__report_aggregate` |
| 286 | `inventory__site_section_chain__geo_visibility__report_event` |

Checking network\_id 516429 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514075812\_749451&externalid=20260514\_075814\_00107\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514075812_749451&externalid=20260514_075814_00107_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514075818\_168959&externalid=20260514\_075856\_00109\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514075818_168959&externalid=20260514_075856_00109_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 129
  Columns B: 129

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (129 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__site_section_chain__asset_group_id                2 row(s)
    inventory__site_section_chain__break_id                      2 row(s)
    inventory__site_section_chain__opportunity_id                2 row(s)
    inventory__site_section_chain__scenario_id                   2 row(s)
    inventory__site_section_chain__portfolio_ids                 2 row(s)
    inventory__site_section_chain__custom_platform_ids           2 row(s)
    inventory__site_section_chain__region_ids                    2 row(s)
    inventory__site_section_chain__network_execution_ctx_flags   2 row(s)
    inventory__site_section_chain__geo_country_visibility        2 row(s)
    inventory__site_section_chain__geo_country_visibility__targetable 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility  2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_brand_visibility     2 row(s)
    inventory__site_section_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_genre_visibility     2 row(s)
    inventory__site_section_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_rating_visibility     2 row(s)
    inventory__site_section_chain__content_rating_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_form_visibility       2 row(s)
    inventory__site_section_chain__content_form_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_language_visibility  2 row(s)
    inventory__site_section_chain__standard_language_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_channel_visibility   2 row(s)
    inventory__site_section_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__site_section_chain                                2 row(s)

  Detailed diffs:

  [row=2]
    inventory__site_section_chain:
      old.csv: '[{"network_id":516429,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":516429,"distributor_network_id":516429,"asset_id":413467098,"site_section_id":19715213,"series_id":1134473675,"site_id":1212768,"asset_group_ids":[1134439078,1539297779],"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"airing_channel_id":-1,"airing_id":-1,"postal_code_package_id":[8885,9385,11421,11423,11612,11636,11859,12059,12511],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46],"tracked_audience_item_ids":[1311495,1311496,1311497,1406353,1407149,1407151,1407154,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407163,1407164,1407166,1407167,1407168,1407169,1407172,1407173,1407215,1407901,1407906,1407911,1407934,1407935,1408295,1408296,1408297,1408370,1416220,1421323,1421373,1479033,1479034,1479035,1479037,1479038],"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[210565,279585,364094]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_ids":[1134439078,1539297779],"asset_id":413467098,"bit_flags":0,"content_owner_network_id":516429,"context_id":72057594451395034,"distributor_network_id":516429,"entity_source":"inventory","inventory_package_ids":[210565,279585,364094],"network_execution_ctx_index":0,"network_id":516429,"postal_code_package_id":[8885,9385,11421,11423,11612,11636,11859,12059,12511],"role":"CRO","series_id":1134473675,"site_id":1212768,"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"site_section_id":19715213,"tracked_audience_item_ids":[1311495,1311496,1311497,1406353,1407149,1407151,1407154,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407163,1407164,1407166,1407167,1407168,1407169,1407172,1407173,1407215,1407901,1407906,1407911,1407934,1407935,1408295,1408296,1408297,1408370,1416220,1421323,1421373,1479033,1479034,1479035,1479037,1479038],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46]}]'

  [row=3]
    inventory__site_section_chain:
      old.csv: '[{"network_id":516429,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":516429,"distributor_network_id":516429,"asset_id":418691252,"site_section_id":19715213,"series_id":1162706512,"site_id":1212768,"asset_group_ids":[1547016268],"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"airing_channel_id":-1,"airing_id":-1,"postal_code_package_id":[11612,11635,11860,12058,12510],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46],"tracked_audience_item_ids":[1406353,1407012,1407147,1407149,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407164,1407169,1407174,1407207,1407208,1407210,1407211,1407212,1407213,1407214,1407215,1407216,1407217,1407904,1407910,1407911,1407913,1407934,1407936,1408293,1408298,1408301,1408303,1408304,1408313,1408364,1408365,1408367,1408370,1408371,1408440,1408442,1408443,1408516,1416220,1428419,1479033,1479034,1479035,1479037,1479038,1479039],"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0,"inventory_package_ids":[226273,279585]}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_ids":[1547016268],"asset_id":418691252,"bit_flags":0,"content_owner_network_id":516429,"context_id":72057594456619188,"distributor_network_id":516429,"entity_source":"inventory","inventory_package_ids":[226273,279585],"network_execution_ctx_index":0,"network_id":516429,"postal_code_package_id":[11612,11635,11860,12058,12510],"role":"CRO","series_id":1162706512,"site_id":1212768,"site_section_group_ids":[783600,783643,783644,1212783,1212784,1212797,1212819,1212820,1212821,1212835,1262402],"site_section_id":19715213,"tracked_audience_item_ids":[1406353,1407012,1407147,1407149,1407155,1407157,1407158,1407159,1407160,1407161,1407162,1407164,1407169,1407174,1407207,1407208,1407210,1407211,1407212,1407213,1407214,1407215,1407216,1407217,1407904,1407910,1407911,1407913,1407934,1407936,1408293,1408298,1408301,1408303,1408304,1408313,1408364,1408365,1408367,1408370,1408371,1408440,1408442,1408443,1408516,1416220,1428419,1479033,1479034,1479035,1479037,1479038,1479039],"visible_concrete_event_id":[32,35,36,37,38,39,40,41,42,43,44,45,46]}]'

========================================================================
  END OF REPORT
========================================================================
```


Summary:

1. Expected difference on the **inventory\_\_site\_section\_chain\_chain **columns ordering. 
2. Schema difference 

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |

---

Checking network\_id 538917 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514080854\_533467&externalid=20260514\_080856\_00111\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514080854_533467&externalid=20260514_080856_00111_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514080854\_533467&externalid=20260514\_080856\_00111\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514080854_533467&externalid=20260514_080856_00111_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 129
  Columns B: 129

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (129 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__site_section_chain__asset_group_id                2 row(s)
    inventory__site_section_chain__break_id                      2 row(s)
    inventory__site_section_chain__opportunity_id                2 row(s)
    inventory__site_section_chain__scenario_id                   2 row(s)
    inventory__site_section_chain__portfolio_ids                 2 row(s)
    inventory__site_section_chain__custom_platform_ids           2 row(s)
    inventory__site_section_chain__region_ids                    2 row(s)
    inventory__site_section_chain__network_execution_ctx_flags   2 row(s)
    inventory__site_section_chain__inventory_package_ids         2 row(s)
    inventory__site_section_chain__geo_country_visibility        2 row(s)
    inventory__site_section_chain__geo_country_visibility__targetable 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility  2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_brand_visibility     2 row(s)
    inventory__site_section_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_genre_visibility     2 row(s)
    inventory__site_section_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_rating_visibility     2 row(s)
    inventory__site_section_chain__content_rating_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_form_visibility       2 row(s)
    inventory__site_section_chain__content_form_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_language_visibility  2 row(s)
    inventory__site_section_chain__standard_language_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_channel_visibility   2 row(s)
    inventory__site_section_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__site_section_chain                                2 row(s)

  Detailed diffs:

  [row=2]
    inventory__site_section_chain:
      old.csv: '[{"network_id":538917,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":538917,"distributor_network_id":538917,"asset_id":449733918,"site_section_id":24253642,"site_id":1274911,"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_id":449733918,"bit_flags":0,"content_owner_network_id":538917,"context_id":72057594487661854,"distributor_network_id":538917,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":538917,"role":"CRO","site_id":1274911,"site_section_id":24253642}]'

  [row=3]
    inventory__site_section_chain:
      old.csv: '[{"network_id":538917,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":538917,"distributor_network_id":538917,"asset_id":449733918,"site_section_id":24253642,"site_id":1274911,"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_id":449733918,"bit_flags":0,"content_owner_network_id":538917,"context_id":72057594487661854,"distributor_network_id":538917,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":538917,"role":"CRO","site_id":1274911,"site_section_id":24253642}]'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

1. Expected difference on the **inventory\_\_site\_section\_chain **columns ordering. 
2. Schema difference → **Marked it as known difference as per discussion with Karan and Wang Yu **

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |


---

Checking network\_id 112214 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514082425\_285282&externalid=20260514\_082427\_00114\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514082425_285282&externalid=20260514_082427_00114_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514082419\_177439&externalid=20260514\_082457\_00115\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514082419_177439&externalid=20260514_082457_00115_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 129
  Columns B: 129

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (129 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    inventory__site_section_chain__break_id                      2 row(s)
    inventory__site_section_chain__opportunity_id                2 row(s)
    inventory__site_section_chain__scenario_id                   2 row(s)
    inventory__site_section_chain__portfolio_ids                 2 row(s)
    inventory__site_section_chain__custom_platform_ids           2 row(s)
    inventory__site_section_chain__region_ids                    2 row(s)
    inventory__site_section_chain__network_execution_ctx_flags   2 row(s)
    inventory__site_section_chain__inventory_package_ids         2 row(s)
    inventory__site_section_chain__geo_country_visibility        2 row(s)
    inventory__site_section_chain__geo_country_visibility__targetable 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__geo_country_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility  2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_endpoint_owner_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_brand_visibility     2 row(s)
    inventory__site_section_chain__standard_brand_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_brand_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_genre_visibility     2 row(s)
    inventory__site_section_chain__standard_genre_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_genre_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_rating_visibility     2 row(s)
    inventory__site_section_chain__content_rating_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_rating_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_programmer_visibility__report_event 2 row(s)
    inventory__site_section_chain__content_form_visibility       2 row(s)
    inventory__site_section_chain__content_form_visibility__targetable 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__content_form_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_language_visibility  2 row(s)
    inventory__site_section_chain__standard_language_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_language_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_channel_visibility   2 row(s)
    inventory__site_section_chain__standard_channel_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_channel_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_daypart_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_series_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_subscription_model_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_credential_status_visibility__report_event 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__targetable 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_aggregate 2 row(s)
    inventory__site_section_chain__standard_content_territory_visibility__report_event 2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    inventory__site_section_chain                                2 row(s)
    inventory__site_section_chain__asset_group_id                2 row(s)

  Detailed diffs:

  [row=2]
    inventory__site_section_chain:
      old.csv: '[{"network_id":112214,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":112214,"distributor_network_id":112214,"asset_id":-1,"site_section_id":23756622,"site_id":1265952,"asset_group_id":540630,"asset_group_ids":[540630],"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_id":540630,"asset_group_ids":[540630],"asset_id":-1,"bit_flags":0,"content_owner_network_id":112214,"context_id":108086391057432534,"distributor_network_id":112214,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":112214,"role":"CRO","site_id":1265952,"site_section_id":23756622}]'
    inventory__site_section_chain__asset_group_id:
      old.csv: '[540630]'
      new.csv: '\\N'

  [row=3]
    inventory__site_section_chain:
      old.csv: '[{"network_id":112214,"role":"CRO","entity_source":"inventory","bit_flags":0,"content_owner_network_id":112214,"distributor_network_id":112214,"asset_id":-1,"site_section_id":23756622,"site_id":1265952,"asset_group_id":540630,"asset_group_ids":[540630],"airing_channel_id":-1,"airing_id":-1,"network_execution_ctx_index":0,"network_is_ad_owner":false,"network_is_extra_item_owner":false,"deal_awareability":false,"demand_dim_awareability":false,"supply_source":0,"sales_channel":0,"programmatic_exchange_rate_to_usd":0.0,"programmatic_exchange_rate_to_eur":0.0}]'
      new.csv: '[{"airing_channel_id":-1,"airing_id":-1,"asset_group_id":540630,"asset_group_ids":[540630],"asset_id":-1,"bit_flags":0,"content_owner_network_id":112214,"context_id":108086391057432534,"distributor_network_id":112214,"entity_source":"inventory","network_execution_ctx_index":0,"network_id":112214,"role":"CRO","site_id":1265952,"site_section_id":23756622}]'
    inventory__site_section_chain__asset_group_id:
      old.csv: '[540630]'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

#### Summary:

1. Expected difference on the **inventory\_\_asset\_chain **columns ordering. 
2. **inventory\_\_site\_section\_chain\_\_asset\_group\_id**is casted as NULL in view definition needs to be updated
3. Schema difference → **Marked it as known difference as per discussion with Karan and Wang Yu **

| Fields only in old | Fields only in new |
| --- | --- |
| `network_is_ad_owner` | `context_id` |
| `network_is_extra_item_owner` |  |
| `deal_awareability` |  |
| `demand_dim_awareability` |  |
| `supply_source` |  |
| `sales_channel` |  |
| `programmatic_exchange_rate_to_usd` |  |
| `programmatic_exchange_rate_to_eur` |  |

### Aggregated Columns (deep dive)

#### **inventory\_\_site\_section\_chain\_\_network\_id**

| **inventory\_\_site\_section\_chain\_\_network\_id** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| `[538917]` | `148802` | `148802` | 0 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513162348_036274&externalid=20260513_162351_00270_kaj4c) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&externalid=20260513_162413_00271_kaj4c) |
| `[516429]` | `34572` | `34572` | 0 |  |
| `[112214]` | `34213` | `34213` | 0 |  |


#### **inventory\_\_site\_section\_chain\_\_role**

| **inventory\_\_site\_section\_chain\_\_role** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| `[CRO]` | `427834` | `397553` | 30281 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515065941_868022&externalid=20260515_065943_00050_bkccs) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515065945_779856&externalid=20260515_070017_00051_bkccs) |
| `[CRO, C]` | `13` | `8` | 5 |  |

**Why? ^ Need to look into the above → **

 

Re-ran analysis using the same query as above.

| **inventory\_\_site\_section\_chain\_\_role** | **Old Count** | **New Count** | **Diff Count**(Old - New) | **LQS Links** |
| --- | --- | --- | --- | --- |
| `[CRO]` | `308494` | `308494` | 0 | [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520230016_409559&externalid=20260520_230023_00489_fk2ih) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520230011_637785&externalid=20260520_230058_00490_fk2ih) |
| `[CRO, C]` | `15` | `15` | 0 |  |

Assumption is data settling in old vs new models. Re-run analysis shows matching data.

### Inventory (execution\_networks)

### Columns Present in Hoover but not in Hoover++ view

##   
Columns NOT available in the ETL query (`etl.public_test1."request"`) but present in `mrm_log_flat.default.request`


execution\_networks\_\_flags  
execution\_networks\_\_reseller\_network\_id  
execution\_networks\_\_revenue  
execution\_networks\_\_content\_owner\_revenue  
execution\_networks\_\_distributor\_revenue  
execution\_networks\_\_reseller\_revenue  
execution\_networks\_\_bidding\_revenue  
execution\_networks\_\_bidding\_up\_revenue  
execution\_networks\_\_content\_owner\_bidding\_revenue  
execution\_networks\_\_content\_owner\_bidding\_modified\_revenue  
execution\_networks\_\_content\_owner\_bidding\_original\_revenue  
execution\_networks\_\_distributor\_bidding\_revenue  
execution\_networks\_\_reseller\_bidding\_revenue  
execution\_networks\_\_ssp\_clearing\_revenue  
execution\_networks\_\_margin  
execution\_networks\_\_competition\_resellers  
execution\_networks\_\_rule\_id  
execution\_networks\_\_rule\_ext\_id  
execution\_networks\_\_rule\_flags  
execution\_networks\_\_rule\_type\_priority  
execution\_networks\_\_unified\_rule\_priority  
execution\_networks\_\_unified\_rule\_priority\_\_priority\_tier  
execution\_networks\_\_unified\_rule\_priority\_\_sub\_priority\_value  
execution\_networks\_\_site\_group\_id  
execution\_networks\_\_airing\_channel\_group\_id  
execution\_networks\_\_edge\_postal\_code\_package\_ids  
execution\_networks\_\_inbound\_rule\_id  
execution\_networks\_\_listing\_id  
execution\_networks\_\_inbound\_order\_type  
execution\_networks\_\_inbound\_order\_auction\_type  
execution\_networks\_\_upstream\_inbound\_order\_id  
execution\_networks\_\_upstream\_global\_currency\_id  
execution\_networks\_\_upstream\_content\_owner\_revenue\_in\_up\_currency  
execution\_networks\_\_outbound\_order\_id  
execution\_networks\_\_outbound\_order\_type  
execution\_networks\_\_outbound\_exchange\_order\_id  
execution\_networks\_\_outbound\_listing\_id  
execution\_networks\_\_unified\_outbound\_order\_priority  
execution\_networks\_\_unified\_outbound\_order\_priority\_\_priority\_tier  
execution\_networks\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value  
execution\_networks\_\_outbound\_order\_transaction\_type  
execution\_networks\_\_outbound\_order\_priority\_type  
execution\_networks\_\_avails\_category  
execution\_networks\_\_avails\_category\_\_avails  
execution\_networks\_\_avails\_category\_\_unfilled\_avails  
execution\_networks\_\_avails\_category\_\_unconstrained\_avails  
execution\_networks\_\_avails\_category\_\_market\_avails  
execution\_networks\_\_avails\_category\_\_ssp\_avails  
execution\_networks\_\_avails\_category\_\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_market\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_total\_avails  
execution\_networks\_\_avails\_category\_\_total\_unfilled\_avails  
execution\_networks\_\_avails\_category\_\_opportunity  
execution\_networks\_\_avails\_category\_\_total\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_opportunity\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot  
execution\_networks\_\_avails\_category\_\_remaining\_avails  
execution\_networks\_\_avails\_category\_\_vod\_programmer\_total\_avails  
execution\_networks\_\_avails\_category\_\_distinct\_inventory\_avails  
execution\_networks\_\_avails\_category\_\_inventory\_avails  
execution\_networks\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot  
execution\_networks\_\_outbound\_rules  
execution\_networks\_\_outbound\_rules\_\_rule\_id  
execution\_networks\_\_outbound\_rules\_\_total\_opp  
execution\_networks\_\_outbound\_rules\_\_win\_opp  
execution\_networks\_\_eligible\_outbound\_orders  
execution\_networks\_\_eligible\_outbound\_orders\_\_down\_network\_id  
execution\_networks\_\_eligible\_outbound\_orders\_\_order\_id  
execution\_networks\_\_eligible\_outbound\_orders\_\_order\_type  
execution\_networks\_\_eligible\_outbound\_orders\_\_exchange\_order\_id  
execution\_networks\_\_eligible\_outbound\_orders\_\_listing\_id  
execution\_networks\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids  
execution\_networks\_\_eligible\_outbound\_orders\_\_bit\_flags  
execution\_networks\_\_eligible\_outbound\_orders\_\_order\_transaction\_type  
execution\_networks\_\_eligible\_outbound\_orders\_\_order\_priority  
execution\_networks\_\_eligible\_outbound\_orders\_\_sales\_channel  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails  
execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot  
execution\_networks\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num  
execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration  
execution\_networks\_\_outbound\_exchange\_listings  
execution\_networks\_\_outbound\_exchange\_listings\_\_listing\_ids  
execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics  
execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration  
execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity  
execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails  
execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails  
execution\_networks\_\_non\_tracked\_audience\_item\_ids  
execution\_networks\_\_marketplace\_audience\_extension\_deal\_ids  
execution\_networks\_\_network\_is\_ad\_owner  
execution\_networks\_\_network\_is\_ad\_unit\_owner  
execution\_networks\_\_network\_is\_extra\_item\_owner  
execution\_networks\_\_network\_is\_vod\_programmer  
execution\_networks\_\_count\_imp\_as\_booked  
execution\_networks\_\_deal\_awareability  
execution\_networks\_\_demand\_dim\_awareability  
execution\_networks\_\_carriage\_inventory\_owner\_id  
execution\_networks\_\_carriage\_listing\_split\_unit\_id  
execution\_networks\_\_eligible\_carriage\_listing\_split\_unit\_ids  
execution\_networks\_\_ad\_priority\_bucket  
execution\_networks\_\_supply\_source\_type  
execution\_networks\_\_sales\_channel  
execution\_networks\_\_programmatic\_exchange\_rate\_to\_usd  
execution\_networks\_\_programmatic\_exchange\_rate\_to\_eur  
execution\_networks\_\_bidder\_seat\_id  
execution\_networks\_\_global\_currency\_id  
execution\_networks\_\_floor\_price  
execution\_networks\_\_ad\_unit\_default\_duration  
execution\_networks\_\_ad\_filling\_status  
execution\_networks\_\_ad\_filling\_status\_\_available\_duration  
execution\_networks\_\_ad\_filling\_status\_\_filled\_ad\_num  
execution\_networks\_\_ad\_filling\_status\_\_filled\_duration  
execution\_networks\_\_ad\_filling\_status\_\_unified\_unfilled\_opp  
execution\_networks\_\_ad\_filling\_status\_\_default\_unfilled\_opp  
execution\_networks\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num  
execution\_networks\_\_ad\_filling\_status\_\_initial\_filled\_duration  
execution\_networks\_\_priority\_tier  
execution\_networks\_\_priority\_value  
execution\_networks\_\_priority\_type  
execution\_networks\_\_supply\_acquisition\_cost  
execution\_networks\_\_supply\_distribution\_cost  
execution\_networks\_\_internal\_deal\_ids  
execution\_networks\_\_inbound\_order\_ids  
execution\_networks\_\_inbound\_listing\_ids  
execution\_networks\_\_buyer\_ids  
execution\_networks\_\_internal\_seat\_ids  
execution\_networks\_\_outbound\_order\_ids  
execution\_networks\_\_outbound\_exchange\_order\_ids  
execution\_networks\_\_matched\_yield\_optimization\_ids  
execution\_networks\_\_selected\_yield\_optimization\_ids  
execution\_networks\_\_selected\_yield\_optimization\_info\_ids  
execution\_networks\_\_matched\_inventory\_package\_ids  
execution\_networks\_\_matched\_audience\_item\_ids  
execution\_networks\_\_matched\_key\_value\_ids  
execution\_networks\_\_matched\_daypart  
execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation  
execution\_networks\_\_inventory\_distribution\_contexts  
execution\_networks\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id  
execution\_networks\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id  
execution\_networks\_\_selected\_yo\_volume\_cap\_ids  
execution\_networks\_\_selected\_yo\_distribution\_id  
execution\_networks\_\_selected\_yo\_distribution\_nip\_id  
execution\_networks\_\_selected\_yo\_inventory\_prioritization\_id  
execution\_networks\_\_selected\_yo\_inventory\_prioritization\_nip\_id  
execution\_networks\_\_selected\_yo\_margin\_id  
execution\_networks\_\_audience\_segment\_max\_cpm  
execution\_networks\_\_audience\_partner\_segment\_infos  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_max\_cpm  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm  
execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_flags  
execution\_networks\_\_geo\_visibility  
execution\_networks\_\_geo\_visibility\_\_targetable  
execution\_networks\_\_geo\_visibility\_\_report\_aggregate  
execution\_networks\_\_geo\_visibility\_\_report\_event

Checking network\_id 516429 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514092811\_850972&externalid=20260514\_092813\_00142\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514092811_850972&externalid=20260514_092813_00142_kaj4c)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514093333\_336578&externalid=20260514\_093408\_00149\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514093333_336578&externalid=20260514_093408_00149_kaj4c)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 222
  Columns B: 222

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (222 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    execution_networks                                           2 row(s)
    execution_networks__bit_flags                                2 row(s)

  Detailed diffs:

  [row=2]
    execution_networks:
      old.csv: '[{"network_id":516429,"role":"CRO","bit_flags":0,"content_owner_network_id":516429,"asset_id":413467098,"site_section_id":19715213,"series_id":1134473675,"site_id":1212768,"network_execution_ctx_index":0,"supply_source":1,"inventory_package_ids":[210565,279585,364094],"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":516429,"demand_type":2}]}}, {"network_id":537323,"role":"R","bit_flags":0,"content_owner_network_id":516429,"inbound_listing_id":[334682],"inbound_order_id":318128,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":1,"supply_source":5,"inventory_package_ids":[336488,368102],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":523319,"role":"R","bit_flags":33554432,"content_owner_network_id":516429,"inbound_listing_id":[210223],"inbound_order_id":4211,"inbound_order_type":"EXCHANGE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":2,"network_execution_ctx_flags":16777217,"supply_source":6,"inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,158660,201739,205333,210772,210775,210777,227940,258379,288913,330797,670073,672262,672263],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":523319,"role":"R","bit_flags":33554432,"content_owner_network_id":516429,"inbound_listing_id":[336963],"inbound_order_id":4211,"inbound_order_type":"EXCHANGE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":3,"network_execution_ctx_flags":16777217,"supply_source":6,"inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,158660,201739,205333,210772,210775,210777,227940,258379,288913,330797,670073,672262,672263],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}]'
      new.csv: '[{"asset_id":413467098,"content_owner_network_id":516429,"inventory_package_ids":[210565,279585,364094],"network_execution_ctx_index":0,"network_id":516429,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":2,"network_id":516429}]},"role":"CRO","series_id":1134473675,"site_id":1212768,"site_section_id":19715213,"supply_source":1}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[334682],"inbound_order_id":318128,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[336488,368102],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":1,"network_id":537323,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[210223],"inbound_order_id":4211,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,158660,201739,205333,210772,210775,210777,227940,258379,288913,330797,670073,672262,672263],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_flags":16777217,"network_execution_ctx_index":2,"network_id":523319,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":6,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[336963],"inbound_order_id":4211,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,158660,201739,205333,210772,210775,210777,227940,258379,288913,330797,670073,672262,672263],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_flags":16777217,"network_execution_ctx_index":3,"network_id":523319,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":6,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}]'
    execution_networks__bit_flags:
      old.csv: '[0, 0, 33554432, 33554432]'
      new.csv: '[null, null, null, null]'

  [row=3]
    execution_networks:
      old.csv: '[{"network_id":516429,"role":"CRO","bit_flags":0,"content_owner_network_id":516429,"asset_id":418691252,"site_section_id":19715213,"series_id":1162706512,"site_id":1212768,"network_execution_ctx_index":0,"supply_source":1,"inventory_package_ids":[226273,279585],"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":516429,"demand_type":2}]}}, {"network_id":376521,"role":"R","bit_flags":0,"content_owner_network_id":516429,"asset_id":-1,"site_section_id":24395702,"site_id":1227033,"inbound_listing_id":[661292],"inbound_order_id":636326,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":1,"supply_source":5,"inventory_package_ids":[132480,199169,230193,230440,230450,456355,550671],"network_selection_info":{},"mapped_site_section_ids":[24395702,24395716],"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":537323,"role":"R","bit_flags":0,"content_owner_network_id":516429,"inbound_listing_id":[334682],"inbound_order_id":318128,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":2,"supply_source":5,"inventory_package_ids":[336488,368102],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":537323,"role":"R","bit_flags":0,"content_owner_network_id":516429,"inbound_listing_id":[334676],"inbound_order_id":318130,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":3,"supply_source":5,"inventory_package_ids":[336488,368102],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":523319,"role":"R","bit_flags":33554432,"content_owner_network_id":516429,"inbound_listing_id":[336963],"inbound_order_id":4211,"inbound_order_type":"EXCHANGE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":4,"network_execution_ctx_flags":16777217,"supply_source":6,"inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,152724,158660,205333,210772,210775,210777,227940,258379,288913,330797,562613,670073,672262,672263],"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}, {"network_id":538726,"role":"R","bit_flags":0,"content_owner_network_id":376521,"inbound_listing_id":[616832],"inbound_order_id":592733,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":5,"supply_source":5,"network_selection_info":{},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}]'
      new.csv: '[{"asset_id":418691252,"content_owner_network_id":516429,"inventory_package_ids":[226273,279585],"network_execution_ctx_index":0,"network_id":516429,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":2,"network_id":516429}]},"role":"CRO","series_id":1162706512,"site_id":1212768,"site_section_id":19715213,"supply_source":1}, {"asset_id":-1,"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[661292],"inbound_order_id":636326,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[132480,199169,230193,230440,230450,456355,550671],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"mapped_site_section_ids":[24395702,24395716],"network_execution_ctx_index":1,"network_id":376521,"network_selection_info":{},"role":"R","site_id":1227033,"site_section_id":24395702,"standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[334682],"inbound_order_id":318128,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[336488,368102],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":2,"network_id":537323,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[334676],"inbound_order_id":318130,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[336488,368102],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":3,"network_id":537323,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":516429,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[336963],"inbound_order_id":4211,"inbound_order_transaction_type":"NON_GUARANTEED","inventory_package_ids":[108244,108495,108502,108659,111702,112563,112576,112615,112616,112618,112662,112668,112674,113232,113237,113244,113246,113247,113248,113249,114324,115224,115225,115226,120538,120541,125008,125032,133700,139918,152724,158660,205333,210772,210775,210777,227940,258379,288913,330797,562613,670073,672262,672263],"ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_flags":16777217,"network_execution_ctx_index":4,"network_id":523319,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":6,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":376521,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[616832],"inbound_order_id":592733,"inbound_order_transaction_type":"NON_GUARANTEED","ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":5,"network_id":538726,"network_selection_info":{},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}]'
    execution_networks__bit_flags:
      old.csv: '[0, 0, 0, 0, 33554432, 0]'
      new.csv: '[null, null, null, null, null, null]'

========================================================================
  END OF REPORT
========================================================================
```


Summary:

1. **execution\_networks** column have below difference

| Object | network\_id | Difference | old | new |
| --- | --- | --- | --- | --- |
| 0 | 516429 | `bit_flags` | `0` | **missing** |
| 1 | 376521 | `bit_flags` | `0` | **missing** |
| 1 | 376521 | `inbound_order_type` | `"MARKETPLACE_ORDER"` | **missing** |
| 2 | 537323 | `bit_flags` | `0` | **missing** |
| 2 | 537323 | `inbound_order_type` | `"MARKETPLACE_ORDER"` | **missing** |
| 3 | 537323 | `bit_flags` | `0` | **missing** |
| 3 | 537323 | `inbound_order_type` | `"MARKETPLACE_ORDER"` | **missing** |
| 4 | 523319 | `bit_flags` | `33554432` | **missing** |
| 4 | 523319 | `inbound_order_type` | `"EXCHANGE_ORDER"` | **missing** |
| 5 | 538726 | `bit_flags` | `0` | **missing** |
| 5 | 538726 | `inbound_order_type` | `"MARKETPLACE_ORDER"` | **missing** |

1. **execution\_networks\_\_bit\_flags** column has below difference  
      old: '\[0, 0, 0, 0, 33554432, 0\]'  
      new: '\[null, null, null, null, null, null\]'


---

Checking network\_id 538917 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260514155713\_986735&externalid=20260514\_155716\_00048\_w4kua](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260514155713_986735&externalid=20260514_155716_00048_w4kua)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515055415\_702492&externalid=20260515\_055448\_00026\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515055415_702492&externalid=20260515_055448_00026_bkccs)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 222
  Columns B: 222

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (222 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    execution_networks__bit_flags                                2 row(s)

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    execution_networks                                           2 row(s)

  Detailed diffs:

  [row=2]
    execution_networks:
      old.csv: '[{"network_id":538917,"role":"CRO","bit_flags":0,"content_owner_network_id":538917,"asset_id":449733918,"site_section_id":24253642,"site_id":1274911,"network_execution_ctx_index":0,"supply_source":1,"network_selection_info":{}}]'
      new.csv: '[{"asset_id":449733918,"content_owner_network_id":538917,"network_execution_ctx_index":0,"network_id":538917,"network_selection_info":{},"role":"CRO","site_id":1274911,"site_section_id":24253642,"supply_source":1}]'

  [row=3]
    execution_networks:
      old.csv: '[{"network_id":538917,"role":"CRO","bit_flags":0,"content_owner_network_id":538917,"asset_id":449733918,"site_section_id":24343800,"site_id":1274911,"network_execution_ctx_index":0,"supply_source":1,"network_selection_info":{}}]'
      new.csv: '[{"asset_id":449733918,"content_owner_network_id":538917,"network_execution_ctx_index":0,"network_id":538917,"network_selection_info":{},"role":"CRO","site_id":1274911,"site_section_id":24343800,"supply_source":1}]'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

1. **execution\_networks **column is missing “bit\_flags” element in new table but available in old


---

Checking network\_id 112214 with specific transaction ids: 

Old model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515063149\_695201&externalid=20260515\_063152\_00041\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515063149_695201&externalid=20260515_063152_00041_bkccs)

New model LQS → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260515063200\_472042&externalid=20260515\_063242\_00042\_bkccs](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515063200_472042&externalid=20260515_063242_00042_bkccs)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 222
  Columns B: 222

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (222 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):
    execution_networks                                           2 row(s)
    execution_networks__bit_flags                                2 row(s)

  Detailed diffs:

  [row=2]
    execution_networks:
      old.csv: '[{"network_id":112214,"role":"CRO","bit_flags":0,"content_owner_network_id":112214,"asset_id":-1,"site_section_id":23756622,"site_id":1265952,"network_execution_ctx_index":0,"supply_source":1,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":112214,"demand_type":2},{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filling_metrics":{"input_ad_number":1,"output_ad_number":1},"network_id":516374,"demand_type":4,"phase_metrics":[{"phase":8,"name":"INPUT_AD_NUMBER","value":1},{"phase":8,"name":"OUTPUT_AD_NUMBER","value":1},{"phase":9,"name":"INPUT_AD_NUMBER","value":1},{"phase":9,"name":"OUTPUT_AD_NUMBER","value":1}]},{"ad_targeting_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":525290,"demand_type":5,"order_id":183840,"phase_metrics":[{"phase":7,"name":"INPUT_AD_NUMBER","value":1},{"phase":7,"name":"OUTPUT_AD_NUMBER","value":1}]}]}}, {"network_id":525290,"role":"R","bit_flags":0,"content_owner_network_id":112214,"inbound_listing_id":[186711],"inbound_order_id":183840,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":1,"supply_source":5,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":525290,"demand_type":2,"phase_metrics":[{"phase":7,"name":"INPUT_AD_NUMBER","value":1},{"phase":7,"name":"OUTPUT_AD_NUMBER","value":1}]}]},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}]'
      new.csv: '[{"asset_id":-1,"content_owner_network_id":112214,"network_execution_ctx_index":0,"network_id":112214,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":2,"network_id":112214},{"ad_creative_checking_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filling_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":4,"network_id":516374,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":8,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":8,"value":1},{"name":"INPUT_AD_NUMBER","phase":9,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":9,"value":1}]},{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_targeting_metrics":{},"demand_type":5,"network_id":525290,"order_id":183840,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":7,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":7,"value":1}]}]},"role":"CRO","site_id":1265952,"site_section_id":23756622,"supply_source":1}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":112214,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[186711],"inbound_order_id":183840,"inbound_order_transaction_type":"NON_GUARANTEED","ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":1,"network_id":525290,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_targeting_metrics":{},"demand_type":2,"network_id":525290,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":7,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":7,"value":1}]}]},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}]'
    execution_networks__bit_flags:
      old.csv: '[0, 0]'
      new.csv: '[null, null]'

  [row=3]
    execution_networks:
      old.csv: '[{"network_id":112214,"role":"CRO","bit_flags":0,"content_owner_network_id":112214,"asset_id":-1,"site_section_id":23756622,"site_id":1265952,"network_execution_ctx_index":0,"supply_source":1,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":112214,"demand_type":2},{"ad_targeting_metrics":{},"ad_filtering_metrics":{},"ad_creative_checking_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filling_metrics":{"input_ad_number":1,"output_ad_number":1},"network_id":516374,"demand_type":4,"phase_metrics":[{"phase":8,"name":"INPUT_AD_NUMBER","value":1},{"phase":8,"name":"OUTPUT_AD_NUMBER","value":1},{"phase":9,"name":"INPUT_AD_NUMBER","value":1},{"phase":9,"name":"OUTPUT_AD_NUMBER","value":1}]},{"ad_targeting_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":525290,"demand_type":5,"order_id":183840,"phase_metrics":[{"phase":7,"name":"INPUT_AD_NUMBER","value":1},{"phase":7,"name":"OUTPUT_AD_NUMBER","value":1}]}]}}, {"network_id":525290,"role":"R","bit_flags":0,"content_owner_network_id":112214,"inbound_listing_id":[186711],"inbound_order_id":183840,"inbound_order_type":"MARKETPLACE_ORDER","inbound_order_transaction_type":"NON_GUARANTEED","network_execution_ctx_index":1,"supply_source":5,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_targeting_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"network_id":525290,"demand_type":2,"phase_metrics":[{"phase":7,"name":"INPUT_AD_NUMBER","value":1},{"phase":7,"name":"OUTPUT_AD_NUMBER","value":1}]}]},"geo_country_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_state_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_city_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"geo_dma_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"user_agent_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"device_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"ip_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"third_party_user_id_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"key_value_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_brand_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_genre_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_rating_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_programmer_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"content_form_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_language_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_channel_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_series_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"targetable":"FULL_VISIBILITY","report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY"}}]'
      new.csv: '[{"asset_id":-1,"content_owner_network_id":112214,"network_execution_ctx_index":0,"network_id":112214,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":2,"network_id":112214},{"ad_creative_checking_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filling_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_filtering_metrics":{},"ad_targeting_metrics":{},"demand_type":4,"network_id":516374,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":8,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":8,"value":1},{"name":"INPUT_AD_NUMBER","phase":9,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":9,"value":1}]},{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_targeting_metrics":{},"demand_type":5,"network_id":525290,"order_id":183840,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":7,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":7,"value":1}]}]},"role":"CRO","site_id":1265952,"site_section_id":23756622,"supply_source":1}, {"content_form_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"content_owner_network_id":112214,"content_rating_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"device_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_city_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_country_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_dma_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_state_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"geo_zip_code_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"inbound_listing_id":[186711],"inbound_order_id":183840,"inbound_order_transaction_type":"NON_GUARANTEED","ip_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"key_value_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"network_execution_ctx_index":1,"network_id":525290,"network_selection_info":{"candidate_ad_funnel_metrics":[{"ad_creative_checking_metrics":{},"ad_filling_metrics":{},"ad_filtering_metrics":{"input_ad_number":1,"output_ad_number":1},"ad_targeting_metrics":{},"demand_type":2,"network_id":525290,"phase_metrics":[{"name":"INPUT_AD_NUMBER","phase":7,"value":1},{"name":"OUTPUT_AD_NUMBER","phase":7,"value":1}]}]},"role":"R","standard_brand_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_channel_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_credential_status_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_daypart_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_series_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_subscription_model_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_content_territory_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_owner_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_endpoint_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_genre_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_language_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"standard_programmer_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"supply_source":5,"third_party_user_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"user_agent_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"},"visitor_custom_id_visibility":{"report_aggregate":"FULL_VISIBILITY","report_event":"FULL_VISIBILITY","targetable":"FULL_VISIBILITY"}}]'
    execution_networks__bit_flags:
      old.csv: '[0, 0]'
      new.csv: '[null, null]'

========================================================================
  END OF REPORT
========================================================================
```

Summary:

1. **execution\_networks** column is missing with elements (`bit_flags, inbound_order_type`) which is present in old but not in new


### Aggregated Columns (deep dive)

#### **execution\_networks\_\_role**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **execution\_networks\_\_role** | **old** | **new** | **diff\_count** | **LQS Links** |
| \[CRO\] | 215419 | 215976 | -557 |  [old](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515070944_889110&externalid=20260515_070946_00056_bkccs) vs [new](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260515070946_950287&externalid=20260515_071024_00057_bkccs) |
|   |  |  |  |  |
| \[CRO, R\] | 100849 | 101531 | -682 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R\] | 15182 | 15282 | -100 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R\] | 12515 | 12586 | -71 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R\] | 10398 | 10457 | -59 |   |
|   |  |  |  |  |
| \[\] | 9911 | 9992 | -81 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R\] | 5931 | 5978 | -47 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R\] | 5345 | 5386 | -41 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R\] | 3406 | 3421 | -15 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 2491 | 2515 | -24 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R\] | 2085 | 2100 | -15 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 2082 | 2096 | -14 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R\] | 1935 | 1946 | -11 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1696 | 1709 | -13 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R\] | 1687 | 1699 | -12 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1127 | 1133 | -6 |   |
|   |  |  |  |  |
| \[CRO, R, R, R\] | 1098 | 1101 | -3 |   |
|   |  |  |  |  |
| \[CRO, R, R\] | 745 | 748 | -3 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 519 | 522 | -3 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 338 | 339 | -1 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 247 | 250 | -3 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 185 | 188 | -3 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 144 | 146 | -2 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 130 | 130 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 98 | 98 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 76 | 76 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 56 | 56 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 25 | 25 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 16 | 16 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 13 | 13 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 12 | 12 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 6 | 6 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 6 | 6 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 6 | 6 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 6 | 6 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 3 | 3 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 3 | 3 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 2 | 2 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1 | 1 | 0 |   |
|   |  |  |  |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1 | 1 | 0 |   |
|   |  |  |  |  |

**Why? ^ Need to look into the above → **

 

Re-run analysis using same query as above.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Role** | **Old** | **New** | **Diff** | **Links** |
| \[CRO\] | 248783 | 248783 | 0 | Old → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260520232751\_225497&externalid=20260520\_232753\_00502\_fk2ih](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520232751_225497&externalid=20260520_232753_00502_fk2ih) |
| \[\] | 11091 | 11091 | 0 | New → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260520232758\_976403](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260520232758_976403) |
| \[CRO, R, R, R, R, R, R\] | 10372 | 10372 | 0 |  |
| \[CRO, R, R, R, R, R\] | 8794 | 8794 | 0 |  |
| \[CRO, R, R, R, R, R, R, R\] | 6322 | 6322 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R\] | 3422 | 3422 | 0 |  |
| \[CRO, R, R, R, R\] | 2892 | 2892 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 2694 | 2694 | 0 |  |
| \[CRO, R, R, R\] | 2283 | 2283 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R\] | 2207 | 2207 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1139 | 1139 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1026 | 1026 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R\] | 872 | 872 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R\] | 770 | 770 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 763 | 763 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 680 | 680 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 656 | 656 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 623 | 623 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R\] | 553 | 553 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 433 | 433 | 0 |  |
| \[CRO, R\] | 351 | 351 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 351 | 351 | 0 |  |
| \[CRO, R, R\] | 339 | 339 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 328 | 328 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 175 | 175 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 162 | 162 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 114 | 114 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 100 | 100 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 79 | 79 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 73 | 73 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 29 | 29 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 15 | 15 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 6 | 6 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 5 | 5 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 3 | 3 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 3 | 3 | 0 |  |
| \[CRO, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R, R\] | 1 | 1 | 0 |  |

Re-done analysis shows that the row counts match between old and new hoover++ models. Assumption, maybe data latency?  
  

## Aggregated Columns Summary:


| **Column\_name** | **Status** |
| --- | --- |
| request\_\_context\_\_rbp\_device\_type | Matching |
| request\_\_context\_\_rbp\_platform | Matching |
| inventory\_\_site\_section\_chain\_\_role | Matching |
| inventory\_\_site\_section\_chain\_\_network\_id | Matching |
| inventory\_\_asset\_chain\_\_role | Matching |
| inventory\_\_asset\_chain\_\_network\_id | Matching |
| visitor\_\_dma\_code\_id | Matching |
| visitor\_\_country | Matching |
| request\_info\_\_slot\_ad\_unit\_ids | Matching |
| execution\_networks\_\_role | Matching |

  
════════════════════════════════════════════════════════════  
  AGGREGATE COLUMN: request\_\_context\_\_rbp\_device\_type  
════════════════════════════════════════════════════════════  
  SQL USED FOR THIS AGG VALIDATION:  
  \[Hoover SQL\]  
  time=55.93s | rows=6  
  **SELECT request\_\_context\_\_rbp\_device\_type, COUNT(*****) AS cnt FROM mrm\_log\_flat.default.request WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_rbp\_device\_type ORDER BY cnt DESC***  
*  \[HooverPP SQL\]*  
*  time=53.32s | rows=6*  
*  **SELECT request\_\_context\_\_rbp\_device\_type, COUNT(*****) AS cnt FROM etl.public\_test1.request WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470) GROUP BY request\_\_context\_\_rbp\_device\_type ORDER BY cnt DESC**  
  Value                                          Hoover     HooverPP         Diff     Status

  MOB                                             41529        41529            0      MATCH  
  None                                               52           52            0      MATCH  
  OTT                                            447950       447950            0      MATCH  
  PC                                              10690        10690            0      MATCH  
  STB VOD                                            31           31            0      MATCH  
  UNDETERMINED                                    21951        21951            0      MATCH  
  ✅ PASS: counts match for all 6 value(s).  
  Match % (values): 6/6 (100.00%)  
  Match % (volume): 522,203/522,203 (100.00%)


════════════════════════════════════════════════════════════  
  AGGREGATE COLUMN: request\_\_context\_\_rbp\_platform  
════════════════════════════════════════════════════════════  
  SQL USED FOR THIS AGG VALIDATION:  
  \[Hoover SQL\]  
  time=46.89s | rows=7  
  **SELECT request\_\_context\_\_rbp\_platform, COUNT(*****) AS cnt FROM mrm\_log\_flat.default.request WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_rbp\_platform ORDER BY cnt DESC***  
*  \[HooverPP SQL\]*  
*  time=52.33s | rows=7*  
*  **SELECT request\_\_context\_\_rbp\_platform, COUNT(*****) AS cnt FROM etl.public\_test1.request WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470) GROUP BY request\_\_context\_\_rbp\_platform ORDER BY cnt DESC**  
  Value                                          Hoover     HooverPP         Diff     Status

  DESKTOP                                         10690        10690            0      MATCH  
  MOBILE\_APP                                       9094         9094            0      MATCH  
  MOBILE\_WEB                                      32435        32435            0      MATCH  
  None                                               52           52            0      MATCH  
  OTHER                                           21951        21951            0      MATCH  
  OTT                                            447950       447950            0      MATCH  
  VOD                                                31           31            0      MATCH  
  ✅ PASS: counts match for all 7 value(s).  
  Match % (values): 7/7 (100.00%)  
  Match % (volume): 522,203/522,203 (100.00%)  
  
════════════════════════════════════════════════════════════  
  AGGREGATE COLUMN: request\_info\_\_slot\_ad\_unit\_ids  
════════════════════════════════════════════════════════════  
  SQL USED FOR THIS AGG VALIDATION:  
  \[Hoover SQL\]  
  time=41.80s | rows=18  
  **SELECT request\_info\_\_slot\_ad\_unit\_ids, COUNT(*****) AS cnt FROM mrm\_log\_flat.default.request WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_info\_\_slot\_ad\_unit\_ids ORDER BY cnt DESC***  
*  \[HooverPP SQL\]*  
*  time=52.29s | rows=18*  
*  **SELECT request\_info\_\_slot\_ad\_unit\_ids, COUNT(*****) AS cnt FROM etl.public\_test1.request WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-06-03 18:00:00' as TIMESTAMP))) AND batch\_id IN ('20260603170000','20260603180000','20260603190000')   AND request\_\_context\_\_network\_id IN (538917, 545336, 112214, 512116, 534470) GROUP BY request\_info\_\_slot\_ad\_unit\_ids ORDER BY cnt DESC**  
  Value                                          Hoover     HooverPP         Diff     Status

  None                                             1533         1533            0      MATCH  
  \[1, 3, 47241, 66742, 66743, 66745\]               2099         2099            0      MATCH  
  \[1, 64505, 64507, 64508, 64509, 64649, 68265, 68266, 68267, 68268, 68269\]           43           43            0      MATCH  
  \[1\]                                             51483        51483            0      MATCH  
  \[22201\]                                            32           32            0      MATCH  
  \[22885\]                                           109          109            0      MATCH  
  \[2\]                                            255797       255797            0      MATCH  
  \[3\]                                               159          159            0      MATCH  
  \[4\]                                                77           77            0      MATCH  
  \[5, 63536, 63537, 63538, 63539, 63540\]              2            2            0      MATCH  
  \[5, 63541, 63542, 63543, 63544, 63547, 63548, 63549, 63551, 63553, 63556, 63557, 63558, 63559, 63560, 63561, 63562, 63563, 63589, 63620, 63844, 64254, 64331, 64332, 64333, 64334, 64335, 64608, 64768, 64769, 64770, 66376, 66377, 68357, 68420, 68823, 68824, 69416, 69455, 71021, 73359, 76308\]            7            7            0      MATCH  
  \[5, 63541, 63542, 63543, 63544, 63547, 63548, 63549, 63551, 63553, 63556, 63557, 63558, 63559, 63560, 63561, 63562, 63563, 63589, 63620, 63844, 64254, 64331, 64332, 64333, 64334, 64335, 64608, 64768, 64769, 64770, 66376, 66377, 68357, 68420, 68823, 68824, 69416, 69455, 71021, 73359\]           23           23            0      MATCH  
  \[5, 63570, 63571, 63572, 63573, 63574\]              4            4            0      MATCH  
  \[55803\]                                           781          781            0      MATCH  
  \[5\]                                               317          317            0      MATCH  
  \[67525\]                                             4            4            0      MATCH  
  \[74128\]                                             3            3            0      MATCH  
  \[74129\]                                        209730       209730            0      MATCH  
  ✅ PASS: counts match for all 18 value(s).  
  Match % (values): 18/18 (100.00%)  
  Match % (volume): 522,203/522,203 (100.00%)

## Questions?

@Bhargava, Karan

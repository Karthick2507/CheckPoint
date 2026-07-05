# mrm\_log\_flat\.default\."ad" vs etl\.public\_test1\."ad"

## Introduction:

Below is a list of all the `ad` level entities that were validated. Event level validations script (built from event\_validations.py) does this.

Top 5 networks (by record count for an hour) → **384777, 112214, 518308, 512166, 169843**

**Old model (mrm\_log\_flat)** → process\_batch\_id = '20250511180000'  
**New model (etl.public\_test1)** → event\_hour = '20250511180000'

**Filter: bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0**

**Matched by composite key: (request\_\_transaction\_id, advertisement\_\_ad\_id)**

## Entity

### Ad

| Entity | Columns |
| --- | --- |
| advertisement | advertisement\_\_ad\_id |
| advertisement | advertisement\_\_ad\_replica\_id |
| advertisement | advertisement\_\_rendition\_id |
| advertisement | advertisement\_\_creative\_id |
| advertisement | advertisement\_\_placement\_id |
| advertisement | advertisement\_\_campaign\_id |
| advertisement | advertisement\_\_io\_id |
| advertisement | advertisement\_\_insertion\_order\_id |
| advertisement | advertisement\_\_ad\_oo\_network\_id |
| advertisement | advertisement\_\_ad\_unit\_id |
| advertisement | advertisement\_\_advertiser\_id |
| advertisement | advertisement\_\_agency\_id |
| advertisement | advertisement\_\_global\_advertiser\_ids |
| advertisement | advertisement\_\_global\_brand\_ids |
| advertisement | advertisement\_\_global\_industry\_ids |
| advertisement | advertisement\_\_duration |
| advertisement | advertisement\_\_ad\_delivery\_method |
| advertisement | advertisement\_\_linear\_decision\_type |
| advertisement | advertisement\_\_placement\_type\_priority |
| advertisement | advertisement\_\_inventory\_protection\_flags |
| advertisement | advertisement\_\_unified\_priority |
| advertisement | advertisement\_\_effective\_unified\_priority |
| advertisement | advertisement\_\_unified\_yield |
| advertisement | advertisement\_\_is\_replacement |
| advertisement | advertisement\_\_replaced\_ad\_id |
| advertisement | advertisement\_\_replaced\_creative\_id |
| advertisement | advertisement\_\_replaced\_ad\_unit\_id |
| advertisement | advertisement\_\_replaced\_campaign\_id |
| advertisement | advertisement\_\_is\_uy\_replaced |
| advertisement | advertisement\_\_is\_ax |
| advertisement | advertisement\_\_replaced\_ad\_network\_id |
| advertisement | advertisement\_\_flags |
| advertisement | advertisement\_\_bit\_flags |
| advertisement | advertisement\_\_extra\_flags |
| advertisement | advertisement\_\_extra\_flags2 |
| advertisement | advertisement\_\_error |

---

**Network 384777**  
  
**Step 1 – Request\_\_transaction\_id and ad\_id for network 384777 at a given hour**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512034646\_999009&externalid=20260512\_034648\_00020\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512034646_999009&externalid=20260512_034648_00020_qk7z5)

**Step 2 – Old Hoover Ad query (mrm\_log\_flat) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512040333\_541810&externalid=20260512\_040335\_00025\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512040333_541810&externalid=20260512_040335_00025_qk7z5)

**Step 3 – Hoover++ Ad query (etl.public\_test1) for 384777:**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512040332\_845166&externalid=20260512\_040504\_00026\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512040332_845166&externalid=20260512_040504_00026_qk7z5)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_ad.csv
  Source B : new_ad.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'advertisement__ad_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- **Row counts match**: 5 = 5
- **Column headers identical**: 37 columns
- **No field-level differences found**
- **No known differences triggered**

Network 384777 ad-level validation: **all clear**, old Hoover and new Hoover++ produce identical ad entity data when matched by `(request__transaction_id, advertisement__ad_id)`.

---

**Network 112214**

**Step 1 – Request\_\_transaction\_id and ad\_id for network 112214 at a given hour**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512041830\_512788&externalid=20260512\_041832\_00028\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512041830_512788&externalid=20260512_041832_00028_qk7z5)

**Step 2 – Old Hoover Ad query (mrm\_log\_flat) for 112214**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512042303\_341011&externalid=20260512\_042305\_00030\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512042303_341011&externalid=20260512_042305_00030_qk7z5)

**Step 3 – Hoover++ Ad query (etl.public\_test1) for 112214:**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512042314\_851031&externalid=20260512\_042445\_00031\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512042314_851031&externalid=20260512_042445_00031_qk7z5)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_ad_112214.csv
  Source B : new_ad_112214.csv
  Rows  A  : 6
  Rows  B  : 6
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 6

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'advertisement__ad_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):
    advertisement__global_advertiser_ids                         6 row(s)
    advertisement__global_brand_ids                              6 row(s)
    advertisement__global_industry_ids                           6 row(s)

  Detailed diffs:

  [key=('1778524159953543809', '92979974')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

  [key=('1778524159953543809', '93532612')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

  [key=('1778524159953543809', '93801424')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

  [key=('1778524674723240435', '92979974')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

  [key=('1778524674723240435', '93532612')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

  [key=('1778524674723240435', '93801424')]
    advertisement__global_advertiser_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_brand_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'
    advertisement__global_industry_ids:
      old_ad_112214.csv: '[]'
      new_ad_112214.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

**Network 112214 results:**

- **Row counts match**: 6 = 6
- **6 rows have differences** across 3 columns presenting all the same pattern:
    - `advertisement__global_advertiser_ids`: `[]` in Hoover vs `\N` in Hoover++
    - `advertisement__global_brand_ids`: `[]` in Hoover vs `\N` in Hoover++
    - `advertisement__global_industry_ids`: `[]` in Hoover vs `\N` in Hoover++

This is the same type of semantic equivalence finding (`[]` vs `\N`). These are representational differences :empty list vs null, not real data differences. 

---

**Network 518308**

**Step 1 – Request\_\_transaction\_id and ad\_id for network 518308 at a given hour**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512145629\_989942&externalid=20260512\_145631\_00204\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512145629_989942&externalid=20260512_145631_00204_qk7z5)

**Step 2 – Old Hoover Ad query (mrm\_log\_flat) for 518308**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512151041\_160119&externalid=20260512\_151128\_00002\_psqrd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512151041_160119&externalid=20260512_151128_00002_psqrd)

**Step 3 – Hoover++ Ad query (etl.public\_test1) for 518308:**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512151049\_066708&externalid=20260512\_151241\_00214\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512151049_066708&externalid=20260512_151241_00214_qk7z5)  

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_ad_518308.csv
  Source B : new_ad_518308.csv
  Rows  A  : 10
  Rows  B  : 10
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 10

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'advertisement__ad_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):
    advertisement__inventory_protection_flags                    6 row(s)
    advertisement__replaced_ad_network_id                        6 row(s)

  Detailed diffs:

  [key=('1778523006465104765', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '88'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '531516'
      new_ad_518308.csv: '\\N'

  [key=('1778523146994271154', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '80'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '523319'
      new_ad_518308.csv: '\\N'

  [key=('1778523153036756417', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '80'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '523319'
      new_ad_518308.csv: '\\N'

  [key=('1778523549593175507', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '80'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '523319'
      new_ad_518308.csv: '\\N'

  [key=('1778523684902379854', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '88'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '531516'
      new_ad_518308.csv: '\\N'

  [key=('1778525933027140809', '53236803')]
    advertisement__inventory_protection_flags:
      old_ad_518308.csv: '88'
      new_ad_518308.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_518308.csv: '529349'
      new_ad_518308.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

**Network 518308 results:**

- **Row counts match**: 10 = 10
- **6 rows have differences** across 2 columns — all on the same ad\_id `53236803`:
    - `advertisement__inventory_protection_flags`: has values (`80` or `88`) in Hoover vs `\N` in Hoover++
    - `advertisement__replaced_ad_network_id`: has values (`531516`, `523319`, `529349`) in Hoover vs `\N` in Hoover++
    - Hoover has actual inventory protection flags and replaced network IDs that are null in Hoover++.

---

**Network 512166**

**Step 1 – Request\_\_transaction\_id and ad\_id for network 512166 at a given hour**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512152121\_990030&externalid=20260512\_152122\_00224\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512152121_990030&externalid=20260512_152122_00224_qk7z5)

**Step 2 – Old Hoover Ad query (mrm\_log\_flat) for 512166**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512152324\_716364&externalid=20260512\_152326\_00226\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512152324_716364&externalid=20260512_152326_00226_qk7z5)

**Step 3 – Hoover++ Ad query (etl.public\_test1) for 512166:**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512152334\_130165&externalid=20260512\_151241\_00214\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512152334_130165&externalid=20260512_151241_00214_qk7z5)  

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_ad_512166.csv
  Source B : new_ad_512166.csv
  Rows  A  : 9
  Rows  B  : 9
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 9

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'advertisement__ad_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):
    advertisement__inventory_protection_flags                    6 row(s)
    advertisement__replaced_ad_network_id                        6 row(s)

  Detailed diffs:

  [key=('1778522432589309610', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

  [key=('1778524084682469219', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

  [key=('1778524468130059068', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

  [key=('1778524522973867492', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

  [key=('1778525310506703338', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

  [key=('1778525338149837072', '53782914')]
    advertisement__inventory_protection_flags:
      old_ad_512166.csv: '88'
      new_ad_512166.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old_ad_512166.csv: '530362'
      new_ad_512166.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

**Network 512166 results:**

- **Row counts match**: 9 = 9
- **6 rows have differences** — same pattern as 518308:
    - `advertisement__inventory_protection_flags`: `88` in Hoover vs `\N` in Hoover++
    - `advertisement__replaced_ad_network_id`: `530362` in Hoover vs `\N` in Hoover++
    - All on the same ad\_id `53782914`

Hoover++ isn't populating inventory protection flags and replaced ad network ID. Consistent across network ids, 518308 and 512166.

---

**Network 169843**

**Step 1 – Request\_\_transaction\_id and ad\_id for network 169843 at a given hour**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512161523\_805995&externalid=20260512\_161525\_00279\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512161523_805995&externalid=20260512_161525_00279_qk7z5)

**Step 2 – Old Hoover Ad query (mrm\_log\_flat) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512161912\_338000&externalid=20260512\_161914\_00283\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512161912_338000&externalid=20260512_161914_00283_qk7z5)

**Step 3 – Hoover++ Ad query (etl.public\_test1) for 169843:**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512161924\_663754&externalid=20260512\_162106\_00284\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512161924_663754&externalid=20260512_162106_00284_qk7z5)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_ad_169843.csv
  Source B : new_ad_169843.csv
  Rows  A  : 11
  Rows  B  : 6
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=11  B=6  diff=5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'advertisement__ad_id']) ───────────────────────────

  ⚠️  5 key(s) only in old_ad_169843.csv:
    ('1778522389912074012', '68483172')
    ('1778522389912074012', '68483173')
    ('1778522389912074012', '92869858')
    ('1778522389912074012', '92869859')
    ('1778522389912074012', '93494903')
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  ✅ No known-difference columns triggered.

  ❌ 5 row(s) have differences:

  Column diff summary (sorted by frequency):
    advertisement__inventory_protection_flags                    5 row(s)
    advertisement__global_brand_ids                              2 row(s)

  Detailed diffs:

  [key=('1778525962899217119', '91419565')]
    advertisement__inventory_protection_flags:
      old_ad_169843.csv: '4'
      new_ad_169843.csv: '\\N'

  [key=('1778525962899217119', '92969015')]
    advertisement__global_brand_ids:
      old_ad_169843.csv: '[]'
      new_ad_169843.csv: '\\N'
    advertisement__inventory_protection_flags:
      old_ad_169843.csv: '10'
      new_ad_169843.csv: '\\N'

  [key=('1778525962899217119', '93004847')]
    advertisement__inventory_protection_flags:
      old_ad_169843.csv: '10'
      new_ad_169843.csv: '\\N'

  [key=('1778525962899217119', '93248446')]
    advertisement__inventory_protection_flags:
      old_ad_169843.csv: '10'
      new_ad_169843.csv: '\\N'

  [key=('1778525962899217119', '93584166')]
    advertisement__global_brand_ids:
      old_ad_169843.csv: '[]'
      new_ad_169843.csv: '\\N'
    advertisement__inventory_protection_flags:
      old_ad_169843.csv: '4'
      new_ad_169843.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```


**Network 169843 results:**

- **Row count mismatch**: old=11, new=6 (5 extra rows in old)
- **5 keys only in old** — transaction `1778522389912074012` has 5 ads not present in Hoover++
- **5 rows with field diffs**:
    - `advertisement__inventory_protection_flags`: populated (`4`, `10`) in Hoover vs `\N` in Hoover++ (5 rows)
    - `advertisement__global_brand_ids`: `[]` vs `\N` (2 rows, semantic equivalence)  

Summary of all 5 network ids above:

| Network | Rows | Result |
| --- | --- | --- |
| 384777 | 5/5 | No differences |
| 112214 | 6/6 | \[\] vs \\N on global\_advertiser\_ids, global\_brand\_ids, global\_industry\_ids (semantic) |
| 518308 | 10/10 | inventory\_protection\_flags + replaced\_ad\_network\_id populated in old, null in new |
| 512166 | 9/9 | Same as 518308 |
| 169843 | 11/6 | 5 missing rows in new + inventory\_protection\_flags null in new + global\_brand\_ids semantic diff |

### Request

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=6.30s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=4.20s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: request)
========================================================================
  Total columns  — Hoover  : 344
  Total columns  — HooverPP: 259
  Common columns           : 231
  Only in Hoover           : 113
  Only in HooverPP         : 28
  Data-type mismatches     : 1
  Match % (common columns) : 231/372 (62.10%)
  Match % (type on common) : 230/231 (99.57%)
  Match % (overall schema) : 230/372 (61.83%)

  Columns only in Hoover:
    request__bid_request__impression__currency  [array(varchar)]
    request__bid_request__impression__deal__auction_type  [array(array(varchar))]
    request__bid_request__impression__deal__currency  [array(array(varchar))]
    request__bid_request__impression__deal__floor  [array(array(real))]
    request__bid_request__site_domain  [varchar]
    request__bid_request__site_page_hash  [integer]
    request__cbp__network_id  [bigint]
    request__client_facing_reason_code  [array(varchar)]
    request__context__ab_test_item__is_effective  [array(boolean)]
    request__context__casu_id  [varchar]
    request__context__custom_distributor_category  [varchar]
    request__context__custom_distributor_id  [varchar]
    request__context__custom_distributor_signature  [varchar]
    request__context__distributor_video_asset_group_id  [bigint]
    request__context__extracted_key_value  [varchar]
    request__context__extracted_key_value___fw_dbp  [varchar]
    request__context__extracted_key_value___fw_lto  [varchar]
    request__context__headend_inserter_id  [varchar]
    request__context__mvpd  [varchar]
    request__context__p2_handler_source  [varchar]
    request__context__request_trace_id  [varchar]
    request__context__site_section_cro_asset_group_id  [bigint]
    request__context__site_section_cro_parsed_site_section_id  [bigint]
    request__context__ssto  [varchar]
    request__context__uri  [varchar]
    request__context__ux_conf_id  [bigint]
    request__context__ux_network_id  [bigint]
    request__context__ux_section_id  [bigint]
    request__context__video_cro_context_group_id  [bigint]
    request__context__video_cro_pre_targeting_yield_optimization_ids  [array(bigint)]
    request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_type  [array(varchar)]
    request__context__video_cro_selected_yield_optimization_infos__sub_yo_type  [array(varchar)]
    request__context__video_cro_yield_optimization_ids  [array(bigint)]
    request__context__website_root_id  [bigint]
    request__decision_info__decision_log  [varchar]
    request__decision_info__networks  [array(bigint)]
    request__decision_info__reject_ads  [array(varchar)]
    request__decision_info__reject_ads__ad_id  [array(bigint)]
    request__decision_info__reject_ads__ad_reason  [array(integer)]
    request__decision_info__reject_ads__slot_reason  [array(integer)]
    request__experiment_platform  [varchar]
    request__experiment_platform__experiment  [array(varchar)]
    request__experiment_platform__experiment__domain_id  [array(integer)]
    request__experiment_platform__experiment__experiment_id  [array(integer)]
    request__experiment_platform__experiment__flags  [array(bigint)]
    request__experiment_platform__experiment__index_id  [array(integer)]
    request__experiment_platform__experiment__layer_id  [array(integer)]
    request__experiment_platform__experiment__parameter  [array(array(varchar))]
    request__experiment_platform__experiment__parameter__id  [array(array(integer))]
    request__experiment_platform__experiment__parameter__value  [array(array(varchar))]
    request__experiment_platform__experiment__partition_index  [array(integer)]
    request__extra_geo_info  [varchar]
    request__extra_geo_info__descriptions  [array(varchar)]
    request__extra_geo_info__edge_networks  [array(bigint)]
    request__extra_geo_info__ids  [array(integer)]
    request__extra_geo_info__is_pulse  [boolean]
    request__gateway_ingested_supply_cost  [double]
    request__gateway_source_filepath  [varchar]
    request__identifier  [varchar]
    request__identifier__sequence  [bigint]
    request__identifier__source  [varchar]
    request__ifa_type  [varchar]
    request__is_all_data_visibility  [boolean]
    request__log_version  [varchar]
    request__log_version__build  [integer]
    request__log_version__major_release_version  [integer]
    request__log_version__major_version  [integer]
    request__log_version__minor_release_version  [integer]
    request__network_ctx  [array(varchar)]
    request__network_ctx__network_id  [array(bigint)]
    request__network_data_visibility_config  [array(varchar)]
    request__network_data_visibility_config__data_right  [array(array(varchar))]
    request__network_data_visibility_config__data_right__field  [array(array(varchar))]
    request__network_data_visibility_config__data_right__right  [array(array(integer))]
    request__network_data_visibility_config__device_id_visibility  [array(varchar)]
    request__network_data_visibility_config__geo_visibility  [array(varchar)]
    request__network_data_visibility_config__ip_visibility  [array(varchar)]
    request__network_data_visibility_config__key_value_visibility  [array(varchar)]
    request__network_data_visibility_config__network_id  [array(bigint)]
    request__network_data_visibility_config__user_agent_visibility  [array(varchar)]
    request__network_data_visibility_config__visible_data_fields_mask  [array(bigint)]
    request__network_data_visibility_config__visitor_custom_id_visibility  [array(varchar)]
    request__phantom_candidate  [array(varchar)]
    request__phantom_candidate__ad_id  [array(bigint)]
    request__phantom_candidate__creative_id  [array(bigint)]
    request__phantom_candidate__position_in_slot  [array(integer)]
    request__phantom_candidate__rendition_id  [array(bigint)]
    request__phantom_candidate__slot_custom_id  [array(varchar)]
    request__privacy_info__gdpr_cmp_id  [integer]
    request__private_data_accessible_networks  [array(bigint)]
    request__process_timestamp  [bigint]
    request__request_throttling_info__model_info  [array(varchar)]
    request__request_throttling_info__model_info__model_flags  [array(bigint)]
    request__request_throttling_info__model_info__model_id  [array(integer)]
    request__scores__ad_id  [array(bigint)]
    request__scte_message_id  [varchar]
    request__time_record__external_candidate  [integer]
    request__time_record__external_creative  [integer]
    request__time_record__external_playlist_notification  [integer]
    request__time_record__external_sds  [integer]
    request__traffic_compliance__endpoint_flag  [integer]
    request__userdb_audience_user_info__bg_query_key  [array(varchar)]
    request__userdb_audience_user_info__bg_query_key__key  [array(varchar)]
    request__userdb_audience_user_info__bg_query_key__set  [array(varchar)]
    request__userdb_audience_user_info__dx_alias_growth_ratio  [double]
    request__userdb_audience_user_info__dx_query_key  [array(varchar)]
    request__userdb_audience_user_info__dx_query_key__key  [array(varchar)]
    request__userdb_audience_user_info__dx_query_key__set  [array(varchar)]
    request__userdb_audience_user_info__num_dx_enriched_alias_ids  [integer]
    request__userdb_audience_user_info__num_dx_enriched_keys  [integer]
    request__userdb_audience_user_info__num_keys  [integer]
    request__vod_session_id  [varchar]
    request__xdevice_killed_placement  [array(bigint)]

  Columns only in HooverPP:
    request__audience_item  [array(varchar)]
    request__audience_item__audience_item_id  [array(bigint)]
    request__bid_request__site__domain  [varchar]
    request__bid_request__site__page_hash  [integer]
    request__context__key_value  [array(varchar)]
    request__context__key_value__key  [array(varchar)]
    request__context__key_value__value  [array(varchar)]
    request__errors  [array(varchar)]
    request__errors__ad_id  [array(bigint)]
    request__errors__code  [array(varchar)]
    request__errors__domain  [array(varchar)]
    request__errors__network_id  [array(bigint)]
    request__errors__partner  [array(varchar)]
    request__errors__type  [array(varchar)]
    request__external_bridge_records  [array(varchar)]
    request__external_bridge_records__duration  [array(integer)]
    request__external_bridge_records__error  [array(varchar)]
    request__external_bridge_records__flags  [array(integer)]
    request__external_bridge_records__http_status_code  [array(integer)]
    request__external_bridge_records__slot_index  [array(integer)]
    request__inventory_group  [array(varchar)]
    request__inventory_group__group_id  [array(array(bigint))]
    request__network_execution_ctx  [array(varchar)]
    request__network_execution_ctx__candidate_ad_num  [array(integer)]
    request__network_execution_ctx__network_id  [array(bigint)]
    request__network_execution_ctx__programmatic_cadidate_ad_num  [array(integer)]
    request__network_execution_ctx__supply_source_type  [array(varchar)]
    request__network_execution_ctx__upstream_network_id  [array(bigint)]

  Data-type mismatches:
    Column                                                       Hoover               HooverPP
    ------------------------------------------------------------------------------------------
    request__timestamp                                           timestamp(3)         bigint

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=26.49s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=328.40s | rows=2  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=75.71s | rows=2  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=request, network=169843)  
  Source B : HooverPP (entity=request, network=169843)  
  Rows  A  : 2  
  Rows  B  : 2  
  Columns A: 231  
  Columns B: 231

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 2

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (231 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/2 (0.00%)
  Column match %    : 223/231 (96.54%)
  Cell/value match %: 447/462 (96.75%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
request__client_facing_ivt_reason_flag                       2 row(s)
request__context__profile_concrete_event_id                  2 row(s)
request__context__standard_content_viewership_profile_ids    2 row(s)
request__context__standard_iab_category_ids                  2 row(s)
request__context__standard_sport_entity_ids                  2 row(s)
request__decision_info__external_bridge                      2 row(s)
request__decision_info__external_bridge__slot_index          2 row(s)
request__decision_info__external_bridge__status              2 row(s)
request__guaranteed_deal_avail                               2 row(s)
request__guaranteed_deal_avail__buyer_id                     2 row(s)
request__guaranteed_deal_avail__internal_deal_id             2 row(s)
request__linear_capnedit                                     2 row(s)
request__linear_capnedit__active_state                       2 row(s)
request__linear_capnedit__device_id                          2 row(s)
request__linear_capnedit__is_dvr                             2 row(s)
request__linear_capnedit__last_activity_time                 2 row(s)
request__linear_capnedit__mode                               2 row(s)
request__linear_capnedit__tune_time                          2 row(s)
request__mpe_matcher_filters                                 2 row(s)
request__mpe_matcher_filters__bucket_id                      2 row(s)
request__mpe_matcher_filters__id                             2 row(s)
request__mpe_matcher_filters__weight                         2 row(s)
request__mrc_compliance_label                                2 row(s)
request__soft_guaranteed_ad                                  2 row(s)
request__soft_guaranteed_ad__ad_id                           2 row(s)
request__soft_guaranteed_ad__entity_id                       2 row(s)
request__soft_guaranteed_ad__entity_type                     2 row(s)
request__soft_guaranteed_ad__network_id                      2 row(s)
request__soft_guaranteed_ad__num_competing_ads               2 row(s)
request__context__standard_genre_ids                         1 row(s)
request__yield_optimization_ids                              1 row(s)
request__yield_optimization_ids__demand_id                   1 row(s)
request__yield_optimization_ids__demand_type                 1 row(s)
request__yield_optimization_ids__optimization_ids            1 row(s)
```

  ❌ 2 row(s) have differences:

  Column diff summary (sorted by frequency):  
    request\_\_cbp                                                 2 row(s)  
    request\_\_context                                             2 row(s)  
    request\_\_scores                                              2 row(s)  
    request\_\_time\_record                                         2 row(s)  
    request\_\_timestamp                                           2 row(s)  
    request\_\_traffic\_compliance                                  2 row(s)  
    request\_\_userdb\_audience\_user\_info                           2 row(s)  
    request\_\_decision\_info                                       1 row(s)

  Detailed diffs:

  \[row=2\]  
    request\_\_cbp:  
      Hoover (entity=request, network=169843): '{"network\_id":169843,"slot\_template\_id":82531}'  
      HooverPP (entity=request, network=169843): '{"slot\_template\_id":82531}'  
    request\_\_context:  
      Hoover (entity=request, network=169843): '{"network\_id":169843,"asset\_id":462050467,"custom\_asset\_id":"169843/MDLVault\_EP019155650004","site\_section\_id":23620202,"page\_random":"1780171200254","video\_random":"1780171200254","asset\_duration":600.0,"request\_duration":60.0,"time\_position":0.0,"profile\_id":14603,"request\_format":1,"response\_format":13,"ab\_test\_item":\[{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":291},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":293},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":519},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2010,"bucket\_id":2018},{"collection\_id":2012,"bucket\_id":2021},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282738,"bucket\_id":3282953},{"collection\_id":3282738,"bucket\_id":3282961},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[29773.v.fwmrm.net](http://29773.v.fwmrm.net)","request\_trace\_id":"26f7d7b7c55c799e1fc22396cb4790e2","rbp\_platform":"OTT","stream\_mode\_id":1,"standard\_brand\_id":3030,"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":45,"standard\_endpoint\_id":99,"website\_root\_id":1217285,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4892,"standard\_content\_subscription\_model\_id":3,"transcode\_package\_id":337,"stream\_mode\_ids":\[1\],"standard\_app\_bundle\_id":8690,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,26,30\],"video\_cro\_network\_id":169843,"video\_cro\_context\_id":23620202,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":462050467,"video\_cro\_site\_id":1217285,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":9260},{"sub\_yo\_id":9278},{"sub\_yo\_id":9813,"nested\_sub\_yo\_ids":\[17512\]},{"sub\_yo\_id":9816,"nested\_sub\_yo\_ids":\[17409\]},{"sub\_yo\_id":14240,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":14811},{"sub\_yo\_id":14812},{"sub\_yo\_id":18292,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":20155,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":20273,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":22609,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":25790,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":26159,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":27789,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":50520,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":50950,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":51046,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":51445,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":51478,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":51556,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":51614,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":51624,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":51773,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":53231,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":54277,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":54478,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":54999,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":55171,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":55485,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":56525,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":56789,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":58635,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":60190,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":60513,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":61245,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":62044,"nested\_sub\_yo\_ids":\[64125\]},{"sub\_yo\_id":62469,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":62628,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":64432,"nested\_sub\_yo\_ids":\[17512\]},{"sub\_yo\_id":64435,"nested\_sub\_yo\_ids":\[17409\]},{"sub\_yo\_id":64841,"nested\_sub\_yo\_ids":\[64819\]},{"sub\_yo\_id":64844,"nested\_sub\_yo\_ids":\[64819\]},{"sub\_yo\_id":65399,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":65547,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":65704,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":66273,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":66279,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":66525,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":66534,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":66863,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":67289,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":67344,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":67536,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":67582,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":67731,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":67953,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":68720,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":69309,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69530,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":69564,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":69595,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":69665,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":69675,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69682,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":69711,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":69966,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69981,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69988,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":69999,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":70017,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":70020,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":70033,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":70233,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":70241,"nested\_sub\_yo\_ids":\[15721\]},{"sub\_yo\_id":70816,"nested\_sub\_yo\_ids":\[64819\]},{"sub\_yo\_id":70820,"nested\_sub\_yo\_ids":\[64819\]},{"sub\_yo\_id":70883,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":70911,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":70966,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":70979,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":71036,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":71149,"nested\_sub\_yo\_ids":\[15715\]},{"sub\_yo\_id":71238,"nested\_sub\_yo\_ids":\[22302\]}\],"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638},{"sub\_yo\_id":14811},{"sub\_yo\_id":14812}\],"site\_section\_cro\_network\_id":169843,"site\_section\_cro\_asset\_id":23620202,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1217285,"site\_section\_cro\_parsed\_site\_section\_id":23620202,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":462050467,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23620202,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=169843): '{"ab\_test\_item":\[{"bucket\_id":289,"collection\_id":86},{"bucket\_id":291,"collection\_id":87},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":293,"collection\_id":88},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":519,"collection\_id":182},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2018,"collection\_id":2010},{"bucket\_id":2021,"collection\_id":2012},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282953,"collection\_id":3282738},{"bucket\_id":3282961,"collection\_id":3282738},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"151908","name":"the roku channel","storeurl":"<http://therokuchannel.com> "},"asset\_duration":600.0,"asset\_id":462050467,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"169843/MDLVault\_EP019155650004","distributor\_network\_id":169843,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23620202,"distributor\_video\_asset\_id":462050467,"host\_name":"[29773.v.fwmrm.net](http://29773.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_app\_bundle","value":"151908"},{"key":"\_fw\_app\_store\_url","value":"<http://therokuchannel.com> "},{"key":"\_fw\_did","value":"RIDA:a466546c-9800-509b-96d2-3a4cd59105c6"},{"key":"\_fw\_h\_referer","value":"<http://nbc.com> "},{"key":"\_fw\_h\_user\_agent","value":"Roku/DVP-15.2 (15.2.4.3442-51)"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1YNN"},{"key":"\_fw\_vcid2","value":"a466546c-9800-509b-96d2-3a4cd59105c6"}\],"network\_id":169843,"page\_random":"1780171200254","profile\_id":14603,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":60.0,"request\_format":1,"response\_format":13,"site\_section\_cro\_asset\_id":23620202,"site\_section\_cro\_network\_id":169843,"site\_section\_cro\_site\_id":1217285,"site\_section\_id":23620202,"standard\_addressability\_ids":\[4,5,26,30\],"standard\_app\_bundle\_id":8690,"standard\_app\_id":4892,"standard\_brand\_id":3030,"standard\_content\_subscription\_model\_id":3,"standard\_endpoint\_id":99,"standard\_endpoint\_owner\_id":45,"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":88,"stream\_mode\_id":1,"stream\_mode\_ids":\[1\],"time\_position":0.0,"transcode\_package\_id":337,"video\_cro\_asset\_id":462050467,"video\_cro\_context\_id":23620202,"video\_cro\_network\_id":169843,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638},{"sub\_yo\_id":14811},{"sub\_yo\_id":14812}\],"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":9260},{"sub\_yo\_id":9278},{"nested\_sub\_yo\_ids":\[17512\],"sub\_yo\_id":9813},{"nested\_sub\_yo\_ids":\[17409\],"sub\_yo\_id":9816},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":14240},{"sub\_yo\_id":14811},{"sub\_yo\_id":14812},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":18292},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":20155},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":20273},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":22609},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":25790},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":26159},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":27789},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":50520},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":50950},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":51046},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":51445},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":51478},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":51556},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":51614},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":51624},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":51773},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":53231},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":54277},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":54478},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":54999},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":55171},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":55485},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":56525},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":56789},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":58635},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":60190},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":60513},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":61245},{"nested\_sub\_yo\_ids":\[64125\],"sub\_yo\_id":62044},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":62469},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":62628},{"nested\_sub\_yo\_ids":\[17512\],"sub\_yo\_id":64432},{"nested\_sub\_yo\_ids":\[17409\],"sub\_yo\_id":64435},{"nested\_sub\_yo\_ids":\[64819\],"sub\_yo\_id":64841},{"nested\_sub\_yo\_ids":\[64819\],"sub\_yo\_id":64844},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":65399},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":65547},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":65704},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":66273},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":66279},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":66525},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":66534},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":66863},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":67289},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":67344},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":67536},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":67582},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":67731},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":67953},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":68720},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69309},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":69530},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69564},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69595},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69665},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69675},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69682},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":69711},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69966},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69981},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69988},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":69999},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":70017},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":70020},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":70033},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":70233},{"nested\_sub\_yo\_ids":\[15721\],"sub\_yo\_id":70241},{"nested\_sub\_yo\_ids":\[64819\],"sub\_yo\_id":70816},{"nested\_sub\_yo\_ids":\[64819\],"sub\_yo\_id":70820},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":70883},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":70911},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":70966},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":70979},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":71036},{"nested\_sub\_yo\_ids":\[15715\],"sub\_yo\_id":71149},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":71238}\],"video\_cro\_site\_id":1217285,"video\_random":"1780171200254"}'  
    request\_\_scores:  
      Hoover (entity=request, network=169843): '\[\\'{"network\_id":169843,"ad\_id":93989699,"flag":258,"score":0}\\'\]'  
      HooverPP (entity=request, network=169843): '\[\\'{"flag":258,"network\_id":169843,"score":0}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=169843): '{"total":311,"external\_creative":2,"external\_candidate":205}'  
      HooverPP (entity=request, network=169843): '{"total":311}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=169843): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=169843): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=169843): '{"num\_keys":5,"dx\_alias\_growth\_ratio":1798.0,"bg\_alias\_growth\_ratio":3013.0,"num\_dx\_enriched\_keys":1750,"num\_dx\_enriched\_alias\_ids":120}'  
      HooverPP (entity=request, network=169843): '{"bg\_alias\_growth\_ratio":3013.0}'

  \[row=3\]  
    request\_\_cbp:  
      Hoover (entity=request, network=169843): '{"network\_id":169843,"slot\_template\_id":82531}'  
      HooverPP (entity=request, network=169843): '{"slot\_template\_id":82531}'  
    request\_\_context:  
      Hoover (entity=request, network=169843): '{"network\_id":169843,"asset\_id":427635061,"custom\_asset\_id":"169843/l13bpsws4hlm","site\_section\_id":19803924,"page\_random":"4037019315","video\_random":"4037019315","asset\_duration":600.0,"request\_duration":120.0,"time\_position":0.0,"profile\_id":10438,"request\_format":1,"response\_format":13,"ab\_test\_item":\[{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":293},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":297},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":178,"bucket\_id":509},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2006,"bucket\_id":2011},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2010,"bucket\_id":2018},{"collection\_id":2012,"bucket\_id":2021},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282738,"bucket\_id":3282953},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[29773.v.fwmrm.net](http://29773.v.fwmrm.net)","request\_trace\_id":"8726de82210471c0bde543501a151542","rbp\_platform":"OTT","stream\_mode\_id":1,"standard\_brand\_id":5726,"standard\_genre\_ids":\[2,25,26,28,38,40,100\],"content\_form\_id":3,"content\_rating\_id":6,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":32,"standard\_endpoint\_id":45,"website\_root\_id":974571,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":46,"standard\_content\_subscription\_model\_id":3,"stream\_mode\_ids":\[1\],"standard\_app\_bundle\_id":395,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,25,30\],"video\_cro\_network\_id":169843,"video\_cro\_context\_id":19803924,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":427635061,"video\_cro\_site\_id":974571,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638},{"sub\_yo\_id":9260},{"sub\_yo\_id":9813,"nested\_sub\_yo\_ids":\[17504\]},{"sub\_yo\_id":9816,"nested\_sub\_yo\_ids":\[17407\]},{"sub\_yo\_id":18292,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":20149},{"sub\_yo\_id":20273,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":21919,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":22607,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":50950,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":51407},{"sub\_yo\_id":51478,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":51614,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":51624,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":51773,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":53231,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":54478,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":54774,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":54798,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":55171,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":62012,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":62044,"nested\_sub\_yo\_ids":\[64129\]},{"sub\_yo\_id":64432,"nested\_sub\_yo\_ids":\[17504\]},{"sub\_yo\_id":64435,"nested\_sub\_yo\_ids":\[17407\]},{"sub\_yo\_id":64841,"nested\_sub\_yo\_ids":\[64825\]},{"sub\_yo\_id":64844,"nested\_sub\_yo\_ids":\[64825\]},{"sub\_yo\_id":65399,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":65704,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":66273,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":66279,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":67056,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":67082,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":67118,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":67289,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":67536,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":67731,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":67752,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":67849,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":68011,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":68720,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":69072,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69214,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69309,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69530,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":69564,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69595,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69665,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69675,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69682,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69745,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":69966,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69981,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":69988,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":69999,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":70017,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":70020,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":70033,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":70233,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":70241,"nested\_sub\_yo\_ids":\[13454\]},{"sub\_yo\_id":70816,"nested\_sub\_yo\_ids":\[64825\]},{"sub\_yo\_id":70820,"nested\_sub\_yo\_ids":\[64825\]},{"sub\_yo\_id":70883,"nested\_sub\_yo\_ids":\[22302\]},{"sub\_yo\_id":70886,"nested\_sub\_yo\_ids":\[16196\]},{"sub\_yo\_id":70911,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":70966,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":70979,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":71020,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":71036,"nested\_sub\_yo\_ids":\[22285\]},{"sub\_yo\_id":71149,"nested\_sub\_yo\_ids":\[13385\]},{"sub\_yo\_id":71238,"nested\_sub\_yo\_ids":\[22302\]}\],"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638}\],"site\_section\_cro\_network\_id":169843,"site\_section\_cro\_asset\_id":19803924,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":974571,"site\_section\_cro\_parsed\_site\_section\_id":19803924,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":427635061,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":19803924,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=169843): '{"ab\_test\_item":\[{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":293,"collection\_id":88},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":297,"collection\_id":90},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":509,"collection\_id":178},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2011,"collection\_id":2006},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2018,"collection\_id":2010},{"bucket\_id":2021,"collection\_id":2012},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282953,"collection\_id":3282738},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g15147002586","name":"samsung tv plus","storeurl":"<https://www.samsung.com/us/appstore/app/G15147002586/> "},"asset\_duration":600.0,"asset\_id":427635061,"content\_form\_id":3,"content\_rating\_id":6,"custom\_asset\_id":"169843/l13bpsws4hlm","distributor\_network\_id":169843,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":19803924,"distributor\_video\_asset\_id":427635061,"host\_name":"[29773.v.fwmrm.net](http://29773.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_app\_bundle","value":"G15147002586"},{"key":"\_fw\_did","value":"tifa:a244c49b-e29f-61c3-9369-d6cf9175b63e"},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0+(SMART-TV;+Linux;+Tizen+3.0)+AppleWebKit/538.1+(KHTML,+like+Gecko)+Version/3.0+TV+Safari/538.1"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1YNY"},{"key":"\_fw\_vcid2","value":"4551085668124971"}\],"network\_id":169843,"page\_random":"4037019315","profile\_id":10438,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":120.0,"request\_format":1,"response\_format":13,"site\_section\_cro\_asset\_id":19803924,"site\_section\_cro\_network\_id":169843,"site\_section\_cro\_site\_id":974571,"site\_section\_id":19803924,"standard\_addressability\_ids":\[4,5,25,30\],"standard\_app\_bundle\_id":395,"standard\_app\_id":46,"standard\_brand\_id":5726,"standard\_content\_subscription\_model\_id":3,"standard\_endpoint\_id":45,"standard\_endpoint\_owner\_id":32,"standard\_genre\_ids":\[2,25,26,28,38,40,100\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":88,"stream\_mode\_id":1,"stream\_mode\_ids":\[1\],"time\_position":0.0,"video\_cro\_asset\_id":427635061,"video\_cro\_context\_id":19803924,"video\_cro\_network\_id":169843,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638}\],"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":8100},{"sub\_yo\_id":8638},{"sub\_yo\_id":9260},{"nested\_sub\_yo\_ids":\[17504\],"sub\_yo\_id":9813},{"nested\_sub\_yo\_ids":\[17407\],"sub\_yo\_id":9816},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":18292},{"sub\_yo\_id":20149},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":20273},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":21919},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":22607},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":50950},{"sub\_yo\_id":51407},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":51478},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":51614},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":51624},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":51773},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":53231},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":54478},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":54774},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":54798},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":55171},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":62012},{"nested\_sub\_yo\_ids":\[64129\],"sub\_yo\_id":62044},{"nested\_sub\_yo\_ids":\[17504\],"sub\_yo\_id":64432},{"nested\_sub\_yo\_ids":\[17407\],"sub\_yo\_id":64435},{"nested\_sub\_yo\_ids":\[64825\],"sub\_yo\_id":64841},{"nested\_sub\_yo\_ids":\[64825\],"sub\_yo\_id":64844},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":65399},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":65704},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":66273},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":66279},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":67056},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":67082},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":67118},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":67289},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":67536},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":67731},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":67752},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":67849},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":68011},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":68720},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69072},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69214},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69309},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":69530},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69564},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69595},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69665},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69675},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69682},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":69745},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69966},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":69981},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69988},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":69999},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":70017},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":70020},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":70033},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":70233},{"nested\_sub\_yo\_ids":\[13454\],"sub\_yo\_id":70241},{"nested\_sub\_yo\_ids":\[64825\],"sub\_yo\_id":70816},{"nested\_sub\_yo\_ids":\[64825\],"sub\_yo\_id":70820},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":70883},{"nested\_sub\_yo\_ids":\[16196\],"sub\_yo\_id":70886},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":70911},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":70966},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":70979},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":71020},{"nested\_sub\_yo\_ids":\[22285\],"sub\_yo\_id":71036},{"nested\_sub\_yo\_ids":\[13385\],"sub\_yo\_id":71149},{"nested\_sub\_yo\_ids":\[22302\],"sub\_yo\_id":71238}\],"video\_cro\_site\_id":974571,"video\_random":"4037019315"}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=169843): '{"flag1":1077936132,"flag2":51380224,"value1":1507329,"value2":262303,"flag3":67403824,"value3":13318495111,"value4":1099511718144,"value5":4441030262784,"value6":1095219808768,"value7":117440513,"flag4":1623232512,"decision\_log":":::::::geoinfo#ip#0#0#0#0#4623#528","value9":2677,"value10":2143,"value11":53,"value12":174,"value13":8,"value14":1,"inventory\_protections":\[{"level":2,"scope":1,"separation":1}\],"value15":0}'  
      HooverPP (entity=request, network=169843): '{"flag1":1077936132,"flag2":51380224,"flag3":67403824,"flag4":1623232512,"inventory\_protections":\[{"level":2,"scope":1,"separation":1}\],"value1":1507329,"value10":2143,"value11":53,"value12":174,"value13":8,"value14":1,"value15":0,"value2":262303,"value3":13318495111,"value4":1099511718144,"value5":4441030262784,"value6":1095219808768,"value7":117440513,"value9":2677}'  
    request\_\_scores:  
      Hoover (entity=request, network=169843): '\[\\'{"network\_id":169843,"ad\_id":93989699,"flag":258,"score":0}\\'\]'  
      HooverPP (entity=request, network=169843): '\[\\'{"flag":258,"network\_id":169843,"score":0}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=169843): '{"total":864,"external\_creative":11,"external\_candidate":601}'  
      HooverPP (entity=request, network=169843): '{"total":864}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=169843): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=169843): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=169843): '{"num\_keys":6,"dx\_alias\_growth\_ratio":2150.0,"bg\_alias\_growth\_ratio":2684.0,"num\_dx\_enriched\_keys":1383,"num\_dx\_enriched\_alias\_ids":236}'  
      HooverPP (entity=request, network=169843): '{"bg\_alias\_growth\_ratio":2684.0}'

```
  END OF REPORT
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=16.59s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=441.29s | rows=15  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415975, 92676151, 93415904, 93418034, 93340683, 93185984, 93417083, 92700205, 92874299, 93093201)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=69.33s | rows=15  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415975, 92676151, 93415904, 93418034, 93340683, 93185984, 93417083, 92700205, 92874299, 93093201)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=request, network=191701)  
  Source B : HooverPP (entity=request, network=191701)  
  Rows  A  : 15  
  Rows  B  : 15  
  Columns A: 231  
  Columns B: 231

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 15

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (231 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/15 (0.00%)
  Column match %    : 224/231 (96.97%)
  Cell/value match %: 3,371/3,465 (97.29%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
request__client_facing_ivt_reason_flag                       15 row(s)
request__context__profile_concrete_event_id                  15 row(s)
request__context__standard_content_viewership_profile_ids    15 row(s)
request__context__standard_iab_category_ids                  15 row(s)
request__context__standard_sport_entity_ids                  15 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos 15 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids 15 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id 15 row(s)
request__decision_info__external_bridge                      15 row(s)
request__decision_info__external_bridge__slot_index          15 row(s)
request__decision_info__external_bridge__status              15 row(s)
request__decision_info__inventory_protections                15 row(s)
request__decision_info__inventory_protections__level         15 row(s)
request__decision_info__inventory_protections__scope         15 row(s)
request__decision_info__inventory_protections__separation    15 row(s)
request__linear_capnedit                                     15 row(s)
request__linear_capnedit__active_state                       15 row(s)
request__linear_capnedit__device_id                          15 row(s)
request__linear_capnedit__is_dvr                             15 row(s)
request__linear_capnedit__last_activity_time                 15 row(s)
request__linear_capnedit__mode                               15 row(s)
request__linear_capnedit__tune_time                          15 row(s)
request__mrc_compliance_label                                15 row(s)
request__soft_guaranteed_ad                                  15 row(s)
request__soft_guaranteed_ad__ad_id                           15 row(s)
request__soft_guaranteed_ad__entity_id                       15 row(s)
request__soft_guaranteed_ad__entity_type                     15 row(s)
request__soft_guaranteed_ad__network_id                      15 row(s)
request__soft_guaranteed_ad__num_competing_ads               15 row(s)
request__guaranteed_deal_avail                               11 row(s)
request__guaranteed_deal_avail__buyer_id                     11 row(s)
request__guaranteed_deal_avail__internal_deal_id             11 row(s)
request__yield_optimization_ids                              11 row(s)
request__yield_optimization_ids__demand_id                   11 row(s)
request__yield_optimization_ids__demand_type                 11 row(s)
request__yield_optimization_ids__optimization_ids            11 row(s)
request__context__standard_language_ids                      4 row(s)
```

  ❌ 15 row(s) have differences:

  Column diff summary (sorted by frequency):  
    request\_\_cbp                                                 15 row(s)  
    request\_\_context                                             15 row(s)  
    request\_\_scores                                              15 row(s)  
    request\_\_time\_record                                         15 row(s)  
    request\_\_timestamp                                           15 row(s)  
    request\_\_traffic\_compliance                                  15 row(s)  
    request\_\_userdb\_audience\_user\_info                           4 row(s)

  Detailed diffs:

  \[row=2\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=3\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=4\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=5\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=6\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=7\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=8\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=9\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=10\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=11\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=12\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":70223}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":70223}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":529832,"asset\_id":201539518,"custom\_asset\_id":"191701/149485\_004\_US","site\_section\_id":23287348,"video\_random":"4021037899","asset\_duration":2552.0,"request\_duration":2552.0,"time\_position":0.0,"profile\_id":16004,"request\_format":1,"response\_format":12,"ab\_test\_item":\[{"collection\_id":66,"bucket\_id":242},{"collection\_id":88,"bucket\_id":499},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","request\_trace\_id":"765cf079cc2d471bcb09544f6dbb8254","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,16,28,33,43,70\],"content\_form\_id":3,"content\_rating\_id":13,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":67,"standard\_endpoint\_id":467,"website\_root\_id":1159746,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":600,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":23287350,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":201539518,"video\_cro\_site\_id":1256035,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1159746,"site\_section\_cro\_parsed\_site\_section\_id":23287348,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":201539518,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":242,"collection\_id":66},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"g20280015643","name":"DiscoveryPlus","storeurl":"<https://www.samsung.com/us/appstore/app/G20280015643/> "},"asset\_duration":2552.0,"asset\_id":201539518,"content\_form\_id":3,"content\_rating\_id":13,"custom\_asset\_id":"191701/149485\_004\_US","distributor\_network\_id":529832,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23287348,"distributor\_video\_asset\_id":201539518,"host\_name":"[815a8.v.fwmrm.net](http://815a8.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_did","value":"tifa:"},{"key":"\_fw\_h\_referer","value":"<https://www.discoveryplus.com/> "},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) Ignition X11/1.1 TV Safari/538.1"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P5A0FD4DE-4AE6-4B22-811B-36B9BD091980"},{"key":"\_fw\_vcid2","value":"529832:Ef01zYA5uKp90td014T52mZKvcINAmYAPvGkiikZw-I"},{"key":"agerange","value":"3"}\],"network\_id":529832,"profile\_id":16004,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":600},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":2552.0,"request\_format":1,"response\_format":12,"site\_section\_cro\_asset\_id":23287348,"site\_section\_cro\_network\_id":529832,"site\_section\_cro\_site\_id":1159746,"site\_section\_id":23287348,"standard\_addressability\_ids":\[4,5\],"standard\_brand\_id":2082,"standard\_endpoint\_id":467,"standard\_endpoint\_owner\_id":67,"standard\_genre\_ids":\[2,16,28,33,43,70\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":201539518,"video\_cro\_context\_id":23287350,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53149}\],"video\_cro\_site\_id":1256035,"video\_random":"4021037899"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":92785534,"flag":258,"score":11000}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":258,"network\_id":191701,"score":11000}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":338,"external\_candidate":229}'  
      HooverPP (entity=request, network=191701): '{"total":338}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=191701): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'

  \[row=13\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":78037}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":78037}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"asset\_id":372601141,"custom\_asset\_id":"191701/230147.004.695","site\_section\_id":17308529,"page\_random":"9773372672","video\_random":"5045536570","asset\_duration":3389.0,"request\_duration":3389.0,"time\_position":0.0,"profile\_id":12318,"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":42,"bucket\_id":366},{"collection\_id":51,"bucket\_id":138},{"collection\_id":66,"bucket\_id":242},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":291},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","request\_trace\_id":"b63e00aa16313cb65a327d5dacfc3137","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,27,28,125\],"content\_form\_id":3,"content\_rating\_id":12,"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":56,"standard\_endpoint\_id":629,"website\_root\_id":1074211,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":17308529,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":372601141,"video\_cro\_site\_id":1074211,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1074211,"site\_section\_cro\_parsed\_site\_section\_id":17308529,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":372601141,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":366,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":242,"collection\_id":66},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":291,"collection\_id":87},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"61322","name":"HBOMAX","storeurl":"<https://channelstore.roku.com/details/61322> "},"asset\_duration":3389.0,"asset\_id":372601141,"content\_form\_id":3,"content\_rating\_id":12,"custom\_asset\_id":"191701/230147.004.695","distributor\_network\_id":191701,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_video\_asset\_id":372601141,"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_uid","value":"UID2:A4AAADf66xotgRqG5o4MNVNLhnqHLwNGiAZpEK-2W6wlQAZlPM-aQ0UuAcJAWRb8h83imWDme0BbvPhqnxe6QpO\_vuyoUxhRbUjXjM2KRx6t5ywvt\_\_zjXPX9HvZ2iCvYwC1fACMAGqnLGudfie4HDF\_bPJMz7unnreyiD9BpVNczfW2qMWueLxovDU-Fb\_XMYgzRWfo7KaXk1DEv8rfrmom-Q,IDL:Am3ORhb256dNxb6doIBQZNejP\_xkp7vBICidNkV5OX17AtN17DpKWtuN3x7zZmC9sz5pIwTTvg\_a-UuCTk1budhlDp1I2OgAM3xhG\_zdG1zrrKU1MwcM8FsQE0uBmTeuICIsWg-EHZK259pHEGsEZdZGB45njhXW8pmH\_qHDJz497uWvjEFCTovLOcN2J3vF4xMkHGeX,PAIRID:WyJBMDR5Mjl2bEthaWI5OGYycXlJR3oxR29kQTFuaWRZc3hSQkg1UGFGUEJwcSJd"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"rida:40ea950c-3c53-5b0d-a25f-5d79a6f7cd58"},{"key":"\_fw\_gdpr","value":"0"},{"key":"\_fw\_h\_referer","value":"<https://play.max.com> "},{"key":"\_fw\_h\_user\_agent","value":"Roku/DVP-15.2+(15.2.4.3442-JW)"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"PBF1AE4D4-1B43-4E68-B057-2E3A54A235E5"},{"key":"\_fw\_us\_privacy","value":"1YNN"},{"key":"\_fw\_vcid2","value":"126a72a3-f848-4eaa-8a58-69d732f2c82d"},{"key":"accountid","value":"1681234581891800346"},{"key":"asset\_vds\_id","value":"301c39a0-ed6a-4888-91a5-3df678c6a671"},{"key":"garm\_categories","value":"1400"},{"key":"garm\_categories","value":"200"},{"key":"garm\_categories","value":"700"},{"key":"garm\_categories","value":"300"},{"key":"garm\_categories","value":"1200"},{"key":"garm\_categories","value":"401"},{"key":"garm\_categories","value":"802"},{"key":"garm\_categories","value":"803"},{"key":"iab\_categories","value":"53"},{"key":"iab\_categories","value":"52"},{"key":"iab\_categories","value":"1"},{"key":"iab\_categories","value":"552"},{"key":"iab\_categories","value":"210"},{"key":"iab\_categories","value":"380"},{"key":"iab\_categories","value":"579"},{"key":"iab\_categories","value":"132"},{"key":"iab\_categories","value":"379"},{"key":"iab\_categories","value":"239"},{"key":"iab\_categories","value":"163"},{"key":"iab\_categories","value":"153"},{"key":"iab\_categories","value":"179"},{"key":"paln","value":"YXNlbGM9MyZhc3Njc19jb3JyZWxhdG9yPWRlY2M3M2MyLTFmZGYtNGEzMy05ZDQ5LTg3MzE4YTY1MDRkZiZjdHY9MSZndXY9ci4yLjAuMGIyJmlkX3R5cGU9cmlkYSZpbWF2PXIuMy4yLjImaXNfbGF0PTAmbXNpZD02MTMyMiZwc3M9MCZyZGlkPTQwZWE5NTBjLTNjNTMtNWIwZC1hMjVmLTVkNzlhNmY3Y2Q1OCZzaWQ9ZjY1ZmI1MmMtN2MxZS00ZmU5LWFkN2MtYzFkZTdjYTQxNmU5JnVfc289bCZ1YT1IQk8lMjBNYXglMkY3LjMuMCUyMCUyOFJva3UlMjAxNS4yLjQlM0IlMjBlbl9VUyUzQiUyMFN0cmVhbWluZyUyMFN0aWNrJTNCJTIwQnVpbGQlMkYzNDQyJTI5JnVybD1kaXNjb3ZlcnkuY29tJnZjb25wPTImdmlkZW9fdXJsX3RvX2ZldGNoPWRpc2NvdmVyeS5jb20mdnBfaD0xMDgwJnZwX3c9MTkyMCZ2cGE9YXV0byZ2cG11dGU9MCZ3dGE9MQ.."},{"key":"platform","value":"roku"},{"key":"playbackId","value":"2445cf88-1fd1-4e39-af1d-d2edb312b51c"},{"key":"playername","value":"RokuPSDK/0.1.0"},{"key":"preroll","value":"1"},{"key":"product"},{"key":"program\_id","value":"2521d05d-cbc0-4cb7-84a7-28a9cf193aa0"},{"key":"restrictedProfile","value":"0"},{"key":"sentiment"}\],"network\_id":191701,"page\_random":"9773372672","profile\_id":12318,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":3389.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_site\_id":1074211,"site\_section\_id":17308529,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"standard\_brand\_id":2082,"standard\_endpoint\_id":629,"standard\_endpoint\_owner\_id":56,"standard\_genre\_ids":\[2,27,28,125\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":372601141,"video\_cro\_context\_id":17308529,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"video\_cro\_site\_id":1074211,"video\_random":"5045536570"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":94128743,"flag":513,"score":2666}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":513,"network\_id":191701,"score":2666}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":1439,"external\_creative":199,"external\_candidate":1003}'  
      HooverPP (entity=request, network=191701): '{"total":1439}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:01.000'  
      HooverPP (entity=request, network=191701): '1780171201'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=191701): '{"num\_keys":8,"dx\_alias\_growth\_ratio":2752.0,"bg\_alias\_growth\_ratio":2768.0,"num\_dx\_enriched\_keys":2666,"num\_dx\_enriched\_alias\_ids":240}'  
      HooverPP (entity=request, network=191701): '{"bg\_alias\_growth\_ratio":2768.0}'

  \[row=14\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":78037}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":78037}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"asset\_id":372601141,"custom\_asset\_id":"191701/230147.004.695","site\_section\_id":17308529,"page\_random":"9773372672","video\_random":"5045536570","asset\_duration":3389.0,"request\_duration":3389.0,"time\_position":0.0,"profile\_id":12318,"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":42,"bucket\_id":366},{"collection\_id":51,"bucket\_id":138},{"collection\_id":66,"bucket\_id":242},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":291},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","request\_trace\_id":"b63e00aa16313cb65a327d5dacfc3137","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,27,28,125\],"content\_form\_id":3,"content\_rating\_id":12,"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":56,"standard\_endpoint\_id":629,"website\_root\_id":1074211,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":17308529,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":372601141,"video\_cro\_site\_id":1074211,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1074211,"site\_section\_cro\_parsed\_site\_section\_id":17308529,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":372601141,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":366,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":242,"collection\_id":66},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":291,"collection\_id":87},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"61322","name":"HBOMAX","storeurl":"<https://channelstore.roku.com/details/61322> "},"asset\_duration":3389.0,"asset\_id":372601141,"content\_form\_id":3,"content\_rating\_id":12,"custom\_asset\_id":"191701/230147.004.695","distributor\_network\_id":191701,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_video\_asset\_id":372601141,"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_uid","value":"UID2:A4AAADf66xotgRqG5o4MNVNLhnqHLwNGiAZpEK-2W6wlQAZlPM-aQ0UuAcJAWRb8h83imWDme0BbvPhqnxe6QpO\_vuyoUxhRbUjXjM2KRx6t5ywvt\_\_zjXPX9HvZ2iCvYwC1fACMAGqnLGudfie4HDF\_bPJMz7unnreyiD9BpVNczfW2qMWueLxovDU-Fb\_XMYgzRWfo7KaXk1DEv8rfrmom-Q,IDL:Am3ORhb256dNxb6doIBQZNejP\_xkp7vBICidNkV5OX17AtN17DpKWtuN3x7zZmC9sz5pIwTTvg\_a-UuCTk1budhlDp1I2OgAM3xhG\_zdG1zrrKU1MwcM8FsQE0uBmTeuICIsWg-EHZK259pHEGsEZdZGB45njhXW8pmH\_qHDJz497uWvjEFCTovLOcN2J3vF4xMkHGeX,PAIRID:WyJBMDR5Mjl2bEthaWI5OGYycXlJR3oxR29kQTFuaWRZc3hSQkg1UGFGUEJwcSJd"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"rida:40ea950c-3c53-5b0d-a25f-5d79a6f7cd58"},{"key":"\_fw\_gdpr","value":"0"},{"key":"\_fw\_h\_referer","value":"<https://play.max.com> "},{"key":"\_fw\_h\_user\_agent","value":"Roku/DVP-15.2+(15.2.4.3442-JW)"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"PBF1AE4D4-1B43-4E68-B057-2E3A54A235E5"},{"key":"\_fw\_us\_privacy","value":"1YNN"},{"key":"\_fw\_vcid2","value":"126a72a3-f848-4eaa-8a58-69d732f2c82d"},{"key":"accountid","value":"1681234581891800346"},{"key":"asset\_vds\_id","value":"301c39a0-ed6a-4888-91a5-3df678c6a671"},{"key":"garm\_categories","value":"1400"},{"key":"garm\_categories","value":"200"},{"key":"garm\_categories","value":"700"},{"key":"garm\_categories","value":"300"},{"key":"garm\_categories","value":"1200"},{"key":"garm\_categories","value":"401"},{"key":"garm\_categories","value":"802"},{"key":"garm\_categories","value":"803"},{"key":"iab\_categories","value":"53"},{"key":"iab\_categories","value":"52"},{"key":"iab\_categories","value":"1"},{"key":"iab\_categories","value":"552"},{"key":"iab\_categories","value":"210"},{"key":"iab\_categories","value":"380"},{"key":"iab\_categories","value":"579"},{"key":"iab\_categories","value":"132"},{"key":"iab\_categories","value":"379"},{"key":"iab\_categories","value":"239"},{"key":"iab\_categories","value":"163"},{"key":"iab\_categories","value":"153"},{"key":"iab\_categories","value":"179"},{"key":"paln","value":"YXNlbGM9MyZhc3Njc19jb3JyZWxhdG9yPWRlY2M3M2MyLTFmZGYtNGEzMy05ZDQ5LTg3MzE4YTY1MDRkZiZjdHY9MSZndXY9ci4yLjAuMGIyJmlkX3R5cGU9cmlkYSZpbWF2PXIuMy4yLjImaXNfbGF0PTAmbXNpZD02MTMyMiZwc3M9MCZyZGlkPTQwZWE5NTBjLTNjNTMtNWIwZC1hMjVmLTVkNzlhNmY3Y2Q1OCZzaWQ9ZjY1ZmI1MmMtN2MxZS00ZmU5LWFkN2MtYzFkZTdjYTQxNmU5JnVfc289bCZ1YT1IQk8lMjBNYXglMkY3LjMuMCUyMCUyOFJva3UlMjAxNS4yLjQlM0IlMjBlbl9VUyUzQiUyMFN0cmVhbWluZyUyMFN0aWNrJTNCJTIwQnVpbGQlMkYzNDQyJTI5JnVybD1kaXNjb3ZlcnkuY29tJnZjb25wPTImdmlkZW9fdXJsX3RvX2ZldGNoPWRpc2NvdmVyeS5jb20mdnBfaD0xMDgwJnZwX3c9MTkyMCZ2cGE9YXV0byZ2cG11dGU9MCZ3dGE9MQ.."},{"key":"platform","value":"roku"},{"key":"playbackId","value":"2445cf88-1fd1-4e39-af1d-d2edb312b51c"},{"key":"playername","value":"RokuPSDK/0.1.0"},{"key":"preroll","value":"1"},{"key":"product"},{"key":"program\_id","value":"2521d05d-cbc0-4cb7-84a7-28a9cf193aa0"},{"key":"restrictedProfile","value":"0"},{"key":"sentiment"}\],"network\_id":191701,"page\_random":"9773372672","profile\_id":12318,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":3389.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_site\_id":1074211,"site\_section\_id":17308529,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"standard\_brand\_id":2082,"standard\_endpoint\_id":629,"standard\_endpoint\_owner\_id":56,"standard\_genre\_ids":\[2,27,28,125\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":372601141,"video\_cro\_context\_id":17308529,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"video\_cro\_site\_id":1074211,"video\_random":"5045536570"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":94128743,"flag":513,"score":2666}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":513,"network\_id":191701,"score":2666}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":1439,"external\_creative":199,"external\_candidate":1003}'  
      HooverPP (entity=request, network=191701): '{"total":1439}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:01.000'  
      HooverPP (entity=request, network=191701): '1780171201'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=191701): '{"num\_keys":8,"dx\_alias\_growth\_ratio":2752.0,"bg\_alias\_growth\_ratio":2768.0,"num\_dx\_enriched\_keys":2666,"num\_dx\_enriched\_alias\_ids":240}'  
      HooverPP (entity=request, network=191701): '{"bg\_alias\_growth\_ratio":2768.0}'

  \[row=15\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":78037}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":78037}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"asset\_id":372601141,"custom\_asset\_id":"191701/230147.004.695","site\_section\_id":17308529,"page\_random":"9773372672","video\_random":"5045536570","asset\_duration":3389.0,"request\_duration":3389.0,"time\_position":0.0,"profile\_id":12318,"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":42,"bucket\_id":366},{"collection\_id":51,"bucket\_id":138},{"collection\_id":66,"bucket\_id":242},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":291},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","request\_trace\_id":"b63e00aa16313cb65a327d5dacfc3137","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,27,28,125\],"content\_form\_id":3,"content\_rating\_id":12,"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":56,"standard\_endpoint\_id":629,"website\_root\_id":1074211,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":17308529,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":372601141,"video\_cro\_site\_id":1074211,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1074211,"site\_section\_cro\_parsed\_site\_section\_id":17308529,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":372601141,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":366,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":242,"collection\_id":66},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":291,"collection\_id":87},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"61322","name":"HBOMAX","storeurl":"<https://channelstore.roku.com/details/61322> "},"asset\_duration":3389.0,"asset\_id":372601141,"content\_form\_id":3,"content\_rating\_id":12,"custom\_asset\_id":"191701/230147.004.695","distributor\_network\_id":191701,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_video\_asset\_id":372601141,"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_uid","value":"UID2:A4AAADf66xotgRqG5o4MNVNLhnqHLwNGiAZpEK-2W6wlQAZlPM-aQ0UuAcJAWRb8h83imWDme0BbvPhqnxe6QpO\_vuyoUxhRbUjXjM2KRx6t5ywvt\_\_zjXPX9HvZ2iCvYwC1fACMAGqnLGudfie4HDF\_bPJMz7unnreyiD9BpVNczfW2qMWueLxovDU-Fb\_XMYgzRWfo7KaXk1DEv8rfrmom-Q,IDL:Am3ORhb256dNxb6doIBQZNejP\_xkp7vBICidNkV5OX17AtN17DpKWtuN3x7zZmC9sz5pIwTTvg\_a-UuCTk1budhlDp1I2OgAM3xhG\_zdG1zrrKU1MwcM8FsQE0uBmTeuICIsWg-EHZK259pHEGsEZdZGB45njhXW8pmH\_qHDJz497uWvjEFCTovLOcN2J3vF4xMkHGeX,PAIRID:WyJBMDR5Mjl2bEthaWI5OGYycXlJR3oxR29kQTFuaWRZc3hSQkg1UGFGUEJwcSJd"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"rida:40ea950c-3c53-5b0d-a25f-5d79a6f7cd58"},{"key":"\_fw\_gdpr","value":"0"},{"key":"\_fw\_h\_referer","value":"<https://play.max.com> "},{"key":"\_fw\_h\_user\_agent","value":"Roku/DVP-15.2+(15.2.4.3442-JW)"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"PBF1AE4D4-1B43-4E68-B057-2E3A54A235E5"},{"key":"\_fw\_us\_privacy","value":"1YNN"},{"key":"\_fw\_vcid2","value":"126a72a3-f848-4eaa-8a58-69d732f2c82d"},{"key":"accountid","value":"1681234581891800346"},{"key":"asset\_vds\_id","value":"301c39a0-ed6a-4888-91a5-3df678c6a671"},{"key":"garm\_categories","value":"1400"},{"key":"garm\_categories","value":"200"},{"key":"garm\_categories","value":"700"},{"key":"garm\_categories","value":"300"},{"key":"garm\_categories","value":"1200"},{"key":"garm\_categories","value":"401"},{"key":"garm\_categories","value":"802"},{"key":"garm\_categories","value":"803"},{"key":"iab\_categories","value":"53"},{"key":"iab\_categories","value":"52"},{"key":"iab\_categories","value":"1"},{"key":"iab\_categories","value":"552"},{"key":"iab\_categories","value":"210"},{"key":"iab\_categories","value":"380"},{"key":"iab\_categories","value":"579"},{"key":"iab\_categories","value":"132"},{"key":"iab\_categories","value":"379"},{"key":"iab\_categories","value":"239"},{"key":"iab\_categories","value":"163"},{"key":"iab\_categories","value":"153"},{"key":"iab\_categories","value":"179"},{"key":"paln","value":"YXNlbGM9MyZhc3Njc19jb3JyZWxhdG9yPWRlY2M3M2MyLTFmZGYtNGEzMy05ZDQ5LTg3MzE4YTY1MDRkZiZjdHY9MSZndXY9ci4yLjAuMGIyJmlkX3R5cGU9cmlkYSZpbWF2PXIuMy4yLjImaXNfbGF0PTAmbXNpZD02MTMyMiZwc3M9MCZyZGlkPTQwZWE5NTBjLTNjNTMtNWIwZC1hMjVmLTVkNzlhNmY3Y2Q1OCZzaWQ9ZjY1ZmI1MmMtN2MxZS00ZmU5LWFkN2MtYzFkZTdjYTQxNmU5JnVfc289bCZ1YT1IQk8lMjBNYXglMkY3LjMuMCUyMCUyOFJva3UlMjAxNS4yLjQlM0IlMjBlbl9VUyUzQiUyMFN0cmVhbWluZyUyMFN0aWNrJTNCJTIwQnVpbGQlMkYzNDQyJTI5JnVybD1kaXNjb3ZlcnkuY29tJnZjb25wPTImdmlkZW9fdXJsX3RvX2ZldGNoPWRpc2NvdmVyeS5jb20mdnBfaD0xMDgwJnZwX3c9MTkyMCZ2cGE9YXV0byZ2cG11dGU9MCZ3dGE9MQ.."},{"key":"platform","value":"roku"},{"key":"playbackId","value":"2445cf88-1fd1-4e39-af1d-d2edb312b51c"},{"key":"playername","value":"RokuPSDK/0.1.0"},{"key":"preroll","value":"1"},{"key":"product"},{"key":"program\_id","value":"2521d05d-cbc0-4cb7-84a7-28a9cf193aa0"},{"key":"restrictedProfile","value":"0"},{"key":"sentiment"}\],"network\_id":191701,"page\_random":"9773372672","profile\_id":12318,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":3389.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_site\_id":1074211,"site\_section\_id":17308529,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"standard\_brand\_id":2082,"standard\_endpoint\_id":629,"standard\_endpoint\_owner\_id":56,"standard\_genre\_ids":\[2,27,28,125\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":372601141,"video\_cro\_context\_id":17308529,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"video\_cro\_site\_id":1074211,"video\_random":"5045536570"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":94128743,"flag":513,"score":2666}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":513,"network\_id":191701,"score":2666}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":1439,"external\_creative":199,"external\_candidate":1003}'  
      HooverPP (entity=request, network=191701): '{"total":1439}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:01.000'  
      HooverPP (entity=request, network=191701): '1780171201'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=191701): '{"num\_keys":8,"dx\_alias\_growth\_ratio":2752.0,"bg\_alias\_growth\_ratio":2768.0,"num\_dx\_enriched\_keys":2666,"num\_dx\_enriched\_alias\_ids":240}'  
      HooverPP (entity=request, network=191701): '{"bg\_alias\_growth\_ratio":2768.0}'

  \[row=16\]  
    request\_\_cbp:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"slot\_template\_id":78037}'  
      HooverPP (entity=request, network=191701): '{"slot\_template\_id":78037}'  
    request\_\_context:  
      Hoover (entity=request, network=191701): '{"network\_id":191701,"asset\_id":372601141,"custom\_asset\_id":"191701/230147.004.695","site\_section\_id":17308529,"page\_random":"9773372672","video\_random":"5045536570","asset\_duration":3389.0,"request\_duration":3389.0,"time\_position":0.0,"profile\_id":12318,"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":42,"bucket\_id":366},{"collection\_id":51,"bucket\_id":138},{"collection\_id":66,"bucket\_id":242},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":291},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":134,"bucket\_id":429},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":3282739,"bucket\_id":3282955},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","request\_trace\_id":"b63e00aa16313cb65a327d5dacfc3137","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":2082,"standard\_genre\_ids":\[2,27,28,125\],"content\_form\_id":3,"content\_rating\_id":12,"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":645,"standard\_endpoint\_owner\_id":56,"standard\_endpoint\_id":629,"website\_root\_id":1074211,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":200},"stream\_mode\_ids":\[2\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"video\_cro\_network\_id":191701,"video\_cro\_context\_id":17308529,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":372601141,"video\_cro\_site\_id":1074211,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1074211,"site\_section\_cro\_parsed\_site\_section\_id":17308529,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":372601141,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=191701): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":366,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":242,"collection\_id":66},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":291,"collection\_id":87},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":3282955,"collection\_id":3282739},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"61322","name":"HBOMAX","storeurl":"<https://channelstore.roku.com/details/61322> "},"asset\_duration":3389.0,"asset\_id":372601141,"content\_form\_id":3,"content\_rating\_id":12,"custom\_asset\_id":"191701/230147.004.695","distributor\_network\_id":191701,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17308529,"distributor\_video\_asset\_id":372601141,"host\_name":"[2ecd5.v.fwmrm.net](http://2ecd5.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_uid","value":"UID2:A4AAADf66xotgRqG5o4MNVNLhnqHLwNGiAZpEK-2W6wlQAZlPM-aQ0UuAcJAWRb8h83imWDme0BbvPhqnxe6QpO\_vuyoUxhRbUjXjM2KRx6t5ywvt\_\_zjXPX9HvZ2iCvYwC1fACMAGqnLGudfie4HDF\_bPJMz7unnreyiD9BpVNczfW2qMWueLxovDU-Fb\_XMYgzRWfo7KaXk1DEv8rfrmom-Q,IDL:Am3ORhb256dNxb6doIBQZNejP\_xkp7vBICidNkV5OX17AtN17DpKWtuN3x7zZmC9sz5pIwTTvg\_a-UuCTk1budhlDp1I2OgAM3xhG\_zdG1zrrKU1MwcM8FsQE0uBmTeuICIsWg-EHZK259pHEGsEZdZGB45njhXW8pmH\_qHDJz497uWvjEFCTovLOcN2J3vF4xMkHGeX,PAIRID:WyJBMDR5Mjl2bEthaWI5OGYycXlJR3oxR29kQTFuaWRZc3hSQkg1UGFGUEJwcSJd"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"rida:40ea950c-3c53-5b0d-a25f-5d79a6f7cd58"},{"key":"\_fw\_gdpr","value":"0"},{"key":"\_fw\_h\_referer","value":"<https://play.max.com> "},{"key":"\_fw\_h\_user\_agent","value":"Roku/DVP-15.2+(15.2.4.3442-JW)"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"PBF1AE4D4-1B43-4E68-B057-2E3A54A235E5"},{"key":"\_fw\_us\_privacy","value":"1YNN"},{"key":"\_fw\_vcid2","value":"126a72a3-f848-4eaa-8a58-69d732f2c82d"},{"key":"accountid","value":"1681234581891800346"},{"key":"asset\_vds\_id","value":"301c39a0-ed6a-4888-91a5-3df678c6a671"},{"key":"garm\_categories","value":"1400"},{"key":"garm\_categories","value":"200"},{"key":"garm\_categories","value":"700"},{"key":"garm\_categories","value":"300"},{"key":"garm\_categories","value":"1200"},{"key":"garm\_categories","value":"401"},{"key":"garm\_categories","value":"802"},{"key":"garm\_categories","value":"803"},{"key":"iab\_categories","value":"53"},{"key":"iab\_categories","value":"52"},{"key":"iab\_categories","value":"1"},{"key":"iab\_categories","value":"552"},{"key":"iab\_categories","value":"210"},{"key":"iab\_categories","value":"380"},{"key":"iab\_categories","value":"579"},{"key":"iab\_categories","value":"132"},{"key":"iab\_categories","value":"379"},{"key":"iab\_categories","value":"239"},{"key":"iab\_categories","value":"163"},{"key":"iab\_categories","value":"153"},{"key":"iab\_categories","value":"179"},{"key":"paln","value":"YXNlbGM9MyZhc3Njc19jb3JyZWxhdG9yPWRlY2M3M2MyLTFmZGYtNGEzMy05ZDQ5LTg3MzE4YTY1MDRkZiZjdHY9MSZndXY9ci4yLjAuMGIyJmlkX3R5cGU9cmlkYSZpbWF2PXIuMy4yLjImaXNfbGF0PTAmbXNpZD02MTMyMiZwc3M9MCZyZGlkPTQwZWE5NTBjLTNjNTMtNWIwZC1hMjVmLTVkNzlhNmY3Y2Q1OCZzaWQ9ZjY1ZmI1MmMtN2MxZS00ZmU5LWFkN2MtYzFkZTdjYTQxNmU5JnVfc289bCZ1YT1IQk8lMjBNYXglMkY3LjMuMCUyMCUyOFJva3UlMjAxNS4yLjQlM0IlMjBlbl9VUyUzQiUyMFN0cmVhbWluZyUyMFN0aWNrJTNCJTIwQnVpbGQlMkYzNDQyJTI5JnVybD1kaXNjb3ZlcnkuY29tJnZjb25wPTImdmlkZW9fdXJsX3RvX2ZldGNoPWRpc2NvdmVyeS5jb20mdnBfaD0xMDgwJnZwX3c9MTkyMCZ2cGE9YXV0byZ2cG11dGU9MCZ3dGE9MQ.."},{"key":"platform","value":"roku"},{"key":"playbackId","value":"2445cf88-1fd1-4e39-af1d-d2edb312b51c"},{"key":"playername","value":"RokuPSDK/0.1.0"},{"key":"preroll","value":"1"},{"key":"product"},{"key":"program\_id","value":"2521d05d-cbc0-4cb7-84a7-28a9cf193aa0"},{"key":"restrictedProfile","value":"0"},{"key":"sentiment"}\],"network\_id":191701,"page\_random":"9773372672","profile\_id":12318,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":3389.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17308529,"site\_section\_cro\_network\_id":191701,"site\_section\_cro\_site\_id":1074211,"site\_section\_id":17308529,"standard\_addressability\_ids":\[4,5,8,9,15,26,30,31\],"standard\_brand\_id":2082,"standard\_endpoint\_id":629,"standard\_endpoint\_owner\_id":56,"standard\_genre\_ids":\[2,27,28,125\],"standard\_privacy\_id":1,"standard\_programmer\_id":645,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":372601141,"video\_cro\_context\_id":17308529,"video\_cro\_network\_id":191701,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":53141}\],"video\_cro\_site\_id":1074211,"video\_random":"5045536570"}'  
    request\_\_scores:  
      Hoover (entity=request, network=191701): '\[\\'{"network\_id":191701,"ad\_id":94128743,"flag":513,"score":2666}\\'\]'  
      HooverPP (entity=request, network=191701): '\[\\'{"flag":513,"network\_id":191701,"score":2666}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=191701): '{"total":1439,"external\_creative":199,"external\_candidate":1003}'  
      HooverPP (entity=request, network=191701): '{"total":1439}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=191701): '2026-05-30 20:00:01.000'  
      HooverPP (entity=request, network=191701): '1780171201'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=191701): '{"endpoint\_id":992,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=191701): '{"num\_keys":8,"dx\_alias\_growth\_ratio":2752.0,"bg\_alias\_growth\_ratio":2768.0,"num\_dx\_enriched\_keys":2666,"num\_dx\_enriched\_alias\_ids":240}'  
      HooverPP (entity=request, network=191701): '{"bg\_alias\_growth\_ratio":2768.0}'

```
  END OF REPORT
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=48.68s | rows=3  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=677.38s | rows=4  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=70.72s | rows=4  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=request, network=384777)  
  Source B : HooverPP (entity=request, network=384777)  
  Rows  A  : 4  
  Rows  B  : 4  
  Columns A: 231  
  Columns B: 231

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 4

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (231 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/4 (0.00%)
  Column match %    : 226/231 (97.84%)
  Cell/value match %: 906/924 (98.05%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
request__client_facing_ivt_reason_flag                       4 row(s)
request__context__profile_concrete_event_id                  4 row(s)
request__context__standard_content_viewership_profile_ids    4 row(s)
request__context__standard_genre_ids                         4 row(s)
request__context__standard_iab_category_ids                  4 row(s)
request__context__standard_language_ids                      4 row(s)
request__context__standard_sport_entity_ids                  4 row(s)
request__decision_info__external_bridge                      4 row(s)
request__decision_info__external_bridge__slot_index          4 row(s)
request__decision_info__external_bridge__status              4 row(s)
request__decision_info__inventory_protections                4 row(s)
request__decision_info__inventory_protections__level         4 row(s)
request__decision_info__inventory_protections__scope         4 row(s)
request__decision_info__inventory_protections__separation    4 row(s)
request__guaranteed_deal_avail                               4 row(s)
request__guaranteed_deal_avail__buyer_id                     4 row(s)
request__guaranteed_deal_avail__internal_deal_id             4 row(s)
request__mrc_compliance_label                                4 row(s)
request__yield_optimization_ids                              4 row(s)
request__yield_optimization_ids__demand_id                   4 row(s)
request__yield_optimization_ids__demand_type                 4 row(s)
request__yield_optimization_ids__optimization_ids            4 row(s)
request__candidates                                          2 row(s)
request__context__video_cro_selected_yield_optimization_infos 2 row(s)
request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids 2 row(s)
request__context__video_cro_selected_yield_optimization_infos__sub_yo_id 2 row(s)
request__scores                                              2 row(s)
request__scores__flag                                        2 row(s)
request__scores__network_id                                  2 row(s)
request__scores__score                                       2 row(s)
request__soft_guaranteed_ad                                  2 row(s)
request__soft_guaranteed_ad__ad_id                           2 row(s)
request__soft_guaranteed_ad__entity_id                       2 row(s)
request__soft_guaranteed_ad__entity_type                     2 row(s)
request__soft_guaranteed_ad__network_id                      2 row(s)
request__soft_guaranteed_ad__num_competing_ads               2 row(s)
```

  ❌ 4 row(s) have differences:

  Column diff summary (sorted by frequency):  
    request\_\_context                                             4 row(s)  
    request\_\_decision\_info                                       4 row(s)  
    request\_\_timestamp                                           4 row(s)  
    request\_\_userdb\_audience\_user\_info                           4 row(s)  
    request\_\_scores                                              2 row(s)

  Detailed diffs:

  \[row=2\]  
    request\_\_context:  
      Hoover (entity=request, network=384777): '{"network\_id":384777,"asset\_id":1388837484,"site\_section\_id":9437036,"request\_duration":2.147483647E9,"time\_position":0.0,"profile\_id":6456,"request\_format":3,"response\_format":18,"ab\_test\_item":\[{"collection\_id":1102,"bucket\_id":1103},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"tv\_network\_id":63,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","station\_id":"5608086763860174117","stream\_id":"8348966700753924163","host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","request\_trace\_id":"d03016a4a733d68dcd383795aab8facb","source\_id":"18292","linear\_break\_source":4,"rbp\_platform":"VOD","stream\_mode\_id":4,"standard\_brand\_id":96,"content\_form\_id":3,"content\_rating\_id":6,"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":18,"standard\_endpoint\_id":1046,"p2\_handler\_source":"ip-10-204-87-184.ec2.internal","website\_root\_id":765030,"po\_type":"DISTRIBUTOR","transcode\_package\_id":383,"stream\_mode\_ids":\[1,4\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[1\],"video\_cro\_network\_id":384777,"video\_cro\_context\_id":9437036,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":765030,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":69300}\],"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":765030,"site\_section\_cro\_parsed\_site\_section\_id":9437036,"rbp\_device\_type":"STB VOD","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1388837484,"distributor\_site\_section\_id":9437036,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND","extracted\_key\_value":{"\_fw\_lto":"2026-05-30T15:00:00.634-05:00"},"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\]}'  
      HooverPP (entity=request, network=384777): '{"ab\_test\_item":\[{"bucket\_id":1103,"collection\_id":1102},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"com.xfinity.livelinear"},"asset\_id":1388837484,"content\_form\_id":3,"content\_rating\_id":6,"distributor\_network\_id":384777,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":9437036,"distributor\_video\_asset\_id":-1,"host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_vs","value":"49517656-56fd-4a9c-aa3d-e55e4e6c60c9"},{"key":"\_fw\_lto","value":"2026-05-30T15:00:00.634-05:00"},{"key":"\_fw\_session\_id","value":"49517656-56fd-4a9c-aa3d-e55e4e6c60c9"},{"key":"\_fw\_po\_type","value":"distributor"},{"key":"\_fwu:390191:\_fw\_hhid","value":"44d7c3f60f14dadd58322ca559b933ae"},{"key":"\_fw\_goverride\_zipcode","value":"77469"}\],"linear\_break\_source":4,"network\_id":384777,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","po\_type":"DISTRIBUTOR","profile\_id":6456,"profile\_type":"COMPOUND","rbp\_device\_type":"STB VOD","rbp\_platform":"VOD","request\_duration":2.147483647E9,"request\_format":3,"response\_format":18,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_site\_id":765030,"site\_section\_id":9437036,"source\_id":"18292","standard\_addressability\_ids":\[1\],"standard\_brand\_id":96,"standard\_endpoint\_id":1046,"standard\_endpoint\_owner\_id":18,"standard\_privacy\_id":1,"standard\_programmer\_id":88,"station\_id":"5608086763860174117","stream\_id":"8348966700753924163","stream\_mode\_id":4,"stream\_mode\_ids":\[1,4\],"time\_position":0.0,"transcode\_package\_id":383,"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\],"tv\_network\_id":63,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":9437036,"video\_cro\_network\_id":384777,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":69300}\],"video\_cro\_site\_id":765030}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"value1":65792,"value2":0,"flag3":40,"value3":0,"value4":2199023321088,"value5":0,"value6":66048,"value7":16777216,"flag4":12619776,"decision\_log":":::::::geoinfo#pcm#0#0#4231#618#0#0","value9":197,"value10":197,"value11":1,"value12":0,"value13":2,"value15":0}'  
      HooverPP (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"flag3":40,"flag4":12619776,"value1":65792,"value10":197,"value11":1,"value12":0,"value13":2,"value15":0,"value2":0,"value3":0,"value4":2199023321088,"value5":0,"value6":66048,"value7":16777216,"value9":197}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=384777): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=384777): '1780171200'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=384777): '{"num\_keys":1,"dx\_alias\_growth\_ratio":197.0,"bg\_alias\_growth\_ratio":418.0,"num\_dx\_enriched\_keys":197,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=384777): '{"bg\_alias\_growth\_ratio":418.0}'

  \[row=3\]  
    request\_\_context:  
      Hoover (entity=request, network=384777): '{"network\_id":384777,"asset\_id":1388837484,"site\_section\_id":9437036,"request\_duration":2.147483647E9,"time\_position":0.0,"profile\_id":6456,"request\_format":3,"response\_format":18,"ab\_test\_item":\[{"collection\_id":1102,"bucket\_id":1103},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"tv\_network\_id":63,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","station\_id":"5608086763860174117","stream\_id":"8348966700753924163","host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","request\_trace\_id":"d03016a4a733d68dcd383795aab8facb","source\_id":"18292","linear\_break\_source":4,"rbp\_platform":"VOD","stream\_mode\_id":4,"standard\_brand\_id":96,"content\_form\_id":3,"content\_rating\_id":6,"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":18,"standard\_endpoint\_id":1046,"p2\_handler\_source":"ip-10-204-87-184.ec2.internal","website\_root\_id":765030,"po\_type":"DISTRIBUTOR","transcode\_package\_id":383,"stream\_mode\_ids":\[1,4\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[1\],"video\_cro\_network\_id":384777,"video\_cro\_context\_id":9437036,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":765030,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":69300}\],"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":765030,"site\_section\_cro\_parsed\_site\_section\_id":9437036,"rbp\_device\_type":"STB VOD","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1388837484,"distributor\_site\_section\_id":9437036,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND","extracted\_key\_value":{"\_fw\_lto":"2026-05-30T15:00:00.634-05:00"},"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\]}'  
      HooverPP (entity=request, network=384777): '{"ab\_test\_item":\[{"bucket\_id":1103,"collection\_id":1102},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"com.xfinity.livelinear"},"asset\_id":1388837484,"content\_form\_id":3,"content\_rating\_id":6,"distributor\_network\_id":384777,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":9437036,"distributor\_video\_asset\_id":-1,"host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_vs","value":"49517656-56fd-4a9c-aa3d-e55e4e6c60c9"},{"key":"\_fw\_lto","value":"2026-05-30T15:00:00.634-05:00"},{"key":"\_fw\_session\_id","value":"49517656-56fd-4a9c-aa3d-e55e4e6c60c9"},{"key":"\_fw\_po\_type","value":"distributor"},{"key":"\_fwu:390191:\_fw\_hhid","value":"44d7c3f60f14dadd58322ca559b933ae"},{"key":"\_fw\_goverride\_zipcode","value":"77469"}\],"linear\_break\_source":4,"network\_id":384777,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","po\_type":"DISTRIBUTOR","profile\_id":6456,"profile\_type":"COMPOUND","rbp\_device\_type":"STB VOD","rbp\_platform":"VOD","request\_duration":2.147483647E9,"request\_format":3,"response\_format":18,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_site\_id":765030,"site\_section\_id":9437036,"source\_id":"18292","standard\_addressability\_ids":\[1\],"standard\_brand\_id":96,"standard\_endpoint\_id":1046,"standard\_endpoint\_owner\_id":18,"standard\_privacy\_id":1,"standard\_programmer\_id":88,"station\_id":"5608086763860174117","stream\_id":"8348966700753924163","stream\_mode\_id":4,"stream\_mode\_ids":\[1,4\],"time\_position":0.0,"transcode\_package\_id":383,"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\],"tv\_network\_id":63,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":9437036,"video\_cro\_network\_id":384777,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":69300}\],"video\_cro\_site\_id":765030}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"value1":65792,"value2":0,"flag3":40,"value3":0,"value4":2199023321088,"value5":0,"value6":66048,"value7":16777216,"flag4":12619776,"decision\_log":":::::::geoinfo#pcm#0#0#4231#618#0#0","value9":197,"value10":197,"value11":1,"value12":0,"value13":2,"value15":0}'  
      HooverPP (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"flag3":40,"flag4":12619776,"value1":65792,"value10":197,"value11":1,"value12":0,"value13":2,"value15":0,"value2":0,"value3":0,"value4":2199023321088,"value5":0,"value6":66048,"value7":16777216,"value9":197}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=384777): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=384777): '1780171200'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=384777): '{"num\_keys":1,"dx\_alias\_growth\_ratio":197.0,"bg\_alias\_growth\_ratio":418.0,"num\_dx\_enriched\_keys":197,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=384777): '{"bg\_alias\_growth\_ratio":418.0}'

  \[row=4\]  
    request\_\_context:  
      Hoover (entity=request, network=384777): '{"network\_id":384777,"asset\_id":1388837484,"site\_section\_id":9437036,"request\_duration":2.147483647E9,"time\_position":0.0,"profile\_id":6456,"request\_format":3,"response\_format":18,"ab\_test\_item":\[{"collection\_id":140,"bucket\_id":431},{"collection\_id":1102,"bucket\_id":1103},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"tv\_network\_id":63,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","station\_id":"5608086763860174117","stream\_id":"8348966700753924163","host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","request\_trace\_id":"a888a8e9621c1428c72d95030f61a961","source\_id":"18292","linear\_break\_source":4,"rbp\_platform":"VOD","stream\_mode\_id":4,"standard\_brand\_id":96,"content\_form\_id":3,"content\_rating\_id":6,"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":18,"standard\_endpoint\_id":1046,"p2\_handler\_source":"ip-10-204-87-184.ec2.internal","website\_root\_id":765030,"po\_type":"DISTRIBUTOR","transcode\_package\_id":383,"stream\_mode\_ids":\[1,4\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[1\],"video\_cro\_network\_id":384777,"video\_cro\_context\_id":9437036,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":765030,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":50041},{"sub\_yo\_id":65878}\],"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":65878},{"sub\_yo\_id":69300}\],"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":765030,"site\_section\_cro\_parsed\_site\_section\_id":9437036,"rbp\_device\_type":"STB VOD","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1388837484,"distributor\_site\_section\_id":9437036,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND","extracted\_key\_value":{"\_fw\_lto":"2026-05-30T16:00:00.722-04:00"},"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\]}'  
      HooverPP (entity=request, network=384777): '{"ab\_test\_item":\[{"bucket\_id":431,"collection\_id":140},{"bucket\_id":1103,"collection\_id":1102},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"com.xfinity.livelinear"},"asset\_id":1388837484,"content\_form\_id":3,"content\_rating\_id":6,"distributor\_network\_id":384777,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":9437036,"distributor\_video\_asset\_id":-1,"host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_vs","value":"acae052a-f210-4202-9243-e535d670471f"},{"key":"\_fw\_lto","value":"2026-05-30T16:00:00.722-04:00"},{"key":"\_fw\_session\_id","value":"acae052a-f210-4202-9243-e535d670471f"},{"key":"\_fw\_po\_type","value":"distributor"},{"key":"\_fwu:390191:\_fw\_hhid","value":"dd44c9d9e8f9bf3d483740b3e6a677c4"},{"key":"\_fw\_goverride\_zipcode","value":"33442"}\],"linear\_break\_source":4,"network\_id":384777,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","po\_type":"DISTRIBUTOR","profile\_id":6456,"profile\_type":"COMPOUND","rbp\_device\_type":"STB VOD","rbp\_platform":"VOD","request\_duration":2.147483647E9,"request\_format":3,"response\_format":18,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_site\_id":765030,"site\_section\_id":9437036,"source\_id":"18292","standard\_addressability\_ids":\[1\],"standard\_brand\_id":96,"standard\_endpoint\_id":1046,"standard\_endpoint\_owner\_id":18,"standard\_privacy\_id":1,"standard\_programmer\_id":88,"station\_id":"5608086763860174117","stream\_id":"8348966700753924163","stream\_mode\_id":4,"stream\_mode\_ids":\[1,4\],"time\_position":0.0,"transcode\_package\_id":383,"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\],"tv\_network\_id":63,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":9437036,"video\_cro\_network\_id":384777,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":65878},{"sub\_yo\_id":69300}\],"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":50041},{"sub\_yo\_id":65878}\],"video\_cro\_site\_id":765030}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"value1":65793,"value2":393229,"flag3":32,"value3":21475164173,"value4":2203318618112,"value5":4398046511104,"value6":111669281280,"value7":16777216,"flag4":12619776,"decision\_log":":::::::geoinfo#pcm#0#0#4622#528#0#0","value9":167,"value10":167,"value11":2,"value12":5,"value13":2,"value15":0}'  
      HooverPP (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"flag3":32,"flag4":12619776,"value1":65793,"value10":167,"value11":2,"value12":5,"value13":2,"value15":0,"value2":393229,"value3":21475164173,"value4":2203318618112,"value5":4398046511104,"value6":111669281280,"value7":16777216,"value9":167}'  
    request\_\_scores:  
      Hoover (entity=request, network=384777): '\[\\'{"network\_id":384777,"ad\_id":93966487,"flag":514,"score":2334}\\'\]'  
      HooverPP (entity=request, network=384777): '\[\\'{"flag":514,"network\_id":384777,"score":2334}\\'\]'  
    request\_\_timestamp:  
      Hoover (entity=request, network=384777): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=384777): '1780171200'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=384777): '{"num\_keys":1,"dx\_alias\_growth\_ratio":167.0,"bg\_alias\_growth\_ratio":395.0,"num\_dx\_enriched\_keys":167,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=384777): '{"bg\_alias\_growth\_ratio":395.0}'

  \[row=5\]  
    request\_\_context:  
      Hoover (entity=request, network=384777): '{"network\_id":384777,"asset\_id":1388837484,"site\_section\_id":9437036,"request\_duration":2.147483647E9,"time\_position":0.0,"profile\_id":6456,"request\_format":3,"response\_format":18,"ab\_test\_item":\[{"collection\_id":140,"bucket\_id":431},{"collection\_id":1102,"bucket\_id":1103},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"tv\_network\_id":63,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","station\_id":"5608086763860174117","stream\_id":"8348966700753924163","host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","request\_trace\_id":"a888a8e9621c1428c72d95030f61a961","source\_id":"18292","linear\_break\_source":4,"rbp\_platform":"VOD","stream\_mode\_id":4,"standard\_brand\_id":96,"content\_form\_id":3,"content\_rating\_id":6,"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":18,"standard\_endpoint\_id":1046,"p2\_handler\_source":"ip-10-204-87-184.ec2.internal","website\_root\_id":765030,"po\_type":"DISTRIBUTOR","transcode\_package\_id":383,"stream\_mode\_ids":\[1,4\],"standard\_privacy\_id":1,"standard\_addressability\_ids":\[1\],"video\_cro\_network\_id":384777,"video\_cro\_context\_id":9437036,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":765030,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":50041},{"sub\_yo\_id":65878}\],"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":65878},{"sub\_yo\_id":69300}\],"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":765030,"site\_section\_cro\_parsed\_site\_section\_id":9437036,"rbp\_device\_type":"STB VOD","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1388837484,"distributor\_site\_section\_id":9437036,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND","extracted\_key\_value":{"\_fw\_lto":"2026-05-30T16:00:00.722-04:00"},"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\]}'  
      HooverPP (entity=request, network=384777): '{"ab\_test\_item":\[{"bucket\_id":431,"collection\_id":140},{"bucket\_id":1103,"collection\_id":1102},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"com.xfinity.livelinear"},"asset\_id":1388837484,"content\_form\_id":3,"content\_rating\_id":6,"distributor\_network\_id":384777,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":9437036,"distributor\_video\_asset\_id":-1,"host\_name":"[5df09-linear.v.fwmrm.net](http://5df09-linear.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_vs","value":"acae052a-f210-4202-9243-e535d670471f"},{"key":"\_fw\_lto","value":"2026-05-30T16:00:00.722-04:00"},{"key":"\_fw\_session\_id","value":"acae052a-f210-4202-9243-e535d670471f"},{"key":"\_fw\_po\_type","value":"distributor"},{"key":"\_fwu:390191:\_fw\_hhid","value":"dd44c9d9e8f9bf3d483740b3e6a677c4"},{"key":"\_fw\_goverride\_zipcode","value":"33442"}\],"linear\_break\_source":4,"network\_id":384777,"out\_signal\_id":"O87dKgB89loxcLQYQt1E-wAA","po\_type":"DISTRIBUTOR","profile\_id":6456,"profile\_type":"COMPOUND","rbp\_device\_type":"STB VOD","rbp\_platform":"VOD","request\_duration":2.147483647E9,"request\_format":3,"response\_format":18,"site\_section\_cro\_asset\_id":9437036,"site\_section\_cro\_network\_id":384777,"site\_section\_cro\_site\_id":765030,"site\_section\_id":9437036,"source\_id":"18292","standard\_addressability\_ids":\[1\],"standard\_brand\_id":96,"standard\_endpoint\_id":1046,"standard\_endpoint\_owner\_id":18,"standard\_privacy\_id":1,"standard\_programmer\_id":88,"station\_id":"5608086763860174117","stream\_id":"8348966700753924163","stream\_mode\_id":4,"stream\_mode\_ids":\[1,4\],"time\_position":0.0,"transcode\_package\_id":383,"tv\_network\_group\_ids":\[176,177,182,187,188,212,214,217,219,220,226,228,229,234,241,246,247,249,250,254,255,256,259,262,267,270,274,276,281,283,285,286,305,307,309,310,314,317,320,322,323,326,336,337,343,346,351,352,353,355,357,359,361,362,366,370,372,427,523,564,567,569,570,619,620,622,644,645,652,664,740,741,742,758,759,760,761,775,776,783,784,785,786,842,853,1049\],"tv\_network\_id":63,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":9437036,"video\_cro\_network\_id":384777,"video\_cro\_pre\_targeting\_yield\_optimization\_infos":\[{"sub\_yo\_id":50812},{"sub\_yo\_id":65878},{"sub\_yo\_id":69300}\],"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":50041},{"sub\_yo\_id":65878}\],"video\_cro\_site\_id":765030}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"value1":65793,"value2":393229,"flag3":32,"value3":21475164173,"value4":2203318618112,"value5":4398046511104,"value6":111669281280,"value7":16777216,"flag4":12619776,"decision\_log":":::::::geoinfo#pcm#0#0#4622#528#0#0","value9":167,"value10":167,"value11":2,"value12":5,"value13":2,"value15":0}'  
      HooverPP (entity=request, network=384777): '{"flag1":1220542464,"flag2":1099956224,"flag3":32,"flag4":12619776,"value1":65793,"value10":167,"value11":2,"value12":5,"value13":2,"value15":0,"value2":393229,"value3":21475164173,"value4":2203318618112,"value5":4398046511104,"value6":111669281280,"value7":16777216,"value9":167}'  
    request\_\_scores:  
      Hoover (entity=request, network=384777): '\[\\'{"network\_id":384777,"ad\_id":93966487,"flag":514,"score":2334}\\'\]'  
      HooverPP (entity=request, network=384777): '\[\\'{"flag":514,"network\_id":384777,"score":2334}\\'\]'  
    request\_\_timestamp:  
      Hoover (entity=request, network=384777): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=384777): '1780171200'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=384777): '{"num\_keys":1,"dx\_alias\_growth\_ratio":167.0,"bg\_alias\_growth\_ratio":395.0,"num\_dx\_enriched\_keys":167,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=384777): '{"bg\_alias\_growth\_ratio":395.0}'

```
  END OF REPORT
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=50.16s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=936.39s | rows=6  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=69.92s | rows=6  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=request, network=512166)  
  Source B : HooverPP (entity=request, network=512166)  
  Rows  A  : 6  
  Rows  B  : 6  
  Columns A: 231  
  Columns B: 231

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 6

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (231 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/6 (0.00%)
  Column match %    : 222/231 (96.10%)
  Cell/value match %: 1,340/1,386 (96.68%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
request__candidates                                          6 row(s)
request__client_facing_ivt_reason_flag                       6 row(s)
request__context__profile_concrete_event_id                  6 row(s)
request__context__standard_content_viewership_profile_ids    6 row(s)
request__context__standard_sport_entity_ids                  6 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos 6 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids 6 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id 6 row(s)
request__decision_info__external_bridge                      6 row(s)
request__decision_info__external_bridge__slot_index          6 row(s)
request__decision_info__external_bridge__status              6 row(s)
request__decision_info__inventory_protections                6 row(s)
request__decision_info__inventory_protections__level         6 row(s)
request__decision_info__inventory_protections__scope         6 row(s)
request__decision_info__inventory_protections__separation    6 row(s)
request__guaranteed_deal_avail                               6 row(s)
request__guaranteed_deal_avail__buyer_id                     6 row(s)
request__guaranteed_deal_avail__internal_deal_id             6 row(s)
request__linear_capnedit                                     6 row(s)
request__linear_capnedit__active_state                       6 row(s)
request__linear_capnedit__device_id                          6 row(s)
request__linear_capnedit__is_dvr                             6 row(s)
request__linear_capnedit__last_activity_time                 6 row(s)
request__linear_capnedit__mode                               6 row(s)
request__linear_capnedit__tune_time                          6 row(s)
request__mrc_compliance_label                                6 row(s)
request__scores                                              6 row(s)
request__scores__flag                                        6 row(s)
request__scores__network_id                                  6 row(s)
request__scores__score                                       6 row(s)
request__soft_guaranteed_ad                                  6 row(s)
request__soft_guaranteed_ad__ad_id                           6 row(s)
request__soft_guaranteed_ad__entity_id                       6 row(s)
request__soft_guaranteed_ad__entity_type                     6 row(s)
request__soft_guaranteed_ad__network_id                      6 row(s)
request__soft_guaranteed_ad__num_competing_ads               6 row(s)
request__context__video_cro_selected_yield_optimization_infos 5 row(s)
request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids 5 row(s)
request__context__video_cro_selected_yield_optimization_infos__sub_yo_id 5 row(s)
request__yield_optimization_ids                              5 row(s)
request__yield_optimization_ids__demand_id                   5 row(s)
request__yield_optimization_ids__demand_type                 5 row(s)
request__yield_optimization_ids__optimization_ids            5 row(s)
```

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):  
    request\_\_context                                             6 row(s)  
    request\_\_time\_record                                         6 row(s)  
    request\_\_timestamp                                           6 row(s)  
    request\_\_traffic\_compliance                                  6 row(s)  
    request\_\_userdb\_audience\_user\_info                           6 row(s)  
    request\_\_bid\_request                                         5 row(s)  
    request\_\_bid\_request\_\_impression                             5 row(s)  
    request\_\_request\_throttling\_info                             5 row(s)  
    request\_\_decision\_info                                       1 row(s)

  Detailed diffs:

  \[row=2\]  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":512116,"asset\_id":13501405,"custom\_asset\_id":"512116/0x4D757264657253686557726F74655F4550303030303239393530313836","site\_section\_id":19810070,"page\_random":"1780171200484931212","video\_random":"1780171200484931952","request\_duration":180.0,"time\_position":0.0,"profile\_id":10753,"request\_format":1,"response\_format":13,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":117},{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":56,"bucket\_id":155},{"collection\_id":90,"bucket\_id":298},{"collection\_id":110,"bucket\_id":348},{"collection\_id":136,"bucket\_id":430},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":178,"bucket\_id":509},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1102,"bucket\_id":1104},{"collection\_id":2006,"bucket\_id":2011},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2010,"bucket\_id":2018},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":2017,"bucket\_id":2030},{"collection\_id":3282740,"bucket\_id":3282957},{"collection\_id":3282740,"bucket\_id":3282958},{"collection\_id":3282740,"bucket\_id":3282962},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7d074.v.fwmrm.net](http://7d074.v.fwmrm.net)","request\_trace\_id":"c5f475da9506d99b65c166e1dd37a455","rbp\_platform":"OTT","stream\_mode\_id":1,"standard\_brand\_id":3029,"standard\_genre\_ids":\[2,27\],"content\_form\_id":3,"content\_rating\_id":11,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":88,"standard\_endpoint\_owner\_id":18,"standard\_endpoint\_id":103,"website\_root\_id":1071698,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1350,"post\_selection\_external\_ad\_timeout":1350},"standard\_app\_id":87,"stream\_mode\_ids":\[1\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_app\_bundle\_id":22499,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,6\],"video\_cro\_network\_id":512116,"video\_cro\_context\_id":19810070,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1071698,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":69737}\],"site\_section\_cro\_network\_id":512116,"site\_section\_cro\_asset\_id":19810070,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1071698,"site\_section\_cro\_parsed\_site\_section\_id":19810070,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":13501405,"distributor\_site\_section\_id":19810070,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":117,"collection\_id":42},{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":155,"collection\_id":56},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":348,"collection\_id":110},{"bucket\_id":430,"collection\_id":136},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":509,"collection\_id":178},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1104,"collection\_id":1102},{"bucket\_id":2011,"collection\_id":2006},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2018,"collection\_id":2010},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":2030,"collection\_id":2017},{"bucket\_id":3282957,"collection\_id":3282740},{"bucket\_id":3282958,"collection\_id":3282740},{"bucket\_id":3282962,"collection\_id":3282740},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"com.xfinity.stream","name":"xfinity stream","storeurl":"<https://www.xumo.com/api/apps?bundleid=com.xfinity.stream> "},"asset\_id":13501405,"content\_form\_id":3,"content\_rating\_id":11,"custom\_asset\_id":"512116/0x4D757264657253686557726F74655F4550303030303239393530313836","distributor\_network\_id":512116,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":19810070,"distributor\_video\_asset\_id":-1,"host\_name":"[7d074.v.fwmrm.net](http://7d074.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3p\_uid","value":"UID2:,IDL:"},{"key":"\_fw\_app\_bundle","value":"com.xfinity.stream"},{"key":"\_fw\_app\_name","value":"XfinityStream"},{"key":"\_fw\_app\_store\_url","value":"<https://www.xumo.com/api/apps?bundleid=com.xfinity.stream> "},{"key":"\_fw\_content\_category","value":"IAB1-7"},{"key":"\_fw\_content\_genre","value":"television"},{"key":"\_fw\_content\_id"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_content\_length","value":"0"},{"key":"\_fw\_content\_rating","value":"tv-g"},{"key":"\_fw\_content\_title"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_deviceMake"},{"key":"\_fw\_device\_model"},{"key":"\_fw\_devicetype","value":"3-Connected\_TV"},{"key":"\_fw\_did","value":"b0a29557-4d79-4ddb-8548-a6ba574a04b0"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_key\_words"},{"key":"\_fw\_us\_privacy","value":"1-N-"},{"key":"\_fw\_vcid2","value":"512116:b0a29557-4d79-4ddb-8548-a6ba574a04b0"},{"key":"appName","value":"XfinityStream"},{"key":"channelId","value":"[d14l8r3214nwiw.cloudfront.net/channel/88889198/hls"},{"key":"provider\_asset\_id"},{"key":"ssai","value":"1"},{"key":"xumo\_ProviderID","value":"3927"},{"key":"xumo\_ProviderName","value":"NBCUMurderSheWrote"},{"key":"xumo\_channelId","value":"d14l8r3214nwiw.cloudfront.net/channel/88889198/hls"},{"key":"xumo\_contentID","value":"3927"},{"key":"xumo\_contentname","value":"nbcumurdershewrote"},{"key":"xumo\_ifaType","value":"dpid"},{"key":"\_fw\_am\_fed\_segs","value":"xumo:house,xumo:iso"}\],"network\_id":512116,"page\_random":"1780171200484931212","profile\_id":10753,"profile\_trait":{"post\_selection\_external\_ad\_timeout":1350,"pre\_selection\_external\_ad\_timeout":1350},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":180.0,"request\_format":1,"response\_format":13,"site\_section\_cro\_asset\_id":19810070,"site\_section\_cro\_network\_id":512116,"site\_section\_cro\_site\_id":1071698,"site\_section\_id":19810070,"standard\_addressability\_ids":\[4,6\],"standard\_app\_bundle\_id":22499,"standard\_app\_id":87,"standard\_brand\_id":3029,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":103,"standard\_endpoint\_owner\_id":18,"standard\_genre\_ids":\[2,27\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":88,"stream\_mode\_id":1,"stream\_mode\_ids":\[1\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":19810070,"video\_cro\_network\_id":512116,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":69737}\],"video\_cro\_site\_id":1071698,"video\_random":"1780171200484931952](http://d14l8r3214nwiw.cloudfront.net/channel/88889198/hls%22%7D,%7B%22key%22:%22provider_asset_id%22%7D,%7B%22key%22:%22ssai%22,%22value%22:%221%22%7D,%7B%22key%22:%22xumo_ProviderID%22,%22value%22:%223927%22%7D,%7B%22key%22:%22xumo_ProviderName%22,%22value%22:%22NBCUMurderSheWrote%22%7D,%7B%22key%22:%22xumo_channelId%22,%22value%22:%22d14l8r3214nwiw.cloudfront.net/channel/88889198/hls%22%7D,%7B%22key%22:%22xumo_contentID%22,%22value%22:%223927%22%7D,%7B%22key%22:%22xumo_contentname%22,%22value%22:%22nbcumurdershewrote%22%7D,%7B%22key%22:%22xumo_ifaType%22,%22value%22:%22dpid%22%7D,%7B%22key%22:%22_fw_am_fed_segs%22,%22value%22:%22xumo:house,xumo:iso%22%7D%5D,%22network_id%22:512116,%22page_random%22:%221780171200484931212%22,%22profile_id%22:10753,%22profile_trait%22:%7B%22post_selection_external_ad_timeout%22:1350,%22pre_selection_external_ad_timeout%22:1350%7D,%22profile_type%22:%22COMPOUND%22,%22rbp_device_type%22:%22OTT%22,%22rbp_platform%22:%22OTT%22,%22request_duration%22:180.0,%22request_format%22:1,%22response_format%22:13,%22site_section_cro_asset_id%22:19810070,%22site_section_cro_network_id%22:512116,%22site_section_cro_site_id%22:1071698,%22site_section_id%22:19810070,%22standard_addressability_ids%22:%5B4,6%5D,%22standard_app_bundle_id%22:22499,%22standard_app_id%22:87,%22standard_brand_id%22:3029,%22standard_content_territory_id%22:165,%22standard_endpoint_id%22:103,%22standard_endpoint_owner_id%22:18,%22standard_genre_ids%22:%5B2,27%5D,%22standard_iab_category_ids%22:%5B1,8%5D,%22standard_language_ids%22:%5B1%5D,%22standard_privacy_id%22:1,%22standard_programmer_id%22:88,%22stream_mode_id%22:1,%22stream_mode_ids%22:%5B1%5D,%22time_position%22:0.0,%22video_cro_asset_id%22:-1,%22video_cro_context_id%22:19810070,%22video_cro_network_id%22:512116,%22video_cro_selected_yield_optimization_infos%22:%5B%7B%22sub_yo_id%22:69737%7D%5D,%22video_cro_site_id%22:1071698,%22video_random%22:%221780171200484931952)"}'  
    request\_\_decision\_info:  
      Hoover (entity=request, network=512166): '{"flag1":1077936128,"flag2":17825792,"value1":1966081,"value2":8,"flag3":671121458,"value3":4598927950,"value4":1099511634176,"value5":12884967424,"value6":1095219677440,"value7":83886082,"flag4":12619776,"decision\_log":":::::::geoinfo#ip#0#0#0#0#6494#770","value9":643,"value10":485,"value11":47,"value12":159,"value14":1,"value15":0}'  
      HooverPP (entity=request, network=512166): '{"flag1":1077936128,"flag2":17825792,"flag3":671121458,"flag4":12619776,"value1":1966081,"value10":485,"value11":47,"value12":159,"value14":1,"value15":0,"value2":8,"value3":4598927950,"value4":1099511634176,"value5":12884967424,"value6":1095219677440,"value7":83886082,"value9":643}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":974,"external\_candidate":800}'  
      HooverPP (entity=request, network=512166): '{"total":974}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":1215.0,"bg\_alias\_growth\_ratio":1378.0,"num\_dx\_enriched\_keys":561,"num\_dx\_enriched\_alias\_ids":249}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":1378.0}'

  \[row=3\]  
    request\_\_bid\_request:  
      Hoover (entity=request, network=512166): '{"publisher\_id":"535258","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_bundle":"B076X8FKXP","impression":\[{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"}\]}'  
      HooverPP (entity=request, network=512166): '{"app\_bundle":"B076X8FKXP","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_storeurl":"<https://www.amazon.com/dp/B076X8FKXP> ","channel\_name":"Fawesome - Free Awesome TV & Movies","domain":"<http://fawesome.tv> ","impression":\[{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false}\],"publisher\_id":"535258"}'  
    request\_\_bid\_request\_\_impression:  
      Hoover (entity=request, network=512166): '\[\\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\'\]'  
      HooverPP (entity=request, network=512166): '\[\\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\'\]'  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":535258,"asset\_id":1309893687,"site\_section\_id":23382577,"asset\_duration":7028.0,"request\_duration":7028.0,"time\_position":0.0,"profile\_id":16676,"request\_format":7,"response\_format":19,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":98,"bucket\_id":484},{"collection\_id":140,"bucket\_id":431},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1101,"bucket\_id":1102},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","request\_trace\_id":"10aea168a04b08f77b20418d63fbf07a","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"content\_form\_id":3,"content\_rating\_id":12,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":28,"website\_root\_id":1251191,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1750,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4712,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,6\],"standard\_app\_bundle\_id":8626,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[20,30\],"video\_cro\_network\_id":535258,"video\_cro\_context\_id":23382577,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1251191,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1251191,"site\_section\_cro\_parsed\_site\_section\_id":23382577,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1309893687,"distributor\_site\_section\_id":23382577,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":484,"collection\_id":98},{"bucket\_id":431,"collection\_id":140},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1102,"collection\_id":1101},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"asset\_duration":7028.0,"asset\_id":1309893687,"content\_form\_id":3,"content\_rating\_id":12,"distributor\_network\_id":535258,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23382577,"distributor\_video\_asset\_id":-1,"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_content\_genre","value":"Crime,Drama,Musical,Tennis,Thriller,War"},{"key":"\_fw\_did\_google\_advertising\_id","value":"89a66413-5fb5-4f94-b628-2d0a70031f26"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_us\_privacy","value":"1YNN"}\],"network\_id":535258,"profile\_id":16676,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1750},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":7028.0,"request\_format":7,"response\_format":19,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_site\_id":1251191,"site\_section\_id":23382577,"standard\_addressability\_ids":\[20,30\],"standard\_app\_bundle\_id":8626,"standard\_app\_id":4712,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"standard\_iab\_category\_ids":\[1,6\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":28,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":23382577,"video\_cro\_network\_id":535258,"video\_cro\_site\_id":1251191}'  
    request\_\_request\_throttling\_info:  
      Hoover (entity=request, network=512166): '{"flags":2,"model\_info":\[{"model\_id":67,"model\_flags":2},{"model\_id":66,"model\_flags":0}\]}'  
      HooverPP (entity=request, network=512166): '{"flags":2}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":346,"external\_candidate":307}'  
      HooverPP (entity=request, network=512166): '{"total":346}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":651.0,"bg\_alias\_growth\_ratio":651.0,"num\_dx\_enriched\_keys":651,"num\_dx\_enriched\_alias\_ids":651}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":651.0}'

  \[row=4\]  
    request\_\_bid\_request:  
      Hoover (entity=request, network=512166): '{"publisher\_id":"535258","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_bundle":"B076X8FKXP","impression":\[{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"}\]}'  
      HooverPP (entity=request, network=512166): '{"app\_bundle":"B076X8FKXP","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_storeurl":"<https://www.amazon.com/dp/B076X8FKXP> ","channel\_name":"Fawesome - Free Awesome TV & Movies","domain":"<http://fawesome.tv> ","impression":\[{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false}\],"publisher\_id":"535258"}'  
    request\_\_bid\_request\_\_impression:  
      Hoover (entity=request, network=512166): '\[\\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\'\]'  
      HooverPP (entity=request, network=512166): '\[\\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\'\]'  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":535258,"asset\_id":1309893687,"site\_section\_id":23382577,"asset\_duration":7028.0,"request\_duration":7028.0,"time\_position":0.0,"profile\_id":16676,"request\_format":7,"response\_format":19,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":98,"bucket\_id":484},{"collection\_id":140,"bucket\_id":431},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1101,"bucket\_id":1102},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","request\_trace\_id":"10aea168a04b08f77b20418d63fbf07a","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"content\_form\_id":3,"content\_rating\_id":12,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":28,"website\_root\_id":1251191,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1750,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4712,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,6\],"standard\_app\_bundle\_id":8626,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[20,30\],"video\_cro\_network\_id":535258,"video\_cro\_context\_id":23382577,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1251191,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1251191,"site\_section\_cro\_parsed\_site\_section\_id":23382577,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1309893687,"distributor\_site\_section\_id":23382577,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":484,"collection\_id":98},{"bucket\_id":431,"collection\_id":140},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1102,"collection\_id":1101},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"asset\_duration":7028.0,"asset\_id":1309893687,"content\_form\_id":3,"content\_rating\_id":12,"distributor\_network\_id":535258,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23382577,"distributor\_video\_asset\_id":-1,"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_content\_genre","value":"Crime,Drama,Musical,Tennis,Thriller,War"},{"key":"\_fw\_did\_google\_advertising\_id","value":"89a66413-5fb5-4f94-b628-2d0a70031f26"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_us\_privacy","value":"1YNN"}\],"network\_id":535258,"profile\_id":16676,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1750},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":7028.0,"request\_format":7,"response\_format":19,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_site\_id":1251191,"site\_section\_id":23382577,"standard\_addressability\_ids":\[20,30\],"standard\_app\_bundle\_id":8626,"standard\_app\_id":4712,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"standard\_iab\_category\_ids":\[1,6\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":28,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":23382577,"video\_cro\_network\_id":535258,"video\_cro\_site\_id":1251191}'  
    request\_\_request\_throttling\_info:  
      Hoover (entity=request, network=512166): '{"flags":2,"model\_info":\[{"model\_id":67,"model\_flags":2},{"model\_id":66,"model\_flags":0}\]}'  
      HooverPP (entity=request, network=512166): '{"flags":2}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":346,"external\_candidate":307}'  
      HooverPP (entity=request, network=512166): '{"total":346}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":651.0,"bg\_alias\_growth\_ratio":651.0,"num\_dx\_enriched\_keys":651,"num\_dx\_enriched\_alias\_ids":651}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":651.0}'

  \[row=5\]  
    request\_\_bid\_request:  
      Hoover (entity=request, network=512166): '{"publisher\_id":"535258","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_bundle":"B076X8FKXP","impression":\[{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"}\]}'  
      HooverPP (entity=request, network=512166): '{"app\_bundle":"B076X8FKXP","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_storeurl":"<https://www.amazon.com/dp/B076X8FKXP> ","channel\_name":"Fawesome - Free Awesome TV & Movies","domain":"<http://fawesome.tv> ","impression":\[{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false}\],"publisher\_id":"535258"}'  
    request\_\_bid\_request\_\_impression:  
      Hoover (entity=request, network=512166): '\[\\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\'\]'  
      HooverPP (entity=request, network=512166): '\[\\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\'\]'  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":535258,"asset\_id":1309893687,"site\_section\_id":23382577,"asset\_duration":7028.0,"request\_duration":7028.0,"time\_position":0.0,"profile\_id":16676,"request\_format":7,"response\_format":19,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":98,"bucket\_id":484},{"collection\_id":140,"bucket\_id":431},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1101,"bucket\_id":1102},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","request\_trace\_id":"10aea168a04b08f77b20418d63fbf07a","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"content\_form\_id":3,"content\_rating\_id":12,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":28,"website\_root\_id":1251191,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1750,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4712,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,6\],"standard\_app\_bundle\_id":8626,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[20,30\],"video\_cro\_network\_id":535258,"video\_cro\_context\_id":23382577,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1251191,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1251191,"site\_section\_cro\_parsed\_site\_section\_id":23382577,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1309893687,"distributor\_site\_section\_id":23382577,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":484,"collection\_id":98},{"bucket\_id":431,"collection\_id":140},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1102,"collection\_id":1101},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"asset\_duration":7028.0,"asset\_id":1309893687,"content\_form\_id":3,"content\_rating\_id":12,"distributor\_network\_id":535258,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23382577,"distributor\_video\_asset\_id":-1,"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_content\_genre","value":"Crime,Drama,Musical,Tennis,Thriller,War"},{"key":"\_fw\_did\_google\_advertising\_id","value":"89a66413-5fb5-4f94-b628-2d0a70031f26"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_us\_privacy","value":"1YNN"}\],"network\_id":535258,"profile\_id":16676,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1750},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":7028.0,"request\_format":7,"response\_format":19,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_site\_id":1251191,"site\_section\_id":23382577,"standard\_addressability\_ids":\[20,30\],"standard\_app\_bundle\_id":8626,"standard\_app\_id":4712,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"standard\_iab\_category\_ids":\[1,6\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":28,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":23382577,"video\_cro\_network\_id":535258,"video\_cro\_site\_id":1251191}'  
    request\_\_request\_throttling\_info:  
      Hoover (entity=request, network=512166): '{"flags":2,"model\_info":\[{"model\_id":67,"model\_flags":2},{"model\_id":66,"model\_flags":0}\]}'  
      HooverPP (entity=request, network=512166): '{"flags":2}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":346,"external\_candidate":307}'  
      HooverPP (entity=request, network=512166): '{"total":346}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":651.0,"bg\_alias\_growth\_ratio":651.0,"num\_dx\_enriched\_keys":651,"num\_dx\_enriched\_alias\_ids":651}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":651.0}'

  \[row=6\]  
    request\_\_bid\_request:  
      Hoover (entity=request, network=512166): '{"publisher\_id":"535258","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_bundle":"B076X8FKXP","impression":\[{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"}\]}'  
      HooverPP (entity=request, network=512166): '{"app\_bundle":"B076X8FKXP","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_storeurl":"<https://www.amazon.com/dp/B076X8FKXP> ","channel\_name":"Fawesome - Free Awesome TV & Movies","domain":"<http://fawesome.tv> ","impression":\[{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false}\],"publisher\_id":"535258"}'  
    request\_\_bid\_request\_\_impression:  
      Hoover (entity=request, network=512166): '\[\\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\'\]'  
      HooverPP (entity=request, network=512166): '\[\\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\'\]'  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":535258,"asset\_id":1309893687,"site\_section\_id":23382577,"asset\_duration":7028.0,"request\_duration":7028.0,"time\_position":0.0,"profile\_id":16676,"request\_format":7,"response\_format":19,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":98,"bucket\_id":484},{"collection\_id":140,"bucket\_id":431},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1101,"bucket\_id":1102},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","request\_trace\_id":"10aea168a04b08f77b20418d63fbf07a","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"content\_form\_id":3,"content\_rating\_id":12,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":28,"website\_root\_id":1251191,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1750,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4712,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,6\],"standard\_app\_bundle\_id":8626,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[20,30\],"video\_cro\_network\_id":535258,"video\_cro\_context\_id":23382577,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1251191,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1251191,"site\_section\_cro\_parsed\_site\_section\_id":23382577,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1309893687,"distributor\_site\_section\_id":23382577,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":484,"collection\_id":98},{"bucket\_id":431,"collection\_id":140},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1102,"collection\_id":1101},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"asset\_duration":7028.0,"asset\_id":1309893687,"content\_form\_id":3,"content\_rating\_id":12,"distributor\_network\_id":535258,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23382577,"distributor\_video\_asset\_id":-1,"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_content\_genre","value":"Crime,Drama,Musical,Tennis,Thriller,War"},{"key":"\_fw\_did\_google\_advertising\_id","value":"89a66413-5fb5-4f94-b628-2d0a70031f26"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_us\_privacy","value":"1YNN"}\],"network\_id":535258,"profile\_id":16676,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1750},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":7028.0,"request\_format":7,"response\_format":19,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_site\_id":1251191,"site\_section\_id":23382577,"standard\_addressability\_ids":\[20,30\],"standard\_app\_bundle\_id":8626,"standard\_app\_id":4712,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"standard\_iab\_category\_ids":\[1,6\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":28,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":23382577,"video\_cro\_network\_id":535258,"video\_cro\_site\_id":1251191}'  
    request\_\_request\_throttling\_info:  
      Hoover (entity=request, network=512166): '{"flags":2,"model\_info":\[{"model\_id":67,"model\_flags":2},{"model\_id":66,"model\_flags":0}\]}'  
      HooverPP (entity=request, network=512166): '{"flags":2}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":346,"external\_candidate":307}'  
      HooverPP (entity=request, network=512166): '{"total":346}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":651.0,"bg\_alias\_growth\_ratio":651.0,"num\_dx\_enriched\_keys":651,"num\_dx\_enriched\_alias\_ids":651}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":651.0}'

  \[row=7\]  
    request\_\_bid\_request:  
      Hoover (entity=request, network=512166): '{"publisher\_id":"535258","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_bundle":"B076X8FKXP","impression":\[{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"},{"private\_auction":false,"floor":9.0,"currency":"USD"}\]}'  
      HooverPP (entity=request, network=512166): '{"app\_bundle":"B076X8FKXP","app\_id":"927101","app\_name":"Fawesome - Free Awesome TV & Movies","app\_storeurl":"<https://www.amazon.com/dp/B076X8FKXP> ","channel\_name":"Fawesome - Free Awesome TV & Movies","domain":"<http://fawesome.tv> ","impression":\[{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false},{"floor":9.0,"private\_auction":false}\],"publisher\_id":"535258"}'  
    request\_\_bid\_request\_\_impression:  
      Hoover (entity=request, network=512166): '\[\\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\', \\'{"private\_auction":false,"floor":9.0,"currency":"USD"}\\'\]'  
      HooverPP (entity=request, network=512166): '\[\\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\', \\'{"floor":9.0,"private\_auction":false}\\'\]'  
    request\_\_context:  
      Hoover (entity=request, network=512166): '{"network\_id":535258,"asset\_id":1309893687,"site\_section\_id":23382577,"asset\_duration":7028.0,"request\_duration":7028.0,"time\_position":0.0,"profile\_id":16676,"request\_format":7,"response\_format":19,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":87,"bucket\_id":498},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":98,"bucket\_id":484},{"collection\_id":140,"bucket\_id":431},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":182,"bucket\_id":520},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":1101,"bucket\_id":1102},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","request\_trace\_id":"10aea168a04b08f77b20418d63fbf07a","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"content\_form\_id":3,"content\_rating\_id":12,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":28,"website\_root\_id":1251191,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1750,"post\_selection\_external\_ad\_timeout":200},"standard\_app\_id":4712,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,6\],"standard\_app\_bundle\_id":8626,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[20,30\],"video\_cro\_network\_id":535258,"video\_cro\_context\_id":23382577,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":-1,"video\_cro\_site\_id":1251191,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1251191,"site\_section\_cro\_parsed\_site\_section\_id":23382577,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":-1,"distributor\_video\_asset\_group\_id":1309893687,"distributor\_site\_section\_id":23382577,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=512166): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":498,"collection\_id":87},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":484,"collection\_id":98},{"bucket\_id":431,"collection\_id":140},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":520,"collection\_id":182},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":1102,"collection\_id":1101},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"asset\_duration":7028.0,"asset\_id":1309893687,"content\_form\_id":3,"content\_rating\_id":12,"distributor\_network\_id":535258,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":23382577,"distributor\_video\_asset\_id":-1,"host\_name":"[82ada.v.fwmrm.net](http://82ada.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_content\_genre","value":"Crime,Drama,Musical,Tennis,Thriller,War"},{"key":"\_fw\_did\_google\_advertising\_id","value":"89a66413-5fb5-4f94-b628-2d0a70031f26"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_us\_privacy","value":"1YNN"}\],"network\_id":535258,"profile\_id":16676,"profile\_trait":{"post\_selection\_external\_ad\_timeout":200,"pre\_selection\_external\_ad\_timeout":1750},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":7028.0,"request\_format":7,"response\_format":19,"site\_section\_cro\_asset\_id":23382577,"site\_section\_cro\_network\_id":535258,"site\_section\_cro\_site\_id":1251191,"site\_section\_id":23382577,"standard\_addressability\_ids":\[20,30\],"standard\_app\_bundle\_id":8626,"standard\_app\_id":4712,"standard\_brand\_id":233,"standard\_genre\_ids":\[8,86\],"standard\_iab\_category\_ids":\[1,6\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":28,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":-1,"video\_cro\_context\_id":23382577,"video\_cro\_network\_id":535258,"video\_cro\_site\_id":1251191}'  
    request\_\_request\_throttling\_info:  
      Hoover (entity=request, network=512166): '{"flags":2,"model\_info":\[{"model\_id":67,"model\_flags":2},{"model\_id":66,"model\_flags":0}\]}'  
      HooverPP (entity=request, network=512166): '{"flags":2}'  
    request\_\_time\_record:  
      Hoover (entity=request, network=512166): '{"total":346,"external\_candidate":307}'  
      HooverPP (entity=request, network=512166): '{"total":346}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=512166): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=512166): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=512166): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=512166): '{"num\_keys":5,"dx\_alias\_growth\_ratio":651.0,"bg\_alias\_growth\_ratio":651.0,"num\_dx\_enriched\_keys":651,"num\_dx\_enriched\_alias\_ids":651}'  
      HooverPP (entity=request, network=512166): '{"bg\_alias\_growth\_ratio":651.0}'

```
  END OF REPORT
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=20.92s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=361.74s | rows=10  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (94243247, 90366976, 87143704, 88990076, 92962295, 93722436, 91693131, 93697813, 93380951, 93918320)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=77.42s | rows=10  
SELECT request\_\_transaction\_id, request\_\_advertisement\_count, request\_\_advertisement\_delivered\_count, request\_\_audience\_flags, request\_\_backend\_filtration\_reason, request\_\_bid\_request, request\_\_bid\_request\_\_app\_bundle, request\_\_bid\_request\_\_app\_id, request\_\_bid\_request\_\_app\_name, request\_\_bid\_request\_\_auction\_type, request\_\_bid\_request\_\_impression, request\_\_bid\_request\_\_impression\_\_deal, request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id, request\_\_bid\_request\_\_impression\_\_floor, request\_\_bid\_request\_\_impression\_\_private\_auction, request\_\_bid\_request\_\_inventory\_source, request\_\_bid\_request\_\_publisher\_id, request\_\_bit\_flags, request\_\_candidates, request\_\_cbp, request\_\_cbp\_\_slot\_template\_id, request\_\_client\_facing\_ivt\_reason\_flag, request\_\_context, request\_\_context\_\_ab\_test\_item, request\_\_context\_\_ab\_test\_item\_\_bucket\_id, request\_\_context\_\_ab\_test\_item\_\_collection\_id, request\_\_context\_\_airing\_channel\_id, request\_\_context\_\_asset\_duration, request\_\_context\_\_asset\_id, request\_\_context\_\_content\_form\_id, request\_\_context\_\_content\_rating\_id, request\_\_context\_\_custom\_airing\_break\_id, request\_\_context\_\_custom\_airing\_channel\_id, request\_\_context\_\_custom\_airing\_id, request\_\_context\_\_custom\_asset\_id, request\_\_context\_\_custom\_site\_section\_id, request\_\_context\_\_distributor\_asset\_id, request\_\_context\_\_distributor\_site\_section\_group\_id, request\_\_context\_\_distributor\_site\_section\_id, request\_\_context\_\_distributor\_video\_asset\_id, request\_\_context\_\_explicit\_candidates, request\_\_context\_\_host\_name, request\_\_context\_\_inventory\_location\_id, request\_\_context\_\_ip\_enabled\_audience\_id, request\_\_context\_\_linear\_break\_source, request\_\_context\_\_network\_id, request\_\_context\_\_out\_signal\_id, request\_\_context\_\_page\_random, request\_\_context\_\_po\_id, request\_\_context\_\_po\_type, request\_\_context\_\_profile\_concrete\_event\_id, request\_\_context\_\_profile\_id, request\_\_context\_\_profile\_trait, request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout, request\_\_context\_\_profile\_type, request\_\_context\_\_rbp\_device\_type, request\_\_context\_\_rbp\_platform, request\_\_context\_\_request\_duration, request\_\_context\_\_request\_format, request\_\_context\_\_response\_format, request\_\_context\_\_site\_section\_cro\_asset\_id, request\_\_context\_\_site\_section\_cro\_network\_id, request\_\_context\_\_site\_section\_cro\_site\_id, request\_\_context\_\_site\_section\_id, request\_\_context\_\_source\_id, request\_\_context\_\_standard\_addressability\_ids, request\_\_context\_\_standard\_app\_bundle\_id, request\_\_context\_\_standard\_app\_id, request\_\_context\_\_standard\_brand\_id, request\_\_context\_\_standard\_channel\_id, request\_\_context\_\_standard\_content\_credential\_status\_id, request\_\_context\_\_standard\_content\_daypart\_id, request\_\_context\_\_standard\_content\_series\_id, request\_\_context\_\_standard\_content\_subscription\_model\_id, request\_\_context\_\_standard\_content\_territory\_id, request\_\_context\_\_standard\_content\_viewership\_profile\_ids, request\_\_context\_\_standard\_endpoint\_id, request\_\_context\_\_standard\_endpoint\_owner\_id, request\_\_context\_\_standard\_genre\_ids, request\_\_context\_\_standard\_iab\_category\_ids, request\_\_context\_\_standard\_language\_ids, request\_\_context\_\_standard\_movie\_rating\_id, request\_\_context\_\_standard\_privacy\_id, request\_\_context\_\_standard\_programmer\_id, request\_\_context\_\_standard\_publisher\_id, request\_\_context\_\_standard\_site\_domain\_id, request\_\_context\_\_standard\_sport\_entity\_ids, request\_\_context\_\_standard\_ssp\_channel\_id, request\_\_context\_\_station\_id, request\_\_context\_\_stream\_id, request\_\_context\_\_stream\_mode\_id, request\_\_context\_\_stream\_mode\_ids, request\_\_context\_\_time\_position, request\_\_context\_\_transcode\_package\_id, request\_\_context\_\_tv\_network\_group\_ids, request\_\_context\_\_tv\_network\_id, request\_\_context\_\_video\_cro\_asset\_id, request\_\_context\_\_video\_cro\_context\_id, request\_\_context\_\_video\_cro\_network\_id, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids, request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id, request\_\_context\_\_video\_cro\_site\_id, request\_\_context\_\_video\_random, request\_\_context\_\_video\_slot\_compatible\_dimensions, request\_\_decision\_info, request\_\_decision\_info\_\_external\_bridge, request\_\_decision\_info\_\_external\_bridge\_\_slot\_index, request\_\_decision\_info\_\_external\_bridge\_\_status, request\_\_decision\_info\_\_flag1, request\_\_decision\_info\_\_flag2, request\_\_decision\_info\_\_flag3, request\_\_decision\_info\_\_flag4, request\_\_decision\_info\_\_inventory\_protections, request\_\_decision\_info\_\_inventory\_protections\_\_level, request\_\_decision\_info\_\_inventory\_protections\_\_scope, request\_\_decision\_info\_\_inventory\_protections\_\_separation, request\_\_decision\_info\_\_value1, request\_\_decision\_info\_\_value10, request\_\_decision\_info\_\_value11, request\_\_decision\_info\_\_value12, request\_\_decision\_info\_\_value13, request\_\_decision\_info\_\_value14, request\_\_decision\_info\_\_value15, request\_\_decision\_info\_\_value2, request\_\_decision\_info\_\_value3, request\_\_decision\_info\_\_value4, request\_\_decision\_info\_\_value5, request\_\_decision\_info\_\_value6, request\_\_decision\_info\_\_value7, request\_\_decision\_info\_\_value8, request\_\_decision\_info\_\_value9, request\_\_delivery\_method, request\_\_demand\_log\_magnifier, request\_\_dro\_network\_id, request\_\_extra\_flags, request\_\_extra\_flags2, request\_\_extra\_flags3, request\_\_flags, request\_\_geo\_data\_provider\_id, request\_\_global\_currency\_version, request\_\_guaranteed\_deal\_avail, request\_\_guaranteed\_deal\_avail\_\_buyer\_id, request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id, request\_\_hashed\_key\_value, request\_\_is\_data\_right\_enabled, request\_\_is\_filtered, request\_\_is\_first\_user\_visitor, request\_\_is\_no\_selection, request\_\_is\_ssp\_bidder\_request, request\_\_kafka\_msg\_key, request\_\_kafka\_msg\_size, request\_\_linear\_capnedit, request\_\_linear\_capnedit\_\_active\_state, request\_\_linear\_capnedit\_\_device\_id, request\_\_linear\_capnedit\_\_is\_dvr, request\_\_linear\_capnedit\_\_last\_activity\_time, request\_\_linear\_capnedit\_\_mode, request\_\_linear\_capnedit\_\_tune\_time, request\_\_log\_sampling, request\_\_log\_sampling\_\_magnifier, request\_\_log\_sampling\_\_mode, request\_\_magnifier, request\_\_mpe\_matcher\_filters, request\_\_mpe\_matcher\_filters\_\_bucket\_id, request\_\_mpe\_matcher\_filters\_\_id, request\_\_mpe\_matcher\_filters\_\_weight, request\_\_mrc\_compliance\_label, request\_\_multiplier, request\_\_networks, request\_\_prebid\_sivt, request\_\_prebid\_sivt\_\_capnedit, request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason, request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid, request\_\_prebid\_sivt\_\_gateway\_response, request\_\_prebid\_sivt\_\_inhouse, request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason, request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted, request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid, request\_\_prebid\_sivt\_\_sivt\_model, request\_\_prebid\_sivt\_\_whiteops, request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason, request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id, request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid, request\_\_privacy\_choice\_ids, request\_\_privacy\_info, request\_\_privacy\_info\_\_compliance\_flag, request\_\_privacy\_info\_\_gdpr\_flag, request\_\_privacy\_info\_\_gpp, request\_\_privacy\_info\_\_gpp\_\_flag, request\_\_privacy\_info\_\_gpp\_\_section, request\_\_privacy\_info\_\_impacted\_features\_flag, request\_\_privacy\_jurisdiction\_ids, request\_\_request\_prefilter, request\_\_request\_prefilter\_\_flag, request\_\_request\_throttling\_info, request\_\_request\_throttling\_info\_\_exempt\_thousandth, request\_\_request\_throttling\_info\_\_flags, request\_\_request\_throttling\_info\_\_level, request\_\_scores, request\_\_scores\_\_flag, request\_\_scores\_\_network\_id, request\_\_scores\_\_score, request\_\_server\_group, request\_\_server\_id, request\_\_server\_pool, request\_\_simulated\_tiemstamp, request\_\_soft\_guaranteed\_ad, request\_\_soft\_guaranteed\_ad\_\_ad\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_id, request\_\_soft\_guaranteed\_ad\_\_entity\_type, request\_\_soft\_guaranteed\_ad\_\_network\_id, request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads, request\_\_time\_record, request\_\_time\_record\_\_total, request\_\_timestamp, request\_\_traffic\_compliance, request\_\_traffic\_compliance\_\_endpoint\_id, request\_\_traffic\_compliance\_\_mrc\_compliance\_flag, request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type, request\_\_traffic\_type, request\_\_userdb\_audience\_user\_info, request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio, request\_\_yield\_optimization\_ids, request\_\_yield\_optimization\_ids\_\_demand\_id, request\_\_yield\_optimization\_ids\_\_demand\_type, request\_\_yield\_optimization\_ids\_\_optimization\_ids FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (94243247, 90366976, 87143704, 88990076, 92962295, 93722436, 91693131, 93697813, 93380951, 93918320)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=request, network=520311)  
  Source B : HooverPP (entity=request, network=520311)  
  Rows  A  : 10  
  Rows  B  : 10  
  Columns A: 231  
  Columns B: 231

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 10

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (231 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/10 (0.00%)
  Column match %    : 224/231 (96.97%)
  Cell/value match %: 2,240/2,310 (96.97%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
request__client_facing_ivt_reason_flag                       10 row(s)
request__context__standard_content_viewership_profile_ids    10 row(s)
request__context__standard_sport_entity_ids                  10 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos 10 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__nested_sub_yo_ids 10 row(s)
request__context__video_cro_pre_targeting_yield_optimization_infos__sub_yo_id 10 row(s)
request__decision_info__external_bridge                      10 row(s)
request__decision_info__external_bridge__slot_index          10 row(s)
request__decision_info__external_bridge__status              10 row(s)
request__linear_capnedit                                     10 row(s)
request__linear_capnedit__active_state                       10 row(s)
request__linear_capnedit__device_id                          10 row(s)
request__linear_capnedit__is_dvr                             10 row(s)
request__linear_capnedit__last_activity_time                 10 row(s)
request__linear_capnedit__mode                               10 row(s)
request__linear_capnedit__tune_time                          10 row(s)
request__mpe_matcher_filters                                 10 row(s)
request__mpe_matcher_filters__bucket_id                      10 row(s)
request__mpe_matcher_filters__id                             10 row(s)
request__mpe_matcher_filters__weight                         10 row(s)
request__mrc_compliance_label                                10 row(s)
request__context__standard_iab_category_ids                  4 row(s)
request__context__video_cro_selected_yield_optimization_infos 4 row(s)
request__context__video_cro_selected_yield_optimization_infos__nested_sub_yo_ids 4 row(s)
request__context__video_cro_selected_yield_optimization_infos__sub_yo_id 4 row(s)
request__guaranteed_deal_avail                               4 row(s)
request__guaranteed_deal_avail__buyer_id                     4 row(s)
request__guaranteed_deal_avail__internal_deal_id             4 row(s)
request__yield_optimization_ids                              4 row(s)
request__yield_optimization_ids__demand_id                   4 row(s)
request__yield_optimization_ids__demand_type                 4 row(s)
request__yield_optimization_ids__optimization_ids            4 row(s)
```

  ❌ 10 row(s) have differences:

Column diff summary (sorted by frequency):  
    request\_\_cbp                                                 10 row(s)  
    request\_\_context                                             10 row(s)  
    request\_\_scores                                              10 row(s)  
    request\_\_time\_record                                         10 row(s)  
    request\_\_timestamp                                           10 row(s)  
    request\_\_traffic\_compliance                                  10 row(s)  
    request\_\_userdb\_audience\_user\_info                           10 row(s)

  Detailed diffs:

  \[row=2\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":71393}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":71393}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":385677798,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","site\_section\_id":17804989,"page\_random":"dcdb2c2553080469","video\_random":"e9282f7c9d1ef7b5","asset\_duration":1301.0,"request\_duration":119.0,"time\_position":0.0,"profile\_id":11410,"ux\_network\_id":520311,"ux\_section\_id":1106579,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32,53\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":43,"bucket\_id":121},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":159,"bucket\_id":462},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"12b127969c1f7ff617bfea3a3f09a347","rbp\_platform":"DESKTOP","stream\_mode\_id":3,"standard\_brand\_id":1170,"standard\_genre\_ids":\[10\],"content\_form\_id":3,"content\_rating\_id":6,"standard\_language\_ids":\[12\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":63,"standard\_endpoint\_owner\_id":52,"standard\_endpoint\_id":396,"website\_root\_id":1106579,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":2000,"post\_selection\_external\_ad\_timeout":1000},"standard\_app\_id":44,"stream\_mode\_ids":\[1,3\],"standard\_content\_territory\_id":21,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17804989,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":385677798,"video\_cro\_site\_id":1106579,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1106579,"site\_section\_cro\_parsed\_site\_section\_id":17804989,"rbp\_device\_type":"PC","distributor\_video\_asset\_id":385677798,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":121,"collection\_id":43},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"tv.vidaa.ui.plus","name":"pluto tv","storeurl":"<https://apps.vidaa.com/app-detail?id=2375> "},"asset\_duration":1301.0,"asset\_id":385677798,"content\_form\_id":3,"content\_rating\_id":6,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_video\_asset\_id":385677798,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_UID"},{"key":"\_fw\_content\_language","value":"pt"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"vidaa:7d5f5656-24b0-8cee-242e-6ce6f206671e"},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.146 Odin/111.5563.5.1 Safari/537.36 Model/VIDAA-MT9602 VIDAA/9.0(TOSHIBA;SmartTV;65C350LS;MTK9602/V0000.09.09M.P1124;UHD;65C350LS;)"},{"key":"\_fw\_h\_x\_country","value":"BR"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1---"},{"key":"\_fw\_vcid2","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"break\_num","value":"2"},{"key":"cbp\_duration","value":"119"},{"key":"cht"},{"key":"content\_type","value":"vll"},{"key":"fms\_bididtype"},{"key":"fms\_emailhash"},{"key":"fms\_hh\_ramp\_id"},{"key":"fms\_idfv"},{"key":"fms\_ifa"},{"key":"fms\_liveramp\_idl"},{"key":"fms\_ramp\_id"},{"key":"fms\_ruleid","value":"10003,10004"},{"key":"fms\_subscriberid"},{"key":"fms\_userid","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"fms\_vcid2type","value":"userid"},{"key":"paln"},{"key":"playername\_version","value":"7.0.1-5c6cff9"},{"key":"pluto\_deviceId","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"pluto\_deviceMake","value":"hisense"},{"key":"pluto\_deviceModel","value":"vidaa"},{"key":"pluto\_partnerCode","value":"ZOOGBRJV4MZRE67P"},{"key":"pluto\_session\_id","value":"5608c29b-5c60-11f1-9e94-0a29ec600514"},{"key":"pluto\_transaction\_id","value":"4b8d5173-fe34-40fe-ac11-b6e28a4144b1"},{"key":"vauth","value":"Njak4MfA9PKgFC7xjcY9xQTS-HbTYaibXayQqt\_04pJL6pD3jGa96DVw-jFj3bnTAcF9fdAqm4mxg6TT7QgaBWisIovNNPoZ\_v24deZK8\_PzvsO1ylvR9pdandQ5Kl7Av0Ztz135I\_DLL3B-wSw2eL\_mgkU7ww4td4Sm7jH9RtYbplOHcO1qlsEWWR-Q7ZgtrhmuUEGcWNSKxTNiZSSSTw"}\],"network\_id":520311,"page\_random":"dcdb2c2553080469","profile\_concrete\_event\_id":\[32,53\],"profile\_id":11410,"profile\_trait":{"post\_selection\_external\_ad\_timeout":1000,"pre\_selection\_external\_ad\_timeout":2000},"profile\_type":"COMPOUND","rbp\_device\_type":"PC","rbp\_platform":"DESKTOP","request\_duration":119.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1106579,"site\_section\_id":17804989,"standard\_addressability\_ids":\[4,5\],"standard\_app\_id":44,"standard\_brand\_id":1170,"standard\_content\_territory\_id":21,"standard\_endpoint\_id":396,"standard\_endpoint\_owner\_id":52,"standard\_genre\_ids":\[10\],"standard\_language\_ids":\[12\],"standard\_privacy\_id":1,"standard\_programmer\_id":63,"stream\_mode\_id":3,"stream\_mode\_ids":\[1,3\],"time\_position":0.0,"video\_cro\_asset\_id":385677798,"video\_cro\_context\_id":17804989,"video\_cro\_network\_id":520311,"video\_cro\_site\_id":1106579,"video\_random":"e9282f7c9d1ef7b5"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":94243247,"flag":514,"score":1601}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":1601}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":318,"external\_candidate":280}'  
      HooverPP (entity=request, network=520311): '{"total":318}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":4,"dx\_alias\_growth\_ratio":0.0,"bg\_alias\_growth\_ratio":1.0,"num\_dx\_enriched\_keys":0,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":1.0}'

  \[row=3\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":71393}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":71393}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":385677798,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","site\_section\_id":17804989,"page\_random":"dcdb2c2553080469","video\_random":"e9282f7c9d1ef7b5","asset\_duration":1301.0,"request\_duration":119.0,"time\_position":0.0,"profile\_id":11410,"ux\_network\_id":520311,"ux\_section\_id":1106579,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32,53\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":43,"bucket\_id":121},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":159,"bucket\_id":462},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"12b127969c1f7ff617bfea3a3f09a347","rbp\_platform":"DESKTOP","stream\_mode\_id":3,"standard\_brand\_id":1170,"standard\_genre\_ids":\[10\],"content\_form\_id":3,"content\_rating\_id":6,"standard\_language\_ids":\[12\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":63,"standard\_endpoint\_owner\_id":52,"standard\_endpoint\_id":396,"website\_root\_id":1106579,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":2000,"post\_selection\_external\_ad\_timeout":1000},"standard\_app\_id":44,"stream\_mode\_ids":\[1,3\],"standard\_content\_territory\_id":21,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17804989,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":385677798,"video\_cro\_site\_id":1106579,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1106579,"site\_section\_cro\_parsed\_site\_section\_id":17804989,"rbp\_device\_type":"PC","distributor\_video\_asset\_id":385677798,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":121,"collection\_id":43},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"tv.vidaa.ui.plus","name":"pluto tv","storeurl":"<https://apps.vidaa.com/app-detail?id=2375> "},"asset\_duration":1301.0,"asset\_id":385677798,"content\_form\_id":3,"content\_rating\_id":6,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_video\_asset\_id":385677798,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_UID"},{"key":"\_fw\_content\_language","value":"pt"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"vidaa:7d5f5656-24b0-8cee-242e-6ce6f206671e"},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.146 Odin/111.5563.5.1 Safari/537.36 Model/VIDAA-MT9602 VIDAA/9.0(TOSHIBA;SmartTV;65C350LS;MTK9602/V0000.09.09M.P1124;UHD;65C350LS;)"},{"key":"\_fw\_h\_x\_country","value":"BR"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1---"},{"key":"\_fw\_vcid2","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"break\_num","value":"2"},{"key":"cbp\_duration","value":"119"},{"key":"cht"},{"key":"content\_type","value":"vll"},{"key":"fms\_bididtype"},{"key":"fms\_emailhash"},{"key":"fms\_hh\_ramp\_id"},{"key":"fms\_idfv"},{"key":"fms\_ifa"},{"key":"fms\_liveramp\_idl"},{"key":"fms\_ramp\_id"},{"key":"fms\_ruleid","value":"10003,10004"},{"key":"fms\_subscriberid"},{"key":"fms\_userid","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"fms\_vcid2type","value":"userid"},{"key":"paln"},{"key":"playername\_version","value":"7.0.1-5c6cff9"},{"key":"pluto\_deviceId","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"pluto\_deviceMake","value":"hisense"},{"key":"pluto\_deviceModel","value":"vidaa"},{"key":"pluto\_partnerCode","value":"ZOOGBRJV4MZRE67P"},{"key":"pluto\_session\_id","value":"5608c29b-5c60-11f1-9e94-0a29ec600514"},{"key":"pluto\_transaction\_id","value":"4b8d5173-fe34-40fe-ac11-b6e28a4144b1"},{"key":"vauth","value":"Njak4MfA9PKgFC7xjcY9xQTS-HbTYaibXayQqt\_04pJL6pD3jGa96DVw-jFj3bnTAcF9fdAqm4mxg6TT7QgaBWisIovNNPoZ\_v24deZK8\_PzvsO1ylvR9pdandQ5Kl7Av0Ztz135I\_DLL3B-wSw2eL\_mgkU7ww4td4Sm7jH9RtYbplOHcO1qlsEWWR-Q7ZgtrhmuUEGcWNSKxTNiZSSSTw"}\],"network\_id":520311,"page\_random":"dcdb2c2553080469","profile\_concrete\_event\_id":\[32,53\],"profile\_id":11410,"profile\_trait":{"post\_selection\_external\_ad\_timeout":1000,"pre\_selection\_external\_ad\_timeout":2000},"profile\_type":"COMPOUND","rbp\_device\_type":"PC","rbp\_platform":"DESKTOP","request\_duration":119.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1106579,"site\_section\_id":17804989,"standard\_addressability\_ids":\[4,5\],"standard\_app\_id":44,"standard\_brand\_id":1170,"standard\_content\_territory\_id":21,"standard\_endpoint\_id":396,"standard\_endpoint\_owner\_id":52,"standard\_genre\_ids":\[10\],"standard\_language\_ids":\[12\],"standard\_privacy\_id":1,"standard\_programmer\_id":63,"stream\_mode\_id":3,"stream\_mode\_ids":\[1,3\],"time\_position":0.0,"video\_cro\_asset\_id":385677798,"video\_cro\_context\_id":17804989,"video\_cro\_network\_id":520311,"video\_cro\_site\_id":1106579,"video\_random":"e9282f7c9d1ef7b5"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":94243247,"flag":514,"score":1601}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":1601}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":318,"external\_candidate":280}'  
      HooverPP (entity=request, network=520311): '{"total":318}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":4,"dx\_alias\_growth\_ratio":0.0,"bg\_alias\_growth\_ratio":1.0,"num\_dx\_enriched\_keys":0,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":1.0}'

  \[row=4\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":71393}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":71393}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":385677798,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","site\_section\_id":17804989,"page\_random":"dcdb2c2553080469","video\_random":"e9282f7c9d1ef7b5","asset\_duration":1301.0,"request\_duration":119.0,"time\_position":0.0,"profile\_id":11410,"ux\_network\_id":520311,"ux\_section\_id":1106579,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32,53\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":43,"bucket\_id":121},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":159,"bucket\_id":462},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"12b127969c1f7ff617bfea3a3f09a347","rbp\_platform":"DESKTOP","stream\_mode\_id":3,"standard\_brand\_id":1170,"standard\_genre\_ids":\[10\],"content\_form\_id":3,"content\_rating\_id":6,"standard\_language\_ids":\[12\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":63,"standard\_endpoint\_owner\_id":52,"standard\_endpoint\_id":396,"website\_root\_id":1106579,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":2000,"post\_selection\_external\_ad\_timeout":1000},"standard\_app\_id":44,"stream\_mode\_ids":\[1,3\],"standard\_content\_territory\_id":21,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17804989,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":385677798,"video\_cro\_site\_id":1106579,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1106579,"site\_section\_cro\_parsed\_site\_section\_id":17804989,"rbp\_device\_type":"PC","distributor\_video\_asset\_id":385677798,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":121,"collection\_id":43},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"tv.vidaa.ui.plus","name":"pluto tv","storeurl":"<https://apps.vidaa.com/app-detail?id=2375> "},"asset\_duration":1301.0,"asset\_id":385677798,"content\_form\_id":3,"content\_rating\_id":6,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_video\_asset\_id":385677798,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_UID"},{"key":"\_fw\_content\_language","value":"pt"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"vidaa:7d5f5656-24b0-8cee-242e-6ce6f206671e"},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.146 Odin/111.5563.5.1 Safari/537.36 Model/VIDAA-MT9602 VIDAA/9.0(TOSHIBA;SmartTV;65C350LS;MTK9602/V0000.09.09M.P1124;UHD;65C350LS;)"},{"key":"\_fw\_h\_x\_country","value":"BR"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1---"},{"key":"\_fw\_vcid2","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"break\_num","value":"2"},{"key":"cbp\_duration","value":"119"},{"key":"cht"},{"key":"content\_type","value":"vll"},{"key":"fms\_bididtype"},{"key":"fms\_emailhash"},{"key":"fms\_hh\_ramp\_id"},{"key":"fms\_idfv"},{"key":"fms\_ifa"},{"key":"fms\_liveramp\_idl"},{"key":"fms\_ramp\_id"},{"key":"fms\_ruleid","value":"10003,10004"},{"key":"fms\_subscriberid"},{"key":"fms\_userid","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"fms\_vcid2type","value":"userid"},{"key":"paln"},{"key":"playername\_version","value":"7.0.1-5c6cff9"},{"key":"pluto\_deviceId","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"pluto\_deviceMake","value":"hisense"},{"key":"pluto\_deviceModel","value":"vidaa"},{"key":"pluto\_partnerCode","value":"ZOOGBRJV4MZRE67P"},{"key":"pluto\_session\_id","value":"5608c29b-5c60-11f1-9e94-0a29ec600514"},{"key":"pluto\_transaction\_id","value":"4b8d5173-fe34-40fe-ac11-b6e28a4144b1"},{"key":"vauth","value":"Njak4MfA9PKgFC7xjcY9xQTS-HbTYaibXayQqt\_04pJL6pD3jGa96DVw-jFj3bnTAcF9fdAqm4mxg6TT7QgaBWisIovNNPoZ\_v24deZK8\_PzvsO1ylvR9pdandQ5Kl7Av0Ztz135I\_DLL3B-wSw2eL\_mgkU7ww4td4Sm7jH9RtYbplOHcO1qlsEWWR-Q7ZgtrhmuUEGcWNSKxTNiZSSSTw"}\],"network\_id":520311,"page\_random":"dcdb2c2553080469","profile\_concrete\_event\_id":\[32,53\],"profile\_id":11410,"profile\_trait":{"post\_selection\_external\_ad\_timeout":1000,"pre\_selection\_external\_ad\_timeout":2000},"profile\_type":"COMPOUND","rbp\_device\_type":"PC","rbp\_platform":"DESKTOP","request\_duration":119.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1106579,"site\_section\_id":17804989,"standard\_addressability\_ids":\[4,5\],"standard\_app\_id":44,"standard\_brand\_id":1170,"standard\_content\_territory\_id":21,"standard\_endpoint\_id":396,"standard\_endpoint\_owner\_id":52,"standard\_genre\_ids":\[10\],"standard\_language\_ids":\[12\],"standard\_privacy\_id":1,"standard\_programmer\_id":63,"stream\_mode\_id":3,"stream\_mode\_ids":\[1,3\],"time\_position":0.0,"video\_cro\_asset\_id":385677798,"video\_cro\_context\_id":17804989,"video\_cro\_network\_id":520311,"video\_cro\_site\_id":1106579,"video\_random":"e9282f7c9d1ef7b5"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":94243247,"flag":514,"score":1601}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":1601}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":318,"external\_candidate":280}'  
      HooverPP (entity=request, network=520311): '{"total":318}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":4,"dx\_alias\_growth\_ratio":0.0,"bg\_alias\_growth\_ratio":1.0,"num\_dx\_enriched\_keys":0,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":1.0}'

  \[row=5\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":71393}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":71393}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":385677798,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","site\_section\_id":17804989,"page\_random":"dcdb2c2553080469","video\_random":"e9282f7c9d1ef7b5","asset\_duration":1301.0,"request\_duration":119.0,"time\_position":0.0,"profile\_id":11410,"ux\_network\_id":520311,"ux\_section\_id":1106579,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32,53\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":43,"bucket\_id":121},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":159,"bucket\_id":462},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"12b127969c1f7ff617bfea3a3f09a347","rbp\_platform":"DESKTOP","stream\_mode\_id":3,"standard\_brand\_id":1170,"standard\_genre\_ids":\[10\],"content\_form\_id":3,"content\_rating\_id":6,"standard\_language\_ids":\[12\],"ip\_enabled\_audience\_id":1,"standard\_programmer\_id":63,"standard\_endpoint\_owner\_id":52,"standard\_endpoint\_id":396,"website\_root\_id":1106579,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":2000,"post\_selection\_external\_ad\_timeout":1000},"standard\_app\_id":44,"stream\_mode\_ids":\[1,3\],"standard\_content\_territory\_id":21,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,5\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17804989,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":385677798,"video\_cro\_site\_id":1106579,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1106579,"site\_section\_cro\_parsed\_site\_section\_id":17804989,"rbp\_device\_type":"PC","distributor\_video\_asset\_id":385677798,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":121,"collection\_id":43},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"tv.vidaa.ui.plus","name":"pluto tv","storeurl":"<https://apps.vidaa.com/app-detail?id=2375> "},"asset\_duration":1301.0,"asset\_id":385677798,"content\_form\_id":3,"content\_rating\_id":6,"custom\_asset\_id":"520311/61af74afeb667e0013a6d156\_61af74b2eb667e0013a6d1c9","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17804989,"distributor\_video\_asset\_id":385677798,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":1,"key\_value":\[{"key":"\_fw\_3P\_UID"},{"key":"\_fw\_content\_language","value":"pt"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"vidaa:7d5f5656-24b0-8cee-242e-6ce6f206671e"},{"key":"\_fw\_h\_user\_agent","value":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.146 Odin/111.5563.5.1 Safari/537.36 Model/VIDAA-MT9602 VIDAA/9.0(TOSHIBA;SmartTV;65C350LS;MTK9602/V0000.09.09M.P1124;UHD;65C350LS;)"},{"key":"\_fw\_h\_x\_country","value":"BR"},{"key":"\_fw\_is\_lat","value":"1"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_us\_privacy","value":"1---"},{"key":"\_fw\_vcid2","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"break\_num","value":"2"},{"key":"cbp\_duration","value":"119"},{"key":"cht"},{"key":"content\_type","value":"vll"},{"key":"fms\_bididtype"},{"key":"fms\_emailhash"},{"key":"fms\_hh\_ramp\_id"},{"key":"fms\_idfv"},{"key":"fms\_ifa"},{"key":"fms\_liveramp\_idl"},{"key":"fms\_ramp\_id"},{"key":"fms\_ruleid","value":"10003,10004"},{"key":"fms\_subscriberid"},{"key":"fms\_userid","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"fms\_vcid2type","value":"userid"},{"key":"paln"},{"key":"playername\_version","value":"7.0.1-5c6cff9"},{"key":"pluto\_deviceId","value":"21aea3f0-f126-11f0-b93f-3511698341af"},{"key":"pluto\_deviceMake","value":"hisense"},{"key":"pluto\_deviceModel","value":"vidaa"},{"key":"pluto\_partnerCode","value":"ZOOGBRJV4MZRE67P"},{"key":"pluto\_session\_id","value":"5608c29b-5c60-11f1-9e94-0a29ec600514"},{"key":"pluto\_transaction\_id","value":"4b8d5173-fe34-40fe-ac11-b6e28a4144b1"},{"key":"vauth","value":"Njak4MfA9PKgFC7xjcY9xQTS-HbTYaibXayQqt\_04pJL6pD3jGa96DVw-jFj3bnTAcF9fdAqm4mxg6TT7QgaBWisIovNNPoZ\_v24deZK8\_PzvsO1ylvR9pdandQ5Kl7Av0Ztz135I\_DLL3B-wSw2eL\_mgkU7ww4td4Sm7jH9RtYbplOHcO1qlsEWWR-Q7ZgtrhmuUEGcWNSKxTNiZSSSTw"}\],"network\_id":520311,"page\_random":"dcdb2c2553080469","profile\_concrete\_event\_id":\[32,53\],"profile\_id":11410,"profile\_trait":{"post\_selection\_external\_ad\_timeout":1000,"pre\_selection\_external\_ad\_timeout":2000},"profile\_type":"COMPOUND","rbp\_device\_type":"PC","rbp\_platform":"DESKTOP","request\_duration":119.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17804989,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1106579,"site\_section\_id":17804989,"standard\_addressability\_ids":\[4,5\],"standard\_app\_id":44,"standard\_brand\_id":1170,"standard\_content\_territory\_id":21,"standard\_endpoint\_id":396,"standard\_endpoint\_owner\_id":52,"standard\_genre\_ids":\[10\],"standard\_language\_ids":\[12\],"standard\_privacy\_id":1,"standard\_programmer\_id":63,"stream\_mode\_id":3,"stream\_mode\_ids":\[1,3\],"time\_position":0.0,"video\_cro\_asset\_id":385677798,"video\_cro\_context\_id":17804989,"video\_cro\_network\_id":520311,"video\_cro\_site\_id":1106579,"video\_random":"e9282f7c9d1ef7b5"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":94243247,"flag":514,"score":1601}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":1601}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":318,"external\_candidate":280}'  
      HooverPP (entity=request, network=520311): '{"total":318}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":4,"dx\_alias\_growth\_ratio":0.0,"bg\_alias\_growth\_ratio":1.0,"num\_dx\_enriched\_keys":0,"num\_dx\_enriched\_alias\_ids":0}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":1.0}'

  \[row=6\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

  \[row=7\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

  \[row=8\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

  \[row=9\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

  \[row=10\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

  \[row=11\]  
    request\_\_cbp:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"slot\_template\_id":89691}'  
      HooverPP (entity=request, network=520311): '{"slot\_template\_id":89691}'  
    request\_\_context:  
      Hoover (entity=request, network=520311): '{"network\_id":520311,"asset\_id":423047900,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","site\_section\_id":17471497,"page\_random":"1711301913584752654","video\_random":"3684049057403737935","asset\_duration":1250.0,"request\_duration":1250.0,"time\_position":0.0,"profile\_id":10056,"ux\_network\_id":520311,"ux\_section\_id":1080218,"ux\_conf\_id":922798,"profile\_concrete\_event\_id":\[32\],"request\_format":1,"response\_format":15,"ab\_test\_item":\[{"collection\_id":42,"bucket\_id":119},{"collection\_id":51,"bucket\_id":138},{"collection\_id":62,"bucket\_id":230},{"collection\_id":65,"bucket\_id":238},{"collection\_id":86,"bucket\_id":288},{"collection\_id":86,"bucket\_id":289},{"collection\_id":86,"bucket\_id":421},{"collection\_id":88,"bucket\_id":499},{"collection\_id":90,"bucket\_id":298},{"collection\_id":134,"bucket\_id":429},{"collection\_id":151,"bucket\_id":471},{"collection\_id":159,"bucket\_id":462},{"collection\_id":174,"bucket\_id":495},{"collection\_id":174,"bucket\_id":496},{"collection\_id":174,"bucket\_id":497},{"collection\_id":175,"bucket\_id":512},{"collection\_id":183,"bucket\_id":521},{"collection\_id":183,"bucket\_id":522},{"collection\_id":185,"bucket\_id":525},{"collection\_id":2007,"bucket\_id":2013},{"collection\_id":2007,"bucket\_id":2014},{"collection\_id":2012,"bucket\_id":2022},{"collection\_id":5413842,"bucket\_id":5414433},{"collection\_id":17191056,"bucket\_id":17191119}\],"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","request\_trace\_id":"b18b328f718dec93e08a82715f2a3a27","rbp\_platform":"OTT","stream\_mode\_id":2,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_genre\_ids":\[2,31\],"content\_form\_id":3,"content\_rating\_id":10,"standard\_language\_ids":\[1\],"ip\_enabled\_audience\_id":2,"standard\_programmer\_id":674,"standard\_endpoint\_owner\_id":59,"standard\_endpoint\_id":243,"website\_root\_id":1080218,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"profile\_trait":{"pre\_selection\_external\_ad\_timeout":1000,"post\_selection\_external\_ad\_timeout":400},"standard\_app\_id":6037,"stream\_mode\_ids":\[2\],"standard\_iab\_category\_ids":\[1,8\],"standard\_content\_territory\_id":165,"standard\_privacy\_id":1,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"video\_cro\_network\_id":520311,"video\_cro\_context\_id":17471497,"video\_cro\_context\_group\_id":-1,"video\_cro\_asset\_id":423047900,"video\_cro\_site\_id":1080218,"video\_cro\_selected\_yield\_optimization\_infos":\[{"sub\_yo\_id":26439,"nested\_sub\_yo\_ids":\[15234\]},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"sub\_yo\_id":46478,"nested\_sub\_yo\_ids":\[15234\]}\],"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_asset\_group\_id":-1,"site\_section\_cro\_site\_id":1080218,"site\_section\_cro\_parsed\_site\_section\_id":17471497,"rbp\_device\_type":"OTT","distributor\_video\_asset\_id":423047900,"distributor\_video\_asset\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_site\_section\_group\_id":-1,"profile\_type":"COMPOUND"}'  
      HooverPP (entity=request, network=520311): '{"ab\_test\_item":\[{"bucket\_id":119,"collection\_id":42},{"bucket\_id":138,"collection\_id":51},{"bucket\_id":230,"collection\_id":62},{"bucket\_id":238,"collection\_id":65},{"bucket\_id":288,"collection\_id":86},{"bucket\_id":289,"collection\_id":86},{"bucket\_id":421,"collection\_id":86},{"bucket\_id":499,"collection\_id":88},{"bucket\_id":298,"collection\_id":90},{"bucket\_id":429,"collection\_id":134},{"bucket\_id":471,"collection\_id":151},{"bucket\_id":462,"collection\_id":159},{"bucket\_id":495,"collection\_id":174},{"bucket\_id":496,"collection\_id":174},{"bucket\_id":497,"collection\_id":174},{"bucket\_id":512,"collection\_id":175},{"bucket\_id":521,"collection\_id":183},{"bucket\_id":522,"collection\_id":183},{"bucket\_id":525,"collection\_id":185},{"bucket\_id":2013,"collection\_id":2007},{"bucket\_id":2014,"collection\_id":2007},{"bucket\_id":2022,"collection\_id":2012},{"bucket\_id":5414433,"collection\_id":5413842},{"bucket\_id":17191119,"collection\_id":17191056}\],"app":{"bundle":"G17292010383","name":"paramount plus","storeurl":"<https://www.samsung.com/us/appstore/app.do?appId=G17292010384>"},"asset\_duration":1250.0,"asset\_id":423047900,"content\_form\_id":3,"content\_rating\_id":10,"custom\_asset\_id":"520311/SwSacjWcFh5rNVnwZ7chvQJxPx7i14v7","distributor\_network\_id":520311,"distributor\_site\_section\_group\_id":-1,"distributor\_site\_section\_id":17471497,"distributor\_video\_asset\_id":423047900,"host\_name":"[7f077.v.fwmrm.net](http://7f077.v.fwmrm.net)","ip\_enabled\_audience\_id":2,"key\_value":\[{"key":"\_fw\_3P\_UID","value":"IDL:Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA,PAIRID:ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD,connectid:ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg,UID2:A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ,VIANTP:1bb3187917473e41ce087da594f9ca8b99f986ac42e98a288c6d010d7adc7bb4,TINUITI:b7ac1ee5a5b05a08935dedb85c9eb2249337f8f59112f667a4f4afcceaf1b60d"},{"key":"\_fw\_content\_language","value":"en"},{"key":"\_fw\_continuous\_play","value":"1"},{"key":"\_fw\_coppa","value":"0"},{"key":"\_fw\_did","value":"tifa:256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"\_fw\_h\_referer"},{"key":"\_fw\_h\_x\_country","value":"us"},{"key":"\_fw\_is\_lat","value":"0"},{"key":"\_fw\_nielsen\_app\_id","value":"P0C0C37AD-20C4-4EF7-AF25-BEBCB16DF85E"},{"key":"\_fw\_player\_height","value":"1080"},{"key":"\_fw\_player\_width","value":"1920"},{"key":"\_fw\_vcid2","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"cadence","value":"monthly"},{"key":"cms","value":"sdr"},{"key":"cpPre","value":"1"},{"key":"cpSession","value":"1"},{"key":"dai-excl","value":"codec:dvh\*"},{"key":"dai-sr","value":"375000:15000000"},{"key":"daiCmsId","value":"2497752"},{"key":"dai\_stream\_activity\_id","value":"9af71e00-3378-4ff3-9ab4-45c5946491f6"},{"key":"device\_region\_language","value":"en"},{"key":"endcard","value":"true"},{"key":"fms\_bididtype","value":"1040,1050,1030,1010,1070,1080"},{"key":"fms\_connectid","value":"ja6PIq1jEfwYbf-oN2SwyyKJAts782a93rpP6B9vSBp3QSNVFnXMYzixLLNHdvqHFq-f4bSD1Nj01xUZM3hEjg"},{"key":"fms\_emailhash","value":"796462c8e3a1d1a195f240a5425d334daeb53862b55a337bc8d4fb8fb0f71e95"},{"key":"fms\_hh\_ramp\_id","value":"UNMATCHED"},{"key":"fms\_ifa","value":"256d72ba-f5a2-6d4b-216b-424cd3f75fbc"},{"key":"fms\_pair","value":"ApIkog36lNF9fBgPpW/ULzAoYqJgZ9DGmkOxhsHO7+KD"},{"key":"fms\_ramp\_envelope","value":"Aox7mS\_nFSBavOIMKGdvfrUELE2Z24DDp1UnRqBPOA1N43vNWqUlskHxblNkrhIQhnGMkRYOEjAN7OUsA63pxbxnvrvou3LW1ewWSnrqcAhjir1-55ML3ZqTky9lvg\_5A64AQkIPlQcIDB4dBys4uKKFPhamsPNlw04YzvWVHGuM7EhAtDERRE\_s2llYKUFIYrD8-00vEOS3A3gGvdPqqumgrpeJOo8illfD8SEWFLLMjAl7Tt0-fll5BZuP7K2ZVdMBj8PnkPbnoiIVqzNrgQBfVBBRoMlhBXbABmmDo1vvDoKjk8vbYw2yNBYA8NmEWUzLGr-qgHtaT2puQS0J91HIido5k-Hqj-BoTPqMaA"},{"key":"fms\_ramp\_id","value":"XY6395clWCgU6YM7dft2iQ0cGex24miLIZmZj9NFdGpoCP\_ZI"},{"key":"fms\_ruleid","value":"10000"},{"key":"fms\_subscriberid","value":"238012554195"},{"key":"fms\_uid2","value":"A4AAADZULd2Ct8DyJMh-0L84lpPK0e0-f0GVoRrAK2l6L0kB-xNY6p9dQiJsfDR4KlOAsOFaH3pSt2llX0A-4LMi3AAfHGxyUX2tCCddAl0GvUb-ZGmQFfe5VIDsLFHcMGF\_ZIVE0zDgIKe5yBK3jqfiC6GzDaB0kj6AcbIVUmAhbJuZKBT-cxA5TyoLZApr9Xm1aSQYqVlo-5ySCWxTZ-iEfQ"},{"key":"fms\_vcid2type","value":"liveramp"},{"key":"ge","value":"0"},{"key":"givn"},{"key":"gr","value":"3"},{"key":"is\_lat","value":"0"},{"key":"language\_selection","value":"en"},{"key":"packageSource","value":"appleitunes"},{"key":"packageType","value":"D2C"},{"key":"playername\_version","value":"@cbsinteractive/avia-js\_2.54.0"},{"key":"profile","value":"107172089661"},{"key":"ptype","value":"video"},{"key":"recommended\_show","value":"956609957"},{"key":"recommended\_show","value":"61456636"},{"key":"recommended\_show","value":"61457137"},{"key":"recommended\_show","value":"61457250"},{"key":"recommended\_show","value":"941630057"},{"key":"recommended\_show","value":"955719957"},{"key":"recommended\_show","value":"651500157"},{"key":"recommended\_show","value":"61459196"},{"key":"recommended\_show","value":"956419957"},{"key":"recommended\_show","value":"941410057"},{"key":"region","value":"us"},{"key":"sb","value":"22"},{"key":"session","value":"b"},{"key":"source","value":"end\_of\_episode"},{"key":"sub","value":"238012554195"},{"key":"sublife","value":"f"},{"key":"subses","value":"1"},{"key":"sz","value":"640x480"},{"key":"tfcd","value":"0"},{"key":"user","value":"ADULT"},{"key":"vendorUserType","value":"null"},{"key":"vguid","value":"2d001a3b-bafc-4f12-8f63-1b8ba0046ce6"}\],"network\_id":520311,"page\_random":"1711301913584752654","profile\_concrete\_event\_id":\[32\],"profile\_id":10056,"profile\_trait":{"post\_selection\_external\_ad\_timeout":400,"pre\_selection\_external\_ad\_timeout":1000},"profile\_type":"COMPOUND","rbp\_device\_type":"OTT","rbp\_platform":"OTT","request\_duration":1250.0,"request\_format":1,"response\_format":15,"site\_section\_cro\_asset\_id":17471497,"site\_section\_cro\_network\_id":520311,"site\_section\_cro\_site\_id":1080218,"site\_section\_id":17471497,"standard\_addressability\_ids":\[4,8,9,10,15,25,27,30,31\],"standard\_app\_id":6037,"standard\_brand\_id":688,"standard\_channel\_id":1457,"standard\_content\_daypart\_id":1,"standard\_content\_series\_id":6234,"standard\_content\_territory\_id":165,"standard\_endpoint\_id":243,"standard\_endpoint\_owner\_id":59,"standard\_genre\_ids":\[2,31\],"standard\_iab\_category\_ids":\[1,8\],"standard\_language\_ids":\[1\],"standard\_privacy\_id":1,"standard\_programmer\_id":674,"stream\_mode\_id":2,"stream\_mode\_ids":\[2\],"time\_position":0.0,"video\_cro\_asset\_id":423047900,"video\_cro\_context\_id":17471497,"video\_cro\_network\_id":520311,"video\_cro\_selected\_yield\_optimization\_infos":\[{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":26439},{"sub\_yo\_id":26704},{"sub\_yo\_id":26705},{"sub\_yo\_id":26706},{"sub\_yo\_id":26707},{"nested\_sub\_yo\_ids":\[15234\],"sub\_yo\_id":46478}\],"video\_cro\_site\_id":1080218,"video\_random":"3684049057403737935"}'  
    request\_\_scores:  
      Hoover (entity=request, network=520311): '\[\\'{"network\_id":520311,"ad\_id":92752962,"flag":514,"score":2214}\\'\]'  
      HooverPP (entity=request, network=520311): '\[\\'{"flag":514,"network\_id":520311,"score":2214}\\'\]'  
    request\_\_time\_record:  
      Hoover (entity=request, network=520311): '{"total":1334,"external\_candidate":1008}'  
      HooverPP (entity=request, network=520311): '{"total":1334}'  
    request\_\_timestamp:  
      Hoover (entity=request, network=520311): '2026-05-30 20:00:00.000'  
      HooverPP (entity=request, network=520311): '1780171200'  
    request\_\_traffic\_compliance:  
      Hoover (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}'  
      HooverPP (entity=request, network=520311): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}'  
    request\_\_userdb\_audience\_user\_info:  
      Hoover (entity=request, network=520311): '{"num\_keys":7,"dx\_alias\_growth\_ratio":2065.0,"bg\_alias\_growth\_ratio":5035.0,"num\_dx\_enriched\_keys":1966,"num\_dx\_enriched\_alias\_ids":958}'  
      HooverPP (entity=request, network=520311): '{"bg\_alias\_growth\_ratio":5035.0}'

```
  END OF REPORT
```

#### Aggregation Validation

##### Aggregate Column: request\_\_context\_\_po\_type

Aggregation Validation SQL  
-- Hoover SQL  
time=28.88s | rows=3  
SELECT request\_\_context\_\_po\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=27.60s | rows=3*  
*SELECT request\_\_context\_\_po\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC  
Aggregate column: request\_\_context\_\_po\_type  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=28.88s | rows=3  
SELECT request\_\_context\_\_po\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=27.60s | rows=3*  
*SELECT request\_\_context\_\_po\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| DISTRIBUTOR | 20486 | 20486 | 0 | MATCH |
| None | 166107 | 166107 | 0 | MATCH |
| PROVIDER | 283 | 283 | 0 | MATCH |

```text
PASS: counts match for all 3 value(s).
Match % (values): 3/3 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

##### Aggregate Column: request\_\_is\_filtered

Aggregation Validation SQL  
-- Hoover SQL  
time=20.56s | rows=2  
SELECT request\_\_is\_filtered, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_is\_filtered ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=43.10s | rows=2*  
*SELECT request\_\_is\_filtered, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY request\_\_is\_filtered ORDER BY cnt DESC  
Aggregate column: request\_\_is\_filtered  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=20.56s | rows=2  
SELECT request\_\_is\_filtered, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_is\_filtered ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=43.10s | rows=2*  
*SELECT request\_\_is\_filtered, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY request\_\_is\_filtered ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| False | 173799 | 173946 | -147 | MISMATCH |
| True | 13077 | 12930 | 147 | MISMATCH |

```text
FAIL: count mismatches for 2 of 2 value(s).
Match % (values): 0/2 (0.00%)
Match % (volume): 186,729/186,876 (99.92%)
```

#### Execution Summary

Total execution time: 3436.75s (57.28m)

### Visitor

Hoover table: ad  
HooverPP view: ad  
Hour: 20260525200000

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=5.76s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=3.50s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: visitor)
========================================================================
  Total columns  — Hoover  : 75
  Total columns  — HooverPP: 62
  Common columns           : 62
  Only in Hoover           : 13
  Only in HooverPP         : 0
  Data-type mismatches     : 0
  Match % (common columns) : 62/75 (82.67%)
  Match % (type on common) : 62/62 (100.00%)
  Match % (overall schema) : 62/75 (82.67%)

  Columns only in Hoover:
    visitor__accept_language  [varchar]
    visitor__flash_version  [varchar]
    visitor__internal_user_id  [varchar]
    visitor__isp  [varchar]
    visitor__original_ip_address  [varchar]
    visitor__ortb_fields_from_ua  [varchar]
    visitor__postal_code_id  [array(integer)]
    visitor__postal_code_package  [array(varchar)]
    visitor__postal_code_package__network_id  [array(integer)]
    visitor__postal_code_package__postal_code_package_id  [array(array(integer))]
    visitor__session_id  [varchar]
    visitor__user_agent_device_id  [bigint]
    visitor__user_group  [array(integer)]

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=42.64s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=105.47s | rows=2  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200092577128', '1779739200923397602') AND advertisement\_\_ad\_id IN (92688537, 93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=83.05s | rows=2  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1779739200092577128', '1779739200923397602') AND advertisement\_\_ad\_id IN (92688537, 93989699)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=visitor, network=169843)
  Source B : HooverPP (entity=visitor, network=169843)
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 63
  Columns B: 63

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (63 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 2/2 (100.00%)
  Column match %    : 63/63 (100.00%)
  Cell/value match %: 126/126 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__identity_user_ids__authorized_network_id            2 row(s)

  ✅ No field-level differences found!
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=33.81s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=398.32s | rows=10  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200492270296', '1779739201841836046') AND advertisement\_\_ad\_id IN (93836193, 93505919, 93551200, 93796331, 93206784, 92856240, 94167753, 92919868, 92966514, 94168572)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=69.84s | rows=10  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1779739200492270296', '1779739201841836046') AND advertisement\_\_ad\_id IN (93836193, 93505919, 93551200, 93796331, 93206784, 92856240, 94167753, 92919868, 92966514, 94168572)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=visitor, network=191701)
  Source B : HooverPP (entity=visitor, network=191701)
  Rows  A  : 10
  Rows  B  : 10
  Columns A: 63
  Columns B: 63

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 10

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (63 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 10/10 (100.00%)
  Column match %    : 63/63 (100.00%)
  Cell/value match %: 630/630 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__identity_user_ids__authorized_network_id            10 row(s)
    visitor__tracked_term                                        5 row(s)

  ✅ No field-level differences found!
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=60.96s | rows=8  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=597.44s | rows=12  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200361036064', '1779739200621079825') AND advertisement\_\_ad\_id IN (94196190, 93731427, 93731428, 94196191, 93936868, 93936869)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=74.63s | rows=12  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1779739200361036064', '1779739200621079825') AND advertisement\_\_ad\_id IN (94196190, 93731427, 93731428, 94196191, 93936868, 93936869)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=visitor, network=384777)
  Source B : HooverPP (entity=visitor, network=384777)
  Rows  A  : 12
  Rows  B  : 12
  Columns A: 63
  Columns B: 63

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 12

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (63 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 12/12 (100.00%)
  Column match %    : 63/63 (100.00%)
  Cell/value match %: 756/756 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__identity_user_ids__authorized_network_id            12 row(s)

  ✅ No field-level differences found!
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=102.40s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=991.73s | rows=2  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200023068880', '1779739200088135550') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=80.14s | rows=2  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1779739200023068880', '1779739200088135550') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=visitor, network=512166)
  Source B : HooverPP (entity=visitor, network=512166)
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 63
  Columns B: 63

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (63 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 2/2 (100.00%)
  Column match %    : 63/63 (100.00%)
  Cell/value match %: 126/126 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__identity_user_ids__authorized_network_id            2 row(s)
    visitor__tracked_term                                        1 row(s)

  ✅ No field-level differences found!
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=33.25s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=138.23s | rows=11  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739201271074723', '1779739202361368064') AND advertisement\_\_ad\_id IN (93881202, 93973877, 92517231, 93833278, 93978490, 93978491, 90939896, 93617711, 93772582, 54224598)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=81.41s | rows=11  
SELECT request\_\_transaction\_id, visitor\_\_active\_state, visitor\_\_address, visitor\_\_app\_bundle\_id, visitor\_\_caller, visitor\_\_city, visitor\_\_city\_id, visitor\_\_cookie\_user\_id, visitor\_\_country, visitor\_\_country\_id, visitor\_\_custom\_user\_id, visitor\_\_device\_id, visitor\_\_device\_type, visitor\_\_dma\_code, visitor\_\_dma\_code\_id, visitor\_\_filtration\_reason, visitor\_\_flags, visitor\_\_household\_id, visitor\_\_identity\_user\_ids, visitor\_\_identity\_user\_ids\_\_authorized\_network\_id, visitor\_\_identity\_user\_ids\_\_id, visitor\_\_identity\_user\_ids\_\_namespace\_id, visitor\_\_internal\_address, visitor\_\_isp\_id, visitor\_\_operator\_zone\_id, visitor\_\_parsed\_user\_agent, visitor\_\_peer\_address, visitor\_\_platform\_browser\_id, visitor\_\_platform\_device\_id, visitor\_\_platform\_group, visitor\_\_platform\_os\_id, visitor\_\_postal\_code, visitor\_\_private\_universal\_hhid, visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_hhid\_\_id, visitor\_\_private\_universal\_iid, visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids, visitor\_\_private\_universal\_iid\_\_id, visitor\_\_programmer\_individual\_id, visitor\_\_referrer, visitor\_\_referrer\_banning\_rule\_id, visitor\_\_server\_side\_user\_id, visitor\_\_standard\_device\_type\_child\_id, visitor\_\_standard\_device\_type\_ids, visitor\_\_standard\_environment\_id, visitor\_\_standard\_manufacturer\_id, visitor\_\_standard\_operator\_id, visitor\_\_standard\_os\_id, visitor\_\_standard\_retailer\_id, visitor\_\_state, visitor\_\_state\_id, visitor\_\_syscode, visitor\_\_timezone, visitor\_\_timezone\_offset, visitor\_\_tracked\_audience\_item\_ids, visitor\_\_tracked\_term, visitor\_\_universal\_hhid, visitor\_\_universal\_iids, visitor\_\_user\_agent, visitor\_\_user\_agent\_device\_type, visitor\_\_user\_id, visitor\_\_user\_segments\_lookup\_key, visitor\_\_xfinity\_idfa FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1779739201271074723', '1779739202361368064') AND advertisement\_\_ad\_id IN (93881202, 93973877, 92517231, 93833278, 93978490, 93978491, 90939896, 93617711, 93772582, 54224598)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=visitor, network=520311)
  Source B : HooverPP (entity=visitor, network=520311)
  Rows  A  : 11
  Rows  B  : 11
  Columns A: 63
  Columns B: 63

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 11

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (63 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 11/11 (100.00%)
  Column match %    : 63/63 (100.00%)
  Cell/value match %: 693/693 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__tracked_term                                        11 row(s)
    visitor__universal_iids                                      11 row(s)
    visitor__identity_user_ids__authorized_network_id            1 row(s)
    visitor__user_segments_lookup_key                            1 row(s)

  ✅ No field-level differences found!
```

#### Aggregation Validation

##### Aggregate Column: visitor\_\_device\_type

Aggregation Validation SQL  
-- Hoover SQL  
time=97.97s | rows=40  
SELECT visitor\_\_device\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_device\_type ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=65.75s | rows=40*  
*SELECT visitor\_\_device\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY visitor\_\_device\_type ORDER BY cnt DESC  
Aggregate column: visitor\_\_device\_type  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=97.97s | rows=40  
SELECT visitor\_\_device\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_device\_type ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=65.75s | rows=40*  
*SELECT visitor\_\_device\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY visitor\_\_device\_type ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| 29136f62-8247-521f-a3d7-4ee802b2f49b | 1 | 1 | 0 | MATCH |
| 7a7516b4-0574-507f-a906-43b46702f2d5 | 1 | 1 | 0 | MATCH |
| 83f8d9fa-e267-5d59-aeca-266ac81c3979 | 1 | 1 | 0 | MATCH |
| 9229ba1e-cac2-58fe-a423-33475908bd1f | 1 | 1 | 0 | MATCH |
| None | 50798 | 50798 | 0 | MATCH |
| a047c6e4-7bae-4c91-adb9-0e36e5c82191 | 1 | 1 | 0 | MATCH |
| aaid | 461 | 461 | 0 | MATCH |
| adid | 70 | 70 | 0 | MATCH |
| afai | 818 | 818 | 0 | MATCH |
| afid | 4 | 4 | 0 | MATCH |
| amazon\_advertising\_id | 14177 | 14177 | 0 | MATCH |
| android\_id | 93 | 93 | 0 | MATCH |
| atv | 1896 | 1896 | 0 | MATCH |
| bdab3460-183a-ea06-787f-d9feb1b38912 | 1 | 1 | 0 | MATCH |
| chtv | 54 | 54 | 0 | MATCH |
| comcastx\_id | 441 | 441 | 0 | MATCH |
| ctv | 1462 | 1462 | 0 | MATCH |
| dpid | 5870 | 5870 | 0 | MATCH |
| gateway | 431 | 431 | 0 | MATCH |
| google\_advertising\_id | 23952 | 23952 | 0 | MATCH |
| idfa | 7717 | 7717 | 0 | MATCH |
| idfv | 886 | 886 | 0 | MATCH |
| ip\_player | 2624 | 2624 | 0 | MATCH |
| lg | 280 | 280 | 0 | MATCH |
| lgudid | 2433 | 2433 | 0 | MATCH |
| ppid | 156 | 156 | 0 | MATCH |
| psn | 196 | 196 | 0 | MATCH |
| rida | 32739 | 32739 | 0 | MATCH |
| roku | 537 | 537 | 0 | MATCH |
| sessionid | 303 | 303 | 0 | MATCH |
| stb | 17458 | 17458 | 0 | MATCH |
| tifa | 11534 | 11534 | 0 | MATCH |
| tvos | 6 | 6 | 0 | MATCH |
| vida | 3600 | 3600 | 0 | MATCH |
| vidaa | 280 | 280 | 0 | MATCH |
| web | 128 | 128 | 0 | MATCH |
| windows\_advertising\_id | 1955 | 1955 | 0 | MATCH |
| wtaid | 55 | 55 | 0 | MATCH |
| xifa | 297 | 297 | 0 | MATCH |
| {{ifa\_type\]\] | 1 | 1 | 0 | MATCH |

```text
PASS: counts match for all 40 value(s).
Match % (values): 40/40 (100.00%)
Match % (volume): 183,718/183,718 (100.00%)
```

##### Aggregate Column: visitor\_\_timezone

Aggregation Validation SQL  
-- Hoover SQL  
time=112.35s | rows=68  
SELECT visitor\_\_timezone, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_timezone ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=68.72s | rows=68*  
*SELECT visitor\_\_timezone, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY visitor\_\_timezone ORDER BY cnt DESC  
Aggregate column: visitor\_\_timezone  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=112.35s | rows=68  
SELECT visitor\_\_timezone, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_timezone ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=68.72s | rows=68*  
*SELECT visitor\_\_timezone, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY visitor\_\_timezone ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| Africa/Dakar | 1 | 1 | 0 | MATCH |
| Africa/Johannesburg | 4 | 4 | 0 | MATCH |
| Africa/Nairobi | 1 | 1 | 0 | MATCH |
| America/Anchorage | 210 | 210 | 0 | MATCH |
| America/Asuncion | 15 | 15 | 0 | MATCH |
| America/Bogota | 239 | 239 | 0 | MATCH |
| America/Caracas | 185 | 185 | 0 | MATCH |
| America/Chicago | 45723 | 45723 | 0 | MATCH |
| America/Chihuahua | 588 | 588 | 0 | MATCH |
| America/Costa\_Rica | 35 | 35 | 0 | MATCH |
| America/Denver | 7209 | 7209 | 0 | MATCH |
| America/Edmonton | 77 | 77 | 0 | MATCH |
| America/El\_Salvador | 15 | 15 | 0 | MATCH |
| America/Guatemala | 7 | 7 | 0 | MATCH |
| America/Guayaquil | 84 | 84 | 0 | MATCH |
| America/Halifax | 55 | 55 | 0 | MATCH |
| America/Indianapolis | 3312 | 3312 | 0 | MATCH |
| America/Jamaica | 1 | 1 | 0 | MATCH |
| America/La\_Paz | 41 | 41 | 0 | MATCH |
| America/Lima | 147 | 147 | 0 | MATCH |
| America/Los\_Angeles | 21242 | 21242 | 0 | MATCH |
| America/Managua | 6 | 6 | 0 | MATCH |
| America/Mendoza | 287 | 287 | 0 | MATCH |
| America/Montevideo | 34 | 34 | 0 | MATCH |
| America/Montreal | 40 | 40 | 0 | MATCH |
| America/New\_York | 76436 | 76436 | 0 | MATCH |
| America/Panama | 20 | 20 | 0 | MATCH |
| America/Phoenix | 2794 | 2794 | 0 | MATCH |
| America/Rainy\_River | 343 | 343 | 0 | MATCH |
| America/Regina | 25 | 25 | 0 | MATCH |
| America/Santo\_Domingo | 20 | 20 | 0 | MATCH |
| America/St\_Johns | 33 | 33 | 0 | MATCH |
| America/Tegucigalpa | 21 | 21 | 0 | MATCH |
| America/Vancouver | 87 | 87 | 0 | MATCH |
| America/Whitehorse | 1 | 1 | 0 | MATCH |
| America/Winnipeg | 23 | 23 | 0 | MATCH |
| Asia/Hong\_Kong | 1 | 1 | 0 | MATCH |
| Asia/Istanbul | 3 | 3 | 0 | MATCH |
| Asia/Manila | 2 | 2 | 0 | MATCH |
| Australia/Canberra | 43 | 43 | 0 | MATCH |
| Australia/NSW | 78 | 78 | 0 | MATCH |
| Australia/Queensland | 69 | 69 | 0 | MATCH |
| Australia/Tasmania | 2 | 2 | 0 | MATCH |
| Australia/Victoria | 105 | 105 | 0 | MATCH |
| Australia/West | 19 | 19 | 0 | MATCH |
| Brazil/Acre | 1543 | 1543 | 0 | MATCH |
| Chile/Continental | 144 | 144 | 0 | MATCH |
| Europe/Amsterdam | 21 | 21 | 0 | MATCH |
| Europe/Berlin | 712 | 712 | 0 | MATCH |
| Europe/Brussels | 128 | 128 | 0 | MATCH |
| Europe/Bucharest | 17 | 17 | 0 | MATCH |
| Europe/Copenhagen | 59 | 59 | 0 | MATCH |
| Europe/Dublin | 112 | 112 | 0 | MATCH |
| Europe/Helsinki | 121 | 121 | 0 | MATCH |
| Europe/London | 6834 | 6834 | 0 | MATCH |
| Europe/Madrid | 541 | 541 | 0 | MATCH |
| Europe/Oslo | 35 | 35 | 0 | MATCH |
| Europe/Paris | 3309 | 3309 | 0 | MATCH |
| Europe/Rome | 307 | 307 | 0 | MATCH |
| Europe/Stockholm | 250 | 250 | 0 | MATCH |
| Europe/Tallinn | 1 | 1 | 0 | MATCH |
| Europe/Vienna | 98 | 98 | 0 | MATCH |
| Europe/Warsaw | 39 | 39 | 0 | MATCH |
| Europe/Zurich | 16 | 16 | 0 | MATCH |
| None | 9446 | 9446 | 0 | MATCH |
| Pacific/Auckland | 1 | 1 | 0 | MATCH |
| Pacific/Guam | 1 | 1 | 0 | MATCH |
| Pacific/Honolulu | 300 | 300 | 0 | MATCH |

```text
PASS: counts match for all 68 value(s).
Match % (values): 68/68 (100.00%)
Match % (volume): 183,718/183,718 (100.00%)
```

#### Execution Summary

Total execution time: 3346.14s (55.77m)

### Slot

Hoover table: ad  
HooverPP view: ad  
Hour: 20260525200000

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=5.09s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=3.48s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: slot)
========================================================================
  Total columns  — Hoover  : 98
  Total columns  — HooverPP: 39
  Common columns           : 39
  Only in Hoover           : 59
  Only in HooverPP         : 0
  Data-type mismatches     : 0
  Match % (common columns) : 39/98 (39.80%)
  Match % (type on common) : 39/39 (100.00%)
  Match % (overall schema) : 39/98 (39.80%)

  Columns only in Hoover:
    slot__ad_units  [varchar]
    slot__carriage_inventory_owner_id  [bigint]
    slot__carriage_listing_split_unit_id  [bigint]
    slot__compatible_dimensions  [varchar]
    slot__content_right_owner  [bigint]
    slot__content_type  [array(integer)]
    slot__content_type_id  [integer]
    slot__creative_api  [array(bigint)]
    slot__cue_point_sequence  [integer]
    slot__custom_id  [varchar]
    slot__eligible_carriage_listing_split_unit_ids  [array(bigint)]
    slot__forecast_avails_metrics  [varchar]
    slot__forecast_avails_metrics__booked_avails_with_forecast_factor  [integer]
    slot__forecast_avails_metrics__remaining_avails  [integer]
    slot__forecast_avails_metrics__remaining_avails_with_forecast_factor  [integer]
    slot__forecast_avails_metrics__total_avails_with_forecast_factor  [integer]
    slot__guaranteed_flags  [bigint]
    slot__height  [integer]
    slot__inbound_rule  [array(varchar)]
    slot__inbound_rule__network_id  [array(bigint)]
    slot__inbound_rule__win_inbound_rule_id  [array(array(bigint))]
    slot__inventory_mask  [bigint]
    slot__listing_id  [array(bigint)]
    slot__market_avails  [integer]
    slot__max_bitrate  [integer]
    slot__min_bitrate  [integer]
    slot__network_execution_ctx_index  [integer]
    slot__original_ad_unit  [varchar]
    slot__original_max_ads  [integer]
    slot__outbound_order  [array(varchar)]
    slot__outbound_order__active_aim_audience_ids  [array(array(integer))]
    slot__outbound_order__aim_audience_targeting_expression  [array(varchar)]
    slot__outbound_order__down_reseller_index  [array(integer)]
    slot__outbound_order__effective_exclude_aim_audience_ids  [array(array(integer))]
    slot__outbound_order__listing_id  [array(array(bigint))]
    slot__outbound_order__order_id  [array(bigint)]
    slot__outbound_order__order_priority  [array(varchar)]
    slot__outbound_order__order_transaction_type  [array(varchar)]
    slot__outbound_order__order_type  [array(varchar)]
    slot__outbound_order__price  [array(double)]
    slot__outbound_order__unified_priority  [array(varchar)]
    slot__outbound_order__unified_priority__priority_tier  [array(varchar)]
    slot__outbound_order__unified_priority__sub_priority_value  [array(integer)]
    slot__primary_content_type  [array(integer)]
    slot__raw_max_ads  [integer]
    slot__raw_max_duration  [integer]
    slot__rules  [array(varchar)]
    slot__rules__network_id  [array(bigint)]
    slot__rules__opp_rule_id  [array(array(bigint))]
    slot__rules__win_rule_id  [array(array(bigint))]
    slot__scheduled_timestamp  [bigint]
    slot__sfx_avails  [integer]
    slot__slot_context  [array(varchar)]
    slot__slot_context__network_ctx_index  [array(integer)]
    slot__slot_context__network_execution_ctx_index  [array(integer)]
    slot__time_position_sequence  [varchar]
    slot__width  [integer]
    slot__window_duration  [integer]
    slot__window_start_timestamp  [bigint]

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=41.36s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=56.00s | rows=2  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200092577128', '1779739200923397602') AND advertisement\_\_ad\_id IN (92688537, 93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=75.81s | rows=2  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1779739200092577128', '1779739200923397602') AND advertisement\_\_ad\_id IN (92688537, 93989699)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=slot, network=169843)
  Source B : HooverPP (entity=slot, network=169843)
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 40
  Columns B: 40

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (40 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 2/2 (100.00%)
  Column match %    : 40/40 (100.00%)
  Cell/value match %: 80/80 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=28.56s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=88.17s | rows=10  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200492270296', '1779739201841836046') AND advertisement\_\_ad\_id IN (93505919, 93796331, 93206784, 93551200, 93836193, 94168572, 92966514, 93980386, 94167753, 92856240)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=75.01s | rows=10  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1779739200492270296', '1779739201841836046') AND advertisement\_\_ad\_id IN (93505919, 93796331, 93206784, 93551200, 93836193, 94168572, 92966514, 93980386, 94167753, 92856240)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=slot, network=191701)
  Source B : HooverPP (entity=slot, network=191701)
  Rows  A  : 10
  Rows  B  : 10
  Columns A: 40
  Columns B: 40

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 10

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (40 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 10/10 (100.00%)
  Column match %    : 40/40 (100.00%)
  Cell/value match %: 400/400 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=61.13s | rows=8  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=165.98s | rows=12  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200361036064', '1779739200621079825') AND advertisement\_\_ad\_id IN (94196191, 93731427, 93731428, 94196190, 93936868, 93936869)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=81.41s | rows=12  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1779739200361036064', '1779739200621079825') AND advertisement\_\_ad\_id IN (94196191, 93731427, 93731428, 94196190, 93936868, 93936869)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=slot, network=384777)
  Source B : HooverPP (entity=slot, network=384777)
  Rows  A  : 12
  Rows  B  : 12
  Columns A: 40
  Columns B: 40

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 12

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (40 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 12/12 (100.00%)
  Column match %    : 40/40 (100.00%)
  Cell/value match %: 480/480 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=100.54s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=233.13s | rows=2  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739200023068880', '1779739200088135550') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=80.30s | rows=2  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1779739200023068880', '1779739200088135550') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=slot, network=512166)
  Source B : HooverPP (entity=slot, network=512166)
  Rows  A  : 2
  Rows  B  : 2
  Columns A: 40
  Columns B: 40

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 2

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (40 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 2/2 (100.00%)
  Column match %    : 40/40 (100.00%)
  Cell/value match %: 80/80 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=26.25s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=57.01s | rows=11  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1779739201271074723', '1779739202361368064') AND advertisement\_\_ad\_id IN (93772582, 93617711, 93978491, 92517231, 93973877, 93978490, 93881202, 93833278, 90939896, 54224598)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=84.07s | rows=11  
SELECT request\_\_transaction\_id, slot\_\_ad\_unit\_default\_duration, slot\_\_ad\_unit\_id, slot\_\_ad\_unit\_network\_id, slot\_\_avail\_type, slot\_\_avails, slot\_\_avails\_metrics, slot\_\_avails\_metrics\_\_avails, slot\_\_avails\_metrics\_\_default\_duration, slot\_\_avails\_metrics\_\_opportunity, slot\_\_avails\_metrics\_\_unfilled\_avails, slot\_\_break\_display\_id, slot\_\_break\_id, slot\_\_carriage\_listing\_origin\_split\_unit\_num, slot\_\_carriage\_listing\_split\_unit\_num, slot\_\_environment, slot\_\_flags, slot\_\_index, slot\_\_initial\_num\_ads, slot\_\_initial\_time\_unfilled, slot\_\_initial\_unfilled\_avails, slot\_\_max\_ad\_duration, slot\_\_max\_ads, slot\_\_max\_duration, slot\_\_min\_duration, slot\_\_normalized\_ad\_unit\_id, slot\_\_num\_ads, slot\_\_opportunity\_display\_id, slot\_\_opportunity\_id, slot\_\_parent\_time\_unfilled, slot\_\_profile\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id, slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num, slot\_\_sequence, slot\_\_slot\_sequence, slot\_\_time\_position, slot\_\_time\_position\_class, slot\_\_time\_unfilled, slot\_\_unfilled\_avails FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1779739201271074723', '1779739202361368064') AND advertisement\_\_ad\_id IN (93772582, 93617711, 93978491, 92517231, 93973877, 93978490, 93881202, 93833278, 90939896, 54224598)) ORDER BY request\_\_transaction\_id

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  EVENT-LEVEL CSV COMPARISON REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Source A : Hoover (entity=slot, network=520311)
  Source B : HooverPP (entity=slot, network=520311)
  Rows  A  : 11
  Rows  B  : 11
  Columns A: 40
  Columns B: 40

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 11

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (40 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────

── [3a] UNIQUE KEY CHECK (request__transaction_id) ──────────────────────────────
  ✅ All request__transaction_id values match between files — rows correspond to the same events.

── [M] MATCH PERCENTAGE SUMMARY ────────────────────────────────────
  Row match %       : 11/11 (100.00%)
  Column match %    : 40/40 (100.00%)
  Cell/value match %: 440/440 (100.00%)

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!
```

#### Aggregation Validation

##### Aggregate Column: slot\_\_avail\_type

Aggregation Validation SQL  
-- Hoover SQL  
time=105.44s | rows=3  
SELECT slot\_\_avail\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_avail\_type ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=69.63s | rows=3*  
*SELECT slot\_\_avail\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY slot\_\_avail\_type ORDER BY cnt DESC  
Aggregate column: slot\_\_avail\_type  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=105.44s | rows=3  
SELECT slot\_\_avail\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_avail\_type ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=69.63s | rows=3*  
*SELECT slot\_\_avail\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY slot\_\_avail\_type ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| ADDRESSABLE\_SPLIT\_AVAIL | 4650 | 4650 | 0 | MATCH |
| NON\_ADDRESSABLE | 15893 | 15893 | 0 | MATCH |
| None | 163175 | 163175 | 0 | MATCH |

```text
PASS: counts match for all 3 value(s).
Match % (values): 3/3 (100.00%)
Match % (volume): 183,718/183,718 (100.00%)
```

##### Aggregate Column: slot\_\_max\_ad\_duration

Aggregation Validation SQL  
-- Hoover SQL  
time=99.30s | rows=84  
SELECT slot\_\_max\_ad\_duration, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_max\_ad\_duration ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=66.38s | rows=84*  
*SELECT slot\_\_max\_ad\_duration, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY slot\_\_max\_ad\_duration ORDER BY cnt DESC  
Aggregate column: slot\_\_max\_ad\_duration  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=99.30s | rows=84  
SELECT slot\_\_max\_ad\_duration, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_max\_ad\_duration ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=66.38s | rows=84*  
*SELECT slot\_\_max\_ad\_duration, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-25 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260525190000','20260525200000','20260525210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY slot\_\_max\_ad\_duration ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| -1 | 4454 | 4454 | 0 | MATCH |
| 0 | 37 | 37 | 0 | MATCH |
| 10 | 869 | 869 | 0 | MATCH |
| 100 | 14 | 14 | 0 | MATCH |
| 1000 | 60 | 60 | 0 | MATCH |
| 10000 | 2 | 2 | 0 | MATCH |
| 105 | 18162 | 18162 | 0 | MATCH |
| 106 | 1 | 1 | 0 | MATCH |
| 11 | 326 | 326 | 0 | MATCH |
| 110 | 14 | 14 | 0 | MATCH |
| 112 | 7 | 7 | 0 | MATCH |
| 12 | 18 | 18 | 0 | MATCH |
| 120 | 44093 | 44093 | 0 | MATCH |
| 121 | 552 | 552 | 0 | MATCH |
| 122 | 391 | 391 | 0 | MATCH |
| 123 | 270 | 270 | 0 | MATCH |
| 124 | 4 | 4 | 0 | MATCH |
| 125 | 25 | 25 | 0 | MATCH |
| 135 | 254 | 254 | 0 | MATCH |
| 15 | 1300 | 1300 | 0 | MATCH |
| 150 | 3927 | 3927 | 0 | MATCH |
| 157 | 4 | 4 | 0 | MATCH |
| 16 | 166 | 166 | 0 | MATCH |
| 160 | 1 | 1 | 0 | MATCH |
| 162 | 1 | 1 | 0 | MATCH |
| 165 | 312 | 312 | 0 | MATCH |
| 17 | 72 | 72 | 0 | MATCH |
| 180 | 6140 | 6140 | 0 | MATCH |
| 182 | 579 | 579 | 0 | MATCH |
| 183 | 5879 | 5879 | 0 | MATCH |
| 185 | 337 | 337 | 0 | MATCH |
| 19 | 1 | 1 | 0 | MATCH |
| 190 | 225 | 225 | 0 | MATCH |
| 195 | 459 | 459 | 0 | MATCH |
| 20 | 1100 | 1100 | 0 | MATCH |
| 200 | 1243 | 1243 | 0 | MATCH |
| 21 | 63 | 63 | 0 | MATCH |
| 210 | 1819 | 1819 | 0 | MATCH |
| 213 | 639 | 639 | 0 | MATCH |
| 22 | 2 | 2 | 0 | MATCH |
| 225 | 599 | 599 | 0 | MATCH |
| 240 | 158 | 158 | 0 | MATCH |
| 255 | 11933 | 11933 | 0 | MATCH |
| 30 | 10986 | 10986 | 0 | MATCH |
| 300 | 51 | 51 | 0 | MATCH |
| 30000 | 7 | 7 | 0 | MATCH |
| 31 | 4981 | 4981 | 0 | MATCH |
| 32 | 443 | 443 | 0 | MATCH |
| 33 | 9 | 9 | 0 | MATCH |
| 35 | 274 | 274 | 0 | MATCH |
| 36 | 3 | 3 | 0 | MATCH |
| 3600 | 83 | 83 | 0 | MATCH |
| 37 | 5 | 5 | 0 | MATCH |
| 40 | 28 | 28 | 0 | MATCH |
| 45 | 18 | 18 | 0 | MATCH |
| 450 | 292 | 292 | 0 | MATCH |
| 46 | 9 | 9 | 0 | MATCH |
| 47 | 2 | 2 | 0 | MATCH |
| 49000 | 1 | 1 | 0 | MATCH |
| 5 | 761 | 761 | 0 | MATCH |
| 50 | 2 | 2 | 0 | MATCH |
| 6 | 211 | 211 | 0 | MATCH |
| 60 | 7960 | 7960 | 0 | MATCH |
| 61 | 11809 | 11809 | 0 | MATCH |
| 62 | 2584 | 2584 | 0 | MATCH |
| 65 | 26 | 26 | 0 | MATCH |
| 67 | 6 | 6 | 0 | MATCH |
| 7 | 3498 | 3498 | 0 | MATCH |
| 70 | 52 | 52 | 0 | MATCH |
| 75 | 166 | 166 | 0 | MATCH |
| 77 | 87 | 87 | 0 | MATCH |
| 8 | 12 | 12 | 0 | MATCH |
| 80 | 99 | 99 | 0 | MATCH |
| 82 | 1 | 1 | 0 | MATCH |
| 86400 | 40 | 40 | 0 | MATCH |
| 89 | 121 | 121 | 0 | MATCH |
| 9 | 930 | 930 | 0 | MATCH |
| 90 | 3360 | 3360 | 0 | MATCH |
| 91 | 9846 | 9846 | 0 | MATCH |
| 92 | 12682 | 12682 | 0 | MATCH |
| 93 | 442 | 442 | 0 | MATCH |
| 94 | 1 | 1 | 0 | MATCH |
| 999 | 89 | 89 | 0 | MATCH |
| None | 5229 | 5229 | 0 | MATCH |

```text
PASS: counts match for all 84 value(s).
Match % (values): 84/84 (100.00%)
Match % (volume): 183,718/183,718 (100.00%)
```

#### Execution Summary

Total execution time: 1726.05s (28.77m)

### Candidate

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=6.63s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=4.51s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: candidate)
========================================================================
  Total columns  — Hoover  : 110
  Total columns  — HooverPP: 68
  Common columns           : 67
  Only in Hoover           : 43
  Only in HooverPP         : 1
  Data-type mismatches     : 0
  Match % (common columns) : 67/111 (60.36%)
  Match % (type on common) : 67/67 (100.00%)
  Match % (overall schema) : 67/111 (60.36%)

  Columns only in Hoover:
    candidate__ad_replica_id  [integer]
    candidate__advertiser_domain  [varchar]
    candidate__auction_network_execution_ctx_index  [integer]
    candidate__auction_outbound_listing_id  [array(bigint)]
    candidate__bid_replica_id  [integer]
    candidate__bsi_id  [integer]
    candidate__candidate_network_to_auction_seller_network_exchange_rate  [double]
    candidate__cch_key  [varchar]
    candidate__cch_key_domain_config_id  [integer]
    candidate__content_type  [varchar]
    candidate__creative_approval_request  [array(varchar)]
    candidate__creative_approval_request__approval_scope  [array(varchar)]
    candidate__creative_approval_request__approval_type  [array(varchar)]
    candidate__creative_approval_request__network_id  [array(bigint)]
    candidate__domain  [varchar]
    candidate__domain_chain  [array(varchar)]
    candidate__duration  [integer]
    candidate__exchange_order_id  [bigint]
    candidate__external_ad_id_domain_config_id  [integer]
    candidate__external_network_id  [bigint]
    candidate__flags  [bigint]
    candidate__has_advertisement  [boolean]
    candidate__has_auction  [boolean]
    candidate__internal_group_deal_id  [bigint]
    candidate__mbd_deduction_on_selection_ratio  [double]
    candidate__mpe_deduction_on_selection_fixed_fee  [double]
    candidate__network_execution_ctx_index  [integer]
    candidate__order_id  [bigint]
    candidate__playlist_response_time  [integer]
    candidate__pod_replica_id  [integer]
    candidate__price  [double]
    candidate__price_type  [varchar]
    candidate__profile_check_passed  [boolean]
    candidate__redirect_count  [integer]
    candidate__response_industry  [array(bigint)]
    candidate__response_time  [integer]
    candidate__response_time_first_hop  [integer]
    candidate__rtb_impression_id  [varchar]
    candidate__rtb_impression_index  [integer]
    candidate__rtb_impression_slot_index  [integer]
    candidate__trust_id  [varchar]
    candidate__two_phase_translated  [boolean]
    candidate__zone_id  [integer]

  Columns only in HooverPP:
    candidate__market_integration_type  [varchar]

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=38.97s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=73.27s | rows=2  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=84.07s | rows=2  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=candidate, network=169843)  
  Source B : HooverPP (entity=candidate, network=169843)  
  Rows  A  : 2  
  Rows  B  : 2  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 2

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 2/2 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 136/136 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=29.03s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=83.69s | rows=15  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93185984, 92676151, 93340683, 93415904, 93418034, 93415975, 92922663, 92870642, 92398093, 93010669)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=67.02s | rows=15  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93185984, 92676151, 93340683, 93415904, 93418034, 93415975, 92922663, 92870642, 92398093, 93010669)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=candidate, network=191701)  
  Source B : HooverPP (entity=candidate, network=191701)  
  Rows  A  : 15  
  Rows  B  : 15  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 15

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 15/15 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 1,020/1,020 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=59.95s | rows=3  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=160.19s | rows=4  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=68.65s | rows=4  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=candidate, network=384777)  
  Source B : HooverPP (entity=candidate, network=384777)  
  Rows  A  : 4  
  Rows  B  : 4  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 4

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 4/4 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 272/272 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=107.99s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=269.50s | rows=6  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=71.44s | rows=6  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=candidate, network=512166)  
  Source B : HooverPP (entity=candidate, network=512166)  
  Rows  A  : 6  
  Rows  B  : 6  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 6

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 2/6 (33.33%)
  Column match %    : 67/68 (98.53%)
  Cell/value match %: 404/408 (99.02%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
candidate__ortb_fwpartners                                   6 row(s)
candidate__ortb_fwpartners__idtype                           6 row(s)
candidate__ortb_fwpartners__idvalue                          6 row(s)
candidate__advertisement_index                               2 row(s)
candidate__filter_reason                                     2 row(s)
candidate__filter_reason__error                              2 row(s)
candidate__filter_reason__error_category                     2 row(s)
candidate__filter_reason__slot_index                         2 row(s)
candidate__global_agency_ids                                 1 row(s)
```

  ❌ 4 row(s) have differences:

  Column diff summary (sorted by frequency):  
    candidate\_\_advertisement\_index                               4 row(s)

  Detailed diffs:

  \[row=4\]  
    candidate\_\_advertisement\_index:  
      Hoover (entity=candidate, network=512166): '1'  
      HooverPP (entity=candidate, network=512166): ''

  \[row=5\]  
    candidate\_\_advertisement\_index:  
      Hoover (entity=candidate, network=512166): '2'  
      HooverPP (entity=candidate, network=512166): ''

  \[row=6\]  
    candidate\_\_advertisement\_index:  
      Hoover (entity=candidate, network=512166): '3'  
      HooverPP (entity=candidate, network=512166): ''

  \[row=7\]  
    candidate\_\_advertisement\_index:  
      Hoover (entity=candidate, network=512166): '4'  
      HooverPP (entity=candidate, network=512166): ''

```
  END OF REPORT
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=31.16s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=73.50s | rows=10  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (87143704, 90366976, 94243247, 88990076, 92692770, 92934849, 92900021, 93914607, 92933270, 93743083)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=72.49s | rows=10  
SELECT request\_\_transaction\_id, candidate\_\_ad\_id, candidate\_\_advertisement\_index, candidate\_\_advertiser\_id, candidate\_\_asset\_id, candidate\_\_auction\_outbound\_bid\_floor, candidate\_\_auction\_type, candidate\_\_bid\_status, candidate\_\_bidding\_buyer\_id, candidate\_\_bidding\_seat\_id, candidate\_\_bit\_flags, candidate\_\_brand\_id, candidate\_\_buyer\_group\_id, candidate\_\_buyer\_id, candidate\_\_buyer\_platform\_id, candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate, candidate\_\_clearing\_price, candidate\_\_clock\_number, candidate\_\_deal\_id, candidate\_\_deal\_type, candidate\_\_discount\_barter, candidate\_\_discount\_barter\_\_amount, candidate\_\_discount\_barter\_\_id, candidate\_\_discount\_post\_auction, candidate\_\_discount\_post\_auction\_\_amount, candidate\_\_discount\_post\_auction\_\_id, candidate\_\_dsp\_adid, candidate\_\_dsp\_cid, candidate\_\_dsp\_clearing\_price, candidate\_\_dsp\_clearing\_price\_discounted, candidate\_\_dsp\_crid, candidate\_\_dsp\_currency\_id, candidate\_\_dsp\_id, candidate\_\_error, candidate\_\_external\_ad\_id, candidate\_\_external\_seat\_id, candidate\_\_filter\_reason, candidate\_\_filter\_reason\_\_error, candidate\_\_filter\_reason\_\_error\_category, candidate\_\_filter\_reason\_\_slot\_index, candidate\_\_global\_advertiser\_ids, candidate\_\_global\_agency\_ids, candidate\_\_global\_brand\_ids, candidate\_\_global\_industry\_ids, candidate\_\_integration\_type, candidate\_\_internal\_deal\_id, candidate\_\_internal\_seat\_id, candidate\_\_market\_ad\_id, candidate\_\_media\_buyer\_id, candidate\_\_network\_id, candidate\_\_original\_price, candidate\_\_ortb\_fwpartners, candidate\_\_ortb\_fwpartners\_\_idtype, candidate\_\_ortb\_fwpartners\_\_idvalue, candidate\_\_post\_auction\_discount\_id, candidate\_\_raw\_price, candidate\_\_rtb\_auction\_index, candidate\_\_series\_id, candidate\_\_sfx\_buyer\_id, candidate\_\_sfx\_dsp\_id, candidate\_\_site\_id, candidate\_\_site\_section\_id, candidate\_\_trading\_desk\_id, candidate\_\_unified\_deal\_priority, candidate\_\_unified\_deal\_priority\_\_priority\_tier, candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value, candidate\_\_universal\_ad\_id, candidate\_\_vast\_creative\_id FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (87143704, 90366976, 94243247, 88990076, 92692770, 92934849, 92900021, 93914607, 92933270, 93743083)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=candidate, network=520311)  
  Source B : HooverPP (entity=candidate, network=520311)  
  Rows  A  : 10  
  Rows  B  : 10  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 10

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 10/10 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 680/680 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

#### Aggregation Validation

##### Aggregate Column: candidate\_\_deal\_type

Aggregation Validation SQL  
-- Hoover SQL  
time=100.78s | rows=6  
SELECT candidate\_\_deal\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_deal\_type ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=41.21s | rows=6*  
*SELECT candidate\_\_deal\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY candidate\_\_deal\_type ORDER BY cnt DESC  
Aggregate column: candidate\_\_deal\_type  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=100.78s | rows=6  
SELECT candidate\_\_deal\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_deal\_type ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=41.21s | rows=6*  
*SELECT candidate\_\_deal\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY candidate\_\_deal\_type ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| BACKFILL\_DEAL | 60 | 60 | 0 | MATCH |
| BIDDABLE\_GUARANTEED\_DEAL | 3118 | 3118 | 0 | MATCH |
| DEAL | 7247 | 7247 | 0 | MATCH |
| FIRST\_LOOK\_DEAL | 1252 | 1252 | 0 | MATCH |
| None | 161459 | 161459 | 0 | MATCH |
| PROGRAMMATIC\_GUARANTEED\_TRADING\_DESK\_DEAL | 13740 | 13740 | 0 | MATCH |

```text
PASS: counts match for all 6 value(s).
Match % (values): 6/6 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

##### Aggregate Column: candidate\_\_error

Aggregation Validation SQL  
-- Hoover SQL  
time=106.86s | rows=15  
SELECT candidate\_\_error, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_error ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=52.45s | rows=15*  
*SELECT candidate\_\_error, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY candidate\_\_error ORDER BY cnt DESC  
Aggregate column: candidate\_\_error  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=106.86s | rows=15  
SELECT candidate\_\_error, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_error ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=52.45s | rows=15*  
*SELECT candidate\_\_error, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY candidate\_\_error ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| AD\_PENDING\_APPROVAL | 3 | 3 | 0 | MATCH |
| CLIENT\_RENDITION\_REQUIRED | 10 | 10 | 0 | MATCH |
| COMPETITION\_FAILURE | 721 | 721 | 0 | MATCH |
| COMPLIANCE\_NOT\_APPROVED | 121 | 121 | 0 | MATCH |
| EMPTY\_RESPONSE | 1 | 1 | 0 | MATCH |
| EXTERNAL\_CREATIVE\_PROFILE\_CHECK\_FAILED | 9 | 9 | 0 | MATCH |
| FLOOR\_PRICE\_NOTMET | 586 | 586 | 0 | MATCH |
| HTTP\_ERROR | 5 | 5 | 0 | MATCH |
| NO\_BIDS | 7017 | 7017 | 0 | MATCH |
| NO\_VALID\_CREATIVE | 46 | 46 | 0 | MATCH |
| None | 178270 | 178270 | 0 | MATCH |
| PROFILE\_CHECK\_FAILED | 1 | 1 | 0 | MATCH |
| TIMEOUT | 41 | 41 | 0 | MATCH |
| UNEXPECTED\_EXTERNAL\_AD\_ID | 6 | 6 | 0 | MATCH |
| WRAPPER\_TIMEOUT | 39 | 39 | 0 | MATCH |

```text
PASS: counts match for all 15 value(s).
Match % (values): 15/15 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

#### Execution Summary

Total execution time: 1715.62s (28.59m)

### Auction

Hoover table: ad  
HooverPP view: ad  
Hour: 20260530200000

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=6.02s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=3.75s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: auction)
========================================================================
  Total columns  — Hoover  : 115
  Total columns  — HooverPP: 68
  Common columns           : 67
  Only in Hoover           : 48
  Only in HooverPP         : 1
  Data-type mismatches     : 0
  Match % (common columns) : 67/116 (57.76%)
  Match % (type on common) : 67/67 (100.00%)
  Match % (overall schema) : 67/116 (57.76%)

  Columns only in Hoover:
    auction__ab_test_item_index  [array(integer)]
    auction__ab_test_items  [array(varchar)]
    auction__ab_test_items__bucket_id  [array(integer)]
    auction__ab_test_items__collection_id  [array(integer)]
    auction__ab_test_items__is_effective  [array(boolean)]
    auction__app_storeurl  [varchar]
    auction__auction_network_context_index  [integer]
    auction__bid_request_count  [bigint]
    auction__bid_throttling_info__exempt_thousandth  [integer]
    auction__bid_to_eur_exchange_rate  [double]
    auction__buyer_id  [array(bigint)]
    auction__buyer_platform_url_id  [bigint]
    auction__dynamic_floor_price_algorithm  [varchar]
    auction__error  [varchar]
    auction__execution_contexts  [array(varchar)]
    auction__execution_contexts__network_execution_ctx_index  [array(integer)]
    auction__execution_node_id  [bigint]
    auction__experiment  [array(varchar)]
    auction__experiment__experiment_id  [array(integer)]
    auction__external_network_id  [bigint]
    auction__extra_flags  [integer]
    auction__height  [integer]
    auction__ifa_type  [varchar]
    auction__index  [integer]
    auction__internal_seat_id  [array(bigint)]
    auction__is_exchange_auction  [boolean]
    auction__is_faked_auction  [boolean]
    auction__is_market_auction  [boolean]
    auction__is_order_prog_auction  [boolean]
    auction__is_ssp_auction  [boolean]
    auction__market_integration_type  [varchar]
    auction__media_buyer_id  [array(bigint)]
    auction__metadata_auditing_flags  [bigint]
    auction__network_execution_ctx_index  [integer]
    auction__privacy_flags  [integer]
    auction__response_time  [integer]
    auction__supply_chain  [varchar]
    auction__supply_chain__complete  [boolean]
    auction__supply_chain__nodes  [array(varchar)]
    auction__supply_chain__nodes__asi  [array(varchar)]
    auction__supply_chain__nodes__domain  [array(varchar)]
    auction__supply_chain__nodes__hp  [array(integer)]
    auction__supply_chain__nodes__name  [array(varchar)]
    auction__supply_chain__nodes__rid  [array(varchar)]
    auction__supply_chain__nodes__sid  [array(varchar)]
    auction__supply_chain__ver  [varchar]
    auction__trading_desk_id  [array(bigint)]
    auction__width  [integer]

  Columns only in HooverPP:
    auction__auction_network_execution_ctx_index  [integer]

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=23.60s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=158.81s | rows=2  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=141.44s | rows=2  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=auction, network=169843)  
  Source B : HooverPP (entity=auction, network=169843)  
  Rows  A  : 2  
  Rows  B  : 2  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 2

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 2/2 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 136/136 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=20.53s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=241.98s | rows=15  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415975, 92676151, 93415904, 93418034, 93340683, 93185984, 93093201, 92700205, 92874299, 93115000)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=212.81s | rows=15  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415975, 92676151, 93415904, 93418034, 93340683, 93185984, 93093201, 92700205, 92874299, 93115000)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=auction, network=191701)  
  Source B : HooverPP (entity=auction, network=191701)  
  Rows  A  : 15  
  Rows  B  : 15  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 15

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 15/15 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 1,020/1,020 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=43.42s | rows=3  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=362.87s | rows=4  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=49.91s | rows=4  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=auction, network=384777)  
  Source B : HooverPP (entity=auction, network=384777)  
  Rows  A  : 4  
  Rows  B  : 4  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 4

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 4/4 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 272/272 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=44.81s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=520.61s | rows=6  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=58.98s | rows=6  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=auction, network=512166)  
  Source B : HooverPP (entity=auction, network=512166)  
  Rows  A  : 6  
  Rows  B  : 6  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 6

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/6 (0.00%)
  Column match %    : 66/68 (97.06%)
  Cell/value match %: 396/408 (97.06%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
auction__bid_throttling_info__model_info                     6 row(s)
auction__bid_throttling_info__model_info__model_flags        6 row(s)
auction__bid_throttling_info__model_info__model_id           6 row(s)
auction__impression__deals__matched_inventory_package_ids    6 row(s)
auction__impression__deals__media_buyer_id                   6 row(s)
auction__impression__deals__trading_desk_id                  6 row(s)
auction__mkpl_partner_tags                                   6 row(s)
auction__mkpl_partner_tags__network_execution_ctx_index      6 row(s)
auction__mkpl_partner_tags__strategy                         6 row(s)
```

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):  
    auction\_\_bid\_request\_id                                      6 row(s)  
    auction\_\_invite\_deal\_size                                    6 row(s)

  Detailed diffs:

  \[row=2\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'o1179-1780171200055030888-3-523319-midroll\_1-24'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '74'  
      HooverPP (entity=auction, network=512166): ''

  \[row=3\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'es31b5-1780171200408852200-3-523319-midroll\_2-1'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '63'  
      HooverPP (entity=auction, network=512166): ''

  \[row=4\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'es31b5-1780171200408852200-3-523319-midroll\_5-4'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '63'  
      HooverPP (entity=auction, network=512166): ''

  \[row=5\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'es31b5-1780171200408852200-3-523319-midroll\_3-2'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '63'  
      HooverPP (entity=auction, network=512166): ''

  \[row=6\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'es31b5-1780171200408852200-3-523319-midroll\_1-5'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '63'  
      HooverPP (entity=auction, network=512166): ''

  \[row=7\]  
    auction\_\_bid\_request\_id:  
      Hoover (entity=auction, network=512166): 'es31b5-1780171200408852200-3-523319-midroll\_4-3'  
      HooverPP (entity=auction, network=512166): ''  
    auction\_\_invite\_deal\_size:  
      Hoover (entity=auction, network=512166): '63'  
      HooverPP (entity=auction, network=512166): ''

```
  END OF REPORT
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=84.41s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=374.50s | rows=10  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (90366976, 94243247, 87143704, 88990076, 93129695, 93802992, 93959314, 92402774, 93858320, 92933270)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=71.96s | rows=10  
SELECT request\_\_transaction\_id, auction\_\_app\_bundle, auction\_\_application\_type, auction\_\_asset\_id, auction\_\_auction\_network\_to\_eur\_exchange\_rate, auction\_\_auction\_network\_to\_usd\_exchange\_rate, auction\_\_auction\_sampling, auction\_\_auction\_sampling\_\_magnifier, auction\_\_auction\_sampling\_\_mode, auction\_\_auction\_status, auction\_\_bid\_request\_id, auction\_\_bid\_throttling\_exempt\_ratio, auction\_\_bid\_throttling\_info, auction\_\_bid\_throttling\_info\_\_flags, auction\_\_bid\_throttling\_info\_\_level, auction\_\_bid\_throttling\_info\_\_model\_info, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags, auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id, auction\_\_bid\_throttling\_status, auction\_\_bid\_to\_usd\_exchange\_rate, auction\_\_buyer\_group\_id, auction\_\_buyer\_platform\_id, auction\_\_device\_type, auction\_\_dsp\_id, auction\_\_flags, auction\_\_impression, auction\_\_impression\_\_bid\_floor, auction\_\_impression\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals, auction\_\_impression\_\_deals\_\_auction\_type, auction\_\_impression\_\_deals\_\_bid\_floor, auction\_\_impression\_\_deals\_\_bid\_floor\_uplift, auction\_\_impression\_\_deals\_\_buyer\_group\_id, auction\_\_impression\_\_deals\_\_buyers, auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id, auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id, auction\_\_impression\_\_deals\_\_impression\_index, auction\_\_impression\_\_deals\_\_internal\_deal\_id, auction\_\_impression\_\_deals\_\_is\_auction\_rule, auction\_\_impression\_\_deals\_\_listing\_id, auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_deals\_\_media\_buyer\_id, auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index, auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id, auction\_\_impression\_\_deals\_\_order\_id, auction\_\_impression\_\_deals\_\_order\_type, auction\_\_impression\_\_deals\_\_outbound\_order\_index, auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot, auction\_\_impression\_\_deals\_\_slot\_index, auction\_\_impression\_\_deals\_\_trading\_desk\_id, auction\_\_impression\_\_equivalent\_opportunity\_number, auction\_\_impression\_\_error, auction\_\_impression\_\_index, auction\_\_impression\_\_matched\_inventory\_package\_ids, auction\_\_impression\_\_max\_duration, auction\_\_impression\_\_slot\_index, auction\_\_integration\_type, auction\_\_invite\_deal\_size, auction\_\_mkpl\_partner\_tags, auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index, auction\_\_mkpl\_partner\_tags\_\_strategy, auction\_\_network\_id, auction\_\_publisher\_id, auction\_\_series\_id, auction\_\_site\_domain, auction\_\_site\_id, auction\_\_site\_section\_id, auction\_\_time\_position\_class FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (90366976, 94243247, 87143704, 88990076, 93129695, 93802992, 93959314, 92402774, 93858320, 92933270)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=auction, network=520311)  
  Source B : HooverPP (entity=auction, network=520311)  
  Rows  A  : 10  
  Rows  B  : 10  
  Columns A: 68  
  Columns B: 68

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 10

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (68 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 10/10 (100.00%)
  Column match %    : 68/68 (100.00%)
  Cell/value match %: 680/680 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  ✅ No known-difference columns triggered.

  ✅ No field-level differences found!

```
  END OF REPORT
```

#### Aggregation Validation

##### Aggregate Column: auction\_\_buyer\_platform\_id

Aggregation Validation SQL  
-- Hoover SQL  
time=33.65s | rows=2  
SELECT auction\_\_buyer\_platform\_id, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_buyer\_platform\_id ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=30.73s | rows=2*  
*SELECT auction\_\_buyer\_platform\_id, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY auction\_\_buyer\_platform\_id ORDER BY cnt DESC  
Aggregate column: auction\_\_buyer\_platform\_id  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=33.65s | rows=2  
SELECT auction\_\_buyer\_platform\_id, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_buyer\_platform\_id ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=30.73s | rows=2*  
*SELECT auction\_\_buyer\_platform\_id, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY auction\_\_buyer\_platform\_id ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| 3 | 25776 | 25776 | 0 | MATCH |
| None | 161100 | 161100 | 0 | MATCH |

```text
PASS: counts match for all 2 value(s).
Match % (values): 2/2 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

##### Aggregate Column: auction\_\_integration\_type

Aggregation Validation SQL  
-- Hoover SQL  
time=52.58s | rows=3  
SELECT auction\_\_integration\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_integration\_type ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=30.21s | rows=3*  
*SELECT auction\_\_integration\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY auction\_\_integration\_type ORDER BY cnt DESC  
Aggregate column: auction\_\_integration\_type  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=52.58s | rows=3  
SELECT auction\_\_integration\_type, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_integration\_type ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=30.21s | rows=3*  
*SELECT auction\_\_integration\_type, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY auction\_\_integration\_type ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| NORMAL | 12036 | 12036 | 0 | MATCH |
| None | 161100 | 161100 | 0 | MATCH |
| PG\_TD | 13740 | 13740 | 0 | MATCH |

```text
PASS: counts match for all 3 value(s).
Match % (values): 3/3 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

#### Execution Summary

Total execution time: 2625.40s (43.76m)

### Partners

#### Schema Validation

Schema Validation SQL  
-- Hoover schema SQL  
time=6.30s  
SHOW COLUMNS FROM mrm\_log\_flat.default.ad  
-- HooverPP schema SQL  
time=4.05s  
SHOW COLUMNS FROM etl.public\_test1.ad

```text
========================================================================
  COLUMN COMPARISON REPORT  (entity: partners)
========================================================================
  Total columns  — Hoover  : 413
  Total columns  — HooverPP: 198
  Common columns           : 197
  Only in Hoover           : 216
  Only in HooverPP         : 1
  Data-type mismatches     : 0
  Match % (common columns) : 197/414 (47.58%)
  Match % (type on common) : 197/197 (100.00%)
  Match % (overall schema) : 197/414 (47.58%)

  Columns only in Hoover:
    partners__ad_filling_status  [array(varchar)]
    partners__ad_filling_status__available_duration  [array(integer)]
    partners__ad_filling_status__default_unfilled_opp  [array(integer)]
    partners__ad_filling_status__filled_ad_num  [array(integer)]
    partners__ad_filling_status__filled_duration  [array(integer)]
    partners__ad_filling_status__initial_filled_ad_num  [array(integer)]
    partners__ad_filling_status__initial_filled_duration  [array(integer)]
    partners__ad_filling_status__unified_unfilled_opp  [array(integer)]
    partners__ad_priority_bucket  [array(varchar)]
    partners__ad_unit_default_duration  [array(integer)]
    partners__airing_channel_group_id  [array(array(bigint))]
    partners__audience_partner_segment_infos  [array(array(varchar))]
    partners__audience_partner_segment_infos__audience_partner_id  [array(array(bigint))]
    partners__audience_partner_segment_infos__matched_segments  [array(array(array(varchar)))]
    partners__audience_partner_segment_infos__matched_segments__cpm  [array(array(array(double)))]
    partners__audience_partner_segment_infos__matched_segments__flags  [array(array(array(bigint)))]
    partners__audience_partner_segment_infos__matched_segments__id  [array(array(array(integer)))]
    partners__audience_partner_segment_infos__max_cpm  [array(array(double))]
    partners__audience_segment_max_cpm  [array(double)]
    partners__avails_category  [array(varchar)]
    partners__avails_category__avails  [array(integer)]
    partners__avails_category__avails_in_played_slot  [array(integer)]
    partners__avails_category__distinct_inventory_avails  [array(bigint)]
    partners__avails_category__inventory_avails  [array(bigint)]
    partners__avails_category__market_avails  [array(integer)]
    partners__avails_category__market_avails_in_played_slot  [array(integer)]
    partners__avails_category__opportunity  [array(integer)]
    partners__avails_category__opportunity_in_played_slot  [array(integer)]
    partners__avails_category__raw_inventory_distinct_avails_in_played_slot  [array(bigint)]
    partners__avails_category__raw_opportunity_in_played_slot  [array(integer)]
    partners__avails_category__raw_total_avails_in_played_slot  [array(integer)]
    partners__avails_category__remaining_avails  [array(integer)]
    partners__avails_category__slot_opp_avails_in_played_slot  [array(integer)]
    partners__avails_category__ssp_avails  [array(integer)]
    partners__avails_category__ssp_avails_in_played_slot  [array(integer)]
    partners__avails_category__total_avails  [array(integer)]
    partners__avails_category__total_avails_in_played_slot  [array(integer)]
    partners__avails_category__total_unfilled_avails  [array(integer)]
    partners__avails_category__total_unfilled_avails_in_played_slot  [array(integer)]
    partners__avails_category__unconstrained_avails  [array(integer)]
    partners__avails_category__unconstrained_avails_in_played_slot  [array(integer)]
    partners__avails_category__unfilled_avails  [array(integer)]
    partners__avails_category__unfilled_avails_in_played_slot  [array(integer)]
    partners__avails_category__vod_programmer_total_avails  [array(integer)]
    partners__buyer_ids  [array(array(bigint))]
    partners__competition_resellers  [array(integer)]
    partners__count_imp_as_booked  [array(boolean)]
    partners__edge_postal_code_package_ids  [array(array(integer))]
    partners__eligible_outbound_orders  [array(array(varchar))]
    partners__eligible_outbound_orders__ad_filling_status  [array(array(varchar))]
    partners__eligible_outbound_orders__ad_filling_status__available_duration  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__default_unfilled_opp  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__filled_ad_num  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__filled_duration  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__initial_filled_ad_num  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__initial_filled_duration  [array(array(integer))]
    partners__eligible_outbound_orders__ad_filling_status__unified_unfilled_opp  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category  [array(array(varchar))]
    partners__eligible_outbound_orders__avails_category__avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__distinct_inventory_avails  [array(array(bigint))]
    partners__eligible_outbound_orders__avails_category__inventory_avails  [array(array(bigint))]
    partners__eligible_outbound_orders__avails_category__market_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__market_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__opportunity  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__opportunity_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__raw_inventory_distinct_avails_in_played_slot  [array(array(bigint))]
    partners__eligible_outbound_orders__avails_category__raw_opportunity_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__raw_total_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__remaining_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__slot_opp_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__ssp_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__ssp_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__total_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__total_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__total_unfilled_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__total_unfilled_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__unconstrained_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__unconstrained_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__unfilled_avails  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__unfilled_avails_in_played_slot  [array(array(integer))]
    partners__eligible_outbound_orders__avails_category__vod_programmer_total_avails  [array(array(integer))]
    partners__eligible_outbound_orders__bit_flags  [array(array(bigint))]
    partners__eligible_outbound_orders__count_true_avails_as_booked  [array(array(boolean))]
    partners__eligible_outbound_orders__down_network_id  [array(array(bigint))]
    partners__eligible_outbound_orders__exchange_order_id  [array(array(bigint))]
    partners__eligible_outbound_orders__listing_id  [array(array(array(bigint)))]
    partners__eligible_outbound_orders__matched_inventory_package_ids  [array(array(array(bigint)))]
    partners__eligible_outbound_orders__order_id  [array(array(bigint))]
    partners__eligible_outbound_orders__order_priority  [array(array(varchar))]
    partners__eligible_outbound_orders__order_transaction_type  [array(array(varchar))]
    partners__eligible_outbound_orders__order_type  [array(array(varchar))]
    partners__eligible_outbound_orders__sales_channel  [array(array(integer))]
    partners__floor_price  [array(double)]
    partners__geo_visibility  [array(varchar)]
    partners__geo_visibility__report_aggregate  [array(varchar)]
    partners__geo_visibility__report_event  [array(varchar)]
    partners__geo_visibility__targetable  [array(varchar)]
    partners__inbound_order_ids  [array(array(bigint))]
    partners__internal_deal_ids  [array(array(bigint))]
    partners__internal_seat_ids  [array(array(bigint))]
    partners__inventory_distribution_contexts  [array(array(varchar))]
    partners__inventory_distribution_contexts__carriage_inventory_owner_id  [array(array(bigint))]
    partners__inventory_distribution_contexts__carriage_listing_split_unit_id  [array(array(bigint))]
    partners__listing_id  [array(array(bigint))]
    partners__mapped_asset_ids  [array(array(bigint))]
    partners__mapped_site_section_ids  [array(array(bigint))]
    partners__matched_yield_optimization_ids  [array(array(bigint))]
    partners__network_is_ad_unit_owner  [array(boolean)]
    partners__network_is_vod_programmer  [array(boolean)]
    partners__network_selection_info  [array(varchar)]
    partners__network_selection_info__candidate_ad_funnel_metrics  [array(array(varchar))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics  [array(array(varchar))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__auction_max_ad_duration  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__competition_failure_in_pick_many  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__compliance_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__exclusivity  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__floor_price_not_met  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__frequency_cap  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inbound_order_competition_failure  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__input_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__inventory_source_restriction  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__listing_creative_duration_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__market_ad_not_approved  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__met_yield_optimization  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__mpe_listing_restriction  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_excluded_by_sponsor  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_applicable_slot_not_compatible  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_ad_asset_store_availability  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_bitrate_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_creative_targeting_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_date_range_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_compatible_dimension_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_creative_slot_max_ad_duration_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__no_suitable_rule_path  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__output_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__pg_deal_bid_throttling  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__profile_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__reseller_restriction  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__restriction  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__undefined  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_creative_checking_metrics__unmapped  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics  [array(array(varchar))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__companion_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__do_not_repeat  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__input_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__no_creative  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__output_fallback_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__pod_position_targeting_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_exclusivity_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_filled_by_multi_ad  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_duration  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_max_num_ads  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_not_found  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__slot_sponsorship_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__time_based_freq_cap  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__undefined  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filling_metrics__unmapped  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics  [array(array(varchar))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__ad_truncation  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__cpx_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__exclusivity_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__frequency_cap  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__input_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_budget  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_schedule  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__met_yield_optimization  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_ad_domain  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_no_external_rule  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_compatible  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_not_resellable  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_promo_only  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_applicable_slot_user_experience  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__no_slot_assigned_through_mrm_rule  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__output_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__rbp_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__sponsorship_check_failed  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__undefined  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_filtering_metrics__unmapped  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics  [array(array(varchar))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__data_privacy  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__input_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__output_ad_number  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__restriction  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__undefined  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__ad_targeting_metrics__unmapped  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__demand_type  [array(array(integer))]
    partners__network_selection_info__candidate_ad_funnel_metrics__listing_ids  [array(array(array(bigint)))]
    partners__network_selection_info__candidate_ad_funnel_metrics__network_id  [array(array(bigint))]
    partners__network_selection_info__candidate_ad_funnel_metrics__order_id  [array(array(bigint))]
    partners__network_selection_info__candidate_ad_funnel_metrics__phase_metrics  [array(array(array(varchar)))]
    partners__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__name  [array(array(array(varchar)))]
    partners__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__phase  [array(array(array(bigint)))]
    partners__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__value  [array(array(array(bigint)))]
    partners__outbound_exchange_listings  [array(array(varchar))]
    partners__outbound_exchange_listings__avails_metrics  [array(array(varchar))]
    partners__outbound_exchange_listings__avails_metrics__avails  [array(array(integer))]
    partners__outbound_exchange_listings__avails_metrics__default_duration  [array(array(integer))]
    partners__outbound_exchange_listings__avails_metrics__opportunity  [array(array(integer))]
    partners__outbound_exchange_listings__avails_metrics__unfilled_avails  [array(array(integer))]
    partners__outbound_exchange_listings__listing_ids  [array(array(array(bigint)))]
    partners__outbound_exchange_order_ids  [array(array(bigint))]
    partners__outbound_rules  [array(array(varchar))]
    partners__outbound_rules__rule_id  [array(array(bigint))]
    partners__outbound_rules__total_opp  [array(array(bigint))]
    partners__outbound_rules__win_opp  [array(array(bigint))]
    partners__postal_code_package_id  [array(array(integer))]
    partners__rule_ext_id  [array(bigint)]
    partners__rule_flags  [array(bigint)]
    partners__site_group_id  [array(bigint)]
    partners__ssp_clearing_revenue  [array(double)]
    partners__supply_source_type  [array(varchar)]

  Columns only in HooverPP:
    partners__network__mkpl_info__ad_outbound_order__active_term_ids  [array(array(bigint))]

========================================================================
```

#### Column Data Validation

##### Network: 169843

Column Data Validation SQL  
-- PK discovery SQL  
time=23.46s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 169843 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=421.30s | rows=2  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=103.34s | rows=2  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 169843   AND (request\_\_transaction\_id IN ('1780171200012271646', '1780171200456259772') AND advertisement\_\_ad\_id IN (93989699)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=partners, network=169843)  
  Source B : HooverPP (entity=partners, network=169843)  
  Rows  A  : 2  
  Rows  B  : 2  
  Columns A: 198  
  Columns B: 198

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 2

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (198 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 2/2 (100.00%)
  Column match %    : 198/198 (100.00%)
  Cell/value match %: 396/396 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
partners__eligible_carriage_listing_split_unit_ids           2 row(s)
partners__outbound_exchange_order_id                         2 row(s)
partners__programmatic_exchange_rate_to_eur                  2 row(s)
partners__programmatic_exchange_rate_to_usd                  2 row(s)
```

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 191701

Column Data Validation SQL  
-- PK discovery SQL  
time=55.65s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 191701 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=378.31s | rows=15  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415904, 93340683, 93415975, 93185984, 92676151, 93418034, 93456612, 93010669, 93115000, 93743116)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=137.44s | rows=15  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 191701   AND (request\_\_transaction\_id IN ('1780171200152600120', '1780171201168859349') AND advertisement\_\_ad\_id IN (93415904, 93340683, 93415975, 93185984, 92676151, 93418034, 93456612, 93010669, 93115000, 93743116)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=partners, network=191701)  
  Source B : HooverPP (entity=partners, network=191701)  
  Rows  A  : 15  
  Rows  B  : 15  
  Columns A: 198  
  Columns B: 198

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 15

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (198 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 4/15 (26.67%)
  Column match %    : 197/198 (99.49%)
  Cell/value match %: 2,959/2,970 (99.63%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
partners__eligible_carriage_listing_split_unit_ids           15 row(s)
partners__outbound_exchange_order_id                         15 row(s)
partners__programmatic_exchange_rate_to_eur                  15 row(s)
partners__programmatic_exchange_rate_to_usd                  15 row(s)
partners__selected_yield_optimization_info_ids               11 row(s)
partners__selected_yo_volume_cap_ids                         11 row(s)
```

  ❌ 11 row(s) have differences:

  Column diff summary (sorted by frequency):  
    partners\_\_inventory\_package\_ids                              11 row(s)

  Detailed diffs:

  \[row=2\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=3\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=4\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=5\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=6\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=7\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=8\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=9\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=10\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=11\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

  \[row=12\]  
    partners\_\_inventory\_package\_ids:  
      Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]'  
      HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]'

```
  END OF REPORT
```

##### Network: 384777

Column Data Validation SQL  
-- PK discovery SQL  
time=34.28s | rows=3  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 384777 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=890.07s | rows=4  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=126.36s | rows=4  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 384777   AND (request\_\_transaction\_id IN ('1780171200021241125', '1780171200031006257') AND advertisement\_\_ad\_id IN (33042948, 93966487)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=partners, network=384777)  
  Source B : HooverPP (entity=partners, network=384777)  
  Rows  A  : 4  
  Rows  B  : 4  
  Columns A: 198  
  Columns B: 198

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 4

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (198 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 4/4 (100.00%)
  Column match %    : 198/198 (100.00%)
  Cell/value match %: 792/792 (100.00%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
partners__eligible_carriage_listing_split_unit_ids           4 row(s)
partners__outbound_exchange_order_id                         4 row(s)
partners__programmatic_exchange_rate_to_eur                  4 row(s)
partners__programmatic_exchange_rate_to_usd                  4 row(s)
partners__selected_yield_optimization_info_ids               3 row(s)
partners__selected_yo_volume_cap_ids                         3 row(s)
partners__inventory_package_ids                              2 row(s)
```

  ✅ No field-level differences found!

```
  END OF REPORT
```

##### Network: 512166

Column Data Validation SQL  
-- PK discovery SQL  
time=23.22s | rows=2  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 512166 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=1315.31s | rows=6  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=117.65s | rows=6  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 512166   AND (request\_\_transaction\_id IN ('1780171200055030888', '1780171200408852200') AND advertisement\_\_ad\_id IN (53782914)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=partners, network=512166)  
  Source B : HooverPP (entity=partners, network=512166)  
  Rows  A  : 6  
  Rows  B  : 6  
  Columns A: 198  
  Columns B: 198

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 6

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (198 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 0/6 (0.00%)
  Column match %    : 191/198 (96.46%)
  Cell/value match %: 1,156/1,188 (97.31%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
partners__eligible_carriage_listing_split_unit_ids           6 row(s)
partners__selected_yield_optimization_info_ids               5 row(s)
partners__selected_yo_volume_cap_ids                         5 row(s)
```

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):  
    partners\_\_inbound\_listing\_ids                                6 row(s)  
    partners\_\_inbound\_order\_transaction\_type                     6 row(s)  
    partners\_\_outbound\_exchange\_order\_id                         6 row(s)  
    partners\_\_outbound\_listing\_id                                6 row(s)  
    partners\_\_unified\_outbound\_order\_priority                    6 row(s)  
    partners\_\_selected\_yield\_optimization\_info\_ids               1 row(s)  
    partners\_\_selected\_yo\_volume\_cap\_ids                         1 row(s)

  Detailed diffs:

  \[row=2\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[257759\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[257759\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[257759\], None, None\]'  
    partners\_\_selected\_yield\_optimization\_info\_ids:  
      Hoover (entity=partners, network=512166): '\[\[\], \[\[14681, -1\]\], \[\]\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[\[14681, -1\]\], None\]'  
    partners\_\_selected\_yo\_volume\_cap\_ids:  
      Hoover (entity=partners, network=512166): '\[\[\], \[14681\], \[\]\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[14681\], None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

  \[row=3\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[255728\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[255728\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[255728\], None, None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

  \[row=4\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[255728\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[255728\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[255728\], None, None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

  \[row=5\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[255728\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[255728\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[255728\], None, None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

  \[row=6\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[255728\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[255728\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[255728\], None, None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

  \[row=7\]  
    partners\_\_inbound\_listing\_ids:  
      Hoover (entity=partners, network=512166): '\[None, None, None\]'  
      HooverPP (entity=partners, network=512166): '\[None, \[255728\], None\]'  
    partners\_\_inbound\_order\_transaction\_type:  
      Hoover (entity=partners, network=512166): "\[None, 'NON\_GUARANTEED', None\]"  
      HooverPP (entity=partners, network=512166): '\[None, None, None\]'  
    partners\_\_outbound\_exchange\_order\_id:  
      Hoover (entity=partners, network=512166): '\[4211, None, None\]'  
      HooverPP (entity=partners, network=512166): ''  
    partners\_\_outbound\_listing\_id:  
      Hoover (entity=partners, network=512166): '\[\[255728\], \[\], None\]'  
      HooverPP (entity=partners, network=512166): '\[\[255728\], None, None\]'  
    partners\_\_unified\_outbound\_order\_priority:  
      Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]'  
      HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]'

```
  END OF REPORT
```

##### Network: 520311

Column Data Validation SQL  
-- PK discovery SQL  
time=9.49s | rows=10  
SELECT DISTINCT request\_\_transaction\_id, advertisement\_\_ad\_id FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND advertisement\_\_ad\_oo\_network\_id = 520311 ORDER BY request\_\_transaction\_id LIMIT 10  
-- Hoover SQL  
time=294.53s | rows=10  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (94243247, 88990076, 90366976, 87143704, 92877229, 93802992, 93743083, 94201621, 88675621, 93773414)) ORDER BY request\_\_transaction\_id  
-- HooverPP SQL  
time=262.02s | rows=10  
SELECT request\_\_transaction\_id, partners\_\_airing\_channel\_id, partners\_\_airing\_id, partners\_\_asset\_group\_id, partners\_\_asset\_group\_ids, partners\_\_asset\_id, partners\_\_bidder\_seat\_id, partners\_\_bidding\_revenue, partners\_\_bidding\_up\_revenue, partners\_\_bit\_flags, partners\_\_break\_id, partners\_\_carriage\_inventory\_owner\_id, partners\_\_carriage\_listing\_split\_unit\_id, partners\_\_content\_form\_visibility, partners\_\_content\_form\_visibility\_\_report\_aggregate, partners\_\_content\_form\_visibility\_\_report\_event, partners\_\_content\_form\_visibility\_\_targetable, partners\_\_content\_owner\_bidding\_modified\_revenue, partners\_\_content\_owner\_bidding\_original\_revenue, partners\_\_content\_owner\_bidding\_revenue, partners\_\_content\_owner\_network\_id, partners\_\_content\_owner\_revenue, partners\_\_content\_rating\_visibility, partners\_\_content\_rating\_visibility\_\_report\_aggregate, partners\_\_content\_rating\_visibility\_\_report\_event, partners\_\_content\_rating\_visibility\_\_targetable, partners\_\_custom\_platform\_ids, partners\_\_deal\_awareability, partners\_\_demand\_dim\_awareability, partners\_\_device\_id\_visibility, partners\_\_device\_id\_visibility\_\_report\_aggregate, partners\_\_device\_id\_visibility\_\_report\_event, partners\_\_device\_id\_visibility\_\_targetable, partners\_\_distributor\_bidding\_revenue, partners\_\_distributor\_network\_id, partners\_\_distributor\_revenue, partners\_\_eligible\_carriage\_listing\_split\_unit\_ids, partners\_\_entity\_source, partners\_\_flags, partners\_\_geo\_city\_visibility, partners\_\_geo\_city\_visibility\_\_report\_aggregate, partners\_\_geo\_city\_visibility\_\_report\_event, partners\_\_geo\_city\_visibility\_\_targetable, partners\_\_geo\_country\_visibility, partners\_\_geo\_country\_visibility\_\_report\_aggregate, partners\_\_geo\_country\_visibility\_\_report\_event, partners\_\_geo\_country\_visibility\_\_targetable, partners\_\_geo\_dma\_visibility, partners\_\_geo\_dma\_visibility\_\_report\_aggregate, partners\_\_geo\_dma\_visibility\_\_report\_event, partners\_\_geo\_dma\_visibility\_\_targetable, partners\_\_geo\_state\_visibility, partners\_\_geo\_state\_visibility\_\_report\_aggregate, partners\_\_geo\_state\_visibility\_\_report\_event, partners\_\_geo\_state\_visibility\_\_targetable, partners\_\_geo\_zip\_code\_visibility, partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate, partners\_\_geo\_zip\_code\_visibility\_\_report\_event, partners\_\_geo\_zip\_code\_visibility\_\_targetable, partners\_\_global\_currency\_id, partners\_\_inbound\_listing\_id, partners\_\_inbound\_listing\_ids, partners\_\_inbound\_order\_auction\_type, partners\_\_inbound\_order\_id, partners\_\_inbound\_order\_transaction\_type, partners\_\_inbound\_order\_type, partners\_\_inbound\_rule\_id, partners\_\_inventory\_package\_ids, partners\_\_ip\_visibility, partners\_\_ip\_visibility\_\_report\_aggregate, partners\_\_ip\_visibility\_\_report\_event, partners\_\_ip\_visibility\_\_targetable, partners\_\_key\_value\_visibility, partners\_\_key\_value\_visibility\_\_report\_aggregate, partners\_\_key\_value\_visibility\_\_report\_event, partners\_\_key\_value\_visibility\_\_targetable, partners\_\_margin, partners\_\_marketplace\_audience\_extension\_deal\_ids, partners\_\_matched\_audience\_item\_ids, partners\_\_matched\_daypart, partners\_\_matched\_inventory\_package\_ids, partners\_\_matched\_key\_value\_ids, partners\_\_network\_execution\_ctx\_flags, partners\_\_network\_execution\_ctx\_index, partners\_\_network\_id, partners\_\_network\_is\_ad\_owner, partners\_\_network\_is\_extra\_item\_owner, partners\_\_non\_tracked\_audience\_item\_ids, partners\_\_opportunity\_id, partners\_\_outbound\_exchange\_order\_id, partners\_\_outbound\_listing\_id, partners\_\_outbound\_order\_id, partners\_\_outbound\_order\_ids, partners\_\_outbound\_order\_priority\_type, partners\_\_outbound\_order\_transaction\_type, partners\_\_outbound\_order\_type, partners\_\_portfolio\_ids, partners\_\_priority\_tier, partners\_\_priority\_type, partners\_\_priority\_value, partners\_\_programmatic\_exchange\_rate\_to\_eur, partners\_\_programmatic\_exchange\_rate\_to\_usd, partners\_\_region\_ids, partners\_\_reseller\_bidding\_revenue, partners\_\_reseller\_network\_id, partners\_\_reseller\_revenue, partners\_\_revenue, partners\_\_role, partners\_\_rule\_id, partners\_\_rule\_type\_priority, partners\_\_sales\_channel, partners\_\_scenario\_id, partners\_\_selected\_yield\_optimization\_ids, partners\_\_selected\_yield\_optimization\_info\_ids, partners\_\_selected\_yo\_distribution\_id, partners\_\_selected\_yo\_distribution\_nip\_id, partners\_\_selected\_yo\_inventory\_prioritization\_id, partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id, partners\_\_selected\_yo\_margin\_id, partners\_\_selected\_yo\_volume\_cap\_ids, partners\_\_series\_id, partners\_\_site\_id, partners\_\_site\_section\_group\_ids, partners\_\_site\_section\_id, partners\_\_standard\_brand\_visibility, partners\_\_standard\_brand\_visibility\_\_report\_aggregate, partners\_\_standard\_brand\_visibility\_\_report\_event, partners\_\_standard\_brand\_visibility\_\_targetable, partners\_\_standard\_channel\_visibility, partners\_\_standard\_channel\_visibility\_\_report\_aggregate, partners\_\_standard\_channel\_visibility\_\_report\_event, partners\_\_standard\_channel\_visibility\_\_targetable, partners\_\_standard\_content\_credential\_status\_visibility, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event, partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable, partners\_\_standard\_content\_daypart\_visibility, partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_daypart\_visibility\_\_report\_event, partners\_\_standard\_content\_daypart\_visibility\_\_targetable, partners\_\_standard\_content\_series\_visibility, partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_series\_visibility\_\_report\_event, partners\_\_standard\_content\_series\_visibility\_\_targetable, partners\_\_standard\_content\_subscription\_model\_visibility, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event, partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable, partners\_\_standard\_content\_territory\_visibility, partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate, partners\_\_standard\_content\_territory\_visibility\_\_report\_event, partners\_\_standard\_content\_territory\_visibility\_\_targetable, partners\_\_standard\_endpoint\_owner\_visibility, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable, partners\_\_standard\_endpoint\_visibility, partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate, partners\_\_standard\_endpoint\_visibility\_\_report\_event, partners\_\_standard\_endpoint\_visibility\_\_targetable, partners\_\_standard\_genre\_visibility, partners\_\_standard\_genre\_visibility\_\_report\_aggregate, partners\_\_standard\_genre\_visibility\_\_report\_event, partners\_\_standard\_genre\_visibility\_\_targetable, partners\_\_standard\_language\_visibility, partners\_\_standard\_language\_visibility\_\_report\_aggregate, partners\_\_standard\_language\_visibility\_\_report\_event, partners\_\_standard\_language\_visibility\_\_targetable, partners\_\_standard\_programmer\_visibility, partners\_\_standard\_programmer\_visibility\_\_report\_aggregate, partners\_\_standard\_programmer\_visibility\_\_report\_event, partners\_\_standard\_programmer\_visibility\_\_targetable, partners\_\_supply\_acquisition\_cost, partners\_\_supply\_distribution\_cost, partners\_\_supply\_source, partners\_\_third\_party\_user\_id\_visibility, partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate, partners\_\_third\_party\_user\_id\_visibility\_\_report\_event, partners\_\_third\_party\_user\_id\_visibility\_\_targetable, partners\_\_tracked\_audience\_item\_ids, partners\_\_unified\_outbound\_order\_priority, partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier, partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value, partners\_\_unified\_rule\_priority, partners\_\_unified\_rule\_priority\_\_priority\_tier, partners\_\_unified\_rule\_priority\_\_sub\_priority\_value, partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency, partners\_\_upstream\_global\_currency\_id, partners\_\_upstream\_inbound\_order\_id, partners\_\_user\_agent\_visibility, partners\_\_user\_agent\_visibility\_\_report\_aggregate, partners\_\_user\_agent\_visibility\_\_report\_event, partners\_\_user\_agent\_visibility\_\_targetable, partners\_\_visible\_concrete\_event\_id, partners\_\_visitor\_custom\_id\_visibility, partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate, partners\_\_visitor\_custom\_id\_visibility\_\_report\_event, partners\_\_visitor\_custom\_id\_visibility\_\_targetable FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id = 520311   AND (request\_\_transaction\_id IN ('1780171200040704883', '1780171200424500999') AND advertisement\_\_ad\_id IN (94243247, 88990076, 90366976, 87143704, 92877229, 93802992, 93743083, 94201621, 88675621, 93773414)) ORDER BY request\_\_transaction\_id

```
  EVENT-LEVEL CSV COMPARISON REPORT
```

  Source A : Hoover (entity=partners, network=520311)  
  Source B : HooverPP (entity=partners, network=520311)  
  Rows  A  : 10  
  Rows  B  : 10  
  Columns A: 198  
  Columns B: 198

── \[1\] ROW COUNT CHECK ─────────────────────────────────────────────────  
  ✅ Row counts match: 10

── \[2\] COLUMN HEADER CHECK ────────────────────────────────────────────  
  ✅ Column headers identical (198 columns)

── \[3\] ROW DIFFS (matched by row position) ─────────────────────────────

── \[3a\] UNIQUE KEY CHECK (request\_\_transaction\_id) ──────────────────────────────  
  ✅ All request\_\_transaction\_id values match between files — rows correspond to the same events.

── \[M\] MATCH PERCENTAGE SUMMARY ────────────────────────────────────

```text
  Row match %       : 4/10 (40.00%)
  Column match %    : 189/198 (95.45%)
  Cell/value match %: 1,940/1,980 (97.98%)
```

── \[K\] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────  
  Global equivalence groups (apply to all columns automatically):  
    \['', '0', '\\\\N', '\\\\n', 'false', 'none', 'null'\]  
    \['', '\[\]', '\\\\N', '\\\\n', 'none', 'null', '{}'\]

  Suppressed diffs by column (semantically equivalent values):

```
partners__outbound_exchange_order_id                         10 row(s)
partners__programmatic_exchange_rate_to_eur                  10 row(s)
partners__programmatic_exchange_rate_to_usd                  10 row(s)
partners__eligible_carriage_listing_split_unit_ids           4 row(s)
partners__selected_yield_optimization_info_ids               4 row(s)
partners__selected_yo_volume_cap_ids                         4 row(s)
```

  ❌ 6 row(s) have differences:

  Column diff summary (sorted by frequency):  
    partners\_\_bidding\_revenue                                    6 row(s)  
    partners\_\_reseller\_bidding\_revenue                           6 row(s)  
    partners\_\_reseller\_revenue                                   6 row(s)  
    partners\_\_revenue                                            6 row(s)  
    partners\_\_bit\_flags                                          4 row(s)  
    partners\_\_selected\_yield\_optimization\_info\_ids               4 row(s)  
    partners\_\_selected\_yo\_inventory\_prioritization\_id            4 row(s)  
    partners\_\_priority\_tier                                      2 row(s)  
    partners\_\_priority\_value                                     2 row(s)

  Detailed diffs:

  \[row=6\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02048\]'  
      HooverPP (entity=partners, network=520311): '\[0.01804\]'  
    partners\_\_bit\_flags:  
      Hoover (entity=partners, network=520311): '\[0\]'  
      HooverPP (entity=partners, network=520311): '\[18014398509481984\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02048\]'  
      HooverPP (entity=partners, network=520311): '\[0.01804\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02048\]'  
      HooverPP (entity=partners, network=520311): '\[0.01804\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02048\]'  
      HooverPP (entity=partners, network=520311): '\[0.01804\]'  
    partners\_\_selected\_yield\_optimization\_info\_ids:  
      Hoover (entity=partners, network=520311): '\[\[\[26704, -1\]\]\]'  
      HooverPP (entity=partners, network=520311): '\[\[\[26705, -1\]\]\]'  
    partners\_\_selected\_yo\_inventory\_prioritization\_id:  
      Hoover (entity=partners, network=520311): '\[26704\]'  
      HooverPP (entity=partners, network=520311): '\[26705\]'

  \[row=7\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0215\]'  
      HooverPP (entity=partners, network=520311): '\[0.0095\]'  
    partners\_\_bit\_flags:  
      Hoover (entity=partners, network=520311): '\[18014398509481984\]'  
      HooverPP (entity=partners, network=520311): '\[0\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0215\]'  
      HooverPP (entity=partners, network=520311): '\[0.0095\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0215\]'  
      HooverPP (entity=partners, network=520311): '\[0.0095\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0215\]'  
      HooverPP (entity=partners, network=520311): '\[0.0095\]'

  \[row=8\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0135\]'  
      HooverPP (entity=partners, network=520311): '\[0.02048\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0135\]'  
      HooverPP (entity=partners, network=520311): '\[0.02048\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0135\]'  
      HooverPP (entity=partners, network=520311): '\[0.02048\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0135\]'  
      HooverPP (entity=partners, network=520311): '\[0.02048\]'  
    partners\_\_selected\_yield\_optimization\_info\_ids:  
      Hoover (entity=partners, network=520311): '\[\[\[26705, -1\]\]\]'  
      HooverPP (entity=partners, network=520311): '\[\[\[26704, -1\]\]\]'  
    partners\_\_selected\_yo\_inventory\_prioritization\_id:  
      Hoover (entity=partners, network=520311): '\[26705\]'  
      HooverPP (entity=partners, network=520311): '\[26704\]'

  \[row=9\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02186\]'  
      HooverPP (entity=partners, network=520311): '\[0.0215\]'  
    partners\_\_priority\_tier:  
      Hoover (entity=partners, network=520311): "\['TIER\_4'\]"  
      HooverPP (entity=partners, network=520311): "\['TIER\_3'\]"  
    partners\_\_priority\_value:  
      Hoover (entity=partners, network=520311): '\[-65536\]'  
      HooverPP (entity=partners, network=520311): '\[0\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02186\]'  
      HooverPP (entity=partners, network=520311): '\[0.0215\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02186\]'  
      HooverPP (entity=partners, network=520311): '\[0.0215\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.02186\]'  
      HooverPP (entity=partners, network=520311): '\[0.0215\]'  
    partners\_\_selected\_yield\_optimization\_info\_ids:  
      Hoover (entity=partners, network=520311): '\[\[\[26705, -1\]\]\]'  
      HooverPP (entity=partners, network=520311): '\[\[\[26704, -1\]\]\]'  
    partners\_\_selected\_yo\_inventory\_prioritization\_id:  
      Hoover (entity=partners, network=520311): '\[26705\]'  
      HooverPP (entity=partners, network=520311): '\[26704\]'

  \[row=10\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.01804\]'  
      HooverPP (entity=partners, network=520311): '\[0.0135\]'  
    partners\_\_bit\_flags:  
      Hoover (entity=partners, network=520311): '\[18014398509481984\]'  
      HooverPP (entity=partners, network=520311): '\[0\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.01804\]'  
      HooverPP (entity=partners, network=520311): '\[0.0135\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.01804\]'  
      HooverPP (entity=partners, network=520311): '\[0.0135\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.01804\]'  
      HooverPP (entity=partners, network=520311): '\[0.0135\]'

  \[row=11\]  
    partners\_\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0095\]'  
      HooverPP (entity=partners, network=520311): '\[0.02186\]'  
    partners\_\_bit\_flags:  
      Hoover (entity=partners, network=520311): '\[0\]'  
      HooverPP (entity=partners, network=520311): '\[18014398509481984\]'  
    partners\_\_priority\_tier:  
      Hoover (entity=partners, network=520311): "\['TIER\_3'\]"  
      HooverPP (entity=partners, network=520311): "\['TIER\_4'\]"  
    partners\_\_priority\_value:  
      Hoover (entity=partners, network=520311): '\[0\]'  
      HooverPP (entity=partners, network=520311): '\[-65536\]'  
    partners\_\_reseller\_bidding\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0095\]'  
      HooverPP (entity=partners, network=520311): '\[0.02186\]'  
    partners\_\_reseller\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0095\]'  
      HooverPP (entity=partners, network=520311): '\[0.02186\]'  
    partners\_\_revenue:  
      Hoover (entity=partners, network=520311): '\[0.0095\]'  
      HooverPP (entity=partners, network=520311): '\[0.02186\]'  
    partners\_\_selected\_yield\_optimization\_info\_ids:  
      Hoover (entity=partners, network=520311): '\[\[\[26704, -1\]\]\]'  
      HooverPP (entity=partners, network=520311): '\[\[\[26705, -1\]\]\]'  
    partners\_\_selected\_yo\_inventory\_prioritization\_id:  
      Hoover (entity=partners, network=520311): '\[26704\]'  
      HooverPP (entity=partners, network=520311): '\[26705\]'

```
  END OF REPORT
```

#### Aggregation Validation

##### Aggregate Column: partners\_\_entity\_source

Aggregation Validation SQL  
-- Hoover SQL  
time=25.06s | rows=5  
SELECT partners\_\_entity\_source, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_entity\_source ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=13.01s | rows=5*  
*SELECT partners\_\_entity\_source, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY partners\_\_entity\_source ORDER BY cnt DESC  
Aggregate column: partners\_\_entity\_source  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=25.06s | rows=5  
SELECT partners\_\_entity\_source, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_entity\_source ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=13.01s | rows=5*  
*SELECT partners\_\_entity\_source, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY partners\_\_entity\_source ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| \['ad', 'ad', 'ad', 'ad', 'ad'\] | 95 | 95 | 0 | MATCH |
| \['ad', 'ad', 'ad', 'ad'\] | 648 | 648 | 0 | MATCH |
| \['ad', 'ad', 'ad'\] | 10267 | 10267 | 0 | MATCH |
| \['ad', 'ad'\] | 57183 | 57183 | 0 | MATCH |
| \['ad'\] | 118683 | 118683 | 0 | MATCH |

```text
PASS: counts match for all 5 value(s).
Match % (values): 5/5 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

##### Aggregate Column: partners\_\_role

Aggregation Validation SQL  
-- Hoover SQL  
time=50.98s | rows=17  
SELECT partners\_\_role, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_role ORDER BY cnt DESC*  
*-- HooverPP SQL*  
*time=30.31s | rows=17*  
*SELECT partners\_\_role, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY partners\_\_role ORDER BY cnt DESC  
Aggregate column: partners\_\_role  
SQL USED FOR THIS AGG VALIDATION:  
\[Hoover SQL\]  
time=50.98s | rows=17  
SELECT partners\_\_role, COUNT(*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_role ORDER BY cnt DESC*  
*\[HooverPP SQL\]*  
*time=30.31s | rows=17*  
*SELECT partners\_\_role, COUNT(*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-30 20:00:00' as TIMESTAMP))) AND batch\_id IN ('20260530190000','20260530200000','20260530210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 384777, 169843, 512166) GROUP BY partners\_\_role ORDER BY cnt DESC

| Value | Hoover | HooverPP | Diff | Status |
| --- | --- | --- | --- | --- |
| \['CRO', 'C'\] | 44 | 44 | 0 | MATCH |
| \['CRO', 'D', 'C'\] | 283 | 283 | 0 | MATCH |
| \['CRO', 'D', 'D'\] | 1206 | 1206 | 0 | MATCH |
| \['CRO', 'D'\] | 36786 | 36786 | 0 | MATCH |
| \['CRO', 'R', 'C'\] | 276 | 276 | 0 | MATCH |
| \['CRO', 'R', 'D', 'C'\] | 39 | 39 | 0 | MATCH |
| \['CRO', 'R', 'D', 'D'\] | 130 | 130 | 0 | MATCH |
| \['CRO', 'R', 'D'\] | 1939 | 1939 | 0 | MATCH |
| \['CRO', 'R', 'R', 'C'\] | 3 | 3 | 0 | MATCH |
| \['CRO', 'R', 'R', 'D', 'D'\] | 23 | 23 | 0 | MATCH |
| \['CRO', 'R', 'R', 'D'\] | 329 | 329 | 0 | MATCH |
| \['CRO', 'R', 'R', 'R', 'D'\] | 59 | 59 | 0 | MATCH |
| \['CRO', 'R', 'R', 'R', 'R'\] | 13 | 13 | 0 | MATCH |
| \['CRO', 'R', 'R', 'R'\] | 147 | 147 | 0 | MATCH |
| \['CRO', 'R', 'R'\] | 6563 | 6563 | 0 | MATCH |
| \['CRO', 'R'\] | 20353 | 20353 | 0 | MATCH |
| \['CRO'\] | 118683 | 118683 | 0 | MATCH |

```text
PASS: counts match for all 17 value(s).
Match % (values): 17/17 (100.00%)
Match % (volume): 186,876/186,876 (100.00%)
```

#### Execution Summary

Total execution time: 4355.76s (72.60m)

## Aggregated Columns

### advertisement\_\_ad\_oo\_network\_id

| **Network ID** | **Old Count** | **New Count** |
| --- | --- | --- |
| 384777 | `21773` | `21773` |
| 112214 | `261` | `261` |
| 518308 | `11560` | `11560` |
| 512166 | `17025` | `17025` |
| 169843 | `18597` | `18597` |

Result: All counts match for the column **advertisement\_\_ad\_oo\_network\_id** for all 5 network ids above. 

Old Count: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512171148\_178863&externalid=20260512\_171150\_00344\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512171148_178863&externalid=20260512_171150_00344_qk7z5)

New Count: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512171613\_416002&externalid=20260512\_171645\_00350\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512171613_416002&externalid=20260512_171645_00350_qk7z5)  
  
 

 

\============================================================

  TOP NETWORK FETCH SQL USED

\============================================================

time=114.96s

SELECT advertisement\_\_ad\_oo\_network\_id, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY advertisement\_\_ad\_oo\_network\_id ORDER BY cnt DESC LIMIT 5

\============================================================

  END OF TOP NETWORK FETCH SQL USED

\============================================================

 

\============================================================

  TOP NETWORK DISCOVERY

  Network column: advertisement\_\_ad\_oo\_network\_id

  Requested top N: 5

  PK transaction sample N: 2

  Returned networks: 5

\============================================================

  Rank  Network                             Count

  --------------------------------------------------

     1  520311                             56,026

     2  191701                             37,611

     3  169843                             28,775

     4  384777                             25,928

     5  512166                             25,727

 

\============================================================

  END OF TOP NETWORK DISCOVERY

\============================================================

 

\============================================================

  AGGREGATION VALIDATION REPORT

  Table : ad

  Networks sampled: \['520311', '191701', '169843', '384777', '512166'\]

\============================================================

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: request\_\_context\_\_po\_type

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=93.93s | rows=3

  SELECT request\_\_context\_\_po\_type, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=62.97s | rows=3

  SELECT request\_\_context\_\_po\_type, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY request\_\_context\_\_po\_type ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  DISTRIBUTOR                                     17102        17102            0      MATCH

  None                                           156741       156741            0      MATCH

  PROVIDER                                          224          224            0      MATCH

  ✅ PASS: counts match for all 3 value(s).

  Match % (values): 3/3 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: request\_\_context\_\_standard\_content\_daypart\_id

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=84.84s | rows=4

  SELECT request\_\_context\_\_standard\_content\_daypart\_id, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY request\_\_context\_\_standard\_content\_daypart\_id ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=58.97s | rows=4

  SELECT request\_\_context\_\_standard\_content\_daypart\_id, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY request\_\_context\_\_standard\_content\_daypart\_id ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  1                                                9869         9869            0      MATCH

  2                                                2226         2226            0      MATCH

  3                                                 292          292            0      MATCH

  None                                           161680       161680            0      MATCH

  ✅ PASS: counts match for all 4 value(s).

  Match % (values): 4/4 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: visitor\_\_country

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=98.54s | rows=53

  SELECT visitor\_\_country, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_country ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=146.60s | rows=53

  SELECT visitor\_\_country, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY visitor\_\_country ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  None                                                8            8            0      MATCH

  ar                                                324          324            0      MATCH

  at                                                 71           71            0      MATCH

  au                                                313          313            0      MATCH

  be                                                 48           48            0      MATCH

  bm                                                  1            1            0      MATCH

  bo                                                 14           14            0      MATCH

  br                                               1554         1554            0      MATCH

  bs                                                  1            1            0      MATCH

  ca                                                609          609            0      MATCH

  ch                                                 21           21            0      MATCH

  cl                                                149          149            0      MATCH

  co                                                225          225            0      MATCH

  cr                                                 38           38            0      MATCH

  de                                                751          751            0      MATCH

  dk                                                 76           76            0      MATCH

  do                                                 30           30            0      MATCH

  ec                                                 75           75            0      MATCH

  es                                                522          522            0      MATCH

  fi                                                 96           96            0      MATCH

  fr                                               3447         3447            0      MATCH

  gb                                               8873         8873            0      MATCH

  ge                                                  1            1            0      MATCH

  gl                                                  1            1            0      MATCH

  gr                                                  1            1            0      MATCH

  gt                                                 15           15            0      MATCH

  hk                                                  1            1            0      MATCH

  hn                                                  2            2            0      MATCH

  ie                                                 35           35            0      MATCH

  in                                                  1            1            0      MATCH

  it                                                342          342            0      MATCH

  jm                                                  2            2            0      MATCH

  mq                                                  1            1            0      MATCH

  mx                                                870          870            0      MATCH

  ni                                                 17           17            0      MATCH

  nl                                                 11           11            0      MATCH

  no                                                  4            4            0      MATCH

  nz                                                  1            1            0      MATCH

  pa                                                 22           22            0      MATCH

  pe                                                 68           68            0      MATCH

  ph                                                  1            1            0      MATCH

  pl                                                 20           20            0      MATCH

  pr                                                 76           76            0      MATCH

  py                                                 17           17            0      MATCH

  ro                                                 10           10            0      MATCH

  se                                                182          182            0      MATCH

  spain                                               1            1            0      MATCH

  sv                                                 21           21            0      MATCH

  tr                                                  1            1            0      MATCH

  us                                             154861       154861            0      MATCH

  uy                                                 42           42            0      MATCH

  ve                                                193          193            0      MATCH

  za                                                  1            1            0      MATCH

  ✅ PASS: counts match for all 53 value(s).

  Match % (values): 53/53 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: visitor\_\_platform\_os\_id

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=102.22s | rows=8

  SELECT visitor\_\_platform\_os\_id, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY visitor\_\_platform\_os\_id ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=58.79s | rows=8

  SELECT visitor\_\_platform\_os\_id, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY visitor\_\_platform\_os\_id ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  1249                                             1877         1877            0      MATCH

  1250                                            34899        34899            0      MATCH

  263                                             17486        17486            0      MATCH

  6                                                5819         5819            0      MATCH

  7                                               25812        25812            0      MATCH

  8                                                2490         2490            0      MATCH

  9                                               40987        40987            0      MATCH

  None                                            44697        44697            0      MATCH

  ✅ PASS: counts match for all 8 value(s).

  Match % (values): 8/8 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: slot\_\_max\_duration

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=99.78s | rows=266

  SELECT slot\_\_max\_duration, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_max\_duration ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=59.03s | rows=266

  SELECT slot\_\_max\_duration, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY slot\_\_max\_duration ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  10                                               1070         1070            0      MATCH

  100                                                44           44            0      MATCH

  1000                                              119          119            0      MATCH

  10000                                               9            9            0      MATCH

  101                                                45           45            0      MATCH

  103                                                15           15            0      MATCH

  104                                                26           26            0      MATCH

  105                                             13549        13549            0      MATCH

  106                                               390          390            0      MATCH

  107                                                32           32            0      MATCH

  108                                                21           21            0      MATCH

  109                                              2393         2393            0      MATCH

  11                                                182          182            0      MATCH

  110                                               158          158            0      MATCH

  111                                               119          119            0      MATCH

  112                                                21           21            0      MATCH

  113                                                 3            3            0      MATCH

  114                                                39           39            0      MATCH

  115                                                67           67            0      MATCH

  116                                                12           12            0      MATCH

  117                                               111          111            0      MATCH

  118                                                 1            1            0      MATCH

  119                                               363          363            0      MATCH

  120                                             12139        12139            0      MATCH

  121                                              1136         1136            0      MATCH

  122                                              1075         1075            0      MATCH

  123                                                49           49            0      MATCH

  124                                               408          408            0      MATCH

  125                                               100          100            0      MATCH

  126                                                40           40            0      MATCH

  127                                                15           15            0      MATCH

  128                                                74           74            0      MATCH

  129                                                91           91            0      MATCH

  130                                                73           73            0      MATCH

  131                                                44           44            0      MATCH

  132                                                 3            3            0      MATCH

  133                                                39           39            0      MATCH

  134                                               221          221            0      MATCH

  135                                               936          936            0      MATCH

  136                                                 9            9            0      MATCH

  137                                                19           19            0      MATCH

  140                                                37           37            0      MATCH

  143                                                14           14            0      MATCH

  144                                                70           70            0      MATCH

  145                                                 3            3            0      MATCH

  146                                                 1            1            0      MATCH

  147                                                 4            4            0      MATCH

  148                                                 1            1            0      MATCH

  149                                                95           95            0      MATCH

  15                                               4214         4214            0      MATCH

  150                                              9444         9444            0      MATCH

  151                                               799          799            0      MATCH

  152                                                33           33            0      MATCH

  153                                                 1            1            0      MATCH

  155                                                52           52            0      MATCH

  156                                                13           13            0      MATCH

  157                                                17           17            0      MATCH

  158                                                 5            5            0      MATCH

  159                                                16           16            0      MATCH

  16                                                109          109            0      MATCH

  160                                               113          113            0      MATCH

  161                                                22           22            0      MATCH

  162                                               161          161            0      MATCH

  163                                                26           26            0      MATCH

  164                                                10           10            0      MATCH

  165                                              1892         1892            0      MATCH

  167                                               253          253            0      MATCH

  168                                               218          218            0      MATCH

  17                                                 13           13            0      MATCH

  170                                               167          167            0      MATCH

  171                                                15           15            0      MATCH

  172                                                20           20            0      MATCH

  173                                                 1            1            0      MATCH

  174                                                27           27            0      MATCH

  175                                                56           56            0      MATCH

  177                                                14           14            0      MATCH

  178                                                 2            2            0      MATCH

  179                                                68           68            0      MATCH

  18                                                  1            1            0      MATCH

  180                                              6810         6810            0      MATCH

  181                                               845          845            0      MATCH

  182                                               351          351            0      MATCH

  183                                              1979         1979            0      MATCH

  184                                                23           23            0      MATCH

  185                                               108          108            0      MATCH

  186                                                34           34            0      MATCH

  187                                                37           37            0      MATCH

  188                                                13           13            0      MATCH

  189                                                 3            3            0      MATCH

  19                                                  5            5            0      MATCH

  190                                               319          319            0      MATCH

  191                                                18           18            0      MATCH

  192                                                14           14            0      MATCH

  193                                                 1            1            0      MATCH

  194                                                12           12            0      MATCH

  195                                              1437         1437            0      MATCH

  196                                                61           61            0      MATCH

  197                                                10           10            0      MATCH

  199                                                 1            1            0      MATCH

  20                                               1129         1129            0      MATCH

  200                                                75           75            0      MATCH

  201                                                 2            2            0      MATCH

  202                                                29           29            0      MATCH

  204                                                 6            6            0      MATCH

  207                                                42           42            0      MATCH

  209                                               266          266            0      MATCH

  21                                                 29           29            0      MATCH

  210                                              6079         6079            0      MATCH

  211                                               416          416            0      MATCH

  212                                                 1            1            0      MATCH

  214                                                 7            7            0      MATCH

  215                                                10           10            0      MATCH

  216                                                 1            1            0      MATCH

  217                                                 1            1            0      MATCH

  22                                                 13           13            0      MATCH

  220                                                 1            1            0      MATCH

  221                                                 3            3            0      MATCH

  222                                                 1            1            0      MATCH

  223                                                 6            6            0      MATCH

  225                                               626          626            0      MATCH

  227                                                 3            3            0      MATCH

  229                                                16           16            0      MATCH

  23                                                  3            3            0      MATCH

  230                                                50           50            0      MATCH

  234                                                 5            5            0      MATCH

  235                                               201          201            0      MATCH

  237                                               320          320            0      MATCH

  239                                               189          189            0      MATCH

  24                                                  8            8            0      MATCH

  240                                              2666         2666            0      MATCH

  241                                               271          271            0      MATCH

  242                                                 1            1            0      MATCH

  245                                                 9            9            0      MATCH

  246                                                 1            1            0      MATCH

  247                                                 3            3            0      MATCH

  25                                                  9            9            0      MATCH

  250                                                 1            1            0      MATCH

  254                                                 1            1            0      MATCH

  255                                                90           90            0      MATCH

  257                                                 3            3            0      MATCH

  26                                                  1            1            0      MATCH

  260                                               536          536            0      MATCH

  261                                                 3            3            0      MATCH

  262                                                 1            1            0      MATCH

  265                                                 7            7            0      MATCH

  267                                                 1            1            0      MATCH

  27                                                  6            6            0      MATCH

  270                                              4467         4467            0      MATCH

  275                                                87           87            0      MATCH

  28                                                  1            1            0      MATCH

  280                                                 5            5            0      MATCH

  285                                                79           79            0      MATCH

  29                                                  1            1            0      MATCH

  290                                                29           29            0      MATCH

  297                                                23           23            0      MATCH

  30                                              21004        21004            0      MATCH

  300                                              1811         1811            0      MATCH

  30000                                              20           20            0      MATCH

  301                                               135          135            0      MATCH

  302                                                54           54            0      MATCH

  31                                               2518         2518            0      MATCH

  310                                                 5            5            0      MATCH

  315                                               150          150            0      MATCH

  32                                                581          581            0      MATCH

  320                                                15           15            0      MATCH

  329                                                 7            7            0      MATCH

  33                                                 99           99            0      MATCH

  330                                              1025         1025            0      MATCH

  331                                               112          112            0      MATCH

  34                                                  6            6            0      MATCH

  345                                              6549         6549            0      MATCH

  346                                                13           13            0      MATCH

  35                                                509          509            0      MATCH

  350                                                19           19            0      MATCH

  356                                                14           14            0      MATCH

  36                                                  4            4            0      MATCH

  360                                              1759         1759            0      MATCH

  3600                                               13           13            0      MATCH

  368                                                33           33            0      MATCH

  369                                                22           22            0      MATCH

  37                                                 17           17            0      MATCH

  375                                               125          125            0      MATCH

  38                                                  3            3            0      MATCH

  380                                                19           19            0      MATCH

  39                                                 52           52            0      MATCH

  390                                               539          539            0      MATCH

  40                                                647          647            0      MATCH

  400                                                30           30            0      MATCH

  405                                                17           17            0      MATCH

  41                                                 30           30            0      MATCH

  42                                                 11           11            0      MATCH

  420                                                14           14            0      MATCH

  43                                               1718         1718            0      MATCH

  430                                                17           17            0      MATCH

  44                                                 13           13            0      MATCH

  45                                                198          198            0      MATCH

  450                                              1110         1110            0      MATCH

  46                                                  8            8            0      MATCH

  47                                                 53           53            0      MATCH

  475                                                 1            1            0      MATCH

  48                                                  6            6            0      MATCH

  480                                               391          391            0      MATCH

  49                                                 13           13            0      MATCH

  5                                                 771          771            0      MATCH

  50                                                 86           86            0      MATCH

  50000                                               1            1            0      MATCH

  508                                                 4            4            0      MATCH

  51                                                 13           13            0      MATCH

  52                                                 19           19            0      MATCH

  53                                                  9            9            0      MATCH

  54                                                  8            8            0      MATCH

  55                                                 20           20            0      MATCH

  56                                                  4            4            0      MATCH

  560                                                 1            1            0      MATCH

  57                                                  7            7            0      MATCH

  58                                                  6            6            0      MATCH

  59                                                185          185            0      MATCH

  6                                                 115          115            0      MATCH

  60                                               5829         5829            0      MATCH

  61                                                 81           81            0      MATCH

  610                                                 1            1            0      MATCH

  62                                                587          587            0      MATCH

  63                                              11958        11958            0      MATCH

  64                                                 12           12            0      MATCH

  65                                                 50           50            0      MATCH

  66                                                 51           51            0      MATCH

  67                                                 36           36            0      MATCH

  68                                                 10           10            0      MATCH

  69                                                  8            8            0      MATCH

  7                                                2296         2296            0      MATCH

  70                                                 47           47            0      MATCH

  71                                                  3            3            0      MATCH

  72                                                  3            3            0      MATCH

  73                                                 11           11            0      MATCH

  74                                                 11           11            0      MATCH

  75                                                368          368            0      MATCH

  752                                                30           30            0      MATCH

  76                                                 25           25            0      MATCH

  764                                                 1            1            0      MATCH

  77                                                246          246            0      MATCH

  772                                                 2            2            0      MATCH

  78                                                127          127            0      MATCH

  79                                                 22           22            0      MATCH

  80                                                357          357            0      MATCH

  81                                                 14           14            0      MATCH

  82                                                 13           13            0      MATCH

  83                                                  3            3            0      MATCH

  84                                                  4            4            0      MATCH

  85                                                 40           40            0      MATCH

  86                                                  7            7            0      MATCH

  86400                                              94           94            0      MATCH

  87                                                  1            1            0      MATCH

  88                                                  6            6            0      MATCH

  89                                                 19           19            0      MATCH

  90                                               3434         3434            0      MATCH

  900                                                22           22            0      MATCH

  91                                               1779         1779            0      MATCH

  92                                              12386        12386            0      MATCH

  93                                                912          912            0      MATCH

  94                                               1123         1123            0      MATCH

  95                                                 28           28            0      MATCH

  96                                                 53           53            0      MATCH

  97                                                 22           22            0      MATCH

  98                                                  8            8            0      MATCH

  99                                                 25           25            0      MATCH

  None                                             5956         5956            0      MATCH

  ✅ PASS: counts match for all 266 value(s).

  Match % (values): 266/266 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: slot\_\_initial\_num\_ads

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=103.41s | rows=37

  SELECT slot\_\_initial\_num\_ads, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY slot\_\_initial\_num\_ads ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=226.00s | rows=37

  SELECT slot\_\_initial\_num\_ads, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY slot\_\_initial\_num\_ads ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  0                                                 185          185            0      MATCH

  1                                               50239        50239            0      MATCH

  10                                               3687         3687            0      MATCH

  11                                               3205         3205            0      MATCH

  12                                               3031         3031            0      MATCH

  13                                               2872         2872            0      MATCH

  14                                               1629         1629            0      MATCH

  15                                                678          678            0      MATCH

  16                                                414          414            0      MATCH

  17                                                394          394            0      MATCH

  18                                                150          150            0      MATCH

  19                                                 50           50            0      MATCH

  2                                               13012        13012            0      MATCH

  20                                                 42           42            0      MATCH

  21                                                  2            2            0      MATCH

  22                                                  2            2            0      MATCH

  23                                                  4            4            0      MATCH

  24                                                  2            2            0      MATCH

  3                                               24427        24427            0      MATCH

  4                                               19446        19446            0      MATCH

  46                                                138          138            0      MATCH

  48                                                 48           48            0      MATCH

  5                                               15215        15215            0      MATCH

  50                                                 50           50            0      MATCH

  51                                                153          153            0      MATCH

  52                                                208          208            0      MATCH

  53                                                159          159            0      MATCH

  54                                                 54           54            0      MATCH

  55                                                330          330            0      MATCH

  56                                                 56           56            0      MATCH

  57                                                 57           57            0      MATCH

  58                                                 58           58            0      MATCH

  6                                               11680        11680            0      MATCH

  7                                                7355         7355            0      MATCH

  8                                                6574         6574            0      MATCH

  9                                                4779         4779            0      MATCH

  None                                             3682         3682            0      MATCH

  ✅ PASS: counts match for all 37 value(s).

  Match % (values): 37/37 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: advertisement\_\_is\_fallback

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=119.04s | rows=2

  SELECT advertisement\_\_is\_fallback, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY advertisement\_\_is\_fallback ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=65.97s | rows=2

  SELECT advertisement\_\_is\_fallback, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY advertisement\_\_is\_fallback ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  False                                          118125       118125            0      MATCH

  True                                            55942        55942            0      MATCH

  ✅ PASS: counts match for all 2 value(s).

  Match % (values): 2/2 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: advertisement\_\_ad\_priority\_type

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=103.36s | rows=5

  SELECT advertisement\_\_ad\_priority\_type, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY advertisement\_\_ad\_priority\_type ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=58.83s | rows=5

  SELECT advertisement\_\_ad\_priority\_type, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY advertisement\_\_ad\_priority\_type ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  ABOVE\_PAYING\_ADS                                36196        36196            0      MATCH

  AMONGST\_PAYING\_ADS                                  3            3            0      MATCH

  BELOW\_PAYING\_ADS                                49330        49330            0      MATCH

  None                                            79437        79437            0      MATCH

  SPONSORSHIP                                      9101         9101            0      MATCH

  ✅ PASS: counts match for all 5 value(s).

  Match % (values): 5/5 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: auction\_\_integration\_type

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=101.35s | rows=3

  SELECT auction\_\_integration\_type, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_integration\_type ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=58.78s | rows=1

  SELECT auction\_\_integration\_type, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY auction\_\_integration\_type ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  NORMAL                                          14180            0        14180   MISMATCH

  None                                           148340       174067       -25727   MISMATCH

  PG\_TD                                           11547            0        11547   MISMATCH

  ❌ FAIL: count mismatches for 3 of 3 value(s).

  Match % (values): 0/3 (0.00%)

  Match % (volume): 148,340/174,067 (85.22%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: auction\_\_invite\_deal\_size

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=104.93s | rows=650

  SELECT auction\_\_invite\_deal\_size, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY auction\_\_invite\_deal\_size ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=56.31s | rows=1

  SELECT auction\_\_invite\_deal\_size, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY auction\_\_invite\_deal\_size ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  0                                                 127            0          127   MISMATCH

  1                                               12079            0        12079   MISMATCH

  10                                                 59            0           59   MISMATCH

  100                                                63            0           63   MISMATCH

  101                                                24            0           24   MISMATCH

  102                                                51            0           51   MISMATCH

  103                                                31            0           31   MISMATCH

  104                                                25            0           25   MISMATCH

  105                                                33            0           33   MISMATCH

  106                                                21            0           21   MISMATCH

  107                                                27            0           27   MISMATCH

  108                                                31            0           31   MISMATCH

  109                                                45            0           45   MISMATCH

  11                                                103            0          103   MISMATCH

  110                                                13            0           13   MISMATCH

  111                                                28            0           28   MISMATCH

  112                                                22            0           22   MISMATCH

  113                                                34            0           34   MISMATCH

  114                                                38            0           38   MISMATCH

  115                                                24            0           24   MISMATCH

  116                                                48            0           48   MISMATCH

  117                                                32            0           32   MISMATCH

  118                                                30            0           30   MISMATCH

  119                                                68            0           68   MISMATCH

  12                                                 69            0           69   MISMATCH

  120                                                63            0           63   MISMATCH

  121                                                22            0           22   MISMATCH

  122                                                32            0           32   MISMATCH

  123                                                18            0           18   MISMATCH

  124                                                40            0           40   MISMATCH

  125                                                41            0           41   MISMATCH

  126                                                31            0           31   MISMATCH

  127                                                30            0           30   MISMATCH

  128                                                35            0           35   MISMATCH

  129                                                19            0           19   MISMATCH

  13                                                 43            0           43   MISMATCH

  130                                                11            0           11   MISMATCH

  131                                                14            0           14   MISMATCH

  132                                                25            0           25   MISMATCH

  133                                                 4            0            4   MISMATCH

  134                                                28            0           28   MISMATCH

  135                                                 5            0            5   MISMATCH

  136                                                13            0           13   MISMATCH

  137                                                21            0           21   MISMATCH

  138                                                15            0           15   MISMATCH

  139                                                33            0           33   MISMATCH

  14                                                 53            0           53   MISMATCH

  140                                                25            0           25   MISMATCH

  141                                                30            0           30   MISMATCH

  142                                                 3            0            3   MISMATCH

  143                                                 4            0            4   MISMATCH

  144                                                 3            0            3   MISMATCH

  145                                                 5            0            5   MISMATCH

  146                                                 8            0            8   MISMATCH

  147                                                 7            0            7   MISMATCH

  148                                                 7            0            7   MISMATCH

  149                                                 5            0            5   MISMATCH

  15                                                104            0          104   MISMATCH

  150                                                12            0           12   MISMATCH

  151                                                 6            0            6   MISMATCH

  152                                                13            0           13   MISMATCH

  153                                                 9            0            9   MISMATCH

  154                                                 3            0            3   MISMATCH

  155                                                 5            0            5   MISMATCH

  156                                                13            0           13   MISMATCH

  157                                                 5            0            5   MISMATCH

  158                                                 3            0            3   MISMATCH

  159                                                 2            0            2   MISMATCH

  16                                                 42            0           42   MISMATCH

  161                                                 1            0            1   MISMATCH

  162                                                 5            0            5   MISMATCH

  163                                                 3            0            3   MISMATCH

  164                                                 2            0            2   MISMATCH

  165                                                 1            0            1   MISMATCH

  166                                                 4            0            4   MISMATCH

  168                                                 6            0            6   MISMATCH

  169                                                 3            0            3   MISMATCH

  17                                                 48            0           48   MISMATCH

  170                                                 3            0            3   MISMATCH

  171                                                 3            0            3   MISMATCH

  172                                                 1            0            1   MISMATCH

  174                                                 3            0            3   MISMATCH

  175                                                 9            0            9   MISMATCH

  176                                                 8            0            8   MISMATCH

  177                                                11            0           11   MISMATCH

  178                                                12            0           12   MISMATCH

  179                                                11            0           11   MISMATCH

  18                                                 77            0           77   MISMATCH

  180                                                 4            0            4   MISMATCH

  181                                                14            0           14   MISMATCH

  182                                                19            0           19   MISMATCH

  183                                                15            0           15   MISMATCH

  184                                                15            0           15   MISMATCH

  185                                                 9            0            9   MISMATCH

  186                                                20            0           20   MISMATCH

  187                                                29            0           29   MISMATCH

  188                                                15            0           15   MISMATCH

  189                                                16            0           16   MISMATCH

  19                                                 89            0           89   MISMATCH

  190                                                14            0           14   MISMATCH

  191                                                11            0           11   MISMATCH

  192                                                19            0           19   MISMATCH

  193                                                22            0           22   MISMATCH

  194                                                14            0           14   MISMATCH

  195                                                15            0           15   MISMATCH

  196                                                 5            0            5   MISMATCH

  197                                                17            0           17   MISMATCH

  198                                                 6            0            6   MISMATCH

  199                                                 9            0            9   MISMATCH

  2                                                 111            0          111   MISMATCH

  20                                                 98            0           98   MISMATCH

  200                                                15            0           15   MISMATCH

  201                                                13            0           13   MISMATCH

  202                                                13            0           13   MISMATCH

  203                                                 9            0            9   MISMATCH

  204                                                13            0           13   MISMATCH

  205                                                10            0           10   MISMATCH

  206                                                21            0           21   MISMATCH

  207                                                21            0           21   MISMATCH

  208                                                22            0           22   MISMATCH

  209                                                29            0           29   MISMATCH

  21                                                 89            0           89   MISMATCH

  210                                                51            0           51   MISMATCH

  211                                                31            0           31   MISMATCH

  212                                                32            0           32   MISMATCH

  213                                                16            0           16   MISMATCH

  214                                                12            0           12   MISMATCH

  215                                                 9            0            9   MISMATCH

  216                                                 9            0            9   MISMATCH

  217                                                11            0           11   MISMATCH

  218                                                 7            0            7   MISMATCH

  219                                                13            0           13   MISMATCH

  22                                                 73            0           73   MISMATCH

  220                                                 7            0            7   MISMATCH

  221                                                 5            0            5   MISMATCH

  222                                                 9            0            9   MISMATCH

  223                                                13            0           13   MISMATCH

  224                                                14            0           14   MISMATCH

  225                                                14            0           14   MISMATCH

  226                                                17            0           17   MISMATCH

  227                                                 9            0            9   MISMATCH

  228                                                19            0           19   MISMATCH

  229                                                21            0           21   MISMATCH

  23                                                 90            0           90   MISMATCH

  230                                                19            0           19   MISMATCH

  231                                                22            0           22   MISMATCH

  232                                                41            0           41   MISMATCH

  233                                                33            0           33   MISMATCH

  234                                                30            0           30   MISMATCH

  235                                                33            0           33   MISMATCH

  236                                                47            0           47   MISMATCH

  237                                                37            0           37   MISMATCH

  238                                                34            0           34   MISMATCH

  239                                                47            0           47   MISMATCH

  24                                                 60            0           60   MISMATCH

  240                                                41            0           41   MISMATCH

  241                                                28            0           28   MISMATCH

  242                                                32            0           32   MISMATCH

  243                                                21            0           21   MISMATCH

  244                                                42            0           42   MISMATCH

  245                                                17            0           17   MISMATCH

  246                                                24            0           24   MISMATCH

  247                                                15            0           15   MISMATCH

  248                                                16            0           16   MISMATCH

  249                                                 8            0            8   MISMATCH

  25                                                 56            0           56   MISMATCH

  250                                                 4            0            4   MISMATCH

  251                                                 4            0            4   MISMATCH

  252                                                 9            0            9   MISMATCH

  253                                                 5            0            5   MISMATCH

  254                                                 6            0            6   MISMATCH

  255                                                 5            0            5   MISMATCH

  256                                                 3            0            3   MISMATCH

  257                                                 2            0            2   MISMATCH

  258                                                 1            0            1   MISMATCH

  259                                                 4            0            4   MISMATCH

  26                                                 41            0           41   MISMATCH

  260                                                 5            0            5   MISMATCH

  261                                                 7            0            7   MISMATCH

  262                                                17            0           17   MISMATCH

  263                                                14            0           14   MISMATCH

  264                                                 2            0            2   MISMATCH

  265                                                 4            0            4   MISMATCH

  266                                                 4            0            4   MISMATCH

  267                                                 2            0            2   MISMATCH

  268                                                 5            0            5   MISMATCH

  269                                                 1            0            1   MISMATCH

  27                                                 46            0           46   MISMATCH

  270                                                 2            0            2   MISMATCH

  271                                                 3            0            3   MISMATCH

  272                                                 1            0            1   MISMATCH

  274                                                 3            0            3   MISMATCH

  275                                                 4            0            4   MISMATCH

  276                                                 1            0            1   MISMATCH

  277                                                 8            0            8   MISMATCH

  278                                                 1            0            1   MISMATCH

  279                                                 2            0            2   MISMATCH

  28                                                 43            0           43   MISMATCH

  280                                                 2            0            2   MISMATCH

  281                                                 3            0            3   MISMATCH

  282                                                 2            0            2   MISMATCH

  283                                                 4            0            4   MISMATCH

  284                                                10            0           10   MISMATCH

  285                                                 7            0            7   MISMATCH

  286                                                 5            0            5   MISMATCH

  287                                                 9            0            9   MISMATCH

  288                                                 1            0            1   MISMATCH

  29                                                 54            0           54   MISMATCH

  290                                                 4            0            4   MISMATCH

  291                                                 3            0            3   MISMATCH

  292                                                 4            0            4   MISMATCH

  293                                                 5            0            5   MISMATCH

  294                                                 7            0            7   MISMATCH

  295                                                 4            0            4   MISMATCH

  296                                                 7            0            7   MISMATCH

  298                                                 1            0            1   MISMATCH

  299                                                 3            0            3   MISMATCH

  3                                                  57            0           57   MISMATCH

  30                                                 24            0           24   MISMATCH

  300                                                 1            0            1   MISMATCH

  301                                                 3            0            3   MISMATCH

  302                                                 1            0            1   MISMATCH

  303                                                 1            0            1   MISMATCH

  304                                                 2            0            2   MISMATCH

  306                                                 2            0            2   MISMATCH

  307                                                 4            0            4   MISMATCH

  308                                                 3            0            3   MISMATCH

  31                                                110            0          110   MISMATCH

  310                                                 1            0            1   MISMATCH

  311                                                 1            0            1   MISMATCH

  312                                                 3            0            3   MISMATCH

  313                                                 4            0            4   MISMATCH

  314                                                 9            0            9   MISMATCH

  315                                                10            0           10   MISMATCH

  316                                                12            0           12   MISMATCH

  317                                                 3            0            3   MISMATCH

  318                                                 9            0            9   MISMATCH

  319                                                 3            0            3   MISMATCH

  32                                                 48            0           48   MISMATCH

  320                                                 1            0            1   MISMATCH

  321                                                 2            0            2   MISMATCH

  322                                                 3            0            3   MISMATCH

  323                                                 8            0            8   MISMATCH

  324                                                 6            0            6   MISMATCH

  325                                                 1            0            1   MISMATCH

  326                                                 2            0            2   MISMATCH

  327                                                 5            0            5   MISMATCH

  328                                                 4            0            4   MISMATCH

  329                                                 9            0            9   MISMATCH

  33                                                 29            0           29   MISMATCH

  330                                                 4            0            4   MISMATCH

  331                                                 3            0            3   MISMATCH

  332                                                 6            0            6   MISMATCH

  333                                                 8            0            8   MISMATCH

  334                                                13            0           13   MISMATCH

  335                                                15            0           15   MISMATCH

  336                                                17            0           17   MISMATCH

  337                                                11            0           11   MISMATCH

  338                                                10            0           10   MISMATCH

  339                                                 7            0            7   MISMATCH

  34                                                 26            0           26   MISMATCH

  340                                                10            0           10   MISMATCH

  341                                                 6            0            6   MISMATCH

  342                                                14            0           14   MISMATCH

  343                                                14            0           14   MISMATCH

  344                                                10            0           10   MISMATCH

  345                                                17            0           17   MISMATCH

  346                                                 9            0            9   MISMATCH

  347                                                13            0           13   MISMATCH

  348                                                18            0           18   MISMATCH

  349                                                19            0           19   MISMATCH

  35                                                 33            0           33   MISMATCH

  350                                                40            0           40   MISMATCH

  351                                                17            0           17   MISMATCH

  352                                                31            0           31   MISMATCH

  353                                                19            0           19   MISMATCH

  354                                                 8            0            8   MISMATCH

  355                                                29            0           29   MISMATCH

  356                                                16            0           16   MISMATCH

  357                                                26            0           26   MISMATCH

  358                                                33            0           33   MISMATCH

  359                                                39            0           39   MISMATCH

  36                                                 35            0           35   MISMATCH

  360                                                33            0           33   MISMATCH

  361                                                20            0           20   MISMATCH

  362                                                16            0           16   MISMATCH

  363                                                17            0           17   MISMATCH

  364                                                21            0           21   MISMATCH

  365                                                11            0           11   MISMATCH

  366                                                18            0           18   MISMATCH

  367                                                31            0           31   MISMATCH

  368                                                29            0           29   MISMATCH

  369                                                 9            0            9   MISMATCH

  37                                                 32            0           32   MISMATCH

  370                                                 9            0            9   MISMATCH

  371                                                15            0           15   MISMATCH

  372                                                 5            0            5   MISMATCH

  373                                                 5            0            5   MISMATCH

  374                                                 4            0            4   MISMATCH

  375                                                 8            0            8   MISMATCH

  376                                                15            0           15   MISMATCH

  377                                                 5            0            5   MISMATCH

  378                                                16            0           16   MISMATCH

  379                                                 4            0            4   MISMATCH

  38                                                 24            0           24   MISMATCH

  380                                                 8            0            8   MISMATCH

  381                                                 6            0            6   MISMATCH

  382                                                15            0           15   MISMATCH

  383                                                12            0           12   MISMATCH

  384                                                26            0           26   MISMATCH

  385                                                 1            0            1   MISMATCH

  386                                                 2            0            2   MISMATCH

  387                                                 7            0            7   MISMATCH

  388                                                 5            0            5   MISMATCH

  389                                                11            0           11   MISMATCH

  39                                                 32            0           32   MISMATCH

  390                                                23            0           23   MISMATCH

  391                                                 9            0            9   MISMATCH

  392                                                 9            0            9   MISMATCH

  393                                                24            0           24   MISMATCH

  394                                                11            0           11   MISMATCH

  395                                                 7            0            7   MISMATCH

  396                                                19            0           19   MISMATCH

  397                                                15            0           15   MISMATCH

  398                                                 4            0            4   MISMATCH

  399                                                 5            0            5   MISMATCH

  4                                                 177            0          177   MISMATCH

  40                                                 44            0           44   MISMATCH

  400                                                15            0           15   MISMATCH

  401                                                 5            0            5   MISMATCH

  402                                                 8            0            8   MISMATCH

  403                                                 1            0            1   MISMATCH

  404                                                 1            0            1   MISMATCH

  405                                                 6            0            6   MISMATCH

  406                                                 6            0            6   MISMATCH

  407                                                 2            0            2   MISMATCH

  408                                                11            0           11   MISMATCH

  409                                                 6            0            6   MISMATCH

  41                                                155            0          155   MISMATCH

  410                                                15            0           15   MISMATCH

  411                                                18            0           18   MISMATCH

  412                                                16            0           16   MISMATCH

  413                                                 8            0            8   MISMATCH

  414                                                 4            0            4   MISMATCH

  416                                                 2            0            2   MISMATCH

  417                                                 4            0            4   MISMATCH

  418                                                 1            0            1   MISMATCH

  419                                                 2            0            2   MISMATCH

  42                                                 58            0           58   MISMATCH

  420                                                 7            0            7   MISMATCH

  421                                                15            0           15   MISMATCH

  422                                                18            0           18   MISMATCH

  423                                                 7            0            7   MISMATCH

  424                                                19            0           19   MISMATCH

  425                                                 3            0            3   MISMATCH

  426                                                 5            0            5   MISMATCH

  427                                                 2            0            2   MISMATCH

  428                                                 1            0            1   MISMATCH

  429                                                 2            0            2   MISMATCH

  43                                                 51            0           51   MISMATCH

  430                                                 1            0            1   MISMATCH

  431                                                 1            0            1   MISMATCH

  432                                                 1            0            1   MISMATCH

  433                                                 4            0            4   MISMATCH

  434                                                 3            0            3   MISMATCH

  435                                                 1            0            1   MISMATCH

  436                                                 6            0            6   MISMATCH

  437                                                 6            0            6   MISMATCH

  438                                                 4            0            4   MISMATCH

  439                                                 3            0            3   MISMATCH

  44                                                 67            0           67   MISMATCH

  440                                                 4            0            4   MISMATCH

  441                                                18            0           18   MISMATCH

  442                                                 1            0            1   MISMATCH

  443                                                23            0           23   MISMATCH

  444                                                13            0           13   MISMATCH

  445                                                 7            0            7   MISMATCH

  446                                                12            0           12   MISMATCH

  447                                                 2            0            2   MISMATCH

  448                                                 6            0            6   MISMATCH

  45                                                 19            0           19   MISMATCH

  450                                                 1            0            1   MISMATCH

  452                                                 2            0            2   MISMATCH

  454                                                 1            0            1   MISMATCH

  455                                                 2            0            2   MISMATCH

  456                                                 1            0            1   MISMATCH

  457                                                 1            0            1   MISMATCH

  458                                                 8            0            8   MISMATCH

  459                                                 2            0            2   MISMATCH

  46                                                 55            0           55   MISMATCH

  460                                                 1            0            1   MISMATCH

  461                                                 1            0            1   MISMATCH

  462                                                 2            0            2   MISMATCH

  463                                                 1            0            1   MISMATCH

  465                                                 2            0            2   MISMATCH

  466                                                 1            0            1   MISMATCH

  469                                                 1            0            1   MISMATCH

  47                                                 46            0           46   MISMATCH

  470                                                 2            0            2   MISMATCH

  472                                                 3            0            3   MISMATCH

  474                                                 3            0            3   MISMATCH

  476                                                 2            0            2   MISMATCH

  479                                                 1            0            1   MISMATCH

  48                                                 53            0           53   MISMATCH

  480                                                 1            0            1   MISMATCH

  481                                                 1            0            1   MISMATCH

  486                                                 1            0            1   MISMATCH

  487                                                 3            0            3   MISMATCH

  488                                                 2            0            2   MISMATCH

  489                                                 3            0            3   MISMATCH

  49                                                186            0          186   MISMATCH

  490                                                 2            0            2   MISMATCH

  498                                                 2            0            2   MISMATCH

  499                                                 2            0            2   MISMATCH

  5                                                  79            0           79   MISMATCH

  50                                                 28            0           28   MISMATCH

  504                                                 1            0            1   MISMATCH

  505                                                 2            0            2   MISMATCH

  506                                                 1            0            1   MISMATCH

  51                                                 35            0           35   MISMATCH

  514                                                 3            0            3   MISMATCH

  516                                                 2            0            2   MISMATCH

  52                                                 27            0           27   MISMATCH

  521                                                 1            0            1   MISMATCH

  523                                                 1            0            1   MISMATCH

  525                                                 1            0            1   MISMATCH

  526                                                 3            0            3   MISMATCH

  527                                                 1            0            1   MISMATCH

  528                                                 1            0            1   MISMATCH

  529                                                 5            0            5   MISMATCH

  53                                                 35            0           35   MISMATCH

  530                                                 1            0            1   MISMATCH

  531                                                 2            0            2   MISMATCH

  532                                                 1            0            1   MISMATCH

  534                                                 2            0            2   MISMATCH

  535                                                 2            0            2   MISMATCH

  536                                                 2            0            2   MISMATCH

  537                                                 3            0            3   MISMATCH

  54                                                 71            0           71   MISMATCH

  540                                                 1            0            1   MISMATCH

  541                                                 3            0            3   MISMATCH

  542                                                 7            0            7   MISMATCH

  543                                                 3            0            3   MISMATCH

  544                                                 3            0            3   MISMATCH

  545                                                 5            0            5   MISMATCH

  546                                                 2            0            2   MISMATCH

  547                                                 2            0            2   MISMATCH

  548                                                 3            0            3   MISMATCH

  549                                                 3            0            3   MISMATCH

  55                                                 54            0           54   MISMATCH

  550                                                 5            0            5   MISMATCH

  551                                                 1            0            1   MISMATCH

  552                                                 2            0            2   MISMATCH

  553                                                 3            0            3   MISMATCH

  555                                                 5            0            5   MISMATCH

  556                                                 2            0            2   MISMATCH

  557                                                 5            0            5   MISMATCH

  558                                                 1            0            1   MISMATCH

  559                                                 3            0            3   MISMATCH

  56                                                 56            0           56   MISMATCH

  560                                                 2            0            2   MISMATCH

  562                                                 1            0            1   MISMATCH

  563                                                 5            0            5   MISMATCH

  564                                                 2            0            2   MISMATCH

  565                                                 6            0            6   MISMATCH

  566                                                 7            0            7   MISMATCH

  567                                                10            0           10   MISMATCH

  568                                                 6            0            6   MISMATCH

  569                                                 7            0            7   MISMATCH

  57                                                 68            0           68   MISMATCH

  570                                                 6            0            6   MISMATCH

  571                                                 8            0            8   MISMATCH

  572                                                11            0           11   MISMATCH

  573                                                 2            0            2   MISMATCH

  574                                                11            0           11   MISMATCH

  575                                                 9            0            9   MISMATCH

  576                                                12            0           12   MISMATCH

  577                                                 1            0            1   MISMATCH

  578                                                 6            0            6   MISMATCH

  579                                                 1            0            1   MISMATCH

  58                                                 55            0           55   MISMATCH

  580                                                 5            0            5   MISMATCH

  581                                                 2            0            2   MISMATCH

  582                                                 3            0            3   MISMATCH

  583                                                 8            0            8   MISMATCH

  584                                                 4            0            4   MISMATCH

  586                                                 3            0            3   MISMATCH

  587                                                 5            0            5   MISMATCH

  588                                                 3            0            3   MISMATCH

  589                                                 4            0            4   MISMATCH

  59                                                 39            0           39   MISMATCH

  590                                                 6            0            6   MISMATCH

  591                                                 2            0            2   MISMATCH

  592                                                 6            0            6   MISMATCH

  593                                                 2            0            2   MISMATCH

  594                                                 3            0            3   MISMATCH

  595                                                 5            0            5   MISMATCH

  596                                                 5            0            5   MISMATCH

  597                                                 4            0            4   MISMATCH

  598                                                 3            0            3   MISMATCH

  599                                                 3            0            3   MISMATCH

  6                                                 218            0          218   MISMATCH

  60                                                 60            0           60   MISMATCH

  600                                                 6            0            6   MISMATCH

  601                                                 4            0            4   MISMATCH

  602                                                 2            0            2   MISMATCH

  603                                                 7            0            7   MISMATCH

  604                                                 1            0            1   MISMATCH

  605                                                14            0           14   MISMATCH

  606                                                 1            0            1   MISMATCH

  607                                                 3            0            3   MISMATCH

  608                                                 9            0            9   MISMATCH

  609                                                 2            0            2   MISMATCH

  61                                                 71            0           71   MISMATCH

  610                                                24            0           24   MISMATCH

  611                                                 7            0            7   MISMATCH

  612                                                 4            0            4   MISMATCH

  613                                                10            0           10   MISMATCH

  614                                                 4            0            4   MISMATCH

  615                                                 7            0            7   MISMATCH

  616                                                14            0           14   MISMATCH

  617                                                25            0           25   MISMATCH

  618                                                12            0           12   MISMATCH

  619                                                13            0           13   MISMATCH

  62                                                 64            0           64   MISMATCH

  620                                                13            0           13   MISMATCH

  621                                                12            0           12   MISMATCH

  622                                                14            0           14   MISMATCH

  623                                                17            0           17   MISMATCH

  624                                                21            0           21   MISMATCH

  625                                                21            0           21   MISMATCH

  626                                                20            0           20   MISMATCH

  627                                                13            0           13   MISMATCH

  628                                                13            0           13   MISMATCH

  629                                                 9            0            9   MISMATCH

  63                                                142            0          142   MISMATCH

  630                                                13            0           13   MISMATCH

  631                                                20            0           20   MISMATCH

  632                                                 9            0            9   MISMATCH

  633                                                30            0           30   MISMATCH

  634                                                45            0           45   MISMATCH

  635                                                22            0           22   MISMATCH

  636                                                36            0           36   MISMATCH

  637                                                35            0           35   MISMATCH

  638                                                47            0           47   MISMATCH

  639                                                40            0           40   MISMATCH

  64                                                 88            0           88   MISMATCH

  640                                                43            0           43   MISMATCH

  641                                                29            0           29   MISMATCH

  642                                                27            0           27   MISMATCH

  643                                                34            0           34   MISMATCH

  644                                                24            0           24   MISMATCH

  645                                                34            0           34   MISMATCH

  646                                                41            0           41   MISMATCH

  647                                                42            0           42   MISMATCH

  648                                                33            0           33   MISMATCH

  649                                                37            0           37   MISMATCH

  65                                                 85            0           85   MISMATCH

  650                                                25            0           25   MISMATCH

  651                                                42            0           42   MISMATCH

  652                                                17            0           17   MISMATCH

  653                                                31            0           31   MISMATCH

  654                                                41            0           41   MISMATCH

  655                                                33            0           33   MISMATCH

  656                                                38            0           38   MISMATCH

  657                                                33            0           33   MISMATCH

  658                                                39            0           39   MISMATCH

  659                                                33            0           33   MISMATCH

  66                                                 92            0           92   MISMATCH

  660                                                26            0           26   MISMATCH

  661                                                31            0           31   MISMATCH

  662                                                13            0           13   MISMATCH

  663                                                21            0           21   MISMATCH

  664                                                18            0           18   MISMATCH

  665                                                27            0           27   MISMATCH

  666                                                30            0           30   MISMATCH

  667                                                12            0           12   MISMATCH

  668                                                18            0           18   MISMATCH

  669                                                19            0           19   MISMATCH

  67                                                112            0          112   MISMATCH

  670                                                26            0           26   MISMATCH

  671                                                17            0           17   MISMATCH

  672                                                 8            0            8   MISMATCH

  673                                                15            0           15   MISMATCH

  674                                                20            0           20   MISMATCH

  675                                                 5            0            5   MISMATCH

  676                                                10            0           10   MISMATCH

  677                                                10            0           10   MISMATCH

  678                                                 9            0            9   MISMATCH

  679                                                 2            0            2   MISMATCH

  68                                                161            0          161   MISMATCH

  680                                                 5            0            5   MISMATCH

  681                                                 1            0            1   MISMATCH

  682                                                 3            0            3   MISMATCH

  683                                                 3            0            3   MISMATCH

  684                                                 1            0            1   MISMATCH

  685                                                 3            0            3   MISMATCH

  686                                                 4            0            4   MISMATCH

  688                                                 1            0            1   MISMATCH

  69                                                 88            0           88   MISMATCH

  693                                                 1            0            1   MISMATCH

  694                                                 2            0            2   MISMATCH

  7                                                 125            0          125   MISMATCH

  70                                                 67            0           67   MISMATCH

  703                                                 2            0            2   MISMATCH

  705                                                 1            0            1   MISMATCH

  706                                                 1            0            1   MISMATCH

  708                                                 2            0            2   MISMATCH

  71                                                 76            0           76   MISMATCH

  710                                                 1            0            1   MISMATCH

  718                                                 5            0            5   MISMATCH

  72                                                 47            0           47   MISMATCH

  722                                                 2            0            2   MISMATCH

  723                                                 1            0            1   MISMATCH

  727                                                 1            0            1   MISMATCH

  73                                                 48            0           48   MISMATCH

  74                                                 78            0           78   MISMATCH

  741                                                 2            0            2   MISMATCH

  75                                                 72            0           72   MISMATCH

  752                                                 1            0            1   MISMATCH

  76                                                114            0          114   MISMATCH

  764                                                 1            0            1   MISMATCH

  77                                                110            0          110   MISMATCH

  78                                                 92            0           92   MISMATCH

  79                                                 74            0           74   MISMATCH

  791                                                 1            0            1   MISMATCH

  795                                                 1            0            1   MISMATCH

  8                                                 131            0          131   MISMATCH

  80                                                 38            0           38   MISMATCH

  81                                                106            0          106   MISMATCH

  82                                                192            0          192   MISMATCH

  83                                                200            0          200   MISMATCH

  84                                                 97            0           97   MISMATCH

  85                                                 54            0           54   MISMATCH

  86                                                 26            0           26   MISMATCH

  87                                                 65            0           65   MISMATCH

  88                                                 88            0           88   MISMATCH

  89                                                 66            0           66   MISMATCH

  9                                                 128            0          128   MISMATCH

  90                                                 81            0           81   MISMATCH

  91                                                 35            0           35   MISMATCH

  92                                                 58            0           58   MISMATCH

  93                                                 33            0           33   MISMATCH

  94                                                 48            0           48   MISMATCH

  95                                                 37            0           37   MISMATCH

  96                                                 31            0           31   MISMATCH

  97                                                 34            0           34   MISMATCH

  98                                                 32            0           32   MISMATCH

  99                                                 42            0           42   MISMATCH

  None                                           148340       174067       -25727   MISMATCH

  ❌ FAIL: count mismatches for 650 of 650 value(s).

  Match % (values): 0/650 (0.00%)

  Match % (volume): 148,340/174,067 (85.22%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: candidate\_\_bid\_status

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=100.58s | rows=5

  SELECT candidate\_\_bid\_status, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_bid\_status ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=58.27s | rows=1

  SELECT candidate\_\_bid\_status, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY candidate\_\_bid\_status ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  15                                              19362            0        19362   MISMATCH

  4                                                5017            0         5017   MISMATCH

  5                                                 291            0          291   MISMATCH

  7                                                1057            0         1057   MISMATCH

  None                                           148340       174067       -25727   MISMATCH

  ❌ FAIL: count mismatches for 5 of 5 value(s).

  Match % (values): 0/5 (0.00%)

  Match % (volume): 148,340/174,067 (85.22%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: candidate\_\_post\_auction\_discount\_id

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=101.24s | rows=8

  SELECT candidate\_\_post\_auction\_discount\_id, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY candidate\_\_post\_auction\_discount\_id ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=59.10s | rows=1

  SELECT candidate\_\_post\_auction\_discount\_id, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY candidate\_\_post\_auction\_discount\_id ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  59                                                 34            0           34   MISMATCH

  60                                                 84            0           84   MISMATCH

  61                                                241            0          241   MISMATCH

  62                                                 42            0           42   MISMATCH

  63                                               1682            0         1682   MISMATCH

  66                                                349            0          349   MISMATCH

  67                                                708            0          708   MISMATCH

  None                                           170927       174067        -3140   MISMATCH

  ❌ FAIL: count mismatches for 8 of 8 value(s).

  Match % (values): 0/8 (0.00%)

  Match % (volume): 170,927/174,067 (98.20%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: partners\_\_role

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=102.90s | rows=16

  SELECT partners\_\_role, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_role ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=61.01s | rows=16

  SELECT partners\_\_role, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY partners\_\_role ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  \['CRO', 'C'\]                                       65           65            0      MATCH

  \['CRO', 'D', 'C'\]                                 224          224            0      MATCH

  \['CRO', 'D', 'D'\]                                4388         4388            0      MATCH

  \['CRO', 'D'\]                                    33380        33380            0      MATCH

  \['CRO', 'R', 'C'\]                                 315          315            0      MATCH

  \['CRO', 'R', 'D', 'C'\]                             48           48            0      MATCH

  \['CRO', 'R', 'D', 'D'\]                            219          219            0      MATCH

  \['CRO', 'R', 'D'\]                                1936         1936            0      MATCH

  \['CRO', 'R', 'R', 'D', 'D'\]                        79           79            0      MATCH

  \['CRO', 'R', 'R', 'D'\]                            572          572            0      MATCH

  \['CRO', 'R', 'R', 'R', 'D', 'D'\]                    1            1            0      MATCH

  \['CRO', 'R', 'R', 'R', 'D'\]                       112          112            0      MATCH

  \['CRO', 'R', 'R', 'R'\]                            360          360            0      MATCH

  \['CRO', 'R', 'R'\]                                6945         6945            0      MATCH

  \['CRO', 'R'\]                                    20848        20848            0      MATCH

  \['CRO'\]                                        104575       104575            0      MATCH

  ✅ PASS: counts match for all 16 value(s).

  Match % (values): 16/16 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

════════════════════════════════════════════════════════════

  AGGREGATE COLUMN: partners\_\_matched\_daypart

════════════════════════════════════════════════════════════

 

  SQL USED FOR THIS AGG VALIDATION:

  \[Hoover SQL\]

  time=94.47s | rows=14

  SELECT partners\_\_matched\_daypart, COUNT(\*) AS cnt FROM mrm\_log\_flat.default.ad WHERE (date\_trunc('HOUR', cast(request\_\_timestamp as timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND process\_batch\_id IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166)   AND bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0 GROUP BY partners\_\_matched\_daypart ORDER BY cnt DESC

 

  \[HooverPP SQL\]

  time=61.16s | rows=14

  SELECT partners\_\_matched\_daypart, COUNT(\*) AS cnt FROM etl.public\_test1.ad WHERE (date\_trunc('HOUR', from\_unixtime(request\_\_timestamp)) = date\_trunc('HOUR', CAST('2026-05-20 20:00:00' as TIMESTAMP))) AND event\_hour IN ('20260520190000','20260520200000','20260520210000')   AND advertisement\_\_ad\_oo\_network\_id IN (520311, 191701, 169843, 384777, 512166) GROUP BY partners\_\_matched\_daypart ORDER BY cnt DESC

 

  Value                                          Hoover     HooverPP         Diff     Status

  --------------------------------------------------------------------------------------------

  \[False, False, False, None, None, None\]             1            1            0      MATCH

  \[False, False, False, None, None\]                  42           42            0      MATCH

  \[False, False, False, None\]                       360          360            0      MATCH

  \[False, False, None, None, None\]                   79           79            0      MATCH

  \[False, False, None, None\]                        572          572            0      MATCH

  \[False, False, None\]                             6090         6090            0      MATCH

  \[False, None, None, None\]                         267          267            0      MATCH

  \[False, None, None\]                              2251         2251            0      MATCH

  \[False, None\]                                   20848        20848            0      MATCH

  \[False, True, False, None, None\]                   70           70            0      MATCH

  \[None, None, None\]                               4612         4612            0      MATCH

  \[None, None\]                                    33445        33445            0      MATCH

  \[None\]                                         104575       104575            0      MATCH

  \[True, False, None\]                               855          855            0      MATCH

  ✅ PASS: counts match for all 14 value(s).

  Match % (values): 14/14 (100.00%)

  Match % (volume): 174,067/174,067 (100.00%)

 

\============================================================

  END OF AGGREGATION REPORT

\============================================================

 

\============================================================

  EXECUTION TIME SUMMARY

  Total execution time: 2619.15s (43.65m)

\============================================================

---

##   
++Request entity:++  
Hoover++ Validations Event Level

  
**Network ID 384777 **

- **Transactions for a given hour:**  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512193746\_909187](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512193746_909187)
- **Old Hoover Ad query (mrm\_log\_flat): **[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512200733\_389815&externalid=20260512\_200735\_00580\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512200733_389815&externalid=20260512_200735_00580_qk7z5)
- **Hoover++ Ad query (etl.public\_test1)**:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512200929\_953383&externalid=20260512\_201211\_00001\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512200929_953383&externalid=20260512_201211_00001_etzx5)  
  

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : request_old_384777.csv
  Source B : request_new_384777.csv
  Rows  A  : 17
  Rows  B  : 17
  Columns A: 49
  Columns B: 49

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 17

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (49 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  The following columns had value mismatches that are semantically equivalent
  (as defined in KNOWN_DIFFERENCES) and were excluded from the diff report:

    request__yield_optimization_ids                              2 row(s)  [equiv: ['', '[]', '\\N', '\\n', 'none', 'null']]
    request__client_facing_ivt_reason_flag                       2 row(s)  [equiv: ['', '0', '\\N', '\\n', 'none', 'null']]

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================

```

**++Network 384777: Request Entity (in Ad Table) Summary:++**

- **Row counts match**: 17 = 17
- **Column headers identical**: 49 columns
- **Known differences suppressed** (semantic equivalences):
    - `request__yield_optimization_ids`: `[]` vs `\N` (2 rows)
    - `request__client_facing_ivt_reason_flag`: `\N` vs `0` (2 rows)
- **No field-level differences found**

---

**++Network ID 112214 ++**

- **Transactions for a given hour:**  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513182224\_587338&externalid=20260513\_182226\_00001\_sgzas](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513182224_587338&externalid=20260513_182226_00001_sgzas)
- **Old Hoover Ad query (mrm\_log\_flat): **[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513182828\_136486&externalid=20260513\_182830\_00015\_sgzas](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513182828_136486&externalid=20260513_182830_00015_sgzas)
- **Hoover++ Ad query (etl.public\_test1)**:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513182838\_696855&externalid=20260513\_182909\_00016\_sgzas](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513182838_696855&externalid=20260513_182909_00016_sgzas)  

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_request_112214.csv
  Source B : new_request_112214.csv
  Rows  A  : 5
  Rows  B  : 5
  Columns A: 49
  Columns B: 49

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 5

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (49 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                              4 row(s)
    request__client_facing_ivt_reason_flag                       4 row(s)
    request__backend_filtration_reason                           2 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**++Network 112214: Request Entity (in Ad Table) Summary:++**

- **Row counts match**: 5 = 5
- **Column headers identical**: 49 columns
- **Known differences suppressed** (global equivalence groups auto-caught all):
    - `request__yield_optimization_ids`: 4 rows
    - `request__client_facing_ivt_reason_flag`: 4 rows
    - `request__backend_filtration_reason`: 2 rows
- **No field-level differences found!**

Global equiv groups (`0` vs `\N`, `[]` vs `\N`) now suppress everything automatically, including the `backend_filtration_reason` that was flagged before.  

---

**++Network ID 538917++**

- **Transactions for a given hour:**  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513185017\_059637&externalid=20260513\_185018\_00009\_iefjc](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513185017_059637&externalid=20260513_185018_00009_iefjc)
- **Old Hoover Ad query (mrm\_log\_flat): **[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513185326\_279748&externalid=20260513\_185327\_00015\_iefjc](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513185326_279748&externalid=20260513_185327_00015_iefjc)
- **Hoover++ Ad query (etl.public\_test1)**:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513185346\_218931&externalid=20260513\_185418\_00017\_iefjc](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513185346_218931&externalid=20260513_185418_00017_iefjc)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old_request_ 538917.csv
  Source B : new_request_ 538917.csv
  Rows  A  : 6
  Rows  B  : 5
  Columns A: 49
  Columns B: 49

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=6  B=5  diff=1

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (49 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) only in old_request_ 538917.csv:
    ('1778522380523794012',)
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                              4 row(s)
    request__client_facing_ivt_reason_flag                       4 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**++Network 538917 — Request Entity Summary:++**

- **Row count mismatch**: old=6, new=5 (1 extra in old)
- **1 transaction only in old**: `1778522380523794012` — not present in Hoover++
- **Known differences suppressed**:
    - `request__yield_optimization_ids`: 4 rows
    - `request__client_facing_ivt_reason_flag`: 4 rows
- **No field-level differences found** on matched rows

Clean on matched transactions, the only issue is 1 missing transaction in Hoover++.

---

**++Network ID 543709++**

- **Transactions for a given hour:**  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513195228\_908535&externalid=20260513\_195230\_00402\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513195228_908535&externalid=20260513_195230_00402_kaj4c)
- **Old Hoover Ad query (mrm\_log\_flat): **[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513195507\_294378&externalid=20260513\_195509\_00407\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513195507_294378&externalid=20260513_195509_00407_kaj4c)
- **Hoover++ Ad query (etl.public\_test1)**:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513200338\_153206&externalid=20260513\_200427\_00002\_csg65](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513200338_153206&externalid=20260513_200427_00002_csg65)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : OLD_REQUEST_543709.csv
  Source B : NEW_REQUEST_543709.csv
  Rows  A  : 6
  Rows  B  : 6
  Columns A: 49
  Columns B: 49

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 6

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (49 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                              6 row(s)
    request__client_facing_ivt_reason_flag                       6 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

  **Network 543709 — Request Entity Summary:**
    - **Row counts match**: 6 = 6
    - **Column headers identical**: 49 columns
    - **Known differences suppressed**:
        - `request__yield_optimization_ids`: 6 rows
        - `request__client_facing_ivt_reason_flag`: 6 rows
    - **No field-level differences found!**

---

**++Network ID 535275 ++**

- **Transactions for a given hour:**  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513201748\_065203&externalid=20260513\_201750\_00419\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513201748_065203&externalid=20260513_201750_00419_kaj4c)
- **Old Hoover Ad query (mrm\_log\_flat): **[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513201903\_156964&externalid=20260513\_201904\_00420\_kaj4c](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513201903_156964&externalid=20260513_201904_00420_kaj4c)
- **Hoover++ Ad query (etl.public\_test1)**:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260513200338\_153206&externalid=20260513\_200427\_00002\_csg65](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260513200338_153206&externalid=20260513_200427_00002_csg65)


## Summary

### **Visitor**

  
**Suppressed diffs by column (semantically equivalent values):**  
visitor\_\_identity\_user\_ids\_\_authorized\_network\_id  
visitor\_\_tracked\_term  
visitor\_\_universal\_iids  
visitor\_\_user\_segments\_lookup\_key

All the rows matched for top 5 networks with 2 sample transaction ids

**Aggregated column:**  
visitor\_\_timezone and visitor\_\_device\_type - Both Match

### Slot

  
All the rows matched for top 5 networks with 2 sample transaction ids  
**Aggregated column:**  
slot\_\_max\_ad\_duration and slot\_\_avail\_type - Both Match

### Candidate

  
**Columns only in HooverPP:**  
candidate\_\_market\_integration\_type

**Suppressed diffs by column (semantically equivalent values):**  
candidate\_\_ortb\_fwpartners  
candidate\_\_ortb\_fwpartners\_\_idtype  
candidate\_\_ortb\_fwpartners\_\_idvalue  
candidate\_\_advertisement\_index  
candidate\_\_filter\_reason  
candidate\_\_filter\_reason\_\_error  
candidate\_\_filter\_reason\_\_error\_category  
candidate\_\_ortb\_fwpartners\_\_idvalue  
candidate\_\_filter\_reason\_\_slot\_index  
candidate\_\_global\_agency\_ids

**Mismatched Columns:**  
candidate\_\_advertisement\_index

**Aggregation Column:**  
candidate\_\_deal\_type and candidate\_\_error - Both are not matched

### Auction

  
**Columns only in HooverPP:**  
auction\_\_auction\_network\_execution\_ctx\_index

**Suppressed diffs by column (semantically equivalent values):**  
auction\_\_bid\_throttling\_info\_\_model\_info  
auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags  
auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id  
auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids  
auction\_\_impression\_\_deals\_\_media\_buyer\_id  
auction\_\_impression\_\_deals\_\_trading\_desk\_id  
auction\_\_mkpl\_partner\_tags  
auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index  
auction\_\_mkpl\_partner\_tags\_\_strategy

**Mismatched Columns:**  
auction\_\_bid\_request\_id  
auction\_\_invite\_deal\_size

**Aggregated Column:**  
auction\_\_buyer\_platform\_id and auction\_\_integration\_type

### Partners

  
**Columns only in HooverPP:**  
partners\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_active\_term\_ids

**Suppressed diffs by column (semantically equivalent values):**  
partners\_\_eligible\_carriage\_listing\_split\_unit\_ids  
partners\_\_outbound\_exchange\_order\_id  
partners\_\_programmatic\_exchange\_rate\_to\_eur  
partners\_\_programmatic\_exchange\_rate\_to\_usd  
partners\_\_selected\_yield\_optimization\_info\_ids  
partners\_\_selected\_yo\_volume\_cap\_ids

**Mismatched Columns:**  
partners\_\_inventory\_package\_ids - Can be ignored since mismatch is (Hoover (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], \[\]\]' and HooverPP (entity=partners, network=191701): '\[\[113569, 149704, 178235, 191914, 260753, 326983, 370180, 570527\], None\]’)  
partners\_\_inbound\_listing\_ids  
partners\_\_inbound\_order\_transaction\_type  
partners\_\_outbound\_exchange\_order\_id  
partners\_\_outbound\_listing\_id - Can be ignored since mismatch is (Hoover (entity=partners, network=512166): '\[\[257759\], \[\], None\]' and HooverPP (entity=partners, network=512166): '\[\[257759\], None, None\]')  
partners\_\_unified\_outbound\_order\_priority - Can be ignored since mismatch is (Hoover (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', None, None\]' and HooverPP (entity=partners, network=512166): '\[\\'{"priority\_tier":"TIER\_4","sub\_priority\_value":-65535}\\', \\'{}\\', None\]')  
partners\_\_selected\_yield\_optimization\_info\_ids - Can be ignored since mismatch is (Hoover (entity=partners, network=512166): '\[\[\], \[\[14681, -1\]\], \[\]\]' and HooverPP (entity=partners, network=512166): '\[None, \[\[14681, -1\]\], None\]’)  
partners\_\_selected\_yo\_volume\_cap\_ids - Can be ignored since mismatch is (Hoover (entity=partners, network=512166): '\[\[\], \[14681\], \[\]\]' and HooverPP (entity=partners, network=512166): '\[None, \[14681\], None\]')  
partners\_\_bidding\_revenue  
partners\_\_bit\_flags  
partners\_\_reseller\_bidding\_revenue  
partners\_\_reseller\_revenue  
partners\_\_revenue  
partners\_\_selected\_yo\_inventory\_prioritization\_id

**Aggregation columns:**  
 partners\_\_entity\_source and partners\_\_role- Both value matches

### Request

  
**Columns only in HooverPP:**  
  request\_\_audience\_item \[array(varchar)\]  
  request\_\_audience\_item\_\_audience\_item\_id \[array(bigint)\]  
  request\_\_bid\_request\_\_site\_\_domain \[varchar\]  
  request\_\_bid\_request\_\_site\_\_page\_hash \[integer\]  
  request\_\_context\_\_key\_value \[array(varchar)\]  
  request\_\_context\_\_key\_value\_\_key \[array(varchar)\]  
  request\_\_context\_\_key\_value\_\_value \[array(varchar)\]  
  request\_\_errors \[array(varchar)\]  
  request\_\_errors\_\_ad\_id \[array(bigint)\]  
  request\_\_errors\_\_code \[array(varchar)\]  
  request\_\_errors\_\_domain \[array(varchar)\]  
  request\_\_errors\_\_network\_id \[array(bigint)\]  
  request\_\_errors\_\_partner \[array(varchar)\]  
  request\_\_errors\_\_type \[array(varchar)\]  
  request\_\_external\_bridge\_records \[array(varchar)\]  
  request\_\_external\_bridge\_records\_\_duration \[array(integer)\]  
  request\_\_external\_bridge\_records\_\_error \[array(varchar)\]  
  request\_\_external\_bridge\_records\_\_flags \[array(integer)\]  
  request\_\_external\_bridge\_records\_\_http\_status\_code \[array(integer)\]  
  request\_\_external\_bridge\_records\_\_slot\_index \[array(integer)\]  
  request\_\_inventory\_group \[array(varchar)\]  
  request\_\_inventory\_group\_\_group\_id \[array(array(bigint))\]  
  request\_\_network\_execution\_ctx \[array(varchar)\]  
  request\_\_network\_execution\_ctx\_\_candidate\_ad\_num \[array(integer)\]  
  request\_\_network\_execution\_ctx\_\_network\_id \[array(bigint)\]  
  request\_\_network\_execution\_ctx\_\_programmatic\_cadidate\_ad\_num \[array(integer)\]  
  request\_\_network\_execution\_ctx\_\_supply\_source\_type \[array(varchar)\]  
  request\_\_network\_execution\_ctx\_\_upstream\_network\_id \[array(bigint)\]

**Datatype Mismatch**  
request\_\_timestamp                      timestamp(3) (hoover)    bigint (hoover++)

**Suppressed diffs by column (semantically equivalent values):**  
request\_\_client\_facing\_ivt\_reason\_flag  
request\_\_context\_\_profile\_concrete\_event\_id  
request\_\_context\_\_standard\_content\_viewership\_profile\_ids  
request\_\_context\_\_standard\_iab\_category\_ids  
request\_\_context\_\_standard\_sport\_entity\_ids  
request\_\_decision\_info\_\_external\_bridge  
request\_\_decision\_info\_\_external\_bridge\_\_slot\_index  
request\_\_decision\_info\_\_external\_bridge\_\_status  
request\_\_guaranteed\_deal\_avail  
request\_\_guaranteed\_deal\_avail\_\_buyer\_id  
request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id  
request\_\_linear\_capnedit  
request\_\_linear\_capnedit\_\_active\_state  
request\_\_linear\_capnedit\_\_device\_id  
request\_\_linear\_capnedit\_\_is\_dvr  
request\_\_linear\_capnedit\_\_last\_activity\_time  
request\_\_linear\_capnedit\_\_mode  
request\_\_linear\_capnedit\_\_tune\_time  
request\_\_mpe\_matcher\_filters  
request\_\_mpe\_matcher\_filters\_\_bucket\_id  
request\_\_mpe\_matcher\_filters\_\_id  
request\_\_mpe\_matcher\_filters\_\_weight  
request\_\_mrc\_compliance\_label  
request\_\_soft\_guaranteed\_ad  
request\_\_soft\_guaranteed\_ad\_\_ad\_id  
request\_\_soft\_guaranteed\_ad\_\_entity\_id  
request\_\_soft\_guaranteed\_ad\_\_entity\_type  
request\_\_soft\_guaranteed\_ad\_\_network\_id  
request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads  
request\_\_context\_\_standard\_genre\_ids  
request\_\_yield\_optimization\_ids  
request\_\_yield\_optimization\_ids\_\_demand\_id  
request\_\_yield\_optimization\_ids\_\_demand\_type  
request\_\_yield\_optimization\_ids\_\_optimization\_ids

**Mismatched Columns:**  
request\_\_cbp - network\_id is missing in the dictionary (Hoover (entity=request, network=169843): '{"network\_id":169843,"slot\_template\_id":82531}' and HooverPP (entity=request, network=169843): '{"slot\_template\_id":82531}')  
request\_\_context  
request\_\_scores - ad\_id is missing in the dictionary (Hoover (entity=request, network=169843): '\[\\'{"network\_id":169843,"ad\_id":93989699,"flag":258,"score":0}\\'\]' and HooverPP (entity=request, network=169843): '\[\\'{"flag":258,"network\_id":169843,"score":0}\\'\]')  
request\_\_time\_record - external\_creative and external\_candidate is missing in the dictionary (Hoover (entity=request, network=169843): '{"total":864,"external\_creative":11,"external\_candidate":601}' and HooverPP (entity=request, network=169843): '{"total":864}')  
request\_\_timestamp - datatype mismatch  
request\_\_traffic\_compliance - endpoint\_flag is missing in the dictionary (Hoover (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3,"endpoint\_flag":0}' and HooverPP (entity=request, network=169843): '{"endpoint\_id":-3,"mrc\_compliance\_flag":1,"mrc\_non\_compliance\_type":3}')  
request\_\_userdb\_audience\_user\_info - num\_keys, dx\_alias\_growth\_ratio, num\_dx\_enriched\_keys and num\_dx\_enriched\_alias\_ids are missing (Hoover (entity=request, network=169843): '{"num\_keys":6,"dx\_alias\_growth\_ratio":2150.0,"bg\_alias\_growth\_ratio":2684.0,"num\_dx\_enriched\_keys":1383,"num\_dx\_enriched\_alias\_ids":236}' and HooverPP (entity=request, network=169843): '{"bg\_alias\_growth\_ratio":2684.0}')  
request\_\_decision\_info

**Aggregated columns:**  
request\_\_context\_\_po\_type - Matched  
request\_\_is\_filtered is not matched

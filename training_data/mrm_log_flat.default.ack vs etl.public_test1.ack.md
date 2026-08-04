# mrm\_log\_flat\.default\.ack vs etl\.public\_test1\.ack

Query to find largest 5 networks by count:

- [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260518074633\_960177&externalid=20260518\_074637\_00028\_qbski](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260518074633_960177&externalid=20260518_074637_00028_qbski)
- [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611163320\_652261&externalid=20260611\_163324\_00130\_uzsvq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611163320_652261&externalid=20260611_163324_00130_uzsvq)

Top 5 networks (by record count for an hour) → 520311, `535262`, `384777`, `169843`, 532076

**Old model (mrm\_log\_flat)** → process\_batch\_id = '20260529180000'  
**New model (etl.public\_test1)** → event\_hour = '20260529180000'

**Filters: **

bitwise\_and(request\_\_bit\_flags, 576460752303423488) \> 0

### **Ack Entity Level:**

`ack__ack_entity_type, ack__metrics__ad_net_avail,ack__metrics__ad_gross_avail`,`ack__metrics__ad_unconstrained_gross_avail`are not supported in Hoover++ with reference - [Entity - AckCtx](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191808341/Entity+-+AckCtx)

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530091947\_532254&externalid=20260530\_091951\_00015\_sx25n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530091947_532254&externalid=20260530_091951_00015_sx25n)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530091707\_100119&externalid=20260530\_091735\_00012\_sx25n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530091707_100119&externalid=20260530_091735_00012_sx25n)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 29
  Columns B: 29

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (29 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     16 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotEnd', 'ack__metrics__ad_impression': '0', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0', 'ack__metrics__fire_event_revenue_ratio': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}
      {'request__transaction_id': '1780078157127344945', 'ack__slot_id': '0', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__ad_impression': '0', 'ack__metrics__slot_impression': '1', 'ack__metrics__click': '0', 'ack__metrics__video_view': '0', 'ack__metrics__first_quartile': '0', 'ack__metrics__middle_quartile': '0', 'ack__metrics__third_quartile': '0', 'ack__metrics__complete_quartile': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    ack__metrics__slot_impression                                1 row(s)
    ack__metrics__video_view                                     1 row(s)
    ack__metrics__fire_event_slot_revenue_ratio                  1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    ack__event_name                                              1 row(s)
    ack__metrics__ad_impression                                  1 row(s)
    ack__metrics__third_quartile                                 1 row(s)
    ack__metrics__fire_event_revenue_ratio                       1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    ack__event_name:
      old.csv: 'defaultImpression'
      new.csv: 'thirdQuartile'
    ack__metrics__ad_impression:
      old.csv: '1'
      new.csv: '\\N'
    ack__metrics__third_quartile:
      old.csv: '\\N'
      new.csv: '1'
    ack__metrics__fire_event_revenue_ratio:
      old.csv: '1'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

Summary**: **33 rows in Hoover and 49 rows in Hoover++. need to check on **ack\_\_ad\_id** which are null.  
  
**Updated Analysis:**

-  Updated Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260610174755\_675958&externalid=20260610\_174759\_00204\_745mg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260610174755_675958&externalid=20260610_174759_00204_745mg)
- Updated Hoover ++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260610174818\_778346&externalid=20260610\_175246\_00213\_745mg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260610174818_778346&externalid=20260610_175246_00213_745mg)
- **Query Change:** Added `AND ack__ad_id IS NOT NULL` to both queries. Without this filter, Hoover returns 33 rows and Hoover++ returns 49 rows (16 extra). The extra rows are all slot-level events (`ack__ad_id = NULL`):

`slotImpression`: Hoover has 1, Hoover++ has 9

`slotEnd`: Hoover has 1, Hoover++ has 9

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : ack_old_520311.csv
  Source B : ack_new_520311.csv
  Rows  A  : 31
  Rows  B  : 31
  Columns A: 29
  Columns B: 29

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 31

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (29 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'ack__ad_id', 'ack__creative_rendition_id', 'ack__event_name']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '0.0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    ack__metrics__slot_impression                                28 row(s)
    ack__metrics__video_view                                     28 row(s)
    ack__metrics__fire_event_slot_revenue_ratio                  28 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

  
Confirmed via `ack__kafka_msg_key` that the 9 duplicate rows share the same Kafka message key, this is the known Kafka Connect duplication issue from broker restarts and won't be an issue in PRD env.   
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260610183117\_408523&externalid=20260610\_183533\_00243\_745mg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260610183117_408523&externalid=20260610_183533_00243_745mg)  
  
**Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530115837\_889219&externalid=20260530\_115841\_00001\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530115837_889219&externalid=20260530_115841_00001_4ujey)

**Step 2 – Hoover (etl.publictest1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530115843\_842651&externalid=20260530\_115917\_00002\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530115843_842651&externalid=20260530_115917_00002_4ujey)

```
Reading old.csv …
Reading new.csv …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 4
  Rows  B  : 4
  Columns A: 89
  Columns B: 89

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 4

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (89 columns)

── [3] ROW DIFFS (matched by row position) ─────────────────────────────
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    ack__metrics__break_starts                                   4 row(s)
    ack__metrics__fire_event_slot_revenue_ratio                  4 row(s)
    ack__metrics__slot_impression                                4 row(s)
    ack__metrics__video_view                                     4 row(s)

  ❌ 4 row(s) have differences:

  Column diff summary (sorted by frequency):
    ack__ad_id                                                   4 row(s)
    ack__creative_rendition_id                                   4 row(s)
    ack__timestamp                                               4 row(s)
    ack__event_name                                              2 row(s)
    ack__kafka_msg_key                                           2 row(s)
    ack__metrics__first_quartile                                 2 row(s)
    ack__metrics__third_quartile                                 2 row(s)
    ack__user_id                                                 2 row(s)

  Detailed diffs:

  [row=2]
    ack__ad_id:
      old.csv: '53783013'
      new.csv: '2089670227153693157'
    ack__creative_rendition_id:
      old.csv: '56999673'
      new.csv: '2882303761574117113'
    ack__timestamp:
      old.csv: '2026-05-13 18:25:34.000'
      new.csv: '1778696734'

  [row=3]
    ack__ad_id:
      old.csv: '53783013'
      new.csv: '2089670227153693157'
    ack__creative_rendition_id:
      old.csv: '56999673'
      new.csv: '2882303761574117113'
    ack__event_name:
      old.csv: 'firstQuartile'
      new.csv: 'thirdQuartile'
    ack__kafka_msg_key:
      old.csv: '1778695888300624081-os2589-1778696734174-2002-685b8404'
      new.csv: '1778695888300624081-os2589-1778696734220-7448-2daca8d1'
    ack__metrics__first_quartile:
      old.csv: '1'
      new.csv: '\\N'
    ack__metrics__third_quartile:
      old.csv: '\\N'
      new.csv: '1'
    ack__timestamp:
      old.csv: '2026-05-13 18:25:34.000'
      new.csv: '1778696734'
    ack__user_id:
      old.csv: 'ecb695_7639444302032186059'
      new.csv: 'ec5ed8_7639444302032231784'

  [row=4]
    ack__ad_id:
      old.csv: '53783013'
      new.csv: '2089670227153693157'
    ack__creative_rendition_id:
      old.csv: '56999673'
      new.csv: '2882303761574117113'
    ack__timestamp:
      old.csv: '2026-05-13 18:25:34.000'
      new.csv: '1778696734'

  [row=5]
    ack__ad_id:
      old.csv: '53783013'
      new.csv: '2089670227153693157'
    ack__creative_rendition_id:
      old.csv: '56999673'
      new.csv: '2882303761574117113'
    ack__event_name:
      old.csv: 'thirdQuartile'
      new.csv: 'firstQuartile'
    ack__kafka_msg_key:
      old.csv: '1778695888300624081-os2589-1778696734220-7448-2daca8d1'
      new.csv: '1778695888300624081-os2589-1778696734174-2002-685b8404'
    ack__metrics__first_quartile:
      old.csv: '\\N'
      new.csv: '1'
    ack__metrics__third_quartile:
      old.csv: '1'
      new.csv: '\\N'
    ack__timestamp:
      old.csv: '2026-05-13 18:25:34.000'
      new.csv: '1778696734'
    ack__user_id:
      old.csv: 'ec5ed8_7639444302032231784'
      new.csv: 'ecb695_7639444302032186059'

========================================================================
  END OF REPORT
========================================================================
```

Summary: Hoover has 5 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- request\_\_transaction\_id = `1781180575132557551`
- Updated Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611163934\_644067&externalid=20260611\_163937\_00141\_uzsvq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611163934_644067&externalid=20260611_163937_00141_uzsvq)
- Updated Hoover ++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611164029\_579478&externalid=20260611\_164113\_00144\_uzsvq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611164029_579478&externalid=20260611_164113_00144_uzsvq)

```py
========================================================================
  ACK ENTITY — VALIDATION REPORT
  Network: 535262  |  Transaction: 1781180575132557551
  Hour: 2026-06-11 12:00:00 UTC
========================================================================

  Hoover (OLD):    mrm_log_flat.default.ack
    + bitwise_and(request__bit_flags, 576460752303423488) > 0
  Hoover++ (NEW):  etl.public_test1.ack

── [1] ROW COUNT CHECK ───────────────────────────────────────
  ✅ Row counts match: 12 rows each.
  Event mix: 5 slot-level slotImpression (slot_id 0-4, ad_id=\\N)
             + 7 ad-level events (defaultImpression x3, firstQuartile,
               _q_midPoint, thirdQuartile, _q_complete).

── [2] COLUMN HEADER CHECK ────────────────────────────────────
  ✅ Column headers identical (29 columns).

── [3] ROW DIFFS (key: transaction_id + ad_id + creative_rendition_id
                     + slot_id + event_name) ───────────────────────────
  ✅ All keys match between both files — no missing or extra rows.
  Note: defaultImpression appears 3x on BOTH sides (matched 3-for-3).

── [K] KNOWN DIFFERENCES (suppressed — semantically equivalent) ─────
  All field-level diffs are metric columns emitting '\\N' (OLD) vs '0' (NEW)
  — suppressed via the 0/null global equivalence group:

    ack__metrics__video_view                       10 row(s)
    ack__metrics__ad_impression                     5 row(s)
    ack__metrics__slot_impression                   5 row(s)
    ack__metrics__click                             5 row(s)
    ack__metrics__first_quartile                    5 row(s)
    ack__metrics__middle_quartile                   5 row(s)
    ack__metrics__third_quartile                    5 row(s)
    ack__metrics__complete_quartile                 5 row(s)
    ack__metrics__fire_event_revenue_ratio          5 row(s)
    ack__metrics__fire_event_slot_revenue_ratio     5 row(s)
    ack__metrics__fire_event_bid_revenue_ratio      5 row(s)

── FIELD-LEVEL COMPARISON ──────────────────────────────────────
  Columns compared : 29
  Real data diffs  : 0

── RESULT ───────────────────────────────────────────────────
  ✅ EXACT MATCH — OLD and NEW ack are identical for this transaction.
     All rows align on the composite key; the only differences are
     metric \\N-vs-0 null/zero semantics (no real data drift).

========================================================================
  END OF REPORT
========================================================================
```

    
**Summary:**  
Network 535262, transaction `1781180575132557551`: EXACT MATCH all 12 rows align on the composite key with zero real data diffs (only `\N`-vs-`0` metric null/zero semantics).  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530120247\_392523&externalid=20260530\_120252\_00004\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530120247_392523&externalid=20260530_120252_00004_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530120259\_616203&externalid=20260530\_120338\_00005\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530120259_616203&externalid=20260530_120338_00005_4ujey)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 29
  Columns B: 29

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (29 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     3 row(s) are in old.csv but have NO matching row in new.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550', 'ack__slot_id': '7', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__slot_impression': '1', 'ack__metrics__fire_event_slot_revenue_ratio': '1', 'ack__client_facing_ivt_reason_flag': '0', 'ack__traffic_type': '0', 'ack__flags': '1', 'ack__extra_flags': '0', 'ack__bit_flags': '0', 'ack__is_faked': 'false'}
      {'request__transaction_id': '1780076927707289550', 'ack__slot_id': '5', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__slot_impression': '1', 'ack__metrics__fire_event_slot_revenue_ratio': '1', 'ack__client_facing_ivt_reason_flag': '0', 'ack__traffic_type': '0', 'ack__flags': '1', 'ack__extra_flags': '0', 'ack__bit_flags': '0', 'ack__is_faked': 'false'}
      {'request__transaction_id': '1780076927707289550', 'ack__slot_id': '3', 'ack__event_type': 'i', 'ack__event_name': 'slotImpression', 'ack__metrics__slot_impression': '1', 'ack__metrics__fire_event_slot_revenue_ratio': '1', 'ack__client_facing_ivt_reason_flag': '0', 'ack__traffic_type': '0', 'ack__flags': '1', 'ack__extra_flags': '0', 'ack__bit_flags': '0', 'ack__is_faked': 'false'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    ack__metrics__slot_impression                                1 row(s)
    ack__metrics__video_view                                     1 row(s)
    ack__metrics__fire_event_slot_revenue_ratio                  1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    ack__ad_id                                                   1 row(s)
    ack__creative_rendition_id                                   1 row(s)
    ack__event_name                                              1 row(s)
    ack__metrics__ad_impression                                  1 row(s)
    ack__metrics__third_quartile                                 1 row(s)
    ack__metrics__fire_event_revenue_ratio                       1 row(s)
    ack__flags                                                   1 row(s)

  Detailed diffs:

  [key=('1780076927707289550',)]
    ack__ad_id:
      old.csv: '92698599'
      new.csv: '92694419'
    ack__creative_rendition_id:
      old.csv: '1189554371'
      new.csv: '1189591204'
    ack__event_name:
      old.csv: 'thirdQuartile'
      new.csv: 'defaultImpression'
    ack__metrics__ad_impression:
      old.csv: '\\N'
      new.csv: '1'
    ack__metrics__third_quartile:
      old.csv: '1'
      new.csv: '\\N'
    ack__metrics__fire_event_revenue_ratio:
      old.csv: '\\N'
      new.csv: '1'
    ack__flags:
      old.csv: '0'
      new.csv: '1'

========================================================================
  END OF REPORT
========================================================================
```

Summary: The records with ack\_\_slot\_id 3,5,7 are removed in Hoover++, compared to Hoover.  
  
**Updated Analysis:**  
Hoover (current) 384777:  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611161334\_039400&externalid=20260611\_161337\_00093\_uzsvq](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611161334_039400&externalid=20260611_161337_00093_uzsvq)  
Hoover ++ 384777:  
[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611161338\_904345&externalid=20260611\_161409\_00168\_y8a4i](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611161338_904345&externalid=20260611_161409_00168_y8a4i)

```py
========================================================================
  REQUEST ENTITY — VALIDATION REPORT
  Network: 384777  |  Transaction: 1781177811482546296
  Hour: 2026-06-11 12:00:00 UTC
========================================================================

  Hoover (OLD):    mrm_log_flat.default.ack
    + bitwise_and(request__bit_flags, 576460752303423488) > 0
  Hoover++ (NEW):  etl.public_test1.ack

── [1] ROW COUNT CHECK ───────────────────────────────────────
  Row counts match: 84 rows each.
  All 84 rows in OLD are identical (1 unique request-level row).
  All 84 rows in NEW are identical (1 unique request-level row).

── [2] COLUMN HEADER CHECK ────────────────────────────────────
   Column headers identical (48 columns).

── [3] KEY CHECK (request__transaction_id) ────────────────────────
   Same transaction_id on both sides — same event.

── [K] KNOWN DIFFERENCES (suppressed — semantically equivalent) ─────

  request__yield_optimization_ids:
    OLD: '[]'   NEW: '\\N'    -> 0/null equivalence 
  request__client_facing_ivt_reason_flag:
    OLD: '\\N'  NEW: '0'     -> 0/null equivalence 

── FIELD-LEVEL COMPARISON (1 unique row vs 1 unique row) ────────────
  Columns compared : 48
  Columns matching : 46
  Semantic diffs   : 2  (suppressed above)
  Real data diffs  : 0

── RESULT ───────────────────────────────────────────────────
  ✅ EXACT MATCH — OLD and NEW ack are identical for this transaction.
     Only diffs are 2 null/0 semantic equivalences.

========================================================================
  END OF REPORT
========================================================================
```

**Summary**:  
**EXACT MATCH **between OLD and NEW ack are identical for this transaction. Only diffs are 2 null/0 semantic equivalences.  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530121825\_336236&externalid=20260530\_121830\_00007\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530121825_336236&externalid=20260530_121830_00007_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530121838\_902700&externalid=20260530\_121915\_00008\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530121838_902700&externalid=20260530_121915_00008_4ujey)

Summary: No real differences found 


1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530092531\_316082&externalid=20260530\_092535\_00017\_sx25n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530092531_316082&externalid=20260530_092535_00017_sx25n)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530093428\_642650&externalid=20260530\_093457\_00021\_sx25n](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530093428_642650&externalid=20260530_093457_00021_sx25n)

```
```

Summary: Hoover has 4 rows and Hoover++ has 0 rows.  
  
**Updated analysis:**  
  
Old hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611185410\_604883&externalid=20260611\_185414\_00002\_vhcd2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611185410_604883&externalid=20260611_185414_00002_vhcd2)  
New Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611183838\_544047&externalid=20260611\_183937\_00030\_n8jnw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611183838_544047&externalid=20260611_183937_00030_n8jnw)  
  
**Network 532076** — transaction `1781179336336761918`

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : oldhoover.csv
  Source B : newhoover.csv
  Rows  A  : 26
  Rows  B  : 26
  Columns A: 29
  Columns B: 29

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  [OK] Row counts match: 26

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  [OK] Column headers identical (29 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id', 'ack__ad_id', 'ack__creative_rendition_id', 'ack__slot_id', 'ack__event_name']) ──────────
  [OK] All keys match between both files — no missing or duplicate rows.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Suppressed diffs by column (semantically equivalent values):

    ack__metrics__video_view                         26 row(s)
    ack__metrics__slot_impression                    20 row(s)
    ack__metrics__fire_event_slot_revenue_ratio      20 row(s)
    ack__metrics__ad_impression                      6 row(s)
    ack__metrics__click                              6 row(s)
    ack__metrics__first_quartile                     6 row(s)
    ack__metrics__middle_quartile                    6 row(s)
    ack__metrics__third_quartile                     6 row(s)
    ack__metrics__complete_quartile                  6 row(s)
    ack__metrics__fire_event_revenue_ratio           6 row(s)
    ack__metrics__fire_event_bid_revenue_ratio       6 row(s)

  [OK] No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**  
Hoover vs Hoover++ ack for transaction `1781179336336761918`: MATCH, all 26 rows align 1-to-1 on the 5-column key with zero real field diffs (only `\N`-vs-`0` metric null/zero semantics).

### **Request Entity Level:**

request\_\_prebid\_sivt\_\_inhouse\_sivt\_reason, request\_\_prebid\_sivt\_\_whiteops\_sivt\_reason mentioned in the Event validations level is not present in Hoover.

`request__client_facing_reason_code` is present in Hoover, missing in Hoover++.

1. **Network 520311**

`request__transaction_id: 1778695200227372195`

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530123218\_018258&externalid=20260530\_123223\_00010\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530123218_018258&externalid=20260530_123223_00010_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530123414\_290098&externalid=20260530\_123445\_00012\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530123414_290098&externalid=20260530_123445_00012_4ujey)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     33 row(s) are in old.csv but have NO matching row in new.csv.
     49 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780078157127344945', 'request__context__network_id': '520311', 'request__context__profile_id': '11410', 'request__context__standard_endpoint_id': '427', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__backend_filtration_reason                           1 row(s)
    request__client_facing_ivt_reason_flag                       1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    request__flags                                               1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    request__flags:
      old.csv: '1224999433'
      new.csv: '1090781705'

========================================================================
  END OF REPORT
========================================================================
```

Summary: 33 rows in Hoover and 49 rows in Hoover++.  
  
**Updated Analysis:**  
  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611201057\_528906&externalid=20260611\_201134\_00002\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611201057_528906&externalid=20260611_201134_00002_m8zwn)  
Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611201052\_602415&externalid=20260611\_201125\_00053\_ucrff](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611201052_602415&externalid=20260611_201125_00053_ucrff)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : oldhoover.csv
  Source B : newhoover.csv
  Rows  A  : 263
  Rows  B  : 263
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  [OK] Row counts match: 263

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  [OK] Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ──────────
  [OK] All keys match between both files — no missing or duplicate rows.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                  1 row(s)
    request__client_facing_ivt_reason_flag           1 row(s)

  [OK] No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

  
**Summary:**  
Hoover vs Hoover++ for transaction `1781177635874057052` (network 520311): Match; all 263 rows and 48 columns match.


1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124102\_721983&externalid=20260530\_124106\_00013\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124102_721983&externalid=20260530_124106_00013_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124108\_161918&externalid=20260530\_124141\_00016\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124108_161918&externalid=20260530_124141_00016_4ujey)

Summary: 5 rows in Hoover and 0 in Hoover++.  
  
**Updated Analysis:**

- (transaction `1781180575132557551`, network 535262)
- Old Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611202327\_344916&externalid=20260611\_202332\_00028\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611202327_344916&externalid=20260611_202332_00028_m8zwn)
- Hoover ++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611202321\_904200&externalid=20260611\_202355\_00029\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611202321_904200&externalid=20260611_202355_00029_m8zwn)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : oldhoover.csv
  Source B : newhoover.csv
  Rows  A  : 12
  Rows  B  : 12
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  [OK] Row counts match: 12

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  [OK] Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ──────────

  [WARN]  1 key(s) have multiple rows (fan-out detected).
     7 row(s) are in oldhoover.csv but have NO matching row in newhoover.csv.
     7 row(s) are in newhoover.csv but have NO matching row in oldhoover.csv.


── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                  1 row(s)
    request__client_facing_ivt_reason_flag           1 row(s)

  [FAIL] 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    request__flags                                   1 row(s)

  Detailed diffs:

  [key=('1781180575132557551',)]
    request__flags:
      oldhoover.csv: '136630785'
      newhoover.csv: '2413057'

========================================================================
  END OF REPORT
========================================================================
```

**Important finding for transaction **`1781180575132557551` **(network 535262)**  
**Result: REVIEW REQUIRED: **

`request__flags`** differs by exactly bit 27 (2^27 = 134217728).**

- OLD (Hoover): all 12 rows = `136630785` → bit 27 **set** (consistent).
- NEW (Hoover++): `2413057` on **7 rows** (bit 27 **not set**) and `136630785` on **5 rows** (bit 27 set).

**So Hoover++ is inconsistently dropping bit 27**of `request__flags`,  **it's present on 5 of the 12 ack rows but missing on the other 7, whereas Hoover sets it on all 12**.  All other 47 columns match (the two `\N`/`0`/`[]` diffs are expected semantics). **As confirmed by team, this difference can be safely ignored, will be documented as known difference that does not impact reporting business. **  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124116\_643778&externalid=20260530\_124121\_00014\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124116_643778&externalid=20260530_124121_00014_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124621\_161237&externalid=20260530\_124652\_00020\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124621_161237&externalid=20260530_124652_00020_4ujey)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     3 row(s) are in old.csv but have NO matching row in new.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550', 'request__context__network_id': '384777', 'request__context__profile_id': '2563', 'request__context__standard_endpoint_id': '103', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780076927707289550', 'request__context__network_id': '384777', 'request__context__profile_id': '2563', 'request__context__standard_endpoint_id': '103', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
      {'request__transaction_id': '1780076927707289550', 'request__context__network_id': '384777', 'request__context__profile_id': '2563', 'request__context__standard_endpoint_id': '103', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                              1 row(s)
    request__client_facing_ivt_reason_flag                       1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary: Difference of 3 records b/w Hoover and Hoover++.  
  
**Updated Analysis:**

- For transaction `1781177811482546296`, network 384777
- Hoover:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611204524\_646299&externalid=20260611\_204528\_00059\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611204524_646299&externalid=20260611_204528_00059_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611204520\_107972&externalid=20260611\_204656\_00060\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611204520_107972&externalid=20260611_204656_00060_m8zwn)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : oldhoover.csv
  Source B : newhoover.csv
  Rows  A  : 84
  Rows  B  : 84
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  [OK] Row counts match: 84

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  [OK] Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ──────────
  [OK] All keys match between both files — no missing or duplicate rows.

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                  1 row(s)
    request__client_facing_ivt_reason_flag           1 row(s)

  [OK] No field-level differences found!

========================================================================
  END OF REPORT
========================================================================


```

**Summary:**  
Hoover vs Hoover++ for transaction `1781177811482546296` (network 384777): Match, all 84 rows and 48 columns match exactly, only the expected `\N`/`0`/`[]` null-zero semantics.

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124136\_629174&externalid=20260530\_124141\_00015\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124136_629174&externalid=20260530_124141_00015_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124143\_992060&externalid=20260530\_124219\_00018\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124143_992060&externalid=20260530_124219_00018_4ujey)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     1 row(s) are in old.csv but have NO matching row in new.csv.
     1 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780079174184480780',)]  old.csv: 3 rows  |  new.csv: 3 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780079174184480780', 'request__context__network_id': '169843', 'request__context__profile_id': '18269', 'request__context__standard_endpoint_id': '101', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780079174184480780', 'request__context__network_id': '169843', 'request__context__profile_id': '18269', 'request__context__standard_endpoint_id': '101', 'request__log_sampling__magnifier': '1', 'request__log_sampling__mode': 'NO_SAMPLING', 'request__magnifier': '1', 'request__is_filtered': 'false', 'request__is_first_user_visitor': 'false', 'request__is_no_selection': 'false', 'request__is_ssp_bidder_request': 'false', 'request__context__profile_type': 'COMPOUND'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                              1 row(s)
    request__client_facing_ivt_reason_flag                       1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    request__flags                                               1 row(s)

  Detailed diffs:

  [key=('1780079174184480780',)]
    request__flags:
      old.csv: '1225007745'
      new.csv: '1090790017'

========================================================================
  END OF REPORT
========================================================================
```

Summary: request\_\_flags column has a difference.  
  
**Updated Analysis:**

- Network 169843 (transaction `1781179289223686607`)
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611205426\_218767&externalid=20260611\_205429\_00005\_hqqp3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611205426_218767&externalid=20260611_205429_00005_hqqp3)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611205422\_356226&externalid=20260611\_205448\_00006\_hqqp3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611205422_356226&externalid=20260611_205448_00006_hqqp3)

```
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : oldhoover.csv
  Source B : newhoover.csv
  Rows  A  : 186
  Rows  B  : 186
  Columns A: 48
  Columns B: 48

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  [OK] Row counts match: 186

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  [OK] Column headers identical (48 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ──────────

  [WARN]  1 key(s) have multiple rows (fan-out detected).
     179 row(s) are in oldhoover.csv but have NO matching row in newhoover.csv.
     179 row(s) are in newhoover.csv but have NO matching row in oldhoover.csv.


── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Suppressed diffs by column (semantically equivalent values):

    request__yield_optimization_ids                  1 row(s)
    request__client_facing_ivt_reason_flag           1 row(s)

  [FAIL] 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    request__flags                                   1 row(s)

  Detailed diffs:

  [key=('1781179289223686607',)]
    request__flags:
      oldhoover.csv: '1225261697'
      newhoover.csv: '1091043969'

========================================================================
  END OF REPORT
========================================================================
```

  
**Result: REVIEW REQUIRED: **same `request__flags` bit-27 issue as network 535262, now reproduced on network 169843 (transaction `1781179289223686607`).

- Difference is exactly bit 27 (`1225261697 XOR 1091043969 = 134217728 = 2^27`), set only in OLD.
- OLD (Hoover): all 186 rows = `1225261697` (bit 27 set) — consistent.
- NEW (Hoover++): `1091043969` on 179 rows (bit 27 cleared) and `1225261697` on 7 rows (bit 27 set).

So Hoover++ again drops `request__flags` bit 27 inconsistently,  present on 7 of 186 ack rows, missing on 179, while Hoover sets it on all 186. All other 47 columns match (only the expected `\N`/`0`/`[]` semantics). **As confirmed by team, this difference can be safely ignored, will be documented as known difference that does not impact reporting business. **  

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124150\_308829&externalid=20260530\_124155\_00017\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124150_308829&externalid=20260530_124155_00017_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530124157\_529555&externalid=20260530\_124233\_00019\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530124157_529555&externalid=20260530_124233_00019_4ujey)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781179991809961739`, network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611212032\_119442&externalid=20260611\_212037\_00086\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611212032_119442&externalid=20260611_212037_00086_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611212029\_479585&externalid=20260611\_212148\_00087\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611212029_479585&externalid=20260611_212148_00087_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 26 / 26
  Columns compared : 48

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 26 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (48 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [FAIL] 1 column(s) differ between Hoover and Hoover++:

    request__flags
      OLD (Hoover)   : 136888841 x26
      NEW (Hoover++) : 2671113 x20, 136888841 x6


── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - request__yield_optimization_ids
    - request__client_facing_ivt_reason_flag

── RESULT ────────────────────────────────────────────────────────────────
  [FAIL] REVIEW REQUIRED — real differences detected

========================================================================
  END OF REPORT
========================================================================
```

**Result: REVIEW REQUIRED** — same `request__flags` bit-27 issue, now on a **third network** (532076, transaction `1781179991809961739`).

- Hoover vs Hoover++ parity for request `1781179991809961739` (network 532076): row counts (26/26) and all 48 column headers match.
- One real difference is `request__flags`: **Hoover sets bit 27 (2^27) on all 26 rows, while Hoover++ drops it on 20 of 26 rows** (`136888841 x26` vs `2671113 x20, 136888841 x6`); the only other deltas are expected `\N`/`0`/`[]` null-zero semantics.
- **Same reproducible bit-27 regression already seen on networks 535262 and 169843. As confirmed by team, this difference can be safely ignored, will be documented as known difference that does not impact reporting business. **  

### **Visitor Entity Level:**

`visitor__postal_code_id` is missing in Hoover++

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530162222\_316092&externalid=20260530\_162227\_00024\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530162222_316092&externalid=20260530_162227_00024_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530162230\_084160&externalid=20260530\_162312\_00025\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530162230_084160&externalid=20260530_162312_00025_4ujey)

Summary: Difference of 16 rows 

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     16 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}
      {'request__transaction_id': '1780078157127344945', 'visitor__user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__server_side_user_id': 'Xi6395AtS1DVb2iQlKmeLYbU1fVDvU5M8X2q_3UFaE_-ztl0gfwzENkieXWiMEM9FQDGcf', 'visitor__universal_hhid': '1887zzw1ueljc74ikuicx1u8tg==', 'visitor__universal_iids': '[jselzlhchh4evkb4]', 'visitor__device_id': '8ffcd721-73e4-4bdd-84d7-1f4e32457a83', 'visitor__device_type': 'vida', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2263', 'visitor__state': 'ca', 'visitor__dma_code_id': '207'}

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

**Updated Analysis:**

- Transaction `1781177635874057052`, Network 520311
- Hoover:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611215403\_127118&externalid=20260611\_215421\_00099\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611215403_127118&externalid=20260611_215421_00099_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611215408\_339330&externalid=20260611\_215442\_00100\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611215408_339330&externalid=20260611_215442_00100_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 263 / 263
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 263 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__tracked_term

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**  
Hoover vs Hoover++ visitor-entity parity for request `1781177635874057052`: Match, all 263 rows and 37 columns match exactly, only the expected `[]`-vs-`\N` empty-list semantics differ.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163339\_133074&externalid=20260530\_163343\_00026\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163339_133074&externalid=20260530_163343_00026_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163344\_621602&externalid=20260530\_163423\_00029\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163344_621602&externalid=20260530_163423_00029_4ujey)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction: `1781180575132557551`, Network 535262
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611220503\_054005&externalid=20260611\_220508\_00102\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611220503_054005&externalid=20260611_220508_00102_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611220501\_242349&externalid=20260611\_220539\_00103\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611220501_242349&externalid=20260611_220539_00103_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 12 / 12
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 12 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__postal_code_id
    - visitor__tracked_term
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**  
Representational-only differences (suppressed, not real data difference):

- `visitor__identity_user_ids`:JSON key-order only: Hoover emits `{"namespace_id","id"}`, Hoover++ emits `{"id","namespace_id"}`; identical values.
- `visitor__universal_iids` :empty-list vs null (`[]` in Hoover vs `\N` in Hoover++).
- `visitor__tracked_term`: empty-list vs null (`[]` vs `\N`).
- `visitor__postal_code_id` :null/zero representation.  
**Row count: 12 vs 12 (match); column headers: 37 vs 37 (identical); all 37 columns match with zero real differences.**  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163351\_790651&externalid=20260530\_163356\_00027\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163351_790651&externalid=20260530_163356_00027_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163358\_754520&externalid=20260530\_163431\_00031\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163358_754520&externalid=20260530_163431_00031_4ujey)

Summary: Difference of 3 rows.  

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     3 row(s) are in old.csv but have NO matching row in new.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781177811482546296` (Network 384777).
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611231301\_515929&externalid=20260611\_231307\_00114\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611231301_515929&externalid=20260611_231307_00114_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611231300\_269229&externalid=20260611\_231340\_00115\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611231300_269229&externalid=20260611_231340_00115_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 84 / 84
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 84 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- `visitor__identity_user_ids` differs by JSON key order only (Hoover `{"namespace_id","id"}` vs Hoover++ `{"id","namespace_id"}`, same values), and `visitor__universal_iids` is `[]` (Hoover) vs `\N` (Hoover++).  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163404\_475088&externalid=20260530\_163409\_00028\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163404_475088&externalid=20260530_163409_00028_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163412\_050837&externalid=20260530\_163443\_00032\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163412_050837&externalid=20260530_163443_00032_4ujey)

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

Summary: No real differences found 

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163419\_694362&externalid=20260530\_163423\_00030\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163419_694362&externalid=20260530_163423_00030_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163428\_921340&externalid=20260530\_163458\_00033\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163428_921340&externalid=20260530_163458_00033_4ujey)

Summary: Hoover has 4 records and Hoover++ has 0 records.

**Updated Analysis:**

- Transaction `1781179336336761918`, Network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611232154\_487844&externalid=20260611\_232159\_00116\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611232154_487844&externalid=20260611_232159_00116_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611232151\_241337&externalid=20260611\_232229\_00117\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611232151_241337&externalid=20260611_232229_00117_m8zwn) 

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 26 / 26
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 26 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__tracked_term
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Matching,  All 26 rows and 37 columns are identical between Hoover and Hoover++, with no actual data differences.
- The only differences are formatting/representation, not content: `visitor__identity_user_ids` lists the same JSON keys and values but in a different order (Hoover `{"namespace_id","id"}` vs Hoover++ `{"id","namespace_id"}`), and `visitor__universal_iids` / `visitor__tracked_term` represent "empty" differently (`[]` in Hoover vs `\N` in Hoover++). 

### **Advertisement Entity Level:**

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530170229\_844051&externalid=20260530\_170233\_00034\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530170229_844051&externalid=20260530_170233_00034_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530170238\_475387&externalid=20260530\_170318\_00035\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530170238_475387&externalid=20260530_170318_00035_4ujey)

Summary: Difference of 16 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     16 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'advertisement__ad_id': '0', 'advertisement__ad_replica_id': '0', 'advertisement__rendition_id': '0', 'advertisement__creative_id': '0', 'advertisement__placement_id': '0', 'advertisement__campaign_id': '0', 'advertisement__io_id': '0', 'advertisement__insertion_order_id': '0', 'advertisement__ad_oo_network_id': '0', 'advertisement__ad_unit_id': '0', 'advertisement__advertiser_id': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    advertisement__campaign_id                                   1 row(s)
    advertisement__io_id                                         1 row(s)
    advertisement__insertion_order_id                            1 row(s)
    advertisement__advertiser_id                                 1 row(s)
    advertisement__agency_id                                     1 row(s)
    advertisement__replaced_ad_id                                1 row(s)
    advertisement__replaced_creative_id                          1 row(s)
    advertisement__replaced_ad_unit_id                           1 row(s)
    advertisement__replaced_campaign_id                          1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    advertisement__ad_id                                         1 row(s)
    advertisement__ad_replica_id                                 1 row(s)
    advertisement__rendition_id                                  1 row(s)
    advertisement__creative_id                                   1 row(s)
    advertisement__placement_id                                  1 row(s)
    advertisement__ad_oo_network_id                              1 row(s)
    advertisement__ad_unit_id                                    1 row(s)
    advertisement__global_advertiser_ids                         1 row(s)
    advertisement__global_brand_ids                              1 row(s)
    advertisement__global_industry_ids                           1 row(s)
    advertisement__duration                                      1 row(s)
    advertisement__ad_delivery_method                            1 row(s)
    advertisement__linear_decision_type                          1 row(s)
    advertisement__placement_type_priority                       1 row(s)
    advertisement__inventory_protection_flags                    1 row(s)
    advertisement__unified_priority                              1 row(s)
    advertisement__effective_unified_priority                    1 row(s)
    advertisement__replaced_ad_network_id                        1 row(s)
    advertisement__flags                                         1 row(s)
    advertisement__bit_flags                                     1 row(s)
    advertisement__extra_flags                                   1 row(s)
    advertisement__extra_flags2                                  1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    advertisement__ad_id:
      old.csv: '65920238'
      new.csv: '0'
    advertisement__ad_replica_id:
      old.csv: '131072'
      new.csv: '0'
    advertisement__rendition_id:
      old.csv: '265003542'
      new.csv: '0'
    advertisement__creative_id:
      old.csv: '54812104'
      new.csv: '0'
    advertisement__placement_id:
      old.csv: '65920236'
      new.csv: '0'
    advertisement__ad_oo_network_id:
      old.csv: '525290'
      new.csv: '0'
    advertisement__ad_unit_id:
      old.csv: '57838'
      new.csv: '0'
    advertisement__global_advertiser_ids:
      old.csv: '[1724375]'
      new.csv: '\\N'
    advertisement__global_brand_ids:
      old.csv: '[1724376]'
      new.csv: '\\N'
    advertisement__global_industry_ids:
      old.csv: '[87]'
      new.csv: '\\N'
    advertisement__duration:
      old.csv: '60'
      new.csv: '0'
    advertisement__ad_delivery_method:
      old.csv: 'Dynamic'
      new.csv: '\\N'
    advertisement__linear_decision_type:
      old.csv: 'Not Applicable'
      new.csv: '\\N'
    advertisement__placement_type_priority:
      old.csv: 'PREEMPTIBLE'
      new.csv: '\\N'
    advertisement__inventory_protection_flags:
      old.csv: '16'
      new.csv: '0'
    advertisement__unified_priority:
      old.csv: '{"priority_tier":"TIER_4","sub_priority_value":0}'
      new.csv: '\\N'
    advertisement__effective_unified_priority:
      old.csv: '{"priority_tier":"TIER_3","sub_priority_value":0}'
      new.csv: '\\N'
    advertisement__replaced_ad_network_id:
      old.csv: '516429'
      new.csv: '0'
    advertisement__flags:
      old.csv: '11'
      new.csv: '0'
    advertisement__bit_flags:
      old.csv: '2048'
      new.csv: '0'
    advertisement__extra_flags:
      old.csv: '8388608'
      new.csv: '0'
    advertisement__extra_flags2:
      old.csv: '67110914'
      new.csv: '0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178064848289535`, Network 520311
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611233336\_180496&externalid=20260611\_233340\_00119\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611233336_180496&externalid=20260611_233340_00119_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611233334\_018106&externalid=20260611\_233408\_00120\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611233334_018106&externalid=20260611_233408_00120_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 258 / 258
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 258 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - advertisement__ad_id
    - advertisement__ad_replica_id
    - advertisement__rendition_id
    - advertisement__creative_id
    - advertisement__placement_id
    - advertisement__campaign_id
    - advertisement__io_id
    - advertisement__insertion_order_id
    - advertisement__ad_oo_network_id
    - advertisement__ad_unit_id
    - advertisement__advertiser_id
    - advertisement__agency_id
    - advertisement__global_brand_ids
    - advertisement__duration
    - advertisement__inventory_protection_flags
    - advertisement__is_replacement
    - advertisement__replaced_ad_id
    - advertisement__replaced_creative_id
    - advertisement__replaced_ad_unit_id
    - advertisement__replaced_campaign_id
    - advertisement__is_uy_replaced
    - advertisement__is_ax
    - advertisement__replaced_ad_network_id
    - advertisement__flags
    - advertisement__bit_flags
    - advertisement__extra_flags
    - advertisement__extra_flags2

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Match, all 258 rows and 37 columns match exactly; differences are only Hoover's `\N` vs Hoover++'s `0`/`false` null-zero representation.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163339\_133074&externalid=20260530\_163343\_00026\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163339_133074&externalid=20260530_163343_00026_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163344\_621602&externalid=20260530\_163423\_00029\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163344_621602&externalid=20260530_163423_00029_4ujey)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781180575132557551`, Network **535262**
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611234017\_869244&externalid=20260611\_234021\_00122\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611234017_869244&externalid=20260611_234021_00122_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611234014\_250246&externalid=20260611\_234046\_00123\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611234014_250246&externalid=20260611_234046_00123_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 12 / 12
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 12 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__postal_code_id
    - visitor__tracked_term
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Match: all 12 rows and 37 columns identical between Hoover and Hoover++, with zero real data differences.
- Only formatting differences: `visitor__identity_user_ids` has the same keys/values in a different JSON order (Hoover `{"namespace_id","id"}` vs Hoover++ `{"id","namespace_id"}`), and `visitor__universal_iids` / `visitor__tracked_term` / `visitor__postal_code_id` differ only in how "empty/no value" is written (`[]` or `\N` vs `0`/`null`)


1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163351\_790651&externalid=20260530\_163356\_00027\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163351_790651&externalid=20260530_163356_00027_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163358\_754520&externalid=20260530\_163431\_00031\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163358_754520&externalid=20260530_163431_00031_4ujey)

Summary: Difference of 3 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     3 row(s) are in old.csv but have NO matching row in new.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}
      {'request__transaction_id': '1780076927707289550', 'visitor__user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__custom_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__server_side_user_id': '1944CDB4761E8CD30494EDA6052B8699', 'visitor__household_id': 'comcast:1944cdb4761e8cd30494eda6052b8699', 'visitor__universal_iids': '[]', 'visitor__country_id': '165', 'visitor__country': 'us', 'visitor__state_id': '2297', 'visitor__state': 'pa', 'visitor__dma_code_id': '66', 'visitor__dma_code': '566'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178373156217993`, Network 384777
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611234633\_666922&externalid=20260611\_234637\_00124\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611234633_666922&externalid=20260611_234637_00124_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260611234630\_311405&externalid=20260611\_234659\_00125\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260611234630_311405&externalid=20260611_234659_00125_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 80 / 80
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 80 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Match; all 80 rows and 37 columns match exactly. Only representational differences `visitor__identity_user_ids` JSON key order (same values across all 3 identity entries) and `visitor__universal_iids` `[]`-vs-`\N` empty notation.  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163404\_475088&externalid=20260530\_163409\_00028\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163404_475088&externalid=20260530_163409_00028_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163412\_050837&externalid=20260530\_163443\_00032\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163412_050837&externalid=20260530_163443_00032_4ujey)

Summary: No real differences found 

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 37
  Columns B: 37

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (37 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    visitor__universal_iids                                      1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163419\_694362&externalid=20260530\_163423\_00030\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163419_694362&externalid=20260530_163423_00030_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530163428\_921340&externalid=20260530\_163458\_00033\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530163428_921340&externalid=20260530_163458_00033_4ujey)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781180525817076708`, Network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612031828\_002093&externalid=20260612\_031832\_00054\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612031828_002093&externalid=20260612_031832_00054_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612031825\_723975&externalid=20260612\_031900\_00055\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612031825_723975&externalid=20260612_031900_00055_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 21 / 21
  Columns compared : 37

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 21 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (37 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 37 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - visitor__universal_iids
    - visitor__tracked_term
    - visitor__identity_user_ids

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Match: 21/21 rows, 37/37 columns, zero real data differences.
- `visitor__identity_user_ids` :JSON key-order only: Hoover `{"namespace_id":6,"id":"...UUID..."}` vs Hoover++ `{"id":"...UUID...","namespace_id":6}`, same keys/values.
- `visitor__universal_iids` / `visitor__tracked_term` empty written differently: `[]` (Hoover) vs `\N` (Hoover++).  
  
  
**Candidate Entity Level:**

candidate\_\_rtb\_impression\_index, `candidate__flags` are not in Hoover++.

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530180842\_096650&externalid=20260530\_180845\_00039\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530180842_096650&externalid=20260530_180845_00039_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530180732\_360737&externalid=20260530\_180800\_00038\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530180732_360737&externalid=20260530_180800_00038_4ujey)

Summary: Difference of 16 rows

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     2 row(s) are in old.csv but have NO matching row in new.csv.
     18 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780078157127344945'}
      {'request__transaction_id': '1780078157127344945'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780078157127344945', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    candidate__site_id                                           1 row(s)
    candidate__site_section_id                                   1 row(s)
    candidate__asset_id                                          1 row(s)
    candidate__series_id                                         1 row(s)
    candidate__internal_deal_id                                  1 row(s)
    candidate__internal_group_deal_id                            1 row(s)
    candidate__buyer_id                                          1 row(s)
    candidate__buyer_group_id                                    1 row(s)
    candidate__buyer_platform_id                                 1 row(s)
    candidate__dsp_id                                            1 row(s)
    candidate__media_buyer_id                                    1 row(s)
    candidate__trading_desk_id                                   1 row(s)
    candidate__sfx_buyer_id                                      1 row(s)
    candidate__sfx_dsp_id                                        1 row(s)
    candidate__filter_reason__error_category                     1 row(s)
    candidate__filter_reason__error                              1 row(s)
    candidate__filter_reason__slot_index                         1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    candidate__ad_id                                             1 row(s)
    candidate__rtb_auction_index                                 1 row(s)
    candidate__bid_status                                        1 row(s)
    candidate__original_price                                    1 row(s)
    candidate__raw_price                                         1 row(s)
    candidate__clearing_price                                    1 row(s)
    candidate__dsp_clearing_price                                1 row(s)
    candidate__dsp_clearing_price_discounted                     1 row(s)
    candidate__integration_type                                  1 row(s)
    candidate__market_ad_id                                      1 row(s)
    candidate__external_ad_id                                    1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    candidate__ad_id:
      old.csv: '65920238'
      new.csv: '0'
    candidate__rtb_auction_index:
      old.csv: '36'
      new.csv: '0'
    candidate__bid_status:
      old.csv: '15'
      new.csv: '0'
    candidate__original_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__raw_price:
      old.csv: '12.0'
      new.csv: '0.0'
    candidate__clearing_price:
      old.csv: '12.0'
      new.csv: '0.0'
    candidate__dsp_clearing_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__dsp_clearing_price_discounted:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__integration_type:
      old.csv: 'MKPL_PARTNER_TAG'
      new.csv: '\\N'
    candidate__market_ad_id:
      old.csv: '306953498'
      new.csv: '0'
    candidate__external_ad_id:
      old.csv: 'pt:innovid.com/59fa4d7b68c0ff2c032cd5c934864cf19075516950750130445'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178064848289535`, Network 520311
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612032926\_654220&externalid=20260612\_032930\_00056\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612032926_654220&externalid=20260612_032930_00056_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612032924\_254545&externalid=20260612\_033001\_00057\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612032924_254545&externalid=20260612_033001_00057_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++  REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 258 / 258
  Columns compared : 33

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 258 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (33 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 33 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - candidate__ad_id
    - candidate__rtb_auction_index
    - candidate__site_id
    - candidate__site_section_id
    - candidate__asset_id
    - candidate__series_id
    - candidate__bid_status
    - candidate__original_price
    - candidate__raw_price
    - candidate__clearing_price
    - candidate__dsp_clearing_price
    - candidate__dsp_clearing_price_discounted
    - candidate__internal_deal_id
    - candidate__internal_group_deal_id
    - candidate__buyer_id
    - candidate__buyer_group_id
    - candidate__buyer_platform_id
    - candidate__dsp_id
    - candidate__media_buyer_id
    - candidate__trading_desk_id
    - candidate__market_ad_id
    - candidate__sfx_buyer_id
    - candidate__sfx_dsp_id
    - candidate__bit_flags
    - candidate__filter_reason__error_category
    - candidate__filter_reason__error
    - candidate__filter_reason__slot_index

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- **MATCH** for candidate-entity transaction `1781178064848289535`.
- 258 rows each, 33 columns identical, all compared columns match.
- Hoover writes every field as `\N`, while Hoover++ writes `0` / `0.0` / `\N`. All 27 differing columns (including `candidate__bit_flags`) are null-vs-zero representation only, so they're suppressed as semantically equivalent.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530180947\_866327&externalid=20260530\_180950\_00040\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530180947_866327&externalid=20260530_180950_00040_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530180953\_156975&externalid=20260530\_181020\_00042\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530180953_156975&externalid=20260530_181020_00042_4ujey)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.  
  
**Updated Analysis:**

- Transaction `1781179885207066284`, Network 535262
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612033658\_135917&externalid=20260612\_033703\_00058\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612033658_135917&externalid=20260612_033703_00058_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612033656\_914932&externalid=20260612\_033734\_00059\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612033656_914932&externalid=20260612_033734_00059_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : oldhoover.csv
  Source B (NEW / Hoover++)  : newhoover.csv
  Rows  A / B      : 10 / 10
  Columns compared : 33

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 10 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (33 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 33 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - candidate__ad_id
    - candidate__rtb_auction_index
    - candidate__site_id
    - candidate__site_section_id
    - candidate__asset_id
    - candidate__series_id
    - candidate__bid_status
    - candidate__original_price
    - candidate__raw_price
    - candidate__clearing_price
    - candidate__dsp_clearing_price
    - candidate__dsp_clearing_price_discounted
    - candidate__internal_deal_id
    - candidate__internal_group_deal_id
    - candidate__buyer_id
    - candidate__buyer_group_id
    - candidate__buyer_platform_id
    - candidate__dsp_id
    - candidate__media_buyer_id
    - candidate__trading_desk_id
    - candidate__market_ad_id
    - candidate__sfx_buyer_id
    - candidate__sfx_dsp_id
    - candidate__bit_flags
    - candidate__filter_reason__error_category
    - candidate__filter_reason__error
    - candidate__filter_reason__slot_index

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: MATCH** for candidate-entity transaction `1781179885207066284`.

- 10 rows each, 33 columns identical, all compared columns match.
- Empty/no-candidate record: Hoover writes every field as `\N`, Hoover++ writes `0` / `0.0` / `\N`. All 27 differing columns (including `candidate__bit_flags`) are null-vs-zero representation only, suppressed as semantically equivalent.  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181001\_400357&externalid=20260530\_181005\_00041\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181001_400357&externalid=20260530_181005_00041_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181009\_457158&externalid=20260530\_181036\_00045\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181009_457158&externalid=20260530_181036_00045_4ujey)

Summary: Difference of 3 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     9 row(s) are in old.csv but have NO matching row in new.csv.
     6 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}
      {'request__transaction_id': '1780076927707289550', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    candidate__ad_id                                             1 row(s)
    candidate__rtb_auction_index                                 1 row(s)
    candidate__site_id                                           1 row(s)
    candidate__site_section_id                                   1 row(s)
    candidate__asset_id                                          1 row(s)
    candidate__series_id                                         1 row(s)
    candidate__bid_status                                        1 row(s)
    candidate__internal_deal_id                                  1 row(s)
    candidate__internal_group_deal_id                            1 row(s)
    candidate__buyer_id                                          1 row(s)
    candidate__buyer_group_id                                    1 row(s)
    candidate__buyer_platform_id                                 1 row(s)
    candidate__dsp_id                                            1 row(s)
    candidate__media_buyer_id                                    1 row(s)
    candidate__trading_desk_id                                   1 row(s)
    candidate__market_ad_id                                      1 row(s)
    candidate__sfx_buyer_id                                      1 row(s)
    candidate__sfx_dsp_id                                        1 row(s)
    candidate__bit_flags                                         1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    candidate__original_price                                    1 row(s)
    candidate__raw_price                                         1 row(s)
    candidate__clearing_price                                    1 row(s)
    candidate__dsp_clearing_price                                1 row(s)
    candidate__dsp_clearing_price_discounted                     1 row(s)

  Detailed diffs:

  [key=('1780076927707289550',)]
    candidate__original_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__raw_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__clearing_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__dsp_clearing_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__dsp_clearing_price_discounted:
      old.csv: '\\N'
      new.csv: '0.0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178825199440529`, Network 384777
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612035308\_305047&externalid=20260612\_035312\_00061\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612035308_305047&externalid=20260612_035312_00061_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612035306\_390445&externalid=20260612\_035340\_00062\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612035306_390445&externalid=20260612_035340_00062_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 79 / 79
  Columns compared : 33

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 79 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (33 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 33 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - candidate__ad_id
    - candidate__rtb_auction_index
    - candidate__site_id
    - candidate__site_section_id
    - candidate__asset_id
    - candidate__series_id
    - candidate__bid_status
    - candidate__original_price
    - candidate__raw_price
    - candidate__clearing_price
    - candidate__dsp_clearing_price
    - candidate__dsp_clearing_price_discounted
    - candidate__internal_deal_id
    - candidate__internal_group_deal_id
    - candidate__buyer_id
    - candidate__buyer_group_id
    - candidate__buyer_platform_id
    - candidate__dsp_id
    - candidate__media_buyer_id
    - candidate__trading_desk_id
    - candidate__market_ad_id
    - candidate__sfx_buyer_id
    - candidate__sfx_dsp_id
    - candidate__bit_flags

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: MATCH** for candidate-entity transaction `1781178825199440529`.

- 79 rows each, 33 columns identical, all compared columns match.
- Empty/no-candidate record: Hoover writes every field as `\N`, Hoover++ writes `0` / `0.0` / `\N`. All 24 differing columns (including `candidate__bit_flags`) are null-vs-zero representation only, suppressed as semantically equivalent.  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181018\_736566&externalid=20260530\_181021\_00043\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181018_736566&externalid=20260530_181021_00043_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181025\_093358&externalid=20260530\_181104\_00046\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181025_093358&externalid=20260530_181104_00046_4ujey)

Summary: Some differences with the same number of rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     1 row(s) are in old.csv but have NO matching row in new.csv.
     1 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780079174184480780',)]  old.csv: 3 rows  |  new.csv: 3 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780079174184480780'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780079174184480780', 'candidate__ad_id': '0', 'candidate__rtb_auction_index': '0', 'candidate__site_id': '0', 'candidate__site_section_id': '0', 'candidate__asset_id': '0', 'candidate__series_id': '0', 'candidate__bid_status': '0', 'candidate__original_price': '0.0', 'candidate__raw_price': '0.0', 'candidate__clearing_price': '0.0', 'candidate__dsp_clearing_price': '0.0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    candidate__ad_id                                             1 row(s)
    candidate__rtb_auction_index                                 1 row(s)
    candidate__site_id                                           1 row(s)
    candidate__site_section_id                                   1 row(s)
    candidate__asset_id                                          1 row(s)
    candidate__series_id                                         1 row(s)
    candidate__bid_status                                        1 row(s)
    candidate__internal_deal_id                                  1 row(s)
    candidate__internal_group_deal_id                            1 row(s)
    candidate__buyer_id                                          1 row(s)
    candidate__buyer_group_id                                    1 row(s)
    candidate__buyer_platform_id                                 1 row(s)
    candidate__dsp_id                                            1 row(s)
    candidate__media_buyer_id                                    1 row(s)
    candidate__trading_desk_id                                   1 row(s)
    candidate__market_ad_id                                      1 row(s)
    candidate__sfx_buyer_id                                      1 row(s)
    candidate__sfx_dsp_id                                        1 row(s)
    candidate__bit_flags                                         1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    candidate__original_price                                    1 row(s)
    candidate__raw_price                                         1 row(s)
    candidate__clearing_price                                    1 row(s)
    candidate__dsp_clearing_price                                1 row(s)
    candidate__dsp_clearing_price_discounted                     1 row(s)

  Detailed diffs:

  [key=('1780079174184480780',)]
    candidate__original_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__raw_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__clearing_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__dsp_clearing_price:
      old.csv: '\\N'
      new.csv: '0.0'
    candidate__dsp_clearing_price_discounted:
      old.csv: '\\N'
      new.csv: '0.0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781180431719065593`, Network 169843
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612040142\_888399&externalid=20260612\_040147\_00063\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612040142_888399&externalid=20260612_040147_00063_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612040140\_363290&externalid=20260612\_040215\_00064\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612040140_363290&externalid=20260612_040215_00064_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 150 / 150
  Columns compared : 33

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 150 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (33 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 33 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - candidate__ad_id
    - candidate__rtb_auction_index
    - candidate__site_id
    - candidate__site_section_id
    - candidate__asset_id
    - candidate__series_id
    - candidate__bid_status
    - candidate__original_price
    - candidate__raw_price
    - candidate__clearing_price
    - candidate__dsp_clearing_price
    - candidate__dsp_clearing_price_discounted
    - candidate__internal_deal_id
    - candidate__internal_group_deal_id
    - candidate__buyer_id
    - candidate__buyer_group_id
    - candidate__buyer_platform_id
    - candidate__dsp_id
    - candidate__media_buyer_id
    - candidate__trading_desk_id
    - candidate__market_ad_id
    - candidate__sfx_buyer_id
    - candidate__sfx_dsp_id
    - candidate__bit_flags
    - candidate__filter_reason__error_category
    - candidate__filter_reason__error
    - candidate__filter_reason__slot_index

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** Match all 150/150 rows, 33/33 columns match; real candidate values (ad IDs, prices, dsp IDs, bid\_status) are identical, only empty-row notation differs (`\N` vs `0`/`0.0`).  

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181031\_359552&externalid=20260530\_181036\_00044\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181031_359552&externalid=20260530_181036_00044_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530181039\_103714&externalid=20260530\_181108\_00047\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530181039_103714&externalid=20260530_181108_00047_4ujey)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781180525817076708`, Network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612041140\_176902&externalid=20260612\_041145\_00065\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612041140_176902&externalid=20260612_041145_00065_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612041138\_416282&externalid=20260612\_041216\_00066\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612041138_416282&externalid=20260612_041216_00066_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 21 / 21
  Columns compared : 33

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 21 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (33 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 33 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - candidate__ad_id
    - candidate__rtb_auction_index
    - candidate__site_id
    - candidate__site_section_id
    - candidate__asset_id
    - candidate__series_id
    - candidate__bid_status
    - candidate__original_price
    - candidate__raw_price
    - candidate__clearing_price
    - candidate__dsp_clearing_price
    - candidate__dsp_clearing_price_discounted
    - candidate__internal_deal_id
    - candidate__internal_group_deal_id
    - candidate__buyer_id
    - candidate__buyer_group_id
    - candidate__buyer_platform_id
    - candidate__dsp_id
    - candidate__media_buyer_id
    - candidate__trading_desk_id
    - candidate__market_ad_id
    - candidate__sfx_buyer_id
    - candidate__sfx_dsp_id
    - candidate__bit_flags
    - candidate__filter_reason__error_category
    - candidate__filter_reason__error
    - candidate__filter_reason__slot_index

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: **Match: 21/21 rows, 33/33 columns, zero real data differences.

- Both files carry the same 15 rows of real candidate data: `candidate__ad_id 53386504`, `bid_status 15`, `clearing_price 11.0`, `bit_flags 524288`, plus the `COMPETITION_FAILURE` / `EXCEED_MAX_NUM_ADVERTISEMENTS` filter reasons with identical counts. The only difference is the 6 empty rows: `\N` (Hoover) vs `0`/`0.0` (Hoover++), which is expected null-zero representation.  

### **Slot Entity Level:**

slot\_\_slot\_id is missing in Hoover++

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182355\_478069&externalid=20260530\_182359\_00049\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182355_478069&externalid=20260530_182359_00049_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182246\_312309&externalid=20260530\_182319\_00048\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182246_312309&externalid=20260530_182319_00048_4ujey)

Summary: Difference of 16 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 25
  Columns B: 25

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (25 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     16 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}
      {'request__transaction_id': '1780078157127344945', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '19', 'slot__ad_unit_id': '71720', 'slot__ad_unit_network_id': '520311', 'slot__normalized_ad_unit_id': '71720', 'slot__max_ads': '5', 'slot__num_ads': '5', 'slot__max_duration': '121', 'slot__min_duration': '121', 'slot__initial_time_unfilled': '1'}

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

**Updated Analysis:**

- Transaction `1781179145292123127`, Network 520311
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612041907\_822444&externalid=20260612\_041912\_00067\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612041907_822444&externalid=20260612_041912_00067_m8zwn)
- Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612041904\_629791&externalid=20260612\_041942\_00068\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612041904_629791&externalid=20260612_041942_00068_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 199 / 199
  Columns compared : 25

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 199 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (25 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 25 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  [OK] None.

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: ** Match, all 199 rows and 25 columns match exactly, including `slot__flags`, with no differences of any kind.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182403\_163912&externalid=20260530\_182407\_00050\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182403_163912&externalid=20260530_182407_00050_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182408\_239166&externalid=20260530\_182436\_00053\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182408_239166&externalid=20260530_182436_00053_4ujey)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781180575132557551`**,** Network 535262
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612042508\_464865&externalid=20260612\_042511\_00070\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612042508_464865&externalid=20260612_042511_00070_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612042506\_879177&externalid=20260612\_042538\_00071\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612042506_879177&externalid=20260612_042538_00071_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 12 / 12
  Columns compared : 25

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 12 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (25 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 25 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  [OK] None.

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** Match, all 12 rows and 25 columns match exactly, including `slot__flags`, with no differences of any kind.


1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182414\_284830&externalid=20260530\_182418\_00051\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182414_284830&externalid=20260530_182418_00051_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182421\_998368&externalid=20260530\_182450\_00055\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182421_998368&externalid=20260530_182450_00055_4ujey)

Summary: Difference of 4 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 25
  Columns B: 25

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (25 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     6 row(s) are in old.csv but have NO matching row in new.csv.
     3 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550', 'slot__index': '7', 'slot__slot_sequence': '3', 'slot__sequence': '2', 'slot__normalized_ad_unit_id': '2', 'slot__max_ads': '1', 'slot__num_ads': '1', 'slot__avails': '1', 'slot__unfilled_avails': '0', 'slot__time_position': '0.0', 'slot__avails_metrics__opportunity': '[1]', 'slot__avails_metrics__avails': '[1]'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550', 'slot__index': '5', 'slot__slot_sequence': '2', 'slot__sequence': '1', 'slot__normalized_ad_unit_id': '2', 'slot__max_ads': '1', 'slot__num_ads': '1', 'slot__avails': '1', 'slot__unfilled_avails': '0', 'slot__time_position': '0.0', 'slot__avails_metrics__opportunity': '[1]', 'slot__avails_metrics__avails': '[1]'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550', 'slot__index': '3', 'slot__slot_sequence': '1', 'slot__sequence': '0', 'slot__normalized_ad_unit_id': '2', 'slot__max_ads': '1', 'slot__num_ads': '1', 'slot__avails': '1', 'slot__unfilled_avails': '0', 'slot__time_position': '0.0', 'slot__avails_metrics__opportunity': '[1]', 'slot__avails_metrics__avails': '[1]'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780076927707289550', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '0', 'slot__break_id': '0', 'slot__opportunity_id': '0', 'slot__ad_unit_id': '0', 'slot__ad_unit_network_id': '0', 'slot__normalized_ad_unit_id': '0', 'slot__max_ads': '0', 'slot__num_ads': '0', 'slot__max_duration': '0'}
      {'request__transaction_id': '1780076927707289550', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '0', 'slot__break_id': '0', 'slot__opportunity_id': '0', 'slot__ad_unit_id': '0', 'slot__ad_unit_network_id': '0', 'slot__normalized_ad_unit_id': '0', 'slot__max_ads': '0', 'slot__num_ads': '0', 'slot__max_duration': '0'}
      {'request__transaction_id': '1780076927707289550', 'slot__index': '0', 'slot__slot_sequence': '0', 'slot__sequence': '0', 'slot__break_id': '0', 'slot__opportunity_id': '0', 'slot__ad_unit_id': '0', 'slot__ad_unit_network_id': '0', 'slot__normalized_ad_unit_id': '0', 'slot__max_ads': '0', 'slot__num_ads': '0', 'slot__max_duration': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    slot__break_id                                               1 row(s)
    slot__opportunity_id                                         1 row(s)
    slot__ad_unit_id                                             1 row(s)
    slot__ad_unit_network_id                                     1 row(s)
    slot__min_duration                                           1 row(s)
    slot__avails_metrics__unfilled_avails                        1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    slot__index                                                  1 row(s)
    slot__slot_sequence                                          1 row(s)
    slot__sequence                                               1 row(s)
    slot__normalized_ad_unit_id                                  1 row(s)
    slot__max_ads                                                1 row(s)
    slot__num_ads                                                1 row(s)
    slot__max_duration                                           1 row(s)
    slot__avails                                                 1 row(s)
    slot__avails_metrics__opportunity                            1 row(s)
    slot__avails_metrics__avails                                 1 row(s)
    slot__time_position_class                                    1 row(s)
    slot__environment                                            1 row(s)
    slot__profile_id                                             1 row(s)
    slot__flags                                                  1 row(s)

  Detailed diffs:

  [key=('1780076927707289550',)]
    slot__index:
      old.csv: '4'
      new.csv: '0'
    slot__slot_sequence:
      old.csv: '2'
      new.csv: '0'
    slot__sequence:
      old.csv: '1'
      new.csv: '0'
    slot__normalized_ad_unit_id:
      old.csv: '2'
      new.csv: '0'
    slot__max_ads:
      old.csv: '1'
      new.csv: '0'
    slot__num_ads:
      old.csv: '1'
      new.csv: '0'
    slot__max_duration:
      old.csv: '30'
      new.csv: '0'
    slot__avails:
      old.csv: '1'
      new.csv: '0'
    slot__avails_metrics__opportunity:
      old.csv: '[1]'
      new.csv: '\\N'
    slot__avails_metrics__avails:
      old.csv: '[1]'
      new.csv: '\\N'
    slot__time_position_class:
      old.csv: 'midroll'
      new.csv: '\\N'
    slot__environment:
      old.csv: 'VIDEO'
      new.csv: '\\N'
    slot__profile_id:
      old.csv: '2563'
      new.csv: '0'
    slot__flags:
      old.csv: '2080'
      new.csv: '0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178825199440529`, Network 384777
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612043036\_889459&externalid=20260612\_043039\_00072\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612043036_889459&externalid=20260612_043039_00072_m8zwn)
- Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612043040\_658566&externalid=20260612\_043115\_00073\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612043040_658566&externalid=20260612_043115_00073_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 79 / 79
  Columns compared : 25

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 79 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (25 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 25 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - slot__index
    - slot__slot_sequence
    - slot__sequence
    - slot__break_id
    - slot__opportunity_id
    - slot__ad_unit_id
    - slot__ad_unit_network_id
    - slot__normalized_ad_unit_id
    - slot__max_ads
    - slot__num_ads
    - slot__max_duration
    - slot__min_duration
    - slot__initial_time_unfilled
    - slot__time_unfilled
    - slot__avails
    - slot__unfilled_avails
    - slot__time_position
    - slot__profile_id
    - slot__flags

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** Match, 79/79 rows, all 25 columns match; real slot data and `slot__flags 2048` identical, only `\N`-vs-`0` empty notation differs.

- Visitor, advertisement, candidate, slot entities: all match , the differences limited to representational only (`\N`/`0`/`[]` null-zero semantics and JSON key order).  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182427\_848177&externalid=20260530\_182431\_00052\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182427_848177&externalid=20260530_182431_00052_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182440\_372608&externalid=20260530\_182508\_00056\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182440_372608&externalid=20260530_182508_00056_4ujey)

Summary: No real differences found 

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 25
  Columns B: 25

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (25 columns)

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

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182441\_565826&externalid=20260530\_181036\_00044\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182441_565826&externalid=20260530_181036_00044_4ujey)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260530182452\_673724&externalid=20260530\_182520\_00057\_4ujey](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260530182452_673724&externalid=20260530_182520_00057_4ujey)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

**Updated Analysis:**

- Transaction `1781179991809961739` Network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612044332\_255596&externalid=20260612\_044337\_00075\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612044332_255596&externalid=20260612_044337_00075_m8zwn)
- Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612044330\_779973&externalid=20260612\_044404\_00077\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612044330_779973&externalid=20260612_044404_00077_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 26 / 26
  Columns compared : 25

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 26 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (25 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 25 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  [OK] None.

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** Match, 26 rows each side, all 25 compared columns hold identical value multisets, with `slot__flags 256` consistent throughout.

`slot__index`** looks different row-by-row in file order** (Hoover starts `2,2,2,2,2…`, Hoover++ starts `0,1,2,3…`), **but once sorted both files are identical: **`0×6, 1×6, 2×6, 3×6, 4×1, 5×1`:  **same slots, same counts, only the row ordering within the file differs.**

So there is no data difference here; the only thing to note is that Hoover groups rows by slot while Hoover++ interleaves them, which is an ordering difference, not a value difference.


### **Auction Entity Level:**

auction\_\_network\_execution\_ctx\_index, `auction__bid_request_count, auction__bid_to_eur_exchange_rate,auction__buyer_id,auction__metadata_auditing_flags` is missing in Hoover++

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531061325\_147159&externalid=20260531\_061330\_00006\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531061325_147159&externalid=20260531_061330_00006_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531060239\_040387&externalid=20260531\_060319\_00005\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531060239_040387&externalid=20260531_060319_00005_k22np)

Summary: Difference of 16 rows

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 22
  Columns B: 22

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (22 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     2 row(s) are in old.csv but have NO matching row in new.csv.
     18 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780078157127344945'}
      {'request__transaction_id': '1780078157127344945'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780078157127344945', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    auction__site_id                                             1 row(s)
    auction__site_section_id                                     1 row(s)
    auction__series_id                                           1 row(s)
    auction__asset_id                                            1 row(s)
    auction__dsp_id                                              1 row(s)
    auction__buyer_group_id                                      1 row(s)
    auction__buyer_platform_id                                   1 row(s)
    auction__bid_throttling_info__flags                          1 row(s)
    auction__bid_throttling_status                               1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    auction__network_id                                          1 row(s)
    auction__auction_status                                      1 row(s)
    auction__auction_network_to_eur_exchange_rate                1 row(s)
    auction__auction_network_to_usd_exchange_rate                1 row(s)
    auction__time_position_class                                 1 row(s)
    auction__flags                                               1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    auction__network_id:
      old.csv: '516429'
      new.csv: '0'
    auction__auction_status:
      old.csv: '14'
      new.csv: '0'
    auction__auction_network_to_eur_exchange_rate:
      old.csv: '0.858187'
      new.csv: '0.0'
    auction__auction_network_to_usd_exchange_rate:
      old.csv: '1.0'
      new.csv: '0.0'
    auction__time_position_class:
      old.csv: 'midroll'
      new.csv: '\\N'
    auction__flags:
      old.csv: '151519744'
      new.csv: '0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178306696942889`, Network 520311
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612045131\_067738&externalid=20260612\_045134\_00078\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612045131_067738&externalid=20260612_045134_00078_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612045135\_029036&externalid=20260612\_045206\_00079\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612045135_029036&externalid=20260612_045206_00079_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 197 / 197
  Columns compared : 22

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 197 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (22 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 22 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - auction__network_id
    - auction__site_id
    - auction__site_section_id
    - auction__series_id
    - auction__asset_id
    - auction__auction_status
    - auction__auction_network_to_eur_exchange_rate
    - auction__auction_network_to_usd_exchange_rate
    - auction__bid_to_usd_exchange_rate
    - auction__dsp_id
    - auction__buyer_group_id
    - auction__buyer_platform_id
    - auction__flags
    - auction__bid_throttling_info__flags
    - auction__bid_throttling_status

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: **Match: 197/197 rows, all 22 auction ack columns confirmed identical (real values match, empty counts equal), including `auction__flags` (`268971041 x12`, `285748256 x6` on both sides).

- Only differences are the expected `\N`→`0` null-zero notation on empty rows.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062223\_977676&externalid=20260531\_062227\_00007\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062223_977676&externalid=20260531_062227_00007_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062233\_695668&externalid=20260531\_062309\_00010\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062233_695668&externalid=20260531_062309_00010_k22np)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.

**Updated Analysis: **

- Transaction `1781180575132557551` Network 535262
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612045839\_951420&externalid=20260612\_045843\_00080\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612045839_951420&externalid=20260612_045843_00080_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612045836\_272605&externalid=20260612\_045901\_00081\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612045836_272605&externalid=20260612_045901_00081_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 12 / 12
  Columns compared : 22

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 12 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (22 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 22 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - auction__network_id
    - auction__site_id
    - auction__site_section_id
    - auction__series_id
    - auction__asset_id
    - auction__auction_status
    - auction__auction_network_to_eur_exchange_rate
    - auction__auction_network_to_usd_exchange_rate
    - auction__bid_to_usd_exchange_rate
    - auction__dsp_id
    - auction__buyer_group_id
    - auction__buyer_platform_id
    - auction__flags
    - auction__bid_throttling_info__flags
    - auction__bid_throttling_status

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** Match, Both Hoover and Hoover++ populate auction data identically for this transaction; the only difference is the 5 empty rows written as `\N` (Hoover) vs `0` (Hoover++).  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062241\_010259&externalid=20260531\_062244\_00008\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062241_010259&externalid=20260531_062244_00008_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062250\_336409&externalid=20260531\_062318\_00012\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062250_336409&externalid=20260531_062318_00012_k22np)

Summary: Difference of 3 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 22
  Columns B: 22

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (22 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     9 row(s) are in old.csv but have NO matching row in new.csv.
     6 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
      {'request__transaction_id': '1780076927707289550'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}
      {'request__transaction_id': '1780076927707289550', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    auction__network_id                                          1 row(s)
    auction__site_id                                             1 row(s)
    auction__site_section_id                                     1 row(s)
    auction__series_id                                           1 row(s)
    auction__asset_id                                            1 row(s)
    auction__auction_status                                      1 row(s)
    auction__dsp_id                                              1 row(s)
    auction__buyer_group_id                                      1 row(s)
    auction__buyer_platform_id                                   1 row(s)
    auction__flags                                               1 row(s)
    auction__bid_throttling_info__flags                          1 row(s)
    auction__bid_throttling_status                               1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    auction__auction_network_to_eur_exchange_rate                1 row(s)
    auction__auction_network_to_usd_exchange_rate                1 row(s)
    auction__bid_to_usd_exchange_rate                            1 row(s)

  Detailed diffs:

  [key=('1780076927707289550',)]
    auction__auction_network_to_eur_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'
    auction__auction_network_to_usd_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'
    auction__bid_to_usd_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis: **

- Transaction `1781178373156217993`, Network 384777
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612050428\_657452&externalid=20260612\_050432\_00082\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612050428_657452&externalid=20260612_050432_00082_m8zwn)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612050432\_406091&externalid=20260612\_050509\_00083\_m8zwn](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612050432_406091&externalid=20260612_050509_00083_m8zwn)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 80 / 80
  Columns compared : 22

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 80 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (22 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 22 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - auction__network_id
    - auction__site_id
    - auction__site_section_id
    - auction__series_id
    - auction__asset_id
    - auction__auction_status
    - auction__auction_network_to_eur_exchange_rate
    - auction__auction_network_to_usd_exchange_rate
    - auction__bid_to_usd_exchange_rate
    - auction__dsp_id
    - auction__buyer_group_id
    - auction__buyer_platform_id
    - auction__flags
    - auction__bid_throttling_info__flags
    - auction__bid_throttling_status

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:** All Match:

- All 22 auction ack columns: `real values identical AND empty counts equal => True`.
- This is an empty/no-auction record, there are no real auction values on either side; every cell is empty. Hoover writes all 80 rows as `\N`; Hoover++ writes the same rows as `0`/`0.0` for numeric/flag columns and `\N` for string columns.
- `auction__flags`: OLD `\N x80` vs NEW `\N x67, 0 x13` , both 80 empty, zero real flag values. No flag drift.
- `auction__network_id`: OLD `\N x80` vs NEW `\N x67, 0 x13`, no real network value on either side.  

1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062258\_579128&externalid=20260531\_062301\_00009\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062258_579128&externalid=20260531_062301_00009_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062305\_944616&externalid=20260531\_062333\_00013\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062305_944616&externalid=20260531_062333_00013_k22np)

Summary: Difference of records in 1 row.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 22
  Columns B: 22

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (22 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     1 row(s) are in old.csv but have NO matching row in new.csv.
     1 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780079174184480780',)]  old.csv: 3 rows  |  new.csv: 3 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780079174184480780'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780079174184480780', 'auction__network_id': '0', 'auction__site_id': '0', 'auction__site_section_id': '0', 'auction__series_id': '0', 'auction__asset_id': '0', 'auction__auction_status': '0', 'auction__auction_network_to_eur_exchange_rate': '0.0', 'auction__auction_network_to_usd_exchange_rate': '0.0', 'auction__bid_to_usd_exchange_rate': '0.0', 'auction__dsp_id': '0', 'auction__buyer_group_id': '0'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    auction__network_id                                          1 row(s)
    auction__site_id                                             1 row(s)
    auction__site_section_id                                     1 row(s)
    auction__series_id                                           1 row(s)
    auction__asset_id                                            1 row(s)
    auction__auction_status                                      1 row(s)
    auction__dsp_id                                              1 row(s)
    auction__buyer_group_id                                      1 row(s)
    auction__buyer_platform_id                                   1 row(s)
    auction__flags                                               1 row(s)
    auction__bid_throttling_info__flags                          1 row(s)
    auction__bid_throttling_status                               1 row(s)

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    auction__auction_network_to_eur_exchange_rate                1 row(s)
    auction__auction_network_to_usd_exchange_rate                1 row(s)
    auction__bid_to_usd_exchange_rate                            1 row(s)

  Detailed diffs:

  [key=('1780079174184480780',)]
    auction__auction_network_to_eur_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'
    auction__auction_network_to_usd_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'
    auction__bid_to_usd_exchange_rate:
      old.csv: '\\N'
      new.csv: '0.0'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction 1781177659862718397, Network 169843
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612151206\_048900&externalid=20260612\_151212\_00097\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612151206_048900&externalid=20260612_151212_00097_r4cjx)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612151203\_694220&externalid=20260612\_151242\_00098\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612151203_694220&externalid=20260612_151242_00098_r4cjx)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 140 / 140
  Columns compared : 22

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 140 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (22 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 22 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - auction__network_id
    - auction__site_id
    - auction__site_section_id
    - auction__series_id
    - auction__asset_id
    - auction__auction_status
    - auction__auction_network_to_eur_exchange_rate
    - auction__auction_network_to_usd_exchange_rate
    - auction__bid_to_usd_exchange_rate
    - auction__dsp_id
    - auction__buyer_group_id
    - auction__buyer_platform_id
    - auction__flags
    - auction__bid_throttling_info__flags
    - auction__bid_throttling_status

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

**Summary: Match **140 rows on each side, all 22 auction columns confirmed identical, with the real auction data (`network_id 169843` and `auction__flags 285801761`, each on 10 rows) matching exactly.

- The only difference is that there are empty rows are written as `\N` in Hoover, while Hoover++ writes them as a mix of `\N` and `0` (130 empty total on both sides)  

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062314\_894730&externalid=20260531\_062318\_00011\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062314_894730&externalid=20260531_062318_00011_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531062322\_802284&externalid=20260531\_062349\_00014\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531062322_802284&externalid=20260531_062349_00014_k22np)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

  
**Updated Analysis:**

- Transaction `1781179336336761918`, Network 532076
- Hoover:  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612180912\_712406&externalid=20260612\_180916\_00058\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612180912_712406&externalid=20260612_180916_00058_fnmf6)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612180915\_518156&externalid=20260612\_180950\_00059\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612180915_518156&externalid=20260612_180950_00059_fnmf6)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 26 / 26
  Columns compared : 22

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 26 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (22 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [OK] All 22 compared columns match between Hoover and Hoover++.

── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - auction__network_id
    - auction__site_id
    - auction__site_section_id
    - auction__series_id
    - auction__asset_id
    - auction__auction_status
    - auction__auction_network_to_eur_exchange_rate
    - auction__auction_network_to_usd_exchange_rate
    - auction__bid_to_usd_exchange_rate
    - auction__dsp_id
    - auction__buyer_group_id
    - auction__buyer_platform_id
    - auction__flags
    - auction__bid_throttling_info__flags
    - auction__bid_throttling_status

── RESULT ────────────────────────────────────────────────────────────────
  [OK] PASS — Hoover and Hoover++ are an exact match (only null/zero/empty semantics differ).

========================================================================
  END OF REPORT
========================================================================
```

- **Summary:** Match**, **both Hoover and Hoover++ carry the same 20 rows of real auction data (`network_id 510839`, `flags 352856609`) and 6 empty rows; the only difference is the expected `\N`→`0` notation on those 6 empty rows.


### **Partners Entity Level:**

1. **Network 520311**

request\_\_transaction\_id = 1780078157127344945

**Step 1 – Hoover (mrm\_log\_flat.default) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071429\_922429&externalid=20260531\_071433\_00016\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071429_922429&externalid=20260531_071433_00016_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 520311**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071253\_732660&externalid=20260531\_071334\_00015\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071253_732660&externalid=20260531_071334_00015_k22np)

Summary: Difference of 16 rows.

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 33
  Rows  B  : 49
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=33  B=49  diff=16

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     33 row(s) are in old.csv but have NO matching row in new.csv.
     49 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780078157127344945',)]  old.csv: 33 rows  |  new.csv: 49 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_index': '[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_index': '[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]', 'partners__bit_flags': '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', 'partners__entity_source': '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]', 'partners__asset_id': '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]', 'partners__asset_group_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__series_id': '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]', 'partners__site_section_id': '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]', 'partners__site_section_group_ids': '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 525290, 520311]', 'partners__bit_flags': '[1099513724928, 2199023255552, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 4, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 512167, 520311]', 'partners__bit_flags': '[32, 0, 0]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, null, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[516429, 516429, 516429]', 'partners__asset_id': '[428568186, -1, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]', 'partners__series_id': '[null, null, null]', 'partners__site_section_id': '[24049426, -1, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}
      {'request__transaction_id': '1780078157127344945', 'partners__network_id': '[516429, 520311]', 'partners__bit_flags': '[0, 0]', 'partners__entity_source': '[ad, ad]', 'partners__network_execution_ctx_index': '[0, 1]', 'partners__network_execution_ctx_flags': '[null, null]', 'partners__content_owner_network_id': '[516429, 516429]', 'partners__asset_id': '[428568186, -1]', 'partners__asset_group_id': '[null, null]', 'partners__asset_group_ids': '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null]', 'partners__series_id': '[null, null]', 'partners__site_section_id': '[24049426, 17836669]'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    partners__network_id                                         1 row(s)
    partners__bit_flags                                          1 row(s)
    partners__entity_source                                      1 row(s)
    partners__network_execution_ctx_index                        1 row(s)
    partners__network_execution_ctx_flags                        1 row(s)
    partners__content_owner_network_id                           1 row(s)
    partners__asset_id                                           1 row(s)
    partners__asset_group_id                                     1 row(s)
    partners__asset_group_ids                                    1 row(s)
    partners__series_id                                          1 row(s)
    partners__site_section_id                                    1 row(s)
    partners__site_section_group_ids                             1 row(s)
    partners__site_id                                            1 row(s)
    partners__inventory_package_ids                              1 row(s)
    partners__supply_source                                      1 row(s)
    partners__sales_channel                                      1 row(s)
    partners__inbound_order_id                                   1 row(s)
    partners__inbound_order_type                                 1 row(s)
    partners__inbound_listing_id                                 1 row(s)
    partners__deal_awareability                                  1 row(s)
    partners__reseller_network_id                                1 row(s)
    partners__inbound_listing_ids                                1 row(s)
    partners__outbound_order_type                                1 row(s)
    partners__supply_source_type                                 1 row(s)
    partners__internal_deal_ids                                  1 row(s)
    partners__outbound_order_id                                  1 row(s)
    partners__outbound_order_ids                                 1 row(s)
    partners__buyer_ids                                          1 row(s)
    partners__internal_seat_ids                                  1 row(s)
    partners__outbound_listing_id                                1 row(s)
    partners__matched_inventory_package_ids                      1 row(s)
    partners__global_currency_id                                 1 row(s)

  Detailed diffs:

  [key=('1780078157127344945',)]
    partners__network_id:
      old.csv: '[516429, 525290, 520311]'
      new.csv: '[516429, 525290, 510839, 525290, 537323, 539372, 512029, 539372, 525290, 510839, 512029, 510839, 520311, 523319, 523319, 523319, 528950, 537323, 530362, 539372, 529256, 512029, 535045, 523319, 523319, 523319, 520024, 376521, 505334, 538726, 384777, 538726, 538726, 538726, 524565, 524565]'
    partners__bit_flags:
      old.csv: '[1099513724928, 2199023255552, 0]'
      new.csv: '[4096, 2199023255552, 0, 2199023255552, 0, 0, 0, 0, 2199023255552, 0, 0, 0, 0, 33554432, 33554432, 33554432, 2199023255552, 0, 0, 0, 2199023255552, 0, 2199023255552, 33554432, 33554432, 33554432, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'
    partners__entity_source:
      old.csv: '[ad, ad, ad]'
      new.csv: '[slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot, slot]'
    partners__network_execution_ctx_index:
      old.csv: '[0, 4, 1]'
      new.csv: '\\N'
    partners__network_execution_ctx_flags:
      old.csv: '[null, null, null]'
      new.csv: '[null, null, null, null, null, null, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, 16777217, 16777217, 16777217, null, null, null, null, null, null, null, null, null, null]'
    partners__content_owner_network_id:
      old.csv: '[516429, 516429, 516429]'
      new.csv: '[516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 516429, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 520311, 516429, 520024, 520024, 376521, 520024, 384777, 384777, 384777, 384777, 384777]'
    partners__asset_id:
      old.csv: '[428568186, -1, -1]'
      new.csv: '[428568186, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]'
    partners__asset_group_id:
      old.csv: '[null, null, null]'
      new.csv: '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]'
    partners__asset_group_ids:
      old.csv: '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null]'
      new.csv: '[[18532420, 18698780, 18698781, 1333261694, 1487831009], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]'
    partners__series_id:
      old.csv: '[null, null, null]'
      new.csv: '[null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]'
    partners__site_section_id:
      old.csv: '[24049426, -1, 17836669]'
      new.csv: '[24049426, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17836669, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19718812, -1, -1, -1, -1, -1]'
    partners__site_section_group_ids:
      old.csv: '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496]]'
      new.csv: '[[783644, 783650, 783652, 784102, 796273, 1223055, 1243315, 1262402, 1281009, 1281010, 1281011, 1297876, 1297947], null, null, null, null, null, null, null, null, null, null, null, [929388, 929392, 929393, 929394, 929395, 929447, 929452, 929454, 931976, 932050, 932269, 932579, 932580, 932581, 932584, 949503, 949504, 949505, 949506, 951038, 951046, 951164, 951165, 951166, 951167, 951168, 951169, 951170, 951173, 958104, 979406, 979415, 1038382, 1076721, 1082226, 1082228, 1082229, 1094795, 1105366, 1105389, 1105392, 1105413, 1120591, 1121790, 1162987, 1162988, 1163177, 1164935, 1199800, 1199801, 1248100, 1250445, 1250449, 1256496], null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, [534407, 581917, 581919, 581922, 581923, 581925, 581931, 587093, 665621, 720438, 753140, 782163, 782164, 782782, 789025, 791263, 801486, 801855, 801902, 801976, 802168, 805602, 858725, 858826, 860172, 860495, 861165, 877533, 916550, 920992, 920993, 964566, 1047609, 1077035, 1077154, 1083690, 1083691, 1083692, 1083693, 1083694, 1183944, 1193912, 1193980, 1194380, 1194383, 1195968, 1196600, 1196601, 1196602, 1196604, 1196732, 1196770, 1197476, 1197586, 1197589, 1197603, 1197604, 1203697, 1203699, 1216899, 1218276, 1235434, 1235586, 1235671, 1237227, 1239575, 1244247, 1247388, 1248362, 1261138, 1264552, 1301230], null, null, null, null, null]'
    partners__site_id:
      old.csv: '[null, null, 1094457]'
      new.csv: '[null, null, null, null, null, null, null, null, null, null, null, null, 1094457, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1212913, null, null, null, null, null]'
    partners__inventory_package_ids:
      old.csv: '[[151613, 372147, 432245, 433847, 687274], [], []]'
      new.csv: '[[151613, 372147, 432245, 433847, 687274], null, [121919, 127842, 148772, 163216, 164357, 164367, 164392, 164395, 164398, 166224, 166225, 167261, 167262, 167263, 167264, 167267, 167268, 167269, 167273, 167274, 167275, 167276, 167277, 167279, 167527, 167539, 167544, 172997, 183300, 183823, 213621, 225556, 225557, 231325, 235399, 235432, 235447, 235657, 236693, 237029, 237072, 237082, 237991, 239552, 239583, 242548, 243504, 244302, 245310, 245311, 247215, 247393, 247475, 247539, 247713, 248645, 249221], null, [336488, 349390, 368102, 393904, 488049, 488075, 488076], null, [96105, 96127, 96130, 96131, 96133, 96134, 96135, 96137, 105256, 110708, 119906, 130046, 149805, 152260, 157665, 174990, 206852, 268515, 270225, 275627, 282307, 346953], null, null, [121919, 127842, 148772, 163216, 164357, 164367, 164392, 164395, 164398, 166224, 166225, 167261, 167262, 167263, 167264, 167267, 167268, 167269, 167273, 167274, 167275, 167276, 167277, 167279, 167527, 167539, 167544, 172997, 183300, 183823, 213621, 225556, 225557, 231325, 235399, 235432, 235447, 235657, 236693, 237029, 237072, 237082, 237991, 239552, 239583, 242548, 243504, 244302, 245310, 245311, 247215, 247393, 247475, 247539, 247713, 248645, 249221], [96105, 96127, 96130, 96131, 96133, 96134, 96135, 96137, 105256, 110708, 119906, 130046, 149805, 152260, 157665, 174990, 206852, 268515, 270225, 275627, 282307, 346953], [121919, 127842, 148772, 164367, 164392, 167261, 167273, 183300, 213621, 225556, 225557], [116322, 149801, 185851, 213076, 244149, 311309, 328692, 330836, 368122, 372218, 459324, 569770, 614182, 651324], [108491, 108495, 108498, 108502, 111702, 112558, 112564, 112576, 112615, 112616, 112618, 112662, 112668, 112674, 112841, 113236, 113237, 113244, 113246, 113247, 113248, 113249, 114324, 115224, 115225, 115226, 118195, 125008, 125032, 134163, 139918, 152218, 158608, 158660, 169168, 180665, 197705, 198953, 198957, 205333, 210770, 210772, 210775, 210777, 227940, 234063, 258375, 258378, 258379, 258380, 288913, 330797, 499294, 562613, 670073, 672262, 672263], [108491, 108502, 111702, 112564, 112615, 112616, 112618, 112662, 112668, 112674, 112841, 113247, 113249, 114324, 115224, 115225, 115226, 125008, 125032, 205333, 210770, 210772, 227940, 258375, 258378, 258379, 258380, 288913, 330797, 562613, 670073, 672262, 672263], [108491, 108495, 108498, 108502, 111702, 112558, 112564, 112576, 112615, 112616, 112618, 112662, 112668, 112674, 112841, 113236, 113237, 113244, 113246, 113247, 113248, 113249, 114324, 115224, 115225, 115226, 118195, 125008, 125032, 134163, 139918, 152218, 158608, 158660, 169168, 180665, 197705, 198953, 198957, 205333, 210770, 210772, 210775, 210777, 227940, 234063, 258375, 258378, 258379, 258380, 288913, 330797, 499294, 562613, 670073, 672262, 672263], null, [336488, 349390, 368102, 376116, 488075, 488076], [333927, 455168], null, null, [96131, 96134, 96135, 96137, 119906, 152260, 157665, 174990, 206852, 282307, 346953], null, [108491, 108495, 108498, 108502, 111702, 112576, 112615, 112616, 112618, 113236, 113237, 113247, 113249, 114324, 115224, 115225, 115226, 118195, 125008, 125032, 134163, 139918, 152218, 158608, 205333, 210770, 210772, 227940, 258375, 258378, 258379, 258380, 288913, 330797, 499287, 562613, 670073, 672262, 672263], [108491, 108495, 108498, 108502, 111702, 112558, 112564, 112576, 112615, 112616, 112618, 112662, 112668, 112674, 112841, 113236, 113237, 113244, 113246, 113247, 113248, 113249, 114324, 115224, 115225, 115226, 118195, 125008, 125032, 134163, 139918, 152218, 158608, 158660, 180665, 197705, 198953, 198957, 205333, 205520, 210770, 210772, 210775, 210777, 227940, 234063, 258375, 258378, 258379, 258380, 288913, 330797, 499287, 562613, 670073, 672262, 672263], [108491, 108495, 108498, 108502, 111702, 112558, 112564, 112576, 112615, 112616, 112618, 112662, 112668, 112674, 112841, 113236, 113237, 113244, 113246, 113247, 113248, 113249, 114324, 115224, 115225, 115226, 118195, 125008, 125032, 134163, 139918, 152218, 158608, 158660, 180665, 197705, 198953, 198957, 205333, 205520, 210770, 210772, 210775, 210777, 227940, 234063, 258375, 258378, 258379, 258380, 288913, 330797, 499287, 562613, 670073, 672262, 672263], null, [132480, 199169, 230193, 230450, 469667, 481166, 550671], null, null, [240527, 250660, 269136, 285694, 332675, 335409, 339915, 340613, 399210, 399215, 401663, 423722, 438505, 444460, 461404, 521155, 526531, 526710, 562656, 584861, 591245, 658078, 672270], null, null, null, [232329, 386993, 387032, 424654, 450425, 450429, 672825, 684736, 684738], [232329, 386993, 387032, 424654, 450425, 450429, 672825, 684736, 684738]]'
    partners__supply_source:
      old.csv: '[1, 5, 0]'
      new.csv: '[1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]'
    partners__sales_channel:
      old.csv: '[5, 0, 3]'
      new.csv: '\\N'
    partners__inbound_order_id:
      old.csv: '[null, 327399, null]'
      new.csv: '[null, 405071, 546572, 327399, 428182, 550481, 547678, 550482, 327395, 390703, 232900, 268908, 382795, 4211, 4211, 4211, 612931, 390710, 317413, 452258, 534732, 651999, 350040, 4211, 4211, 4211, 184317, 190345, 225954, 592733, 184380, 482509, 482508, 573050, 504666, 504668]'
    partners__inbound_order_type:
      old.csv: '[null, MARKETPLACE_ORDER, null]'
      new.csv: '[null, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, EXCHANGE_ORDER, EXCHANGE_ORDER, EXCHANGE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, EXCHANGE_ORDER, EXCHANGE_ORDER, EXCHANGE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER, MARKETPLACE_ORDER]'
    partners__inbound_listing_id:
      old.csv: '[null, [344878], null]'
      new.csv: '\\N'
    partners__deal_awareability:
      old.csv: '[false, false, false]'
      new.csv: '\\N'
    partners__reseller_network_id:
      old.csv: '[525290, 525290, 516429]'
      new.csv: '\\N'
    partners__inbound_listing_ids:
      old.csv: '[null, null, null]'
      new.csv: '[null, [424707], [569511], [344878], [443343], [573334], [569620], [573331], [344863], [404943], [243767], [282745], [401571], [563617], [679435], [80656], [637205], [409039], [330839], [471854], [556807], [677570], [368145], [192926], [105638], [265464], [186106], [192541], [234008], [616832], [187255], [387315], [399248], [595961], [521158], [516788]]'
    partners__outbound_order_type:
      old.csv: '[MARKETPLACE_ORDER, null, null]'
      new.csv: '\\N'
    partners__supply_source_type:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__internal_deal_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__outbound_order_id:
      old.csv: '[327399, null, null]'
      new.csv: '\\N'
    partners__outbound_order_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__buyer_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__internal_seat_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__outbound_listing_id:
      old.csv: '[[344878], null, null]'
      new.csv: '\\N'
    partners__matched_inventory_package_ids:
      old.csv: '[[], null, null]'
      new.csv: '\\N'
    partners__global_currency_id:
      old.csv: '[62, 62, 62]'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

  
**Updated Analysis:**

- Transaction 1781177635874057052, Network 520311
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612190304\_197534&externalid=20260612\_190310\_00090\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612190304_197534&externalid=20260612_190310_00090_fnmf6)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612193513\_896480&externalid=20260612\_193551\_00102\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612193513_896480&externalid=20260612_193551_00102_fnmf6)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 263 / 263
  Columns compared : 32

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 263 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (32 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [FAIL] 15 column(s) differ between Hoover and Hoover++:

    partners__bit_flags
      OLD (Hoover)   : [10485760, 0] x141, [0] x26, [1152921504606851072] x22, [10485760, 32, 0] x15, \N x14, [10485760, 18014398509481984] x12, [2251799822073856] x10, [1152921504606846976] x9, [1152921504615235584, 1152923703630102528, 1152921504606846976, 1152923703630102528, 1152921504606846976, 1152921504606846976, 1152921504606846976] x9, [10485760, 18014398509482016, 0] x5
      NEW (Hoover++) : [10485760, 0] x141, [0] x26, [1152921504606851072] x22, [10485760, 32, 0] x15, \N x14, [10485760, 18014398509481984] x12, [2251799822073856] x10, [1152921504615235584, 1152923703630102528, 1152921504606846976, 1152923703630102528, 1152921642045800448, 1152921504606846976, 1152921504606846976] x9, [1152921504606846976] x9, [10485760, 18014398509482016, 0] x5

    partners__network_execution_ctx_index
      OLD (Hoover)   : [0, 4] x153, [0] x67, [0, 4, null] x20, \N x14, [0, 1, 2, 3, 4, 5, 6] x9
      NEW (Hoover++) : [0, 4] x153, \N x54, [0] x36, [0, 4, null] x20

    partners__sales_channel
      OLD (Hoover)   : [5, 2] x153, [2] x36, [0] x31, [5, 4, 4] x20, \N x14, [0, 0, 0, 0, 0, 0, 0] x9
      NEW (Hoover++) : [5, 2] x153, \N x54, [2] x36, [5, 4, 4] x20

    partners__deal_awareability
      OLD (Hoover)   : [false, false] x153, [false] x67, [false, true, true] x20, \N x14, [false, false, false, false, false, false, false] x9
      NEW (Hoover++) : [false, false] x153, \N x54, [false] x36, [false, true, true] x20

    partners__reseller_network_id
      OLD (Hoover)   : [144750, 144750] x153, [520311] x36, [null] x31, [144750, 512167, 512167] x15, \N x14, [null, null, null, null, null, null, null] x9, [144750, 512166, 512166] x5
      NEW (Hoover++) : [144750, 144750] x153, \N x54, [520311] x36, [144750, 512167, 512167] x15, [144750, 512166, 512166] x5

    partners__outbound_order_type
      OLD (Hoover)   : [CARRIAGE_ORDER, null] x153, [null] x67, [CARRIAGE_ORDER, PROGRAMMATIC_ORDER, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [CARRIAGE_ORDER, null] x153, \N x54, [null] x36, [CARRIAGE_ORDER, PROGRAMMATIC_ORDER, null] x20

    partners__supply_source_type
      OLD (Hoover)   : [null, null] x153, [null] x67, [null, null, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : \N x263

    partners__internal_deal_ids
      OLD (Hoover)   : [null, null] x153, [null] x67, [null, null, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : \N x263

    partners__outbound_order_id
      OLD (Hoover)   : [347195, null] x153, [null] x67, [347195, -1, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [347195, null] x153, \N x54, [null] x36, [347195, -1, null] x20

    partners__outbound_order_ids
      OLD (Hoover)   : [null, null] x153, [null] x67, [null, null, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [null, null] x153, \N x54, [null] x36, [null, null, null] x20

    partners__buyer_ids
      OLD (Hoover)   : [null, null] x153, [null] x67, [null, null, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : \N x263

    partners__internal_seat_ids
      OLD (Hoover)   : [null, null] x153, [null] x67, [null, null, null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : \N x263

    partners__outbound_listing_id
      OLD (Hoover)   : [[365211], null] x153, [null] x67, [[365211], [], null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [[365211], null] x153, \N x54, [null] x36, [[365211], null, null] x20

    partners__matched_inventory_package_ids
      OLD (Hoover)   : [[254564], null] x153, [null] x67, [[254564], [], null] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [[254564], null] x153, \N x54, [null] x36, [[254564], [], null] x20

    partners__global_currency_id
      OLD (Hoover)   : [62, 44] x153, [62] x36, [null] x31, [62, 44, 62] x20, \N x14, [null, null, null, null, null, null, null] x9
      NEW (Hoover++) : [62, 44] x153, \N x54, [62] x36, [62, 44, 62] x20


── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - partners__inventory_package_ids

── RESULT ────────────────────────────────────────────────────────────────
  [FAIL] REVIEW REQUIRED — real differences detected (see section [3]).

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- Hoover has 34 columns, Hoover++ 33. partners\_\_inbound\_listing\_ids exists only in Hoover;
    - The bigger thing is **Hoover++ is dropping network-execution-context data**. On partners\_\_network\_execution\_ctx\_index, **Hoover has 249 rows with real context and Hoover++ only 209 , so  the 40 rows do not have context.** An Example: there are 9 rows where Hoover has the full 7-slot context \[0,1,2,3,4,5,6\], and in Hoover++ those are blanked out to \\N. When that context drops, the reseller IDs, sales channels, order info are all empty  on those same rows.
    - **There's also a flag bit difference**: in partners\_\_bit\_flags, that same 7-element array has one value off by exactly 2^37 (bit 37) but Hoover ...606846976 vs Hoover++ ...642045800448.

  There are a few columns that look different (supply\_source\_type, internal\_deal\_ids, buyer\_ids, internal\_seat\_ids) are just \[null,null\] in Hoover vs \\N in Hoover++ but no actual data loss either way, so I'm not counting those.  

1. **Network 535262**

request\_\_transaction\_id = 1780079397633065777

**Step 1 – Hoover (mrm\_log\_flat.default) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071439\_292233&externalid=20260531\_071444\_00017\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071439_292233&externalid=20260531_071444_00017_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 535262**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071452\_510881&externalid=20260531\_071525\_00020\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071452_510881&externalid=20260531_071525_00020_k22np)

Summary: Hoover has 5 rows and Hoover++ has 0 rows.  

- **Updated Analysis:**
- Transaction 1781180575132557551, Network 535262
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612201318\_592775&externalid=20260612\_201322\_00132\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612201318_592775&externalid=20260612_201322_00132_fnmf6)
- Hoover++:  [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612212635\_893907&externalid=20260612\_212709\_00152\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612212635_893907&externalid=20260612_212709_00152_fnmf6)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 12 / 12
  Columns compared : 32

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 12 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (32 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [FAIL] 14 column(s) differ between Hoover and Hoover++:

    partners__network_execution_ctx_index
      OLD (Hoover)   : [0, 1, null] x7, [0, 1, 2, 3] x5
      NEW (Hoover++) : [0, 1, null] x7, \N x5

    partners__sales_channel
      OLD (Hoover)   : [5, 4, 4] x7, [0, 0, 0, 0] x5
      NEW (Hoover++) : [5, 4, 4] x7, \N x5

    partners__deal_awareability
      OLD (Hoover)   : [false, true, true] x7, [false, false, false, false] x5
      NEW (Hoover++) : [false, true, true] x7, \N x5

    partners__reseller_network_id
      OLD (Hoover)   : [524565, 518308, 518308] x7, [null, null, null, null] x5
      NEW (Hoover++) : [524565, 518308, 518308] x7, \N x5

    partners__outbound_order_type
      OLD (Hoover)   : [MARKETPLACE_ORDER, PROGRAMMATIC_ORDER, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : [MARKETPLACE_ORDER, PROGRAMMATIC_ORDER, null] x7, \N x5

    partners__supply_source_type
      OLD (Hoover)   : [null, null, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : \N x12

    partners__internal_deal_ids
      OLD (Hoover)   : [null, null, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : \N x12

    partners__outbound_order_id
      OLD (Hoover)   : [308275, -1, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : [308275, -1, null] x7, \N x5

    partners__outbound_order_ids
      OLD (Hoover)   : [null, null, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : [null, null, null] x7, \N x5

    partners__buyer_ids
      OLD (Hoover)   : [null, null, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : \N x12

    partners__internal_seat_ids
      OLD (Hoover)   : [null, null, null] x7, [null, null, null, null] x5
      NEW (Hoover++) : \N x12

    partners__outbound_listing_id
      OLD (Hoover)   : [[323368], [], null] x7, [null, null, null, null] x5
      NEW (Hoover++) : [[323368], null, null] x7, \N x5

    partners__matched_inventory_package_ids
      OLD (Hoover)   : [[], [], null] x7, [null, null, null, null] x5
      NEW (Hoover++) : [[], [], null] x7, \N x5

    partners__global_currency_id
      OLD (Hoover)   : [62, 49, 62] x7, [null, null, null, null] x5
      NEW (Hoover++) : [62, 49, 62] x7, \N x5


── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - partners__inventory_package_ids

── RESULT ────────────────────────────────────────────────────────────────
  [FAIL] REVIEW REQUIRED 

========================================================================
  END OF REPORT
========================================================================
```

  
**Summary:**

- **Hoover vs Hoover++ Partners Entity (txn **`1781180575132557551`**, network 535262) **
- 14 columns flagged, but all differences fall on the same 5 rows (the `x5` group); the 7 remaining rows are identical on both sides. Substantive fields not flagged (`partners__bit_flags`, `entity_source`, `network_id`, `content_owner_network_id`) match exactly.**The only genuine non-null value difference:** `partners__network_execution_ctx_index`, Hoover holds `[0,1,2,3]` on those 5 rows, Hoover++ holds `\N`.
- **Correlated columns** (`sales_channel`, `deal_awareability`, `reseller_network_id`, `outbound_order_type/id/ids`, `supply_source_type`, `internal_deal_ids`, `buyer_ids`, `internal_seat_ids`, `outbound_listing_id`, `matched_inventory_package_ids`, `global_currency_id`) differ only on those same 5 rows; in Hoover they were null-arrays / zeros / falses, so they are empty-vs-empty.
- **Suppressed (representation only, not a real diff):** `partners__inventory_package_ids` (`\N` vs `0` vs `[]` vs `null`).
- As per team, the  `network_execution_ctx_index` is redundant on slot impression callbacks (already set on the parent slot entity), so its absence in Hoover++ has no reporting impact. Documented as an expected difference.  

1. **Network 384777**

`request__transaction_id = 1780076927707289550`

**Step 1 – Hoover (mrm\_log\_flat.default) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071459\_722212&externalid=20260531\_071504\_00018\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071459_722212&externalid=20260531_071504_00018_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 384777**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071508\_228241&externalid=20260531\_071541\_00022\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071508_228241&externalid=20260531_071541_00022_k22np)

Summary: Difference of 3 rows

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 24
  Rows  B  : 21
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ❌ Row count MISMATCH:  A=24  B=21  diff=3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────

  ⚠️  1 key(s) have multiple rows (fan-out detected).
     21 row(s) are in old.csv but have NO matching row in new.csv.
     18 row(s) are in new.csv but have NO matching row in old.csv.

  [key=('1780076927707289550',)]  old.csv: 24 rows  |  new.csv: 21 rows
    Rows in old.csv with NO match in new.csv:
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 0, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_index': '[0, 2, 3]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701]', 'partners__bit_flags': '[0]', 'partners__entity_source': '[slot]', 'partners__network_execution_ctx_index': '[0]', 'partners__network_execution_ctx_flags': '[null]', 'partners__content_owner_network_id': '[191701]', 'partners__asset_id': '[470541941]', 'partners__asset_group_id': '[null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929]]', 'partners__series_id': '[1184637931]', 'partners__site_section_id': '[23964983]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 0, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_index': '[0, 2, 3]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701]', 'partners__bit_flags': '[0]', 'partners__entity_source': '[slot]', 'partners__network_execution_ctx_index': '[0]', 'partners__network_execution_ctx_flags': '[null]', 'partners__content_owner_network_id': '[191701]', 'partners__asset_id': '[470541941]', 'partners__asset_group_id': '[null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929]]', 'partners__series_id': '[1184637931]', 'partners__site_section_id': '[23964983]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 0, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_index': '[0, 2, 3]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701]', 'partners__bit_flags': '[0]', 'partners__entity_source': '[slot]', 'partners__network_execution_ctx_index': '[0]', 'partners__network_execution_ctx_flags': '[null]', 'partners__content_owner_network_id': '[191701]', 'partners__asset_id': '[470541941]', 'partners__asset_group_id': '[null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929]]', 'partners__series_id': '[1184637931]', 'partners__site_section_id': '[23964983]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
    Rows in new.csv with NO match in old.csv:
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 384777]', 'partners__bit_flags': '[10485760, 0, 1]', 'partners__entity_source': '[ad, ad, ad]', 'partners__network_execution_ctx_index': '[0, 2, 1]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 191701]', 'partners__asset_id': '[470541941, 454096630, 470543010]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]', 'partners__series_id': '[1184637931, 1216787026, 1184722967]', 'partners__site_section_id': '[23964983, 1819063, 1819063]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 137438953472, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]', 'partners__site_section_group_ids': '[[672272, 764545, 764546, 764547, 771583, 771584, 771585, 771586], [581931, 613599, 787818, 787823, 917523], null]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 137438953472, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]', 'partners__site_section_group_ids': '[[672272, 764545, 764546, 764547, 771583, 771584, 771585, 771586], [581931, 613599, 787818, 787823, 917523], null]'}
      {'request__transaction_id': '1780076927707289550', 'partners__network_id': '[191701, 384777, 524565]', 'partners__bit_flags': '[8388608, 137438953472, 0]', 'partners__entity_source': '[slot, slot, slot]', 'partners__network_execution_ctx_flags': '[null, null, null]', 'partners__content_owner_network_id': '[191701, 191701, 384777]', 'partners__asset_id': '[470541941, 454096630, -1]', 'partners__asset_group_id': '[null, null, null]', 'partners__asset_group_ids': '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], null]', 'partners__series_id': '[1184637931, 1216787026, null]', 'partners__site_section_id': '[23964983, 1819063, -1]', 'partners__site_section_group_ids': '[[672272, 764545, 764546, 764547, 771583, 771584, 771585, 771586], [581931, 613599, 787818, 787823, 917523], null]'}

── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  ✅ No known-difference columns triggered.

  ❌ 1 row(s) have differences:

  Column diff summary (sorted by frequency):
    partners__network_id                                         1 row(s)
    partners__bit_flags                                          1 row(s)
    partners__entity_source                                      1 row(s)
    partners__network_execution_ctx_index                        1 row(s)
    partners__network_execution_ctx_flags                        1 row(s)
    partners__content_owner_network_id                           1 row(s)
    partners__asset_id                                           1 row(s)
    partners__asset_group_id                                     1 row(s)
    partners__asset_group_ids                                    1 row(s)
    partners__series_id                                          1 row(s)
    partners__site_section_id                                    1 row(s)
    partners__site_section_group_ids                             1 row(s)
    partners__site_id                                            1 row(s)
    partners__inventory_package_ids                              1 row(s)
    partners__supply_source                                      1 row(s)
    partners__sales_channel                                      1 row(s)
    partners__inbound_order_id                                   1 row(s)
    partners__inbound_order_type                                 1 row(s)
    partners__inbound_listing_id                                 1 row(s)
    partners__deal_awareability                                  1 row(s)
    partners__reseller_network_id                                1 row(s)
    partners__inbound_listing_ids                                1 row(s)
    partners__outbound_order_type                                1 row(s)
    partners__supply_source_type                                 1 row(s)
    partners__internal_deal_ids                                  1 row(s)
    partners__outbound_order_id                                  1 row(s)
    partners__outbound_order_ids                                 1 row(s)
    partners__buyer_ids                                          1 row(s)
    partners__internal_seat_ids                                  1 row(s)
    partners__outbound_listing_id                                1 row(s)
    partners__matched_inventory_package_ids                      1 row(s)
    partners__global_currency_id                                 1 row(s)

  Detailed diffs:

  [key=('1780076927707289550',)]
    partners__network_id:
      old.csv: '[191701, 384777, 384777]'
      new.csv: '\\N'
    partners__bit_flags:
      old.csv: '[10485760, 0, 1]'
      new.csv: '\\N'
    partners__entity_source:
      old.csv: '[ad, ad, ad]'
      new.csv: '\\N'
    partners__network_execution_ctx_index:
      old.csv: '[0, 2, 1]'
      new.csv: '\\N'
    partners__network_execution_ctx_flags:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__content_owner_network_id:
      old.csv: '[191701, 191701, 191701]'
      new.csv: '\\N'
    partners__asset_id:
      old.csv: '[470541941, 454096630, 470543010]'
      new.csv: '\\N'
    partners__asset_group_id:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__asset_group_ids:
      old.csv: '[[15461627, 15668814, 15668832, 15885185, 15885188, 15885202, 16280273, 16280328, 16830959, 16831395, 16832974, 16834475, 16838340, 16848476, 16848477, 16848478, 16848479, 16848480, 16848481, 16848483, 16852408, 16877555, 19248827, 19268653, 22870640, 29786084, 512660207, 512660686, 512666022, 512666544, 898409195, 1604689928, 1604689929], [8063744, 9350144, 9366210, 10488129, 10488132, 10488133, 10558643, 10558644, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1564308170], [8063738, 8063741, 8063744, 8212774, 8220077, 8220078, 8220079, 8220082, 8220084, 8220085, 8525045, 9350144, 9366210, 9504297, 9504357, 9504376, 9651396, 9651397, 10488129, 10488132, 10488133, 10558643, 10558644, 11336241, 11753604, 11753605, 11991826, 11991828, 12302360, 12302365, 12302366, 12302367, 13561978, 13565061, 13565065, 13567114, 13567333, 13567381, 13570246, 13570254, 13570464, 13699478, 13722160, 13722173, 14974048, 14974113, 14974129, 15050518, 15056282, 15077919, 15112788, 15491476, 16229461, 16229571, 16848694, 16848704, 16848714, 16848724, 16848734, 16848744, 16848764, 17360130, 18091798, 18092019, 18368144, 19252407, 19514829, 19515934, 19605391, 19702622, 19703764, 19704622, 19705183, 19987044, 20922201, 20986626, 21106365, 21121180, 21121222, 21121321, 21121445, 21121587, 21122903, 21190562, 21399730, 21400139, 21543259, 21588674, 21589486, 21726955, 21888034, 22029829, 22032767, 22235482, 22237159, 22237428, 22237727, 22237908, 22238292, 22238653, 22238985, 22275051, 22275152, 22276066, 22291114, 22412936, 22413336, 22413908, 22600384, 22602723, 23136022, 23166081, 23183269, 23184866, 23184966, 23185476, 23185758, 23185827, 23186259, 23187808, 23256106, 23323531, 23334360, 23334853, 23694378, 27831829, 27832562, 27833057, 27833290, 27833571, 27834504, 27834895, 27835034, 27835808, 27836252, 27836574, 27912148, 27912367, 27912650, 27914772, 27917570, 27917673, 27919603, 27919813, 27920349, 27921470, 28031599, 28110258, 29284847, 29377864, 30219376, 30277649, 30278034, 30278347, 30278548, 30278870, 30279208, 31851722, 31928125, 31928267, 32050380, 32053067, 32053904, 32060138, 32082747, 32088732, 32146179, 32927694, 32928378, 32929174, 33016939, 33017672, 37945417, 48142132, 63338403, 71406956, 127450131, 128239095, 152369527, 152372022, 152379027, 152383065, 152388649, 164786433, 164787865, 164790238, 164790992, 164792661, 164805415, 164806873, 164808168, 214644033, 289888205, 289895439, 289898586, 289904113, 289907250, 290271588, 355865461, 401206142, 404542502, 414929514, 414940984, 414942232, 414948664, 414956884, 415075296, 415121922, 415590681, 415593971, 415597957, 415678771, 415685655, 415772792, 415825335, 415838794, 415843815, 443114964, 466210867, 468238441, 468244396, 468259745, 468282206, 468284287, 468297534, 468303990, 468312418, 468315314, 468320061, 468331715, 877733953, 942332737, 944328340, 975090600, 975157472, 975927852, 980332185, 980352399, 981123388, 981902992, 982267872, 985974550, 986119340, 986429876, 986614430, 989282061, 989404510, 990060911, 991142595, 991155755, 991270536, 992509812, 1069800998, 1069807273, 1093634106, 1106016346, 1146989479, 1149055772, 1149521753, 1149524104, 1150092083, 1152560100, 1160493104, 1171411883, 1171423252, 1175495965, 1225506126, 1261661120, 1288786235, 1518038486, 1564308170]]'
      new.csv: '\\N'
    partners__series_id:
      old.csv: '[1184637931, 1216787026, 1184722967]'
      new.csv: '\\N'
    partners__site_section_id:
      old.csv: '[23964983, 1819063, 1819063]'
      new.csv: '\\N'
    partners__site_section_group_ids:
      old.csv: '[[672272, 764545, 764546, 764547, 771583, 771584, 771585, 771586], [581931, 613599, 787818, 787823, 917523], [581931, 613599, 787818, 787823, 917523]]'
      new.csv: '\\N'
    partners__site_id:
      old.csv: '[null, 621717, 621717]'
      new.csv: '\\N'
    partners__inventory_package_ids:
      old.csv: '[[232125, 326983, 346750, 416285, 422700], [250660, 269136, 285694, 330788, 330795, 335409, 340613, 372204, 444460, 526859, 562656, 584861, 672270], []]'
      new.csv: '\\N'
    partners__supply_source:
      old.csv: '[1, 5, 0]'
      new.csv: '\\N'
    partners__sales_channel:
      old.csv: '[5, 2, 3]'
      new.csv: '\\N'
    partners__inbound_order_id:
      old.csv: '[null, 396907, null]'
      new.csv: '\\N'
    partners__inbound_order_type:
      old.csv: '[null, CARRIAGE_ORDER, null]'
      new.csv: '\\N'
    partners__inbound_listing_id:
      old.csv: '[null, [416308], null]'
      new.csv: '\\N'
    partners__deal_awareability:
      old.csv: '[false, false, false]'
      new.csv: '\\N'
    partners__reseller_network_id:
      old.csv: '[384777, 384777, 191701]'
      new.csv: '\\N'
    partners__inbound_listing_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__outbound_order_type:
      old.csv: '[CARRIAGE_ORDER, null, null]'
      new.csv: '\\N'
    partners__supply_source_type:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__internal_deal_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__outbound_order_id:
      old.csv: '[396907, null, null]'
      new.csv: '\\N'
    partners__outbound_order_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__buyer_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__internal_seat_ids:
      old.csv: '[null, null, null]'
      new.csv: '\\N'
    partners__outbound_listing_id:
      old.csv: '[[416308], null, null]'
      new.csv: '\\N'
    partners__matched_inventory_package_ids:
      old.csv: '[[416285], null, null]'
      new.csv: '\\N'
    partners__global_currency_id:
      old.csv: '[62, 62, 62]'
      new.csv: '\\N'

========================================================================
  END OF REPORT
========================================================================
```

**Updated Analysis:**

- Transaction `1781178373156217993`, Network 384777
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612214330\_861383&externalid=20260612\_214334\_00154\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612214330_861383&externalid=20260612_214334_00154_fnmf6)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612215040\_654113&externalid=20260612\_215107\_00157\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612215040_654113&externalid=20260612_215107_00157_fnmf6)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 80 / 80
  Columns compared : 32

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 80 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (32 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [FAIL] 15 column(s) differ between Hoover and Hoover++:

    partners__bit_flags
      OLD (Hoover)   : [10485760, 0, 0] x40, [2251799822073856, 0] x22, \N x5, [2251799824171008, 2097152, 18014398509481984, 1] x5, [1152921504615235584, 1152921504606846976, 1152921504640401408, 1152921504640401408, 1152921504640401408, 1152921504606846976, 1152921504606846976] x4, [1152921504606846976] x4
      NEW (Hoover++) : [10485760, 0, 0] x40, [2251799822073856, 0] x22, [2251799824171008, 2097152, 18014398509481984, 1] x5, \N x5, [1152921504615235584, 1152921504606846976, 1152921504640401408, 1152921504640401408, 1152921504640401408, 1152921504606846976, 1152921642045800448] x4, [1152921504606846976] x4

    partners__network_execution_ctx_index
      OLD (Hoover)   : [0, 7, 1] x40, [0, 1] x22, \N x5, [0, 2, 6, 1] x5, [0, 2, 3, 4, 5, 6, 7] x4, [0] x4
      NEW (Hoover++) : [0, 7, 1] x40, [0, 1] x22, \N x13, [0, 2, 6, 1] x5

    partners__sales_channel
      OLD (Hoover)   : [5, 2, 3] x40, [2, 3] x22, \N x5, [5, 5, 2, 3] x5, [0, 0, 0, 0, 0, 0, 0] x4, [0] x4
      NEW (Hoover++) : [5, 2, 3] x40, [2, 3] x22, \N x13, [5, 5, 2, 3] x5

    partners__deal_awareability
      OLD (Hoover)   : [false, false, false] x40, [false, false] x22, \N x5, [false, false, false, false] x5, [false, false, false, false, false, false, false] x4, [false] x4
      NEW (Hoover++) : [false, false, false] x40, [false, false] x22, \N x13, [false, false, false, false] x5

    partners__reseller_network_id
      OLD (Hoover)   : [535279, 535279, 169843] x40, [169843, 169843] x22, \N x5, [520024, 384777, 384777, 169843] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [535279, 535279, 169843] x40, [169843, 169843] x22, \N x13, [520024, 384777, 384777, 169843] x5

    partners__outbound_order_type
      OLD (Hoover)   : [CARRIAGE_ORDER, null, null] x40, [null, null] x22, \N x5, [MARKETPLACE_ORDER, MARKETPLACE_ORDER, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [CARRIAGE_ORDER, null, null] x40, [null, null] x22, \N x13, [MARKETPLACE_ORDER, MARKETPLACE_ORDER, null, null] x5

    partners__supply_source_type
      OLD (Hoover)   : [null, null, null] x40, [null, null] x22, \N x5, [null, null, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : \N x80

    partners__internal_deal_ids
      OLD (Hoover)   : [null, null, null] x40, [null, null] x22, \N x5, [null, null, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : \N x80

    partners__outbound_order_id
      OLD (Hoover)   : [405865, null, null] x40, [null, null] x22, \N x5, [374416, 374421, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [405865, null, null] x40, [null, null] x22, \N x13, [374416, 374421, null, null] x5

    partners__outbound_order_ids
      OLD (Hoover)   : [null, null, null] x40, [null, null] x22, \N x5, [null, null, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [null, null, null] x40, [null, null] x22, \N x13, [null, null, null, null] x5

    partners__buyer_ids
      OLD (Hoover)   : [null, null, null] x40, [null, null] x22, \N x5, [null, null, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : \N x80

    partners__internal_seat_ids
      OLD (Hoover)   : [null, null, null] x40, [null, null] x22, \N x5, [null, null, null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : \N x80

    partners__outbound_listing_id
      OLD (Hoover)   : [[425539], null, null] x40, [null, null] x22, \N x5, [[390826], [393057], null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [[425539], null, null] x40, [null, null] x22, \N x13, [[390826], [393057], null, null] x5

    partners__matched_inventory_package_ids
      OLD (Hoover)   : [[425535], null, null] x40, [null, null] x22, \N x5, [[196099], [], null, null] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [[425535], null, null] x40, [null, null] x22, \N x13, [[196099], [], null, null] x5

    partners__global_currency_id
      OLD (Hoover)   : [62, 62, 62] x40, [62, 62] x22, \N x5, [62, 62, 62, 62] x5, [null, null, null, null, null, null, null] x4, [null] x4
      NEW (Hoover++) : [62, 62, 62] x40, [62, 62] x22, \N x13, [62, 62, 62, 62] x5


── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - partners__inventory_package_ids

── RESULT ────────────────────────────────────────────────────────────────
  [FAIL] REVIEW REQUIRED.

========================================================================
  END OF REPORT
========================================================================
```

**Summary:**

- 15 columns flagged; all differences fall on the slot-sourced rows, the ad-sourced rows (`[0,7,1] x40`, `[0,1] x22`, `[0,2,6,1] x5`) match exactly on both sides.
    1. `partners__network_execution_ctx_index`: 8 slot rows lose context, the 4 rows `[0,2,3,4,5,6,7]` and 4 rows `[0]` become `\N` (so `\N` goes 5→13). Known/expected difference confirmed by the team: the index is redundant on slot impression callbacks since it's already set on the slot entity the impression belongs to, therefore to be documented in the wiki of known differences.
    2. The 13 correlated columns (`sales_channel`, `deal_awareability`, `reseller_network_id`, `outbound_order_type/id/ids`, `supply_source_type`, `internal_deal_ids`, `buyer_ids`, `internal_seat_ids`, `outbound_listing_id`, `matched_inventory_package_ids`, `global_currency_id`) empty out on those same 8 rows; empty-vs-empty in Hoover anyway.
    3. `partners__bit_flags`: on the 7-element array (`x4` rows) the last element differs, Hoover `2^60` (`BIT_FLAG_CONSTRAINED`) vs Hoover++ `2^60+2^37` (adds `BIT_FLAG_NETWORK_IS_CAMPAIGN_MANAGER_DEAL_BUYER`). **(Needs Review and confirmation from team) **  
** Updated and resolved, tracked here with pr:**[Event Level (Backward Compatible Views)](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views)


1. **Network 169843**

`request__transaction_id = 1780079174184480780`

**Step 1 – Hoover (mrm\_log\_flat.default) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071518\_012310&externalid=20260531\_071522\_00019\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071518_012310&externalid=20260531_071522_00019_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 169843**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071526\_733171&externalid=20260531\_071602\_00023\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071526_733171&externalid=20260531_071602_00023_k22np)

Summary: No real differences found 

```
Reading old.csv …
Reading new.csv …
Auto-selecting key-based matching on 'request__transaction_id' (use --key to override) …
========================================================================
  EVENT-LEVEL CSV COMPARISON REPORT
========================================================================
  Source A : old.csv
  Source B : new.csv
  Rows  A  : 3
  Rows  B  : 3
  Columns A: 33
  Columns B: 33

── [1] ROW COUNT CHECK ─────────────────────────────────────────────────
  ✅ Row counts match: 3

── [2] COLUMN HEADER CHECK ────────────────────────────────────────────
  ✅ Column headers identical (33 columns)

── [3] ROW DIFFS (matched by key: ['request__transaction_id']) ───────────────────────────
  ✅ All keys match between both files — no missing or duplicate rows.
── [K] KNOWN DIFFERENCES (suppressed) ─────────────────────────────────
  Global equivalence groups (apply to all columns automatically):
    ['', '0', '\\N', '\\n', 'false', 'none', 'null']
    ['', '[]', '\\N', '\\n', 'none', 'null', '{}']

  Suppressed diffs by column (semantically equivalent values):

    partners__network_execution_ctx_index                        1 row(s)
    partners__sales_channel                                      1 row(s)
    partners__inbound_listing_id                                 1 row(s)
    partners__deal_awareability                                  1 row(s)
    partners__reseller_network_id                                1 row(s)
    partners__outbound_order_type                                1 row(s)
    partners__supply_source_type                                 1 row(s)
    partners__internal_deal_ids                                  1 row(s)
    partners__outbound_order_id                                  1 row(s)
    partners__outbound_order_ids                                 1 row(s)
    partners__buyer_ids                                          1 row(s)
    partners__internal_seat_ids                                  1 row(s)
    partners__outbound_listing_id                                1 row(s)
    partners__matched_inventory_package_ids                      1 row(s)
    partners__global_currency_id                                 1 row(s)

  ✅ No field-level differences found!

========================================================================
  END OF REPORT
========================================================================
```

1. **Network 532076**

request\_\_transaction\_id = 1780078300226561405

**Step 1 – Hoover (mrm\_log\_flat.default) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071534\_775443&externalid=20260531\_071537\_00021\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071534_775443&externalid=20260531_071537_00021_k22np)

**Step 2 – Hoover++ (etl.public\_test1) for 532076**

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260531071543\_112203&externalid=20260531\_071610\_00024\_k22np](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260531071543_112203&externalid=20260531_071610_00024_k22np)

Summary: Hoover has 4 rows and Hoover++ has 0 rows.

**Updated Analysis: **

- Transaction 1780078300226561405, Network 532076
- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612222628\_039507&externalid=20260612\_222631\_00165\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612222628_039507&externalid=20260612_222631_00165_fnmf6)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612222718\_641465&externalid=20260612\_222750\_00166\_fnmf6](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612222718_641465&externalid=20260612_222750_00166_fnmf6)

```
========================================================================
  HOOVER vs HOOVER++ REPORT
========================================================================
  Source A (OLD / Hoover)    : hoover.csv
  Source B (NEW / Hoover++)  : hooverpp.csv
  Rows  A / B      : 24 / 24
  Columns compared : 32

── [1] ROW COUNT ─────────────────────────────────────────────────────────
  [OK] Row counts match: 24 rows in each file.

── [2] COLUMN HEADERS ────────────────────────────────────────────────────
  [OK] Column headers identical (32 columns).

── [3] FIELD-LEVEL COMPARISON ────────────────────────────────────────────
  [FAIL] 14 column(s) differ between Hoover and Hoover++:

    partners__network_execution_ctx_index
      OLD (Hoover)   : [0, 6, 22] x20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49] x4
      NEW (Hoover++) : [0, 6, 22] x20, \N x4

    partners__sales_channel
      OLD (Hoover)   : [5, 5, 2] x20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] x4
      NEW (Hoover++) : [5, 5, 2] x20, \N x4

    partners__deal_awareability
      OLD (Hoover)   : [false, false, false] x20, [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false] x4
      NEW (Hoover++) : [false, false, false] x20, \N x4

    partners__reseller_network_id
      OLD (Hoover)   : [520024, 384777, 384777] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [520024, 384777, 384777] x20, \N x4

    partners__outbound_order_type
      OLD (Hoover)   : [MARKETPLACE_ORDER, MARKETPLACE_ORDER, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [MARKETPLACE_ORDER, MARKETPLACE_ORDER, null] x20, \N x4

    partners__supply_source_type
      OLD (Hoover)   : [null, null, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : \N x24

    partners__internal_deal_ids
      OLD (Hoover)   : [null, null, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : \N x24

    partners__outbound_order_id
      OLD (Hoover)   : [563217, 247719, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [563217, 247719, null] x20, \N x4

    partners__outbound_order_ids
      OLD (Hoover)   : [null, null, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [null, null, null] x20, \N x4

    partners__buyer_ids
      OLD (Hoover)   : [null, null, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : \N x24

    partners__internal_seat_ids
      OLD (Hoover)   : [null, null, null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : \N x24

    partners__outbound_listing_id
      OLD (Hoover)   : [[579207], [259723], null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [[579207], [259723], null] x20, \N x4

    partners__matched_inventory_package_ids
      OLD (Hoover)   : [[464961], [], null] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [[464961], [], null] x20, \N x4

    partners__global_currency_id
      OLD (Hoover)   : [62, 62, 62] x20, [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null] x4
      NEW (Hoover++) : [62, 62, 62] x20, \N x4


── [K] SUPPRESSED DIFFERENCES (semantically equivalent) ─────────────────
  These columns differ only by null/zero/empty representation (\N vs 0 vs [] vs null)
  and are treated as equivalent — not real differences:
    - partners__inventory_package_ids

── RESULT ────────────────────────────────────────────────────────────────
  [FAIL] REVIEW REQUIRED — real differences detected (see section [3]).

========================================================================
  END OF REPORT
========================================================================
```


- **Summary:** 14 columns flagged, all on the same 4 rows, the 20 ad-sourced rows (`[0,6,22]`) match exactly on both sides.
    1. `partners__network_execution_ctx_index`: the 4 slot rows where Hoover carries a full 50-slot context `[0,1,…,49]` become `\N` in Hoover++ is a  known/expected difference confirmed by the team: the index is redundant on slot impression callbacks since it's already set on the slot entity the impression belongs to, and shall be documented in the known differences wiki.
    2. The 13 correlated columns (`sales_channel`, `deal_awareability`, `reseller_network_id`, `outbound_order_type/id/ids`, `supply_source_type`, `internal_deal_ids`, `buyer_ids`, `internal_seat_ids`, `outbound_listing_id`, `matched_inventory_package_ids`, `global_currency_id`) empty out on those same 4 rows, they are null-arrays/zeros/falses in Hoover.   

### Aggregated Validations:

#### **Ack Entity:**

##### ack\_\_event\_type:

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604131936\_815618&externalid=20260604\_131946\_00021\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604131936_815618&externalid=20260604_131946_00021_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604131925\_478876&externalid=20260604\_132044\_00008\_bxmrg](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604131925_478876&externalid=20260604_132044_00008_bxmrg)

Summary: Difference of count for ack\_\_event\_type ‘e' and 'i’.

|  |  |  |  |
| --- | --- | --- | --- |
| **line** | **ack\_\_event\_type** | **Hoover count** | **Hoover++ count** |
| 1 | c | 50 | 50 |
| 2 | e | 17575 | 17585 |
| 3 | i | 467934 | 882893 |
| 4 | n | 382 | 382 |
| 5 | s | 3248 | 3248 |

##### ack\_\_creative\_rendition\_id:

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604131951\_077096&externalid=20260604\_132011\_00022\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604131951_077096&externalid=20260604_132011_00022_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604132003\_787515&externalid=20260604\_132106\_00024\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604132003_787515&externalid=20260604_132106_00024_bjd9w)

Summary: Difference of 1 records b/w Hoover and Hoover++. As output has 10,000+ records, output has not been attached. Queries above.  
  
**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614212357\_365991&externalid=20260614\_212401\_00020\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614212357_365991&externalid=20260614_212401_00020_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614214755\_765679&externalid=20260614\_214821\_00022\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614214755_765679&externalid=20260614_214821_00022_q5d66)  
  
**Summary:**`c` (101), `n` (433), and `s` (5,759) match exactly between Hoover and Hoover++.
- `i` **(impression) has a critical mismatch: Hoover 769,751 vs Hoover++ 2,365,975.** **Hoover++ returns \~3x more impression events (diff = +1,596,224).**
- `e` **(error) has a minor mismatch: Hoover 19,267 vs Hoover++ 19,280 (diff = +13).**
- Queries were re-run using `ack__timestamp` instead of `request__timestamp` to rule out batch-splitting as the cause, the `i` discrepancy persists and is larger than the original run.   

#### Request Entity:

#### request\_\_context\_\_network\_id:

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604132018\_315367&externalid=20260604\_132054\_00023\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604132018_315367&externalid=20260604_132054_00023_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604132121\_918321&externalid=20260604\_132217\_00025\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604132121_918321&externalid=20260604_132217_00025_bjd9w)

Summary: Difference of records for 39 networks.

**Updated Analysis:** Counts are matching between Hoover and Hoover++  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612133600\_983344&externalid=20260612\_133952\_00000\_ukb6k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612133600_983344&externalid=20260612_133952_00000_ukb6k)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612133233\_424483&externalid=20260612\_133322\_00001\_isfdw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612133233_424483&externalid=20260612_133322_00001_isfdw)

#### request\_\_context\_\_standard\_endpoint\_id:

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604132308\_663496&externalid=20260604\_132312\_00027\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604132308_663496&externalid=20260604_132312_00027_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604132348\_325874&externalid=20260604\_132450\_00029\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604132348_325874&externalid=20260604_132450_00029_bjd9w)

Summary: Difference of count between Hoover and Hoover++.  
**Updated Analysis: **Difference of count between Hoover and Hoover++ for standard endpoint id 804 and 'null'.  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612134944\_789148&externalid=20260612\_134948\_00026\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612134944_789148&externalid=20260612_134948_00026_r4cjx)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612134939\_378555&externalid=20260612\_135009\_00027\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612134939_378555&externalid=20260612_135009_00027_r4cjx)

#### **Visitor Entity:**

##### **visitor\_\_device\_type**

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604141905\_156932&externalid=20260604\_141909\_00053\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604141905_156932&externalid=20260604_141909_00053_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604141838\_990081&externalid=20260604\_141956\_00006\_x2h44](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604141838_990081&externalid=20260604_141956_00006_x2h44)

Summary: Difference of visitor\_\_device\_type and their record count.  
**Updated Analysis:**Difference of count between Hoover and Hoover++ for google\_advertising\_id and 'null'.  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612140343\_265108&externalid=20260612\_140348\_00050\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612140343_265108&externalid=20260612_140348_00050_r4cjx)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612140349\_480355&externalid=20260612\_140428\_00051\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612140349_480355&externalid=20260612_140428_00051_r4cjx)  

##### **visitor\_\_platform\_group**

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142004\_696887&externalid=20260604\_142008\_00054\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142004_696887&externalid=20260604_142008_00054_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142001\_996929&externalid=20260604\_142104\_00057\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142001_996929&externalid=20260604_142104_00057_bjd9w)

Summary: Difference of count and new category ‘null’ added in Hoover++.

**Updated Analysis:**Difference of count between Hoover and Hoover++ for few platform groups and 'null'.  
Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612142357\_732153&externalid=20260612\_142436\_00078\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612142357_732153&externalid=20260612_142436_00078_r4cjx)  
Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260612142351\_972589&externalid=20260612\_142356\_00077\_r4cjx](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260612142351_972589&externalid=20260612_142356_00077_r4cjx)

#### **Advertisement Entity:**

##### advertisement\_\_agency\_id

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142036\_976692&externalid=20260604\_142040\_00055\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142036_976692&externalid=20260604_142040_00055_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142041\_983332&externalid=20260604\_142143\_00059\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142041_983332&externalid=20260604_142143_00059_bjd9w)

Summary: advertisement\_\_agency\_id = 0 has been added in Hoover++ and has huge count. 

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614215601\_601442&externalid=20260614\_215604\_00023\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614215601_601442&externalid=20260614_215604_00023_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614215623\_392547&externalid=20260614\_215658\_00024\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614215623_392547&externalid=20260614_215658_00024_q5d66)  
  
**Summary: **Column `advertisement__agency_id`, Hoover has 950 rows and Hoover++ has 951 rows; **945 out of 951 match exactly**.
- **6 do not match**, specifically `agency_id = 0` is the critical one: Hoover has 0 records with a null agency ID, Hoover++ has **1,596,227**, which is the entire source of the total count difference (Hoover 795,311 vs Hoover++ 2,391,548).
- The remaining 5 mismatches are real agency IDs each differing by exactly +2: `90586` (241 vs 243), `92274` (48 vs 50), `109043` (18 vs 20), `114237` (6 vs 8), `127310` (733 vs 735).  

##### advertisement\_\_ad\_delivery\_method

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142124\_596785&externalid=20260604\_142129\_00058\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142124_596785&externalid=20260604_142129_00058_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604142119\_445295&externalid=20260604\_142221\_00061\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604142119_445295&externalid=20260604_142221_00061_bjd9w)

Summary: advertisement\_\_ad\_delivery\_method has new category ‘Null’ with a huge count in Hoover++.

|  |  |  |
| --- | --- | --- |
| advertisement\_\_ad\_delivery\_method | Hoover Count | Hoover++ Count |
| Dynamic | 376784 | 376784 |
| Static | 112405 | 112405 |
| Null | 0 | 414969 |

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614221641\_355161&externalid=20260614\_221645\_00030\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614221641_355161&externalid=20260614_221645_00030_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614221635\_995829&externalid=20260614\_221714\_00031\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614221635_995829&externalid=20260614_221714_00031_q5d66)
- Summary: Column `advertisement__ad_delivery_method`  has 2 values being compared: `Static` matches exactly (Hoover **138,903** vs Hoover++ **138,903**); `Dynamic` differs by +10 (Hoover **656,408** vs Hoover++ **656,418**).Total count: Hoover **795,311** vs Hoover++ **795,321** — overall diff of **+10** on `Dynamic` delivery method only.  

#### Candidate Entity:

##### candidate\_\_site\_id

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604154520\_367269&externalid=20260604\_154525\_00044\_nngc7](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604154520_367269&externalid=20260604_154525_00044_nngc7)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604154524\_837484&externalid=20260604\_154647\_00015\_rw6wd](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604154524_837484&externalid=20260604_154647_00015_rw6wd)

Summary: Count matches, but new category ‘null’ in Hoover++.

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614222556\_577050&externalid=20260614\_222600\_00034\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614222556_577050&externalid=20260614_222600_00034_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614222602\_341487&externalid=20260614\_222630\_00035\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614222602_341487&externalid=20260614_222630_00035_q5d66)
- Summary: The column `candidate__site_id` within Hoover returns 1 row, and all **2,392,150** records have `\N`. In Hoover++, returned 2 rows: **1,596,227** records have `0` and **795,321** have `\N`, with a total of  **2,391,548**. Hoover has **602 more records** than Hoover++ in total (2,392,150 vs 2,391,548); within Hoover++, the same records are split across two representations (`0` and `\N`) rather than written as a single `\N` value as Hoover does.  

##### candidate\_\_buyer\_platform\_id

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604154602\_458443&externalid=20260604\_154606\_00089\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604154602_458443&externalid=20260604_154606_00089_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604154609\_085921&externalid=20260604\_154801\_00091\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604154609_085921&externalid=20260604_154801_00091_bjd9w)

Summary: Difference of count and new category ‘0’ in Hoover++.  

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614223535\_199331&externalid=20260614\_223538\_00036\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614223535_199331&externalid=20260614_223538_00036_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614223544\_807073&externalid=20260614\_223622\_00037\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614223544_807073&externalid=20260614_223622_00037_q5d66)
- **Summary:** Column `candidate__buyer_platform_id` within Hoover has **66 rows**, Hoover++ has **67 rows**; **66 rows match exactly** between both sides.

  The only difference: `candidate__buyer_platform_id = 0` exists **only in Hoover++** with count **1,596,227** being entirely absent from Hoover.  

#### Slot Entity:

##### slot\_\_time\_position\_class

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225003\_559230&externalid=20260614\_225007\_00040\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225003_559230&externalid=20260614_225007_00040_q5d66)

Hoover++ -[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225001\_478001&externalid=20260614\_225508\_00042\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225001_478001&externalid=20260614_225508_00042_q5d66)

Summary: Difference of count and new category ‘null’ in Hoover++.

**Updated Analysis:**

- Hoover:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225003\_559230&externalid=20260614\_225007\_00040\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225003_559230&externalid=20260614_225007_00040_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225001\_478001&externalid=20260614\_225031\_00041\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225001_478001&externalid=20260614_225031_00041_q5d66)
- Summary: Column `slot__time_position_class`, **6 values match exactly but 2 values do not match** for`null`; Hoover **188,837** vs Hoover++ **188,225** (difference **-612**); `pause_midroll` Hoover **2,589** vs Hoover++ **2,599** (difference **+10**).  

##### slot\_\_environment

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604154900\_806700&externalid=20260604\_154904\_00002\_7sut3](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604154900_806700&externalid=20260604_154904_00002_7sut3)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604163427\_278161&externalid=20260604\_163520\_00059\_nngc7](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604163427_278161&externalid=20260604_163520_00059_nngc7)

Summary: Difference of count and new category ‘null’ in Hoover++.

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225935\_007474&externalid=20260614\_225939\_00044\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225935_007474&externalid=20260614_225939_00044_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614225953\_279375&externalid=20260614\_230022\_00046\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614225953_279375&externalid=20260614_230022_00046_q5d66)
- Summary: Column `slot__environment` has 4 values: `PAGE` (**10,627**) and `PLAYER` (**17,386**) match exactly on both sides; `VIDEO` differs by **+10** (Hoover **2,175,300** vs Hoover++ **2,175,310**) and `null` differs by **-612** (Hoover **188,837** vs Hoover++ **188,225**).  

#### Auction Entity:

##### auction\_\_buyer\_group\_id

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165158\_949551&externalid=20260604\_165203\_00122\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165158_949551&externalid=20260604_165203_00122_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165201\_073525&externalid=20260604\_165559\_00028\_ym5ax](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165201_073525&externalid=20260604_165559_00028_ym5ax)

Summary: New category '0' added in Hoover++. Other counts are matching.  

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614230605\_261492&externalid=20260614\_230609\_00047\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614230605_261492&externalid=20260614_230609_00047_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614230609\_456318&externalid=20260614\_230650\_00048\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614230609_456318&externalid=20260614_230650_00048_q5d66)
- Summary: Column `auction__buyer_group_id`; Hoover has **160 rows**, Hoover++ has **161 rows**; **160 rows match exactly** on both sides.

  The only difference is `auction__buyer_group_id = 0` which exists **only in Hoover++** with count **1,596,227**, entirely absent from Hoover.  

##### auction\_\_device\_type

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165216\_730200&externalid=20260604\_165221\_00123\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165216_730200&externalid=20260604_165221_00123_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165221\_807659&externalid=20260604\_165329\_00125\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165221_807659&externalid=20260604_165329_00125_bjd9w)

Summary: Only counts of ‘null’ are mismatching.

####   
**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614234841\_406308&externalid=20260614\_234845\_00051\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614234841_406308&externalid=20260614_234845_00051_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614234845\_492426&externalid=20260614\_234925\_00053\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614234845_492426&externalid=20260614_234925_00053_q5d66)
- Summary: Column `auction__device_type` has 6 values; **5 match exactly**: `CONNECTED_TV` (173,537), `PC` (5,588), `PHONE` (11,228), `SET_TOP_BOX` (17,032) and `TABLET` (1,969).

  The only difference is `null` where Hoover has **2,182,796** and Hoover++ has **2,182,194**, with Hoover having **602 more records** in total (2,392,150 vs 2,391,548).  
  
**Partners Entity:**

##### partners\_\_supply\_source

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165248\_674708&externalid=20260604\_165253\_00124\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165248_674708&externalid=20260604_165253_00124_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604165315\_266661&externalid=20260604\_165422\_00126\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604165315_266661&externalid=20260604_165422_00126_bjd9w)

Summary: Difference of records b/w Hoover and Hoover++ is huge. As output is large, please refer above queries.

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614234903\_854523&externalid=20260614\_234906\_00052\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614234903_854523&externalid=20260614_234906_00052_q5d66)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260614234920\_113165&externalid=20260614\_234950\_00054\_q5d66](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260614234920_113165&externalid=20260614_234950_00054_q5d66) 
- Summary: Only 9 out of \~4,889 distinct values differ between Hoover and Hoover++. Hoover++ has 602 fewer total rows (2,391,548 vs 2,392,150) and 3 more distinct supply\_source patterns. The biggest shift is -1,581 nulls in Hoover++ offset by +893 on `[1]` and +90 on `[1, 5]`. The 10 empty-array rows in Hoover are gone entirely in Hoover++.  

##### partners\_\_entity\_source

Hoover - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604170926\_833242&externalid=20260604\_170929\_00138\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604170926_833242&externalid=20260604_170929_00138_bjd9w)

Hoover++ - [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260604170931\_346055&externalid=20260604\_171038\_00142\_bjd9w](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260604170931_346055&externalid=20260604_171038_00142_bjd9w)

Summary: partners\_\_entity\_source has more categories in Hoover++ and differences are huge.  

**Updated Analysis:**

- Hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260615005852\_896913&externalid=20260615\_005855\_00004\_z7ddk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260615005852_896913&externalid=20260615_005855_00004_z7ddk)
- Hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260615005856\_227803&externalid=20260615\_005937\_00005\_z7ddk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260615005856_227803&externalid=20260615_005937_00005_z7ddk)
- Summary: Hoover has 194 distinct values, Hoover++ has 193. The one missing in Hoover++ is `[]` (empty array). 183 values have the same count in both Hoover and Hoover++. 11 values have different counts: nulls are 189,806 in Hoover vs 188,225 in Hoover++, `[slot]` is 246,946 vs 247,835, `[slot, slot]` is 126,961 vs 127,045, `[ad]` is 466,755 vs 466,759, `[ad, ad]` is 259,979 vs 259,985, `[]` is 10 vs 0, and 5 long slot arrays differ by 1 or 2 each. Total rows: Hoover 2,392,150, Hoover++ 2,391,548. Hoover++ has 602 fewer rows.

# Candidate fields analysis on BCV

# Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

Analysis result was generated at 2026-07-23

- Recommended for Backfill — 45 column(s)
- Recommended Excluded (size ≥ 0.03 TiB) — 1 column(s)
- Recommended No Backfill (usage below threshold) — 723 column(s)


# Columns Recommended for Backfill - 45 column(s)

Talked with Karan in Slack:

The candidate view from Hoover++ DOES NOT include `slot` and `ad` entities..

```js
generally speaking, there is no relationship between candidate <=> slot. A relationship can only be estatbilished after the ad selection process and there is a selected ad on that candidate. in this case, a corresponding slot can be defined by following the route candidate -> selected ad -> slot. but for other candidates without selected ad, we can not link them into any slots.
```

Hence in Hoover++ we do not have `ad` and `slot` entities inside the `candidate_ctx`

We will create separate "enriched" views as well to bridge this gap (later phase)

| **Column Name** | **Type** | **Backfill?** | **Comment** |
| --- | --- | --- | --- |
| auction\_\_internal\_seat\_id | array(bigint) | YESFIXED | Used in LQS(11) |
| auction\_\_error | varchar | YESFIXED | Used in LQS(76), Others(1) |
| auction\_\_ifa\_type | varchar | YESFIXED | Used in Insights(9405), LQS(1), Others(1) |
| auction\_\_market\_integration\_type | varchar | YESFIXED | Used in Arena(12215) |
| auction\_\_dynamic\_floor\_price\_algorithm | varchar | YESFIXED | Used in Arena(1528), LQS(1) |
| auction\_\_supply\_chain | varchar | YESFIXED | Used in Arena(2), LQS(8) |
| auction\_\_third\_party\_identifier\_ids | array(integer) | YESFIXED | Used in ETL(Y), LQS(10) |
| candidate\_\_price | double | YESFIXED | Used in LQS(21), Others(18) |
| candidate\_\_response\_time | integer | YESFIXED | Used in LQS(95), Others(2) |
| candidate\_\_response\_time\_first\_hop | integer | YESFIXED | Used in LQS(86), Others(2) |
| partners\_\_role | array(varchar) | NOALL NULL VALUES | Used in Insights(14215), LQS(82)No need to backfill since all values are NULL. But need to double check since this field is common and widely used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726203915\_058412&externalid=20260726\_203917\_00042\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726203915_058412&externalid=20260726_203917_00042_majn2) |
| partners\_\_rule\_type\_priority | array(varchar) | NOALL NULL VALUES | Used in Insights(5768), LQS(16)All NULL values. But need to double check since this field is common and widely used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204107\_528377&externalid=20260726\_204109\_00043\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204107_528377&externalid=20260726_204109_00043_majn2) |
| partners\_\_unified\_rule\_priority\_\_priority\_tier | array(varchar) | NOALL NULL VALUES | Used in Insights(5768), LQS(10)All NULL values. But need to double check since this field is common and widely used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204206\_863621&externalid=20260726\_204207\_00044\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204206_863621&externalid=20260726_204207_00044_majn2) |
| partners\_\_unified\_rule\_priority\_\_sub\_priority\_value | array(integer) | NOALL NULL VALUES | Used in Insights(5768), LQS(10)All NULL values. But need to double check since this field is common and widely used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204302\_130200&externalid=20260726\_204303\_00045\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204302_130200&externalid=20260726_204303_00045_majn2) |
| partners\_\_distributor\_network\_id | array(bigint) | NOALL NULL VALUES | Used in Insights(13956), LQS(74)No need to backfill since all values are NULL for this field. But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204502\_780711&externalid=20260726\_204504\_00046\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204502_780711&externalid=20260726_204504_00046_majn2) |
| partners\_\_outbound\_order\_id | array(bigint) | NO → YES | Used in LQS(10)Should be ok to not backfill this field since almost all values are NULL (and -1). And usage is very light-weight. But since this field is a pair concept with below “partners\_\_outbound\_order\_type“, I think we should backfill them together. [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204559\_676785&externalid=20260726\_204600\_00047\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204559_676785&externalid=20260726_204600_00047_majn2) |
| partners\_\_outbound\_order\_type | array(varchar) | YES | Used in Insights(5768), LQS(21)We should backfill this field since it could contain meaningful values e.g. “EXCHANGE\_ORDER“[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726204817\_624060&externalid=20260726\_204819\_00048\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726204817_624060&externalid=20260726_204819_00048_majn2) |
| partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier | array(varchar) | NO | Used in Insights(5768), LQS(9)No need to backfill since all values are NULL for this field. But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726205256\_366638&externalid=20260726\_205257\_00049\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726205256_366638&externalid=20260726_205257_00049_majn2) |
| partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | array(integer) | NO | Used in Insights(5768), LQS(10)No need to backfill since all values are NULL for this field. But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726205435\_724357&externalid=20260726\_205437\_00050\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726205435_724357&externalid=20260726_205437_00050_majn2) |
| partners\_\_outbound\_order\_priority\_type | array(varchar) | NO | Used in Insights(5768), LQS(17)No need to backfill since all values are NULL for this field. But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726205559\_476201&externalid=20260726\_205601\_00051\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726205559_476201&externalid=20260726_205601_00051_majn2) |
| partners\_\_network\_is\_extra\_item\_owner | array(boolean) | NO | Used in Insights(18941), LQS(76)No need to backfill since All values `false` . But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726205702\_716764&externalid=20260726\_205704\_00052\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726205702_716764&externalid=20260726_205704_00052_majn2) |

# Columns Recommended for Exclude (size ≥ 0.03 TiB) — 8 column(s)

| **Column Name** | **Type** | **Size(TiB)** | **Exclude?** | **Comment** |
| --- | --- | --- | --- | --- |
| request\_\_identifier\_\_source | varchar | 0.08 | No. Need backfill. | Used in Insights(2183), LQS(50). Also found a lot usage by user AF `svc-ciec-sct`  in Arena ETL. Can’t remove. [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260726210017\_747074&externalid=20260726\_210019\_00053\_majn2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260726210017_747074&externalid=20260726_210019_00053_majn2) |

# Recommended No Backfill (usage below threshold) — 723 column(s)

Details see command line output.

# Columns with Mismatched

Summary: TBD  
Matched transactions: TBD  
Matched fields: TBD  
Unmatched fields: TBD

## Columns with Mismatched Types

| **Column Name** | **SRC Type** | **BCV Type** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| Not found. Type are all the same for same column name. |  |  |  |  |

## Columns with Mismatched Values

**Summary**:

\[2026-07-13 20:17:14\] Value validation batch\_id: 20260712200000  (executing all 1 batch(es))

\[2026-07-13 20:24:02\] Value validation summary:  
\[2026-07-13 20:24:02\] Matched transactions: 86/100  
\[2026-07-13 20:24:02\] Matched fields (exact): 424/532 (97.74%)  +  96 globally-equivalent  
\[2026-07-13 20:24:02\] Unmatched fields: 12/532 (2.26%)

**142** field(s) were skipped during value validation because they are parent structure nodes (type matches a structural type **and** at least one child column exists).

**96** field(s) had value differences that are considered **semantically equivalent** under the global equivalence rules (e.g. `null` ↔ `0`, `[null]` ↔ `null`, `[]` ↔ `null`).


| Metric | Count | Ratio |
| --- | --- | --- |
| SRC Transactions | 100 |  |
| Matched Transactions (SRC ∩ BCV) | 86 | 86% |
| Total Fields | 532 |  |
| Matched Fields (exact) | 424 | 97.7% |
| Globally Equivalent Fields | 96 | 18% |
| **Unmatched Fields** | **12** | **2.3%** |

| **Column Name** | **SRC Values** | **BCV Values** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| ### `request__mrc_compliance_label` | See screenshot | See screenshot | NOKNOWN\_ISSUE | Known Issue: Due to lacking of postbid IVT. |
| ### `request__hashed_key_value` | See screenshot | See screenshot | NO | Known Issue: Tracked in[Request fields analysis on BCV](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV) |
| ### `request__bid_request__auction_type` | See screenshot | See screenshot | NOHOOVER++ IS CORRECT | No need to fix. Hoover++ is correct. Tracked in [Request fields analysis on BCV](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV) |
| ### `slot__time_position_class` | See screenshot | See screenshot | NOQUESTION | Should be due to this as talked with Karan in slack:“The candidate view from Hoover++ DOES NOT include `slot` and `ad` entities..““We will create separate "enriched" views as well to bridge this gap (later phase)“In that case, shall we remove all slot and ad entities from candidate BCV to make the design behaviour consistent? @Bhargava, Karan@Wang, Yu |
| ### `slot__ad_unit_id` | See screenshot | See screenshot | NOQUESTION | Same as above. |
| ### `slot__sequence` | See screenshot | See screenshot | NOQUESTION | Same as above. |
| ### `advertisement__flags` | See screenshot | See screenshot | NOQUESTION | Hoover logic: TBD ? Why Hoover result is NULL? Hoover++ / BCV logic: |
| ### `advertisement__slot_index` | See screenshot | See screenshot | NOQUESTION | Hoover logic: TBD ? Why Hoover result is NULL?Hoover++ / BCV logic: |
| ### `advertisement__active_term_id` | See screenshot | See screenshot | NOQUESTION | Same question as above. |
| ### `auction__ab_test_items__collection_id` | See screenshot | See screenshot | YES | ***Root cause***: we didn’t set “***ab\_test\_items***“ related fields during buildAuction process in CandidateHandler.java |
| ### `auction__ab_test_items__bucket_id` | See screenshot | See screenshot | YES | Same as above. |
| ### `partners__outbound_listing_id` | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260727192813\_146985&externalid=20260727\_192815\_00276\_5izpw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260727192813_146985&externalid=20260727_192815_00276_5izpw) | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260727194928\_942723&externalid=20260727\_195115\_00000\_yd34q](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260727194928_942723&externalid=20260727_195115_00000_yd34q) | YESNEED INVESTIGATION | I checked other transactions in this batch, the “**partners\_\_outbound\_listing\_id**“ is actually showing non-null values and are consistent with Hoover tables. So need extra time to investigate the root cause of this diff for this specific transaction. |
| `request__bit_flags` | `576531121052057600`\` | `612559918071021568` | YESNEED INVESTIGATION | Sometimes the forecast\_bit\_flag is SET sometimes it is not. Needs to be investigated why. |

# Action Items

# Reference

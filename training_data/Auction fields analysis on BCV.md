# Auction fields analysis on BCV

# Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |



# Columns Recommended for Backfill - 12 column(s)

| **Column Name** | **Type** | **Backfill?** | **Comment** |
| --- | --- | --- | --- |
| request\_\_ifa\_type | varchar | YES | Used in LQS(67)One of the deprecated fields from previous analysis. No need to backfill.Confirmed in review meeting. We should backfill it. [Entity - Request](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191808429/Entity+-+Request) |
| auction\_\_privacy\_flags | integer | YES | Used in LQS(62), Custom Report(170) |
| auction\_\_market\_integration\_type | varchar | YES | Used in LQS(6), Arena(6794) |
| auction\_\_supply\_chain\_\_nodes | array(varchar) | NEED RENAMEFIXED | Used in LQS(25)Naming convention mismatch.Need to rename for this field. |
| auction\_\_supply\_chain\_\_ver | varchar | YESFIXED | Used in LQS(25), others(1) |
| auction\_\_third\_party\_identifier\_ids | array(integer) | YESFIXED | Used in ETL(Y), LQS(1) |
| auction\_\_device\_ipv6 | varchar | YESFIXED | Used in LQS(23) |
| auction\_\_device\_ext\_truncated\_ip | integer | YESFIXED | Used in LQS(16) |
| partners\_\_role | array(varchar) | NO | Used in LQS(52), Insights(8459)No need to backfill since all values are NULL for this field. But need to double check since this field is common and widely used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708001007\_698944&externalid=20260708\_001009\_00004\_h9zun](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708001007_698944&externalid=20260708_001009_00004_h9zun) |
| partners\_\_break\_id | array(bigint) | NO | Used in LQS(10)All NULL values but some are \[NULL\]， some are \[NULL, NULL\][https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714030332\_478952&externalid=20260714\_030334\_00011\_v7pgw](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714030332_478952&externalid=20260714_030334_00011_v7pgw) |
| partners\_\_distributor\_network\_id | array(bigint) | NO | Used in LQS(54), Arena(1), Insights(8042)No need to backfill since all values are NULL for this field. But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708001231\_187814&externalid=20260708\_001233\_00008\_h9zun](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708001231_187814&externalid=20260708_001233_00008_h9zun) |
| partners\_\_network\_is\_extra\_item\_owner | array(boolean) | NO | Used in LQS(16), Insights(4293)No need to backfill since All values `false` . But need to double check since this field is common and heavily used by Insights.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708001055\_920680&externalid=20260708\_001057\_00005\_h9zun](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708001055_920680&externalid=20260708_001057_00005_h9zun) |
| process\_batch\_id | varchar | YESFIXED | rename the column batch\_id to process\_batch\_id in H++ views |

# Columns Recommended for Exclude (size ≥ 0.03 TiB) — 8 column(s)

| **Column Name** | **Type** | **Size(TiB)** | **Exclude?** | **Comment** |
| --- | --- | --- | --- | --- |
| auction\_\_internal\_seat\_id | varchar | 0.04 | No. Need backfill. | Used in LQS(18), AF(172). Used by user AF `sa-presto-af-etl`  in Arena ETL. Can’t remove. [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707011941\_347181&externalid=20260707\_011942\_00010\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707011941_347181&externalid=20260707_011942_00010_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_asi | integer | 0.03 | Need confirm with User | Used in LQS(32), Others(5)Used by user: - sa-presto-tier2 (via `trino-python-client`) - LQS users:     - `jcicho200`     - `jsautn873`     - `jjohns816`     - `lxiao160`     - `fcampo027` Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707012212\_205285&externalid=20260707\_012213\_00011\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707012212_205285&externalid=20260707_012213_00011_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_sid | varchar | 0.04 | Need confirm with User | Used in LQS(34), Others(8)Same usage and user as above. Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707012712\_281734&externalid=20260707\_012714\_00012\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707012712_281734&externalid=20260707_012714_00012_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_rid | array(varchar) | 0.04 | Need confirm with User | Used in LQS(25)Same usage and user as above. Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707012907\_928761&externalid=20260707\_012909\_00013\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707012907_928761&externalid=20260707_012909_00013_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_name | varchar | 0.03 | Need confirm with User | Used in LQS(25)Same usage and user as above. Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707020703\_787348&externalid=20260707\_020704\_00019\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707020703_787348&externalid=20260707_020704_00019_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_domain | array(integer) | 0.03 | Need confirm with User | Used in LQS(25)Same usage and user as above. Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707020853\_634086&externalid=20260707\_020854\_00020\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707020853_634086&externalid=20260707_020854_00020_88ykk) |
| auction\_\_supply\_chain\_\_nodes\_\_hp | varchar | 0.03 | Need confirm with User | Used in LQS(25)Same usage and user as above. Need to confirm with Tier-2 team and these personal users for their use case.[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707020946\_732538&externalid=20260707\_020947\_00021\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707020946_732538&externalid=20260707_020947_00021_88ykk) |
| auction\_\_device\_ip | integer | 0.06 | YESFIXED | Used in LQS(23)Used by user: - sa-presto-tier2 (via `trino-python-client`) - LQS users:     - `jcicho200`     - `esoula200`     - `glomsa275` [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260707021044\_099894&externalid=20260707\_021046\_00022\_88ykk](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260707021044_099894&externalid=20260707_021046_00022_88ykk) |

# Recommended No Backfill (usage below threshold) — 410 column(s)

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
\[2026-07-13 20:24:02\] Matched transactions: 100/100  
\[2026-07-13 20:24:02\] Matched fields (exact): 393/472 (99.15%)  +  75 globally-equivalent  
\[2026-07-13 20:24:02\] Unmatched fields: 4/472 (0.85%)

**113** field(s) were skipped during value validation because they are parent structure nodes (type matches a structural type **and** at least one child column exists).

**75** field(s) had value differences that are considered **semantically equivalent** under the global equivalence rules (e.g. `null` ↔ `0`, `[null]` ↔ `null`, `[]` ↔ `null`).


| Metric | Count | Ratio |
| --- | --- | --- |
| SRC Transactions | 100 |  |
| Matched Transactions (SRC ∩ BCV) | 100 | 100.0% |
| Total Fields | 472 |  |
| Matched Fields (exact) | 393 | 99.2% |
| Globally Equivalent Fields | 75 | 15.9% |
| **Unmatched Fields** | **4** | **0.8%** |

| **Column Name** | **SRC Values** | **BCV Values** | **Need Change?** | **Comment** |
| --- | --- | --- | --- | --- |
| ### `request__flags` | See screenshot | See screenshot | NOKNOWN\_ISSUE | Update: Thanks to @Bhargava, Karan helping identify this. Slack convo: <https://freewheel.slack.com/archives/C0AQKLYPGM8/p1784147063047509>  **Possible root cause:** All observed differences are caused by a single flag bit. The SRC value is consistently greater than the BCV value by **134,217,728 (bit 27)**, suggesting that one request flag is set in SRC but not in BCV.134217728 = 2^27 For request\_\_flags, I took a look. 2^27 is NOT `BIT_FLAG_CREATIVE_AUDIENCE_TARGETING_DEFAULT` It's `PRIMARY_REQUEST` for `request__flags` Matcher sets this field for current Hoover. Since there's no matcher component for Hoover++, this field is not set.There is no downstream usage of this field so this is a known difference that can be ignored.`❯ python3 flag_validator.py --control 1224999433 --stage 1090781705  ======================================================================   Control value : 1224999433  (0x0000000049040209)   Stage value   : 1090781705  (0x0000000041040209) ======================================================================  ✅  MATCHING flags (6):     [bit  0]  PREFETCH  (1)     [bit  3]  LIVE  (8)     [bit  9]  SECURE  (512)     [bit 18]  USER_HIT  (262144)     [bit 24]  USE_DEVICE_ID  (16777216)     [bit 30]  DISABLE_TRACKING_REDIRECT  (1073741824)  ❌  Flags SET in CONTROL but MISSING from STAGE (1):     [bit 27]  PRIMARY_REQUEST  (134217728)  ⚠️   Flags SET in STAGE but NOT in CONTROL (0):     (none — no extra flags in stage)  ======================================================================`tool I used -\> [https://github.freewheel.tv/kbharg432/hoover-plus-validation-tool/blob/master/flag\_validator.py](https://github.freewheel.tv/kbharg432/hoover-plus-validation-tool/blob/master/flag_validator.py) |
| ### `auction__buyer_id` | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714234908\_548622&externalid=20260714\_234909\_00085\_btta4](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714234908_548622&externalid=20260714_234909_00085_btta4) | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260714235034\_825190&externalid=20260714\_235222\_00087\_btta4](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260714235034_825190&externalid=20260714_235222_00087_btta4) | YESFIXED | **Possible root cause:** The BCV table appears to encode `auction__buyer_id` into a namespaced/composite `long` value, while the source table stores the original buyer ID. The low-order bits remain unchanged, suggesting that only the high-order bits are used as a namespace or entity-type prefix.**Example:**`SRC: 73157 BCV: -5188146770730738235`In 64-bits format:`SRC 73157: 0x0000000000011dc5  BCV: 0xb800000000011dc5``SRC 12191: 0x0000000000002f9f  BCV: 0xb800000000002f9f`The BCV value preserves the original ID (`73157`) in the low-order bits while adding a fixed high-order prefix, resulting in a negative `long` value. |
| ### `auction__impression__error` | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715000746\_911357&externalid=20260715\_000747\_00016\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715000746_911357&externalid=20260715_000747_00016_a6c4k) | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715000758\_029958&externalid=20260715\_000938\_00017\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715000758_029958&externalid=20260715_000938_00017_a6c4k) | YESFIXED | **Possible root cause:** we didn’t process and set this error field during the auction\_\_impression node processing in Auction\_Handler.java. Need double confirm. Same as what Daniel has identified for Ack table analysis. |
| ### `auction__metadata_auditing_flags` | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715001840\_738582&externalid=20260715\_001841\_00019\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715001840_738582&externalid=20260715_001841_00019_a6c4k) | See screenshot[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260715001853\_103469&externalid=20260715\_002041\_00021\_a6c4k](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260715001853_103469&externalid=20260715_002041_00021_a6c4k) | YES | **Possible root cause:** we didn’t process and set this metadata\_auditing\_flags field during the auction node processing in Auction\_Handler.java. Need double confirm. |
| ### `request__hashed_key_value` | See screenshot | See screenshot | YES | Tracked by [Request fields analysis on BCV](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV) |
| ### `request__bid_request__auction_type` | See screenshot | See screenshot | NO | According to [Request fields analysis on BCV](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/811008074/Request+fields+analysis+on+BCV)H++ is correct |

# Action Items

- Check with Karan to see if all the reviewed fix items could be easily covered by <https://github.freewheel.tv/data/hoover-model/pull/401> 
- Check with Insights Team for the usage of fields that are all NULL or FALSE and how they gonna process this values from business perspective?
- Check with Tier-2 Team for the auction\_\_supply\_chain\_\_nodes\_\* usages is necessary or not so that we can possible remove them since they have bigger column size. 

# Reference

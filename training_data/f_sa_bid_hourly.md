# f\_sa\_bid\_hourly

- Hoover sql: [https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f\_sa\_bid\_hourly.sql](https://github.freewheel.tv/data/transformer/blob/master/config/optimus/sql/f_sa_bid_hourly.sql)
- Hoover++ sql: [https://github.freewheel.tv/data/hoover-model/blob/master/validation\_sqls/transformer\_tables/hoover\_streaming\_src/f\_sa\_bid\_hourly\_h%2B%2B.sql](https://github.freewheel.tv/data/hoover-model/blob/master/validation_sqls/transformer_tables/hoover_streaming_src/f_sa_bid_hourly_h%2B%2B.sql)
- Please check the tracker here: [Discrepancy Tracker](https://freewheel.atlassian.net)
- Validations tracker → [Hoover Validations Documentation Tracker](https://freewheel.atlassian.net/wiki/pages/viewpage.action?spaceKey=Infrastructure&title=Hoover+Validations+Documentation+Tracker)

Below is validation results for f\_sa\_bid\_hourly, comparing data from current hoover model and the new H++ output of the same table.


## New Diffs

Below list is all diffs that need further investigation (unknown diffs)

|  | **Column Name** | **Expected** | **Status** | **Comment** |
| --- | --- | --- | --- | --- |
| 1 | inbound\_listing\_ids | NO | NEEDS FURTHER INVESTIGATION | Needs to be investigated further; validator is UNSURE as to the reason why the diff exists. |

---

# 2026-07-21 → Hour 08

**📋 SUMMARY**

- **Failed checks:** Dimension values, Row-level hash
- Dimensions analyzed: 103 — differences found
- Metrics analyzed: 11 — ✓ pass
- Row count: Control 294,839 / Stage 294,839 — ✓ match
- Row hash diffs: 24 — mismatch


---

**🔍 DIMENSION VALUE DIFFERENCES (Actual Values)**  
*This shows which ACTUAL values are different between control and stage - not just counts!*  

| Dimension | Control Total | Stage Total | Only in Control | Only in Stage |
| --- | --- | --- | --- | --- |
| **inbound\_listing\_ids** | 651 | 655 | 0 | 4 |


**Sample Values (first 5 dimensions with differences):**

**inbound\_listing\_ids:**  
*Only in STAGE (4 total):* \[206034 227229 346526\], \[206034 227229 227230 346526\], \[ 51813 116749 486616\], \[206034 346526\]

**✓ All metric sums match!**

**📐 ROW-LEVEL ANALYSIS (GROUP BY dimensions, SUM metrics, xxhash64)**  

| Check | Result |
| --- | --- |
| **Aggregated Row Count** | ✓ Match (294,839 rows) |
| **Row Hash** | **MISMATCH** (Only in Control: 12, Only in Stage: 12) |




---

#  2026-04-16 → Hour 12

We're NOT aligned between Hoover \<\> Hoover++. Three code-level issues identified, two requiring fixes in the hoover-model repo.

- 
- 
- 
- 

For this hour, we see 377,876 rows in control vs 378,527 rows in stage. The checks completed (and their status):

**Failed checks:** Row-level hash

- Dimensions analyzed: 101 (72 pass, 29 have mismatches) — ❌ mismatch
- Metrics analyzed: 11 — ❌ mismatch
- Row count: Control 377,876 / Stage 378,527 — mismatch (+651 in stage)
- Row hash diffs: 332,476 control-only + 333,121 stage-only — mismatch

## Dimension diffs

29 dimensions have value-level mismatches. They fall into 3 categories:

### Category 1: **Inventory fields** (root cause: Issue 1: protobuf vs Avro null semantics)

6 dimensions mismatch due to inventory field NULLs in **sales\_channel=6 (auction\_upstream)**.  
**sales\_channel=5 (auction)** matches; this single root cause accounts for the vast majority of row hash diffs.


| **Dimension** | **Control unique values** | **Stage unique values** | **Control-only values** | **Stage-only values** |
| --- | --- | --- | --- | --- |
| site\_section\_id | 4,019 | 3,542 | 482 | 5 |
| site\_section\_group\_ids | 3,400 | 2,992 | 412 | 4 |
| site\_id | 1,479 | 1,301 | 180 | 2 |
| asset\_id | 2,646 | 2,495 | 154 | 3 |
| series\_id | 1,477 | 1,400 | 78 | 1 |
| asset\_group\_ids | 2,087 | 2,023 | 65 | 1 |

### Category 2: bit\_flag, 11 values ONLY in control (known difference)

Control has 61 distinct bit\_flag values vs 50 in stage. The 11 control-only values all have bit 55 set (2^55). This is expected — the IVT compaction pipeline isn't running yet so the FORECAST flag (bit 55) isn't set because request\_flags are not populated. Tracked in the Hoover Validations Documentation Tracker (<https://freewheel.atlassian.net/wiki/pages/viewpage.action?spaceKey=Infrastructure&title=Hoover+Validations+Documentation+Tracker>). 

### Category 3: reseller\_id (root cause: Issue 3 — protobuf vs Avro null semantics)

- reseller\_id: Control 121 unique / Stage 122 unique — 1 control-only, 2 stage-only
- Small number of rows where control shows -1 but stage shows 0. See Issue 3 below for root cause and fix.

## Metrics diff

- received\_bid: Control 466,625 / Stage 467,296 — diff +671 (+0.14%)
- resolved\_bid: Control 449,816 / Stage 450,458 — diff +642 (+0.14%)
- bid\_received\_price\_usd: Control $5,084,962.52 / Stage $5,091,855.56 — diff +$6,893.04 (+0.14%)
- bid\_pre\_filtered: Control 292,467 / Stage 292,788 — diff +321 (+0.11%)

## Column-level diff

43 dimension combinations have real metric differences. All 43 are from sales\_channel=6 across network\_id values {533595, 512116}. The pattern is consistent: control has more bids per row (e.g., control=3 vs stage=2) with proportional price differences. Total impact across the 43 combos: received\_bid -60, bid\_received\_price\_usd -$336.53. This is a downstream effect of Issue 1, different inventory values cause bids to aggregate into different GROUP BY buckets. Will auto-resolve when Issue 1 fix is applied.  

**Issue 1 — Inventory Field NULLs (sales\_channel=6):** In setInventoryIdsFromCtx(), the check if (context == null || !context.hasInventory()) return; causes early return for \~30% of auction\_upstream contexts where the ad server never set the inventory sub-message. Old pipeline always materialized Inventory via Avro so this never happened. Result: site\_id, site\_section\_id, asset\_id, series\_id stay NULL → COALESCE → -1. Additionally, inventory.hasSeriesId() and inventory.hasSiteId() have no else-branch, so those fields also stay NULL when false. Fix: remove !context.hasInventory() from the return check, and call Utils.unmask() unconditionally for series\_id/site\_id.  
<https://github.freewheel.tv/data/hoover-model/blob/5f71a57608034236c7d5bee23b76a2f9c3e8ef96/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java>  
  
**Issue 3 — reseller\_id Default Value:** In getAuctionSANetworks(), Utils.unmask(rawAuction.getExternalNetworkId()) returns 0 when the field isn't set (proto default) instead of null (Avro behavior) → COALESCE doesn't fire → stored as 0 instead of -1. In getPartnerTagBuyerNetworks(), same problem plus Utils.unmask() is missing entirely. Fix: add rawAuction.hasExternalNetworkId() ternary in both locations, returning null when not set.

- Both are protobuf vs Avro null semantics differences, old pipeline read Avro (nullable fields), new pipeline reads proto directly (default values instead of null).
- Old pipeline (file: etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java):  
<https://github.freewheel.tv/data/etl/blob/66c60d6633394e15214cee31f586c66dcb39c4ca/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java>

New pipeline (file: hoover-model/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java):  
<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java>  
  

---

## 2026-04-22 → Hour 09

- 
- 
- 

##   
Results Summary:

| **Check** | **Control (Hive)** | **Stage (Hoover++)** | **Difference** |
| --- | --- | --- | --- |
| Total rows | 275,481 | 274,743 | 738 more in control |
| bid\_received\_price\_usd | $4,040,845 | $4,030,498 | $10,347 more in control (0.26%) |
| Dimensions with differences | 102 analyzed | 102 analyzed | 27 mismatch |
| Metrics with differences | 11 analyzed | 11 analyzed | 11 mismatch |
| Row hash differences | 243,595 control-only | 242,870 stage-only | 486,465 total |

### What is sales\_channel?

sales\_channel is a column in the f\_sa\_bid\_hourly table. It tells you what type of auction network the row represents:

- **sales\_channel = 4** (Programmatic) — the buyer side of a deal. Biggest volume, approximately 238,000 rows.
- **sales\_channel = 5** (Auction / Partner Tag) — a marketplace auction. Approximately 18,000 rows.
- **sales\_channel = 6** (Auction Upstream) — the MPE seller side of an exchange deal. Approximately 19,000 rows.

### What is received\_bid and bid\_received\_price\_usd?

These are metric columns in the f\_sa\_bid\_hourly table, defined in the SQL:

- received\_bid = the count of bids received. In the SQL it is computed as SUM(received\_bid).
- bid\_received\_price\_usd = the dollar value of those bids. In the SQL it is computed as SUM(bid\_received\_price\_usd).


| **sales\_channel** | **Description** | **Control Rows** | **Stage Rows** | **Row Difference** | **Control received\_bid** | **Stage received\_bid** | **received\_bid Difference** | **Control bid\_received\_price\_usd** | **Stage bid\_received\_price\_usd** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | Programmatic | 238,199 | 237,581 | 618 more in control | 313,424 | 312,489 | 935 | $3,732,242 | $3,722,793 |
| 5 | Auction | 18,316 | 18,258 | 58 more in control | 24,647 | 24,562 | 85 | $0 | $0 |
| 6 | Auction Upstream | 18,966 | 18,904 | 62 more in control | 26,229 | 26,148 | 81 | $308,603 | $307,705 |

- sales\_channel = 4 drives 91% of the total $10,347 price difference
- sales\_channel = 5 has $0 pricing because partner tag auctions do not carry USD prices
- sales\_channel = 6 contributes $899, almost entirely caused by inventory field NULLs (Issue 2 below)


| **Metric** | **Control** | **Stage** | **Difference** | **Percent Difference** |
| --- | --- | --- | --- | --- |
| received\_bid | 364,300 | 363,199 | 1,101 | 0.30% |
| resolved\_bid | 353,456 | 352,390 | 1,066 | 0.30% |
| selected\_primary\_bid | 76,732 | 76,502 | 230 | 0.30% |
| selected\_fallback\_bid | 5,617 | 5,601 | 16 | 0.28% |
| bid\_received\_price | $4,846,684 | $4,835,287 | $11,396 | 0.24% |
| bid\_resolved\_price | $4,728,809 | $4,717,885 | $10,923 | 0.23% |
| bid\_selected\_price | $1,195,465 | $1,192,327 | $3,137 | 0.26% |
| bid\_received\_price\_usd | $4,040,845 | $4,030,498 | $10,347 | 0.26% |
| bid\_resolved\_price\_usd | $3,988,571 | $3,978,435 | $10,135 | 0.25% |
| bid\_selected\_price\_usd | $904,050 | $901,326 | $2,723 | 0.30% |
| bid\_pre\_filtered | 150,411 | 149,962 | 449 | 0.30% |

All 11 metrics: control is higher than stage by 0.23% to 0.30%.  

| **Category** | **Dimensions Affected** | **What is Different** | **Root Cause** |
| --- | --- | --- | --- |
| 1. Inventory NULLs (6 dimensions) | site\_section\_id, site\_id, asset\_id, series\_id, site\_section\_group\_ids, asset\_group\_ids | Stage has -1 where control has real values. Only sales\_channel = 6. | Java bug in setInventoryIdsFromCtx() method |
| 2. bit\_flag (1 dimension) | bit\_flag | Control has bit 55 set, stage does not. 12 control-only values. | IVT pipeline has not run on Hoover data yet. Not a code bug. |
| 3. reseller\_id (1 dimension) | reseller\_id | Stage has 0 where control has -1. Only sales\_channel = 4. | Java bug in 3 methods |
| 4. Row gap dimensions (19 dimensions) | user\_state\_id, user\_city\_id, postal\_code, deal\_id, programmatic\_advertiser\_id, outbound\_listing\_ids, outbound\_order\_id, global\_advertiser\_ids, global\_brand\_ids, market\_ad\_id, bidding\_buyer\_id, app\_bundle, standard\_content\_series\_id, standard\_iab\_category\_ids, standard\_endpoint\_id, standard\_genre\_ids, inbound\_listing\_ids | Values only exist in the 738 extra control rows | Row gap caused by bit\_flag difference and source timing |

## Why Everything Differs: One Root Cause

The old and new pipelines handle unset protobuf fields differently.

**Old pipeline** (Hive / etl-schema-hoover):

Raw Protobuf → RawToHooverTransformer.transform() → Avro objects → AuctionHandler.java builds Partner objects from Avro → Unset field in Avro = null → SQL: COALESCE(null, -1) = -1 (correct)

**New pipeline** (Hoover++ / hoover-model):

Raw Protobuf → TransactionContext (thin wrapper, NO Avro conversion) → AuctionNetworkHandler.java builds AuctionNetwork objects directly from protobuf → Unset int64 field in protobuf = 0 (not null) → SQL: COALESCE(0, -1) = 0 (wrong — COALESCE does not fire because 0 is not null)

The old HooverGenerator.getRows() was approximately 500 lines and called RawToHooverTransformer.transform() on every auction — this was the implicit null-conversion layer. The new HooverGenerator.buildCtx() is just 5 lines wrapping raw protobuf. The new design is correct for performance, but AuctionNetworkHandler was not updated with has\*() checks to handle protobuf default values.

**The SQL files are identical between old and new, all bugs are in the Java layer.** **HooverGenerator.java does NOT need changes.** **All fixes are in one file: AuctionNetworkHandler.java.**

## Issue 1 — reseller\_id shows 0 instead of -1 (3 bugs in AuctionNetworkHandler.java)

**What is happening:** Every sales\_channel = 4 row where the external\_network\_id field is unset shows reseller\_id = 0 in stage instead of reseller\_id = -1 in control.

**Note about sales\_channel = 5:** sales\_channel = 5 (partner tag buyers) always have a real reseller\_id value set, the field is never unset for those rows. So this bug does not affect sales\_channel = 5. Those rows match perfectly on reseller\_id between control and stage.

The SQL is identical between old and new (COALESCE only fires on null. Protobuf gives 0 (not null) for unset fields, so COALESCE never fires.)

### Bug 1a — in the getAuctionSANetworks() method (builds the sales\_channel = 4 auction seller network)

**Current code in Hoover ++ AuctionNetworkHandler.java:**

[**https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L73**](https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L73)  
  
**Why it is wrong:** rawAuction is raw protobuf. When the field is unset, getExternalNetworkId() returns 0 (not null). Utils.unmask(0) returns 0. The SQL then does COALESCE(0, -1) which equals 0 because 0 is not null.  
  
**Current code in Hoover etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java:** 

<https://github.freewheel.tv/data/etl/blob/6141fb245a232ef470f29cbe7024ab93b50ee28a/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L336>

  
Fix for hoover ++ code:

```
if (rawAuction.hasExternalNetworkId()) {
    network.setReseller_network_id(Utils.unmask(rawAuction.getExternalNetworkId()));
} else {
    network.setReseller_network_id(null);
}
```

### Bug 1b — in the getPartnerTagBuyerNetworks() method (builds sales\_channel = 5 partner tag buyer network)

**Current code in Hoover ++ AuctionNetworkHandler.java:**  
<https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L195>


**Why it is wrong:** Two bug in one line: missing has check + missing Utils.unmask()

**Old working code in AuctionHandler.java: **  
[**https://github.freewheel.tv/data/etl/blob/6141fb245a232ef470f29cbe7024ab93b50ee28a/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L168**](https://github.freewheel.tv/data/etl/blob/6141fb245a232ef470f29cbe7024ab93b50ee28a/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L168)


|  | **Old (AuctionHandler.java \~line 178)** | **New (AuctionNetworkHandler.java)** |
| --- | --- | --- |
| Code | partner.setResellerNetworkId(auction.getExternalNetworkId()); | network.setReseller\_network\_id(rawAuction.getExternalNetworkId()); |
| Object | Avro RTB\_Auction (null when unset, already unmasked) | Raw protobuf (0 when unset, still masked) |
| Problems | None | 1) Missing hasExternalNetworkId() check, 2) Missing Utils.unmask() |

  
Fix:

```
if (rawAuction.hasExternalNetworkId()) {
    network.setReseller_network_id(Utils.unmask(rawAuction.getExternalNetworkId()));
} else {
    network.setReseller_network_id(null);
}
```

In the above validation run, the C=5 (partner tag buyers) always has the field set, never unset for those rows. So this fix won't change current validation numbers (SC=5 already matches). But the fix is still needed for **code correctness** in the scenerio, if a future partner tag row ever has the field unset, the code can break without this fix.  

**Bug 1c — Old code** (AuctionHandler.java, method getOrderSABuyerNetworks()

<https://github.freewheel.tv/data/etl/blob/6141fb245a232ef470f29cbe7024ab93b50ee28a/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L116>

Here auction is the **Avro** RTB\_Auction. When the field is unset, Avro returns **null**. The comment says "already unmask" — RawToHooverTransformer unmasked it during Avro conversion.

**Bug 1c — New code** (AuctionNetworkHandler.java, method buildOrderBuyerNetworks()):

<https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L160>  
  
Fix:

```
if (auction.getExternal_network_id() != null && auction.getExternal_network_id() != 0L) {
    network.setReseller_network_id(auction.getExternal_network_id());
} else {
    network.setReseller_network_id(null);
}
```


In 1a/1b we have the raw protobuf (rawAuction) so we are able to call hasExternalNetworkId() to check if the field was set. In 1c we have the Auction Java object which was already built from the protobuf, it has no has\*() method, so we check for null and 0L instead. All three fixes are in the same file: AuctionNetworkHandler.java.

## Bug 2a: Inventory fields: hasInventory() early return in setInventoryIdsFromCtx()


**Old working code:** etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/PartnerHandler.java  
  
<https://github.freewheel.tv/data/etl/blob/7a606a3b3157e354ca5e70c0a0f98bed8c9f14ee/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/PartnerHandler.java#L830>

**What is broken: Hoover++ file:** AuctionNetworkHandler.java → method setInventoryIdsFromCtx()

** **[**https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L441**](https://github.freewheel.tv/data/hoover-model/blob/6c331608f0c34e13cfa6de5d756e8257d790d853/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L441)

When hasInventory() is false (\~30% of SC=6 rows), the method returns immediately. All 6 inventory fields (site\_section\_id, site\_id, asset\_id, series\_id, site\_section\_group\_ids, asset\_group\_ids) stay null. SQL does COALESCE(null, -1) = -1. The old Hoover pipeline always had the inventory object available (the old Avro conversion layer created it even when protobuf didn't have it), so the old code never hit this early return and always set real values.

**Data impact:** Stage has +5,149 extra -1 in site\_section\_id, +5,115 in site\_id, +3,699 in asset\_id, +1,985 in series\_id vs control which has real values.

**What has to be done:** Change !context.hasInventory() back to a null check that matches the old behavior. When the protobuf Inventory sub-message is not present, context.getInventory() on the raw protobuf still returns a default empty Inventory object (protobuf default instance), which is NOT null. So the fix is:

// CURRENT (broken): if (context == null || !context.hasInventory()) return;

// FIX — match old behavior: if (context == null || context.getInventory() == null) return;

This way, even when hasInventory() is false, context.getInventory() returns the default Inventory instance (not null), the method continues, and each field-level has\*() check handles whether to set a value or not.


## May 6 Validations: 

##   

After running another round of validations after deploying the above code changes, I dug deeper into the remaining discrepancy on **f\_sa\_bid\_hourly** and identified the root cause of the inventory field gaps on sales\_channel = 6 (auction upstream) rows. 

  
**1st Issue:**

- When comparing control (old Hive pipeline) vs stage (Hoover++ pipeline), sales\_channel = 6 rows showed a \~42 percentage point gap in default rates for site\_id, site\_section\_id, asset\_id, and series\_id. Sales\_channel = 5 (partner tag) matched perfectly, so the issue is isolated to the upstream network path only.

**Root Cause:**

1. In the old Avro-based pipeline, getUpstreamNetworkExecutionCtxIndex() returned a nullable Integer object. When the field wasn't set, Avro returned null → extractValue(null, -1) → -1 → isValidIndex(size, -1) → false → returned null → no upstream network built.
2. In the new protobuf-based pipeline, **getUpstreamNetworkExecutionCtxIndex()** returns a primitive int. So when the field was never serialized, protobuf returns 0 instead of null. The code calls **transactionCtx.getNetworkExecutionCtx**(0), treats 0 as a valid index, and then grabs the context that sits at position 0 which, is not the intended upstream context since that field was never set.

The validation data confirms that: sales\_channel = 5 (which uses the auction's own explicitly-set context index via **rawAuction.getNetworkExecutionCtxIndex**()) matches perfectly, proving the inventory logic works when given the correct context. The issue is basically the wrong context selection on the upstream path.

The method **hasUpstreamNetworkExecutionCtxIndex**() exists in the generated code specifically to distinguish "field set to 0" from "field never set." The same codebase already uses this in two places within tv.freewheel.hoover.entity.NetworkHandler : both **isSspResellerVisible**() and **setContentOwnerInfo**() check hasUpstreamNetworkExecutionCtxIndex() before accessing the value. [https://github.freewheel.tv/data/hoover-model/blob/92c7024b2c2324fafb518f51a5d11e3cb3e\[…\]rc/main/java/tv/freewheel/hoover/entity/NetworkHandler.java](https://github.freewheel.tv/data/hoover-model/blob/92c7024b2c2324fafb518f51a5d11e3cb3ead4f1/src/main/java/tv/freewheel/hoover/entity/NetworkHandler.java#L657)

Looks like **AuctionNetworkHandler.buildAuctionUpstreamNetwork()** was the only caller missing this guard.  
[https://github.freewheel.tv/data/hoover-model/blob/92c7024b2c2324fafb518f51a5d11e3cb3e\[…\]/freewheel/hoover/entity/auction/AuctionNetworkHandler.java](https://github.freewheel.tv/data/hoover-model/blob/92c7024b2c2324fafb518f51a5d11e3cb3ead4f1/src/main/java/tv/freewheel/hoover/entity/auction/AuctionNetworkHandler.java#L416)

**Second issue in setInventoryIdsFromCtx(): **  
The current guard uses context.getInventory() == null. In protobuf, message-type fields never return null, getInventory() returns a default empty Inventory instance when the sub-message was never serialized. So this check never fires. After more investigation for contexts without inventory, the method enters the body, and the else branches for asset\_id and site\_section\_id read getAssetId() / getSiteSectionId() which return 0 on the empty instance, producing unmask(0) instead of null. The correct protobuf approach is !context.hasInventory(), this returns true only when the Inventory sub-message was actually written in the data. When it was never written, the check fails and triggers the early return, leaving all fields null (which SQL then converts to -1). This matches how the old Avro code behaved when inventory was null.

**The changes (both in AuctionNetworkHandler.java):**  
*Change 1* — Add if (!context.hasUpstreamNetworkExecutionCtxIndex()) return null; in buildAuctionUpstreamNetwork(), after the isExchangeOrder check, before the upstream context retrieval. This should prevents wrong context selection. Valid cases unaffected since has returns true when the field IS set.  
*Change 2* — Replace context.getInventory() == null with !context.hasInventory() in setInventoryIdsFromCtx(). Correctly early-returns when Inventory was never serialized. Matches old Avro behavior.  
**Impact:**

- Change 1 closes the \~42 percentage point gap (wrong context) seen in my latest validation run and Change 2 should close the gap on asset\_id and site\_section\_id preventing the code from processing an empty protobuf Inventory object as if it contained real data.  
  
PR for reference : <https://github.freewheel.tv/data/hoover-model/pull/339>

##    
  
**June-18 Validations:**

PR changes confirmed working. The reseller\_id is a perfect match now. SC=6 column-level metric differences went from 43 to 0. Both are fixed and resolved.

##   
**July 11  Validation**

- **Validation Run: July 11, 2026 — Hour 08** Date: 2026-07-11 | Hour: 08 | Environment: Production Control table: fw1\_prd.hoover\_validations.f\_sa\_bid\_hourly\_hive Stage table: fw1\_prd.hoover\_validations.f\_sa\_bid\_hourly\_hoover\_plus 
- Control rows: 326,178 | Stage rows: 326,133

  *Passed:*
    - All 11 metric sums match at the aggregate level (received\_bid, resolved\_bid, selected\_primary\_bid, selected\_fallback\_bid, bid\_received\_price, bid\_resolved\_price, bid\_selected\_price, bid\_received\_price\_usd, bid\_resolved\_price\_usd, bid\_selected\_price\_usd, bid\_pre\_filtered)

  *Issues Identified:*
    - Row count mismatch — stage undercounts by 45 rows (Control: 326,178 / Stage: 326,133)
    - Row-level hash mismatch — 6,235 rows present only in control, 6,190 rows present only in stage
    - Dimension mismatch: bit\_flag — 3 values exclusive to control (72 unique in control vs 69 in stage) — tracked discrepancy
    - Dimension mismatch: inbound\_listing\_ids — 4 array combinations exclusive to stage (655 unique in control vs 659 in stage)
    - Dimension mismatch: asset\_group\_ids — 73 array combinations exclusive to control (1,740 unique in control vs 1,667 in stage)
    - Dimension mismatch: site\_section\_group\_ids — 257 array combinations exclusive to control (2,548 unique in control vs 2,291 in stage)
    - Metric-level diffs: 45 dimension combinations with metric differences
    - 43 combos — bid\_pre\_filtered is exactly 2x control in stage, indicating a double-counting issue (networks 511351 and 510962, integration type OPENRTB\_PG\_TD)
    - 2 combos — received\_bid and bid\_received\_price also doubled on network\_id=510962 (OPENRTB\_PG\_TD)  

      


<https://github.freewheel.tv/data/hoover-model/pull/408/files>  
<https://github.freewheel.tv/data/hoover-model/pull/412>

---

## **July 15  Validation**

**Validation Run: July 15, 2026 — Hour 08** Date: 2026-07-15 | Hour: 08 | Environment: Staging Control table: fw1\_stg.kbhargava\_prd\_test.f\_sa\_bid\_hourly\_hive Stage table: fw1\_stg.kbhargava\_prd\_test.f\_sa\_bid\_hourly\_hoover\_plus 

Control rows: 314,489 | Stage rows: 314,489

*Passed:*

- All 11 metric sums match between control and stage
- Row count is an exact match (314,489 / 314,489) — 45-row gap from Jul 11 fully resolved
- Zero metric-level diff combos — bid\_pre\_filtered double-counting fully resolved
- received\_bid and bid\_received\_price doubling on network\_id=510962 fully resolved
- asset\_group\_ids — fully resolved, no longer a discrepancy
- site\_section\_group\_ids — fully resolved, no longer a discrepancy

***Remaining Issues:***

Row-level hash mismatch — 981 rows only in control, 981 rows only in stage (down 84% from 6,235 in Jul 11). Driven by the two dimension mismatches below

- Dimension mismatch: bit\_flag — 3 values exclusive to control (78 unique in control vs 75 in stage) — tracked discrepancy
- Dimension mismatch: inbound\_listing\_ids — 2 array combinations exclusive to stage (674 unique in control vs 676 in stage), improved from 4 in Jul 11 — not currently on the tracker, flagged for review. Submitted the following PR to address this: <https://github.freewheel.tv/data/hoover-model/pull/420>  
  
  
   

## References:

[Discrepancy Tracker](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191814893/Discrepancy+Tracker)

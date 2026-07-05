# Event Level \(Backward Compatible Views\)

## Known Differences

| **Column Name** | **Known** | **Comment** |
| --- | --- | --- |
| request\_\_flags | Y | This difference is due to the fact that flusher will always try to merge the callbacks within 5-min window to its first\_request if the first\_request also appears in the same 5-min window. This is an internal technical optimization to reduce the flush table size and will not have any impacts to reporting business.For traffic\_type = 2, request\_\_flags are also set by the IVT compaction pipeline. |
| request\_\_is\_filtered | Y | This is most likely because the IVT compaction pipeline isn’t running yet. The IVT entity also sets the value of request\_\_flags POST IVT. |
| MISSING FIELDS  (request\_\_scores for example) | Y | Since some columns are not present in Hoover++ (they’re not used by downstream) they were removed. Hence the diff when checking the full column. |
| \*\_in\_played\_slot metrics in Slot | Y | All \*\_in\_played\_slot metrics are `null` because they’re never populated in the Slot table (they come from the ack table. So seeing an array of null vs the whole value being null, is semantically correct. |
| eligible\_outbound\_orders (schema difference) | Y | Eligible outbound orders schema is different in Hoover \<\> Hoover++. Since not all columns are available, this is expected. |
| eligible\_outbound\_orders\_\_order\_priority | Y | If an order is truly `null`, instead of an empty arraylist, it returns `null`. Semantically the same. |
| eligible\_outbound\_orders\_\_order\_transaction\_type | Y | same as above |
| eligible\_outbound\_orders\_\_order\_type | Y | same as above |
| partners\_\_inbound\_listing\_ids (slot view) | Y | This was renamed to `inbound_listing_id` to avert confusion. Since there’s no `inbound_listing_ids` in Slot partners in Hoover (only in Auction Partners), this was changed. |
| Missing `network_execution_ctx_index` for `ad`impression callbacks | Y | From can not really remember why we need to have the **network\_execution\_ctx\_index **set for ad impression callbacks in H++. guessing we need to overwrite some values in the original network\_execution\_ctx based on the info carried in  ad impression callback.I can not think of a scenario where we will have to rely on this index on slot impression, because the index is already set on slot entity where this slot impression belongs to. so I would suggest we just treat this as an expected differences and document it somewhere in the wiki |
| Duplicate rows (especially for acks) | Y | This is because the kafka broker is sometimes restarted and since the PRD testing environment does not have de-duplication, same keys and records make it through.This will NOT happen in the actual PRD environment. |
| `outbound_order` vs `eligible_outbound_order` | Y | From  :the eligible\_outbound\_orders is the enriched version, we need someone to dive into this logics and understand the difference from the raw field. adding the raw back is easy, but I am still reluctant to do so until we are 100% sure the raw is still neededThere is a ticket out there to track this work. Once we know what the differences are and why, we can decide if we need to add this field back into Hoover++ |
| Differences between ack\_\_metrics\_\_ad\_impression between Hoover \<\> Hoover++ | Y | we don't have a corresponding metrics in H++ which makes more sense from metrics definition, that's the new design. If you really want to find something to align, then use traffic\_type != 1 +`ack__metrics__ad_impression` (in H++), it should be = `ack__metrics__ad_impression in current hoover` |
| inbound\_order\_transaction\_type | N | For resellers, inbound\_order\_transaction\_type is NOT set. PR → <https://github.freewheel.tv/data/hoover-model/pull/371> |
| partners\_\_bit\_flags | N | Hoover++ maps `BIT_FLAG_NETWORK_IS_CAMPAIGN_MANAGER_DEAL_BUYER` to `CARRIAGE_ORDER` instead of `CAMPAIGN_MANAGER_ORDER`. This  explains the `2^37` delta between Hoover and Hoover++: in legacy Hoover (`setSlotPartnerBitFlags`), bit 37 is set only for `CAMPAIGN_MANAGER_ORDER`, while in Hoover++ (`setNetworkBitFlags`) it is set for `CARRIAGE_ORDER`.  PR submitted: <https://github.freewheel.tv/data/hoover-model/pull/385> |
| inventory\_\_asset\_chain\* inventory\_\_site\_section\_chain\* in ack table | Y | In the old Hoover table these are null most of the time: <https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/table/AckTable.java#L77> (only set for the video case)We will leave it because this is more data capabilityThread here: <https://freewheel.slack.com/archives/C01S31V42LX/p1782841339175119> |

## Detailed Analysis

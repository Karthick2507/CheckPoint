# Hoover\+\+ Field Name Changes

# Intro

Below is a table listing out the column names that have been changed or have now become plural in Hoover++

### Request

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| request.context.profile\_concrete\_event\_id  | request.context.profile\_concrete\_event\_ids  |  |
| request.context.ab\_test\_item | request.context.ab\_test\_items |  |
| request.context.ab\_test\_item.collection\_id | request.context.ab\_test\_items.collection\_id |  |
| request.context.ab\_test\_item.bucket\_id | request.context.ab\_test\_items.bucket\_id |  |
| request.context.ab\_test\_item.is\_effective | request.context.ab\_test\_items.is\_effective |  |
| request.soft\_guaranteed\_ad | request.soft\_guaranteed\_ads |  |
| request.soft\_guaranteed\_ad.ad\_id | request.soft\_guaranteed\_ads.ad\_id |  |
| request.soft\_guaranteed\_ad.num\_competing\_ads | request.soft\_guaranteed\_ads.num\_competing\_ads |  |
| request.soft\_guaranteed\_ad.network\_id | request.soft\_guaranteed\_ads.network\_id |  |
| request.soft\_guaranteed\_ad.entity\_type | request.soft\_guaranteed\_ads.entity\_type |  |
| request.soft\_guaranteed\_ad.entity\_id | request.soft\_guaranteed\_ads.entity\_id |  |
| request.guaranteed\_deal\_avail, | request.guaranteed\_deal\_avails, |  |
| request.guaranteed\_deal\_avail.internal\_deal\_id, | request.guaranteed\_deal\_avails.internal\_deal\_id, |  |
| request.guaranteed\_deal\_avail.buyer\_id, | request.guaranteed\_deal\_avails.buyer\_id, |  |
| request.decision\_info.external\_bridge, | request.decision\_info.external\_bridges, |  |
| request.decision\_info.external\_bridge.slot\_index, | request.decision\_info.external\_bridges.slot\_index, |  |
| request.decision\_info.external\_bridge.status, | request.decision\_info.external\_bridges.status, |  |
| request.mrc\_compliance\_label, | request.mrc\_compliance\_labels, |  |
| request.linear\_capnedit, | request.linear\_capnedits, |  |
| request.linear\_capnedit.device\_id, | request.linear\_capnedits.device\_id, |  |
| request.linear\_capnedit.active\_state, | request.linear\_capnedits.active\_state, |  |
| request.linear\_capnedit.tune\_time, | request.linear\_capnedits.tune\_time, |  |
| request.linear\_capnedit.last\_activity\_time, | request.linear\_capnedits.last\_activity\_time, |  |
| request.linear\_capnedit.is\_dvr, | request.linear\_capnedits.is\_dvr, |  |
| request.linear\_capnedit.mode, | request.linear\_capnedits.mode, |  |
| request.bid\_request.impression, | request.bid\_request.impressions, |  |
| request.bid\_request.impression.private\_auction, | request.bid\_request.impressions.private\_auction, |  |
| request.bid\_request.impression.floor, | request.bid\_request.impressions.floor, |  |
| request.bid\_request.impression.deal, | request.bid\_request.impressions.deals, |  |
| request.bid\_request.impression.deal.public\_id, | request.bid\_request.impressions.deals.public\_id, |  |
|  |  |  |

### Advertisement

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| advertisement.opp\_rule\_id | advertisement.opp\_rule\_ids |  |
| advertisement.win\_rule\_id | advertisement.win\_rule\_ids |  |
| advertisement.measurable\_concrete\_event\_id | advertisement.measurable\_concrete\_event\_ids |  |
| advertisement.global\_advertiser\_id | advertisement.global\_advertiser\_ids |  |
| advertisement.global\_brand\_id | advertisement.global\_brand\_ids |  |
|  |  |  |

  

### Auction

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| auction.impression | auction.impressions |  |
| auction.impressions.deals.media\_buyer\_id | auction.impressions.deals.media\_buyer\_ids |  |
| auction.impressions.deals.trading\_desk\_id | auction.impressions.deals.trading\_desk\_ids |  |
| auction.impressions.deals.listing\_id | auction.impressions.deals.listing\_ids |  |
| auction.bid\_throttling\_info.model\_info | auction.bid\_throttling\_info.model\_infos |  |

  

### Candidate

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| candidate.filter\_reason | candidate.filter\_reasons |  |
| candidate.response\_industry | candidate.response\_industries |  |
| candidate.filter\_reason | candidate.filter\_reasons |  |
| candidate.creative\_approval\_request | candidate.creative\_approval\_requests |  |
| candidate.auction\_outbound\_listing\_id | candidate.auction\_outbound\_listing\_ids |  |

### Inventory

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| inventory.asset\_chain | inventory.asset\_chains |  |
| inventory.site\_section\_chain | inventory.site\_section\_chains |  |
| inventory.asset\_chains.postal\_code\_package\_id | inventory.asset\_chains.postal\_code\_package\_ids |  |
| inventory.asset\_chains.visible\_concrete\_event\_id | inventory.asset\_chains.visible\_concrete\_event\_ids |  |
| inventory.site\_section\_chains.postal\_code\_package\_id | inventory.site\_section\_chains.postal\_code\_package\_ids |  |
| inventory.site\_section\_chains.visible\_concrete\_event\_id | inventory.site\_section\_chains.visible\_concrete\_event\_ids |  |

### Partners

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| partners.inbound\_listing\_Id | partners.inbound\_listing\_Ids |  |
| partners.outbound\_listing\_id | partners.outbound\_listing\_ids |  |
| partners.visible\_concrete\_event\_id | partners.visible\_concrete\_event\_ids |  |
| partners.postal\_code\_package\_id | partners.postal\_code\_package\_ids |  |
| partner.listing\_id | partners.listing\_ids |  |
| partners.avails\_category.avails, | partners.metrics.avails, |  |
| partners.avails\_category.unfilled\_avails, | partners.metrics.unfilled\_avails, |  |
| partners.avails\_category.unconstrained\_avails, | partners.metrics.unconstrained\_avails, |  |
| partners.avails\_category.market\_avails, | partners.metrics.market\_avails, |  |
| partners.avails\_category.ssp\_avails, | partners.metrics.ssp\_avails, |  |
| partners.avails\_category.avails\_in\_played\_slot, | slot\_ack\_partners.avails\_in\_played\_slot, |  |
| partners.avails\_category.unfilled\_avails\_in\_played\_slot, | slot\_ack\_partners.unfilled\_avails\_in\_played\_slot, |  |
| partners.avails\_category.unconstrained\_avails\_in\_played\_slot, | slot\_ack\_partners.unconstrained\_avails\_in\_played\_slot, |  |
| partners.avails\_category.raw\_total\_avails\_in\_played\_slot, | slot\_ack\_partners.raw\_total\_avails\_in\_played\_slot, |  |
| partners.avails\_category.market\_avails\_in\_played\_slot, | slot\_ack\_partners.market\_avails\_in\_played\_slot, |  |
| partners.avails\_category.ssp\_avails\_in\_played\_slot, | slot\_ack\_partners.ssp\_avails\_in\_played\_slot, |  |
| partners.avails\_category.total\_avails, | partners.metrics.total\_avails, |  |
| partners.avails\_category.total\_unfilled\_avails, | partners.metrics.total\_unfilled\_avails, |  |
| partners.avails\_category.opportunity, | partners.metrics.opportunity, |  |
| partners.avails\_category.total\_avails\_in\_played\_slot, | slot\_ack\_partners.total\_avails\_in\_played\_slot, |  |
| partners.avails\_category.total\_unfilled\_avails\_in\_played\_slot, | slot\_ack\_partners.total\_unfilled\_avails\_in\_played\_slot, |  |
| partners.avails\_category.opportunity\_in\_played\_slot, | slot\_ack\_partners.opportunity\_in\_played\_slot, |  |
| partners.avails\_category.raw\_opportunity\_in\_played\_slot, | slot\_ack\_partners.raw\_opportunity\_in\_played\_slot, |  |
| partners.avails\_category.slot\_opp\_avails\_in\_played\_slot, | slot\_ack\_partners.slot\_opp\_avails\_in\_played\_slot, |  |
| partners.avails\_category.remaining\_avails, | partners.metrics.remaining\_avails, |  |
| partners.avails\_category.distinct\_inventory\_avails, | partners.metrics.distinct\_inventory\_avails, |  |
| partners.avails\_category.inventory\_avails, | partners.metrics.inventory\_avails, |  |
| partners.avails\_category.raw\_inventory\_distinct\_avails\_in\_played\_slot, | slot\_ack\_partners.raw\_inventory\_distinct\_avails\_in\_played\_slot |  |
|  |  |  |

### Execution Networks

| Previous Column Name | New Column Name | Comments |
| --- | --- | --- |
| execution\_networks.postal\_code\_package\_id | execution\_networks.postal\_code\_package\_ids |  |
| execution\_netrworks.visible\_concrete\_event\_id | execution\_netrworks.visible\_concrete\_event\_ids |  |

  

## Questions?

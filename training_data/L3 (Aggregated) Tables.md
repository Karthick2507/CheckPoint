# L3 \(Aggregated\) Tables

## IVT Related Diff (traffic\_type)

```
traffic_type indicates ivt status (0: valid, 1:invalid-marked in prebid, 2:invalid-marked in postbid). the possible IVT diff comes from postbid ivt, because it is using different data between hoover and hoover++. so it means there may be some ivt traffic(traffic_type=2) in the current hoover being marked as valid(traffic_type=0) in h++ or the other way round.

This may lead to differences in the ack table/ view for different dimensions/ metrics
```

## Summary Table:

|  | **Column Name** | **Expected?** | **Table** | **Status** |
| --- | --- | --- | --- | --- |
| 1 | postal\_code | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 2 | buyer\_group\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 3 | programmatic\_advertiser\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 4 | global\_advertiser\_ids | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 5 | global\_brand\_ids | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 6 | market\_ad\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 7 | trading\_desk\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 8 | site\_section\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 9 | site\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 10 | site\_section\_group\_ids | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 11 | bidding\_seat\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 12 | bidding\_buyer\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 13 | external\_seat\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 14 | outbound\_publisher\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 15 | profile\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 16 | rendition\_id | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 17 |  |  | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 18 | ad\_views | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 19 | no\_clicks | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 20 | can\_quartile | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 21 | ad\_expand | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 22 | ad\_mute | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 23 | ad\_unmute | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 24 | ad\_pause | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 25 | ad\_resume | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 26 | ad\_views\_primary | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 27 | measurable\_video\_ads\_quartile\_impression | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 28 | video\_ads\_unmuted | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 29 | video\_ads\_expanded | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 30 | video\_ads\_resumed | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 31 | video\_ads\_paused | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 32 | mrc\_net\_delivered\_impressions | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 33 | mrc\_net\_tracked\_ads | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 34 | mrc\_unknown\_purchased\_net\_delivered\_impressions | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 35 | mrc\_unknown\_auto\_play\_impressions | NO | f\_order\_sa\_delivered\_hourly | TO BE INVESTIGATED |
| 36 | upstream\_bidding\_revenue\_in\_played\_slot | NO | f\_order\_selected\_hourly | TO BE INVESTIGATED |
| 37 | inbound\_listing\_ids | NO | f\_sa\_bid\_hourly | TO BE INVESTIGATED |
| 38 | channel\_id | NO | f\_inventory\_delivered\_portfolio\_hourly | TO BE INVESTIGATED |
| 39 | postal\_code | NO | f\_inventory\_delivered\_portfolio\_hourly | TO BE INVESTIGATED |
| 40 | postal\_code\_package\_ids | NO | f\_inventory\_delivered\_portfolio\_hourly | TO BE INVESTIGATED |
| 41 | user\_city\_id | NO | f\_inventory\_delivered\_portfolio\_hourly | TO BE INVESTIGATED |
| 42 | operator\_zone\_id | NO | f\_inventory\_delivered\_portfolio\_hourly | TO BE INVESTIGATED |
| 43 | network\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 44 | asset\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 45 | series\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 46 | asset\_group\_ids | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 47 | site\_section\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 48 | site\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 49 | site\_section\_group\_ids | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 50 | airing\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 51 | channel\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 52 | break\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 53 | ad\_unit\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 54 | tracked\_audience\_item\_ids | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 55 | postal\_code | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 56 | postal\_code\_package\_ids | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 57 | user\_city\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 58 | user\_dma\_code | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 59 | standard\_brand\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 60 | inbound\_order\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 61 | outbound\_order\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 62 | outbound\_listing\_ids | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 63 | profile\_id | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 64 | **video\_starts** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 65 | **break\_starts** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 66 | **avails** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 67 | **unconstrained\_avails** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 68 | **ad\_views** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 69 | **no\_ad\_views** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 70 | **no\_clicks** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 71 | **first\_quartile** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 72 | **middle\_quartile** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 73 | **third\_quartile** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 74 | **complete\_quartile** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 75 | **can\_quartile** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 76 | **ad\_mute** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 77 | **ad\_unmute** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 78 | **ad\_pause** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 79 | **total\_avails** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 80 | **total\_unfilled\_avails** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 81 | **opportunity** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 82 | **outbound\_avails** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 83 | **outbound\_opportunity** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 84 | **request\_count** | NO | f\_inventory\_delivered\_hourly | TO BE INVESTIGATED |
| 85 | opportunity\*\_in\_played\_slot metrics | NO | f\_inventory\_sa\_delivered\_hourlyf\_market\_bid\_density\_by\_price\_hourly | TO BE INVESTIGATED |
| 86 | ssp\_floor\_revenue\_in\_request | NO | f\_inventory\_sa\_delivered\_hourly | TO BE INVESTIGATED |

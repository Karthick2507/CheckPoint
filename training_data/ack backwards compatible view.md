# ack backwards compatible view

First, we’ll compare the ack table (`mrm_log_flat.default.ack`) with the backwards compatible view (`etl.public_test1.ack`) in different aspects:

- For the fields present in both tables, what are the type differences?
- What are the fields not present in the backwards compatible view?

## Mismatched Types

I highlight in red the types that cause more of a compatibility concern:

| field | type | view\_type |
| --- | --- | --- |
| request\_\_timestamp | timestamp(3) | timestamp(3) with time zone |
| ack\_\_timestamp | timestamp(3) | timestamp(3) with time zone |
| ack\_\_metrics\_\_fire\_event\_bid\_revenue\_ratio | integer | bigint |
| ack\_\_metrics\_\_fire\_margin\_ratio | integer | bigint |
| partners\_\_avails\_category\_\_unconstrained\_avails | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_market\_avails | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_ssp\_avails | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_market\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_total\_avails | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_total\_unfilled\_avails | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_opportunity | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_total\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_opportunity\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | array(integer) | array(bigint) |
| partners\_\_avails\_category\_\_remaining\_avails | array(integer) | array(bigint) |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | array(array(integer)) | array(array(bigint)) |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | array(array(integer)) | array(array(bigint)) |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | array(array(integer)) | array(array(bigint)) |
| partners\_\_outbound\_exchange\_order\_ids | array(array(bigint)) | array(bigint) |
| candidate\_\_advertisement\_index | integer | bigint |
| ads\_in\_slot\_\_partners\_\_outbound\_rules | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info | array(array(varchar)) | array(varchar) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | array(array(array(varchar))) | array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | array(array(array(array(varchar)))) | array(array(array(varchar))) |
| ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts | array(array(array(varchar))) | array(array(varchar)) |

## Missing in view

I used the [BCV\_analyzer](https://github.freewheel.tv/ywang865/BCV_analyzer) by @Wang, Yu to determine missing fields and usage with the following default thresholds:

ETL = 0, Insights = 0, Arena = 0, LQS \< 10, Others \< 100

Below are the results:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Column Name | usage:ETL | usage: Insights | usage: Arena | usage: LQS | usage: Others |
| request\_\_context\_\_extracted\_key\_value |  |  |  | 303 |  |
| request\_\_context\_\_extracted\_key\_value\_\_\_fw\_dbp |  |  |  | 116 | 181 |
| request\_\_request\_throttling\_info\_\_model\_info\_\_model\_id |  |  |  | 13 |  |
| request\_\_client\_facing\_reason\_code | 1 |  |  | 4 | 1 |
| request\_\_bid\_request\_\_impression\_\_deal\_\_floor |  |  |  | 12 |  |
| inventory\_\_asset\_chain\_\_reseller\_network\_id | 1 |  |  | 5 |  |
| inventory\_\_asset\_chain\_\_supply\_source | 1 |  |  | 5 | 6 |
| inventory\_\_asset\_chain\_\_sales\_channel |  |  |  | 11 |  |
| inventory\_\_asset\_chain\_\_floor\_price |  |  |  | 23 |  |
| inventory\_\_asset\_chain\_\_geo\_visibility\_\_report\_aggregate | 1 |  |  | 5 |  |
| inventory\_\_site\_section\_chain\_\_site\_group\_id |  |  |  | 12 | 3 |
| inventory\_\_site\_section\_chain\_\_floor\_price |  |  |  | 23 |  |
| ack\_\_metrics\_\_avails\_event\_count | 1 |  |  | 42 |  |
| ack\_\_metrics\_\_ad\_net\_avail |  |  |  | 17 |  |
| ack\_\_metrics\_\_ad\_gross\_avail |  |  |  | 17 |  |
| ack\_\_metrics\_\_ad\_unconstrained\_gross\_avail |  |  |  | 17 |  |
| ack\_\_ack\_entity\_type | 1 | 39386 | 5449 | 1037 | 60 |
| advertisement\_\_fill\_rate |  |  |  | 103 |  |
| advertisement\_\_billable\_rate\_denominator\_event\_id |  |  |  | 11 |  |
| advertisement\_\_provider\_measured\_event\_id |  |  |  | 13 |  |
| advertisement\_\_original\_bidding\_price |  |  |  | 15 |  |
| advertisement\_\_net\_price |  |  |  | 12 |  |
| advertisement\_\_active\_aim\_audience\_ids |  |  |  | 17 |  |
| advertisement\_\_effective\_exclude\_aim\_audience\_ids |  |  |  | 13 |  |
| advertisement\_\_geo\_as\_audience\_segments\_id\_pks | 1 |  |  | 72 |  |
| advertisement\_\_candidate\_index |  |  |  | 42 |  |
| slot\_\_original\_max\_ads |  |  |  | 12 |  |
| partners |  |  |  | 23 |  |
| partners\_\_avails\_category\_\_supply\_avails |  |  |  | 70 |  |
| partners\_\_inbound\_listing\_ids |  |  |  | 11 |  |
| partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_flags |  |  |  | 13 |  |
| partners\_\_supply\_priority |  |  |  | 27 |  |
| partners\_\_acquired\_supply\_type |  |  |  | 27 |  |
| candidate\_\_duration |  | 3998 |  |  |  |
| auction\_\_index |  |  | 202 |  |  |
| auction\_\_ifa\_type |  | 7955 |  | 1 |  |
| auction\_\_market\_integration\_type |  |  | 2590 |  |  |
| auction\_\_dynamic\_floor\_price\_algorithm |  |  | 9065 | 1 |  |
| auction\_\_third\_party\_identifier\_ids | 1 |  |  | 5 |  |
| ads\_in\_slot\_\_advertisement\_\_geo\_as\_audience\_segments\_id\_pks | 1 |  |  | 87 |  |
| ads\_in\_slot\_\_auction\_\_ifa\_type |  | 7955 |  | 27 |  |
| ads\_in\_slot\_\_auction\_\_third\_party\_identifier\_ids | 1 |  |  |  |  |
| ads\_in\_slot\_\_candidate\_\_duration |  | 3998 |  | 1 |  |
| ads\_in\_slot\_\_partners |  |  |  | 20 |  |
| ads\_in\_slot\_\_partners\_\_bidding\_up\_revenue | 1 |  |  |  |  |
| ads\_in\_slot\_\_partners\_\_internal\_deal\_ids |  |  |  | 82 |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos | 1 |  |  | 5 |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id |  |  |  | 118 |  |
| ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_aggregate | 1 |  |  |  |  |
| process\_batch\_id |  | 48208 | 5960 | 1096 | 225 |
| \_\_path\_\_ |  |  | 972 | 8 |  |

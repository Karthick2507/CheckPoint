# Ack fields analysis and validation on BCV

For the fields that are matched here are the type differences:

Highlighted in red are the type differences that aren’t as simple as Int → Long

| **Column Name** | **SRC Type** | **BCV Type** | **Notes** |
| --- | --- | --- | --- |
| ~~request\_\_timestamp~~ | ~~timestamp(3)~~ | ~~timestamp(3) with time zone~~ |  |
| ~~ack\_\_timestamp~~ | ~~timestamp(3)~~ | ~~timestamp(3) with time zone~~ |  |
| ack\_\_metrics\_\_fire\_event\_bid\_revenue\_ratio | integer | bigint |  |
| ack\_\_metrics\_\_fire\_margin\_ratio | integer | bigint |  |
| partners\_\_avails\_category\_\_unconstrained\_avails | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_market\_avails | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_ssp\_avails | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_market\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_total\_avails | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_total\_unfilled\_avails | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_opportunity | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_total\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_opportunity\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | array(integer) | array(bigint) |  |
| partners\_\_avails\_category\_\_remaining\_avails | array(integer) | array(bigint) |  |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | array(array(integer)) | array(array(bigint)) |  |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | array(array(integer)) | array(array(bigint)) |  |
| partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | array(array(integer)) | array(array(bigint)) |  |
| partners\_\_outbound\_exchange\_order\_ids | array(array(bigint)) | array(bigint) | Inconsistency in how this is structured between clauses |
| candidate\_\_advertisement\_index | integer | bigint |  |
| ads\_in\_slot\_\_partners\_\_outbound\_rules | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info | array(array(varchar)) | array(varchar) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | array(array(array(array(varchar)))) | array(array(array(varchar)) | - Parent node - Always hardcoded null |
| ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts | array(array(array(varchar))) | array(array(varchar)) | - Parent node - Always hardcoded null |

## Fields missing in BCV view

Below are the fields which were not matched and had some downstream usage:

*following thresholds: ETL = Y OR SOS = Y OR Insights \> 0 OR Arena \> 0 OR LQS ≥ 10 OR CP \> 0 OR AF \> 0 OR Others ≥ 100)  AND  size \< 0.03 TiB (or unknown)*

Highlighted in red are fields which can be excluded

Highlighted in yellow are fields which probably can be excluded

The rest have enough usages that we probably need to migrate them all to the new view

| Column Name | **Usage: ETL** | **Usage: SOS** | **Usage: Insights** | **Usage: Arena** | **Usage: LQS** | **Usage: CP** | **Usage: Other** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ~~request\_\_context\_\_extracted\_key\_value~~ |  |  |  |  | ~~303~~ |  |  | ~~Looks like this is in key\_value now and expectation is that users MUST migrate:  ~~[~~https://github.freewheel.tv/data/hoover-model/pull/57~~](https://github.freewheel.tv/data/hoover-model/pull/57) |
| ~~request\_\_context\_\_extracted\_key\_value\_\_\_fw\_dbp~~ |  |  |  |  | ~~116~~ | ~~5655~~ | ~~181~~ | ~~Looks like this is in key\_value now and expectation is that users MUST migrate: ~~[~~https://github.freewheel.tv/data/hoover-model/pull/57~~](https://github.freewheel.tv/data/hoover-model/pull/57) |
| ~~request\_\_context\_\_extracted\_key\_value\_\_\_fw\_lto~~ |  |  |  |  |  | ~~167~~ |  | ~~Looks like this is in key\_value now and expectation is that users MUST migrate: ~~[~~https://github.freewheel.tv/data/hoover-model/pull/57~~](https://github.freewheel.tv/data/hoover-model/pull/57) |
| request\_\_request\_throttling\_info\_\_model\_info\_\_model\_id |  |  |  |  | 13 |  |  | looks legit: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626173401\_074336&externalid=20260626\_173403\_00103\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626173401_074336&externalid=20260626_173403_00103_ytfr8)No similar struct is present in Hoover++ |
| request\_\_client\_facing\_reason\_code | Y |  |  |  | 4 |  | 1 | Looks like this is coming in through IVT <https://github.freewheel.tv/data/etl/search?q=setClientFacingReasonCode>, @Gao, Peng would you please confirm that this is incoming? |
| request\_\_bid\_request\_\_impression\_\_deal\_\_floor |  |  |  |  | 12 |  |  | confirmed this is not needed |
| inventory\_\_asset\_chain\_\_reseller\_network\_id | Y |  |  |  | 5 |  |  | Probably these fields should be coming from partner arrays? |
| inventory\_\_asset\_chain\_\_supply\_source | Y |  |  |  | 5 |  | 6 |  |
| inventory\_\_asset\_chain\_\_sales\_channel |  |  |  |  | 11 |  |  |  |
| inventory\_\_asset\_chain\_\_floor\_price |  |  |  |  | 23 |  |  |  |
| inventory\_\_asset\_chain\_\_geo\_visibility\_\_report\_aggregate | Y |  |  |  | 5 |  |  |  |
| inventory\_\_site\_section\_chain\_\_site\_group\_id |  |  |  |  | 12 |  | 3 |  |
| inventory\_\_site\_section\_chain\_\_floor\_price |  |  |  |  | 23 |  |  |  |
| ack\_\_metrics\_\_avails\_event\_count | Y | Y | 16011 |  | 44 |  |  |  |
| ack\_\_metrics\_\_ad\_net\_avail |  |  |  |  | 17 |  |  | Probably fine to remove, just a few ad-hoc queries over a few days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626190057\_714281&externalid=20260626\_190059\_00141\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626190057_714281&externalid=20260626_190059_00141_ytfr8) |
| ack\_\_metrics\_\_ad\_gross\_avail |  |  |  |  | 17 |  |  | Probably fine to remove, just a few ad-hoc queries over a few days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626190057\_714281&externalid=20260626\_190059\_00141\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626190057_714281&externalid=20260626_190059_00141_ytfr8) |
| ack\_\_metrics\_\_ad\_unconstrained\_gross\_avail |  |  |  |  | 17 |  |  | Probably fine to remove, just a few ad-hoc queries over a few days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626190057\_714281&externalid=20260626\_190059\_00141\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626190057_714281&externalid=20260626_190059_00141_ytfr8) |
| ack\_\_ack\_entity\_type | Y | Y | 143351 | 1177 | 1062 | 167 | 60 | Rename the levels to be the ack entity type @Bhargava, Karan |
| advertisement\_\_fill\_rate |  |  |  |  | 105 |  |  |  |
| advertisement\_\_billable\_rate\_denominator\_event\_id |  |  |  |  | 11 |  |  | Ask about this one: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629140325\_579943&externalid=20260629\_140327\_00101\_tnf3u](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629140325_579943&externalid=20260629_140327_00101_tnf3u) |
| advertisement\_\_provider\_measured\_event\_id |  |  |  |  | 13 |  |  | looks legit: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626185315\_093033&externalid=20260626\_185316\_00016\_37sh5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626185315_093033&externalid=20260626_185316_00016_37sh5) |
| advertisement\_\_original\_bidding\_price |  |  |  |  | 15 |  |  | Probably fine to remove, only a few ad-hoc queries over several days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626184524\_334218&externalid=20260626\_184525\_00140\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626184524_334218&externalid=20260626_184525_00140_ytfr8) |
| advertisement\_\_data\_provider\_id |  |  |  |  | 3 | 42 |  |  |
| advertisement\_\_net\_price |  |  |  |  | 12 |  |  |  |
| advertisement\_\_active\_aim\_audience\_ids |  |  |  |  | 17 |  |  |  |
| advertisement\_\_effective\_exclude\_aim\_audience\_ids |  |  |  |  | 13 |  |  | looks legit: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626183748\_419712&externalid=20260626\_183749\_00137\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626183748_419712&externalid=20260626_183749_00137_ytfr8) |
| advertisement\_\_geo\_as\_audience\_segments\_id\_pks | Y |  |  |  | 72 |  |  |  |
| advertisement\_\_matched\_geo\_ids |  |  |  |  | 3 | 42 |  |  |
| advertisement\_\_matched\_postal\_code\_ids |  |  |  |  | 3 | 42 |  |  |
| advertisement\_\_matched\_postal\_code\_package\_ids |  |  |  |  | 3 | 42 |  |  |
| advertisement\_\_matched\_region\_ids |  |  |  |  | 3 | 42 |  |  |
| advertisement\_\_candidate\_index |  |  |  |  | 42 |  |  |  |
| slot\_\_original\_max\_ads |  |  |  |  | 12 |  |  | unlikely needed, a few ad-hoc queries over a couple days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626183411\_776704&externalid=20260626\_183413\_00006\_37sh5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626183411_776704&externalid=20260626_183413_00006_37sh5) |
| slot\_\_carriage\_listing\_split\_unit\_id |  | Y |  |  | 10 |  |  |  |
| partners |  | Y |  |  | 23 |  |  |  |
| partners\_\_avails\_category\_\_supply\_avails |  | Y |  |  | 74 |  |  |  |
| partners\_\_inbound\_listing\_ids |  |  |  |  | 11 |  |  | unlikely needed, a few ad-hoc queries over a couple of days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626182922\_866451&externalid=20260626\_183118\_00001\_37sh5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626182922_866451&externalid=20260626_183118_00001_37sh5) |
| partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_flags |  |  |  |  | 13 |  |  | unlikely to be needed, a few queries over a couple of days: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626181642\_681005&externalid=20260626\_181643\_00132\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626181642_681005&externalid=20260626_181643_00132_ytfr8) |
| partners\_\_supply\_priority |  |  |  |  | 27 |  |  |  |
| partners\_\_acquired\_supply\_type |  |  |  |  | 27 |  |  |  |
| candidate\_\_duration |  | Y | 4135 |  |  |  |  |  |
| candidate\_\_cch\_key |  |  |  |  |  | 12 |  |  |
| candidate\_\_trust\_id |  |  |  |  |  | 334 |  |  |
| auction\_\_index |  |  |  | 208 |  |  |  |  |
| auction\_\_ifa\_type |  |  | 8223 |  | 1 |  |  |  |
| auction\_\_buyer\_platform\_url\_id |  | Y | 4686 |  | 2 |  |  |  |
| auction\_\_market\_integration\_type |  |  |  | 2670 |  |  |  |  |
| auction\_\_dynamic\_floor\_price\_algorithm |  |  |  | 9342 | 1 |  |  |  |
| auction\_\_third\_party\_identifier\_ids | Y |  |  |  | 6 |  |  |  |
| ads\_in\_slot\_\_advertisement\_\_geo\_as\_audience\_segments\_id\_pks | Y |  |  |  | 87 |  |  |  |
| ads\_in\_slot\_\_auction\_\_ifa\_type |  |  | 8223 |  | 27 |  |  |  |
| ads\_in\_slot\_\_auction\_\_third\_party\_identifier\_ids | Y |  |  |  |  |  |  |  |
| ads\_in\_slot\_\_candidate |  | Y |  |  |  |  |  |  |
| ads\_in\_slot\_\_candidate\_\_duration |  | Y | 4135 |  | 1 |  |  |  |
| ads\_in\_slot\_\_partners |  | Y |  |  | 20 |  |  |  |
| ads\_in\_slot\_\_partners\_\_bidding\_up\_revenue | Y |  |  |  |  |  |  |  |
| ads\_in\_slot\_\_partners\_\_internal\_deal\_ids |  |  |  |  | 82 |  |  |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos | Y |  |  |  | 5 |  |  |  |
| ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_flags |  |  |  |  | 118 |  |  |  |
| ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_aggregate | Y | Y |  |  |  |  |  | Deprecated |
| process\_batch\_id |  |  | 233957 | 5862 | 1152 | 9903 | 48219 |  |

## Negligible fields

I excluded these queries to be left with a shortlist of fields to potentially ignore:

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629170202\_310528&externalid=20260629\_170204\_00186\_tnf3u](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629170202_310528&externalid=20260629_170204_00186_tnf3u)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629174903\_697642&externalid=20260629\_174904\_00220\_tnf3u](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629174903_697642&externalid=20260629_174904_00220_tnf3u)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629175619\_550875&externalid=20260629\_175620\_00230\_tnf3u](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629175619_550875&externalid=20260629_175620_00230_tnf3u)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629180144\_046713&externalid=20260629\_180145\_00232\_tnf3u](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629180144_046713&externalid=20260629_180145_00232_tnf3u)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629181731\_777926&externalid=20260629\_181823\_00001\_egup2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629181731_777926&externalid=20260629_181823_00001_egup2)

[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260629182038\_278128&externalid=20260629\_182039\_00008\_egup2](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260629182038_278128&externalid=20260629_182039_00008_egup2)

| **Column Name** | **Usage: LQS** | **Usage: Others** |
| --- | --- | --- |
| request\_\_context\_\_uri | 1 |  |
| request\_\_context\_\_video\_cro\_context\_group\_id | 3 |  |
| request\_\_context\_\_site\_section\_cro\_asset\_group\_id | 7 |  |
| request\_\_context\_\_distributor\_video\_asset\_group\_id | 1 |  |
| request\_\_scores\_\_ad\_id | 1 |  |
| request\_\_network\_data\_visibility\_config\_\_data\_right | 1 |  |
| request\_\_network\_ctx\_\_network\_id | 2 |  |
| request\_\_extra\_geo\_info\_\_descriptions | 1 |  |
| request\_\_extra\_geo\_info\_\_ids | 1 |  |
| request\_\_extra\_geo\_info\_\_is\_pulse | 1 |  |
| inventory\_\_asset\_chain\_\_revenue | 1 |  |
| inventory\_\_asset\_chain\_\_distributor\_revenue | 1 |  |
| inventory\_\_asset\_chain\_\_ssp\_clearing\_revenue | 2 |  |
| inventory\_\_asset\_chain\_\_site\_group\_id | 6 | 2 |
| inventory\_\_asset\_chain\_\_inbound\_order\_id | 4 |  |
| inventory\_\_asset\_chain\_\_outbound\_order\_id | 5 |  |
| inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_order\_id |  | 1 |
| inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_sales\_channel | 1 |  |
| inventory\_\_asset\_chain\_\_sales\_channel | 8 |  |
| inventory\_\_asset\_chain\_\_internal\_deal\_ids | 4 |  |
| inventory\_\_asset\_chain\_\_audience\_segment\_max\_cpm | 3 |  |
| inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 4 |  |
| inventory\_\_site\_section\_chain\_\_site\_group\_id | 9 | 3 |
| inventory\_\_site\_section\_chain\_\_outbound\_order\_id |  | 2 |
| inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_order\_id |  | 2 |
| inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 1 |  |
| inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 1 |  |
| inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 1 |  |
| inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 1 |  |
| inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 1 |  |
| ack\_\_ad\_unit\_id | 3 |  |
| ack\_\_custom\_ad\_id | 1 |  |
| ack\_\_event\_provider | 5 |  |
| ack\_\_identifier | 2 |  |
| ack\_\_identifier\_\_sequence | 2 |  |
| ack\_\_metrics | 7 |  |
| visitor\_\_session\_id | 4 |  |
| visitor\_\_user\_group | 4 |  |
| visitor\_\_user\_agent\_device\_id | 6 |  |
| visitor\_\_ortb\_fields\_from\_ua | 4 |  |
| visitor\_\_original\_ip\_address | 5 |  |
| advertisement\_\_external\_reseller\_\_competition\_resellers | 1 |  |
| advertisement\_\_billable\_rate\_denominator\_event\_id | 8 |  |
| advertisement\_\_fallback\_ad\_uniq\_id | 1 |  |
| advertisement\_\_net\_price | 9 |  |
| advertisement\_\_error\_partner | 1 |  |
| advertisement\_\_error\_domain | 1 |  |
| slot\_\_time\_position\_sequence | 7 |  |
| slot\_\_ad\_units | 4 |  |
| slot\_\_cue\_point\_sequence | 7 |  |
| slot\_\_raw\_max\_duration | 5 |  |
| slot\_\_raw\_max\_ads | 4 |  |
| slot\_\_outbound\_order\_\_active\_aim\_audience\_ids | 5 |  |
| slot\_\_outbound\_order\_\_effective\_exclude\_aim\_audience\_ids | 5 |  |
| candidate | 8 |  |
| candidate\_\_content\_type | 1 |  |
| candidate\_\_price\_type | 1 |  |
| candidate\_\_flags | 1 |  |
| candidate\_\_rtb\_impression\_index | 1 |  |
| candidate\_\_candidate\_network\_to\_auction\_seller\_network\_exchange\_rate | 1 |  |
| candidate\_\_discount\_barter | 2 |  |
| auction | 7 |  |
| auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids | 3 |  |
| auction\_\_error | 3 |  |
| auction\_\_mkpl\_partner\_tags | 1 |  |
| auction\_\_external\_network\_id | 1 |  |
| ads\_in\_slot | 8 |  |
| ads\_in\_slot\_\_advertisement | 8 |  |
| ads\_in\_slot\_\_advertisement\_\_external\_vast\_ad\_id | 1 |  |
| ads\_in\_slot\_\_partners\_\_site\_group\_id | 5 |  |

## Analysis Results

In this comparison, I compared 100 ack records between Hoover and Hoover++.  This is the summary:

| Metric | Count | Ratio |
| --- | --- | --- |
| SRC Transactions | 100 |  |
| Matched Transactions (SRC ∩ BCV) | 100 | 100.0% |
| Total Fields | 1547 |  |
| Matched Fields | 432 | 27.9% |
| **Unmatched Fields** | **1115** | **72.1%** |

Since there were so many fields I had to break it up into types of differences and explore these separately.

### Null Handling

The simplest case is the records that only differ by how they handle null values:

- Empty list SRC, null in BCV
    - request\_\_context\_\_profile\_concrete\_event\_id
    - request\_\_context\_\_standard\_genre\_ids
    - request\_\_context\_\_standard\_language\_ids
    - request\_\_context\_\_standard\_iab\_category\_ids
    - request\_\_context\_\_standard\_content\_viewership\_profile\_ids
    - request\_\_context\_\_standard\_sport\_entity\_ids
    - request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id
    - request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids
    - request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id
    - request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids
    - request\_\_scores\_\_network\_id
    - request\_\_scores\_\_flag
    - request\_\_scores\_\_score
    - request\_\_candidates
    - request\_\_soft\_guaranteed\_ad\_\_ad\_id
    - request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads
    - request\_\_soft\_guaranteed\_ad\_\_network\_id
    - request\_\_soft\_guaranteed\_ad\_\_entity\_type
    - request\_\_soft\_guaranteed\_ad\_\_entity\_id
    - request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id
    - request\_\_guaranteed\_deal\_avail\_\_buyer\_id
    - request\_\_decision\_info\_\_external\_bridge\_\_slot\_index
    - request\_\_decision\_info\_\_external\_bridge\_\_status
    - request\_\_decision\_info\_\_inventory\_protections\_\_level
    - request\_\_decision\_info\_\_inventory\_protections\_\_scope
    - request\_\_decision\_info\_\_inventory\_protections\_\_separation
    - request\_\_linear\_capnedit\_\_device\_id
    - request\_\_linear\_capnedit\_\_active\_state
    - request\_\_linear\_capnedit\_\_tune\_time
    - request\_\_linear\_capnedit\_\_last\_activity\_time
    - request\_\_linear\_capnedit\_\_is\_dvr
    - request\_\_linear\_capnedit\_\_mode
    - request\_\_yield\_optimization\_ids\_\_demand\_type
    - request\_\_yield\_optimization\_ids\_\_demand\_id
    - request\_\_yield\_optimization\_ids\_\_optimization\_ids
    - request\_\_mpe\_matcher\_filters\_\_id
    - request\_\_mpe\_matcher\_filters\_\_bucket\_id
    - request\_\_mpe\_matcher\_filters\_\_weight
    - visitor\_\_tracked\_term
    - visitor\_\_postal\_code\_id
    - visitor\_\_postal\_code\_package\_\_network\_id
    - visitor\_\_postal\_code\_package\_\_postal\_code\_package\_id
    - visitor\_\_standard\_device\_type\_ids
    - visitor\_\_universal\_iids
    - advertisement\_\_global\_advertiser\_ids
    - advertisement\_\_global\_brand\_ids
    - advertisement\_\_variant\_creative\_ids
    - advertisement\_\_variant\_rendition\_ids
    - advertisement\_\_global\_industry\_ids
    - advertisement\_\_contextual\_billings\_\_segment\_id
    - advertisement\_\_contextual\_billings\_\_cpm
    - advertisement\_\_ad\_opportunity\_rules\_\_network\_id
    - advertisement\_\_ad\_opportunity\_rules\_\_rule\_id
    - advertisement\_\_ad\_opportunity\_rules\_\_total\_opp
    - candidate\_\_filter\_reason\_\_error
    - candidate\_\_filter\_reason\_\_slot\_index
    - candidate\_\_filter\_reason\_\_error\_category
    - candidate\_\_global\_agency\_ids
    - candidate\_\_ortb\_fwpartners\_\_idtype
    - candidate\_\_ortb\_fwpartners\_\_idvalue
    - auction\_\_impression\_\_index
    - auction\_\_impression\_\_slot\_index
    - auction\_\_impression\_\_error
    - auction\_\_impression\_\_equivalent\_opportunity\_number
    - auction\_\_impression\_\_max\_duration
    - auction\_\_impression\_\_bid\_floor
    - auction\_\_impression\_\_bid\_floor\_uplift
    - auction\_\_impression\_\_deals\_\_internal\_deal\_id
    - auction\_\_impression\_\_deals\_\_bid\_floor
    - auction\_\_impression\_\_deals\_\_bid\_floor\_uplift
    - auction\_\_impression\_\_matched\_inventory\_package\_ids
    - auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index
    - auction\_\_mkpl\_partner\_tags\_\_strategy
- Null SRC, 0 BCV
    - request\_\_client\_facing\_ivt\_reason\_flag
    - ack\_\_metrics\_\_ad\_impression
    - ack\_\_metrics\_\_no\_click
    - ack\_\_metrics\_\_first\_quartile
    - ack\_\_metrics\_\_middle\_quartile
    - ack\_\_metrics\_\_third\_quartile
    - ack\_\_metrics\_\_complete\_quartile
    - ack\_\_metrics\_\_can\_quartile
    - ack\_\_metrics\_\_measurable\_ad\_expand\_collapse\_impression
    - ack\_\_metrics\_\_measurable\_ad\_mute\_unmute\_impression
    - ack\_\_metrics\_\_measurable\_ad\_rewind\_impression
    - ack\_\_metrics\_\_measurable\_ad\_pause\_resume\_impression
    - ack\_\_metrics\_\_measurable\_ad\_close\_impression
    - ack\_\_metrics\_\_measurable\_ad\_accept\_invitation\_minimize\_impression
    - ack\_\_metrics\_\_video\_view
    - ack\_\_metrics\_\_click
    - ack\_\_metrics\_\_ad\_bid\_won
    - ack\_\_metrics\_\_ad\_insertion
    - ack\_\_metrics\_\_ad\_collapse
    - ack\_\_metrics\_\_ad\_mute
    - ack\_\_metrics\_\_ad\_unmute
    - ack\_\_metrics\_\_ad\_rewind
    - ack\_\_metrics\_\_ad\_pause
    - ack\_\_metrics\_\_ad\_resume
    - ack\_\_metrics\_\_ad\_close
    - ack\_\_metrics\_\_ad\_accept\_invitation
    - ack\_\_metrics\_\_ad\_minimize
    - ack\_\_metrics\_\_ad\_expand
    - ack\_\_metrics\_\_slot\_impression
    - ack\_\_metrics\_\_raw\_ad\_impression
    - ack\_\_metrics\_\_no\_ad\_impression
    - ack\_\_metrics\_\_break\_starts
    - ack\_\_metrics\_\_hylda\_replacement\_impression\_forfeits
    - ack\_\_metrics\_\_hylda\_replacement\_impression\_gains
    - ack\_\_metrics\_\_fire\_event\_revenue\_ratio
    - ack\_\_metrics\_\_fire\_event\_slot\_revenue\_ratio
    - ack\_\_metrics\_\_fire\_event\_bid\_revenue\_ratio
    - ack\_\_metrics\_\_fire\_margin\_ratio
    - ack\_\_metrics\_\_ad\_error
    - ack\_\_metrics\_\_numerator\_event\_count
    - ack\_\_metrics\_\_denominator\_event\_count
    - ack\_\_metrics\_\_indicator\_event\_count
    - ack\_\_metrics\_\_triggering\_ad\_views
    - ack\_\_metrics\_\_abstract\_event\_measurable\_ad\_views
    - ack\_\_metrics\_\_concrete\_event\_measurable\_ad\_views
    - ack\_\_metrics\_\_abstract\_event\_count
    - ack\_\_metrics\_\_concrete\_event\_count
    - ack\_\_metrics\_\_cpx\_targeted\_event\_count
    - ack\_\_metrics\_\_cpx\_revenue\_ratio
    - ack\_\_metrics\_\_cpx\_abstract\_currency\_ratio
    - ack\_\_metrics\_\_cpx\_targeted\_currency\_ratio
    - advertisement\_\_ad\_id
    - advertisement\_\_ad\_replica\_id
    - advertisement\_\_rendition\_id
    - advertisement\_\_flags
    - advertisement\_\_slot\_index
    - advertisement\_\_external\_reseller\_\_network\_id
    - advertisement\_\_external\_reseller\_\_revenue
    - advertisement\_\_external\_reseller\_\_up\_revenue
    - advertisement\_\_entity\_flags
    - advertisement\_\_targeting\_criteria\_id
    - advertisement\_\_duration
    - advertisement\_\_position\_in\_slot
    - advertisement\_\_abstract\_event\_id
    - advertisement\_\_triggering\_concrete\_event\_id
    - advertisement\_\_placement\_id
    - advertisement\_\_creative\_id
    - advertisement\_\_replaced\_ad\_id
    - advertisement\_\_replaced\_rendition\_id
    - advertisement\_\_inventory\_protection\_flags
    - advertisement\_\_io\_id
    - advertisement\_\_campaign\_id
    - advertisement\_\_ad\_unit\_id
    - advertisement\_\_replaced\_creative\_id
    - advertisement\_\_replaced\_ad\_unit\_id
    - advertisement\_\_advertiser\_id
    - advertisement\_\_agency\_id
    - advertisement\_\_insertion\_order\_id
    - advertisement\_\_extra\_flags
    - advertisement\_\_replaced\_ad\_network\_id
    - advertisement\_\_unified\_yield\_\_uplift\_ecpm
    - advertisement\_\_unified\_yield\_\_replaced\_entity\_id
    - advertisement\_\_unified\_yield\_\_uplift\_revenue
    - advertisement\_\_extra\_flags2
    - advertisement\_\_estimated\_start\_delay
    - advertisement\_\_replaced\_placement\_id
    - advertisement\_\_unified\_priority\_\_sub\_priority\_value
    - advertisement\_\_effective\_unified\_priority\_\_sub\_priority\_value
    - advertisement\_\_cch\_rendition\_id
    - advertisement\_\_replaced\_campaign\_id
    - advertisement\_\_replaced\_io\_id
    - advertisement\_\_market\_ad\_id
    - advertisement\_\_bid\_price\_to\_upstream
    - advertisement\_\_bit\_flags
    - advertisement\_\_replaced\_ad\_bit\_flags
    - advertisement\_\_rbp\_flag
    - advertisement\_\_ad\_oo\_network\_id
    - slot\_\_time\_position
    - slot\_\_ad\_unit\_id
    - slot\_\_max\_ads
    - slot\_\_flags
    - slot\_\_profile\_id
    - slot\_\_max\_duration
    - slot\_\_min\_duration
    - slot\_\_num\_ads
    - slot\_\_max\_ad\_duration
    - slot\_\_slot\_sequence
    - slot\_\_sequence
    - slot\_\_avails
    - slot\_\_break\_id
    - slot\_\_opportunity\_id
    - slot\_\_break\_display\_id
    - slot\_\_opportunity\_display\_id
    - slot\_\_time\_unfilled
    - slot\_\_unfilled\_avails
    - slot\_\_ad\_unit\_network\_id
    - slot\_\_ad\_unit\_default\_duration
    - slot\_\_carriage\_inventory\_owner\_id
    - slot\_\_carriage\_listing\_split\_unit\_num
    - slot\_\_initial\_time\_unfilled
    - slot\_\_initial\_unfilled\_avails
    - slot\_\_initial\_num\_ads
    - slot\_\_carriage\_listing\_origin\_split\_unit\_num
    - slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id
    - slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num
    - slot\_\_index
    - slot\_\_normalized\_ad\_unit\_id
    - slot\_\_parent\_time\_unfilled
    - candidate\_\_network\_id
    - candidate\_\_ad\_id
    - candidate\_\_original\_price
    - candidate\_\_raw\_price
    - candidate\_\_clearing\_price
    - candidate\_\_sfx\_buyer\_id
    - candidate\_\_sfx\_dsp\_id
    - candidate\_\_rtb\_auction\_index
    - candidate\_\_dsp\_id
    - candidate\_\_buyer\_platform\_id
    - candidate\_\_internal\_seat\_id
    - candidate\_\_buyer\_id
    - candidate\_\_buyer\_group\_id
    - candidate\_\_internal\_deal\_id
    - candidate\_\_dsp\_clearing\_price
    - candidate\_\_dsp\_currency\_id
    - candidate\_\_bid\_status
    - candidate\_\_media\_buyer\_id
    - candidate\_\_asset\_id
    - candidate\_\_site\_section\_id
    - candidate\_\_series\_id
    - candidate\_\_site\_id
    - candidate\_\_market\_ad\_id
    - candidate\_\_brand\_id
    - candidate\_\_advertiser\_id
    - candidate\_\_trading\_desk\_id
    - candidate\_\_bidding\_buyer\_id
    - candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate
    - candidate\_\_bidding\_seat\_id
    - candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value
    - candidate\_\_internal\_group\_deal\_id
    - candidate\_\_dsp\_clearing\_price\_discounted
    - candidate\_\_post\_auction\_discount\_id
    - candidate\_\_bit\_flags
    - candidate\_\_auction\_outbound\_bid\_floor
    - candidate\_\_discount\_post\_auction\_\_id
    - candidate\_\_discount\_post\_auction\_\_amount
    - candidate\_\_discount\_barter\_\_id
    - candidate\_\_discount\_barter\_\_amount
    - auction\_\_network\_id
    - auction\_\_dsp\_id
    - auction\_\_buyer\_platform\_id
    - auction\_\_flags
    - auction\_\_buyer\_group\_id
    - auction\_\_auction\_network\_to\_usd\_exchange\_rate
    - auction\_\_auction\_network\_to\_eur\_exchange\_rate
    - auction\_\_bid\_to\_usd\_exchange\_rate
    - auction\_\_asset\_id
    - auction\_\_site\_section\_id
    - auction\_\_series\_id
    - auction\_\_site\_id
    - auction\_\_auction\_status
    - auction\_\_bid\_throttling\_exempt\_ratio
    - auction\_\_bid\_throttling\_status
    - auction\_\_bid\_throttling\_info\_\_flags
    - auction\_\_bid\_throttling\_info\_\_exempt\_thousandth
    - auction\_\_auction\_sampling\_\_magnifier
    - auction\_\_auction\_sampling\_\_mode
    - auction\_\_invite\_deal\_size
- Null SRC, False BCV
    - advertisement\_\_matched\_daypart
    - advertisement\_\_is\_external
    - advertisement\_\_is\_replacement
    - advertisement\_\_is\_ax
    - advertisement\_\_is\_bumper
    - advertisement\_\_is\_undeliverable
    - advertisement\_\_is\_rbp
    - advertisement\_\_is\_fallback
    - advertisement\_\_is\_sstf\_fallback
    - advertisement\_\_is\_embedded\_tracking
    - advertisement\_\_is\_owned\_by\_cro
    - advertisement\_\_is\_uy\_replaced
    - advertisement\_\_has\_candidate

In addition to these there are a few that are one-offs:

- request\_\_backend\_filtration\_reason (0 SRC, null BCV)
- advertisement\_\_active\_term\_id (null SRC, empty list BCV)

**Recommendations**: 

- @Bhargava, Karan suggested not setting (leaving null) in Hoover to align with the Hoover++ behavior
- For the rest of the cases align with the Hoover behavior?

### Nulls in SRC

These are the fields that didn’t fall into the first case that were all null SRC values.  This is often indicative of fields that are not always set for Hoover but always set in Hoover++.

The only fields that met this criteria were `inventory__asset_chain*` and `inventory__site_section_chain*`.  A discussion of this is here: <https://freewheel.slack.com/archives/C01S31V42LX/p1782841339175119> 

And this was added to the known discrepancies: [Event Level (Backward Compatible Views)](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/605258221/Event+Level+Backward+Compatible+Views)

### Nulls in BCV

For these, fields values are coming in for Hoover but not BCV.

Most of the fields fitting this description are in partners which I will handle separately.  The remaining fields are:

| **Field name** | **SRC value** | **Reason/Fix** |
| --- | --- | --- |
| ~~request\_\_mrc\_compliance\_label~~ | `['OTT_CONTINUOUS_PLAY']` | Fix not needed |
| visitor\_\_user\_segments\_lookup\_key | `['37.222.97.0', '7e26e4e27164c12ff5d0e683de5c387a', 'google_dda71f0fc4e67920f806ea90130c5051ca343045', 'univid=-1']` | Privacy PR should fix |
| visitor\_\_identity\_user\_ids\_\_id | `['dda71f0fc4e67920f806ea90130c5051ca343045']` | Privacy PR should fix |
| - auction\_\_ab\_test\_items\_\_collection\_id - auction\_\_ab\_test\_items\_\_bucket\_id - auction\_\_ab\_test\_items\_\_is\_effective | `[65]` | Hardcoded to null: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L4438-L4442](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L4438-L4442)Could have to do with this isValidIndex check: <https://github.freewheel.tv/data/hoover-model/blob/34dfa65f1aaf651d1a9d3c2536cc89d368984d4d/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L264>No checks appear to be happening on the Hoover side |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | `[[None], [None], [None], [None], [None], [None]]``[]` | Always hardcoded null: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L4868](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L4868) |

### Partners array case

There are two overall trends with the discrepancies in the partner array case:

1. When there is an empty list in Hoover, this translates to None in BCV
    - This may be due to the checking present in Hoover++ not to set a field for instance here: <https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/slot/NetworkHandler.java#L73-L75>
2. When there is an array of None’s in Hoover, this translates to Null in BCV
    - This may be due to the fact that many fields are hard-coded to null in the Slot and Request BCV subqueries: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L6056-L6074](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L6056-L6074)

It is possible that these discrepancies do not matter since the data will ultimately be the same to the end-user

The rest of this analysis will concern exceptions to this.  To account for this and simplify my search I wrote the following code:

```py
start_partners_ind = 416
end_partners_ind = 670

def compare_partners(src_raw, bcv_raw):
    src_list = eval(src_raw.replace("`", ""))
    if bcv_raw == '*(null)*':
        try:
            if set(src_list) == {None} or set(src_list) == {0} or set(src_list) == {0.0}:
                return True
            else:
                return False
        except:
            return False
    else:
        bcv_list = eval(bcv_raw.replace("`", ""))
        return compare_partner_lists(src_list, bcv_list)

def compare_partner_lists(src_list, bcv_list):
    if len(src_list) != len(bcv_list):
        return False
    elif src_list == [] and bcv_list == []:
        return True
    else:
        elements_equal = []
        for i in range(len(src_list)):
            if type(src_list[i]) == list and type(bcv_list[i]) == list:
                elements_equal.append(compare_partner_lists(src_list[i], bcv_list[i]))
            else:
                if src_list[i] == bcv_list[i] or (src_list[i] == [] and bcv_list[i] == None):
                    elements_equal.append(True)
                else:
                    return False
    return min(elements_equal)
                
for i in range(start_partners_ind, end_partners_ind + 1):
    for data_record in report[i]["data"]:
        src_raw = data_record[0]
        bcv_raw = data_record[1]
        if not compare_partners(src_raw, bcv_raw):
            print(report[i]["field_name"])
            print(src_raw)
            print(bcv_raw)
            print()
            break
```

When running this code it left me with a few fields left that did not meet this criteria.  I summarize these fields below:

*Highlighted in green are the fields proposed where no changes are needed*

| **Reason** | **Fields** | **Example** | **Fix** |
| --- | --- | --- | --- |
| Off by scaling | - partners\_\_avails\_category\_\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_total\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot - partners\_\_avails\_category\_\_opportunity\_in\_played\_slot - partners\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | `[1, 1, 1] ->` `[100, 100, 100]` | Remove multiplier multiplication in Hoover++ |
| Zero skipped | - partners\_\_avails\_category\_\_avails - partners\_\_avails\_category\_\_unfilled\_avails | `[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ->` `[1]` | @Wang, Yu explained that only a subset is now required in Hoover++ and this is expected |
| Zero for none | - partners\_\_programmatic\_exchange\_rate\_to\_usd - partners\_\_programmatic\_exchange\_rate\_to\_eur | `[1.0, 1.0, 0.0] ->` `[1.0, 1.0, None]` | Difference here: <https://github.freewheel.tv/data/etl/blob/master/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L703-L707><https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/AdHandler.java#L682-L686> |
| Bit flag discrepancies | partners\_\_bit\_flags | `[2097152, 16777216, 162129586618892320, 0] ->` `[2097152, 16777216, 18014398543036448, 0]` | Due to IVT bit flag |
| Eligible outbound order nulls | - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails - partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot - partners\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked - partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration - partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration - partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp - partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num - partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | `[[0, 0], [0, None, None, None, None, None, None, None, None, None, None, None, None, 0, 0, 0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] -> Null` | Difference here:<https://github.freewheel.tv/data/hoover-model/blob/f218b06085ddfa339519cc36504c4e5c04a855f8/src/main/java/tv/freewheel/hoover/entity/slot/NetworkHandler.java#L112-L116><https://github.freewheel.tv/data/etl/blob/00a40b7e8c7500045c34c091276ed32fd9a8b4b1/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/SlotHandler.java#L153-L156>Improvement? |
| Audience partner segment nulls | - partners\_\_audience\_segment\_max\_cpm - partners\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id - partners\_\_audience\_partner\_segment\_infos\_\_max\_cpm - partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id - partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | Null for BCV | Not set in view: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L1529-L1535](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L1529-L1535) |
| Misc null | - partners\_\_rule\_ext\_id - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | Null for BCV | [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L6003](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L6003)[https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L6207](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L6207) |
| listing\_id null | partners\_\_listing\_id | `[[251473, 281474, 281476, 287706, 340702, 467763, 467764, 467765, 470804, 470805, 470806, 691103, 691791, 107966, 108646, 123711, 130392, 153538, 190117, 240922, 240924, 243965, 251470, 257382, 276631, 281473, 287702, 328692, 344829, 360294, 360296, 378919, 601857, 651324, 685111], None, None] -> Null` | Difference in condition:<https://github.freewheel.tv/data/etl/blob/00a40b7e8c7500045c34c091276ed32fd9a8b4b1/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/SlotHandler.java#L149><https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/slot/NetworkHandler.java#L105-L107> |
| raw\_opportunity\_in\_played\_slot None array and null | partners\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] -> [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]` | Looks like it is not actually being set?<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/slot/NetworkHandler.java#L657-L695> |
| network\_execution\_ctx\_index null | partners\_\_network\_execution\_ctx\_index | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] -> Null` | Hard-coded to null most of the time:[https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L6131](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L6131) |
| outbound\_exchange\_order\_ids extra values in BCV | partners\_\_outbound\_exchange\_order\_ids | `[None, None, None] -> [119932, None, None]` | Logic is very different but BCV is simpler and tends to have more values - use this one?<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/ad/AdNetworkHandler.java#L714C13-L714C42><https://github.freewheel.tv/data/etl/blob/00a40b7e8c7500045c34c091276ed32fd9a8b4b1/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AdvertisementHandler.java#L758> |

### ad\_in\_slot fields

Similar to partners, there are several common patterns in the discrepancies:

- Often times when there is an empty list in Hoover, this translates to None in BCV
- When SRC is an empty list then BCV is Null
- When SRC is null BCV is some list value (new one)

This is captured in the following code:

```py
from compare_partners import compare_partner_lists

start_ad_in_slot_ind = 754
end_ad_in_slot_ind = len(report) - 1

def compare_ad_in_slot(src_raw, bcv_raw):
    if src_raw == '*(null)*':
        try:
            bcv = eval(bcv_raw.replace("`", ""))
            if type(bcv) == list:
                return True
            else:
                return False
        except:
            return False
    else:
        src = eval(src_raw.replace("`", ""))
        if src == [] and bcv_raw == '*(null)*':
            return True
        else:
            try:
                bcv = eval(bcv_raw.replace("`", ""))
                return compare_partner_lists(src, bcv)
            except:
                return False

for i in range(start_ad_in_slot_ind, end_ad_in_slot_ind + 1):
    for data_record in report[i]["data"]:
        src_raw = data_record[0]
        bcv_raw = data_record[1]
        if not compare_ad_in_slot(src_raw, bcv_raw):
            print(report[i]["field_name"])
            print(src_raw)
            print(bcv_raw)
            print()
            break
```

Below are the fields which are exceptions to these rules:

| **Field name** | **SRC value** | **BCV value** | **Reason** |
| --- | --- | --- | --- |
| ads\_in\_slot\_\_advertisement\_\_has\_candidate | `[None]` | `[False]` | None is used instead of false in Hoover++:[https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260708204354\_618498&externalid=20260708\_204359\_00012\_gixvt](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260708204354_618498&externalid=20260708_204359_00012_gixvt)Always boolean in Hoover++<https://github.freewheel.tv/data/hoover-model/blob/b7d29a0e046bddb2629e96f2b342d84ffe3a44ca/src/main/java/tv/freewheel/hoover/entity/AdHandler.java#L188> |
| ads\_in\_slot\_\_auction\_\_impression\_\_error | `[['IMPRESSION_NO_BIDS'], []]` | `[[None], None]` | Error does not appear to ever be set: <https://github.freewheel.tv/data/hoover-model/blob/34dfa65f1aaf651d1a9d3c2536cc89d368984d4d/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L595-L621> |
| ads\_in\_slot\_\_auction\_\_invite\_deal\_size | `[1, None]` | `[1, 0]` | Set to 0 if null in hpp: <https://github.freewheel.tv/data/hoover-model/blob/34dfa65f1aaf651d1a9d3c2536cc89d368984d4d/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L403-L406>Set even if value is null: <https://github.freewheel.tv/data/etl/blob/967cc07dcfdc38df6fe792be397227f6a6311574/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/AuctionHandler.java#L271> |
| ads\_in\_slot\_\_candidate\_\_order\_id | `[None, 307425]` | `[None, None]` |  |
| ads\_in\_slot\_\_candidate\_\_advertisement\_index | `[0, 1]` | `[None, None]` | Set in Hoover Generator in Hoover: <https://github.freewheel.tv/data/etl/blob/ff2c36f5200077474c265ce34bb12b92d1a680ff/etl-schema-hoover/src/main/java/tv/freewheel/hoover/avro/HooverGenerator.java#L527>Set in CandidateHandler in Hoover++<https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/CandidateHandler.java#L387>may be some differences in the conditions here |
| ads\_in\_slot\_\_partners\_\_programmatic\_exchange\_rate\_to\_usd | `[[0.0, 0.0]]` | `[[None, None]]` | Default value of 0.0: <https://github.freewheel.tv/data/etl/blob/dae3793fc70c1b03cccd848865c85128fa5937aa/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/PartnerHandler.java#L41-L42> |
| ads\_in\_slot\_\_partners\_\_programmatic\_exchange\_rate\_to\_eur | `[[0.0, 0.0]]` | `[[None, None]]` | Default value of 0.0: <https://github.freewheel.tv/data/etl/blob/dae3793fc70c1b03cccd848865c85128fa5937aa/etl-schema-hoover/src/main/java/tv/freewheel/hoover/entity/PartnerHandler.java#L41-L42> |
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | `[[None, None]]` | Null | Addressed above multiple times ^ not even the right data type |

### Rest of fields

With the fields above that I have covered, this accounts for 1105/1115 or 99% of the mismatched fields.  Here are the remaining fields:

*Highlighted in green are the fields proposed where no changes are needed*

| **Field name** | **SRC value** | **BCV value** | **Reason/Fix** |
| --- | --- | --- | --- |
| - ~~request\_\_timestamp~~ - ~~ack\_\_timestamp~~ | `2026-06-28 16:35:34` | `2026-06-28 12:35:34-04:00` | Remove the timezone in BCV |
| request\_\_flags |  |  | Align flags between the two |
| visitor\_\_identity\_user\_ids\_\_authorized\_network\_id | `[[], [], []]` | `[None, None, None]` | Hoover++ only set if non-empty: <https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/VisitorHandler.java#L240-L246> |
| - advertisement\_\_rules\_\_network\_id - advertisement\_\_rules\_\_opp\_rule\_id - advertisement\_\_rules\_\_win\_rule\_id - advertisement\_\_measurable\_concrete\_event\_id | `[]`Null | Null`[]` | Same thing for ad\_in\_slotFigure out why |
| candidate\_\_order\_id | Null`203256` | 0Null | 1. Hardcoded in BCV SQL to 0: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L4387](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L4387) 2. Doesn’t appear to be set in Hoover++: <https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/CandidateHandler.java> |
| candidate\_\_advertisement\_index | Null`1` | 0Null | 1. Hardcoded in BCV SQL to 0: [https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs\_views/Ack\_Complete.sql#L4388](https://github.freewheel.tv/data/hoover-model/blob/master/views/lqs_views/Ack_Complete.sql#L4388) 2. Set in Hoover Generator in Hoover: <https://github.freewheel.tv/data/etl/blob/ff2c36f5200077474c265ce34bb12b92d1a680ff/etl-schema-hoover/src/main/java/tv/freewheel/hoover/avro/HooverGenerator.java#L527>     Set in CandidateHandler in Hoover++     <https://github.freewheel.tv/data/hoover-model/blob/master/src/main/java/tv/freewheel/hoover/entity/CandidateHandler.java#L387>     may be some differences in the conditions here |

### Summary/Action Items

1. Null handling
    1. Align Hoover with stricter BCV patterns
    2. Align on what we want to do for default values (0, False) vs just leaving null
2. Nulls in BCV
    1. Fix Hoover++ implementation of auction\_\_ab\_test\_items\*
    2. Fix Hoover++ implementation of ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics
3. Partners array
    1. Align on what we want to do for the \[\] → None discrepancy
    2. Fix fields which have substantial discrepancies
4. Ad in slot fields
    1. Overarching fix: understand why there are values coming in when SRC is null
    2. Fix fields which have other discrepancies
5. Remaining fields
    1. ~~request\_\_timestamp~~
    2. ~~ack\_\_timestamp~~
    3. request\_\_flags
    4. candidate\_\_order\_id
    5. candidate\_\_advertisement\_index

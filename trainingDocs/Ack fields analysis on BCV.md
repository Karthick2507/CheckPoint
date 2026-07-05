# Ack fields analysis on BCV

For the fields that are matched here are the type differences:

Highlighted in red are the type differences that aren’t as simple as Int → Long

| Column Name | SRC Type | BCV Type |
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
| ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | array(array(array(array(varchar)))) | array(array(array(varchar)) |
| ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts | array(array(array(varchar))) | array(array(varchar)) |

## Fields missing in BCV view

Below are the fields which were not matched and had some downstream usage:

*following thresholds: ETL = Y OR SOS = Y OR Insights \> 0 OR Arena \> 0 OR LQS ≥ 10 OR CP \> 0 OR AF \> 0 OR Others ≥ 100)  AND  size \< 0.03 TiB (or unknown)*

Highlighted in red are fields which can be excluded

Highlighted in yellow are fields which probably can be excluded

The rest have enough usages that we probably need to migrate them all to the new view

| Column Name | **Usage: ETL** | **Usage: SOS** | **Usage: Insights** | **Usage: Arena** | **Usage: LQS** | **Usage: CP** | **Usage: Other** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| request\_\_context\_\_extracted\_key\_value |  |  |  |  | 303 |  |  |  |
| request\_\_context\_\_extracted\_key\_value\_\_\_fw\_dbp |  |  |  |  | 116 | 5655 | 181 |  |
| request\_\_context\_\_extracted\_key\_value\_\_\_fw\_lto |  |  |  |  |  | 167 |  |  |
| request\_\_request\_throttling\_info\_\_model\_info\_\_model\_id |  |  |  |  | 13 |  |  | looks legit: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260626173401\_074336&externalid=20260626\_173403\_00103\_ytfr8](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260626173401_074336&externalid=20260626_173403_00103_ytfr8) |
| request\_\_client\_facing\_reason\_code | Y |  |  |  | 4 |  | 1 |  |
| request\_\_bid\_request\_\_impression\_\_deal\_\_floor |  |  |  |  | 12 |  |  | confirmed this is not needed |
| inventory\_\_asset\_chain\_\_reseller\_network\_id | Y |  |  |  | 5 |  |  |  |
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
| ack\_\_ack\_entity\_type | Y | Y | 143351 | 1177 | 1062 | 167 | 60 |  |
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
| ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_aggregate | Y | Y |  |  |  |  |  |  |
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

In this comparison, I compared 100 ack records between Hoover and Hoover++.  Attached the the page are the analysis results.

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
- List of None SRC, null BCV
    - partners\_\_reseller\_network\_id
    - partners\_\_revenue
    - partners\_\_content\_owner\_revenue
    - partners\_\_distributor\_revenue
    - partners\_\_reseller\_revenue
    - partners\_\_bidding\_revenue
    - partners\_\_bidding\_up\_revenue
    - partners\_\_content\_owner\_bidding\_revenue
    - partners\_\_content\_owner\_bidding\_modified\_revenue
    - partners\_\_content\_owner\_bidding\_original\_revenue
    - partners\_\_distributor\_bidding\_revenue
    - partners\_\_reseller\_bidding\_revenue
    - partners\_\_ssp\_clearing\_revenue
    - partners\_\_margin
    - partners\_\_competition\_resellers
    - partners\_\_rule\_id
    - partners\_\_rule\_flags
    - partners\_\_rule\_type\_priority
    - partners\_\_unified\_rule\_priority\_\_priority\_tier
    - partners\_\_unified\_rule\_priority\_\_sub\_priority\_value
    - partners\_\_site\_group\_id
    - partners\_\_airing\_channel\_group\_id
    - partners\_\_edge\_postal\_code\_package\_ids
    - partners\_\_inbound\_rule\_id
    - partners\_\_upstream\_inbound\_order\_id
    - partners\_\_upstream\_global\_currency\_id
    - partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency
    - partners\_\_outbound\_order\_id
    - partners\_\_outbound\_order\_type
    - partners\_\_outbound\_exchange\_order\_id
    - partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier
    - partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value
    - partners\_\_outbound\_order\_transaction\_type
    - partners\_\_outbound\_order\_priority\_type
    - partners\_\_avails\_category\_\_unconstrained\_avails
    - partners\_\_avails\_category\_\_market\_avails
    - partners\_\_avails\_category\_\_ssp\_avails
    - partners\_\_avails\_category\_\_market\_avails\_in\_played\_slot
    - partners\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot
    - partners\_\_avails\_category\_\_total\_avails
    - partners\_\_avails\_category\_\_total\_unfilled\_avails
    - partners\_\_avails\_category\_\_opportunity
    - partners\_\_avails\_category\_\_remaining\_avails
    - partners\_\_avails\_category\_\_distinct\_inventory\_avails
    - partners\_\_avails\_category\_\_inventory\_avails
    - partners\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot
    - partners\_\_outbound\_rules\_\_rule\_id
    - partners\_\_outbound\_rules\_\_total\_opp
    - partners\_\_outbound\_rules\_\_win\_opp
    - partners\_\_outbound\_exchange\_listings\_\_listing\_ids
    - partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration
    - partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity
    - partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails
    - partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails
    - partners\_\_network\_is\_ad\_unit\_owner
    - partners\_\_network\_is\_vod\_programmer
    - partners\_\_count\_imp\_as\_booked
    - partners\_\_ad\_priority\_bucket
    - partners\_\_supply\_source\_type
    - partners\_\_global\_currency\_id
    - partners\_\_floor\_price
    - partners\_\_ad\_unit\_default\_duration
    - partners\_\_ad\_filling\_status\_\_available\_duration
    - partners\_\_ad\_filling\_status\_\_filled\_ad\_num
    - partners\_\_ad\_filling\_status\_\_filled\_duration
    - partners\_\_ad\_filling\_status\_\_unified\_unfilled\_opp
    - partners\_\_ad\_filling\_status\_\_default\_unfilled\_opp
    - partners\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num
    - partners\_\_ad\_filling\_status\_\_initial\_filled\_duration
    - partners\_\_priority\_tier
    - partners\_\_priority\_value
    - partners\_\_priority\_type
    - partners\_\_supply\_acquisition\_cost
    - partners\_\_supply\_distribution\_cost
    - partners\_\_internal\_deal\_ids
    - partners\_\_inbound\_order\_ids
    - partners\_\_buyer\_ids
    - partners\_\_internal\_seat\_ids
    - partners\_\_outbound\_order\_ids
    - partners\_\_matched\_yield\_optimization\_ids
    - partners\_\_selected\_yield\_optimization\_ids
    - partners\_\_matched\_inventory\_package\_ids
    - partners\_\_matched\_audience\_item\_ids
    - partners\_\_matched\_key\_value\_ids
    - partners\_\_matched\_daypart
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name
    - partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value
    - partners\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id
    - partners\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id
    - partners\_\_mapped\_asset\_ids
    - partners\_\_mapped\_site\_section\_ids
    - partners\_\_selected\_yo\_distribution\_id
    - partners\_\_selected\_yo\_distribution\_nip\_id
    - partners\_\_selected\_yo\_inventory\_prioritization\_id
    - partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id
    - partners\_\_selected\_yo\_margin\_id
    - partners\_\_geo\_visibility\_\_targetable
    - partners\_\_geo\_visibility\_\_report\_aggregate
    - partners\_\_geo\_visibility\_\_report\_event
    - auction\_\_ab\_test\_items\_\_is\_effective
    - ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics

In addition to these there are a few that are one-offs:

- request\_\_backend\_filtration\_reason (0 SRC, null BCV)
- advertisement\_\_active\_term\_id (null SRC, empty list BCV)

**Recommendation**: align the null-handling behavior for these fields in the view

### Nulls in SRC

These are the fields that didn’t fall into the first case that were all null SRC values.  This is often indicative of fields that are not always set for Hoover but always set in Hoover++.

The only fields that met this criteria were `inventory__asset_chain*` and `inventory__site_section_chain*`.  A discussion of this is here: <https://freewheel.slack.com/archives/C01S31V42LX/p1782841339175119> 

And this was added to the known discrepancies: Event Level (Backward Compatible Views)

### Nulls in BCV

# Hoover\+\+ Validations Event Level

# Introduction

We're getting to a point where we're starting to get ready to validate `event-level`  data between Hoover \<\> Hoover++

The initial work of having the data available in 1 centralized location has been done by the `LQS`  team. We are able to see the current hoover model tables under `mrm_log_flat`  and the new Hoover++ model tables under `hoover_delta`  (hoover\_batch for compacted tables, hoover\_streaming for non-compacted tables)

We also have built `backward compatible views`  using this Hoover++ data that are available in LQS under `etl.public_test1` . 

Using the above information, we'll compare event-level on how data looks between the new model and the old model

| **Table Name** | **Current Hoover Model** | **Hoover++ Model** | **Comments** |
| --- | --- | --- | --- |
| ack | mrm\_log\_flat.default.ack | etl.public\_test1.ack | Since in Hoover++ acks are in 3 locations, there are also entity level ack tablesrequest\_ack, slot\_ack and ad\_ack (also under the same location) |
| ad | mrm\_log\_flat.default.ad | etl.public\_test1.ad |  |
| auction | mrm\_log\_flat.default.auction | etl.public\_test1.auction |  |
| candidate | mrm\_log\_flat.default.candidate | etl.public\_test1.candidate |  |
| request | mrm\_log\_flat.default.request | etl.public\_test1.request |  |
| slot | mrm\_log\_flat.default.slot | etl.public\_test1.slot |  |

If you see things that are WRONG in the SQLs in the Hoover++ model, the code is in the below repo.

[https://github.freewheel.tv/data/hoover-model/tree/master/views/lqs\_views](https://github.freewheel.tv/data/hoover-model/tree/master/views/lqs_views)

# Important things to know

We want to compare the same data between mrm\_log\_flat.default schema and hoover\_delta schema. 

With the help of Peng and Di Wu's team, we have the same source of data between the 2. The same sampled data is used to build the Hoover++ data.

We can get the same sampled data by adding the below flag check:

```
and bitwise_and(request__bit_flags, 576460752303423488) > 0 -- is sampled
```

This is a check for 1 \<\< 59 which is the sampled flag.

# Running Comparisons

Sample query for mrm\_log\_flat.default.request → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260424180626\_914359&externalid=20260424\_180629\_00248\_ypz9x](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260424180626_914359&externalid=20260424_180629_00248_ypz9x)

Similar query using Hoover++ data → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260424180633\_770472&externalid=20260424\_180655\_00250\_ypz9x](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260424180633_770472&externalid=20260424_180655_00250_ypz9x)

To speed up the comparisons we need to add the partition keys for each.

| **Catalog** | **Partition key** | **Comments** |
| --- | --- | --- |
| mrm\_log\_flat.default | process\_batch\_id |  |
| etl.public\_test1.request | event\_hour |  |

We can even use the underlying table to compare (if we don't want to use the view; though it's easier using the view)

Hoover batch query → [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260424181602\_334166&externalid=20260424\_181623\_00257\_ypz9x](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260424181602_334166&externalid=20260424_181623_00257_ypz9x)

# Key Fields to Compare

Going entity by entity, here are some key fields we should validate.

### Request

| **Entity** | **Column** | **Comments** |
| --- | --- | --- |
| request | request\_\_transaction\_id |  |
| request | request\_\_context\_\_network\_id |  |
| request | request\_\_context\_\_profile\_id |  |
| request | request\_\_context\_\_standard\_endpoint\_id |  |
| request | request\_\_log\_sampling\_\_magnifier |  |
| request | request\_\_log\_sampling\_\_mode |  |
| request | request\_\_magnifier |  |
| request | request\_\_is\_filtered |  |
| request | request\_\_is\_first\_user\_visitor |  |
| request | request\_\_is\_no\_selection |  |
| request | request\_\_is\_ssp\_bidder\_request |  |
| request | request\_\_context\_\_profile\_type |  |
| request | request\_\_context\_\_request\_format |  |
| request | request\_\_context\_\_response\_format |  |
| request | request\_\_context\_\_stream\_mode\_id |  |
| request | request\_\_context\_\_stream\_mode\_ids |  |
| request | request\_\_context\_\_tv\_network\_id |  |
| request | request\_\_context\_\_site\_section\_cro\_network\_id |  |
| request | request\_\_context\_\_video\_cro\_network\_id |  |
| request | request\_\_context\_\_standard\_programmer\_id |  |
| request | request\_\_context\_\_standard\_publisher\_id |  |
| request | request\_\_context\_\_standard\_site\_domain\_id |  |
| request | request\_\_context\_\_standard\_ssp\_channel\_id |  |
| request | request\_\_context\_\_time\_position |  |
| request | request\_\_context\_\_request\_duration |  |
| request | request\_\_context\_\_ab\_test\_item\_\_bucket\_id |  |
| request | request\_\_context\_\_ab\_test\_item\_\_collection\_id |  |
| request | request\_\_yield\_optimization\_ids |  |
| request | request\_\_privacy\_info\_\_compliance\_flag |  |
| request | request\_\_privacy\_info\_\_gdpr\_flag |  |
| request | request\_\_privacy\_info\_\_impacted\_features\_flag |  |
| request | request\_\_privacy\_jurisdiction\_ids |  |
| request | request\_\_is\_data\_right\_enabled |  |
| request | request\_\_flags |  |
| request | request\_\_extra\_flags |  |
| request | request\_\_extra\_flags2 |  |
| request | request\_\_backend\_filtration\_reason |  |
| request | request\_\_client\_facing\_ivt\_reason\_flag |  |
| request | request\_\_client\_facing\_reason\_code |  |
| request | request\_\_decision\_info\_\_flag1 |  |
| request | request\_\_decision\_info\_\_value4 |  |
| request | request\_\_decision\_info\_\_value5 |  |
| request | request\_\_decision\_info\_\_value6 |  |
| request | request\_\_decision\_info\_\_value7 |  |
| request | request\_\_decision\_info\_\_value9 |  |
| request | request\_\_request\_prefilter\_\_flag |  |
| request | request\_\_request\_throttling\_infoflags |  |
| request | request\_\_request\_throttling\_infolevel |  |
| request | request\_\_prebid\_sivt\_\_sivt\_model |  |
| request | request\_\_prebid\_sivt\_\_whiteops\_sivt\_reason |  |
| request | request\_\_prebid\_sivt\_\_inhouse\_sivt\_reason |  |

### Visitor

| **Entity** | **Column** | **Comments** |
| --- | --- | --- |
| visitor | visitor\_\_user\_id |  |
| visitor | visitor\_\_cookie\_user\_id |  |
| visitor | visitor\_\_custom\_user\_id |  |
| visitor | visitor\_\_server\_side\_user\_id |  |
| visitor | visitor\_\_household\_id |  |
| visitor | visitor\_\_universal\_hhid |  |
| visitor | visitor\_\_universal\_iids |  |
| visitor | visitor\_\_device\_id |  |
| visitor | visitor\_\_device\_type |  |
| visitor | visitor\_\_country\_id |  |
| visitor | visitor\_\_country |  |
| visitor | visitor\_\_state\_id |  |
| visitor | visitor\_\_state |  |
| visitor | visitor\_\_dma\_code\_id |  |
| visitor | visitor\_\_dma\_code |  |
| visitor | visitor\_\_city\_id |  |
| visitor | visitor\_\_city |  |
| visitor | visitor\_\_postal\_code\_id |  |
| visitor | visitor\_\_postal\_code |  |
| visitor | visitor\_\_platform\_group |  |
| visitor | visitor\_\_platform\_device\_id |  |
| visitor | visitor\_\_platform\_os\_id |  |
| visitor | visitor\_\_platform\_browser\_id |  |
| visitor | visitor\_\_user\_agent |  |
| visitor | visitor\_\_parsed\_user\_agent |  |
| visitor | visitor\_\_user\_agent\_device\_type |  |
| visitor | visitor\_\_tracked\_audience\_item\_ids |  |
| visitor | visitor\_\_tracked\_term |  |
| visitor | visitor\_\_identity\_user\_ids |  |
| visitor | visitor\_\_filtration\_reason |  |
| visitor | visitor\_\_flags |  |
| visitor | visitor\_\_internal\_address |  |
| visitor | visitor\_\_address |  |
| visitor | visitor\_\_peer\_address |  |
| visitor | visitor\_\_timezone |  |
| visitor | visitor\_\_timezone\_offset |  |

### Slot

| **Entity** | **Column** | **Status** | **Comments** |
| --- | --- | --- | --- |
| slot | slot\_\_index |  | slot\_index: hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=tableschema&queryid=presto\_20260512201524\_436164&externalid=20260512\_201526\_00007\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=tableschema&queryid=presto_20260512201524_436164&externalid=20260512_201526_00007_etzx5) hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512201726\_947657&externalid=20260512\_201759\_00009\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512201726_947657&externalid=20260512_201759_00009_etzx5) |
| slot | slot\_\_slot\_sequence |  | slot\_\_slot\_sequence: hoover: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512202827\_194982&externalid=20260512\_202828\_00025\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512202827_194982&externalid=20260512_202828_00025_etzx5) hoover++: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512202833\_974883&externalid=20260512\_202908\_00588\_qk7z5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512202833_974883&externalid=20260512_202908_00588_qk7z5) |
| slot | slot\_\_sequence |  | slot\_\_sequence: [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512203805\_564747](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512203805_564747) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512203941\_336959&externalid=20260512\_204010\_00033\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512203941_336959&externalid=20260512_204010_00033_etzx5) |
| slot | slot\_\_slot\_id |  | Not available |
| slot | slot\_\_break\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512204138\_471857&externalid=20260512\_204139\_00034\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512204138_471857&externalid=20260512_204139_00034_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512204726\_865702&externalid=20260512\_204801\_00036\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512204726_865702&externalid=20260512_204801_00036_etzx5) |
| slot | slot\_\_opportunity\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512204818\_676797&externalid=20260512\_204820\_00037\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512204818_676797&externalid=20260512_204820_00037_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512204839\_790835&externalid=20260512\_204908\_00038\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512204839_790835&externalid=20260512_204908_00038_etzx5) |
| slot | slot\_\_ad\_unit\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512204925\_635940&externalid=20260512\_204927\_00039\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512204925_635940&externalid=20260512_204927_00039_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205106\_001972&externalid=20260512\_205137\_00041\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205106_001972&externalid=20260512_205137_00041_etzx5) |
| slot | slot\_\_ad\_unit\_network\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205420\_936783&externalid=20260512\_205421\_00045\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205420_936783&externalid=20260512_205421_00045_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205416\_247946&externalid=20260512\_205447\_00046\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205416_247946&externalid=20260512_205447_00046_etzx5) |
| slot | slot\_\_normalized\_ad\_unit\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205504\_345343&externalid=20260512\_205505\_00047\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205504_345343&externalid=20260512_205505_00047_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205509\_924344&externalid=20260512\_205538\_00048\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205509_924344&externalid=20260512_205538_00048_etzx5) |
| slot | slot\_\_max\_ads |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205822\_823754&externalid=20260512\_205824\_00053\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205822_823754&externalid=20260512_205824_00053_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205827\_455122&externalid=20260512\_205856\_00055\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205827_455122&externalid=20260512_205856_00055_etzx5) |
| slot | slot\_\_num\_ads |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205913\_318186&externalid=20260512\_205915\_00056\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205913_318186&externalid=20260512_205915_00056_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512205917\_131628&externalid=20260512\_205949\_00059\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512205917_131628&externalid=20260512_205949_00059_etzx5) |
| slot | slot\_\_max\_duration |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210014\_655232&externalid=20260512\_210022\_00060\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210014_655232&externalid=20260512_210022_00060_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210322\_387051&externalid=20260512\_210356\_00064\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210322_387051&externalid=20260512_210356_00064_etzx5) |
| slot | slot\_\_min\_duration |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210115\_118369&externalid=20260512\_210116\_00061\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210115_118369&externalid=20260512_210116_00061_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210329\_389563&externalid=20260512\_210355\_00063\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210329_389563&externalid=20260512_210355_00063_etzx5) |
| slot | slot\_\_initial\_time\_unfilled |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210349\_734824&externalid=20260512\_210350\_00062\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210349_734824&externalid=20260512_210350_00062_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210737\_120622&externalid=20260512\_210810\_00069\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210737_120622&externalid=20260512_210810_00069_etzx5) |
| slot | slot\_\_time\_unfilled |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210425\_884279&externalid=20260512\_210426\_00065\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210425_884279&externalid=20260512_210426_00065_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210744\_136707&externalid=20260512\_210809\_00068\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210744_136707&externalid=20260512_210809_00068_etzx5) |
| slot | slot\_\_avails |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210517\_351999&externalid=20260512\_210518\_00066\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210517_351999&externalid=20260512_210518_00066_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211443\_219161&externalid=20260512\_211519\_00080\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211443_219161&externalid=20260512_211519_00080_etzx5) |
| slot | slot\_\_unfilled\_avails |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210800\_522084&externalid=20260512\_210801\_00067\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210800_522084&externalid=20260512_210801_00067_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211450\_493659&externalid=20260512\_211518\_00079\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211450_493659&externalid=20260512_211518_00079_etzx5) |
| slot | slot\_\_time\_position |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210836\_996740&externalid=20260512\_210837\_00070\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210836_996740&externalid=20260512_210837_00070_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211708\_054309&externalid=20260512\_211742\_00084\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211708_054309&externalid=20260512_211742_00084_etzx5) |
| slot | slot\_\_avails\_metrics\_\_opportunity |  | Array: null vs \[\][https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212008\_524802&externalid=20260512\_212010\_00090\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212008_524802&externalid=20260512_212010_00090_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212411\_977759&externalid=20260512\_212442\_00095\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212411_977759&externalid=20260512_212442_00095_etzx5) |
| slot | slot\_\_avails\_metrics\_\_avails |  | Array: null vs \[\][https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212148\_464483&externalid=20260512\_212149\_00093\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212148_464483&externalid=20260512_212149_00093_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212449\_793178&externalid=20260512\_212522\_00097\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212449_793178&externalid=20260512_212522_00097_etzx5) |
| slot | slot\_\_avails\_metrics\_\_unfilled\_avails |  | Array: null vs \[\][https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212309\_245039&externalid=20260512\_212311\_00094\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212309_245039&externalid=20260512_212311_00094_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212459\_692845&externalid=20260512\_212521\_00096\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212459_692845&externalid=20260512_212521_00096_etzx5) |
| slot | slot\_\_time\_position\_class |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512210950\_286303&externalid=20260512\_210951\_00073\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512210950_286303&externalid=20260512_210951_00073_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211827\_539924&externalid=20260512\_211900\_00085\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211827_539924&externalid=20260512_211900_00085_etzx5) |
| slot | slot\_\_environment |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211434\_838370&externalid=20260512\_211435\_00077\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211434_838370&externalid=20260512_211435_00077_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211938\_609867&externalid=20260512\_212009\_00089\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211938_609867&externalid=20260512_212009_00089_etzx5) |
| slot | slot\_\_profile\_id |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211516\_915630&externalid=20260512\_211518\_00078\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211516_915630&externalid=20260512_211518_00078_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211946\_682984&externalid=20260512\_212008\_00088\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211946_682984&externalid=20260512_212008_00088_etzx5) |
| slot | slot\_\_flags |  | [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512211556\_444104&externalid=20260512\_211557\_00082\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512211556_444104&externalid=20260512_211557_00082_etzx5) [https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto\_20260512212116\_463759&externalid=20260512\_212147\_00092\_etzx5](https://lqs.fwmrm.net/#datasource=prd-internal-presto&engine=presto&tab=result&queryid=presto_20260512212116_463759&externalid=20260512_212147_00092_etzx5) |

### Ad

| **Entity** | **Columns** | **Comments** |
| --- | --- | --- |
| advertisement | advertisement\_\_ad\_id |  |
| advertisement | advertisement\_\_ad\_replica\_id |  |
| advertisement | advertisement\_\_rendition\_id |  |
| advertisement | advertisement\_\_creative\_id |  |
| advertisement | advertisement\_\_placement\_id |  |
| advertisement | advertisement\_\_campaign\_id |  |
| advertisement | advertisement\_\_io\_id |  |
| advertisement | advertisement\_\_insertion\_order\_id |  |
| advertisement | advertisement\_\_ad\_oo\_network\_id |  |
| advertisement | advertisement\_\_ad\_unit\_id |  |
| advertisement | advertisement\_\_advertiser\_id |  |
| advertisement | advertisement\_\_agency\_id |  |
| advertisement | advertisement\_\_global\_advertiser\_ids |  |
| advertisement | advertisement\_\_global\_brand\_ids |  |
| advertisement | advertisement\_\_global\_industry\_ids |  |
| advertisement | advertisement\_\_duration |  |
| advertisement | advertisement\_\_ad\_delivery\_method |  |
| advertisement | advertisement\_\_linear\_decision\_type |  |
| advertisement | advertisement\_\_placement\_type\_priority |  |
| advertisement | advertisement\_\_inventory\_protection\_flags |  |
| advertisement | advertisement\_\_unified\_priority |  |
| advertisement | advertisement\_\_effective\_unified\_priority |  |
| advertisement | advertisement\_\_unified\_yield |  |
| advertisement | advertisement\_\_is\_replacement |  |
| advertisement | advertisement\_\_replaced\_ad\_id |  |
| advertisement | advertisement\_\_replaced\_creative\_id |  |
| advertisement | advertisement\_\_replaced\_ad\_unit\_id |  |
| advertisement | advertisement\_\_replaced\_campaign\_id |  |
| advertisement | advertisement\_\_is\_uy\_replaced |  |
| advertisement | advertisement\_\_is\_ax |  |
| advertisement | advertisement\_\_replaced\_ad\_network\_id |  |
| advertisement | advertisement\_\_flags |  |
| advertisement | advertisement\_\_bit\_flags |  |
| advertisement | advertisement\_\_extra\_flags |  |
| advertisement | advertisement\_\_extra\_flags2 |  |
| advertisement | advertisement\_\_error |  |

### Candidate

| **Entity** | **Column** | **Comments** |
| --- | --- | --- |
| candidate | candidate\_\_ad\_id |  |
| candidate | candidate\_\_rtb\_auction\_index |  |
| candidate | candidate\_\_rtb\_impression\_index |  |
| candidate | candidate\_\_site\_id |  |
| candidate | candidate\_\_site\_section\_id |  |
| candidate | candidate\_\_asset\_id |  |
| candidate | candidate\_\_series\_id |  |
| candidate | candidate\_\_bid\_status |  |
| candidate | candidate\_\_original\_price |  |
| candidate | candidate\_\_raw\_price |  |
| candidate | candidate\_\_clearing\_price |  |
| candidate | candidate\_\_dsp\_clearing\_price |  |
| candidate | candidate\_\_dsp\_clearing\_price\_discounted |  |
| candidate | candidate\_\_internal\_deal\_id |  |
| candidate | candidate\_\_internal\_group\_deal\_id |  |
| candidate | candidate\_\_deal\_id |  |
| candidate | candidate\_\_buyer\_id |  |
| candidate | candidate\_\_buyer\_group\_id |  |
| candidate | candidate\_\_buyer\_platform\_id |  |
| candidate | candidate\_\_dsp\_id |  |
| candidate | candidate\_\_media\_buyer\_id |  |
| candidate | candidate\_\_trading\_desk\_id |  |
| candidate | candidate\_\_integration\_type |  |
| candidate | candidate\_\_market\_ad\_id |  |
| candidate | candidate\_\_external\_ad\_id |  |
| candidate | candidate\_\_external\_seat\_id |  |
| candidate | candidate\_\_sfx\_buyer\_id |  |
| candidate | candidate\_\_sfx\_dsp\_id |  |
| candidate | candidate\_\_flags |  |
| candidate | candidate\_\_bit\_flags |  |
| candidate | candidate\_\_error |  |
| candidate | candidate\_\_filter\_reason\_\_error\_category |  |
| candidate | candidate\_\_filter\_reaso\_\_nerror |  |
| candidate | candidate\_\_filter\_reason\_\_slot\_index |  |

### Ack

| **Enttiy** | **Column** | **Comments** |
| --- | --- | --- |
| ack | ack\_\_ad\_id |  |
| ack | ack\_\_creative\_rendition\_id |  |
| ack | ack\_\_slot\_id |  |
| ack | ack\_\_event\_type |  |
| ack | ack\_\_event\_name |  |
| ack | ack\_\_ack\_entity\_type | `ack__ack_entity_type`is removed in Hoover++ Ref: [Entity - AckCtx](https://freewheel.atlassian.net/wiki/spaces/Infrastructure/pages/191808341/Entity+-+AckCtx) |
| ack | ack\_\_metrics\_\_ad\_impression |  |
| ack | ack\_\_metrics\_\_slot\_impression |  |
| ack | ack\_\_metrics\_\_click |  |
| ack | ack\_\_metrics\_\_video\_view |  |
| ack | ack\_\_metrics\_\_first\_quartile |  |
| ack | ack\_\_metrics\_\_middle\_quartile |  |
| ack | ack\_\_metrics\_\_third\_quartile |  |
| ack | ack\_\_metrics\_\_complete\_quartile |  |
| ack | ack\_\_metrics\_\_ad\_net\_avail |  |
| ack | ack\_\_metrics\_\_ad\_gross\_avail |  |
| ack | ack\_\_metrics\_\_ad\_unconstrained\_gross\_avail |  |
| ack | ack\_\_metrics\_\_fire\_event\_revenue\_ratio |  |
| ack | ack\_\_metrics\_\_fire\_event\_slot\_revenue\_ratio |  |
| ack | ack\_\_metrics\_\_fire\_event\_bid\_revenue\_ratio |  |
| ack | ack\_\_client\_facing\_ivt\_reason\_flag |  |
| ack | ack\_\_traffic\_type |  |
| ack | ack\_\_ivt\_tracked\_info |  |
| ack | ack\_\_flags |  |
| ack | ack\_\_extra\_flags |  |
| ack | ack\_\_bit\_flags |  |
| ack | ack\_\_is\_faked |  |
| ack | ack\_\_is\_filtered |  |
| ack | ack\_\_is\_slot\_impression |  |
| ack | ack\_\_is\_private\_impression |  |
| ack | ack\_\_is\_tracking\_url\_event |  |
| ack | ack\_\_is\_embedded\_tracking\_ad\_event |  |

### Auction

| **Entity** | **Column** | **Comments** |
| --- | --- | --- |
| auction | auction\_\_network\_id |  |
| auction | auction\_\_network\_execution\_ctx\_index |  |
| auction | auction\_\_site\_id |  |
| auction | auction\_\_site\_section\_id |  |
| auction | auction\_\_series\_id |  |
| auction | auction\_\_asset\_id |  |
| auction | auction\_\_auction\_status |  |
| auction | auction\_\_bid\_request\_count |  |
| auction | auction\_\_auction\_network\_to\_eur\_exchange\_rate |  |
| auction | auction\_\_auction\_network\_to\_usd\_exchange\_rate |  |
| auction | auction\_\_bid\_to\_eur\_exchange\_rate |  |
| auction | auction\_\_bid\_to\_usd\_exchange\_rate |  |
| auction | auction\_\_dsp\_id |  |
| auction | auction\_\_buyer\_id |  |
| auction | auction\_\_buyer\_group\_id |  |
| auction | auction\_\_buyer\_platform\_id |  |
| auction | auction\_\_device\_type |  |
| auction | auction\_\_application\_type |  |
| auction | auction\_\_site\_domain |  |
| auction | auction\_\_publisher\_id |  |
| auction | auction\_\_time\_position\_class |  |
| auction | auction\_\_flags |  |
| auction | auction\_\_metadata\_auditing\_flags |  |
| auction | auction\_\_bid\_throttling\_info\_\_flags |  |
| auction | auction\_\_bid\_throttling\_status |  |
| auction | auction\_\_bid\_throttling\_info\_\_level |  |

### Partner (aka Network)

Not all are present in each table, so please double check which table(s) the columns are present in to correctly compare. This is because the `partner`  node was overloaded and now is split in Hoover++.

In each of the view, double check under the `partners__`  field.

| **Entity** | **Column** | **Comments** |
| --- | --- | --- |
| network | network\_id |  |
| network | bit\_flags |  |
| network | entity\_source |  |
| network | network\_execution\_ctx\_index |  |
| network | network\_execution\_ctx\_flags |  |
| network | content\_owner\_network\_id |  |
| network | asset\_id |  |
| network | asset\_group\_id |  |
| network | asset\_group\_ids |  |
| network | series\_id |  |
| network | site\_section\_id |  |
| network | site\_section\_group\_ids |  |
| network | site\_id |  |
| network | \* visibility | VISIBILITY FIELDS (geo visibility is DEPRECATED) |
| network | inventory\_package\_ids |  |
| network | role | Not present in `auction network`  for example |
| network | distributor\_network\_id |  |
| network | scenario\_id |  |
| network | airing\_channel\_id |  |
| network | airing\_id |  |
| network | break\_id |  |
| network | opportunity\_id |  |
| network | postal\_code\_package\_id |  |
|  network | visible\_concrete\_event\_id |  |
| network | portfolio\_ids |  |
| network | custom\_platform\_ids |  |
| network | region\_ids |  |
| network | tracked\_audience\_item\_ids |  |
| network | bidder\_seat\_id |  |
| network | flags |  |
| network | floor\_price |  |
| network | marketplace\_audience\_extension\_deal\_ids |  |
| network | network\_is\_ad\_unit\_owner |  |
| network | ad\_unit\_default\_duration |  |
| network | inventory\_distribution\_contexts |  |
| network | outbound\_rules |  |
| network | eligible\_outbound\_orders |  |
| network | outbound\_exchange\_listings |  |
| network | supply\_source |  |
| network | sales\_channel | Not present in `slot` network for example |
| network | inbound\_order\_id |  |
| network | inbound\_order\_type |  |
| network | inbound\_listing\_id |  |
| network | deal\_awareability |  |
| network | reseller\_network\_id |  |
| network | inbound\_listing\_ids |  |
| network | outbound\_order\_typ |  |
| network | supply\_source\_type | Not present in `ad`  network for example |
| network | internal\_deal\_ids |  |
| network | outbound\_order\_id |  |
| network | outbound\_order\_ids |  |
| network | buyer\_ids |  |
| network | internal\_seat\_ids |  |
| network | outbound\_listing\_id |  |
| network | matched\_inventory\_package\_ids |  |
| network | global\_currency\_id |  |


# Questions?

@Bhargava, Karan 

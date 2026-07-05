# Ad fields analysis on BCV

## Excluded Columns

| **Column Name** | **Type** | **Comment** |
| --- | --- | --- |
| \_\_path\_\_ | varchar | LQS hidden fields, fetched from presto MDS database. will not able to support these fields |
| \_\_offset\_\_ | varchar | same as above |
| \_\_file\_size\_\_ | bigint | same as above |
| \_\_footer\_size\_\_ | bigint | same as above |

## Columns Recommended for Backfill

| **Column Name** | **Type** | **Backfill?** | **Comment** |
| --- | --- | --- | --- |
| advertisement\_\_net\_price | Double | No | Used only in LQS(31). No other references found |
| advertisement\_\_active\_aim\_audience\_ids | array(integer) |   | Used in LQS(24). No other references found |
| advertisement\_\_effective\_exclude\_aim\_audience\_ids | array(integer) |   | Used in LQS(17). No other references found |
| auction\_\_index | Integer |   | Used in LQS(14). No other references found |
| auction\_\_error | varchar |   | Used in LQS(20). No other references found |
| auction\_\_bid\_to\_eur\_exchange\_rate | Double |   | Used in LQS(10). No other references found |
| candidate\_\_duration | Integer |   | Used in LQS(20). No other references found |
| candidate\_\_bid\_replica\_id | Integer |   | Used in LQS(14). No other references found |
| candidate\_\_order\_id | bigint |   | Used in LQS(21). No other references found |
| partners\_\_internal\_deal\_ids | array(array(bigint))) |   | Used in LQS(1). No other references found |
| partners\_\_inbound\_listing\_ids | array(array(bigint))) |   | Used in LQS(12). No other references found |
| partners\_\_audience\_segment\_max\_cpm | array(double) |   | Used in LQS(49). Used in Arena job etl.arena2.arena\_batch\_28120064\_8298, svc-ciec-sct |
| partners\_\_audience\_partner\_segment\_infos | array(array(varchar))) |   | Used in LQS(23). No other references found |
| partners\_\_geo\_visibility\_\_report\_aggregate | array(varchar)) |   | Used in LQS(31).  No other references found |
| process\_batch\_id | varchar |   | rename the column batch\_id to process\_batch\_id in H++ views |

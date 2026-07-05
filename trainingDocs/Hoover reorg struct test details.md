# Hoover reorg struct test details

# Background

This test does not include Auction table. 

We run the same batch on the different Hoover schema structs.

See whether the new plan data storage can be reduced. And whether the use of machines has increased.

depend on the design wiki 

  

# Test config:

| key | value | describe  |
| --- | --- | --- |
| environment | mod |  |
| S3 Data source | [s3://fw-mod-plus-flush-data/]() |  |
| batch  | 20241118-050000 |  |
| hoover lib branch | wxl\_test\_merge\_table  | with   \<etl.version\>bxiao-test-merge-tables-SNAPSHOT\</etl.version\> |
| hoover ec2 number | 3\* r5.16xlarge |  |
| hoover ec2 number |  |  |

  

# New hoover ack table struct schema:  

  

  

# Performance and Output details

|  |  | isNew | isMerge |  | query performance | output size | round2-output file number | row count(same hashkey file row count) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | current | false | false | baseline | 19min |  | {     "tables": \[         {             "table\_name": "request",             "table\_file\_count": 1312,             "table\_file\_size\_bytes": 4528946963,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/request\_20241118-050000.list]()"         },         {             "table\_name": "ack",             "table\_file\_count": 1920,             "table\_file\_size\_bytes": 11679572255,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/ack\_20241118-050000.list]()"         },         {             "table\_name": "ad",             "table\_file\_count": 1312,             "table\_file\_size\_bytes": 1805946643,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/ad\_20241118-050000.list]()"         },         {             "table\_name": "slot",             "table\_file\_count": 1312,             "table\_file\_size\_bytes": 3013084712,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/slot\_20241118-050000.list]()"         },         {             "table\_name": "transaction",             "table\_file\_count": 1920,             "table\_file\_size\_bytes": 16977542120,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/transaction\_20241118-050000.list]()"         },         {             "table\_name": "candidate",             "table\_file\_count": 1310,             "table\_file\_size\_bytes": 2014704204,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_old/hoover/JOB\_SUMMARY/20241118-050000/candidate\_20241118-050000.list]()"         }     \] } | ack: 2998request: 37951transaction:131 |
| 2 | merged ack | true | true | to get merge ack benefit | 20min |  | {     "tables": \[         {             "table\_name": "ack",             "table\_file\_count": 1920,             "table\_file\_size\_bytes": 13020251520,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_new2/hoover/JOB\_SUMMARY/20241118-050000/ack\_20241118-050000.list]()"         },         {             "table\_name": "request",             "table\_file\_count": 1312,             "table\_file\_size\_bytes": 9472090323,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_new2/hoover/JOB\_SUMMARY/20241118-050000/request\_20241118-050000.list]()"         },         {             "table\_name": "transaction",             "table\_file\_count": 1920,             "table\_file\_size\_bytes": 16976587331,             "table\_filelist\_path": "[s3a://fw-itfm/efvhvehj30\_new2/hoover/JOB\_SUMMARY/20241118-050000/transaction\_20241118-050000.list]()"         }     \] } | ack: 2998request: 37951transaction:131 |

  

| table name | current(size/file number) | reorg merge ack | comment |
| --- | --- | --- | --- |
| transaction | 16977542120/1920 | 16976587331/1920 | almost no change |
| request | 4528946963/1312 | 9472090323/1312 | storage is two times of old hoover |
| ack |  11679572255/ 1920 | 13020251520/1920 | increase 11%  storage |
| ad |  1805946643/1312 | 0 |  |
| slot |  3013084712/1312 | 0 |  |
| candidate |  2014704204/1310 | 0 |  |

# Conclusion

current size = 37G  
re-org   size  = 36G

finally:  this plan will reduce 2% storage and performance no big change

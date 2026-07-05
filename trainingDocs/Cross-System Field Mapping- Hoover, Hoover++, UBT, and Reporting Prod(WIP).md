# Cross\-System Field Mapping: Hoover, Hoover\+\+, UBT, and Reporting Prod\(WIP\)

  

- **Raw field in Hoover:** Refers to the original LQS fields from the tables `mrm_log_flat.default.request`, `slot`, `candidate`, `auction`, `ad`, and `ack`.
- **Usage: **Counts all queries over the past 30 days that use `mrm_log_flat.default.*`, including ETL processes, scheduled tasks, and ad-hoc queries.
- **Field in Hoover++: **The corresponding field in the new Hoover++ .
- **Support in UBT:** Indicates whether the field is supported in UBT.
    - **y** = supported
    - **n** = not supported
    - **no need to support** = an alternative field already covers this.  
If users need UBT to support a field marked as ‘n,’ please contact Wang Yue or Wang Yu
- **Field in UBT：** The corresponding field in the UBT .
- **Field in Reprting Prod: **The corresponding field / display name in the Reporting Product .
- **UBT Coverage:**Represents cumulative UBT coverage based on current usage frequency and whether the field is supported in UBT. Each row shows the coverage rate up to and including the current field.

  

|  | Raw Field In Hoover (mrm\_log\_flat.default.\*) | Usage | Field in Hoover++ | Support in UBT | Field in UBT | Field in Reprting Prod | UBT Coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | process\_batch\_id | 146133 |  | y | process\_batch\_id |  | 3.21% |
| 2 | request\_\_timestamp | 119714 |  | y | event\_date |  | 5.84% |
| 3 | request\_\_context\_\_video\_cro\_network\_id | 114443 |  | y | video\_cro\_network\_id |  | 8.36% |
| 4 | request\_\_extra\_flags2 | 88659 |  | y | supply\_traffic\_bit\_flag |  | 10.31% |
| 5 | request\_\_context\_\_profile\_id | 76504 |  | y | profile\_id |  | 11.99% |
| 6 | partners\_\_network\_id | 75720 |  | y | network\_id |  | 13.65% |
| 7 | request\_\_context\_\_network\_id | 74038 |  | y | distributor\_id |  | 15.28% |
| 8 | request\_\_flags | 67519 |  | y | supply\_traffic\_bit\_flag |  | 16.76% |
| 9 | request\_\_extra\_flags | 66805 |  | y | supply\_traffic\_bit\_flag |  | 18.23% |
| 10 | request\_\_delivery\_method | 62783 |  | y | delivery\_method |  | 19.61% |
| 11 | request\_\_server\_pool | 56734 |  | y | server\_pool |  | 20.86% |
| 12 | request\_\_context\_\_request\_format | 53465 |  | n |  |  | FALSE |
| 13 | partners\_\_supply\_source | 50449 |  | y | supply\_source |  | 23.14% |
| 14 | visitor\_\_country\_id | 47173 |  | y | user\_country\_id |  | 24.18% |
| 15 | request\_\_context\_\_standard\_endpoint\_id | 44191 |  | y | standard\_endpoint\_id |  | 25.15% |
| 16 | ack\_\_timestamp | 43473 |  | y | event\_date |  | 26.10% |
| 17 | request\_\_server\_group | 43328 |  | y | server\_group |  | 27.05% |
| 18 | request\_\_log\_sampling\_\_magnifier | 42388 |  | no need to support |  |  | 27.99% |
| 19 | visitor\_\_user\_agent\_device\_type | 42023 |  | n |  |  | FALSE |
| 20 | partners\_\_content\_owner\_network\_id | 41180 |  | y | content\_owner\_network\_id |  | 29.81% |
| 21 | partners\_\_role | 39328 |  | y | role |  | 30.68% |
| 22 | request\_\_context\_\_standard\_endpoint\_owner\_id | 34738 |  | y | standard\_endpoint\_owner\_id |  | 31.44% |
| 23 | request\_\_context\_\_standard\_programmer\_id | 34610 |  | y | standard\_programmer\_id |  | 32.20% |
| 24 | request\_\_context\_\_standard\_brand\_id | 33285 |  | y | standard\_brand\_id |  | 32.93% |
| 25 | auction\_\_network\_id | 32930 |  | y | network\_id |  | 33.66% |
| 26 | partners\_\_sales\_channel | 32698 |  | y | sales\_channel |  | 34.38% |
| 27 | slot\_\_time\_position\_class | 31128 |  | y | time\_position\_classes |  | 35.06% |
| 28 | visitor\_\_standard\_device\_type\_child\_id | 30148 |  | y | standard\_device\_type\_id |  | 35.72% |
| 29 | ack\_\_metrics\_\_raw\_ad\_impression | 29947 |  | y | ad\_views |  | 36.38% |
| 30 | auction\_\_dsp\_id | 29946 |  | y | dsp\_id |  | 37.04% |
| 31 | candidate\_\_internal\_deal\_id | 27669 |  | y | deal\_ids |  | 37.65% |
| 32 | ack\_\_ack\_entity\_type | 27575 |  | no need to support |  |  | 38.25% |
| 33 | candidate\_\_integration\_type | 27426 |  | y | auction\_integration\_type |  | 38.86% |
| 34 | partners\_\_inbound\_order\_id | 27321 |  | y | inbound\_order\_id |  | 39.46% |
| 35 | request\_\_traffic\_type | 27220 |  | y | ivt\_bit\_flag |  | 40.05% |
| 36 | request\_\_context\_\_ab\_test\_item\_\_bucket\_id | 26785 |  | n |  |  | FALSE |
| 37 | ack\_\_metrics\_\_ad\_impression | 25322 |  | y | ad\_views |  | 41.20% |
| 38 | advertisement\_\_flags | 24839 |  | y | ad\_bit\_flag |  | 41.75% |
| 39 | request\_\_request\_throttling\_info\_\_flags | 24781 |  | n |  |  | FALSE |
| 40 | partners\_\_bit\_flags | 23678 |  | y | network\_bit\_flag |  | 42.81% |
| 41 | request\_\_is\_filtered | 23670 |  | n |  |  | FALSE |
| 42 | visitor\_\_standard\_environment\_id | 23389 |  | y | standard\_environment\_id |  | 43.84% |
| 43 | partners\_\_entity\_source | 23297 |  | no need to support |  |  | 44.36% |
| 44 | auction\_\_flags | 23060 |  | y | auction\_bit\_flag |  | 44.86% |
| 45 | visitor\_\_standard\_os\_id | 22530 |  | y | standard\_os\_id |  | 45.36% |
| 46 | partners\_\_inbound\_listing\_id | 22340 |  | y | inbound\_listing\_id |  | 45.85% |
| 47 | candidate\_\_dsp\_id | 22095 |  | y | dsp\_id |  | 46.33% |
| 48 | request\_\_decision\_info\_\_value8 | 21572 |  | n |  |  | FALSE |
| 49 | request\_\_is\_first\_request | 21435 |  | n |  |  | FALSE |
| 50 | request\_\_context\_\_site\_section\_id | 21221 |  | y | site\_section\_id |  | 47.75% |
| 51 | partners\_\_reseller\_network\_id | 21037 |  | y | reseller\_id |  | 48.21% |
| 52 | ack\_\_traffic\_type | 20934 |  | y | ivt\_bit\_flag |  | 48.67% |
| 53 | request\_\_context\_\_stream\_mode\_id | 20116 |  | y | stream\_mode\_id |  | 49.11% |
| 54 | partners\_\_network\_is\_extra\_item\_owner | 19805 |  | n |  |  | FALSE |
| 55 | candidate\_\_bid\_status | 18677 |  | y | bid\_status |  | 49.96% |
| 56 | auction\_\_integration\_type | 17980 |  | y | auction\_integration\_type |  | 50.35% |
| 57 | partners\_\_site\_section\_id | 17361 |  | y | site\_section\_id |  | 50.73% |
| 58 | request\_\_advertisement\_count | 16904 |  | no need to support |  |  | 51.10% |
| 59 | partners\_\_revenue | 16473 |  | y | selected\_ads\_revenue |  | 51.47% |
| 60 | partners\_\_site\_id | 16074 |  | y | site\_id |  | 51.82% |
| 61 | request\_\_context\_\_content\_form\_id | 16060 |  | y | content\_form\_id |  | 52.17% |
| 62 | candidate\_\_clearing\_price | 15911 |  | n | prog\_clearing\_price\_100x |  | FALSE |
| 63 | auction\_\_auction\_status | 15669 |  | y | auction\_status |  | 52.87% |
| 64 | request\_\_context\_\_profile\_type | 15645 |  | y | profile\_type |  | 53.21% |
| 65 | advertisement\_\_placement\_id | 15375 |  | y | placement\_id |  | 53.55% |
| 66 | slot\_\_flags | 15206 |  | no need to support |  |  | 53.88% |
| 67 | request\_\_transaction\_id | 14935 |  | y |  |  | 54.21% |
| 68 | partners\_\_geo\_country\_visibility\_\_report\_aggregate | 14337 |  | y | geo\_country\_visibility |  | 54.53% |
| 69 | partners\_\_user\_agent\_visibility\_\_report\_aggregate | 14337 |  | y | user\_agent\_visibility |  | 54.84% |
| 70 | partners\_\_standard\_programmer\_visibility\_\_report\_aggregate | 14292 |  | y | standard\_programmer\_visibility |  | 55.15% |
| 71 | ack\_\_event\_name | 13751 |  | no need to support |  |  | 55.46% |
| 72 | advertisement\_\_is\_fallback | 13729 |  | y | ad\_bit\_flag |  | 55.76% |
| 73 | candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate | 13639 |  | no need to support |  |  | 56.06% |
| 74 | partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate | 13615 |  | y | standard\_endpoint\_owner\_visibility | 56.36% |  |
| 75 | partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate | 13609 |  | y | standard\_endpoint\_visibility |  | 56.66% |
| 76 | partners\_\_standard\_brand\_visibility\_\_report\_aggregate | 13592 |  | y | standard\_brand\_visibility |  | 56.96% |
| 77 | auction\_\_auction\_sampling\_\_magnifier | 13166 |  | no need to support |  |  | 57.24% |
| 78 | partners\_\_inbound\_order\_type | 13142 |  | y | inbound\_order\_type |  | 57.53% |
| 79 | auction\_\_device\_type | 12987 |  | y | prog\_device\_type |  | 57.82% |
| 80 | candidate\_\_buyer\_group\_id | 12944 |  | y | buyer\_group\_id |  | 58.10% |
| 81 | request\_\_context\_\_site\_section\_cro\_site\_id | 12884 |  | no need to support | site\_id |  | 58.39% |
| 82 | request\_\_context\_\_standard\_publisher\_id | 12725 |  | y | standard\_publisher\_id |  | 58.67% |
| 83 | advertisement\_\_is\_bumper | 12437 |  | y | ad\_bit\_flag |  | 58.94% |
| 84 | advertisement\_\_ad\_oo\_network\_id | 12363 |  | n |  |  | FALSE |
| 85 | partners\_\_distributor\_network\_id | 11916 |  | y | distributor\_id |  | 59.47% |
| 86 | candidate\_\_error | 11366 |  | y | pre\_filtered\_bid\_error\_code failed\_bid\_error\_code filtered\_bid\_error\_code | 59.72% |  |
| 87 | request\_\_context\_\_standard\_app\_id | 11329 |  | y | standard\_app\_id |  | 59.97% |
| 88 | request\_\_context\_\_standard\_app\_bundle\_id | 11257 |  | y | standard\_app\_bundle\_id |  | 60.22% |
| 89 | request\_\_compliance\_mark\_flag | 11198 |  | n |  |  | FALSE |
| 90 | auction\_\_app\_bundle | 11094 |  | y | app\_bundle |  | 60.71% |
| 91 | partners\_\_network\_is\_ad\_owner | 10956 |  | no need to support |  |  | 60.95% |
| 92 | ack\_\_metrics\_\_slot\_impression | 10912 |  | no need to support |  |  | 61.19% |
| 93 | ack\_\_event\_type | 10797 |  | no need to support |  |  | 61.43% |
| 94 | request\_\_magnifier | 10716 |  | no need to support |  |  | 61.66% |
| 95 | candidate\_\_buyer\_platform\_id | 10667 |  | y | buyer\_platform\_id |  | 61.90% |
| 96 | request\_\_multiplier | 10655 |  | no need to support |  |  | 62.13% |
| 97 | request\_\_context\_\_standard\_site\_domain\_id | 10640 |  | y | standard\_site\_domain\_id |  | 62.36% |
| 98 | request\_\_advertisement\_delivered\_count | 10488 |  | y | ads |  | 62.59% |
| 99 | advertisement\_\_ad\_id | 10465 |  | y | ad\_id |  | 62.82% |
| 100 | visitor\_\_standard\_device\_type\_ids | 10311 |  | no need to support |  |  | 63.05% |
| 101 | request\_\_visitor\_\_user\_agent\_device\_type | 10226 |  | n |  |  | FALSE |
| 102 | request\_\_context\_\_standard\_channel\_id | 10184 |  | y | standard\_channel\_id |  | 63.50% |
| 103 | partners\_\_outbound\_order\_id | 10096 |  | y | outbound\_order\_id |  | 63.72% |
| 104 | auction\_\_buyer\_platform\_id | 10034 |  | y | buyer\_platform\_id |  | 63.94% |
| 105 | ack\_\_metrics\_\_click | 10028 |  | y | clicks |  | 64.16% |
| 106 | request\_\_context\_\_response\_format | 10007 |  | n |  |  | FALSE |
| 107 | ack\_\_metrics\_\_fire\_event\_revenue\_ratio | 9984 |  | no need to support |  |  | 64.60% |
| 108 | request\_\_context\_\_video\_cro\_context\_id | 9871 |  | n |  |  | FALSE |
| 109 | slot\_\_max\_ads | 9693 |  | y | raw\_slot\_max\_ads |  | 65.03% |
| 110 | partners\_\_content\_form\_visibility\_\_report\_aggregate | 9685 |  | y | content\_form\_visibility |  | 65.24% |
| 111 | partners\_\_deal\_awareability | 9476 |  | no need to support |  |  | 65.45% |
| 112 | slot\_\_sequence | 9456 |  | y | slot\_sequence |  | 65.66% |
| 113 | auction\_\_error | 9455 |  | y | pre\_filtered\_request\_error\_code |  | 65.87% |
| 114 | visitor\_\_country | 9368 |  | no need to support |  |  | 66.07% |
| 115 | ack\_\_metrics\_\_complete\_quartile | 9340 |  | y | video\_ads\_100\_percent\_complete |  | 66.28% |
| 116 | partners\_\_outbound\_exchange\_order\_id | 9296 |  | n | outbound\_order\_ids |  | FALSE |
| 117 | ack\_\_metrics\_\_first\_quartile | 9251 |  | y | video\_ads\_25\_percent\_complete |  | 66.69% |
| 118 | ack\_\_metrics\_\_middle\_quartile | 9249 |  | y | video\_ads\_50\_percent\_complete |  | 66.89% |
| 119 | ack\_\_metrics\_\_third\_quartile | 9249 |  | y | video\_ads\_75\_percent\_complete |  | 67.09% |
| 120 | slot\_\_num\_ads | 8968 |  | y | ads |  | 67.29% |
| 121 | slot\_\_unfilled\_avails | 8953 |  | y | raw\_slot\_unfilled\_avails |  | 67.49% |
| 122 | advertisement\_\_external\_reseller\_\_network\_id | 8555 |  | n |  |  | FALSE |
| 123 | request\_\_context\_\_site\_section\_cro\_asset\_id | 8535 |  | y | asset\_id |  | 67.86% |
| 124 | visitor\_\_state\_id | 8295 |  | y | user\_state\_id |  | 68.05% |
| 125 | partners\_\_outbound\_listing\_id | 8211 |  | y | outbound\_listing\_id |  | 68.23% |
| 126 | slot\_\_normalized\_ad\_unit\_id | 8207 |  | y | slot\_ad\_unit\_id |  | 68.41% |
| 127 | request\_\_server\_id | 8058 |  | no need to support |  |  | 68.58% |
| 128 | partners\_\_content\_owner\_revenue | 8017 |  | y | content\_owner\_revenue |  | 68.76% |
| 129 | partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier | 7724 |  | y | priority\_tier |  | 68.93% |
| 130 | partners\_\_unified\_rule\_priority\_\_priority\_tier | 7724 |  | y | priority\_tier |  | 69.10% |
| 131 | visitor\_\_dma\_code | 7618 |  | y | user\_dma\_code\_id |  | 69.27% |
| 132 | candidate\_\_flags | 7534 |  | y |  |  | 69.43% |
| 133 | advertisement\_\_extra\_flags | 7530 |  | y | ad\_bit\_flag |  | 69.60% |
| 134 | advertisement\_\_entity\_flags | 7458 |  | y | ad\_bit\_flag |  | 69.76% |
| 135 | auction\_\_time\_position\_class | 7354 |  | y | slot\_time\_position\_class |  | 69.92% |
| 136 | candidate\_\_auction\_type | 7326 |  | y |  |  | 70.08% |
| 137 | partners\_\_reseller\_revenue | 7291 |  | y |  |  | 70.24% |
| 138 | request\_\_context\_\_standard\_language\_ids | 7274 |  | y |  |  | 70.40% |
| 139 | candidate\_\_network\_id | 7257 |  | y |  |  | 70.56% |
| 140 | candidate\_\_bidding\_buyer\_id | 7235 |  | y |  |  | 70.72% |
| 141 | auction\_\_extra\_flags | 7095 |  | y |  |  | 70.88% |
| 142 | request\_\_context\_\_video\_cro\_site\_id | 7066 |  | y |  |  | 71.03% |
| 143 | auction\_\_impression\_\_deals\_\_internal\_deal\_id | 7060 |  | y |  |  | 71.19% |
| 144 | auction\_\_auction\_network\_to\_usd\_exchange\_rate | 7013 |  | y |  |  | 71.34% |
| 145 | auction\_\_site\_domain | 6825 |  | y |  |  | 71.49% |
| 146 | candidate\_\_raw\_price | 6715 |  | y |  |  | 71.64% |
| 147 | request\_\_context\_\_custom\_asset\_id | 6692 |  | y |  |  | 71.79% |
| 148 | advertisement\_\_effective\_unified\_priority\_\_priority\_tier | 6655 |  | y |  |  | 71.93% |
| 149 | advertisement\_\_is\_undeliverable | 6609 |  | y |  |  | 72.08% |
| 150 | visitor\_\_state | 6565 |  | y |  |  | 72.22% |
| 151 | candidate\_\_global\_advertiser\_ids | 6202 |  | y |  |  | 72.36% |
| 152 | candidate\_\_global\_brand\_ids | 6160 |  | y |  |  | 72.49% |
| 153 | advertisement\_\_extra\_flags2 | 6006 |  | y |  |  | 72.63% |
| 154 | visitor\_\_cookie\_user\_id | 5827 |  | y |  |  | 72.75% |
| 155 | visitor\_\_dma\_code\_id | 5798 |  | y |  |  | 72.88% |
| 156 | candidate\_\_filter\_reason\_\_error | 5486 |  | y |  |  | 73.00% |
| 157 | partners\_\_global\_currency\_id | 5469 |  | y |  |  | 73.12% |
| 158 | candidate\_\_global\_industry\_ids | 5449 |  | y |  |  | 73.24% |
| 159 | request\_\_global\_currency\_version | 5380 |  | y |  |  | 73.36% |
| 160 | request\_\_context\_\_standard\_genre\_ids | 5225 |  | y |  |  | 73.48% |
| 161 | ads\_in\_slot\_\_partners\_\_network\_id | 5207 |  | y |  |  | 73.59% |
| 162 | ads\_in\_slot\_\_advertisement\_\_is\_fallback | 5207 |  | y |  |  | 73.70% |
| 163 | request\_\_context\_\_standard\_iab\_category\_ids | 5187 |  | y |  |  | 73.82% |
| 164 | ads\_in\_slot\_\_partners\_\_sales\_channel | 5178 |  | y |  |  | 73.93% |
| 165 | ads\_in\_slot\_\_partners\_\_supply\_source | 5178 |  | y |  |  | 74.05% |
| 166 | execution\_networks\_\_network\_id | 5174 |  | y |  |  | 74.16% |
| 167 | advertisement\_\_duration | 5158 |  | y |  |  | 74.27% |
| 168 | auction\_\_buyer\_group\_id | 5103 |  | y |  |  | 74.39% |
| 169 | candidate\_\_market\_ad\_id | 5079 |  | y |  |  | 74.50% |
| 170 | candidate\_\_unified\_deal\_priority\_\_priority\_tier | 5064 |  | y |  |  | 74.61% |
| 171 | partners\_\_avails\_category\_\_avails\_in\_played\_slot | 5059 |  | y |  |  | 74.72% |
| 172 | advertisement\_\_advertiser\_id | 5048 |  | y |  |  | 74.83% |
| 173 | partners\_\_content\_owner\_bidding\_revenue | 4929 |  | y |  |  | 74.94% |
| 174 | auction\_\_ab\_test\_items\_\_bucket\_id | 4845 |  | y |  |  | 75.05% |
| 175 | advertisement\_\_creative\_id | 4659 |  | y |  |  | 75.15% |
| 176 | slot\_\_max\_duration | 4652 |  | y |  |  | 75.25% |
| 177 | partners\_\_unified\_rule\_priority\_\_sub\_priority\_value | 4648 |  | y |  |  | 75.35% |
| 178 | partners\_\_rule\_type\_priority | 4648 |  | y |  |  | 75.45% |
| 179 | partners\_\_outbound\_order\_priority\_type | 4648 |  | y |  |  | 75.56% |
| 180 | partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | 4648 |  | y |  |  | 75.66% |
| 181 | request\_\_linear\_capnedit | 4582 |  | y |  |  | 75.76% |
| 182 | partners\_\_outbound\_order\_type | 4580 |  | y |  |  | 75.86% |
| 183 | request\_\_cbp\_\_slot\_template\_id | 4580 |  | y |  |  | 75.96% |
| 184 | ads\_in\_slot\_\_advertisement\_\_flags | 4515 |  | y |  |  | 76.06% |
| 185 | auction\_\_impression\_\_deals\_\_bid\_floor | 4509 |  | y |  |  | 76.16% |
| 186 | execution\_networks\_\_supply\_source | 4501 |  | y |  |  | 76.26% |
| 187 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 4483 |  | y |  |  | 76.36% |
| 188 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 4483 |  | y |  |  | 76.45% |
| 189 | ads\_in\_slot\_\_partners\_\_role | 4483 |  | y |  |  | 76.55% |
| 190 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 4483 |  | y |  |  | 76.65% |
| 191 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 4483 |  | y |  |  | 76.75% |
| 192 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 4483 |  | y |  |  | 76.85% |
| 193 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 4483 |  | y |  |  | 76.95% |
| 194 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 4483 |  | y |  |  | 77.05% |
| 195 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 4483 |  | y |  |  | 77.14% |
| 196 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 4483 |  | y |  |  | 77.24% |
| 197 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 4483 |  | y |  |  | 77.34% |
| 198 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 4483 |  | y |  |  | 77.44% |
| 199 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 4483 |  | y |  |  | 77.54% |
| 200 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 4483 |  | y |  |  | 77.64% |
| 201 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 4483 |  | y |  |  | 77.74% |
| 202 | visitor\_\_platform\_group | 4461 |  | y |  |  | 77.83% |
| 203 | auction\_\_site\_section\_id | 4451 |  | y |  |  | 77.93% |
| 204 | partners\_\_series\_id | 4434 |  | y |  |  | 78.03% |
| 205 | visitor\_\_filtration\_reason | 4432 |  | y |  |  | 78.13% |
| 206 | ads\_in\_slot\_\_partners\_\_reseller\_network\_id | 4429 |  | y |  |  | 78.22% |
| 207 | ads\_in\_slot\_\_partners\_\_content\_owner\_network\_id | 4429 |  | y |  |  | 78.32% |
| 208 | ads\_in\_slot\_\_partners\_\_inbound\_order\_id | 4429 |  | y |  |  | 78.42% |
| 209 | candidate\_\_external\_seat\_id | 4345 |  | y |  |  | 78.51% |
| 210 | candidate\_\_filter\_reason\_\_error\_category | 4330 |  | y |  |  | 78.61% |
| 211 | ads\_in\_slot\_\_candidate\_\_internal\_deal\_id | 4327 |  | y |  |  | 78.70% |
| 212 | request\_\_context\_\_tv\_network\_id | 4272 |  | y |  |  | 78.80% |
| 213 | partners\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 4264 |  | y |  |  | 78.89% |
| 214 | request\_\_advertisements\_\_flags | 4257 |  | y |  |  | 78.98% |
| 215 | visitor\_\_caller | 4230 |  | n |  |  | FALSE |
| 216 | candidate\_\_advertiser\_id | 4217 |  | y |  |  | 79.17% |
| 217 | auction\_\_is\_faked\_auction | 4118 |  | no need to support |  |  | 79.26% |
| 218 | request\_\_context\_\_key\_value\_\_key | 4090 |  | n |  |  | FALSE |
| 219 | request\_\_slots\_\_environment | 4038 |  | n |  |  | FALSE |
| 220 | ack\_\_is\_private\_impression | 4037 |  | no need to support |  |  | 79.53% |
| 221 | advertisement\_\_is\_sstf\_fallback | 4032 |  | y |  |  | 79.62% |
| 222 | request\_\_visitor\_\_country\_id | 3960 |  | y |  |  | 79.70% |
| 223 | auction\_\_impression\_\_deals\_\_bid\_floor\_uplift | 3921 |  | n |  |  | FALSE |
| 224 | visitor\_\_syscode | 3906 |  | n |  |  | FALSE |
| 225 | request\_\_visitor\_\_dma\_code\_id | 3889 |  | y |  |  | 79.96% |
| 226 | partners\_\_inbound\_order\_transaction\_type | 3852 |  | y |  |  | 80.05% |
| 227 | acks\_\_metrics\_\_ad\_impression | 3837 |  | y |  |  | 80.13% |
| 228 | execution\_networks\_\_content\_owner\_network\_id | 3828 |  | y |  |  | 80.21% |
| 229 | partners\_\_avails\_category\_\_distinct\_inventory\_avails | 3827 |  | y |  |  | 80.30% |
| 230 | auction\_\_application\_type | 3813 |  | y |  |  | 80.38% |
| 231 | slot\_\_avails | 3787 |  | y |  |  | 80.47% |
| 232 | ads\_in\_slot\_\_partners\_\_site\_section\_id | 3781 |  | y |  |  | 80.55% |
| 233 | slot\_\_time\_unfilled | 3771 |  | y |  |  | 80.63% |
| 234 | visitor\_\_platform\_device\_id | 3756 |  | y |  |  | 80.71% |
| 235 | auction\_\_site\_id | 3747 |  | y |  |  | 80.80% |
| 236 | ads\_in\_slot\_\_partners\_\_distributor\_network\_id | 3727 |  | y |  |  | 80.88% |
| 237 | ads\_in\_slot\_\_partners\_\_network\_is\_extra\_item\_owner | 3727 |  | no need to support |  |  | 80.96% |
| 238 | ads\_in\_slot\_\_partners\_\_site\_id | 3727 |  | y |  |  | 81.04% |
| 239 | auction\_\_ifa\_type | 3687 |  | y |  |  | 81.12% |
| 240 | partners\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 3648 |  | y |  |  | 81.20% |
| 241 | partners\_\_rule\_id | 3633 |  | no need to support |  |  | 81.28% |
| 242 | ack\_\_metrics\_\_no\_click | 3623 |  | y |  |  | 81.36% |
| 243 | ack\_\_metrics\_\_can\_quartile | 3623 |  | y |  |  | 81.44% |
| 244 | ack\_\_metrics\_\_ad\_error | 3618 |  | y |  |  | 81.52% |
| 245 | candidate\_\_deal\_type | 3611 |  | y |  |  | 81.60% |
| 246 | partners\_\_inbound\_rule\_id | 3608 |  | y |  |  | 81.68% |
| 247 | candidate\_\_duration | 3607 |  | y |  |  | 81.76% |
| 248 | partners\_\_demand\_dim\_awareability | 3600 |  | n |  |  | FALSE |
| 249 | advertisement\_\_global\_advertiser\_ids | 3595 |  | y |  |  | 81.92% |
| 250 | advertisement\_\_inventory\_protection\_flags | 3587 |  | y |  |  | 82.00% |
| 251 | advertisement\_\_global\_brand\_ids | 3586 |  | y |  |  | 82.08% |
| 252 | advertisement\_\_unified\_priority\_\_priority\_tier | 3584 |  | y |  |  | 82.15% |
| 253 | advertisement\_\_effective\_unified\_priority\_\_sub\_priority\_value | 3582 |  | y |  |  | 82.23% |
| 254 | advertisement\_\_unified\_priority\_\_sub\_priority\_value | 3582 |  | y |  |  | 82.31% |
| 255 | candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value | 3582 |  | y |  |  | 82.39% |
| 256 | advertisement\_\_ad\_priority\_type | 3582 |  | y |  |  | 82.47% |
| 257 | request\_\_slots\_\_flags | 3574 |  | y |  |  | 82.55% |
| 258 | request\_\_visitor\_\_city\_id | 3550 |  | y |  |  | 82.63% |
| 259 | request\_\_visitor\_\_postal\_code | 3550 |  | y |  |  | 82.70% |
| 260 | advertisement\_\_io\_id | 3533 |  | y |  |  | 82.78% |
| 261 | ack\_\_metrics\_\_ad\_bid\_won | 3515 |  | y |  |  | 82.86% |
| 262 | auction\_\_market\_integration\_type | 3467 |  | y |  |  | 82.93% |
| 263 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_site\_id | 3379 |  | no need to support |  |  | 83.01% |
| 264 | request\_\_visitor\_\_dma\_code | 3286 |  | y |  |  | 83.08% |
| 265 | ack\_\_flags | 3233 |  | y |  |  | 83.15% |
| 266 | request\_\_demand\_log\_magnifier | 3229 |  | no need to support |  |  | 83.22% |
| 267 | request\_\_decision\_info\_\_value15 | 3184 |  | n |  |  | FALSE |
| 268 | slot\_\_ad\_unit\_id | 3178 |  | y |  |  | 83.36% |
| 269 | idx\_\_has\_advertisement | 3130 |  | n |  |  | FALSE |
| 270 | request\_\_visitor\_\_platform\_device\_id | 3077 |  | y |  |  | 83.50% |
| 271 | partners\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 3076 |  | y |  |  | 83.57% |
| 272 | partners\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 3076 |  | y |  |  | 83.63% |
| 273 | partners\_\_ad\_filling\_status\_\_filled\_ad\_num | 3076 |  | y |  |  | 83.70% |
| 274 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id | 3074 |  | y |  |  | 83.77% |
| 275 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type | 3074 |  | y |  |  | 83.84% |
| 276 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id | 3074 |  | y |  |  | 83.90% |
| 277 | slot\_\_ad\_unit\_default\_duration | 3073 |  | n |  |  | FALSE |
| 278 | slot\_\_parent\_time\_unfilled | 3073 |  | n |  |  | FALSE |
| 279 | ads\_in\_slot\_\_advertisement\_\_duration | 3032 |  | y |  |  | 84.11% |
| 280 | request\_\_context\_\_source\_id | 3021 |  | y |  |  | 84.17% |
| 281 | ads\_in\_slot\_\_advertisement\_\_is\_undeliverable | 3016 |  | y |  |  | 84.24% |
| 282 | auction\_\_impression\_\_equivalent\_opportunity\_number | 3012 |  | n |  |  | FALSE |
| 283 | request\_\_visitor\_\_country | 3012 |  | y |  |  | 84.37% |
| 284 | ads\_in\_slot\_\_partners\_\_standard\_programmer\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.44% |
| 285 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.50% |
| 286 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.57% |
| 287 | ads\_in\_slot\_\_partners\_\_user\_agent\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.63% |
| 288 | ads\_in\_slot\_\_partners\_\_content\_form\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.70% |
| 289 | ads\_in\_slot\_\_partners\_\_geo\_country\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.77% |
| 290 | ads\_in\_slot\_\_partners\_\_standard\_brand\_visibility\_\_report\_aggregate | 2987 |  | y |  |  | 84.83% |
| 291 | ads\_in\_slot\_\_partners\_\_bit\_flags | 2987 |  | y |  |  | 84.90% |
| 292 | partners\_\_distributor\_revenue | 2973 |  | y |  |  | 84.96% |
| 293 | execution\_networks\_\_inbound\_listing\_id | 2966 |  | y |  |  | 85.03% |
| 294 | ads\_in\_slot\_\_partners\_\_inbound\_order\_type | 2962 |  | y |  |  | 85.09% |
| 295 | execution\_networks\_\_inbound\_order\_type | 2951 |  | y |  |  | 85.16% |
| 296 | execution\_networks\_\_inbound\_order\_id | 2951 |  | y |  |  | 85.22% |
| 297 | execution\_networks\_\_role | 2951 |  | y |  |  | 85.29% |
| 298 | ack\_\_event\_category | 2941 |  | n |  |  | FALSE |
| 299 | partners\_\_avails\_category\_\_avails | 2935 |  | y |  |  | 85.42% |
| 300 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 2922 |  | y |  |  | 85.48% |
| 301 | ads\_in\_slot\_\_partners\_\_deal\_awareability | 2914 |  | n |  |  | FALSE |
| 302 | ads\_in\_slot\_\_candidate\_\_bidding\_buyer\_id | 2914 |  | y |  |  | 85.61% |
| 303 | auction\_\_impression\_\_index | 2912 |  | y |  |  | 85.67% |
| 304 | ads\_in\_slot\_\_auction\_\_flags | 2903 |  | y |  |  | 85.74% |
| 305 | ads\_in\_slot\_\_candidate\_\_bid\_status | 2903 |  | y |  |  | 85.80% |
| 306 | ads\_in\_slot\_\_candidate\_\_buyer\_group\_id | 2901 |  | y |  |  | 85.86% |
| 307 | candidate\_\_buyer\_id | 2890 |  | y |  |  | 85.93% |
| 308 | request\_\_request\_throttling\_info\_\_exempt\_thousandth | 2889 |  | y |  |  | 85.99% |
| 309 | request\_\_prebid\_sivt\_\_capnedit\_\_traffic\_valid | 2870 |  | y |  |  | 86.05% |
| 310 | request\_\_context\_\_po\_type | 2867 |  | y |  |  | 86.12% |
| 311 | slot\_\_avail\_type | 2861 |  | no need to support |  |  | 86.18% |
| 312 | request\_\_visitor\_\_platform\_browser\_id | 2843 |  | y |  |  | 86.24% |
| 313 | request\_\_visitor\_\_platform\_os\_id | 2843 |  | y |  |  | 86.30% |
| 314 | advertisement\_\_replaced\_ad\_network\_id | 2842 |  | y |  |  | 86.37% |
| 315 | request\_\_time\_record\_\_total | 2839 |  | y |  |  | 86.43% |
| 316 | request\_\_context\_\_standard\_ssp\_channel\_id | 2837 |  | y |  |  | 86.49% |
| 317 | request\_\_context\_\_stream\_id | 2834 |  | y |  |  | 86.55% |
| 318 | request\_\_context\_\_station\_id | 2834 |  | y |  |  | 86.62% |
| 319 | candidate\_\_internal\_group\_deal\_id | 2828 |  | n |  |  | FALSE |
| 320 | ack\_\_metrics\_\_avails\_event\_count | 2828 |  | no need to support |  |  | 86.74% |
| 321 | advertisement\_\_active\_term\_id | 2820 |  | n |  |  | FALSE |
| 322 | partners\_\_content\_owner\_bidding\_original\_revenue | 2818 |  | n |  |  | FALSE |
| 323 | partners\_\_content\_owner\_bidding\_modified\_revenue | 2814 |  | n |  |  | FALSE |
| 324 | partners\_\_ssp\_clearing\_revenue | 2813 |  | n |  |  | FALSE |
| 325 | request\_\_visitor\_\_device\_id | 2715 |  | y |  |  | 87.05% |
| 326 | auction\_\_ab\_test\_items\_\_collection\_id | 2640 |  | n |  |  | FALSE |
| 327 | request\_\_visitor\_\_user\_id | 2601 |  | n |  |  | FALSE |
| 328 | request\_\_context\_\_asset\_id | 2543 |  | y |  |  | 87.22% |
| 329 | visitor\_\_user\_agent | 2527 |  | n |  |  | FALSE |
| 330 | request\_\_visitor\_\_device\_type | 2498 |  | y |  |  | 87.33% |
| 331 | request\_\_mpe\_matcher\_filters\_\_id | 2496 |  | y |  |  | 87.38% |
| 332 | request\_\_visitor\_\_state\_id | 2477 |  | y |  |  | 87.44% |
| 333 | request\_\_visitor\_\_active\_state | 2458 |  | n |  |  | FALSE |
| 334 | request\_\_context\_\_content\_rating\_id | 2433 |  | y |  |  | 87.55% |
| 335 | request\_\_context\_\_request\_duration | 2432 |  | y |  |  | 87.60% |
| 336 | ack\_\_ad\_id | 2356 |  | y |  |  | 87.65% |
| 337 | auction\_\_series\_id | 2346 |  | y |  |  | 87.70% |
| 338 | request\_\_slots\_\_time\_position\_class | 2341 |  | y |  |  | 87.75% |
| 339 | request\_\_advertisements\_\_placement\_id | 2321 |  | y |  |  | 87.81% |
| 340 | candidate\_\_external\_ad\_id | 2320 |  | y |  |  | 87.86% |
| 341 | request\_\_visitor\_\_state | 2299 |  | y |  |  | 87.91% |
| 342 | auction\_\_bid\_throttling\_info\_\_flags | 2293 |  | n |  |  | FALSE |
| 343 | ads\_in\_slot\_\_advertisement\_\_entity\_flags | 2285 |  | y |  |  | 88.01% |
| 344 | ads\_in\_slot\_\_advertisement\_\_is\_bumper | 2285 |  | y |  |  | 88.06% |
| 345 | ads\_in\_slot\_\_advertisement\_\_is\_sstf\_fallback | 2285 |  | y |  |  | 88.11% |
| 346 | advertisement\_\_campaign\_id | 2263 |  | y |  |  | 88.16% |
| 347 | partners\_\_avails\_category\_\_opportunity\_in\_played\_slot | 2261 |  | y |  |  | 88.21% |
| 348 | ads\_in\_slot\_\_partners\_\_unified\_rule\_priority\_\_priority\_tier | 2260 |  | y |  |  | 88.26% |
| 349 | ads\_in\_slot\_\_advertisement\_\_effective\_unified\_priority\_\_priority\_tier | 2260 |  | y |  |  | 88.31% |
| 350 | ads\_in\_slot\_\_partners\_\_unified\_outbound\_order\_priority\_\_priority\_tier | 2260 |  | y |  |  | 88.36% |
| 351 | partners\_\_avails\_category\_\_opportunity | 2255 |  | y |  |  | 88.41% |
| 352 | partners\_\_avails\_category\_\_total\_avails | 2255 |  | y |  |  | 88.46% |
| 353 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 2249 |  | y |  |  | 88.50% |
| 354 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 2249 |  | y |  |  | 88.55% |
| 355 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 2249 |  | y |  |  | 88.60% |
| 356 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 2249 |  | y |  |  | 88.65% |
| 357 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 2249 |  | y |  |  | 88.70% |
| 358 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 2249 |  | y |  |  | 88.75% |
| 359 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 2249 |  | y |  |  | 88.80% |
| 360 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 2249 |  | y |  |  | 88.85% |
| 361 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 2249 |  | y |  |  | 88.90% |
| 362 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 2249 |  | y |  |  | 88.95% |
| 363 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 2249 |  | y |  |  | 89.00% |
| 364 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 2249 |  | y |  |  | 89.05% |
| 365 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 2249 |  | y |  |  | 89.10% |
| 366 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 2249 |  | y |  |  | 89.15% |
| 367 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 2249 |  | y |  |  | 89.20% |
| 368 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 2249 |  | y |  |  | 89.25% |
| 369 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 2249 |  | y |  |  | 89.30% |
| 370 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 2249 |  | y |  |  | 89.35% |
| 371 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 2249 |  | y |  |  | 89.39% |
| 372 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 2249 |  | y |  |  | 89.44% |
| 373 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 2249 |  | y |  |  | 89.49% |
| 374 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 2249 |  | y |  |  | 89.54% |
| 375 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 2249 |  | y |  |  | 89.59% |
| 376 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 2249 |  | y |  |  | 89.64% |
| 377 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 2249 |  | y |  |  | 89.69% |
| 378 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 2249 |  | y |  |  | 89.74% |
| 379 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 2249 |  | y |  |  | 89.79% |
| 380 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 2249 |  | y |  |  | 89.84% |
| 381 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 2249 |  | y |  |  | 89.89% |
| 382 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 2249 |  | y |  |  | 89.94% |
| 383 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 2249 |  | y |  |  | 89.99% |
| 384 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 2249 |  | y |  |  | 90.04% |
| 385 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 2249 |  | y |  |  | 90.09% |
| 386 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 2249 |  | y |  |  | 90.14% |
| 387 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 2249 |  | y |  |  | 90.19% |
| 388 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 2249 |  | y |  |  | 90.23% |
| 389 | execution\_networks\_\_site\_section\_id | 2247 |  | y |  |  | 90.28% |
| 390 | execution\_networks\_\_site\_id | 2247 |  | y |  |  | 90.33% |
| 391 | auction\_\_mkpl\_partner\_tags\_\_strategy | 2229 |  | n |  |  | FALSE |
| 392 | slot\_\_initial\_num\_ads | 2223 |  | y |  |  | 90.43% |
| 393 | slot\_\_initial\_unfilled\_avails | 2223 |  | y |  |  | 90.48% |
| 394 | advertisement\_\_rendition\_id | 2218 |  | y |  |  | 90.53% |
| 395 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type | 2218 |  | y |  |  | 90.58% |
| 396 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 2218 |  | y |  |  | 90.63% |
| 397 | request\_\_visitor\_\_filtration\_reason | 2206 |  | y |  |  | 90.67% |
| 398 | advertisement\_\_ad\_unit\_id | 2202 |  | y |  |  | 90.72% |
| 399 | auction\_\_publisher\_id | 2195 |  | y |  |  | 90.77% |
| 400 | ads\_in\_slot\_\_partners\_\_entity\_source | 2192 |  | y |  |  | 90.82% |
| 401 | ads\_in\_slot\_\_auction\_\_dsp\_id | 2192 |  | y |  |  | 90.87% |
| 402 | ads\_in\_slot\_\_auction\_\_integration\_type | 2192 |  | y |  |  | 90.92% |
| 403 | candidate\_\_external\_network\_id | 2185 |  | y |  |  | 90.96% |
| 404 | auction\_\_invite\_deal\_size | 2184 |  | y |  |  | 91.01% |
| 405 | ads\_in\_slot\_\_candidate\_\_order\_id | 2179 |  | y |  |  | 91.06% |
| 406 | ads\_in\_slot\_\_auction\_\_device\_type | 2179 |  | y |  |  | 91.11% |
| 407 | ads\_in\_slot\_\_partners\_\_inbound\_listing\_id | 2170 |  | y |  |  | 91.16% |
| 408 | request\_\_context\_\_stream\_mode\_ids | 2158 |  | y |  |  | 91.20% |
| 409 | advertisement\_\_error | 2156 |  | y |  |  | 91.25% |
| 410 | visitor\_\_operator\_zone\_id | 2156 |  | y |  |  | 91.30% |
| 411 | auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id | 2152 |  | n |  |  | FALSE |
| 412 | auction\_\_bid\_throttling\_info\_\_exempt\_thousandth | 2147 |  | n |  |  | FALSE |
| 413 | request\_\_advertisements\_\_campaign\_id | 2143 |  | y |  |  | 91.44% |
| 414 | request\_\_mpe\_matcher\_filters\_\_bucket\_id | 2126 |  | n |  |  | FALSE |
| 415 | request\_\_mpe\_matcher\_filters\_\_weight | 2126 |  | n |  |  | FALSE |
| 416 | auction\_\_impression\_\_deals\_\_buyer\_group\_id | 2125 |  | n |  |  | FALSE |
| 417 | request\_\_kafka\_msg\_size | 2125 |  | n |  |  | FALSE |
| 418 | visitor\_\_active\_state | 2124 |  | n |  |  | FALSE |
| 419 | auction\_\_bid\_throttling\_info | 2120 |  | n |  |  | FALSE |
| 420 | partners\_\_airing\_channel\_id | 2114 |  | y |  |  | 91.77% |
| 421 | candidate\_\_auction\_outbound\_bid\_floor | 2092 |  | n |  |  | FALSE |
| 422 | auction\_\_dynamic\_floor\_price\_algorithm | 2088 |  | n |  |  | FALSE |
| 423 | ack\_\_kafka\_msg\_key | 2023 |  | n |  |  | FALSE |
| 424 | partners\_\_internal\_deal\_ids | 1958 |  | y |  |  | 91.95% |
| 425 | visitor\_\_address | 1944 |  | n |  |  | FALSE |
| 426 | request\_\_visitor\_\_universal\_hhid | 1895 |  | n |  |  | FALSE |
| 427 | request\_\_context\_\_site\_section\_cro\_network\_id | 1856 |  | y |  |  | 92.07% |
| 428 | request\_\_linear\_capnedit\_\_device\_id | 1768 |  | n |  |  | FALSE |
| 429 | request\_\_context\_\_distributor\_site\_section\_group\_id | 1762 |  | y |  |  | 92.15% |
| 430 | request\_\_model\_framework\_\_network\_model\_contexts\_\_realtime\_features\_\_feature\_id | 1762 |  | y |  |  | 92.19% |
| 431 | request\_\_model\_framework\_\_network\_model\_contexts\_\_realtime\_features\_\_metric | 1744 |  | y |  |  | 92.22% |
| 432 | request\_\_model\_framework\_\_network\_model\_contexts\_\_realtime\_feature\_group\_id | 1744 |  | y |  |  | 92.26% |
| 433 | request\_\_context\_\_standard\_content\_series\_id | 1731 |  | y |  |  | 92.30% |
| 434 | request\_\_context\_\_standard\_content\_daypart\_id | 1728 |  | y |  |  | 92.34% |
| 435 | visitor\_\_postal\_code | 1724 |  | y |  |  | 92.38% |
| 436 | request\_\_context\_\_host\_name | 1634 |  | n |  |  | FALSE |
| 437 | request\_\_context\_\_key\_value\_\_value | 1620 |  | n |  |  | FALSE |
| 438 | request\_\_request\_prefilter\_\_flag | 1609 |  | y |  |  | 92.48% |
| 439 | visitor\_\_peer\_address | 1602 |  | n |  |  | FALSE |
| 440 | request\_\_decision\_info\_\_flag1 | 1594 |  | n |  |  | FALSE |
| 441 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_channel\_id | 1589 |  | y |  |  | 92.59% |
| 442 | partners\_\_supply\_acquisition\_cost | 1563 |  | y |  |  | 92.62% |
| 443 | partners\_\_supply\_distribution\_cost | 1563 |  | y |  |  | 92.66% |
| 444 | inventory\_\_asset\_chain\_\_site\_id | 1547 |  | y |  |  | 92.69% |
| 445 | inventory\_\_asset\_chain\_\_role | 1547 |  | y |  |  | 92.73% |
| 446 | inventory\_\_asset\_chain\_\_network\_id | 1547 |  | y |  |  | 92.76% |
| 447 | inventory\_\_asset\_chain\_\_distributor\_network\_id | 1547 |  | y |  |  | 92.79% |
| 448 | inventory\_\_asset\_chain\_\_site\_section\_id | 1546 |  | y |  |  | 92.83% |
| 449 | inventory\_\_asset\_chain\_\_content\_owner\_network\_id | 1546 |  | y |  |  | 92.86% |
| 450 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id | 1545 |  | y |  |  | 92.90% |
| 451 | request\_info\_\_slot\_ad\_unit\_ids | 1545 |  | y |  |  | 92.93% |
| 452 | request\_\_context\_\_standard\_content\_territory\_id | 1545 |  | y |  |  | 92.96% |
| 453 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id | 1545 |  | y |  |  | 93.00% |
| 454 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 1545 |  | y |  |  | 93.03% |
| 455 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 1545 |  | y |  |  | 93.07% |
| 456 | request\_info\_\_slot\_time\_position\_classes | 1545 |  | y |  |  | 93.10% |
| 457 | request\_\_context\_\_standard\_content\_subscription\_model\_id | 1545 |  | y |  |  | 93.13% |
| 458 | ads\_in\_slot\_\_partners\_\_inbound\_order\_transaction\_type | 1520 |  | y |  |  | 93.17% |
| 459 | request\_\_decision\_info\_\_flag4 | 1507 |  | n |  |  | FALSE |
| 460 | partners\_\_supply\_source\_type | 1502 |  | n |  |  | FALSE |
| 461 | candidate\_\_order\_id | 1500 |  | y |  |  | 93.27% |
| 462 | ads\_in\_slot\_\_partners\_\_series\_id | 1497 |  | y |  |  | 93.30% |
| 463 | partners\_\_avails\_category\_\_inventory\_avails | 1484 |  | y |  |  | 93.33% |
| 464 | candidate\_\_ad\_id | 1483 |  | y |  |  | 93.36% |
| 465 | slot\_\_initial\_time\_unfilled | 1483 |  | y |  |  | 93.40% |
| 466 | request\_\_advertisements\_\_ad\_id | 1480 |  | y |  |  | 93.43% |
| 467 | request\_\_audience\_flags | 1479 |  | y |  |  | 93.46% |
| 468 | advertisement\_\_external\_reseller\_\_up\_revenue | 1470 |  | n |  |  | FALSE |
| 469 | ads\_in\_slot\_\_candidate\_\_global\_industry\_ids | 1468 |  | y |  |  | 93.53% |
| 470 | ads\_in\_slot\_\_auction\_\_site\_id | 1468 |  | y |  |  | 93.56% |
| 471 | ads\_in\_slot\_\_auction\_\_application\_type | 1468 |  | y |  |  | 93.59% |
| 472 | ads\_in\_slot\_\_auction\_\_site\_domain | 1468 |  | y |  |  | 93.62% |
| 473 | ads\_in\_slot\_\_auction\_\_ifa\_type | 1468 |  | y |  |  | 93.66% |
| 474 | ads\_in\_slot\_\_auction\_\_time\_position\_class | 1468 |  | y |  |  | 93.69% |
| 475 | ads\_in\_slot\_\_candidate\_\_global\_brand\_ids | 1468 |  | y |  |  | 93.72% |
| 476 | ads\_in\_slot\_\_auction\_\_series\_id | 1468 |  | y |  |  | 93.75% |
| 477 | ads\_in\_slot\_\_candidate\_\_external\_seat\_id | 1468 |  | y |  |  | 93.78% |
| 478 | ads\_in\_slot\_\_auction\_\_app\_bundle | 1468 |  | y |  |  | 93.82% |
| 479 | ads\_in\_slot\_\_candidate\_\_global\_advertiser\_ids | 1468 |  | y |  |  | 93.85% |
| 480 | ads\_in\_slot\_\_auction\_\_buyer\_platform\_id | 1468 |  | y |  |  | 93.88% |
| 481 | ads\_in\_slot\_\_candidate\_\_auction\_type | 1468 |  | y |  |  | 93.91% |
| 482 | ads\_in\_slot\_\_auction\_\_site\_section\_id | 1468 |  | y |  |  | 93.95% |
| 483 | candidate\_\_dsp\_crid | 1465 |  | n |  |  | FALSE |
| 484 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_order\_id | 1463 |  | y |  |  | 94.01% |
| 485 | ads\_in\_slot\_\_candidate\_\_unified\_deal\_priority\_\_priority\_tier | 1463 |  | y |  |  | 94.04% |
| 486 | advertisement\_\_market\_ad\_id | 1461 |  | y |  |  | 94.07% |
| 487 | request\_\_visitor\_\_caller | 1458 |  | n |  |  | FALSE |
| 488 | request\_\_bid\_request\_\_publisher\_id | 1454 |  | y |  |  | 94.14% |
| 489 | ads\_in\_slot\_\_advertisement\_\_placement\_id | 1454 |  | y |  |  | 94.17% |
| 490 | request\_\_privacy\_info\_\_compliance\_flag | 1449 |  | y |  |  | 94.20% |
| 491 | candidate\_\_rtb\_auction\_index | 1444 |  | y |  |  | 94.23% |
| 492 | ads\_in\_slot\_\_candidate\_\_market\_ad\_id | 1441 |  | y |  |  | 94.27% |
| 493 | ads\_in\_slot\_\_partners\_\_outbound\_listing\_id | 1441 |  | y |  |  | 94.30% |
| 494 | partners\_\_outbound\_exchange\_listings\_\_listing\_ids | 1440 |  | y |  |  | 94.33% |
| 495 | partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity | 1440 |  | y |  |  | 94.36% |
| 496 | ads\_in\_slot\_\_candidate\_\_dsp\_id | 1434 |  | y |  |  | 94.39% |
| 497 | ads\_in\_slot\_\_candidate\_\_buyer\_platform\_id | 1434 |  | y |  |  | 94.42% |
| 498 | ack\_\_metrics\_\_no\_ad\_impression | 1430 |  | y |  |  | 94.45% |
| 499 | request\_\_context\_\_standard\_content\_credential\_status\_id | 1429 |  | n |  |  | FALSE |
| 500 | request\_\_context\_\_standard\_content\_viewership\_profile\_ids | 1429 |  | y |  |  | 94.52% |
| 501 | request\_\_decision\_info\_\_flag3 | 1428 |  | n |  |  | FALSE |
| 502 | request\_\_decision\_info\_\_flag2 | 1428 |  | n |  |  | FALSE |
| 503 | request\_\_decision\_info\_\_value3 | 1427 |  | n |  |  | FALSE |
| 504 | request\_\_decision\_info\_\_value7 | 1426 |  | n |  |  | FALSE |
| 505 | request\_\_mrc\_compliance\_label | 1426 |  | y |  |  | 94.67% |
| 506 | ads\_in\_slot\_\_partners\_\_network\_is\_ad\_owner | 1425 |  | y |  |  | 94.71% |
| 507 | advertisement\_\_bid\_price\_to\_upstream | 1424 |  | y |  |  | 94.74% |
| 508 | request\_\_context\_\_rbp\_platform | 1424 |  | y |  |  | 94.77% |
| 509 | request\_\_bid\_request\_\_app\_id | 1418 |  | y |  |  | 94.80% |
| 510 | advertisement\_\_global\_industry\_ids | 1417 |  | y |  |  | 94.83% |
| 511 | request\_\_rtb\_auction\_\_index | 1416 |  | n |  |  | FALSE |
| 512 | request\_\_errors\_\_code | 1414 |  | y |  |  | 94.89% |
| 513 | advertisement\_\_is\_owned\_by\_cro | 1414 |  | n |  |  | FALSE |
| 514 | request\_\_rtb\_auction\_\_integration\_type | 1412 |  | y |  |  | 94.95% |
| 515 | advertisement\_\_agency\_id | 1409 |  | y |  |  | 94.99% |
| 516 | advertisement\_\_spot\_id | 1409 |  | n |  |  | FALSE |
| 517 | partners\_\_flags | 1408 |  | y |  |  | 95.05% |
| 518 | partners\_\_network\_execution\_ctx\_flags | 1408 |  | y |  |  | 95.08% |
| 519 | request\_\_context\_\_ab\_test\_item\_\_collection\_id | 1408 |  | y |  |  | 95.11% |
| 520 | ack\_\_metrics\_\_ad\_insertion | 1407 |  | n |  |  | FALSE |
| 521 | ack\_\_metrics\_\_video\_view | 1407 |  | y |  |  | 95.17% |
| 522 | ack\_\_win\_notice\_error | 1406 |  | n |  |  | FALSE |
| 523 | request\_\_log\_sampling\_\_mode | 1355 |  | y |  |  | 95.23% |
| 524 | auction\_\_impression\_\_bid\_floor | 1329 |  | y |  |  | 95.26% |
| 525 | partners\_\_carriage\_inventory\_owner\_id | 1140 |  | y |  |  | 95.29% |
| 526 | partners\_\_carriage\_listing\_split\_unit\_id | 1123 |  | n |  |  | FALSE |
| 527 | auction\_\_bid\_request\_count | 1113 |  | y |  |  | 95.34% |
| 528 | slot\_\_carriage\_listing\_split\_unit\_id | 1109 |  | n |  |  | FALSE |
| 529 | advertisement\_\_slot\_index | 1099 |  | y |  |  | 95.38% |
| 530 | slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id | 1091 |  | n |  |  | FALSE |
| 531 | slot\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num | 1091 |  | n |  |  | FALSE |
| 532 | partners\_\_eligible\_carriage\_listing\_split\_unit\_ids | 1090 |  | n |  |  | FALSE |
| 533 | slot\_\_carriage\_listing\_split\_unit\_num | 1089 |  | n |  |  | FALSE |
| 534 | candidate\_\_filter\_reason\_\_slot\_index | 1085 |  | n |  |  | FALSE |
| 535 | request\_\_decision\_info\_\_value13 | 1072 |  | n |  |  | FALSE |
| 536 | partners\_\_asset\_id | 1071 |  | y |  |  | 95.55% |
| 537 | request\_\_bidding\_context\_\_bid\_request\_\_app\_\_id | 1043 |  | y |  |  | 95.57% |
| 538 | request\_\_bid\_request\_\_app\_bundle | 989 |  | y |  |  | 95.60% |
| 539 | request\_\_context\_\_distributor\_asset\_id | 951 |  | y |  |  | 95.62% |
| 540 | ack\_\_creative\_rendition\_id | 949 |  | y |  |  | 95.64% |
| 541 | request\_\_context\_\_extracted\_key\_value\_\_\_fw\_dbp | 942 |  | y |  |  | 95.66% |
| 542 | request\_\_visitor\_\_standard\_device\_type\_ids | 937 |  | y |  |  | 95.68% |
| 543 | visitor\_\_platform\_os\_id | 914 |  | y |  |  | 95.70% |
| 544 | request\_\_context\_\_key\_value | 911 |  | y |  |  | 95.72% |
| 545 | request\_\_context\_\_ip\_enabled\_audience\_id | 910 |  | y |  |  | 95.74% |
| 546 | request\_\_visitor\_\_user\_agent | 905 |  | n |  |  | FALSE |
| 547 | request\_\_context\_\_inventory\_location\_id | 905 |  | y |  |  | 95.78% |
| 548 | visitor\_\_referrer | 902 |  | n |  |  | FALSE |
| 549 | visitor\_\_platform\_browser\_id | 892 |  | n |  |  | FALSE |
| 550 | visitor\_\_city\_id | 891 |  | y |  |  | 95.84% |
| 551 | request\_\_visitor\_\_household\_id | 891 |  | n |  |  | FALSE |
| 552 | request\_\_visitor\_\_standard\_environment\_id | 885 |  | y |  |  | 95.88% |
| 553 | auction\_\_impression\_\_bid\_floor\_uplift | 859 |  | n |  |  | FALSE |
| 554 | request\_\_context\_\_standard\_movie\_rating\_id | 836 |  | y |  |  | 95.91% |
| 555 | ack\_\_extra\_flags | 836 |  | y |  |  | 95.93% |
| 556 | visitor\_\_universal\_hhid | 834 |  | n |  |  | FALSE |
| 557 | request\_\_prebid\_sivt\_\_whiteops\_\_invalid\_reason | 832 |  | y |  |  | 95.97% |
| 558 | request\_\_prebid\_sivt\_\_inhouse\_\_is\_whitelisted | 829 |  | y |  |  | 95.99% |
| 559 | execution\_networks\_\_network\_execution\_ctx\_flags | 828 |  | n |  |  | FALSE |
| 560 | request\_\_prebid\_sivt\_\_inhouse\_\_invalid\_reason | 827 |  | y |  |  | 96.02% |
| 561 | request\_info\_\_slot\_video\_cro\_ad\_unit\_ids | 809 |  | y |  |  | 96.04% |
| 562 | request\_\_bit\_flags | 808 |  | y |  |  | 96.06% |
| 563 | slot\_\_max\_ad\_duration | 807 |  | y |  |  | 96.08% |
| 564 | inventory\_\_asset\_chain\_\_content\_form\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.09% |
| 565 | inventory\_\_asset\_chain\_\_bit\_flags | 806 |  | y |  |  | 96.11% |
| 566 | inventory\_\_asset\_chain\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.13% |
| 567 | inventory\_\_asset\_chain\_\_standard\_brand\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.15% |
| 568 | inventory\_\_asset\_chain\_\_standard\_programmer\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.16% |
| 569 | inventory\_\_asset\_chain\_\_standard\_endpoint\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.18% |
| 570 | inventory\_\_asset\_chain\_\_geo\_country\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.20% |
| 571 | inventory\_\_asset\_chain\_\_user\_agent\_visibility\_\_report\_aggregate | 806 |  | y |  |  | 96.22% |
| 572 | execution\_networks\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.24% |
| 573 | execution\_networks\_\_standard\_endpoint\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.25% |
| 574 | execution\_networks\_\_content\_form\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.27% |
| 575 | execution\_networks\_\_inbound\_order\_transaction\_type | 805 |  | y |  |  | 96.29% |
| 576 | execution\_networks\_\_bit\_flags | 805 |  | y |  |  | 96.31% |
| 577 | execution\_networks\_\_standard\_brand\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.32% |
| 578 | execution\_networks\_\_standard\_programmer\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.34% |
| 579 | execution\_networks\_\_user\_agent\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.36% |
| 580 | execution\_networks\_\_geo\_country\_visibility\_\_report\_aggregate | 805 |  | y |  |  | 96.38% |
| 581 | request\_\_prebid\_sivt\_\_whiteops | 783 |  | y |  |  | 96.39% |
| 582 | advertisement\_\_external\_reseller | 782 |  | y |  |  | 96.41% |
| 583 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_network\_id | 779 |  | y |  |  | 96.43% |
| 584 | partners\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 776 |  | y |  |  | 96.45% |
| 585 | partners\_\_avails\_category\_\_total\_unfilled\_avails | 776 |  | y |  |  | 96.46% |
| 586 | partners\_\_inbound\_order\_ids | 774 |  | y |  |  | 96.48% |
| 587 | request\_\_visitor\_\_app\_bundle\_id | 765 |  | y |  |  | 96.50% |
| 588 | request\_\_privacy\_info\_\_gdpr\_flag | 760 |  | n |  |  | FALSE |
| 589 | auction\_\_app\_storeurl | 756 |  | y |  |  | 96.53% |
| 590 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_network\_id | 754 |  | y |  |  | 96.55% |
| 591 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_asset\_id | 754 |  | y |  |  | 96.56% |
| 592 | auction\_\_metadata\_auditing\_flags | 753 |  | y |  |  | 96.58% |
| 593 | slot\_\_environment | 753 |  | y |  |  | 96.60% |
| 594 | ads\_in\_slot\_\_advertisement\_\_ad\_id | 752 |  | y |  |  | 96.61% |
| 595 | partners\_\_site\_section\_group\_ids | 744 |  | y |  |  | 96.63% |
| 596 | partners\_\_avails\_category\_\_unfilled\_avails | 744 |  | y |  |  | 96.65% |
| 597 | ads\_in\_slot\_\_partners\_\_flags | 741 |  | y |  |  | 96.66% |
| 598 | ads\_in\_slot\_\_partners\_\_inbound\_rule\_id | 741 |  | y |  |  | 96.68% |
| 599 | ads\_in\_slot\_\_partners\_\_rule\_id | 741 |  | y |  |  | 96.69% |
| 600 | request\_\_request\_byte\_size | 738 |  | y |  |  | 96.71% |
| 601 | candidate\_\_rtb\_impression\_slot\_index | 734 |  | y |  |  | 96.73% |
| 602 | request\_\_traffic\_compliance\_\_endpoint\_id | 734 |  | y |  |  | 96.74% |
| 603 | request\_\_dro\_network\_id | 732 |  | y |  |  | 96.76% |
| 604 | request\_\_context\_\_profile\_trait\_\_pre\_selection\_external\_ad\_timeout | 732 |  | y |  |  | 96.77% |
| 605 | request\_\_context\_\_profile\_trait\_\_post\_selection\_external\_ad\_timeout | 732 |  | y |  |  | 96.79% |
| 606 | request\_\_context\_\_standard\_privacy\_id | 731 |  | y |  |  | 96.81% |
| 607 | request\_\_context\_\_standard\_addressability\_ids | 731 |  | n |  |  | FALSE |
| 608 | request\_\_privacy\_info\_\_impacted\_features\_flag | 730 |  | n |  |  | FALSE |
| 609 | request\_\_traffic\_compliance\_\_mrc\_compliance\_flag | 728 |  | y |  |  | 96.86% |
| 610 | request\_\_context\_\_distributor\_network\_id | 727 |  | y |  |  | 96.87% |
| 611 | advertisement\_\_ad\_replica\_id | 727 |  | n |  |  | FALSE |
| 612 | request\_\_traffic\_compliance\_\_mrc\_non\_compliance\_type | 726 |  | n |  |  | FALSE |
| 613 | request\_\_network\_execution\_ctx\_\_inbound\_order\_id | 726 |  | y |  |  | 96.92% |
| 614 | visitor\_\_standard\_operator\_id | 725 |  | y |  |  | 96.94% |
| 615 | visitor\_\_standard\_retailer\_id | 725 |  | y |  |  | 96.95% |
| 616 | visitor\_\_standard\_manufacturer\_id | 725 |  | y |  |  | 96.97% |
| 617 | request\_\_decision\_info\_\_value2 | 724 |  | n |  |  | FALSE |
| 618 | request\_\_decision\_info\_\_value4 | 724 |  | n |  |  | FALSE |
| 619 | request\_\_prebid\_sivt\_\_capnedit\_\_invalid\_reason | 724 |  | y |  |  | 97.01% |
| 620 | request\_\_privacy\_info\_\_gpp\_\_flag | 724 |  | y |  |  | 97.03% |
| 621 | request\_\_decision\_info\_\_value5 | 724 |  | n |  |  | FALSE |
| 622 | request\_\_decision\_info\_\_value1 | 724 |  | n |  |  | FALSE |
| 623 | request\_\_privacy\_info\_\_gpp | 724 |  | n |  |  | FALSE |
| 624 | request\_\_prebid\_sivt\_\_sivt\_model | 724 |  | y |  |  | 97.09% |
| 625 | request\_\_context\_\_custom\_airing\_break\_id | 724 |  | y |  |  | 97.11% |
| 626 | request\_\_context\_\_linear\_break\_source | 724 |  | y |  |  | 97.13% |
| 627 | request\_\_decision\_info\_\_value6 | 724 |  | y |  |  | 97.14% |
| 628 | request\_\_prebid\_sivt\_\_gateway\_response | 724 |  | y |  |  | 97.16% |
| 629 | request\_\_privacy\_info\_\_gpp\_\_section | 724 |  | y |  |  | 97.17% |
| 630 | ads\_in\_slot\_\_candidate\_\_deal\_type | 723 |  | y |  |  | 97.19% |
| 631 | ads\_in\_slot\_\_advertisement\_\_advertiser\_id | 723 |  | y |  |  | 97.21% |
| 632 | ads\_in\_slot\_\_partners\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | 723 |  | y |  |  | 97.22% |
| 633 | ads\_in\_slot\_\_advertisement\_\_unified\_priority\_\_sub\_priority\_value | 723 |  | y |  |  | 97.24% |
| 634 | ads\_in\_slot\_\_candidate\_\_unified\_deal\_priority\_\_sub\_priority\_value | 723 |  | y |  |  | 97.25% |
| 635 | ads\_in\_slot\_\_advertisement\_\_creative\_id | 723 |  | y |  |  | 97.27% |
| 636 | ads\_in\_slot\_\_advertisement\_\_global\_brand\_ids | 723 |  | y |  |  | 97.28% |
| 637 | ads\_in\_slot\_\_partners\_\_global\_currency\_id | 723 |  | y |  |  | 97.30% |
| 638 | ads\_in\_slot\_\_advertisement\_\_unified\_priority\_\_priority\_tier | 723 |  | y |  |  | 97.32% |
| 639 | ads\_in\_slot\_\_candidate\_\_error | 723 |  | y |  |  | 97.33% |
| 640 | ads\_in\_slot\_\_advertisement\_\_error | 723 |  | y |  |  | 97.35% |
| 641 | ads\_in\_slot\_\_advertisement\_\_ad\_priority\_type | 723 |  | y |  |  | 97.36% |
| 642 | ads\_in\_slot\_\_advertisement\_\_market\_ad\_id | 723 |  | y |  |  | 97.38% |
| 643 | ads\_in\_slot\_\_partners\_\_rule\_type\_priority | 723 |  | y |  |  | 97.40% |
| 644 | ads\_in\_slot\_\_partners\_\_unified\_rule\_priority\_\_sub\_priority\_value | 723 |  | y |  |  | 97.41% |
| 645 | ads\_in\_slot\_\_partners\_\_outbound\_order\_id | 723 |  | y |  |  | 97.43% |
| 646 | ads\_in\_slot\_\_advertisement\_\_effective\_unified\_priority\_\_sub\_priority\_value | 723 |  | y |  |  | 97.44% |
| 647 | ads\_in\_slot\_\_partners\_\_outbound\_order\_priority\_type | 723 |  | y |  |  | 97.46% |
| 648 | ads\_in\_slot\_\_partners\_\_demand\_dim\_awareability | 723 |  | y |  |  | 97.48% |
| 649 | ads\_in\_slot\_\_advertisement\_\_global\_advertiser\_ids | 723 |  | y |  |  | 97.49% |
| 650 | ads\_in\_slot\_\_candidate\_\_buyer\_id | 723 |  | y |  |  | 97.51% |
| 651 | request\_\_userdb\_audience\_user\_info\_\_bg\_alias\_growth\_ratio | 722 |  | y |  |  | 97.52% |
| 652 | request\_\_network\_execution\_ctx\_\_supply\_source\_type | 722 |  | y |  |  | 97.54% |
| 653 | request\_\_kafka\_msg\_key | 721 |  | n |  |  | FALSE |
| 654 | ads\_in\_slot\_\_candidate\_\_duration | 719 |  | y |  |  | 97.57% |
| 655 | ads\_in\_slot\_\_candidate\_\_dsp\_crid | 719 |  | y |  |  | 97.59% |
| 656 | ads\_in\_slot\_\_candidate\_\_external\_ad\_id | 719 |  | y |  |  | 97.60% |
| 657 | request\_\_bid\_request\_\_impression\_\_floor | 716 |  | y |  |  | 97.62% |
| 658 | request\_\_bid\_request\_\_impression\_\_private\_auction | 716 |  | y |  |  | 97.63% |
| 659 | request\_\_bid\_request\_\_impression\_\_deal\_\_public\_id | 716 |  | y |  |  | 97.65% |
| 660 | candidate\_\_redirect\_count | 716 |  | n |  |  | FALSE |
| 661 | request\_\_visitor\_\_platform\_group | 716 |  | y |  |  | 97.68% |
| 662 | request\_\_external\_candidate\_ad\_\_market\_integration\_type | 715 |  | y |  |  | 97.70% |
| 663 | request\_\_external\_candidate\_ad\_\_integration\_type | 715 |  | y |  |  | 97.71% |
| 664 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 714 |  | y |  |  | 97.73% |
| 665 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 714 |  | y |  |  | 97.74% |
| 666 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 714 |  | y |  |  | 97.76% |
| 667 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 714 |  | y |  |  | 97.78% |
| 668 | request\_\_network\_execution\_ctx\_\_context\_sequence | 714 |  | y |  |  | 97.79% |
| 669 | request\_\_slots\_\_outbound\_order\_\_order\_type | 714 |  | y |  |  | 97.81% |
| 670 | request\_\_network\_execution\_ctx\_\_candidate\_ad\_num | 714 |  | y |  |  | 97.82% |
| 671 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 714 |  | y |  |  | 97.84% |
| 672 | request\_\_network\_execution\_ctx\_\_inbound\_listing\_id | 714 |  | y |  |  | 97.85% |
| 673 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_order\_type | 714 |  | y |  |  | 97.87% |
| 674 | request\_\_slots\_\_resellers\_\_listing\_id | 714 |  | y |  |  | 97.89% |
| 675 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 714 |  | y |  |  | 97.90% |
| 676 | execution\_networks\_\_network\_is\_ad\_owner | 714 |  | y |  |  | 97.92% |
| 677 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 714 |  | y |  |  | 97.93% |
| 678 | request\_\_slots\_\_listing\_id | 714 |  | y |  |  | 97.95% |
| 679 | request\_\_network\_execution\_ctx\_\_programmatic\_candidate\_ad\_num | 714 |  | y |  |  | 97.96% |
| 680 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 714 |  | y |  |  | 97.98% |
| 681 | execution\_networks\_\_content\_owner\_bidding\_revenue | 714 |  | y |  |  | 97.99% |
| 682 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 714 |  | y |  |  | 98.01% |
| 683 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 714 |  | y |  |  | 98.03% |
| 684 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 714 |  | y |  |  | 98.04% |
| 685 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 714 |  | y |  |  | 98.06% |
| 686 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 714 |  | y |  |  | 98.07% |
| 687 | ads\_in\_slot\_\_candidate\_\_internal\_group\_deal\_id | 712 |  | y |  |  | 98.09% |
| 688 | ads\_in\_slot\_\_candidate\_\_integration\_type | 712 |  | y |  |  | 98.10% |
| 689 | ads\_in\_slot\_\_auction\_\_network\_id | 712 |  | y |  |  | 98.12% |
| 690 | ads\_in\_slot\_\_candidate\_\_network\_id | 712 |  | y |  |  | 98.14% |
| 691 | request\_\_visitor\_\_syscode | 710 |  | y |  |  | 98.15% |
| 692 | request\_\_visitor\_\_operator\_zone\_id | 710 |  | y |  |  | 98.17% |
| 693 | request\_\_network\_execution\_ctx\_\_data\_right\_\_field | 709 |  | n |  |  | FALSE |
| 694 | request\_\_external\_candidate\_ad\_\_ad\_id | 709 |  | y |  |  | 98.20% |
| 695 | request\_\_bidding\_context\_\_bid\_request\_\_impression\_\_index | 709 |  | no need to support |  |  | 98.21% |
| 696 | request\_\_external\_candidate\_ad\_\_bid\_status | 709 |  | y |  |  | 98.23% |
| 697 | request\_\_system\_degradation\_\_features | 708 |  | n |  |  | FALSE |
| 698 | request\_\_system\_degradation\_\_level | 708 |  | n |  |  | FALSE |
| 699 | request\_\_bidding\_context\_\_bid\_request\_\_publisher\_\_id | 708 |  | y |  |  | 98.28% |
| 700 | ack\_\_event\_value | 708 |  | n |  |  | FALSE |
| 701 | request\_\_slots\_\_outbound\_order\_\_order\_id | 708 |  | y |  |  | 98.31% |
| 702 | request\_\_visitor\_\_universal\_iids | 708 |  | n |  |  | FALSE |
| 703 | request\_\_network\_attribute\_\_kv\_term\_id | 708 |  | n |  |  | FALSE |
| 704 | partners\_\_listing\_id | 705 |  | y |  |  | 98.35% |
| 705 | advertisement\_\_has\_candidate | 705 |  | n |  |  | FALSE |
| 706 | ack\_\_ad\_replica\_id | 704 |  | n |  |  | FALSE |
| 707 | request\_\_context\_\_standard\_iab\_category\_ids\_raw | 704 |  | y |  |  | 98.40% |
| 708 | ads\_in\_slot\_\_partners\_\_content\_owner\_bidding\_revenue | 703 |  | y |  |  | 98.42% |
| 709 | partners\_\_postal\_code\_package\_id | 702 |  | y |  |  | 98.43% |
| 710 | partners\_\_asset\_group\_ids | 702 |  | y |  |  | 98.45% |
| 711 | partners\_\_tracked\_audience\_item\_ids | 702 |  | y |  |  | 98.46% |
| 712 | partners\_\_network\_is\_ad\_unit\_owner | 702 |  | no need to support |  |  | 98.48% |
| 713 | partners\_\_avails\_category\_\_remaining\_avails | 702 |  | n |  |  | FALSE |
| 714 | execution\_networks\_\_mapped\_site\_section\_ids | 683 |  | n |  |  | FALSE |
| 715 | execution\_networks\_\_mapped\_asset\_ids | 683 |  | n |  |  | FALSE |
| 716 | advertisement\_\_external\_reseller\_\_revenue | 676 |  | y |  |  | 98.54% |
| 717 | visitor\_\_user\_id | 570 |  | n |  |  | FALSE |
| 718 | request\_\_visitor\_\_timezone\_offset | 554 |  | n |  |  | FALSE |
| 719 | request\_\_visitor\_\_timezone | 554 |  | n |  |  | FALSE |
| 720 | visitor\_\_timezone | 537 |  | n |  |  | FALSE |
| 721 | visitor\_\_device\_id | 475 |  | y |  |  | 98.60% |
| 722 | \_\_path\_\_ | 450 |  | no need to support |  |  | 98.61% |
| 723 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_public\_id | 411 |  | no need to support |  |  | 98.62% |
| 724 | advertisement\_\_matched\_country\_ids | 403 |  | n |  |  | FALSE |
| 725 | advertisement\_\_matched\_state\_ids | 403 |  | n |  |  | FALSE |
| 726 | advertisement\_\_matched\_city\_ids | 403 |  | n |  |  | FALSE |
| 727 | advertisement\_\_matched\_dma\_ids | 403 |  | n |  |  | FALSE |
| 728 | visitor\_\_custom\_user\_id | 400 |  | n |  |  | FALSE |
| 729 | request\_\_context\_\_custom\_site\_section\_id | 397 |  | n |  |  | FALSE |
| 730 | advertisement\_\_matched\_user\_agent\_ids | 391 |  | n |  |  | FALSE |
| 731 | visitor\_\_user\_segments\_lookup\_key | 388 |  | n |  |  | FALSE |
| 732 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_id | 371 |  | no need to support |  |  | 98.69% |
| 733 | request\_\_slots\_\_break\_display\_id | 371 |  | n |  |  | FALSE |
| 734 | request\_\_context\_\_app\_\_bundle | 365 |  | y |  |  | 98.71% |
| 735 | request\_\_context\_\_app\_\_name | 348 |  | y |  |  | 98.72% |
| 736 | request\_\_context\_\_app\_\_id | 345 |  | y |  |  | 98.73% |
| 737 | request\_\_bidding\_context\_\_bid\_request\_\_app\_\_bundle | 344 |  | n |  |  | FALSE |
| 738 | request\_\_bidding\_context\_\_bid\_request\_\_app\_\_name | 344 |  | n |  |  | FALSE |
| 739 | request\_\_context\_\_app\_\_storeurl | 341 |  | n |  |  | FALSE |
| 740 | request\_\_bidding\_context\_\_bid\_request\_\_app\_\_storeurl | 341 |  | n |  |  | FALSE |
| 741 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_asset\_id | 337 |  | y |  |  | 98.76% |
| 742 | auction\_\_index | 324 |  | n |  |  | FALSE |
| 743 | request\_\_audience\_item\_\_audience\_item\_id | 322 |  | n |  |  | FALSE |
| 744 | request\_\_visitor\_\_custom\_user\_id | 263 |  | n |  |  | FALSE |
| 745 | request\_\_visitor\_\_address | 254 |  | n |  |  | FALSE |
| 746 | request\_\_visitor\_\_peer\_address | 245 |  | n |  |  | FALSE |
| 747 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_context\_id | 243 |  | no need to support |  |  | 98.80% |
| 748 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_context\_id\_raw | 243 |  | no need to support |  |  | 98.80% |
| 749 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_site\_id | 243 |  | no need to support |  |  | 98.81% |
| 750 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_asset\_id\_raw | 243 |  | no need to support |  |  | 98.82% |
| 751 | visitor\_\_server\_side\_user\_id | 238 |  | n |  |  | FALSE |
| 752 | request\_\_visitor\_\_referrer | 219 |  | n |  |  | FALSE |
| 753 | request\_\_slots\_\_avails\_metrics\_\_avails | 218 |  | y |  |  | 98.83% |
| 754 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_scenario\_id | 218 |  | n |  |  | FALSE |
| 755 | request\_\_bidding\_context\_\_bid\_request\_\_auction\_type | 218 |  | n |  |  | FALSE |
| 756 | request\_\_inventory\_group\_\_group\_id | 209 |  | n |  |  | FALSE |
| 757 | request\_\_network\_audience\_items\_\_tracked\_audience\_item\_ids | 209 |  | n |  |  | FALSE |
| 758 | request\_\_network\_audience\_items\_\_non\_tracked\_audience\_item\_ids | 208 |  | n |  |  | FALSE |
| 759 | visitor\_\_device\_type | 204 |  | y |  |  | 98.86% |
| 760 | request\_\_context\_\_explicit\_candidates | 203 |  | n |  |  | FALSE |
| 761 | request\_\_context\_\_video\_random | 203 |  | n |  |  | FALSE |
| 762 | request\_\_context\_\_video\_slot\_compatible\_dimensions | 203 |  | n |  |  | FALSE |
| 763 | request\_\_context\_\_time\_position | 203 |  | no need to support |  |  | 98.88% |
| 764 | request\_\_context\_\_asset\_duration | 203 |  | no need to support |  |  | 98.88% |
| 765 | request\_\_extra\_geo\_info | 203 |  | n |  |  | FALSE |
| 766 | request\_\_context\_\_page\_random | 203 |  | n |  |  | FALSE |
| 767 | request\_\_context\_\_out\_signal\_id | 203 |  | n |  |  | FALSE |
| 768 | request\_\_visitor\_\_server\_side\_user\_id | 201 |  | n |  |  | FALSE |
| 769 | request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id | 197 |  | n |  |  | FALSE |
| 770 | request\_\_candidates | 196 |  | no need to support |  |  | 98.91% |
| 771 | request\_\_scores\_\_score | 195 |  | n |  |  | FALSE |
| 772 | request\_\_scores\_\_network\_id | 195 |  | n |  |  | FALSE |
| 773 | request\_\_scores\_\_flag | 195 |  | n |  |  | FALSE |
| 774 | request\_\_guaranteed\_deal\_avail\_\_buyer\_id | 194 |  | n |  |  | FALSE |
| 775 | request\_\_visitor\_\_cookie\_user\_id | 190 |  | n |  |  | FALSE |
| 776 | request\_\_bidding\_context\_\_bid\_request\_\_app | 189 |  | n |  |  | FALSE |
| 777 | request\_\_bidding\_context\_\_bid\_request\_\_impression | 189 |  | n |  |  | FALSE |
| 778 | request\_\_bidding\_context\_\_bid\_request\_\_channel | 189 |  | n |  |  | FALSE |
| 779 | request\_\_bidding\_context\_\_bid\_request\_\_currency | 189 |  | n |  |  | FALSE |
| 780 | request\_\_visitor\_\_flash\_version | 189 |  | n |  |  | FALSE |
| 781 | request\_\_visitor\_\_isp\_id | 189 |  | n |  |  | FALSE |
| 782 | request\_\_visitor\_\_city | 189 |  | y |  |  | 98.96% |
| 783 | request\_\_visitor\_\_identity\_user\_ids\_\_id | 189 |  | n |  |  | FALSE |
| 784 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_asset\_id\_raw | 189 |  | n |  |  | FALSE |
| 785 | request\_\_context\_\_external\_key\_value | 189 |  | n |  |  | FALSE |
| 786 | request\_\_visitor\_\_postal\_code\_id | 189 |  | y |  |  | 98.97% |
| 787 | request\_\_visitor\_\_standard\_os\_id | 189 |  | y |  |  | 98.98% |
| 788 | request\_\_context\_\_profile\_concrete\_event\_id\_raw | 189 |  | n |  |  | FALSE |
| 789 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_series\_id | 189 |  | no need to support |  |  | 98.99% |
| 790 | request\_\_slots\_\_num\_ads | 189 |  | y |  |  | 98.99% |
| 791 | request\_\_context\_\_network\_id\_raw | 189 |  | no need to support |  |  | 98.99% |
| 792 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_channel\_id\_raw | 189 |  | no need to support |  |  | 99.00% |
| 793 | request\_\_bidding\_context\_\_bid\_request\_\_publisher | 189 |  | y |  |  | 99.00% |
| 794 | request\_\_bidding\_context\_\_bid\_request\_\_inventory\_source | 189 |  | y |  |  | 99.01% |
| 795 | request\_\_visitor\_\_internal\_user\_id | 189 |  | n |  |  | FALSE |
| 796 | request\_\_slots | 189 |  | no need to support |  |  | 99.02% |
| 797 | request\_\_visitor\_\_isp | 189 |  | n |  |  | FALSE |
| 798 | request\_\_visitor\_\_platform\_os\_id\_raw | 189 |  | n |  |  | FALSE |
| 799 | request\_\_context\_\_profile\_id\_raw | 189 |  |  |  |  | FALSE |
| 800 | request\_\_context\_\_asset\_id\_raw | 189 |  |  |  |  | FALSE |
| 801 | request\_\_visitor\_\_identity\_user\_ids\_\_namespace\_id | 189 |  |  |  |  | FALSE |
| 802 | request\_\_bidding\_context\_\_bid\_request\_\_device | 189 |  |  |  |  | FALSE |
| 803 | request\_\_bidding\_context\_\_bid\_request\_\_site | 189 |  |  |  |  | FALSE |
| 804 | request\_\_bidding\_context\_\_bid\_request\_\_deal | 189 |  |  |  |  | FALSE |
| 805 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_scenario\_id | 189 |  |  |  |  | FALSE |
| 806 | request\_\_context\_\_site\_section\_id\_raw | 189 |  |  |  |  | FALSE |
| 807 | request\_\_visitor\_\_platform\_browser\_id\_raw | 189 |  |  |  |  | FALSE |
| 808 | request\_\_bidding\_context\_\_bid\_request | 189 |  |  |  |  | FALSE |
| 809 | visitor\_\_app\_bundle\_id | 187 |  |  |  |  | FALSE |
| 810 | ack\_\_event\_key\_renderer | 173 |  |  |  |  | FALSE |
| 811 | auction\_\_bid\_throttling\_exempt\_ratio | 164 |  |  |  |  | FALSE |
| 812 | request\_\_privacy\_info | 161 |  |  |  |  | FALSE |
| 813 | request\_\_prebid\_sivt\_\_whiteops\_\_traffic\_valid | 137 |  |  |  |  | FALSE |
| 814 | request\_\_prebid\_sivt\_\_inhouse\_\_traffic\_valid | 123 |  |  |  |  | FALSE |
| 815 | partners\_\_scenario\_id | 120 |  |  |  |  | FALSE |
| 816 | request\_\_backend\_filtration\_reason | 116 |  |  |  |  | FALSE |
| 817 | request\_\_context\_\_distributor\_site\_section\_id | 112 |  |  |  |  | FALSE |
| 818 | partners\_\_programmatic\_exchange\_rate\_to\_usd | 98 |  |  |  |  | FALSE |
| 819 | advertisement\_\_position\_in\_slot | 97 |  |  |  |  | FALSE |
| 820 | request\_\_prebid\_sivt\_\_inhouse | 79 |  |  |  |  | FALSE |
| 821 | partners\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 77 |  |  |  |  | FALSE |
| 822 | partners\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 77 |  |  |  |  | FALSE |
| 823 | advertisement\_\_bit\_flags | 75 |  |  |  |  | FALSE |
| 824 | request\_\_context\_\_distributor\_video\_asset\_id | 72 |  |  |  |  | FALSE |
| 825 | ack\_\_bit\_flags | 70 |  |  |  |  | FALSE |
| 826 | request | 66 |  |  |  |  | FALSE |
| 827 | candidate\_\_site\_section\_id | 66 |  |  |  |  | FALSE |
| 828 | candidate\_\_trust\_id | 65 |  |  |  |  | FALSE |
| 829 | acks\_\_ad\_id | 64 |  |  |  |  | FALSE |
| 830 | acks\_\_event\_name | 64 |  |  |  |  | FALSE |
| 831 | advertisement\_\_is\_embedded\_tracking | 62 |  |  |  |  | FALSE |
| 832 | visitor\_\_timezone\_offset | 61 |  |  |  |  | FALSE |
| 833 | visitor\_\_household\_id | 61 |  |  |  |  | FALSE |
| 834 | audiences\_\_audience\_item\_ids | 61 |  |  |  |  | FALSE |
| 835 | candidate\_\_rtb\_impression\_index | 61 |  |  |  |  | FALSE |
| 836 | slot\_\_avails\_metrics\_\_avails | 61 |  |  |  |  | FALSE |
| 837 | candidate\_\_brand\_id | 58 |  |  |  |  | FALSE |
| 838 | aim\_info\_\_aim\_identity\_info\_\_categorized\_signals | 54 |  |  |  |  | FALSE |
| 839 | request\_\_visitor\_\_internal\_address | 53 |  |  |  |  | FALSE |
| 840 | request\_\_advertisements\_\_extra\_flags2 | 51 |  |  |  |  | FALSE |
| 841 | partners\_\_network\_execution\_ctx\_index | 50 |  |  |  |  | FALSE |
| 842 | request\_\_prebid\_sivt\_\_whiteops\_\_lookup\_id | 49 |  |  |  |  | FALSE |
| 843 | request\_\_context\_\_profile\_concrete\_event\_id | 49 |  |  |  |  | FALSE |
| 844 | candidate\_\_original\_price | 49 |  |  |  |  | FALSE |
| 845 | candidate\_\_response\_time | 48 |  |  |  |  | FALSE |
| 846 | request\_\_slots\_\_max\_duration | 48 |  |  |  |  | FALSE |
| 847 | auction\_\_privacy\_flags | 47 |  |  |  |  | FALSE |
| 848 | request\_\_context\_\_extracted\_key\_value\_\_\_fw\_lto | 46 |  |  |  |  | FALSE |
| 849 | request\_\_is\_first\_user\_visitor | 44 |  |  |  |  | FALSE |
| 850 | auction\_\_internal\_seat\_id | 43 |  |  |  |  | FALSE |
| 851 | candidate\_\_response\_industry | 42 |  |  |  |  | FALSE |
| 852 | candidate\_\_response\_time\_first\_hop | 42 |  |  |  |  | FALSE |
| 853 | request\_\_advertisements\_\_network\_id | 41 |  |  |  |  | FALSE |
| 854 | request\_\_slots\_\_outbound\_order\_\_listing\_id | 41 |  |  |  |  | FALSE |
| 855 | request\_\_advertisements\_\_extra\_flags | 41 |  |  |  |  | FALSE |
| 856 | request\_\_slots\_\_outbound\_order\_\_flags | 41 |  |  |  |  | FALSE |
| 857 | request\_\_slots\_\_max\_ads | 40 |  |  |  |  | FALSE |
| 858 | request\_\_context\_\_custom\_distributor\_id | 39 |  |  |  |  | FALSE |
| 859 | request\_\_bidding\_context\_\_bid\_request\_\_site\_\_domain | 39 |  |  |  |  | FALSE |
| 860 | auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id | 39 |  |  |  |  | FALSE |
| 861 | request\_\_bid\_request | 38 |  |  |  |  | FALSE |
| 862 | acks\_\_cpx\_concrete\_event\_id | 37 |  |  |  |  | FALSE |
| 863 | slot\_\_opportunity\_id | 37 |  |  |  |  | FALSE |
| 864 | request\_\_context\_\_site\_\_domain | 37 |  |  |  |  | FALSE |
| 865 | visitor\_\_internal\_address | 36 |  |  |  |  | FALSE |
| 866 | request\_\_slots\_\_ad\_unit\_id | 36 |  |  |  |  | FALSE |
| 867 | advertisement\_\_placement\_type\_priority | 36 |  |  |  |  | FALSE |
| 868 | candidate\_\_internal\_seat\_id | 36 |  |  |  |  | FALSE |
| 869 | request\_\_slots\_\_slot\_sequence | 35 |  |  |  |  | FALSE |
| 870 | request\_\_slots\_\_sequence | 35 |  |  |  |  | FALSE |
| 871 | candidate\_\_cch\_key | 35 |  |  |  |  | FALSE |
| 872 | request\_\_global\_currency\_\_version | 35 |  |  |  |  | FALSE |
| 873 | request\_\_slots\_\_ad\_unit\_default\_duration | 35 |  |  |  |  | FALSE |
| 874 | request\_\_advertisements\_\_reseller\_\_bidding\_revenue | 35 |  |  |  |  | FALSE |
| 875 | request\_\_advertisements\_\_slot\_index | 35 |  |  |  |  | FALSE |
| 876 | acks\_\_event\_type | 35 |  |  |  |  | FALSE |
| 877 | request\_\_slots\_\_resellers\_\_inbound\_order\_auction\_type | 35 |  |  |  |  | FALSE |
| 878 | acks\_\_flags | 35 |  |  |  |  | FALSE |
| 879 | request\_\_global\_currency\_\_currencies\_\_currency\_id | 35 |  |  |  |  | FALSE |
| 880 | request\_\_geo\_data\_provider\_id | 35 |  |  |  |  | FALSE |
| 881 | acks\_\_data\_source | 35 |  |  |  |  | FALSE |
| 882 | acks\_\_ad\_replica\_id | 35 |  |  |  |  | FALSE |
| 883 | candidate\_\_two\_phase\_translated | 35 |  |  |  |  | FALSE |
| 884 | request\_\_advertisements\_\_ad\_replica\_id | 35 |  |  |  |  | FALSE |
| 885 | acks\_\_slot\_id | 35 |  |  |  |  | FALSE |
| 886 | request\_\_advertisements\_\_entity\_flags | 35 |  |  |  |  | FALSE |
| 887 | request\_\_external\_candidate\_count | 35 |  |  |  |  | FALSE |
| 888 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_clearing\_revenue | 35 |  |  |  |  | FALSE |
| 889 | request\_\_context\_\_standard\_sport\_entity\_ids | 34 |  |  |  |  | FALSE |
| 890 | auction\_\_impression\_\_deals\_\_impression\_index | 33 |  |  |  |  | FALSE |
| 891 | partners\_\_priority\_type | 33 |  |  |  |  | FALSE |
| 892 | candidate\_\_dsp\_currency\_id | 33 |  |  |  |  | FALSE |
| 893 | candidate\_\_pod\_replica\_id | 32 |  |  |  |  | FALSE |
| 894 | auction\_\_auction\_sampling\_\_mode | 32 |  |  |  |  | FALSE |
| 895 | slot\_\_min\_duration | 32 |  |  |  |  | FALSE |
| 896 | candidate\_\_network\_execution\_ctx\_index | 32 |  |  |  |  | FALSE |
| 897 | candidate\_\_profile\_check\_passed | 32 |  |  |  |  | FALSE |
| 898 | visitor\_\_parsed\_user\_agent | 31 |  |  |  |  | FALSE |
| 899 | ack\_\_ivt\_tracked\_info\_\_ivt\_not\_dedup\_reason | 31 |  |  |  |  | FALSE |
| 900 | inventory\_\_asset\_chain\_\_asset\_id | 31 |  |  |  |  | FALSE |
| 901 | advertisement\_\_estimated\_start\_delay | 31 |  |  |  |  | FALSE |
| 902 | ack\_\_multiplier | 31 |  |  |  |  | FALSE |
| 903 | slot\_\_index | 30 |  |  |  |  | FALSE |
| 904 | request\_\_context\_\_video\_cro\_asset\_id | 29 |  |  |  |  | FALSE |
| 905 | request\_\_ifa\_type | 29 |  |  |  |  | FALSE |
| 906 | advertisement\_\_measurable\_concrete\_event\_id | 29 |  |  |  |  | FALSE |
| 907 | visitor\_\_identity\_user\_ids | 28 |  |  |  |  | FALSE |
| 908 | request\_\_is\_data\_right\_enabled | 28 |  |  |  |  | FALSE |
| 909 | request\_\_context\_\_distributor\_video\_asset\_group\_id | 28 |  |  |  |  | FALSE |
| 910 | partners\_\_selected\_yo\_margin\_id | 28 |  |  |  |  | FALSE |
| 911 | ack\_\_cpx\_concrete\_event\_id | 27 |  |  |  |  | FALSE |
| 912 | request\_\_context\_\_profile\_trait | 27 |  |  |  |  | FALSE |
| 913 | request\_\_network\_data\_visibility\_config\_\_ip\_visibility | 26 |  |  |  |  | FALSE |
| 914 | request\_\_context\_\_site\_section\_cro\_asset\_group\_id | 26 |  |  |  |  | FALSE |
| 915 | partners | 26 |  |  |  |  | FALSE |
| 916 | aim\_info\_\_aim\_audience\_info\_\_aim\_audience\_id | 26 |  |  |  |  | FALSE |
| 917 | request\_\_context\_\_transcode\_package\_id | 25 |  |  |  |  | FALSE |
| 918 | candidate\_\_dsp\_cid | 25 |  |  |  |  | FALSE |
| 919 | advertisement\_\_matched\_audience\_item\_ids | 25 |  |  |  |  | FALSE |
| 920 | ack\_\_transaction\_id | 24 |  |  |  |  | FALSE |
| 921 | candidate\_\_dsp\_adid | 23 |  |  |  |  | FALSE |
| 922 | slot\_\_carriage\_inventory\_owner\_id | 23 |  |  |  |  | FALSE |
| 923 | request\_\_is\_ssp\_bidder\_request | 23 |  |  |  |  | FALSE |
| 924 | partners\_\_floor\_price | 23 |  |  |  |  | FALSE |
| 925 | candidate\_\_vast\_creative\_id | 23 |  |  |  |  | FALSE |
| 926 | request\_\_time\_record | 22 |  |  |  |  | FALSE |
| 927 | request\_\_context\_\_ab\_test\_item | 22 |  |  |  |  | FALSE |
| 928 | ack\_\_metrics\_\_abstract\_event\_count | 22 |  |  |  |  | FALSE |
| 929 | request\_\_rtb\_auction\_\_deal\_\_internal\_deal\_id | 22 |  |  |  |  | FALSE |
| 930 | request\_\_hashed\_key\_value | 22 |  |  |  |  | FALSE |
| 931 | partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 932 | partners\_\_avails\_category | 21 |  |  |  |  | FALSE |
| 933 | advertisement\_\_is\_ax | 21 |  |  |  |  | FALSE |
| 934 | partners\_\_content\_form\_visibility | 21 |  |  |  |  | FALSE |
| 935 | partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 936 | request\_\_identifier | 21 |  |  |  |  | FALSE |
| 937 | partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 938 | request\_\_network\_data\_visibility\_config\_\_geo\_visibility | 21 |  |  |  |  | FALSE |
| 939 | ack\_\_metrics\_\_concrete\_event\_count | 21 |  |  |  |  | FALSE |
| 940 | partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 941 | visitor\_\_identity\_user\_ids\_\_id | 21 |  |  |  |  | FALSE |
| 942 | partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 943 | advertisement\_\_active\_aim\_audience\_ids | 21 |  |  |  |  | FALSE |
| 944 | partners\_\_standard\_channel\_visibility\_\_report\_aggregate | 21 |  |  |  |  | FALSE |
| 945 | partners\_\_standard\_channel\_visibility | 21 |  |  |  |  | FALSE |
| 946 | advertisement\_\_is\_external | 21 |  |  |  |  | FALSE |
| 947 | request\_\_context | 21 |  |  |  |  | FALSE |
| 948 | partners\_\_matched\_inventory\_package\_ids | 21 |  |  |  |  | FALSE |
| 949 | request\_\_networks | 21 |  |  |  |  | FALSE |
| 950 | partners\_\_standard\_content\_subscription\_model\_visibility | 21 |  |  |  |  | FALSE |
| 951 | request\_\_context\_\_mvpd | 20 |  |  |  |  | FALSE |
| 952 | request\_\_decision\_info\_\_inventory\_protections\_\_scope | 20 |  |  |  |  | FALSE |
| 953 | request\_\_userdb\_audience\_user\_info\_\_num\_dx\_enriched\_alias\_ids | 20 |  |  |  |  | FALSE |
| 954 | request\_\_phantom\_candidate | 20 |  |  |  |  | FALSE |
| 955 | request\_\_context\_\_headend\_inserter\_id | 20 |  |  |  |  | FALSE |
| 956 | request\_\_identifier\_\_source | 20 |  |  |  |  | FALSE |
| 957 | request\_\_experiment\_platform\_\_experiment\_\_index\_id | 20 |  |  |  |  | FALSE |
| 958 | request\_\_context\_\_custom\_airing\_id | 20 |  |  |  |  | FALSE |
| 959 | request\_\_experiment\_platform\_\_experiment\_\_layer\_id | 20 |  |  |  |  | FALSE |
| 960 | request\_\_context\_\_ux\_conf\_id | 20 |  |  |  |  | FALSE |
| 961 | request\_\_experiment\_platform\_\_experiment\_\_domain\_id | 20 |  |  |  |  | FALSE |
| 962 | request\_\_traffic\_compliance | 20 |  |  |  |  | FALSE |
| 963 | request\_\_network\_data\_visibility\_config\_\_user\_agent\_visibility | 20 |  |  |  |  | FALSE |
| 964 | request\_\_gateway\_source\_filepath | 20 |  |  |  |  | FALSE |
| 965 | request\_\_time\_record\_\_external\_playlist\_notification | 20 |  |  |  |  | FALSE |
| 966 | request\_\_request\_throttling\_info\_\_model\_info\_\_model\_flags | 20 |  |  |  |  | FALSE |
| 967 | request\_\_linear\_capnedit\_\_is\_dvr | 20 |  |  |  |  | FALSE |
| 968 | request\_\_extra\_geo\_info\_\_is\_pulse | 20 |  |  |  |  | FALSE |
| 969 | request\_\_xdevice\_killed\_placement | 20 |  |  |  |  | FALSE |
| 970 | \_\_footer\_size\_\_ | 20 |  |  |  |  | FALSE |
| 971 | request\_\_scte\_message\_id | 20 |  |  |  |  | FALSE |
| 972 | request\_\_traffic\_compliance\_\_endpoint\_flag | 20 |  |  |  |  | FALSE |
| 973 | request\_\_soft\_guaranteed\_ad\_\_network\_id | 20 |  |  |  |  | FALSE |
| 974 | request\_\_context\_\_ux\_section\_id | 20 |  |  |  |  | FALSE |
| 975 | request\_\_phantom\_candidate\_\_slot\_custom\_id | 20 |  |  |  |  | FALSE |
| 976 | request\_\_linear\_capnedit\_\_tune\_time | 20 |  |  |  |  | FALSE |
| 977 | request\_\_decision\_info\_\_value10 | 20 |  |  |  |  | FALSE |
| 978 | request\_\_network\_data\_visibility\_config\_\_data\_right\_\_right | 20 |  |  |  |  | FALSE |
| 979 | request\_\_experiment\_platform\_\_experiment\_\_parameter\_\_value | 20 |  |  |  |  | FALSE |
| 980 | request\_\_yield\_optimization\_ids | 20 |  |  |  |  | FALSE |
| 981 | request\_\_soft\_guaranteed\_ad\_\_entity\_type | 20 |  |  |  |  | FALSE |
| 982 | request\_\_decision\_info\_\_reject\_ads | 20 |  |  |  |  | FALSE |
| 983 | request\_\_userdb\_audience\_user\_info | 20 |  |  |  |  | FALSE |
| 984 | request\_\_soft\_guaranteed\_ad | 20 |  |  |  |  | FALSE |
| 985 | request\_\_scores\_\_ad\_id | 20 |  |  |  |  | FALSE |
| 986 | request\_\_context\_\_po\_id | 20 |  |  |  |  | FALSE |
| 987 | request\_\_linear\_capnedit\_\_mode | 20 |  |  |  |  | FALSE |
| 988 | request\_\_request\_throttling\_info\_\_level | 20 |  |  |  |  | FALSE |
| 989 | request\_\_cbp\_\_network\_id | 20 |  |  |  |  | FALSE |
| 990 | request\_\_scores | 20 |  |  |  |  | FALSE |
| 991 | ack\_\_metrics\_\_break\_starts | 20 |  |  |  |  | FALSE |
| 992 | request\_\_phantom\_candidate\_\_creative\_id | 20 |  |  |  |  | FALSE |
| 993 | request\_\_extra\_geo\_info\_\_descriptions | 20 |  |  |  |  | FALSE |
| 994 | request\_\_decision\_info\_\_external\_bridge\_\_slot\_index | 20 |  |  |  |  | FALSE |
| 995 | request\_\_userdb\_audience\_user\_info\_\_num\_keys | 20 |  |  |  |  | FALSE |
| 996 | request\_\_mpe\_matcher\_filters | 20 |  |  |  |  | FALSE |
| 997 | request\_\_context\_\_video\_cro\_context\_group\_id | 20 |  |  |  |  | FALSE |
| 998 | request\_\_context\_\_uri | 20 |  |  |  |  | FALSE |
| 999 | request\_\_decision\_info\_\_external\_bridge\_\_status | 20 |  |  |  |  | FALSE |
| 1000 | request\_\_context\_\_casu\_id | 20 |  |  |  |  | FALSE |
| 1001 | request\_\_network\_data\_visibility\_config\_\_data\_right | 20 |  |  |  |  | FALSE |
| 1002 | request\_\_request\_prefilter | 20 |  |  |  |  | FALSE |
| 1003 | request\_\_log\_sampling | 20 |  |  |  |  | FALSE |
| 1004 | request\_\_context\_\_custom\_airing\_channel\_id | 20 |  |  |  |  | FALSE |
| 1005 | request\_\_extra\_geo\_info\_\_ids | 20 |  |  |  |  | FALSE |
| 1006 | request\_\_context\_\_airing\_channel\_id | 20 |  |  |  |  | FALSE |
| 1007 | request\_\_decision\_info\_\_reject\_ads\_\_ad\_reason | 20 |  |  |  |  | FALSE |
| 1008 | request\_\_network\_data\_visibility\_config | 20 |  |  |  |  | FALSE |
| 1009 | request\_\_gateway\_ingested\_supply\_cost | 20 |  |  |  |  | FALSE |
| 1010 | request\_\_decision\_info\_\_value14 | 20 |  |  |  |  | FALSE |
| 1011 | request\_\_network\_data\_visibility\_config\_\_visitor\_custom\_id\_visibility | 20 |  |  |  |  | FALSE |
| 1012 | request\_\_decision\_info\_\_value9 | 20 |  |  |  |  | FALSE |
| 1013 | request\_\_guaranteed\_deal\_avail | 20 |  |  |  |  | FALSE |
| 1014 | request\_\_network\_data\_visibility\_config\_\_data\_right\_\_field | 20 |  |  |  |  | FALSE |
| 1015 | request\_\_network\_ctx | 20 |  |  |  |  | FALSE |
| 1016 | request\_\_request\_throttling\_info\_\_model\_info\_\_model\_id | 20 |  |  |  |  | FALSE |
| 1017 | request\_\_cbp | 20 |  |  |  |  | FALSE |
| 1018 | advertisement\_\_fill\_rate | 20 |  |  |  |  | FALSE |
| 1019 | request\_\_context\_\_ux\_network\_id | 20 |  |  |  |  | FALSE |
| 1020 | request\_\_context\_\_custom\_distributor\_signature | 20 |  |  |  |  | FALSE |
| 1021 | request\_\_decision\_info\_\_networks | 20 |  |  |  |  | FALSE |
| 1022 | request\_\_identifier\_\_sequence | 20 |  |  |  |  | FALSE |
| 1023 | request\_\_experiment\_platform | 20 |  |  |  |  | FALSE |
| 1024 | request\_\_extra\_geo\_info\_\_edge\_networks | 20 |  |  |  |  | FALSE |
| 1025 | request\_\_decision\_info\_\_value12 | 20 |  |  |  |  | FALSE |
| 1026 | request\_\_userdb\_audience\_user\_info\_\_dx\_query\_key | 20 |  |  |  |  | FALSE |
| 1027 | request\_\_network\_ctx\_\_network\_id | 20 |  |  |  |  | FALSE |
| 1028 | request\_\_phantom\_candidate\_\_rendition\_id | 20 |  |  |  |  | FALSE |
| 1029 | request\_\_decision\_info | 20 |  |  |  |  | FALSE |
| 1030 | request\_\_decision\_info\_\_value11 | 20 |  |  |  |  | FALSE |
| 1031 | request\_\_log\_version\_\_major\_release\_version | 20 |  |  |  |  | FALSE |
| 1032 | request\_\_yield\_optimization\_ids\_\_demand\_type | 20 |  |  |  |  | FALSE |
| 1033 | request\_\_yield\_optimization\_ids\_\_optimization\_ids | 20 |  |  |  |  | FALSE |
| 1034 | request\_\_decision\_info\_\_decision\_log | 20 |  |  |  |  | FALSE |
| 1035 | request\_\_experiment\_platform\_\_experiment | 20 |  |  |  |  | FALSE |
| 1036 | request\_\_context\_\_custom\_distributor\_category | 20 |  |  |  |  | FALSE |
| 1037 | request\_\_decision\_info\_\_inventory\_protections | 20 |  |  |  |  | FALSE |
| 1038 | visitor\_\_internal\_user\_id | 20 |  |  |  |  | FALSE |
| 1039 | data\_partition | 20 |  |  |  |  | FALSE |
| 1040 | request\_\_vod\_session\_id | 20 |  |  |  |  | FALSE |
| 1041 | request\_\_prebid\_sivt\_\_capnedit | 20 |  |  |  |  | FALSE |
| 1042 | request\_\_context\_\_website\_root\_id | 20 |  |  |  |  | FALSE |
| 1043 | request\_\_time\_record\_\_external\_candidate | 20 |  |  |  |  | FALSE |
| 1044 | request\_\_experiment\_platform\_\_experiment\_\_partition\_index | 20 |  |  |  |  | FALSE |
| 1045 | request\_\_decision\_info\_\_external\_bridge | 20 |  |  |  |  | FALSE |
| 1046 | request\_\_decision\_info\_\_reject\_ads\_\_ad\_id | 20 |  |  |  |  | FALSE |
| 1047 | request\_\_prebid\_sivt | 20 |  |  |  |  | FALSE |
| 1048 | request\_\_time\_record\_\_external\_creative | 20 |  |  |  |  | FALSE |
| 1049 | request\_\_time\_record\_\_external\_sds | 20 |  |  |  |  | FALSE |
| 1050 | request\_\_yield\_optimization\_ids\_\_demand\_id | 20 |  |  |  |  | FALSE |
| 1051 | request\_\_log\_version | 20 |  |  |  |  | FALSE |
| 1052 | request\_\_userdb\_audience\_user\_info\_\_dx\_query\_key\_\_set | 20 |  |  |  |  | FALSE |
| 1053 | request\_\_soft\_guaranteed\_ad\_\_entity\_id | 20 |  |  |  |  | FALSE |
| 1054 | request\_\_userdb\_audience\_user\_info\_\_bg\_query\_key\_\_set | 20 |  |  |  |  | FALSE |
| 1055 | request\_\_linear\_capnedit\_\_last\_activity\_time | 20 |  |  |  |  | FALSE |
| 1056 | request\_\_log\_version\_\_build | 20 |  |  |  |  | FALSE |
| 1057 | request\_\_context\_\_ab\_test\_item\_\_is\_effective | 20 |  |  |  |  | FALSE |
| 1058 | request\_\_process\_timestamp | 20 |  |  |  |  | FALSE |
| 1059 | request\_\_context\_\_request\_trace\_id | 20 |  |  |  |  | FALSE |
| 1060 | \_\_file\_size\_\_ | 20 |  |  |  |  | FALSE |
| 1061 | request\_\_experiment\_platform\_\_experiment\_\_experiment\_id | 20 |  |  |  |  | FALSE |
| 1062 | request\_\_context\_\_p2\_handler\_source | 20 |  |  |  |  | FALSE |
| 1063 | request\_\_phantom\_candidate\_\_ad\_id | 20 |  |  |  |  | FALSE |
| 1064 | request\_\_request\_throttling\_info | 20 |  |  |  |  | FALSE |
| 1065 | request\_\_network\_data\_visibility\_config\_\_key\_value\_visibility | 20 |  |  |  |  | FALSE |
| 1066 | request\_\_simulated\_tiemstamp | 20 |  |  |  |  | FALSE |
| 1067 | request\_\_decision\_info\_\_inventory\_protections\_\_level | 20 |  |  |  |  | FALSE |
| 1068 | request\_\_request\_throttling\_info\_\_model\_info | 20 |  |  |  |  | FALSE |
| 1069 | request\_\_userdb\_audience\_user\_info\_\_bg\_query\_key\_\_key | 20 |  |  |  |  | FALSE |
| 1070 | request\_\_userdb\_audience\_user\_info\_\_dx\_alias\_growth\_ratio | 20 |  |  |  |  | FALSE |
| 1071 | \_\_offset\_\_ | 20 |  |  |  |  | FALSE |
| 1072 | request\_\_phantom\_candidate\_\_position\_in\_slot | 20 |  |  |  |  | FALSE |
| 1073 | request\_\_network\_data\_visibility\_config\_\_network\_id | 20 |  |  |  |  | FALSE |
| 1074 | request\_\_network\_data\_visibility\_config\_\_visible\_data\_fields\_mask | 20 |  |  |  |  | FALSE |
| 1075 | request\_\_userdb\_audience\_user\_info\_\_dx\_query\_key\_\_key | 20 |  |  |  |  | FALSE |
| 1076 | request\_\_network\_data\_visibility\_config\_\_device\_id\_visibility | 20 |  |  |  |  | FALSE |
| 1077 | request\_\_context\_\_ssto | 20 |  |  |  |  | FALSE |
| 1078 | request\_\_experiment\_platform\_\_experiment\_\_parameter\_\_id | 20 |  |  |  |  | FALSE |
| 1079 | request\_\_experiment\_platform\_\_experiment\_\_parameter | 20 |  |  |  |  | FALSE |
| 1080 | request\_\_userdb\_audience\_user\_info\_\_bg\_query\_key | 20 |  |  |  |  | FALSE |
| 1081 | request\_\_linear\_capnedit\_\_active\_state | 20 |  |  |  |  | FALSE |
| 1082 | request\_\_private\_data\_accessible\_networks | 20 |  |  |  |  | FALSE |
| 1083 | request\_\_soft\_guaranteed\_ad\_\_ad\_id | 20 |  |  |  |  | FALSE |
| 1084 | request\_\_decision\_info\_\_inventory\_protections\_\_separation | 20 |  |  |  |  | FALSE |
| 1085 | request\_\_log\_version\_\_major\_version | 20 |  |  |  |  | FALSE |
| 1086 | request\_\_experiment\_platform\_\_experiment\_\_flags | 20 |  |  |  |  | FALSE |
| 1087 | request\_\_privacy\_info\_\_gdpr\_cmp\_id | 20 |  |  |  |  | FALSE |
| 1088 | request\_\_userdb\_audience\_user\_info\_\_num\_dx\_enriched\_keys | 20 |  |  |  |  | FALSE |
| 1089 | request\_\_log\_version\_\_minor\_release\_version | 20 |  |  |  |  | FALSE |
| 1090 | visitor\_\_referrer\_banning\_rule\_id | 20 |  |  |  |  | FALSE |
| 1091 | request\_\_decision\_info\_\_reject\_ads\_\_slot\_reason | 20 |  |  |  |  | FALSE |
| 1092 | request\_\_soft\_guaranteed\_ad\_\_num\_competing\_ads | 20 |  |  |  |  | FALSE |
| 1093 | idx | 20 |  |  |  |  | FALSE |
| 1094 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 19 |  |  |  |  | FALSE |
| 1095 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 19 |  |  |  |  | FALSE |
| 1096 | request\_\_context\_\_extracted\_key\_value | 19 |  |  |  |  | FALSE |
| 1097 | visitor\_\_user\_group | 19 |  |  |  |  | FALSE |
| 1098 | visitor\_\_flags | 19 |  |  |  |  | FALSE |
| 1099 | advertisement\_\_data\_provider\_id | 18 |  |  |  |  | FALSE |
| 1100 | request\_\_bid\_request\_\_site\_domain | 18 |  |  |  |  | FALSE |
| 1101 | execution\_networks\_\_tracked\_audience\_item\_ids | 17 |  |  |  |  | FALSE |
| 1102 | visitor\_\_user\_agent\_device\_id | 17 |  |  |  |  | FALSE |
| 1103 | request\_\_bid\_request\_\_inventory\_source | 17 |  |  |  |  | FALSE |
| 1104 | execution\_networks\_\_non\_tracked\_audience\_item\_ids | 17 |  |  |  |  | FALSE |
| 1105 | inventory\_\_site\_section\_chain\_\_site\_section\_id | 16 |  |  |  |  | FALSE |
| 1106 | advertisement\_\_cch\_key | 16 |  |  |  |  | FALSE |
| 1107 | candidate\_\_dsp\_clearing\_price | 16 |  |  |  |  | FALSE |
| 1108 | request\_\_audience\_item\_\_network\_id | 16 |  |  |  |  | FALSE |
| 1109 | request\_\_network\_execution\_ctx\_\_network\_id | 16 |  |  |  |  | FALSE |
| 1110 | candidate\_\_dsp\_clearing\_price\_discounted | 16 |  |  |  |  | FALSE |
| 1111 | slot\_\_slot\_sequence | 16 |  |  |  |  | FALSE |
| 1112 | request\_\_client\_facing\_reason\_code | 16 |  |  |  |  | FALSE |
| 1113 | visitor\_\_tracked\_audience\_item\_ids | 16 |  |  |  |  | FALSE |
| 1114 | advertisement\_\_matched\_postal\_code\_package\_ids | 15 |  |  |  |  | FALSE |
| 1115 | advertisement\_\_matched\_postal\_code\_ids | 15 |  |  |  |  | FALSE |
| 1116 | advertisement\_\_matched\_region\_ids | 15 |  |  |  |  | FALSE |
| 1117 | request\_\_visitor\_\_standard\_operator\_id | 15 |  |  |  |  | FALSE |
| 1118 | request\_\_visitor\_\_parsed\_user\_agent | 15 |  |  |  |  | FALSE |
| 1119 | slot\_\_raw\_max\_duration | 15 |  |  |  |  | FALSE |
| 1120 | advertisement\_\_matched\_geo\_ids | 15 |  |  |  |  | FALSE |
| 1121 | request\_\_advertisements\_\_active\_aim\_audience\_ids | 15 |  |  |  |  | FALSE |
| 1122 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_ids | 15 |  |  |  |  | FALSE |
| 1123 | advertisement\_\_matched\_key\_value\_ids | 15 |  |  |  |  | FALSE |
| 1124 | request\_\_slots\_\_carriage\_inventory\_owner\_id | 15 |  |  |  |  | FALSE |
| 1125 | visitor\_\_universal\_iids | 14 |  |  |  |  | FALSE |
| 1126 | request\_\_bid\_request\_\_impression\_\_deal\_\_currency | 14 |  |  |  |  | FALSE |
| 1127 | advertisement\_\_effective\_exclude\_aim\_audience\_ids | 14 |  |  |  |  | FALSE |
| 1128 | request\_\_context\_\_rbp\_device\_type | 14 |  |  |  |  | FALSE |
| 1129 | visitor\_\_private\_universal\_iid\_\_authorized\_network\_ids | 14 |  |  |  |  | FALSE |
| 1130 | request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos | 14 |  |  |  |  | FALSE |
| 1131 | visitor\_\_postal\_code\_package\_\_postal\_code\_package\_id | 14 |  |  |  |  | FALSE |
| 1132 | visitor\_\_private\_universal\_hhid\_\_id | 14 |  |  |  |  | FALSE |
| 1133 | visitor\_\_postal\_code\_package | 14 |  |  |  |  | FALSE |
| 1134 | request\_\_is\_all\_data\_visibility | 14 |  |  |  |  | FALSE |
| 1135 | request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 14 |  |  |  |  | FALSE |
| 1136 | request\_\_bid\_request\_\_impression\_\_deal\_\_auction\_type | 14 |  |  |  |  | FALSE |
| 1137 | visitor\_\_identity\_user\_ids\_\_authorized\_network\_id | 14 |  |  |  |  | FALSE |
| 1138 | request\_\_bid\_request\_\_impression\_\_deal\_\_floor | 14 |  |  |  |  | FALSE |
| 1139 | visitor\_\_ortb\_fields\_from\_ua | 14 |  |  |  |  | FALSE |
| 1140 | acks\_\_metrics\_\_raw\_ad\_impression | 14 |  |  |  |  | FALSE |
| 1141 | request\_\_privacy\_choice\_ids | 14 |  |  |  |  | FALSE |
| 1142 | idx\_\_process\_batch\_id | 14 |  |  |  |  | FALSE |
| 1143 | request\_\_privacy\_jurisdiction\_ids | 14 |  |  |  |  | FALSE |
| 1144 | visitor\_\_session\_id | 14 |  |  |  |  | FALSE |
| 1145 | request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos | 14 |  |  |  |  | FALSE |
| 1146 | request\_\_client\_facing\_ivt\_reason\_flag | 14 |  |  |  |  | FALSE |
| 1147 | request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 14 |  |  |  |  | FALSE |
| 1148 | visitor\_\_isp | 14 |  |  |  |  | FALSE |
| 1149 | request\_\_context\_\_site\_section\_cro\_parsed\_site\_section\_id | 14 |  |  |  |  | FALSE |
| 1150 | visitor\_\_private\_universal\_hhid | 14 |  |  |  |  | FALSE |
| 1151 | request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 14 |  |  |  |  | FALSE |
| 1152 | visitor\_\_identity\_user\_ids\_\_namespace\_id | 14 |  |  |  |  | FALSE |
| 1153 | candidate\_\_deal\_id | 14 |  |  |  |  | FALSE |
| 1154 | visitor\_\_xfinity\_idfa | 14 |  |  |  |  | FALSE |
| 1155 | inventory\_\_asset\_chain | 14 |  |  |  |  | FALSE |
| 1156 | visitor\_\_flash\_version | 14 |  |  |  |  | FALSE |
| 1157 | request\_\_context\_\_video\_cro\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 14 |  |  |  |  | FALSE |
| 1158 | visitor\_\_accept\_language | 14 |  |  |  |  | FALSE |
| 1159 | visitor\_\_city | 14 |  |  |  |  | FALSE |
| 1160 | request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_ids | 14 |  |  |  |  | FALSE |
| 1161 | request\_\_bid\_request\_\_impression\_\_currency | 14 |  |  |  |  | FALSE |
| 1162 | request\_\_bid\_request\_\_impression\_\_deal | 14 |  |  |  |  | FALSE |
| 1163 | idx\_\_version | 14 |  |  |  |  | FALSE |
| 1164 | request\_\_bid\_request\_\_auction\_type | 14 |  |  |  |  | FALSE |
| 1165 | visitor | 14 |  |  |  |  | FALSE |
| 1166 | request\_\_bid\_request\_\_app\_name | 14 |  |  |  |  | FALSE |
| 1167 | visitor\_\_private\_universal\_hhid\_\_authorized\_network\_ids | 14 |  |  |  |  | FALSE |
| 1168 | visitor\_\_tracked\_term | 14 |  |  |  |  | FALSE |
| 1169 | request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_type | 14 |  |  |  |  | FALSE |
| 1170 | idx\_\_kafka\_msg\_key | 14 |  |  |  |  | FALSE |
| 1171 | visitor\_\_postal\_code\_package\_\_network\_id | 14 |  |  |  |  | FALSE |
| 1172 | request\_\_bid\_request\_\_site\_page\_hash | 14 |  |  |  |  | FALSE |
| 1173 | visitor\_\_private\_universal\_iid | 14 |  |  |  |  | FALSE |
| 1174 | request\_\_is\_no\_selection | 14 |  |  |  |  | FALSE |
| 1175 | request\_\_context\_\_tv\_network\_group\_ids | 14 |  |  |  |  | FALSE |
| 1176 | idx\_\_process\_timestamp | 14 |  |  |  |  | FALSE |
| 1177 | visitor\_\_programmer\_individual\_id | 14 |  |  |  |  | FALSE |
| 1178 | visitor\_\_isp\_id | 14 |  |  |  |  | FALSE |
| 1179 | visitor\_\_postal\_code\_id | 14 |  |  |  |  | FALSE |
| 1180 | request\_\_slots\_\_min\_duration | 14 |  |  |  |  | FALSE |
| 1181 | request\_\_context\_\_video\_cro\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id | 14 |  |  |  |  | FALSE |
| 1182 | request\_\_context\_\_video\_cro\_yield\_optimization\_ids | 14 |  |  |  |  | FALSE |
| 1183 | request\_\_external\_bridge\_records\_\_slot\_index | 14 |  |  |  |  | FALSE |
| 1184 | visitor\_\_private\_universal\_iid\_\_id | 14 |  |  |  |  | FALSE |
| 1185 | request\_\_bid\_request\_\_impression | 14 |  |  |  |  | FALSE |
| 1186 | partners\_\_standard\_endpoint\_visibility | 14 |  |  |  |  | FALSE |
| 1187 | partners\_\_outbound\_rules\_\_rule\_id | 14 |  |  |  |  | FALSE |
| 1188 | auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags | 13 |  |  |  |  | FALSE |
| 1189 | advertisement\_\_cch\_rendition\_id | 13 |  |  |  |  | FALSE |
| 1190 | candidate\_\_cch\_key\_domain\_config\_id | 13 |  |  |  |  | FALSE |
| 1191 | request\_\_advertisements\_\_content\_right\_owner\_\_down\_revenue | 13 |  |  |  |  | FALSE |
| 1192 | inventory\_\_site\_section\_chain | 13 |  |  |  |  | FALSE |
| 1193 | inventory\_\_site\_section\_chain\_\_matched\_audience\_item\_ids | 13 |  |  |  |  | FALSE |
| 1194 | auction\_\_network\_execution\_ctx\_index | 13 |  |  |  |  | FALSE |
| 1195 | inventory\_\_site\_section\_chain\_\_asset\_group\_ids | 13 |  |  |  |  | FALSE |
| 1196 | inventory\_\_site\_section\_chain\_\_asset\_id | 13 |  |  |  |  | FALSE |
| 1197 | aim\_info | 13 |  |  |  |  | FALSE |
| 1198 | request\_\_rtb\_auction\_\_impression\_\_bid\_floor | 13 |  |  |  |  | FALSE |
| 1199 | partners\_\_audience\_segment\_max\_cpm | 12 |  |  |  |  | FALSE |
| 1200 | auction\_\_impression\_\_max\_duration | 12 |  |  |  |  | FALSE |
| 1201 | advertisement\_\_matched\_inventory\_package\_ids | 12 |  |  |  |  | FALSE |
| 1202 | partners\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 12 |  |  |  |  | FALSE |
| 1203 | inventory\_\_asset\_chain\_\_asset\_group\_ids | 12 |  |  |  |  | FALSE |
| 1204 | audiences | 12 |  |  |  |  | FALSE |
| 1205 | partners\_\_audience\_partner\_segment\_infos | 12 |  |  |  |  | FALSE |
| 1206 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_down\_revenue | 12 |  |  |  |  | FALSE |
| 1207 | advertisement | 12 |  |  |  |  | FALSE |
| 1208 | inventory\_\_asset\_chain\_\_geo\_visibility\_\_report\_aggregate | 12 |  |  |  |  | FALSE |
| 1209 | inventory\_\_asset\_chain\_\_matched\_audience\_item\_ids | 12 |  |  |  |  | FALSE |
| 1210 | inventory\_\_asset\_chain\_\_site\_section\_group\_ids | 12 |  |  |  |  | FALSE |
| 1211 | aim\_info\_\_aim\_identity\_info\_\_categorized\_signals\_\_type | 12 |  |  |  |  | FALSE |
| 1212 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1213 | inventory\_\_asset\_chain\_\_revenue | 11 |  |  |  |  | FALSE |
| 1214 | inventory\_\_asset\_chain\_\_inbound\_order\_type | 11 |  |  |  |  | FALSE |
| 1215 | inventory\_\_asset\_chain\_\_standard\_content\_territory\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1216 | inventory\_\_asset\_chain\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1217 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 11 |  |  |  |  | FALSE |
| 1218 | inventory\_\_asset\_chain\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1219 | request\_\_advertisements\_\_content\_owner | 11 |  |  |  |  | FALSE |
| 1220 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 11 |  |  |  |  | FALSE |
| 1221 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | 11 |  |  |  |  | FALSE |
| 1222 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 11 |  |  |  |  | FALSE |
| 1223 | inventory\_\_site\_section\_chain\_\_selected\_yo\_inventory\_prioritization\_nip\_id | 11 |  |  |  |  | FALSE |
| 1224 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 11 |  |  |  |  | FALSE |
| 1225 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status | 11 |  |  |  |  | FALSE |
| 1226 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 11 |  |  |  |  | FALSE |
| 1227 | inventory\_\_site\_section\_chain\_\_geo\_country\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1228 | inventory\_\_asset\_chain\_\_geo\_city\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1229 | inventory\_\_site\_section\_chain\_\_key\_value\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1230 | inventory\_\_asset\_chain\_\_carriage\_inventory\_owner\_id | 11 |  |  |  |  | FALSE |
| 1231 | inventory\_\_site\_section\_chain\_\_site\_group\_id | 11 |  |  |  |  | FALSE |
| 1232 | inventory\_\_asset\_chain\_\_standard\_content\_credential\_status\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1233 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_bit\_flags | 11 |  |  |  |  | FALSE |
| 1234 | inventory\_\_asset\_chain\_\_geo\_state\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1235 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 11 |  |  |  |  | FALSE |
| 1236 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1237 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 11 |  |  |  |  | FALSE |
| 1238 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase | 11 |  |  |  |  | FALSE |
| 1239 | inventory\_\_asset\_chain\_\_airing\_channel\_group\_id | 11 |  |  |  |  | FALSE |
| 1240 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1241 | inventory\_\_asset\_chain\_\_avails\_category\_\_vod\_programmer\_total\_avails | 11 |  |  |  |  | FALSE |
| 1242 | inventory\_\_asset\_chain\_\_standard\_language\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1243 | inventory\_\_site\_section\_chain\_\_standard\_genre\_visibility | 11 |  |  |  |  | FALSE |
| 1244 | inventory\_\_site\_section\_chain\_\_standard\_content\_territory\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1245 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 11 |  |  |  |  | FALSE |
| 1246 | request\_\_rtb\_auction\_\_dsp\_id | 11 |  |  |  |  | FALSE |
| 1247 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1248 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | 11 |  |  |  |  | FALSE |
| 1249 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 11 |  |  |  |  | FALSE |
| 1250 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | 11 |  |  |  |  | FALSE |
| 1251 | inventory\_\_asset\_chain\_\_internal\_seat\_ids | 11 |  |  |  |  | FALSE |
| 1252 | request\_\_prev\_transaction\_id | 11 |  |  |  |  | FALSE |
| 1253 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 11 |  |  |  |  | FALSE |
| 1254 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1255 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails | 11 |  |  |  |  | FALSE |
| 1256 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | 11 |  |  |  |  | FALSE |
| 1257 | inventory\_\_site\_section\_chain\_\_priority\_value | 11 |  |  |  |  | FALSE |
| 1258 | inventory\_\_site\_section\_chain\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | 11 |  |  |  |  | FALSE |
| 1259 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_order\_id | 11 |  |  |  |  | FALSE |
| 1260 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1261 | inventory\_\_asset\_chain\_\_rule\_id | 11 |  |  |  |  | FALSE |
| 1262 | inventory\_\_site\_section\_chain\_\_outbound\_rules\_\_rule\_id | 11 |  |  |  |  | FALSE |
| 1263 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 11 |  |  |  |  | FALSE |
| 1264 | inventory\_\_asset\_chain\_\_standard\_content\_credential\_status\_visibility | 11 |  |  |  |  | FALSE |
| 1265 | inventory\_\_asset\_chain\_\_geo\_dma\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1266 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 11 |  |  |  |  | FALSE |
| 1267 | inventory\_\_site\_section\_chain\_\_network\_is\_extra\_item\_owner | 11 |  |  |  |  | FALSE |
| 1268 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1269 | inventory\_\_asset\_chain\_\_ip\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1270 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_owner\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1271 | inventory\_\_asset\_chain\_\_break\_id | 11 |  |  |  |  | FALSE |
| 1272 | inventory\_\_site\_section\_chain\_\_geo\_zip\_code\_visibility | 11 |  |  |  |  | FALSE |
| 1273 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1274 | inventory\_\_site\_section\_chain\_\_selected\_yo\_margin\_id | 11 |  |  |  |  | FALSE |
| 1275 | inventory\_\_site\_section\_chain\_\_standard\_brand\_visibility | 11 |  |  |  |  | FALSE |
| 1276 | inventory\_\_site\_section\_chain\_\_standard\_content\_credential\_status\_visibility | 11 |  |  |  |  | FALSE |
| 1277 | inventory\_\_asset\_chain\_\_standard\_endpoint\_visibility | 11 |  |  |  |  | FALSE |
| 1278 | inventory\_\_site\_section\_chain\_\_geo\_visibility | 11 |  |  |  |  | FALSE |
| 1279 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1280 | inventory\_\_asset\_chain\_\_geo\_state\_visibility | 11 |  |  |  |  | FALSE |
| 1281 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails | 11 |  |  |  |  | FALSE |
| 1282 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 11 |  |  |  |  | FALSE |
| 1283 | inventory\_\_site\_section\_chain\_\_role | 11 |  |  |  |  | FALSE |
| 1284 | inventory\_\_site\_section\_chain\_\_content\_rating\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1285 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails | 11 |  |  |  |  | FALSE |
| 1286 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1287 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 11 |  |  |  |  | FALSE |
| 1288 | inventory\_\_asset\_chain\_\_unified\_rule\_priority\_\_sub\_priority\_value | 11 |  |  |  |  | FALSE |
| 1289 | inventory\_\_asset\_chain\_\_standard\_content\_series\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1290 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1291 | inventory\_\_site\_section\_chain\_\_matched\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1292 | inventory\_\_site\_section\_chain\_\_upstream\_inbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1293 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_order\_type | 11 |  |  |  |  | FALSE |
| 1294 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1295 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1296 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 11 |  |  |  |  | FALSE |
| 1297 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1298 | inventory\_\_site\_section\_chain\_\_standard\_brand\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1299 | inventory\_\_site\_section\_chain\_\_standard\_genre\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1300 | inventory\_\_asset\_chain\_\_selected\_yo\_distribution\_id | 11 |  |  |  |  | FALSE |
| 1301 | inventory\_\_site\_section\_chain\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 11 |  |  |  |  | FALSE |
| 1302 | inventory\_\_site\_section\_chain\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1303 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 11 |  |  |  |  | FALSE |
| 1304 | inventory\_\_asset\_chain\_\_geo\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1305 | inventory | 11 |  |  |  |  | FALSE |
| 1306 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 11 |  |  |  |  | FALSE |
| 1307 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_owner\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1308 | inventory\_\_site\_section\_chain\_\_standard\_content\_daypart\_visibility | 11 |  |  |  |  | FALSE |
| 1309 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 11 |  |  |  |  | FALSE |
| 1310 | inventory\_\_asset\_chain\_\_avails\_category\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1311 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_order\_ids | 11 |  |  |  |  | FALSE |
| 1312 | inventory\_\_site\_section\_chain\_\_device\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1313 | inventory\_\_asset\_chain\_\_standard\_channel\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1314 | inventory\_\_asset\_chain\_\_unified\_outbound\_order\_priority | 11 |  |  |  |  | FALSE |
| 1315 | inventory\_\_site\_section\_chain\_\_standard\_content\_credential\_status\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1316 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1317 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration | 11 |  |  |  |  | FALSE |
| 1318 | inventory\_\_asset\_chain\_\_carriage\_listing\_split\_unit\_id | 11 |  |  |  |  | FALSE |
| 1319 | inventory\_\_asset\_chain\_\_standard\_content\_territory\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1320 | inventory\_\_asset\_chain\_\_inbound\_rule\_id | 11 |  |  |  |  | FALSE |
| 1321 | inventory\_\_asset\_chain\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1322 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1323 | inventory\_\_site\_section\_chain\_\_inbound\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1324 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1325 | inventory\_\_site\_section\_chain\_\_internal\_seat\_ids | 11 |  |  |  |  | FALSE |
| 1326 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 11 |  |  |  |  | FALSE |
| 1327 | inventory\_\_asset\_chain\_\_marketplace\_audience\_extension\_deal\_ids | 11 |  |  |  |  | FALSE |
| 1328 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1329 | inventory\_\_site\_section\_chain\_\_airing\_channel\_group\_id | 11 |  |  |  |  | FALSE |
| 1330 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 11 |  |  |  |  | FALSE |
| 1331 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1332 | inventory\_\_asset\_chain\_\_standard\_content\_credential\_status\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1333 | inventory\_\_site\_section\_chain\_\_geo\_zip\_code\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1334 | inventory\_\_site\_section\_chain\_\_outbound\_rules\_\_win\_opp | 11 |  |  |  |  | FALSE |
| 1335 | inventory\_\_asset\_chain\_\_outbound\_order\_priority\_type | 11 |  |  |  |  | FALSE |
| 1336 | inventory\_\_site\_section\_chain\_\_standard\_content\_credential\_status\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1337 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1338 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration | 11 |  |  |  |  | FALSE |
| 1339 | inventory\_\_site\_section\_chain\_\_postal\_code\_package\_id | 11 |  |  |  |  | FALSE |
| 1340 | inventory\_\_asset\_chain\_\_unified\_rule\_priority | 11 |  |  |  |  | FALSE |
| 1341 | inventory\_\_site\_section\_chain\_\_device\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1342 | inventory\_\_site\_section\_chain\_\_standard\_content\_territory\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1343 | inventory\_\_asset\_chain\_\_content\_form\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1344 | inventory\_\_asset\_chain\_\_tracked\_audience\_item\_ids | 11 |  |  |  |  | FALSE |
| 1345 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 11 |  |  |  |  | FALSE |
| 1346 | inventory\_\_site\_section\_chain\_\_standard\_programmer\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1347 | inventory\_\_asset\_chain\_\_bidder\_seat\_id | 11 |  |  |  |  | FALSE |
| 1348 | inventory\_\_asset\_chain\_\_geo\_dma\_visibility | 11 |  |  |  |  | FALSE |
| 1349 | inventory\_\_site\_section\_chain\_\_count\_imp\_as\_booked | 11 |  |  |  |  | FALSE |
| 1350 | inventory\_\_site\_section\_chain\_\_standard\_programmer\_visibility | 11 |  |  |  |  | FALSE |
| 1351 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 11 |  |  |  |  | FALSE |
| 1352 | inventory\_\_asset\_chain\_\_non\_tracked\_audience\_item\_ids | 11 |  |  |  |  | FALSE |
| 1353 | inventory\_\_asset\_chain\_\_supply\_source | 11 |  |  |  |  | FALSE |
| 1354 | inventory\_\_site\_section\_chain\_\_distributor\_network\_id | 11 |  |  |  |  | FALSE |
| 1355 | inventory\_\_asset\_chain\_\_asset\_group\_id | 11 |  |  |  |  | FALSE |
| 1356 | inventory\_\_asset\_chain\_\_outbound\_exchange\_order\_id | 11 |  |  |  |  | FALSE |
| 1357 | inventory\_\_site\_section\_chain\_\_unified\_outbound\_order\_priority | 11 |  |  |  |  | FALSE |
| 1358 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id | 11 |  |  |  |  | FALSE |
| 1359 | inventory\_\_site\_section\_chain\_\_standard\_content\_daypart\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1360 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 11 |  |  |  |  | FALSE |
| 1361 | inventory\_\_site\_section\_chain\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1362 | inventory\_\_asset\_chain\_\_standard\_language\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1363 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1364 | inventory\_\_asset\_chain\_\_avails\_category\_\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1365 | inventory\_\_site\_section\_chain\_\_upstream\_content\_owner\_revenue\_in\_up\_currency | 11 |  |  |  |  | FALSE |
| 1366 | inventory\_\_site\_section\_chain\_\_reseller\_revenue | 11 |  |  |  |  | FALSE |
| 1367 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1368 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 11 |  |  |  |  | FALSE |
| 1369 | inventory\_\_site\_section\_chain\_\_rule\_type\_priority | 11 |  |  |  |  | FALSE |
| 1370 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails | 11 |  |  |  |  | FALSE |
| 1371 | inventory\_\_site\_section\_chain\_\_scenario\_id | 11 |  |  |  |  | FALSE |
| 1372 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | 11 |  |  |  |  | FALSE |
| 1373 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1374 | inventory\_\_site\_section\_chain\_\_content\_form\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1375 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1376 | inventory\_\_asset\_chain\_\_avails\_category\_\_avails | 11 |  |  |  |  | FALSE |
| 1377 | inventory\_\_site\_section\_chain\_\_geo\_country\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1378 | inventory\_\_asset\_chain\_\_standard\_language\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1379 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1380 | inventory\_\_asset\_chain\_\_outbound\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1381 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type | 11 |  |  |  |  | FALSE |
| 1382 | inventory\_\_asset\_chain\_\_standard\_content\_series\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1383 | inventory\_\_site\_section\_chain\_\_reseller\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1384 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1385 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1386 | inventory\_\_asset\_chain\_\_network\_selection\_info | 11 |  |  |  |  | FALSE |
| 1387 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1388 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_listing\_id | 11 |  |  |  |  | FALSE |
| 1389 | inventory\_\_asset\_chain\_\_demand\_dim\_awareability | 11 |  |  |  |  | FALSE |
| 1390 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id | 11 |  |  |  |  | FALSE |
| 1391 | inventory\_\_site\_section\_chain\_\_standard\_content\_subscription\_model\_visibility | 11 |  |  |  |  | FALSE |
| 1392 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 11 |  |  |  |  | FALSE |
| 1393 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 11 |  |  |  |  | FALSE |
| 1394 | inventory\_\_site\_section\_chain\_\_outbound\_order\_type | 11 |  |  |  |  | FALSE |
| 1395 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1396 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 11 |  |  |  |  | FALSE |
| 1397 | inventory\_\_asset\_chain\_\_geo\_city\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1398 | inventory\_\_site\_section\_chain\_\_carriage\_listing\_split\_unit\_id | 11 |  |  |  |  | FALSE |
| 1399 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 11 |  |  |  |  | FALSE |
| 1400 | inventory\_\_asset\_chain\_\_key\_value\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1401 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 11 |  |  |  |  | FALSE |
| 1402 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 11 |  |  |  |  | FALSE |
| 1403 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 11 |  |  |  |  | FALSE |
| 1404 | inventory\_\_asset\_chain\_\_edge\_postal\_code\_package\_ids | 11 |  |  |  |  | FALSE |
| 1405 | inventory\_\_site\_section\_chain\_\_geo\_dma\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1406 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1407 | inventory\_\_asset\_chain\_\_standard\_endpoint\_owner\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1408 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 11 |  |  |  |  | FALSE |
| 1409 | inventory\_\_site\_section\_chain\_\_content\_owner\_network\_id | 11 |  |  |  |  | FALSE |
| 1410 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1411 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 11 |  |  |  |  | FALSE |
| 1412 | inventory\_\_site\_section\_chain\_\_ip\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1413 | inventory\_\_asset\_chain\_\_outbound\_order\_type | 11 |  |  |  |  | FALSE |
| 1414 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 11 |  |  |  |  | FALSE |
| 1415 | inventory\_\_asset\_chain\_\_avails\_category\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1416 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 11 |  |  |  |  | FALSE |
| 1417 | inventory\_\_asset\_chain\_\_competition\_resellers | 11 |  |  |  |  | FALSE |
| 1418 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 11 |  |  |  |  | FALSE |
| 1419 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 11 |  |  |  |  | FALSE |
| 1420 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 11 |  |  |  |  | FALSE |
| 1421 | inventory\_\_site\_section\_chain\_\_geo\_city\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1422 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1423 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1424 | inventory\_\_site\_section\_chain\_\_non\_tracked\_audience\_item\_ids | 11 |  |  |  |  | FALSE |
| 1425 | inventory\_\_asset\_chain\_\_ssp\_clearing\_revenue | 11 |  |  |  |  | FALSE |
| 1426 | inventory\_\_asset\_chain\_\_selected\_yo\_inventory\_prioritization\_id | 11 |  |  |  |  | FALSE |
| 1427 | inventory\_\_asset\_chain\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1428 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 11 |  |  |  |  | FALSE |
| 1429 | inventory\_\_asset\_chain\_\_standard\_content\_territory\_visibility | 11 |  |  |  |  | FALSE |
| 1430 | inventory\_\_site\_section\_chain\_\_ip\_visibility | 11 |  |  |  |  | FALSE |
| 1431 | inventory\_\_asset\_chain\_\_rule\_type\_priority | 11 |  |  |  |  | FALSE |
| 1432 | inventory\_\_asset\_chain\_\_content\_rating\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1433 | inventory\_\_asset\_chain\_\_avails\_category\_\_market\_avails | 11 |  |  |  |  | FALSE |
| 1434 | inventory\_\_site\_section\_chain\_\_series\_id | 11 |  |  |  |  | FALSE |
| 1435 | inventory\_\_asset\_chain\_\_third\_party\_user\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1436 | inventory\_\_site\_section\_chain\_\_standard\_content\_series\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1437 | inventory\_\_site\_section\_chain\_\_ip\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1438 | inventory\_\_asset\_chain\_\_standard\_genre\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1439 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1440 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1441 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1442 | inventory\_\_site\_section\_chain\_\_portfolio\_ids | 11 |  |  |  |  | FALSE |
| 1443 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration | 11 |  |  |  |  | FALSE |
| 1444 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1445 | inventory\_\_site\_section\_chain\_\_standard\_content\_series\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1446 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1447 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name | 11 |  |  |  |  | FALSE |
| 1448 | inventory\_\_asset\_chain\_\_standard\_brand\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1449 | inventory\_\_asset\_chain\_\_geo\_city\_visibility | 11 |  |  |  |  | FALSE |
| 1450 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 11 |  |  |  |  | FALSE |
| 1451 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1452 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 11 |  |  |  |  | FALSE |
| 1453 | inventory\_\_asset\_chain\_\_ad\_filling\_status | 11 |  |  |  |  | FALSE |
| 1454 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_exchange\_order\_id | 11 |  |  |  |  | FALSE |
| 1455 | inventory\_\_asset\_chain\_\_ad\_priority\_bucket | 11 |  |  |  |  | FALSE |
| 1456 | inventory\_\_asset\_chain\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1457 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1458 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 11 |  |  |  |  | FALSE |
| 1459 | inventory\_\_site\_section\_chain\_\_internal\_deal\_ids | 11 |  |  |  |  | FALSE |
| 1460 | inventory\_\_site\_section\_chain\_\_competition\_resellers | 11 |  |  |  |  | FALSE |
| 1461 | inventory\_\_site\_section\_chain\_\_entity\_source | 11 |  |  |  |  | FALSE |
| 1462 | inventory\_\_asset\_chain\_\_series\_id | 11 |  |  |  |  | FALSE |
| 1463 | inventory\_\_asset\_chain\_\_matched\_key\_value\_ids | 11 |  |  |  |  | FALSE |
| 1464 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1465 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 11 |  |  |  |  | FALSE |
| 1466 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_down\_network\_id | 11 |  |  |  |  | FALSE |
| 1467 | inventory\_\_site\_section\_chain\_\_user\_agent\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1468 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_remaining\_avails | 11 |  |  |  |  | FALSE |
| 1469 | inventory\_\_asset\_chain\_\_visitor\_custom\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1470 | inventory\_\_asset\_chain\_\_distributor\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1471 | inventory\_\_asset\_chain\_\_inbound\_listing\_id | 11 |  |  |  |  | FALSE |
| 1472 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category | 11 |  |  |  |  | FALSE |
| 1473 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 11 |  |  |  |  | FALSE |
| 1474 | inventory\_\_site\_section\_chain\_\_standard\_content\_territory\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1475 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1476 | inventory\_\_site\_section\_chain\_\_content\_owner\_bidding\_original\_revenue | 11 |  |  |  |  | FALSE |
| 1477 | inventory\_\_site\_section\_chain\_\_standard\_channel\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1478 | inventory\_\_asset\_chain\_\_inbound\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1479 | inventory\_\_asset\_chain\_\_visitor\_custom\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1480 | inventory\_\_asset\_chain\_\_geo\_visibility | 11 |  |  |  |  | FALSE |
| 1481 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_owner\_visibility | 11 |  |  |  |  | FALSE |
| 1482 | inventory\_\_site\_section\_chain\_\_geo\_zip\_code\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1483 | inventory\_\_site\_section\_chain\_\_geo\_city\_visibility | 11 |  |  |  |  | FALSE |
| 1484 | inventory\_\_asset\_chain\_\_visible\_concrete\_event\_id | 11 |  |  |  |  | FALSE |
| 1485 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 11 |  |  |  |  | FALSE |
| 1486 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 11 |  |  |  |  | FALSE |
| 1487 | inventory\_\_asset\_chain\_\_user\_agent\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1488 | inventory\_\_site\_section\_chain\_\_content\_owner\_revenue | 11 |  |  |  |  | FALSE |
| 1489 | inventory\_\_asset\_chain\_\_third\_party\_user\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1490 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 11 |  |  |  |  | FALSE |
| 1491 | inventory\_\_site\_section\_chain\_\_geo\_state\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1492 | inventory\_\_asset\_chain\_\_content\_form\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1493 | inventory\_\_site\_section\_chain\_\_airing\_channel\_id | 11 |  |  |  |  | FALSE |
| 1494 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 11 |  |  |  |  | FALSE |
| 1495 | inventory\_\_asset\_chain\_\_listing\_id | 11 |  |  |  |  | FALSE |
| 1496 | inventory\_\_asset\_chain\_\_network\_is\_vod\_programmer | 11 |  |  |  |  | FALSE |
| 1497 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1498 | inventory\_\_asset\_chain\_\_upstream\_inbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1499 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails | 11 |  |  |  |  | FALSE |
| 1500 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1501 | inventory\_\_asset\_chain\_\_geo\_dma\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1502 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_ssp\_avails | 11 |  |  |  |  | FALSE |
| 1503 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | 11 |  |  |  |  | FALSE |
| 1504 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_total\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1505 | inventory\_\_asset\_chain\_\_avails\_category\_\_total\_avails | 11 |  |  |  |  | FALSE |
| 1506 | inventory\_\_asset\_chain\_\_geo\_zip\_code\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1507 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 11 |  |  |  |  | FALSE |
| 1508 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 11 |  |  |  |  | FALSE |
| 1509 | inventory\_\_asset\_chain\_\_geo\_zip\_code\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1510 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1511 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 11 |  |  |  |  | FALSE |
| 1512 | inventory\_\_site\_section\_chain\_\_network\_is\_vod\_programmer | 11 |  |  |  |  | FALSE |
| 1513 | inventory\_\_asset\_chain\_\_standard\_channel\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1514 | inventory\_\_asset\_chain\_\_network\_execution\_ctx\_flags | 11 |  |  |  |  | FALSE |
| 1515 | inventory\_\_site\_section\_chain\_\_user\_agent\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1516 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1517 | inventory\_\_asset\_chain\_\_user\_agent\_visibility | 11 |  |  |  |  | FALSE |
| 1518 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 11 |  |  |  |  | FALSE |
| 1519 | inventory\_\_site\_section\_chain\_\_content\_form\_visibility | 11 |  |  |  |  | FALSE |
| 1520 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 11 |  |  |  |  | FALSE |
| 1521 | inventory\_\_site\_section\_chain\_\_outbound\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1522 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1523 | inventory\_\_asset\_chain\_\_network\_is\_extra\_item\_owner | 11 |  |  |  |  | FALSE |
| 1524 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 11 |  |  |  |  | FALSE |
| 1525 | slot\_\_rules\_\_opp\_rule\_id | 11 |  |  |  |  | FALSE |
| 1526 | inventory\_\_asset\_chain\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | 11 |  |  |  |  | FALSE |
| 1527 | inventory\_\_site\_section\_chain\_\_network\_id | 11 |  |  |  |  | FALSE |
| 1528 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 11 |  |  |  |  | FALSE |
| 1529 | inventory\_\_asset\_chain\_\_content\_owner\_revenue | 11 |  |  |  |  | FALSE |
| 1530 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 11 |  |  |  |  | FALSE |
| 1531 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails | 11 |  |  |  |  | FALSE |
| 1532 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_sales\_channel | 11 |  |  |  |  | FALSE |
| 1533 | inventory\_\_asset\_chain\_\_ip\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1534 | inventory\_\_asset\_chain\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1535 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_distinct\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1536 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 11 |  |  |  |  | FALSE |
| 1537 | inventory\_\_asset\_chain\_\_device\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1538 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1539 | inventory\_\_site\_section\_chain\_\_user\_agent\_visibility | 11 |  |  |  |  | FALSE |
| 1540 | inventory\_\_asset\_chain\_\_inbound\_order\_auction\_type | 11 |  |  |  |  | FALSE |
| 1541 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1542 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 11 |  |  |  |  | FALSE |
| 1543 | inventory\_\_site\_section\_chain\_\_third\_party\_user\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1544 | inventory\_\_site\_section\_chain\_\_device\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1545 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 11 |  |  |  |  | FALSE |
| 1546 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails | 11 |  |  |  |  | FALSE |
| 1547 | inventory\_\_site\_section\_chain\_\_standard\_language\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1548 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 11 |  |  |  |  | FALSE |
| 1549 | inventory\_\_site\_section\_chain\_\_standard\_channel\_visibility | 11 |  |  |  |  | FALSE |
| 1550 | inventory\_\_site\_section\_chain\_\_geo\_dma\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1551 | inventory\_\_asset\_chain\_\_outbound\_rules | 11 |  |  |  |  | FALSE |
| 1552 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 11 |  |  |  |  | FALSE |
| 1553 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id | 11 |  |  |  |  | FALSE |
| 1554 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1555 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 11 |  |  |  |  | FALSE |
| 1556 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1557 | inventory\_\_asset\_chain\_\_buyer\_ids | 11 |  |  |  |  | FALSE |
| 1558 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 11 |  |  |  |  | FALSE |
| 1559 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked | 11 |  |  |  |  | FALSE |
| 1560 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_order\_id | 11 |  |  |  |  | FALSE |
| 1561 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1562 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 11 |  |  |  |  | FALSE |
| 1563 | inventory\_\_asset\_chain\_\_outbound\_rules\_\_rule\_id | 11 |  |  |  |  | FALSE |
| 1564 | inventory\_\_site\_section\_chain\_\_standard\_channel\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1565 | inventory\_\_asset\_chain\_\_avails\_category\_\_ssp\_avails | 11 |  |  |  |  | FALSE |
| 1566 | inventory\_\_site\_section\_chain\_\_site\_section\_group\_ids | 11 |  |  |  |  | FALSE |
| 1567 | inventory\_\_site\_section\_chain\_\_key\_value\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1568 | inventory\_\_asset\_chain\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1569 | inventory\_\_site\_section\_chain\_\_outbound\_rules\_\_total\_opp | 11 |  |  |  |  | FALSE |
| 1570 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1571 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1572 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 11 |  |  |  |  | FALSE |
| 1573 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1574 | inventory\_\_asset\_chain\_\_outbound\_rules\_\_total\_opp | 11 |  |  |  |  | FALSE |
| 1575 | inventory\_\_site\_section\_chain\_\_standard\_language\_visibility | 11 |  |  |  |  | FALSE |
| 1576 | inventory\_\_asset\_chain\_\_standard\_programmer\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1577 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 11 |  |  |  |  | FALSE |
| 1578 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_exchange\_order\_id | 11 |  |  |  |  | FALSE |
| 1579 | inventory\_\_site\_section\_chain\_\_matched\_yield\_optimization\_ids | 11 |  |  |  |  | FALSE |
| 1580 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1581 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails | 11 |  |  |  |  | FALSE |
| 1582 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_market\_avails | 11 |  |  |  |  | FALSE |
| 1583 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1584 | inventory\_\_asset\_chain\_\_standard\_programmer\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1585 | inventory\_\_site\_section\_chain\_\_marketplace\_audience\_extension\_deal\_ids | 11 |  |  |  |  | FALSE |
| 1586 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 11 |  |  |  |  | FALSE |
| 1587 | inventory\_\_asset\_chain\_\_supply\_source\_type | 11 |  |  |  |  | FALSE |
| 1588 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 11 |  |  |  |  | FALSE |
| 1589 | inventory\_\_site\_section\_chain\_\_global\_currency\_id | 11 |  |  |  |  | FALSE |
| 1590 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 11 |  |  |  |  | FALSE |
| 1591 | inventory\_\_asset\_chain\_\_avails\_category\_\_distinct\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1592 | inventory\_\_site\_section\_chain\_\_tracked\_audience\_item\_ids | 11 |  |  |  |  | FALSE |
| 1593 | inventory\_\_asset\_chain\_\_geo\_zip\_code\_visibility | 11 |  |  |  |  | FALSE |
| 1594 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 11 |  |  |  |  | FALSE |
| 1595 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 11 |  |  |  |  | FALSE |
| 1596 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders | 11 |  |  |  |  | FALSE |
| 1597 | inventory\_\_site\_section\_chain\_\_selected\_yo\_distribution\_id | 11 |  |  |  |  | FALSE |
| 1598 | inventory\_\_site\_section\_chain\_\_outbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1599 | inventory\_\_site\_section\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1600 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1601 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | 11 |  |  |  |  | FALSE |
| 1602 | inventory\_\_asset\_chain\_\_eligible\_carriage\_listing\_split\_unit\_ids | 11 |  |  |  |  | FALSE |
| 1603 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails | 11 |  |  |  |  | FALSE |
| 1604 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 11 |  |  |  |  | FALSE |
| 1605 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_unconstrained\_avails | 11 |  |  |  |  | FALSE |
| 1606 | inventory\_\_asset\_chain\_\_reseller\_network\_id | 11 |  |  |  |  | FALSE |
| 1607 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1608 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 11 |  |  |  |  | FALSE |
| 1609 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_bit\_flags | 11 |  |  |  |  | FALSE |
| 1610 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1611 | inventory\_\_asset\_chain\_\_selected\_yo\_inventory\_prioritization\_nip\_id | 11 |  |  |  |  | FALSE |
| 1612 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 11 |  |  |  |  | FALSE |
| 1613 | inventory\_\_asset\_chain\_\_standard\_genre\_visibility | 11 |  |  |  |  | FALSE |
| 1614 | inventory\_\_asset\_chain\_\_site\_group\_id | 11 |  |  |  |  | FALSE |
| 1615 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1616 | inventory\_\_asset\_chain\_\_standard\_content\_daypart\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1617 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 11 |  |  |  |  | FALSE |
| 1618 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 11 |  |  |  |  | FALSE |
| 1619 | inventory\_\_asset\_chain\_\_programmatic\_exchange\_rate\_to\_usd | 11 |  |  |  |  | FALSE |
| 1620 | inventory\_\_site\_section\_chain\_\_unified\_rule\_priority | 11 |  |  |  |  | FALSE |
| 1621 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | 11 |  |  |  |  | FALSE |
| 1622 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1623 | inventory\_\_site\_section\_chain\_\_supply\_acquisition\_cost | 11 |  |  |  |  | FALSE |
| 1624 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_initial\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1625 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 11 |  |  |  |  | FALSE |
| 1626 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1627 | inventory\_\_asset\_chain\_\_global\_currency\_id | 11 |  |  |  |  | FALSE |
| 1628 | inventory\_\_asset\_chain\_\_geo\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1629 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | 11 |  |  |  |  | FALSE |
| 1630 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_initial\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1631 | inventory\_\_site\_section\_chain\_\_geo\_city\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1632 | inventory\_\_asset\_chain\_\_postal\_code\_package\_id | 11 |  |  |  |  | FALSE |
| 1633 | inventory\_\_site\_section\_chain\_\_rule\_id | 11 |  |  |  |  | FALSE |
| 1634 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 11 |  |  |  |  | FALSE |
| 1635 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1636 | inventory\_\_asset\_chain\_\_rule\_flags | 11 |  |  |  |  | FALSE |
| 1637 | inventory\_\_asset\_chain\_\_avails\_category\_\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1638 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 11 |  |  |  |  | FALSE |
| 1639 | inventory\_\_site\_section\_chain\_\_content\_form\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1640 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 11 |  |  |  |  | FALSE |
| 1641 | inventory\_\_asset\_chain\_\_key\_value\_visibility | 11 |  |  |  |  | FALSE |
| 1642 | inventory\_\_asset\_chain\_\_content\_rating\_visibility | 11 |  |  |  |  | FALSE |
| 1643 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_available\_duration | 11 |  |  |  |  | FALSE |
| 1644 | inventory\_\_asset\_chain\_\_avails\_category\_\_remaining\_avails | 11 |  |  |  |  | FALSE |
| 1645 | inventory\_\_asset\_chain\_\_matched\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1646 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 11 |  |  |  |  | FALSE |
| 1647 | inventory\_\_asset\_chain\_\_network\_execution\_ctx\_index | 11 |  |  |  |  | FALSE |
| 1648 | inventory\_\_asset\_chain\_\_outbound\_rules\_\_win\_opp | 11 |  |  |  |  | FALSE |
| 1649 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1650 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category | 11 |  |  |  |  | FALSE |
| 1651 | inventory\_\_asset\_chain\_\_unified\_rule\_priority\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1652 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1653 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1654 | inventory\_\_asset\_chain\_\_standard\_channel\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1655 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1656 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1657 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | 11 |  |  |  |  | FALSE |
| 1658 | inventory\_\_site\_section\_chain\_\_asset\_group\_id | 11 |  |  |  |  | FALSE |
| 1659 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1660 | inventory\_\_asset\_chain\_\_ip\_visibility | 11 |  |  |  |  | FALSE |
| 1661 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 11 |  |  |  |  | FALSE |
| 1662 | inventory\_\_site\_section\_chain\_\_unified\_rule\_priority\_\_sub\_priority\_value | 11 |  |  |  |  | FALSE |
| 1663 | inventory\_\_asset\_chain\_\_standard\_content\_series\_visibility | 11 |  |  |  |  | FALSE |
| 1664 | inventory\_\_site\_section\_chain\_\_listing\_id | 11 |  |  |  |  | FALSE |
| 1665 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1666 | inventory\_\_asset\_chain\_\_content\_rating\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1667 | inventory\_\_asset\_chain\_\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1668 | inventory\_\_site\_section\_chain\_\_inbound\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1669 | inventory\_\_site\_section\_chain\_\_programmatic\_exchange\_rate\_to\_eur | 11 |  |  |  |  | FALSE |
| 1670 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | 11 |  |  |  |  | FALSE |
| 1671 | inventory\_\_asset\_chain\_\_airing\_id | 11 |  |  |  |  | FALSE |
| 1672 | inventory\_\_site\_section\_chain\_\_bit\_flags | 11 |  |  |  |  | FALSE |
| 1673 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics | 11 |  |  |  |  | FALSE |
| 1674 | inventory\_\_asset\_chain\_\_supply\_acquisition\_cost | 11 |  |  |  |  | FALSE |
| 1675 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1676 | inventory\_\_asset\_chain\_\_floor\_price | 11 |  |  |  |  | FALSE |
| 1677 | inventory\_\_asset\_chain\_\_standard\_content\_daypart\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1678 | inventory\_\_site\_section\_chain\_\_rule\_ext\_id | 11 |  |  |  |  | FALSE |
| 1679 | inventory\_\_asset\_chain\_\_portfolio\_ids | 11 |  |  |  |  | FALSE |
| 1680 | inventory\_\_asset\_chain\_\_standard\_brand\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1681 | inventory\_\_asset\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1682 | inventory\_\_asset\_chain\_\_geo\_country\_visibility | 11 |  |  |  |  | FALSE |
| 1683 | inventory\_\_site\_section\_chain\_\_third\_party\_user\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1684 | inventory\_\_site\_section\_chain\_\_key\_value\_visibility | 11 |  |  |  |  | FALSE |
| 1685 | request\_\_external\_candidate\_ad\_\_dsp\_id | 11 |  |  |  |  | FALSE |
| 1686 | inventory\_\_asset\_chain\_\_standard\_endpoint\_owner\_visibility | 11 |  |  |  |  | FALSE |
| 1687 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name | 11 |  |  |  |  | FALSE |
| 1688 | inventory\_\_asset\_chain\_\_unified\_outbound\_order\_priority\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1689 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 11 |  |  |  |  | FALSE |
| 1690 | inventory\_\_site\_section\_chain\_\_supply\_source\_type | 11 |  |  |  |  | FALSE |
| 1691 | inventory\_\_site\_section\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1692 | request\_\_slots\_\_max\_ad\_duration | 11 |  |  |  |  | FALSE |
| 1693 | inventory\_\_asset\_chain\_\_content\_owner\_bidding\_modified\_revenue | 11 |  |  |  |  | FALSE |
| 1694 | inventory\_\_site\_section\_chain\_\_region\_ids | 11 |  |  |  |  | FALSE |
| 1695 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | 11 |  |  |  |  | FALSE |
| 1696 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1697 | inventory\_\_site\_section\_chain\_\_standard\_content\_daypart\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1698 | inventory\_\_site\_section\_chain\_\_standard\_programmer\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1699 | inventory\_\_site\_section\_chain\_\_priority\_type | 11 |  |  |  |  | FALSE |
| 1700 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1701 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 11 |  |  |  |  | FALSE |
| 1702 | inventory\_\_site\_section\_chain\_\_standard\_content\_series\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1703 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1704 | inventory\_\_site\_section\_chain\_\_inbound\_order\_ids | 11 |  |  |  |  | FALSE |
| 1705 | inventory\_\_asset\_chain\_\_standard\_channel\_visibility | 11 |  |  |  |  | FALSE |
| 1706 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1707 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 11 |  |  |  |  | FALSE |
| 1708 | inventory\_\_asset\_chain\_\_programmatic\_exchange\_rate\_to\_eur | 11 |  |  |  |  | FALSE |
| 1709 | inventory\_\_asset\_chain\_\_selected\_yo\_volume\_cap\_ids | 11 |  |  |  |  | FALSE |
| 1710 | inventory\_\_asset\_chain\_\_content\_rating\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1711 | inventory\_\_asset\_chain\_\_priority\_value | 11 |  |  |  |  | FALSE |
| 1712 | inventory\_\_asset\_chain\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 11 |  |  |  |  | FALSE |
| 1713 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 11 |  |  |  |  | FALSE |
| 1714 | inventory\_\_asset\_chain\_\_entity\_source | 11 |  |  |  |  | FALSE |
| 1715 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1716 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_sales\_channel | 11 |  |  |  |  | FALSE |
| 1717 | inventory\_\_site\_section\_chain\_\_reseller\_network\_id | 11 |  |  |  |  | FALSE |
| 1718 | inventory\_\_site\_section\_chain\_\_standard\_language\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1719 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num | 11 |  |  |  |  | FALSE |
| 1720 | inventory\_\_asset\_chain\_\_standard\_endpoint\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1721 | inventory\_\_asset\_chain\_\_region\_ids | 11 |  |  |  |  | FALSE |
| 1722 | inventory\_\_asset\_chain\_\_deal\_awareability | 11 |  |  |  |  | FALSE |
| 1723 | inventory\_\_asset\_chain\_\_outbound\_exchange\_order\_ids | 11 |  |  |  |  | FALSE |
| 1724 | inventory\_\_site\_section\_chain\_\_content\_owner\_bidding\_modified\_revenue | 11 |  |  |  |  | FALSE |
| 1725 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_vod\_programmer\_total\_avails | 11 |  |  |  |  | FALSE |
| 1726 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 11 |  |  |  |  | FALSE |
| 1727 | inventory\_\_asset\_chain\_\_third\_party\_user\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1728 | inventory\_\_asset\_chain\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1729 | inventory\_\_asset\_chain\_\_geo\_zip\_code\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1730 | inventory\_\_asset\_chain\_\_device\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1731 | inventory\_\_site\_section\_chain\_\_standard\_genre\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1732 | inventory\_\_site\_section\_chain\_\_geo\_country\_visibility | 11 |  |  |  |  | FALSE |
| 1733 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1734 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 11 |  |  |  |  | FALSE |
| 1735 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_total\_avails | 11 |  |  |  |  | FALSE |
| 1736 | inventory\_\_site\_section\_chain\_\_geo\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1737 | inventory\_\_site\_section\_chain\_\_matched\_key\_value\_ids | 11 |  |  |  |  | FALSE |
| 1738 | inventory\_\_asset\_chain\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1739 | inventory\_\_site\_section\_chain\_\_content\_rating\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1740 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails | 11 |  |  |  |  | FALSE |
| 1741 | inventory\_\_site\_section\_chain\_\_geo\_dma\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1742 | inventory\_\_asset\_chain\_\_outbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1743 | inventory\_\_site\_section\_chain\_\_standard\_brand\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1744 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1745 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings | 11 |  |  |  |  | FALSE |
| 1746 | inventory\_\_site\_section\_chain\_\_inbound\_listing\_id | 11 |  |  |  |  | FALSE |
| 1747 | inventory\_\_site\_section\_chain\_\_ssp\_clearing\_revenue | 11 |  |  |  |  | FALSE |
| 1748 | inventory\_\_site\_section\_chain\_\_revenue | 11 |  |  |  |  | FALSE |
| 1749 | inventory\_\_site\_section\_chain\_\_inventory\_package\_ids | 11 |  |  |  |  | FALSE |
| 1750 | inventory\_\_asset\_chain\_\_key\_value\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1751 | inventory\_\_asset\_chain\_\_outbound\_listing\_id | 11 |  |  |  |  | FALSE |
| 1752 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1753 | inventory\_\_asset\_chain\_\_upstream\_global\_currency\_id | 11 |  |  |  |  | FALSE |
| 1754 | inventory\_\_site\_section\_chain\_\_standard\_content\_series\_visibility | 11 |  |  |  |  | FALSE |
| 1755 | inventory\_\_site\_section\_chain\_\_carriage\_inventory\_owner\_id | 11 |  |  |  |  | FALSE |
| 1756 | inventory\_\_site\_section\_chain\_\_visitor\_custom\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1757 | inventory\_\_asset\_chain\_\_inventory\_distribution\_contexts | 11 |  |  |  |  | FALSE |
| 1758 | inventory\_\_site\_section\_chain\_\_content\_rating\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1759 | inventory\_\_site\_section\_chain\_\_avails\_category | 11 |  |  |  |  | FALSE |
| 1760 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 11 |  |  |  |  | FALSE |
| 1761 | inventory\_\_asset\_chain\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1762 | inventory\_\_asset\_chain\_\_avails\_category\_\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1763 | inventory\_\_asset\_chain\_\_geo\_country\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1764 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 11 |  |  |  |  | FALSE |
| 1765 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1766 | inventory\_\_asset\_chain\_\_supply\_distribution\_cost | 11 |  |  |  |  | FALSE |
| 1767 | inventory\_\_site\_section\_chain\_\_geo\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1768 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1769 | inventory\_\_site\_section\_chain\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1770 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1771 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders | 11 |  |  |  |  | FALSE |
| 1772 | inventory\_\_asset\_chain\_\_device\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1773 | inventory\_\_asset\_chain\_\_inbound\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1774 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 11 |  |  |  |  | FALSE |
| 1775 | inventory\_\_asset\_chain\_\_selected\_yield\_optimization\_info\_ids | 11 |  |  |  |  | FALSE |
| 1776 | inventory\_\_site\_section\_chain\_\_ad\_priority\_bucket | 11 |  |  |  |  | FALSE |
| 1777 | inventory\_\_site\_section\_chain\_\_margin | 11 |  |  |  |  | FALSE |
| 1778 | inventory\_\_site\_section\_chain\_\_distributor\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1779 | inventory\_\_site\_section\_chain\_\_network\_execution\_ctx\_flags | 11 |  |  |  |  | FALSE |
| 1780 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | 11 |  |  |  |  | FALSE |
| 1781 | inventory\_\_asset\_chain\_\_standard\_brand\_visibility | 11 |  |  |  |  | FALSE |
| 1782 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_order\_type | 11 |  |  |  |  | FALSE |
| 1783 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 11 |  |  |  |  | FALSE |
| 1784 | inventory\_\_site\_section\_chain\_\_geo\_zip\_code\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1785 | inventory\_\_site\_section\_chain\_\_demand\_dim\_awareability | 11 |  |  |  |  | FALSE |
| 1786 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1787 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_listing\_id | 11 |  |  |  |  | FALSE |
| 1788 | inventory\_\_asset\_chain\_\_key\_value\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1789 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 11 |  |  |  |  | FALSE |
| 1790 | inventory\_\_asset\_chain\_\_network\_is\_ad\_owner | 11 |  |  |  |  | FALSE |
| 1791 | inventory\_\_site\_section\_chain\_\_geo\_state\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1792 | inventory\_\_site\_section\_chain\_\_outbound\_listing\_id | 11 |  |  |  |  | FALSE |
| 1793 | inventory\_\_site\_section\_chain\_\_standard\_channel\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1794 | inventory\_\_site\_section\_chain\_\_custom\_platform\_ids | 11 |  |  |  |  | FALSE |
| 1795 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics | 11 |  |  |  |  | FALSE |
| 1796 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1797 | inventory\_\_site\_section\_chain\_\_distributor\_revenue | 11 |  |  |  |  | FALSE |
| 1798 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails | 11 |  |  |  |  | FALSE |
| 1799 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_avails | 11 |  |  |  |  | FALSE |
| 1800 | inventory\_\_site\_section\_chain\_\_edge\_postal\_code\_package\_ids | 11 |  |  |  |  | FALSE |
| 1801 | inventory\_\_asset\_chain\_\_reseller\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1802 | inventory\_\_site\_section\_chain\_\_sales\_channel | 11 |  |  |  |  | FALSE |
| 1803 | inventory\_\_site\_section\_chain\_\_break\_id | 11 |  |  |  |  | FALSE |
| 1804 | inventory\_\_site\_section\_chain\_\_outbound\_order\_priority\_type | 11 |  |  |  |  | FALSE |
| 1805 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings | 11 |  |  |  |  | FALSE |
| 1806 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1807 | inventory\_\_asset\_chain\_\_content\_owner\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1808 | inventory\_\_asset\_chain\_\_upstream\_content\_owner\_revenue\_in\_up\_currency | 11 |  |  |  |  | FALSE |
| 1809 | inventory\_\_asset\_chain\_\_distributor\_revenue | 11 |  |  |  |  | FALSE |
| 1810 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1811 | inventory\_\_site\_section\_chain\_\_network\_selection\_info | 11 |  |  |  |  | FALSE |
| 1812 | inventory\_\_asset\_chain\_\_avails\_category | 11 |  |  |  |  | FALSE |
| 1813 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 11 |  |  |  |  | FALSE |
| 1814 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 11 |  |  |  |  | FALSE |
| 1815 | inventory\_\_asset\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1816 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1817 | inventory\_\_site\_section\_chain\_\_visitor\_custom\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1818 | inventory\_\_site\_section\_chain\_\_selected\_yield\_optimization\_ids | 11 |  |  |  |  | FALSE |
| 1819 | inventory\_\_asset\_chain\_\_user\_agent\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1820 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 11 |  |  |  |  | FALSE |
| 1821 | inventory\_\_asset\_chain\_\_geo\_state\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1822 | inventory\_\_site\_section\_chain\_\_visible\_concrete\_event\_id | 11 |  |  |  |  | FALSE |
| 1823 | inventory\_\_site\_section\_chain\_\_key\_value\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1824 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 11 |  |  |  |  | FALSE |
| 1825 | inventory\_\_site\_section\_chain\_\_content\_form\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1826 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 11 |  |  |  |  | FALSE |
| 1827 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | 11 |  |  |  |  | FALSE |
| 1828 | inventory\_\_site\_section\_chain\_\_selected\_yo\_distribution\_nip\_id | 11 |  |  |  |  | FALSE |
| 1829 | inventory\_\_site\_section\_chain\_\_geo\_dma\_visibility | 11 |  |  |  |  | FALSE |
| 1830 | inventory\_\_site\_section\_chain\_\_user\_agent\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1831 | inventory\_\_site\_section\_chain\_\_geo\_state\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1832 | inventory\_\_asset\_chain\_\_visitor\_custom\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1833 | inventory\_\_site\_section\_chain\_\_deal\_awareability | 11 |  |  |  |  | FALSE |
| 1834 | inventory\_\_site\_section\_chain\_\_buyer\_ids | 11 |  |  |  |  | FALSE |
| 1835 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1836 | inventory\_\_asset\_chain\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1837 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_order\_transaction\_type | 11 |  |  |  |  | FALSE |
| 1838 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1839 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_order\_priority | 11 |  |  |  |  | FALSE |
| 1840 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_owner\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1841 | inventory\_\_asset\_chain\_\_standard\_endpoint\_owner\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1842 | inventory\_\_asset\_chain\_\_standard\_content\_series\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1843 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 11 |  |  |  |  | FALSE |
| 1844 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1845 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked | 11 |  |  |  |  | FALSE |
| 1846 | inventory\_\_asset\_chain\_\_geo\_dma\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1847 | inventory\_\_site\_section\_chain\_\_visitor\_custom\_id\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1848 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1849 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1850 | inventory\_\_asset\_chain\_\_geo\_city\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1851 | inventory\_\_asset\_chain\_\_ip\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1852 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1853 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_order\_id | 11 |  |  |  |  | FALSE |
| 1854 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1855 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type | 11 |  |  |  |  | FALSE |
| 1856 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1857 | inventory\_\_asset\_chain\_\_standard\_content\_territory\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1858 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 11 |  |  |  |  | FALSE |
| 1859 | inventory\_\_asset\_chain\_\_avails\_category\_\_unconstrained\_avails | 11 |  |  |  |  | FALSE |
| 1860 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 11 |  |  |  |  | FALSE |
| 1861 | inventory\_\_asset\_chain\_\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1862 | inventory\_\_site\_section\_chain\_\_supply\_distribution\_cost | 11 |  |  |  |  | FALSE |
| 1863 | inventory\_\_asset\_chain\_\_rule\_ext\_id | 11 |  |  |  |  | FALSE |
| 1864 | inventory\_\_site\_section\_chain\_\_network\_execution\_ctx\_index | 11 |  |  |  |  | FALSE |
| 1865 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | 11 |  |  |  |  | FALSE |
| 1866 | inventory\_\_asset\_chain\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1867 | inventory\_\_site\_section\_chain\_\_unified\_rule\_priority\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1868 | inventory\_\_asset\_chain\_\_airing\_channel\_id | 11 |  |  |  |  | FALSE |
| 1869 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 11 |  |  |  |  | FALSE |
| 1870 | inventory\_\_asset\_chain\_\_custom\_platform\_ids | 11 |  |  |  |  | FALSE |
| 1871 | inventory\_\_site\_section\_chain\_\_matched\_daypart | 11 |  |  |  |  | FALSE |
| 1872 | inventory\_\_site\_section\_chain\_\_geo\_city\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1873 | inventory\_\_site\_section\_chain\_\_selected\_yo\_inventory\_prioritization\_id | 11 |  |  |  |  | FALSE |
| 1874 | inventory\_\_site\_section\_chain\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1875 | inventory\_\_site\_section\_chain\_\_programmatic\_exchange\_rate\_to\_usd | 11 |  |  |  |  | FALSE |
| 1876 | inventory\_\_site\_section\_chain\_\_flags | 11 |  |  |  |  | FALSE |
| 1877 | inventory\_\_site\_section\_chain\_\_avails\_category\_\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1878 | inventory\_\_asset\_chain\_\_standard\_language\_visibility | 11 |  |  |  |  | FALSE |
| 1879 | inventory\_\_asset\_chain\_\_avails\_category\_\_total\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1880 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 11 |  |  |  |  | FALSE |
| 1881 | inventory\_\_site\_section\_chain\_\_floor\_price | 11 |  |  |  |  | FALSE |
| 1882 | inventory\_\_asset\_chain\_\_inbound\_order\_ids | 11 |  |  |  |  | FALSE |
| 1883 | inventory\_\_site\_section\_chain\_\_inbound\_order\_type | 11 |  |  |  |  | FALSE |
| 1884 | inventory\_\_site\_section\_chain\_\_opportunity\_id | 11 |  |  |  |  | FALSE |
| 1885 | inventory\_\_asset\_chain\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1886 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration | 11 |  |  |  |  | FALSE |
| 1887 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id | 11 |  |  |  |  | FALSE |
| 1888 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 11 |  |  |  |  | FALSE |
| 1889 | inventory\_\_asset\_chain\_\_outbound\_order\_ids | 11 |  |  |  |  | FALSE |
| 1890 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1891 | inventory\_\_site\_section\_chain\_\_standard\_brand\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1892 | inventory\_\_asset\_chain\_\_content\_form\_visibility | 11 |  |  |  |  | FALSE |
| 1893 | inventory\_\_asset\_chain\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 11 |  |  |  |  | FALSE |
| 1894 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1895 | inventory\_\_site\_section\_chain\_\_selected\_yo\_volume\_cap\_ids | 11 |  |  |  |  | FALSE |
| 1896 | inventory\_\_asset\_chain\_\_standard\_programmer\_visibility | 11 |  |  |  |  | FALSE |
| 1897 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 11 |  |  |  |  | FALSE |
| 1898 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1899 | inventory\_\_asset\_chain\_\_standard\_endpoint\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1900 | inventory\_\_site\_section\_chain\_\_ad\_unit\_default\_duration | 11 |  |  |  |  | FALSE |
| 1901 | inventory\_\_site\_section\_chain\_\_rule\_flags | 11 |  |  |  |  | FALSE |
| 1902 | inventory\_\_site\_section\_chain\_\_inbound\_order\_auction\_type | 11 |  |  |  |  | FALSE |
| 1903 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 11 |  |  |  |  | FALSE |
| 1904 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 11 |  |  |  |  | FALSE |
| 1905 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1906 | inventory\_\_asset\_chain\_\_selected\_yield\_optimization\_ids | 11 |  |  |  |  | FALSE |
| 1907 | inventory\_\_site\_section\_chain\_\_third\_party\_user\_id\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1908 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails | 11 |  |  |  |  | FALSE |
| 1909 | inventory\_\_site\_section\_chain\_\_device\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1910 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | 11 |  |  |  |  | FALSE |
| 1911 | inventory\_\_site\_section\_chain\_\_content\_rating\_visibility | 11 |  |  |  |  | FALSE |
| 1912 | inventory\_\_asset\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1913 | inventory\_\_asset\_chain\_\_scenario\_id | 11 |  |  |  |  | FALSE |
| 1914 | inventory\_\_site\_section\_chain\_\_airing\_id | 11 |  |  |  |  | FALSE |
| 1915 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 11 |  |  |  |  | FALSE |
| 1916 | inventory\_\_asset\_chain\_\_count\_imp\_as\_booked | 11 |  |  |  |  | FALSE |
| 1917 | inventory\_\_asset\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 1918 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails | 11 |  |  |  |  | FALSE |
| 1919 | inventory\_\_asset\_chain\_\_mapped\_site\_section\_ids | 11 |  |  |  |  | FALSE |
| 1920 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 11 |  |  |  |  | FALSE |
| 1921 | inventory\_\_asset\_chain\_\_opportunity\_id | 11 |  |  |  |  | FALSE |
| 1922 | inventory\_\_asset\_chain\_\_standard\_content\_subscription\_model\_visibility | 11 |  |  |  |  | FALSE |
| 1923 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1924 | inventory\_\_site\_section\_chain\_\_inbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1925 | inventory\_\_site\_section\_chain\_\_inventory\_distribution\_contexts | 11 |  |  |  |  | FALSE |
| 1926 | inventory\_\_site\_section\_chain\_\_outbound\_rules | 11 |  |  |  |  | FALSE |
| 1927 | inventory\_\_asset\_chain\_\_reseller\_revenue | 11 |  |  |  |  | FALSE |
| 1928 | inventory\_\_site\_section\_chain\_\_network\_is\_ad\_unit\_owner | 11 |  |  |  |  | FALSE |
| 1929 | inventory\_\_site\_section\_chain\_\_inbound\_rule\_id | 11 |  |  |  |  | FALSE |
| 1930 | inventory\_\_site\_section\_chain\_\_standard\_content\_territory\_visibility | 11 |  |  |  |  | FALSE |
| 1931 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 11 |  |  |  |  | FALSE |
| 1932 | inventory\_\_asset\_chain\_\_outbound\_exchange\_listings\_\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1933 | inventory\_\_site\_section\_chain\_\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 1934 | inventory\_\_asset\_chain\_\_standard\_genre\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1935 | inventory\_\_site\_section\_chain\_\_geo\_state\_visibility | 11 |  |  |  |  | FALSE |
| 1936 | inventory\_\_site\_section\_chain\_\_bidder\_seat\_id | 11 |  |  |  |  | FALSE |
| 1937 | inventory\_\_site\_section\_chain\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1938 | inventory\_\_site\_section\_chain\_\_ip\_visibility\_\_report\_event | 11 |  |  |  |  | FALSE |
| 1939 | inventory\_\_asset\_chain\_\_geo\_state\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1940 | inventory\_\_asset\_chain\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1941 | inventory\_\_site\_section\_chain\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 11 |  |  |  |  | FALSE |
| 1942 | inventory\_\_asset\_chain\_\_geo\_country\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1943 | inventory\_\_site\_section\_chain\_\_unified\_outbound\_order\_priority\_\_priority\_tier | 11 |  |  |  |  | FALSE |
| 1944 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 11 |  |  |  |  | FALSE |
| 1945 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 11 |  |  |  |  | FALSE |
| 1946 | inventory\_\_asset\_chain\_\_selected\_yo\_margin\_id | 11 |  |  |  |  | FALSE |
| 1947 | inventory\_\_asset\_chain\_\_margin | 11 |  |  |  |  | FALSE |
| 1948 | inventory\_\_site\_section\_chain\_\_eligible\_carriage\_listing\_split\_unit\_ids | 11 |  |  |  |  | FALSE |
| 1949 | inventory\_\_site\_section\_chain\_\_geo\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1950 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 11 |  |  |  |  | FALSE |
| 1951 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_order\_priority | 11 |  |  |  |  | FALSE |
| 1952 | inventory\_\_site\_section\_chain\_\_mapped\_site\_section\_ids | 11 |  |  |  |  | FALSE |
| 1953 | inventory\_\_asset\_chain\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 11 |  |  |  |  | FALSE |
| 1954 | inventory\_\_asset\_chain\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1955 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 11 |  |  |  |  | FALSE |
| 1956 | inventory\_\_site\_section\_chain\_\_standard\_programmer\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1957 | inventory\_\_asset\_chain\_\_content\_owner\_bidding\_original\_revenue | 11 |  |  |  |  | FALSE |
| 1958 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 11 |  |  |  |  | FALSE |
| 1959 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase | 11 |  |  |  |  | FALSE |
| 1960 | inventory\_\_site\_section\_chain\_\_outbound\_order\_ids | 11 |  |  |  |  | FALSE |
| 1961 | inventory\_\_site\_section\_chain\_\_standard\_language\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1962 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | 11 |  |  |  |  | FALSE |
| 1963 | inventory\_\_asset\_chain\_\_flags | 11 |  |  |  |  | FALSE |
| 1964 | inventory\_\_site\_section\_chain\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails | 11 |  |  |  |  | FALSE |
| 1965 | inventory\_\_site\_section\_chain\_\_standard\_endpoint\_visibility | 11 |  |  |  |  | FALSE |
| 1966 | inventory\_\_asset\_chain\_\_matched\_yield\_optimization\_ids | 11 |  |  |  |  | FALSE |
| 1967 | inventory\_\_asset\_chain\_\_mapped\_asset\_ids | 11 |  |  |  |  | FALSE |
| 1968 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 11 |  |  |  |  | FALSE |
| 1969 | inventory\_\_site\_section\_chain\_\_site\_id | 11 |  |  |  |  | FALSE |
| 1970 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | 11 |  |  |  |  | FALSE |
| 1971 | inventory\_\_asset\_chain\_\_matched\_daypart | 11 |  |  |  |  | FALSE |
| 1972 | inventory\_\_asset\_chain\_\_device\_id\_visibility | 11 |  |  |  |  | FALSE |
| 1973 | inventory\_\_site\_section\_chain\_\_mapped\_asset\_ids | 11 |  |  |  |  | FALSE |
| 1974 | inventory\_\_site\_section\_chain\_\_upstream\_global\_currency\_id | 11 |  |  |  |  | FALSE |
| 1975 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails | 11 |  |  |  |  | FALSE |
| 1976 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 11 |  |  |  |  | FALSE |
| 1977 | inventory\_\_asset\_chain\_\_inbound\_order\_id | 11 |  |  |  |  | FALSE |
| 1978 | inventory\_\_site\_section\_chain\_\_standard\_genre\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1979 | inventory\_\_asset\_chain\_\_selected\_yo\_distribution\_nip\_id | 11 |  |  |  |  | FALSE |
| 1980 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 1981 | inventory\_\_asset\_chain\_\_priority\_type | 11 |  |  |  |  | FALSE |
| 1982 | inventory\_\_asset\_chain\_\_sales\_channel | 11 |  |  |  |  | FALSE |
| 1983 | inventory\_\_site\_section\_chain\_\_geo\_country\_visibility\_\_report\_aggregate | 11 |  |  |  |  | FALSE |
| 1984 | inventory\_\_asset\_chain\_\_network\_is\_ad\_unit\_owner | 11 |  |  |  |  | FALSE |
| 1985 | inventory\_\_site\_section\_chain\_\_network\_is\_ad\_owner | 11 |  |  |  |  | FALSE |
| 1986 | inventory\_\_site\_section\_chain\_\_standard\_content\_subscription\_model\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1987 | inventory\_\_asset\_chain\_\_standard\_genre\_visibility\_\_targetable | 11 |  |  |  |  | FALSE |
| 1988 | inventory\_\_site\_section\_chain\_\_supply\_source | 11 |  |  |  |  | FALSE |
| 1989 | inventory\_\_asset\_chain\_\_internal\_deal\_ids | 11 |  |  |  |  | FALSE |
| 1990 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids | 11 |  |  |  |  | FALSE |
| 1991 | inventory\_\_asset\_chain\_\_standard\_content\_daypart\_visibility | 11 |  |  |  |  | FALSE |
| 1992 | inventory\_\_asset\_chain\_\_ad\_unit\_default\_duration | 11 |  |  |  |  | FALSE |
| 1993 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 11 |  |  |  |  | FALSE |
| 1994 | inventory\_\_site\_section\_chain\_\_ad\_filling\_status\_\_available\_duration | 11 |  |  |  |  | FALSE |
| 1995 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_down\_network\_id | 11 |  |  |  |  | FALSE |
| 1996 | inventory\_\_site\_section\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 11 |  |  |  |  | FALSE |
| 1997 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 11 |  |  |  |  | FALSE |
| 1998 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 11 |  |  |  |  | FALSE |
| 1999 | inventory\_\_site\_section\_chain\_\_selected\_yield\_optimization\_info\_ids | 11 |  |  |  |  | FALSE |
| 2000 | inventory\_\_site\_section\_chain\_\_content\_owner\_bidding\_revenue | 11 |  |  |  |  | FALSE |
| 2001 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 11 |  |  |  |  | FALSE |
| 2002 | inventory\_\_site\_section\_chain\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | 11 |  |  |  |  | FALSE |
| 2003 | inventory\_\_asset\_chain\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 11 |  |  |  |  | FALSE |
| 2004 | execution\_networks\_\_standard\_content\_series\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2005 | execution\_networks\_\_device\_id\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2006 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 10 |  |  |  |  | FALSE |
| 2007 | execution\_networks\_\_standard\_channel\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2008 | execution\_networks\_\_eligible\_outbound\_orders\_\_exchange\_order\_id | 10 |  |  |  |  | FALSE |
| 2009 | execution\_networks\_\_standard\_language\_visibility | 10 |  |  |  |  | FALSE |
| 2010 | audiences\_\_network\_id | 10 |  |  |  |  | FALSE |
| 2011 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails | 10 |  |  |  |  | FALSE |
| 2012 | execution\_networks\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2013 | execution\_networks\_\_ip\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2014 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 10 |  |  |  |  | FALSE |
| 2015 | execution\_networks\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2016 | execution\_networks\_\_standard\_content\_territory\_visibility | 10 |  |  |  |  | FALSE |
| 2017 | execution\_networks\_\_avails\_category\_\_opportunity\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2018 | execution\_networks\_\_airing\_channel\_id | 10 |  |  |  |  | FALSE |
| 2019 | execution\_networks\_\_outbound\_exchange\_order\_ids | 10 |  |  |  |  | FALSE |
| 2020 | execution\_networks\_\_region\_ids | 10 |  |  |  |  | FALSE |
| 2021 | execution\_networks\_\_geo\_dma\_visibility | 10 |  |  |  |  | FALSE |
| 2022 | execution\_networks\_\_priority\_type | 10 |  |  |  |  | FALSE |
| 2023 | execution\_networks\_\_selected\_yo\_distribution\_id | 10 |  |  |  |  | FALSE |
| 2024 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 10 |  |  |  |  | FALSE |
| 2025 | execution\_networks\_\_count\_imp\_as\_booked | 10 |  |  |  |  | FALSE |
| 2026 | execution\_networks\_\_avails\_category\_\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2027 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name | 10 |  |  |  |  | FALSE |
| 2028 | execution\_networks\_\_rule\_flags | 10 |  |  |  |  | FALSE |
| 2029 | execution\_networks\_\_avails\_category\_\_distinct\_inventory\_avails | 10 |  |  |  |  | FALSE |
| 2030 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | 10 |  |  |  |  | FALSE |
| 2031 | execution\_networks\_\_outbound\_listing\_id | 10 |  |  |  |  | FALSE |
| 2032 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration | 10 |  |  |  |  | FALSE |
| 2033 | execution\_networks\_\_standard\_content\_daypart\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2034 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | 10 |  |  |  |  | FALSE |
| 2035 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2036 | execution\_networks\_\_unified\_outbound\_order\_priority | 10 |  |  |  |  | FALSE |
| 2037 | execution\_networks\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 10 |  |  |  |  | FALSE |
| 2038 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2039 | execution\_networks\_\_unified\_rule\_priority\_\_priority\_tier | 10 |  |  |  |  | FALSE |
| 2040 | execution\_networks\_\_standard\_content\_subscription\_model\_visibility | 10 |  |  |  |  | FALSE |
| 2041 | execution\_networks\_\_avails\_category\_\_opportunity | 10 |  |  |  |  | FALSE |
| 2042 | execution\_networks\_\_content\_rating\_visibility | 10 |  |  |  |  | FALSE |
| 2043 | execution\_networks\_\_key\_value\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2044 | execution\_networks\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2045 | execution\_networks\_\_outbound\_exchange\_listings\_\_listing\_ids | 10 |  |  |  |  | FALSE |
| 2046 | execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity | 10 |  |  |  |  | FALSE |
| 2047 | execution\_networks\_\_device\_id\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2048 | execution\_networks\_\_internal\_deal\_ids | 10 |  |  |  |  | FALSE |
| 2049 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2050 | execution\_networks\_\_standard\_endpoint\_owner\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2051 | execution\_networks\_\_content\_owner\_bidding\_modified\_revenue | 10 |  |  |  |  | FALSE |
| 2052 | execution\_networks\_\_supply\_acquisition\_cost | 10 |  |  |  |  | FALSE |
| 2053 | execution\_networks\_\_bidding\_revenue | 10 |  |  |  |  | FALSE |
| 2054 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 10 |  |  |  |  | FALSE |
| 2055 | execution\_networks\_\_standard\_brand\_visibility | 10 |  |  |  |  | FALSE |
| 2056 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | 10 |  |  |  |  | FALSE |
| 2057 | execution\_networks\_\_demand\_dim\_awareability | 10 |  |  |  |  | FALSE |
| 2058 | execution\_networks\_\_avails\_category\_\_unconstrained\_avails | 10 |  |  |  |  | FALSE |
| 2059 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 10 |  |  |  |  | FALSE |
| 2060 | execution\_networks\_\_unified\_rule\_priority | 10 |  |  |  |  | FALSE |
| 2061 | execution\_networks\_\_unified\_rule\_priority\_\_sub\_priority\_value | 10 |  |  |  |  | FALSE |
| 2062 | execution\_networks\_\_upstream\_content\_owner\_revenue\_in\_up\_currency | 10 |  |  |  |  | FALSE |
| 2063 | execution\_networks\_\_outbound\_order\_priority\_type | 10 |  |  |  |  | FALSE |
| 2064 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2065 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 10 |  |  |  |  | FALSE |
| 2066 | execution\_networks\_\_outbound\_order\_id | 10 |  |  |  |  | FALSE |
| 2067 | execution\_networks\_\_content\_owner\_revenue | 10 |  |  |  |  | FALSE |
| 2068 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_ids | 10 |  |  |  |  | FALSE |
| 2069 | execution\_networks\_\_eligible\_outbound\_orders | 10 |  |  |  |  | FALSE |
| 2070 | execution\_networks\_\_geo\_zip\_code\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2071 | execution\_networks\_\_geo\_zip\_code\_visibility | 10 |  |  |  |  | FALSE |
| 2072 | execution\_networks\_\_content\_form\_visibility | 10 |  |  |  |  | FALSE |
| 2073 | execution\_networks\_\_ad\_priority\_bucket | 10 |  |  |  |  | FALSE |
| 2074 | execution\_networks\_\_standard\_genre\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2075 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | 10 |  |  |  |  | FALSE |
| 2076 | execution\_networks\_\_asset\_id | 10 |  |  |  |  | FALSE |
| 2077 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | 10 |  |  |  |  | FALSE |
| 2078 | execution\_networks\_\_selected\_yo\_inventory\_prioritization\_id | 10 |  |  |  |  | FALSE |
| 2079 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 10 |  |  |  |  | FALSE |
| 2080 | execution\_networks\_\_avails\_category\_\_avails | 10 |  |  |  |  | FALSE |
| 2081 | slot\_\_raw\_max\_ads | 10 |  |  |  |  | FALSE |
| 2082 | execution\_networks\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2083 | execution\_networks\_\_revenue | 10 |  |  |  |  | FALSE |
| 2084 | execution\_networks\_\_edge\_postal\_code\_package\_ids | 10 |  |  |  |  | FALSE |
| 2085 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num | 10 |  |  |  |  | FALSE |
| 2086 | execution\_networks\_\_standard\_content\_territory\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2087 | execution\_networks\_\_sales\_channel | 10 |  |  |  |  | FALSE |
| 2088 | execution\_networks\_\_distributor\_revenue | 10 |  |  |  |  | FALSE |
| 2089 | execution\_networks\_\_standard\_content\_territory\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2090 | execution\_networks\_\_standard\_language\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2091 | execution\_networks\_\_geo\_state\_visibility | 10 |  |  |  |  | FALSE |
| 2092 | execution\_networks\_\_buyer\_ids | 10 |  |  |  |  | FALSE |
| 2093 | execution\_networks\_\_key\_value\_visibility | 10 |  |  |  |  | FALSE |
| 2094 | execution\_networks\_\_user\_agent\_visibility | 10 |  |  |  |  | FALSE |
| 2095 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | 10 |  |  |  |  | FALSE |
| 2096 | execution\_networks\_\_content\_rating\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2097 | execution\_networks\_\_outbound\_order\_type | 10 |  |  |  |  | FALSE |
| 2098 | execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails | 10 |  |  |  |  | FALSE |
| 2099 | execution\_networks\_\_standard\_content\_credential\_status\_visibility | 10 |  |  |  |  | FALSE |
| 2100 | audiences\_\_kv\_term\_ids | 10 |  |  |  |  | FALSE |
| 2101 | slot\_\_max\_bitrate | 10 |  |  |  |  | FALSE |
| 2102 | execution\_networks\_\_reseller\_network\_id | 10 |  |  |  |  | FALSE |
| 2103 | execution\_networks\_\_ad\_filling\_status\_\_initial\_filled\_duration | 10 |  |  |  |  | FALSE |
| 2104 | execution\_networks\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 10 |  |  |  |  | FALSE |
| 2105 | execution\_networks\_\_user\_agent\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2106 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category | 10 |  |  |  |  | FALSE |
| 2107 | execution\_networks\_\_key\_value\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2108 | execution\_networks\_\_unified\_outbound\_order\_priority\_\_sub\_priority\_value | 10 |  |  |  |  | FALSE |
| 2109 | execution\_networks\_\_eligible\_outbound\_orders\_\_order\_priority | 10 |  |  |  |  | FALSE |
| 2110 | execution\_networks\_\_ad\_filling\_status\_\_filled\_ad\_num | 10 |  |  |  |  | FALSE |
| 2111 | execution\_networks\_\_standard\_content\_subscription\_model\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2112 | execution\_networks\_\_avails\_category\_\_remaining\_avails | 10 |  |  |  |  | FALSE |
| 2113 | execution\_networks\_\_standard\_programmer\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2114 | execution\_networks\_\_key\_value\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2115 | execution\_networks\_\_competition\_resellers | 10 |  |  |  |  | FALSE |
| 2116 | execution\_networks\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 10 |  |  |  |  | FALSE |
| 2117 | execution\_networks\_\_geo\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2118 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 10 |  |  |  |  | FALSE |
| 2119 | execution\_networks\_\_standard\_content\_series\_visibility | 10 |  |  |  |  | FALSE |
| 2120 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | 10 |  |  |  |  | FALSE |
| 2121 | execution\_networks\_\_ad\_filling\_status | 10 |  |  |  |  | FALSE |
| 2122 | execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics | 10 |  |  |  |  | FALSE |
| 2123 | execution\_networks\_\_geo\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2124 | execution\_networks\_\_standard\_endpoint\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2125 | execution\_networks\_\_ssp\_clearing\_revenue | 10 |  |  |  |  | FALSE |
| 2126 | execution\_networks\_\_postal\_code\_package\_id | 10 |  |  |  |  | FALSE |
| 2127 | execution\_networks\_\_avails\_category\_\_vod\_programmer\_total\_avails | 10 |  |  |  |  | FALSE |
| 2128 | execution\_networks\_\_standard\_programmer\_visibility | 10 |  |  |  |  | FALSE |
| 2129 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2130 | execution\_networks | 10 |  |  |  |  | FALSE |
| 2131 | request\_\_slots\_\_resellers\_\_inbound\_order\_id | 10 |  |  |  |  | FALSE |
| 2132 | execution\_networks\_\_inbound\_order\_ids | 10 |  |  |  |  | FALSE |
| 2133 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2134 | request\_info\_\_raw\_brands | 10 |  |  |  |  | FALSE |
| 2135 | execution\_networks\_\_matched\_yield\_optimization\_ids | 10 |  |  |  |  | FALSE |
| 2136 | execution\_networks\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2137 | execution\_networks\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2138 | execution\_networks\_\_margin | 10 |  |  |  |  | FALSE |
| 2139 | execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration | 10 |  |  |  |  | FALSE |
| 2140 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 10 |  |  |  |  | FALSE |
| 2141 | execution\_networks\_\_geo\_country\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2142 | slot\_\_profile\_id | 10 |  |  |  |  | FALSE |
| 2143 | execution\_networks\_\_eligible\_outbound\_orders\_\_down\_network\_id | 10 |  |  |  |  | FALSE |
| 2144 | execution\_networks\_\_standard\_content\_credential\_status\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2145 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | 10 |  |  |  |  | FALSE |
| 2146 | execution\_networks\_\_entity\_source | 10 |  |  |  |  | FALSE |
| 2147 | execution\_networks\_\_network\_selection\_info | 10 |  |  |  |  | FALSE |
| 2148 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 10 |  |  |  |  | FALSE |
| 2149 | execution\_networks\_\_visitor\_custom\_id\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2150 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 10 |  |  |  |  | FALSE |
| 2151 | execution\_networks\_\_selected\_yield\_optimization\_info\_ids | 10 |  |  |  |  | FALSE |
| 2152 | execution\_networks\_\_standard\_language\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2153 | execution\_networks\_\_series\_id | 10 |  |  |  |  | FALSE |
| 2154 | execution\_networks\_\_avails\_category\_\_market\_avails | 10 |  |  |  |  | FALSE |
| 2155 | execution\_networks\_\_carriage\_inventory\_owner\_id | 10 |  |  |  |  | FALSE |
| 2156 | execution\_networks\_\_ip\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2157 | execution\_networks\_\_geo\_visibility | 10 |  |  |  |  | FALSE |
| 2158 | slot\_\_original\_max\_ads | 10 |  |  |  |  | FALSE |
| 2159 | execution\_networks\_\_standard\_content\_daypart\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2160 | execution\_networks\_\_outbound\_rules\_\_rule\_id | 10 |  |  |  |  | FALSE |
| 2161 | execution\_networks\_\_standard\_channel\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2162 | execution\_networks\_\_geo\_city\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2163 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 10 |  |  |  |  | FALSE |
| 2164 | execution\_networks\_\_standard\_language\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2165 | execution\_networks\_\_priority\_value | 10 |  |  |  |  | FALSE |
| 2166 | execution\_networks\_\_standard\_genre\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2167 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2168 | execution\_networks\_\_geo\_country\_visibility | 10 |  |  |  |  | FALSE |
| 2169 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2170 | execution\_networks\_\_rule\_type\_priority | 10 |  |  |  |  | FALSE |
| 2171 | execution\_networks\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2172 | execution\_networks\_\_standard\_content\_daypart\_visibility | 10 |  |  |  |  | FALSE |
| 2173 | execution\_networks\_\_selected\_yo\_volume\_cap\_ids | 10 |  |  |  |  | FALSE |
| 2174 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 10 |  |  |  |  | FALSE |
| 2175 | execution\_networks\_\_third\_party\_user\_id\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2176 | execution\_networks\_\_inventory\_distribution\_contexts | 10 |  |  |  |  | FALSE |
| 2177 | execution\_networks\_\_visible\_concrete\_event\_id | 10 |  |  |  |  | FALSE |
| 2178 | execution\_networks\_\_ad\_unit\_default\_duration | 10 |  |  |  |  | FALSE |
| 2179 | execution\_networks\_\_geo\_country\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2180 | execution\_networks\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2181 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails | 10 |  |  |  |  | FALSE |
| 2182 | execution\_networks\_\_third\_party\_user\_id\_visibility | 10 |  |  |  |  | FALSE |
| 2183 | execution\_networks\_\_avails\_category | 10 |  |  |  |  | FALSE |
| 2184 | execution\_networks\_\_standard\_content\_credential\_status\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2185 | execution\_networks\_\_geo\_dma\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2186 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails | 10 |  |  |  |  | FALSE |
| 2187 | execution\_networks\_\_unified\_outbound\_order\_priority\_\_priority\_tier | 10 |  |  |  |  | FALSE |
| 2188 | execution\_networks\_\_distributor\_bidding\_revenue | 10 |  |  |  |  | FALSE |
| 2189 | execution\_networks\_\_visitor\_custom\_id\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2190 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails | 10 |  |  |  |  | FALSE |
| 2191 | execution\_networks\_\_standard\_channel\_visibility | 10 |  |  |  |  | FALSE |
| 2192 | execution\_networks\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails | 10 |  |  |  |  | FALSE |
| 2193 | execution\_networks\_\_bidder\_seat\_id | 10 |  |  |  |  | FALSE |
| 2194 | execution\_networks\_\_standard\_content\_series\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2195 | execution\_networks\_\_avails\_category\_\_unfilled\_avails | 10 |  |  |  |  | FALSE |
| 2196 | execution\_networks\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2197 | execution\_networks\_\_network\_execution\_ctx\_index | 10 |  |  |  |  | FALSE |
| 2198 | execution\_networks\_\_site\_section\_group\_ids | 10 |  |  |  |  | FALSE |
| 2199 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined | 10 |  |  |  |  | FALSE |
| 2200 | execution\_networks\_\_standard\_endpoint\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2201 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails | 10 |  |  |  |  | FALSE |
| 2202 | execution\_networks\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2203 | execution\_networks\_\_flags | 10 |  |  |  |  | FALSE |
| 2204 | execution\_networks\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2205 | execution\_networks\_\_standard\_brand\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2206 | execution\_networks\_\_avails\_category\_\_total\_unfilled\_avails | 10 |  |  |  |  | FALSE |
| 2207 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids | 10 |  |  |  |  | FALSE |
| 2208 | execution\_networks\_\_eligible\_outbound\_orders\_\_listing\_id | 10 |  |  |  |  | FALSE |
| 2209 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2210 | execution\_networks\_\_outbound\_exchange\_listings | 10 |  |  |  |  | FALSE |
| 2211 | execution\_networks\_\_eligible\_outbound\_orders\_\_order\_type | 10 |  |  |  |  | FALSE |
| 2212 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 10 |  |  |  |  | FALSE |
| 2213 | execution\_networks\_\_supply\_distribution\_cost | 10 |  |  |  |  | FALSE |
| 2214 | execution\_networks\_\_standard\_programmer\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2215 | execution\_networks\_\_supply\_source\_type | 10 |  |  |  |  | FALSE |
| 2216 | execution\_networks\_\_eligible\_carriage\_listing\_split\_unit\_ids | 10 |  |  |  |  | FALSE |
| 2217 | execution\_networks\_\_geo\_dma\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2218 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration | 10 |  |  |  |  | FALSE |
| 2219 | execution\_networks\_\_eligible\_outbound\_orders\_\_order\_transaction\_type | 10 |  |  |  |  | FALSE |
| 2220 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain | 10 |  |  |  |  | FALSE |
| 2221 | execution\_networks\_\_deal\_awareability | 10 |  |  |  |  | FALSE |
| 2222 | execution\_networks\_\_scenario\_id | 10 |  |  |  |  | FALSE |
| 2223 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 10 |  |  |  |  | FALSE |
| 2224 | execution\_networks\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2225 | execution\_networks\_\_ip\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2226 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | 10 |  |  |  |  | FALSE |
| 2227 | execution\_networks\_\_selected\_yo\_margin\_id | 10 |  |  |  |  | FALSE |
| 2228 | execution\_networks\_\_eligible\_outbound\_orders\_\_order\_id | 10 |  |  |  |  | FALSE |
| 2229 | execution\_networks\_\_rule\_id | 10 |  |  |  |  | FALSE |
| 2230 | execution\_networks\_\_geo\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2231 | execution\_networks\_\_standard\_channel\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2232 | execution\_networks\_\_priority\_tier | 10 |  |  |  |  | FALSE |
| 2233 | auction\_\_bid\_throttling\_status | 10 |  |  |  |  | FALSE |
| 2234 | execution\_networks\_\_internal\_seat\_ids | 10 |  |  |  |  | FALSE |
| 2235 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2236 | execution\_networks\_\_ip\_visibility | 10 |  |  |  |  | FALSE |
| 2237 | execution\_networks\_\_third\_party\_user\_id\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2238 | execution\_networks\_\_geo\_state\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2239 | execution\_networks\_\_matched\_inventory\_package\_ids | 10 |  |  |  |  | FALSE |
| 2240 | execution\_networks\_\_avails\_category\_\_ssp\_avails | 10 |  |  |  |  | FALSE |
| 2241 | execution\_networks\_\_selected\_yo\_inventory\_prioritization\_nip\_id | 10 |  |  |  |  | FALSE |
| 2242 | execution\_networks\_\_listing\_id | 10 |  |  |  |  | FALSE |
| 2243 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 10 |  |  |  |  | FALSE |
| 2244 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_ids | 10 |  |  |  |  | FALSE |
| 2245 | execution\_networks\_\_outbound\_order\_ids | 10 |  |  |  |  | FALSE |
| 2246 | execution\_networks\_\_ad\_filling\_status\_\_filled\_duration | 10 |  |  |  |  | FALSE |
| 2247 | execution\_networks\_\_programmatic\_exchange\_rate\_to\_eur | 10 |  |  |  |  | FALSE |
| 2248 | execution\_networks\_\_inbound\_rule\_id | 10 |  |  |  |  | FALSE |
| 2249 | execution\_networks\_\_site\_group\_id | 10 |  |  |  |  | FALSE |
| 2250 | execution\_networks\_\_standard\_brand\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2251 | request\_info\_\_raw\_channels | 10 |  |  |  |  | FALSE |
| 2252 | execution\_networks\_\_asset\_group\_ids | 10 |  |  |  |  | FALSE |
| 2253 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 10 |  |  |  |  | FALSE |
| 2254 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_ids | 10 |  |  |  |  | FALSE |
| 2255 | execution\_networks\_\_geo\_city\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2256 | execution\_networks\_\_eligible\_outbound\_orders\_\_bit\_flags | 10 |  |  |  |  | FALSE |
| 2257 | execution\_networks\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2258 | execution\_networks\_\_outbound\_exchange\_order\_id | 10 |  |  |  |  | FALSE |
| 2259 | execution\_networks\_\_matched\_key\_value\_ids | 10 |  |  |  |  | FALSE |
| 2260 | execution\_networks\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2261 | execution\_networks\_\_portfolio\_ids | 10 |  |  |  |  | FALSE |
| 2262 | execution\_networks\_\_standard\_endpoint\_owner\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2263 | execution\_networks\_\_standard\_content\_series\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2264 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | 10 |  |  |  |  | FALSE |
| 2265 | execution\_networks\_\_upstream\_global\_currency\_id | 10 |  |  |  |  | FALSE |
| 2266 | execution\_networks\_\_opportunity\_id | 10 |  |  |  |  | FALSE |
| 2267 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 10 |  |  |  |  | FALSE |
| 2268 | execution\_networks\_\_network\_is\_ad\_unit\_owner | 10 |  |  |  |  | FALSE |
| 2269 | execution\_networks\_\_reseller\_bidding\_revenue | 10 |  |  |  |  | FALSE |
| 2270 | execution\_networks\_\_programmatic\_exchange\_rate\_to\_usd | 10 |  |  |  |  | FALSE |
| 2271 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails | 10 |  |  |  |  | FALSE |
| 2272 | execution\_networks\_\_marketplace\_audience\_extension\_deal\_ids | 10 |  |  |  |  | FALSE |
| 2273 | execution\_networks\_\_content\_owner\_bidding\_original\_revenue | 10 |  |  |  |  | FALSE |
| 2274 | execution\_networks\_\_asset\_group\_id | 10 |  |  |  |  | FALSE |
| 2275 | execution\_networks\_\_outbound\_order\_transaction\_type | 10 |  |  |  |  | FALSE |
| 2276 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase | 10 |  |  |  |  | FALSE |
| 2277 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails | 10 |  |  |  |  | FALSE |
| 2278 | execution\_networks\_\_break\_id | 10 |  |  |  |  | FALSE |
| 2279 | execution\_networks\_\_airing\_channel\_group\_id | 10 |  |  |  |  | FALSE |
| 2280 | execution\_networks\_\_ad\_filling\_status\_\_available\_duration | 10 |  |  |  |  | FALSE |
| 2281 | execution\_networks\_\_floor\_price | 10 |  |  |  |  | FALSE |
| 2282 | execution\_networks\_\_device\_id\_visibility | 10 |  |  |  |  | FALSE |
| 2283 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 10 |  |  |  |  | FALSE |
| 2284 | execution\_networks\_\_selected\_yo\_distribution\_nip\_id | 10 |  |  |  |  | FALSE |
| 2285 | execution\_networks\_\_global\_currency\_id | 10 |  |  |  |  | FALSE |
| 2286 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | 10 |  |  |  |  | FALSE |
| 2287 | partners\_\_bidding\_revenue | 10 |  |  |  |  | FALSE |
| 2288 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2289 | execution\_networks\_\_geo\_city\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2290 | execution\_networks\_\_custom\_platform\_ids | 10 |  |  |  |  | FALSE |
| 2291 | execution\_networks\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 10 |  |  |  |  | FALSE |
| 2292 | execution\_networks\_\_standard\_genre\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2293 | execution\_networks\_\_content\_rating\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2294 | execution\_networks\_\_geo\_zip\_code\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2295 | execution\_networks\_\_visitor\_custom\_id\_visibility | 10 |  |  |  |  | FALSE |
| 2296 | execution\_networks\_\_content\_form\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2297 | execution\_networks\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked | 10 |  |  |  |  | FALSE |
| 2298 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 10 |  |  |  |  | FALSE |
| 2299 | execution\_networks\_\_avails\_category\_\_total\_avails | 10 |  |  |  |  | FALSE |
| 2300 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 10 |  |  |  |  | FALSE |
| 2301 | execution\_networks\_\_standard\_content\_territory\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2302 | execution\_networks\_\_geo\_city\_visibility | 10 |  |  |  |  | FALSE |
| 2303 | execution\_networks\_\_network\_is\_vod\_programmer | 10 |  |  |  |  | FALSE |
| 2304 | execution\_networks\_\_selected\_yield\_optimization\_ids | 10 |  |  |  |  | FALSE |
| 2305 | execution\_networks\_\_standard\_genre\_visibility | 10 |  |  |  |  | FALSE |
| 2306 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 10 |  |  |  |  | FALSE |
| 2307 | execution\_networks\_\_carriage\_listing\_split\_unit\_id | 10 |  |  |  |  | FALSE |
| 2308 | execution\_networks\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 10 |  |  |  |  | FALSE |
| 2309 | execution\_networks\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2310 | execution\_networks\_\_network\_is\_extra\_item\_owner | 10 |  |  |  |  | FALSE |
| 2311 | execution\_networks\_\_geo\_zip\_code\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2312 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 10 |  |  |  |  | FALSE |
| 2313 | execution\_networks\_\_matched\_audience\_item\_ids | 10 |  |  |  |  | FALSE |
| 2314 | execution\_networks\_\_upstream\_inbound\_order\_id | 10 |  |  |  |  | FALSE |
| 2315 | execution\_networks\_\_geo\_state\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2316 | execution\_networks\_\_geo\_state\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2317 | execution\_networks\_\_reseller\_revenue | 10 |  |  |  |  | FALSE |
| 2318 | execution\_networks\_\_geo\_dma\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2319 | execution\_networks\_\_standard\_endpoint\_visibility | 10 |  |  |  |  | FALSE |
| 2320 | execution\_networks\_\_inventory\_package\_ids | 10 |  |  |  |  | FALSE |
| 2321 | execution\_networks\_\_airing\_id | 10 |  |  |  |  | FALSE |
| 2322 | execution\_networks\_\_avails\_category\_\_inventory\_avails | 10 |  |  |  |  | FALSE |
| 2323 | execution\_networks\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 10 |  |  |  |  | FALSE |
| 2324 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails | 10 |  |  |  |  | FALSE |
| 2325 | execution\_networks\_\_inbound\_order\_auction\_type | 10 |  |  |  |  | FALSE |
| 2326 | execution\_networks\_\_rule\_ext\_id | 10 |  |  |  |  | FALSE |
| 2327 | execution\_networks\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2328 | execution\_networks\_\_inbound\_listing\_ids | 10 |  |  |  |  | FALSE |
| 2329 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_hp | 10 |  |  |  |  | FALSE |
| 2330 | execution\_networks\_\_outbound\_rules\_\_win\_opp | 10 |  |  |  |  | FALSE |
| 2331 | execution\_networks\_\_user\_agent\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2332 | execution\_networks\_\_standard\_endpoint\_owner\_visibility | 10 |  |  |  |  | FALSE |
| 2333 | request\_info | 10 |  |  |  |  | FALSE |
| 2334 | execution\_networks\_\_outbound\_rules\_\_total\_opp | 10 |  |  |  |  | FALSE |
| 2335 | execution\_networks\_\_device\_id\_visibility\_\_targetable | 10 |  |  |  |  | FALSE |
| 2336 | execution\_networks\_\_content\_rating\_visibility\_\_report\_aggregate | 10 |  |  |  |  | FALSE |
| 2337 | execution\_networks\_\_content\_form\_visibility\_\_report\_event | 10 |  |  |  |  | FALSE |
| 2338 | execution\_networks\_\_outbound\_rules | 10 |  |  |  |  | FALSE |
| 2339 | execution\_networks\_\_matched\_daypart | 10 |  |  |  |  | FALSE |
| 2340 | execution\_networks\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails | 10 |  |  |  |  | FALSE |
| 2341 | execution\_networks\_\_eligible\_outbound\_orders\_\_sales\_channel | 10 |  |  |  |  | FALSE |
| 2342 | execution\_networks\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 10 |  |  |  |  | FALSE |
| 2343 | execution\_networks\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids | 10 |  |  |  |  | FALSE |
| 2344 | execution\_networks\_\_distributor\_network\_id | 10 |  |  |  |  | FALSE |
| 2345 | partners\_\_ip\_visibility | 9 |  |  |  |  | FALSE |
| 2346 | partners\_\_inventory\_package\_ids | 9 |  |  |  |  | FALSE |
| 2347 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 9 |  |  |  |  | FALSE |
| 2348 | advertisement\_\_is\_replacement | 9 |  |  |  |  | FALSE |
| 2349 | advertisement\_\_global\_brand\_id | 9 |  |  |  |  | FALSE |
| 2350 | partners\_\_geo\_visibility\_\_report\_event | 9 |  |  |  |  | FALSE |
| 2351 | aim\_info\_\_aim\_audience\_info\_\_segments\_\_id | 9 |  |  |  |  | FALSE |
| 2352 | request\_\_advertisements\_\_content\_owner\_\_down\_revenue | 9 |  |  |  |  | FALSE |
| 2353 | slot | 9 |  |  |  |  | FALSE |
| 2354 | acks\_\_multiplier | 9 |  |  |  |  | FALSE |
| 2355 | auction\_\_asset\_id | 9 |  |  |  |  | FALSE |
| 2356 | advertisement\_\_vast\_creative\_id | 9 |  |  |  |  | FALSE |
| 2357 | partners\_\_geo\_visibility\_\_targetable | 9 |  |  |  |  | FALSE |
| 2358 | partners\_\_geo\_visibility\_\_report\_aggregate | 9 |  |  |  |  | FALSE |
| 2359 | auction\_\_impression\_\_slot\_index | 9 |  |  |  |  | FALSE |
| 2360 | request\_\_external\_candidate\_ad\_\_filter\_reason\_\_error | 9 |  |  |  |  | FALSE |
| 2361 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 9 |  |  |  |  | FALSE |
| 2362 | partners\_\_ad\_unit\_default\_duration | 9 |  |  |  |  | FALSE |
| 2363 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_down\_revenue | 9 |  |  |  |  | FALSE |
| 2364 | partners\_\_visible\_concrete\_event\_id | 9 |  |  |  |  | FALSE |
| 2365 | request\_\_advertisements\_\_creative\_id | 9 |  |  |  |  | FALSE |
| 2366 | partners\_\_geo\_visibility | 9 |  |  |  |  | FALSE |
| 2367 | request\_\_external\_candidate\_ad\_\_filter\_reason\_\_error\_category | 8 |  |  |  |  | FALSE |
| 2368 | slot\_\_time\_position | 8 |  |  |  |  | FALSE |
| 2369 | advertisement\_\_insertion\_order\_id | 8 |  |  |  |  | FALSE |
| 2370 | request\_\_advertisements\_\_measurable\_concrete\_event\_id\_raw | 8 |  |  |  |  | FALSE |
| 2371 | forecast\_\_meta\_\_ip\_address | 8 |  |  |  |  | FALSE |
| 2372 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_rid | 8 |  |  |  |  | FALSE |
| 2373 | request\_\_context\_\_time\_span | 8 |  |  |  |  | FALSE |
| 2374 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 8 |  |  |  |  | FALSE |
| 2375 | request\_\_network\_attribute\_\_visible\_concrete\_event\_id\_raw | 8 |  |  |  |  | FALSE |
| 2376 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 8 |  |  |  |  | FALSE |
| 2377 | request\_\_external\_candidate\_ad\_\_error | 8 |  |  |  |  | FALSE |
| 2378 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_name | 8 |  |  |  |  | FALSE |
| 2379 | request\_\_advertisements\_\_measurable\_concrete\_event\_id | 8 |  |  |  |  | FALSE |
| 2380 | auction | 8 |  |  |  |  | FALSE |
| 2381 | request\_\_external\_candidate\_ad\_\_dsp\_clearing\_price | 8 |  |  |  |  | FALSE |
| 2382 | request\_\_external\_candidate\_ad\_\_filter\_reason | 8 |  |  |  |  | FALSE |
| 2383 | request\_\_external\_candidate\_ad\_\_sfx\_dsp\_id | 8 |  |  |  |  | FALSE |
| 2384 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_domain | 8 |  |  |  |  | FALSE |
| 2385 | request\_\_model\_framework\_\_network\_model\_contexts | 8 |  |  |  |  | FALSE |
| 2386 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_sid | 8 |  |  |  |  | FALSE |
| 2387 | partners\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 8 |  |  |  |  | FALSE |
| 2388 | partners\_\_bidding\_up\_revenue | 8 |  |  |  |  | FALSE |
| 2389 | request\_\_external\_candidate\_ad\_\_clearing\_price | 8 |  |  |  |  | FALSE |
| 2390 | request\_\_network\_attribute\_\_visible\_concrete\_event\_id | 8 |  |  |  |  | FALSE |
| 2391 | request\_\_external\_candidate\_ad\_\_dsp\_clearing\_price\_discounted | 8 |  |  |  |  | FALSE |
| 2392 | candidate | 8 |  |  |  |  | FALSE |
| 2393 | request\_\_external\_candidate\_ad\_\_original\_price | 8 |  |  |  |  | FALSE |
| 2394 | request\_\_advertisements | 7 |  |  |  |  | FALSE |
| 2395 | candidate\_\_content\_type | 7 |  |  |  |  | FALSE |
| 2396 | request\_\_rtb\_auction\_\_asset\_id | 7 |  |  |  |  | FALSE |
| 2397 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos | 7 |  |  |  |  | FALSE |
| 2398 | advertisement\_\_abstract\_event\_id | 7 |  |  |  |  | FALSE |
| 2399 | request\_\_errors | 7 |  |  |  |  | FALSE |
| 2400 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 7 |  |  |  |  | FALSE |
| 2401 | advertisement\_\_original\_bidding\_price | 7 |  |  |  |  | FALSE |
| 2402 | request\_\_rtb\_auction | 7 |  |  |  |  | FALSE |
| 2403 | candidate\_\_filter\_reason | 7 |  |  |  |  | FALSE |
| 2404 | aim\_info\_\_aim\_audience\_info\_\_segments | 7 |  |  |  |  | FALSE |
| 2405 | request\_\_visitor\_\_postal\_code\_package\_\_postal\_code\_package\_id | 7 |  |  |  |  | FALSE |
| 2406 | slot\_\_original\_ad\_unit | 7 |  |  |  |  | FALSE |
| 2407 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos | 7 |  |  |  |  | FALSE |
| 2408 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 7 |  |  |  |  | FALSE |
| 2409 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos | 7 |  |  |  |  | FALSE |
| 2410 | request\_\_network\_execution\_ctx\_\_inventory\_package\_ids | 7 |  |  |  |  | FALSE |
| 2411 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos | 7 |  |  |  |  | FALSE |
| 2412 | request\_\_model\_framework | 7 |  |  |  |  | FALSE |
| 2413 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos | 7 |  |  |  |  | FALSE |
| 2414 | request\_\_external\_candidate\_ad | 7 |  |  |  |  | FALSE |
| 2415 | advertisement\_\_net\_price | 7 |  |  |  |  | FALSE |
| 2416 | aim\_info\_\_aim\_audience\_info | 7 |  |  |  |  | FALSE |
| 2417 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_complete | 7 |  |  |  |  | FALSE |
| 2418 | request\_\_visitor\_\_user\_agent\_device\_id | 7 |  |  |  |  | FALSE |
| 2419 | acks\_\_process\_timestamp | 6 |  |  |  |  | FALSE |
| 2420 | request\_\_auction\_network\_contexts\_\_auction\_network\_to\_eur\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 2421 | request\_\_auction\_network\_contexts\_\_publisher\_id | 6 |  |  |  |  | FALSE |
| 2422 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2423 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 2424 | request\_\_external\_candidate\_ad\_\_dsp\_currency\_id | 6 |  |  |  |  | FALSE |
| 2425 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_segments | 6 |  |  |  |  | FALSE |
| 2426 | request\_\_advertisements\_\_content\_right\_owner\_\_bidding\_revenue | 6 |  |  |  |  | FALSE |
| 2427 | request\_\_advertisements\_\_content\_owner\_\_bidding\_up\_modified\_revenue | 6 |  |  |  |  | FALSE |
| 2428 | request\_\_advertisements\_\_distributor | 6 |  |  |  |  | FALSE |
| 2429 | request\_\_advertisements\_\_replaced\_placement\_id | 6 |  |  |  |  | FALSE |
| 2430 | request\_\_advertisements\_\_reseller\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 2431 | acks\_\_event\_value | 6 |  |  |  |  | FALSE |
| 2432 | request\_\_advertisements\_\_fallback\_ad\_uniq\_id | 6 |  |  |  |  | FALSE |
| 2433 | acks\_\_metrics\_\_measurable\_ad\_rewind\_impression | 6 |  |  |  |  | FALSE |
| 2434 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2435 | request\_\_advertisements\_\_content\_owner\_\_unified\_rule\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 2436 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 2437 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 2438 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 6 |  |  |  |  | FALSE |
| 2439 | acks\_\_metrics\_\_complete\_quartile | 6 |  |  |  |  | FALSE |
| 2440 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_pretty\_id | 6 |  |  |  |  | FALSE |
| 2441 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 2442 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 2443 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 2444 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 6 |  |  |  |  | FALSE |
| 2445 | acks\_\_yield\_optimization\_ids\_\_demand\_id | 6 |  |  |  |  | FALSE |
| 2446 | request\_\_context\_\_asset\_chain\_\_distributor\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 2447 | request\_\_slots\_\_resellers\_\_avails\_metrics | 6 |  |  |  |  | FALSE |
| 2448 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2449 | request\_\_advertisements\_\_cch\_rendition\_id | 6 |  |  |  |  | FALSE |
| 2450 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2451 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2452 | request\_\_external\_candidate\_ad\_\_domain | 6 |  |  |  |  | FALSE |
| 2453 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records | 6 |  |  |  |  | FALSE |
| 2454 | request\_\_advertisements\_\_content\_right\_owner\_\_site\_id | 6 |  |  |  |  | FALSE |
| 2455 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 2456 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 2457 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2458 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 2459 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2460 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 2461 | request\_\_advertisements\_\_unified\_yield\_\_replaced\_type | 6 |  |  |  |  | FALSE |
| 2462 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_id | 6 |  |  |  |  | FALSE |
| 2463 | request\_\_bidding\_context\_\_bid\_request\_\_device\_\_ifa | 6 |  |  |  |  | FALSE |
| 2464 | request\_\_slots\_\_resellers\_\_inbound\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 2465 | request\_\_slots\_\_outbound\_order\_\_unified\_priority | 6 |  |  |  |  | FALSE |
| 2466 | request\_\_rtb\_auction\_\_auction\_status | 6 |  |  |  |  | FALSE |
| 2467 | request\_\_slots\_\_outbound\_order\_\_active\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 2468 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2469 | acks\_\_psn\_msg\_\_distributor\_id\_raw | 6 |  |  |  |  | FALSE |
| 2470 | request\_\_slots\_\_carriage\_listing\_origin\_split\_unit\_num | 6 |  |  |  |  | FALSE |
| 2471 | request\_\_decision\_info\_\_reject\_ads\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 2472 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2473 | request\_\_slots\_\_cue\_point\_sequence | 6 |  |  |  |  | FALSE |
| 2474 | request\_\_advertisements\_\_distributor\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 2475 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2476 | request\_\_advertisements\_\_distributor\_\_rule\_id | 6 |  |  |  |  | FALSE |
| 2477 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2478 | request\_\_context\_\_ux\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 2479 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 2480 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_unconstraint\_gross\_avail\_committed | 6 |  |  |  |  | FALSE |
| 2481 | request\_\_advertisements\_\_deprecate\_\_acked\_ad\_impression | 6 |  |  |  |  | FALSE |
| 2482 | acks\_\_metrics\_\_raw\_measurable\_ad\_rewind\_impression | 6 |  |  |  |  | FALSE |
| 2483 | request\_\_slots\_\_inbound\_rule\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2484 | request\_\_advertisements\_\_content\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2485 | request\_\_rtb\_auction\_\_ab\_test\_item\_index | 6 |  |  |  |  | FALSE |
| 2486 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 2487 | request\_\_auction\_network\_contexts\_\_auction\_network\_to\_usd\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 2488 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 2489 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 2490 | request\_\_advertisements\_\_variant\_creative\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2491 | request\_\_advertisements\_\_replaced\_rendition\_id\_raw | 6 |  |  |  |  | FALSE |
| 2492 | forecast\_\_plan\_id | 6 |  |  |  |  | FALSE |
| 2493 | request\_\_advertisements\_\_distributor\_\_rule\_priority | 6 |  |  |  |  | FALSE |
| 2494 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 2495 | request\_\_advertisements\_\_content\_right\_owner\_\_context\_id | 6 |  |  |  |  | FALSE |
| 2496 | request\_\_external\_candidate\_ad\_\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 2497 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 2498 | request\_\_ifa | 6 |  |  |  |  | FALSE |
| 2499 | request\_\_advertisements\_\_network\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 2500 | request\_\_decision\_info\_\_candidates\_info | 6 |  |  |  |  | FALSE |
| 2501 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 2502 | request\_\_external\_candidate\_ad\_\_site\_id | 6 |  |  |  |  | FALSE |
| 2503 | request\_\_slots\_\_sponsor\_ad | 6 |  |  |  |  | FALSE |
| 2504 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 2505 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 2506 | uids\_\_external\_candidate\_uid | 6 |  |  |  |  | FALSE |
| 2507 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 2508 | request\_\_audience\_item\_\_active\_kv\_term\_id\_raw | 6 |  |  |  |  | FALSE |
| 2509 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2510 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2511 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2512 | acks\_\_metrics\_\_raw\_click | 6 |  |  |  |  | FALSE |
| 2513 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 2514 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2515 | request\_\_slots\_\_resellers\_\_avails\_metrics\_\_default\_duration | 6 |  |  |  |  | FALSE |
| 2516 | acks\_\_deprecate\_\_third\_quartile | 6 |  |  |  |  | FALSE |
| 2517 | request\_\_network\_execution\_ctx\_\_floor\_price | 6 |  |  |  |  | FALSE |
| 2518 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 2519 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2520 | request\_\_external\_candidate\_ad\_\_global\_industry\_ids | 6 |  |  |  |  | FALSE |
| 2521 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 2522 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 2523 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2524 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2525 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2526 | request\_\_slots\_\_resellers\_\_forecast\_avails\_metrics | 6 |  |  |  |  | FALSE |
| 2527 | acks\_\_metrics\_\_raw\_video\_view | 6 |  |  |  |  | FALSE |
| 2528 | request\_\_advertisements\_\_content\_owner\_\_revenue | 6 |  |  |  |  | FALSE |
| 2529 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2530 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 2531 | request\_\_network\_attribute\_\_id\_graph\_\_policy\_\_alias\_\_id | 6 |  |  |  |  | FALSE |
| 2532 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2533 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2534 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2535 | aim\_info\_\_envelope\_info\_\_envelope\_identifiers\_\_type | 6 |  |  |  |  | FALSE |
| 2536 | acks\_\_psn\_msg\_\_ad\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2537 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 2538 | request\_\_advertisements\_\_unified\_yield\_\_replaced\_entity\_id\_raw | 6 |  |  |  |  | FALSE |
| 2539 | uids\_\_request\_uid | 6 |  |  |  |  | FALSE |
| 2540 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2541 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2542 | request\_\_visitor\_\_ortb\_fields\_from\_ua | 6 |  |  |  |  | FALSE |
| 2543 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 2544 | request\_\_slots\_\_attrition\_ratio\_\_event\_ratio | 6 |  |  |  |  | FALSE |
| 2545 | request\_\_advertisements\_\_reseller\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 2546 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 2547 | request\_\_advertisements\_\_content\_right\_owner\_\_margin | 6 |  |  |  |  | FALSE |
| 2548 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_revenue | 6 |  |  |  |  | FALSE |
| 2549 | request\_\_advertisements\_\_network\_\_role | 6 |  |  |  |  | FALSE |
| 2550 | request\_\_slots\_\_outbound\_order\_\_unified\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 2551 | request\_\_advertisements\_\_advertisement\_context\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2552 | request\_\_external\_candidate\_ad\_\_post\_auction\_discount\_id | 6 |  |  |  |  | FALSE |
| 2553 | request\_\_advertisements\_\_content\_right\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2554 | request\_\_advertisements\_\_reseller\_\_marketplace\_audience\_extension\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 2555 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2556 | request\_\_external\_candidate\_ad\_\_bidding\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 2557 | request\_\_visitor\_\_user\_segments\_lookup\_key | 6 |  |  |  |  | FALSE |
| 2558 | request\_\_slots\_\_rules\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2559 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 2560 | request\_\_network\_execution\_ctx\_\_inventory\_\_series\_id | 6 |  |  |  |  | FALSE |
| 2561 | request\_\_advertisements\_\_unified\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 2562 | request\_\_context\_\_asset\_chain\_\_inventory\_context | 6 |  |  |  |  | FALSE |
| 2563 | request\_\_advertisements\_\_deprecate\_\_third\_quartile | 6 |  |  |  |  | FALSE |
| 2564 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 2565 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 2566 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2567 | request\_\_advertisements\_\_external\_reseller\_\_up\_revenue\_as\_content\_owner | 6 |  |  |  |  | FALSE |
| 2568 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 2569 | request\_\_external\_candidate\_ad\_\_advertiser\_domain | 6 |  |  |  |  | FALSE |
| 2570 | request\_\_rtb\_auction\_\_series\_id | 6 |  |  |  |  | FALSE |
| 2571 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 2572 | request\_\_errors\_\_ad\_replica\_id | 6 |  |  |  |  | FALSE |
| 2573 | request\_\_slots\_\_rules\_\_win\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 2574 | request\_\_slots\_\_resellers\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 6 |  |  |  |  | FALSE |
| 2575 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 6 |  |  |  |  | FALSE |
| 2576 | request\_\_rtb\_auction\_\_dsp\_id\_raw | 6 |  |  |  |  | FALSE |
| 2577 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 2578 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 2579 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_unconstraint\_gross\_avail | 6 |  |  |  |  | FALSE |
| 2580 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2581 | request\_\_rtb\_auction\_\_execution\_node\_id | 6 |  |  |  |  | FALSE |
| 2582 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 2583 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_hhids | 6 |  |  |  |  | FALSE |
| 2584 | request\_\_advertisements\_\_content\_owner\_\_bidding\_revenue | 6 |  |  |  |  | FALSE |
| 2585 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 2586 | request\_\_rtb\_auction\_\_external\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2587 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2588 | request\_\_network\_execution\_ctx\_\_inventory\_\_mapped\_site\_section\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2589 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 6 |  |  |  |  | FALSE |
| 2590 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 2591 | request\_\_advertisements\_\_distributor\_\_series\_id | 6 |  |  |  |  | FALSE |
| 2592 | request\_\_external\_candidate\_ad\_\_pod\_replica\_id | 6 |  |  |  |  | FALSE |
| 2593 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 2594 | request\_\_context\_\_standard\_addressability\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2595 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 2596 | request\_\_external\_candidate\_ad\_\_internal\_ad\_index | 6 |  |  |  |  | FALSE |
| 2597 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2598 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 2599 | request\_\_network\_audience\_items | 6 |  |  |  |  | FALSE |
| 2600 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2601 | request\_\_advertisements\_\_creative\_id\_raw | 6 |  |  |  |  | FALSE |
| 2602 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 2603 | request\_\_external\_candidate\_ad\_\_internal\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 2604 | request\_\_advertisements\_\_distributor\_\_unified\_rule\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 2605 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 2606 | request\_\_advertisements\_\_reseller\_\_bidding\_down\_revenue | 6 |  |  |  |  | FALSE |
| 2607 | request\_\_rtb\_auction\_\_time\_position\_class | 6 |  |  |  |  | FALSE |
| 2608 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 2609 | request\_\_slots\_\_attrition\_ratio\_\_ad\_view\_ratio | 6 |  |  |  |  | FALSE |
| 2610 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 2611 | request\_\_advertisements\_\_trimmed\_tracking\_domains\_\_domain\_package\_ids | 6 |  |  |  |  | FALSE |
| 2612 | request\_\_errors\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 2613 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 2614 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver | 6 |  |  |  |  | FALSE |
| 2615 | request\_\_context\_\_asset\_chain\_\_distributor\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 2616 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 2617 | request\_\_advertisements\_\_estimated\_start\_delay | 6 |  |  |  |  | FALSE |
| 2618 | acks\_\_nielsen\_demographic\_id | 6 |  |  |  |  | FALSE |
| 2619 | request\_\_advertisements\_\_contextual\_billings\_\_cpm | 6 |  |  |  |  | FALSE |
| 2620 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 2621 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2622 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 2623 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes | 6 |  |  |  |  | FALSE |
| 2624 | forecast\_\_metrics\_\_portfolio\_competing\_map | 6 |  |  |  |  | FALSE |
| 2625 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 2626 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2627 | request\_\_rtb\_auction\_\_internal\_seat\_id\_raw | 6 |  |  |  |  | FALSE |
| 2628 | request\_\_slots\_\_opportunity\_id | 6 |  |  |  |  | FALSE |
| 2629 | request\_\_advertisements\_\_external\_reseller\_\_count\_imp\_as\_booked | 6 |  |  |  |  | FALSE |
| 2630 | request\_\_context\_\_distributor\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2631 | request\_\_slots\_\_sfx\_avails | 6 |  |  |  |  | FALSE |
| 2632 | acks\_\_keys\_\_is\_zero\_revenue | 6 |  |  |  |  | FALSE |
| 2633 | request\_\_advertisements\_\_abstract\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 2634 | request\_\_context\_\_external\_key\_value\_\_key | 6 |  |  |  |  | FALSE |
| 2635 | request\_\_advertisements\_\_external\_reseller\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 2636 | slot\_\_rules\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2637 | request\_\_network\_execution\_ctx\_\_upstream\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2638 | request\_\_context\_\_standard\_content\_subscription\_model\_id\_raw | 6 |  |  |  |  | FALSE |
| 2639 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2640 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2641 | request\_\_advertisements\_\_external\_reseller\_\_marketplace\_audience\_extension\_deal\_id | 6 |  |  |  |  | FALSE |
| 2642 | request\_\_advertisements\_\_reseller\_\_rule\_id | 6 |  |  |  |  | FALSE |
| 2643 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2644 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 2645 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_currency | 6 |  |  |  |  | FALSE |
| 2646 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 2647 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 2648 | request\_\_advertisements\_\_distributor\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2649 | acks\_\_metrics\_\_ad\_close | 6 |  |  |  |  | FALSE |
| 2650 | request\_\_context\_\_site\_section\_cro\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 2651 | request\_\_audience\_item\_\_audience\_item\_id\_raw | 6 |  |  |  |  | FALSE |
| 2652 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2653 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_iids\_\_id | 6 |  |  |  |  | FALSE |
| 2654 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key | 6 |  |  |  |  | FALSE |
| 2655 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 2656 | request\_\_advertisements\_\_global\_brand\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2657 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 2658 | request\_\_advertisements\_\_content\_right\_owner\_\_up\_revenue\_as\_content\_owner | 6 |  |  |  |  | FALSE |
| 2659 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 2660 | request\_\_external\_candidate\_ad\_\_global\_agency\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2661 | request\_\_advertisements\_\_content\_owner\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 2662 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 2663 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 2664 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 2665 | request\_\_slots\_\_break\_id\_raw | 6 |  |  |  |  | FALSE |
| 2666 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_total\_avail | 6 |  |  |  |  | FALSE |
| 2667 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2668 | acks\_\_deprecate\_\_creative\_id\_raw | 6 |  |  |  |  | FALSE |
| 2669 | request\_\_slots\_\_resellers\_\_marketplace\_audience\_extension\_deal\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2670 | aim\_info\_\_aim\_audience\_info\_\_flag | 6 |  |  |  |  | FALSE |
| 2671 | request\_\_slots\_\_resellers\_\_ad\_unit\_default\_duration | 6 |  |  |  |  | FALSE |
| 2672 | request\_\_advertisements\_\_network\_\_reseller\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2673 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 2674 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 2675 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails\_committed\_\_key | 6 |  |  |  |  | FALSE |
| 2676 | forecast\_\_meta\_\_request\_time | 6 |  |  |  |  | FALSE |
| 2677 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 2678 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 2679 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 6 |  |  |  |  | FALSE |
| 2680 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_revenue | 6 |  |  |  |  | FALSE |
| 2681 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2682 | acks\_\_psn\_msg\_\_content\_provider\_id | 6 |  |  |  |  | FALSE |
| 2683 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_active\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 2684 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_scheduled\_impression | 6 |  |  |  |  | FALSE |
| 2685 | forecast\_\_metrics\_\_transactional\_map\_\_key | 6 |  |  |  |  | FALSE |
| 2686 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 2687 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 2688 | request\_\_advertisements\_\_shading\_context\_\_bid\_floor\_price\_usd | 6 |  |  |  |  | FALSE |
| 2689 | request\_\_advertisements\_\_variant\_rendition\_ids | 6 |  |  |  |  | FALSE |
| 2690 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 2691 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 2692 | request\_\_advertisements\_\_content\_owner\_\_ad\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 2693 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2694 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2695 | request\_\_advertisements\_\_reseller\_\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 2696 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 2697 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2698 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2699 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 2700 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 2701 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 2702 | request\_\_global\_currency\_\_currencies\_\_exchange\_rates\_\_rate | 6 |  |  |  |  | FALSE |
| 2703 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 2704 | request\_\_rtb\_auction\_\_header\_bidding\_key\_value\_index | 6 |  |  |  |  | FALSE |
| 2705 | forecast\_\_meta\_\_override\_geo\_term | 6 |  |  |  |  | FALSE |
| 2706 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value | 6 |  |  |  |  | FALSE |
| 2707 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 2708 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 2709 | request\_\_rtb\_auction\_\_deal\_\_media\_buyer\_id | 6 |  |  |  |  | FALSE |
| 2710 | request\_\_external\_candidate\_ad\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2711 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 2712 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 2713 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2714 | request\_\_external\_candidate\_ad\_\_media\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 2715 | request\_\_external\_candidate\_ad\_\_creative\_approval\_request\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2716 | request\_\_advertisements\_\_content\_owner\_\_series\_id | 6 |  |  |  |  | FALSE |
| 2717 | request\_\_advertisements\_\_global\_advertiser\_id | 6 |  |  |  |  | FALSE |
| 2718 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 2719 | request\_\_advertisements\_\_content\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2720 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 2721 | request\_\_guaranteed\_deal\_avail\_\_internal\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 2722 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2723 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 2724 | request\_\_advertisements\_\_unified\_yield\_\_substitute\_type | 6 |  |  |  |  | FALSE |
| 2725 | request\_\_advertisements\_\_external\_reseller\_\_rule\_id | 6 |  |  |  |  | FALSE |
| 2726 | request\_\_advertisements\_\_advertisement\_context | 6 |  |  |  |  | FALSE |
| 2727 | request\_\_external\_candidate\_ad\_\_internal\_seat\_id | 6 |  |  |  |  | FALSE |
| 2728 | request\_\_inventory\_group | 6 |  |  |  |  | FALSE |
| 2729 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_net\_avail | 6 |  |  |  |  | FALSE |
| 2730 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 2731 | request\_\_slots\_\_resellers\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 2732 | request\_\_slots\_\_resellers\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 2733 | request\_\_context\_\_header\_bidding\_\_key\_value\_\_value | 6 |  |  |  |  | FALSE |
| 2734 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2735 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver\_committed | 6 |  |  |  |  | FALSE |
| 2736 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 2737 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2738 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_forecast\_portfolio\_id\_raw | 6 |  |  |  |  | FALSE |
| 2739 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 2740 | request\_\_advertisements\_\_network\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2741 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 2742 | acks\_\_metrics\_\_raw\_can\_quartile | 6 |  |  |  |  | FALSE |
| 2743 | request\_\_context\_\_video\_cro\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2744 | request\_\_decision\_info\_\_decision\_log\_2 | 6 |  |  |  |  | FALSE |
| 2745 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_order\_transaction\_type | 6 |  |  |  |  | FALSE |
| 2746 | request\_\_external\_candidate\_ad\_\_ortb\_fwpartners\_\_idtype | 6 |  |  |  |  | FALSE |
| 2747 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 2748 | forecast\_\_meta\_\_n\_mid | 6 |  |  |  |  | FALSE |
| 2749 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails\_committed\_\_value | 6 |  |  |  |  | FALSE |
| 2750 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails\_committed | 6 |  |  |  |  | FALSE |
| 2751 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 2752 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 2753 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 2754 | request\_\_context\_\_external\_key\_value\_\_value | 6 |  |  |  |  | FALSE |
| 2755 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 2756 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_total\_avail | 6 |  |  |  |  | FALSE |
| 2757 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 2758 | request\_\_visitor\_\_identity\_user\_ids\_\_authorized\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2759 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2760 | request\_\_rtb\_auction\_\_execution\_contexts\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2761 | request\_\_advertisements\_\_companion\_ad\_uniq\_id\_raw | 6 |  |  |  |  | FALSE |
| 2762 | request\_\_slots\_\_selection\_info | 6 |  |  |  |  | FALSE |
| 2763 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_parent | 6 |  |  |  |  | FALSE |
| 2764 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 2765 | request\_\_advertisements\_\_reseller\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 2766 | request\_\_context\_\_site\_section\_chain\_\_inventory\_context | 6 |  |  |  |  | FALSE |
| 2767 | request\_\_advertisements\_\_content\_right\_owner\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 2768 | request\_\_network\_attribute\_\_id\_graph\_\_policy | 6 |  |  |  |  | FALSE |
| 2769 | request\_\_slots\_\_resellers\_\_forecast\_avails\_metrics\_\_total\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 2770 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 2771 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2772 | request\_\_advertisements\_\_external\_reseller\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 2773 | request\_\_slots\_\_outbound\_order | 6 |  |  |  |  | FALSE |
| 2774 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 2775 | acks\_\_metrics\_\_error | 6 |  |  |  |  | FALSE |
| 2776 | request\_\_advertisements\_\_active\_data\_suite\_segment | 6 |  |  |  |  | FALSE |
| 2777 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 2778 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 2779 | request\_\_advertisements\_\_position\_in\_slot | 6 |  |  |  |  | FALSE |
| 2780 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 2781 | request\_\_advertisements\_\_external\_reseller\_\_ssp\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 2782 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_iids | 6 |  |  |  |  | FALSE |
| 2783 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 2784 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_is\_guaranteed | 6 |  |  |  |  | FALSE |
| 2785 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2786 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 2787 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 2788 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_hhids\_\_type | 6 |  |  |  |  | FALSE |
| 2789 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2790 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails\_\_key | 6 |  |  |  |  | FALSE |
| 2791 | request\_\_advertisements\_\_reseller\_\_revenue | 6 |  |  |  |  | FALSE |
| 2792 | request\_\_slots\_\_resellers\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2793 | forecast\_\_metrics\_\_transactional\_map\_\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 2794 | request\_\_advertisements\_\_distributor\_\_up\_revenue\_as\_content\_owner | 6 |  |  |  |  | FALSE |
| 2795 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 2796 | request\_\_advertisements\_\_rules\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2797 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2798 | request\_\_network\_attribute\_\_id\_graph\_\_vendor | 6 |  |  |  |  | FALSE |
| 2799 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 2800 | request\_\_external\_candidate\_ad\_\_redirect\_count | 6 |  |  |  |  | FALSE |
| 2801 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_pretty\_dimension\_ids | 6 |  |  |  |  | FALSE |
| 2802 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 2803 | acks\_\_psn\_msg\_\_spot\_asset\_id | 6 |  |  |  |  | FALSE |
| 2804 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_flags | 6 |  |  |  |  | FALSE |
| 2805 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 2806 | request\_\_errors\_\_http\_status\_code | 6 |  |  |  |  | FALSE |
| 2807 | request\_\_advertisements\_\_reseller\_\_supply\_distribution\_cost | 6 |  |  |  |  | FALSE |
| 2808 | request\_\_advertisements\_\_distributor\_\_bidding\_up\_revenue | 6 |  |  |  |  | FALSE |
| 2809 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 2810 | request\_\_advertisements\_\_vast\_creative\_id | 6 |  |  |  |  | FALSE |
| 2811 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 2812 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2813 | request\_\_advertisements\_\_content\_owner\_\_ssp\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 2814 | request\_\_rtb\_auction\_\_deal\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 2815 | request\_\_advertisements\_\_global\_industry\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2816 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 2817 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_id | 6 |  |  |  |  | FALSE |
| 2818 | request\_\_slots\_\_original\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 2819 | idx\_\_is\_filtered\_transaction | 6 |  |  |  |  | FALSE |
| 2820 | request\_\_external\_candidate\_ad\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 2821 | request\_\_rtb\_auction\_\_deal\_\_auction\_type | 6 |  |  |  |  | FALSE |
| 2822 | acks\_\_event\_key\_values | 6 |  |  |  |  | FALSE |
| 2823 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 2824 | request\_\_network\_execution\_ctx\_\_data\_right\_\_value | 6 |  |  |  |  | FALSE |
| 2825 | request\_\_slots\_\_resellers\_\_avails\_metrics\_\_seller\_sponsor\_avails | 6 |  |  |  |  | FALSE |
| 2826 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_total\_capacity | 6 |  |  |  |  | FALSE |
| 2827 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 2828 | request\_\_external\_candidate\_ad\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2829 | request\_\_global\_currency\_\_currencies\_\_exchange\_rates\_\_destination\_currency\_id | 6 |  |  |  |  | FALSE |
| 2830 | request\_\_visitor\_\_standard\_retailer\_id\_raw | 6 |  |  |  |  | FALSE |
| 2831 | aim\_info\_\_aim\_identity\_info\_\_categorized\_signals\_\_id | 6 |  |  |  |  | FALSE |
| 2832 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2833 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 2834 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 2835 | request\_\_network\_execution\_ctx\_\_inventory | 6 |  |  |  |  | FALSE |
| 2836 | idx\_\_server\_id | 6 |  |  |  |  | FALSE |
| 2837 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 2838 | acks\_\_unit | 6 |  |  |  |  | FALSE |
| 2839 | request\_\_advertisements\_\_distributor\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2840 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 2841 | request\_\_advertisements\_\_shading\_context\_\_shading\_model\_name | 6 |  |  |  |  | FALSE |
| 2842 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 2843 | request\_\_external\_candidate\_ad\_\_global\_advertiser\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2844 | request\_\_visitor\_\_standard\_manufacturer\_id | 6 |  |  |  |  | FALSE |
| 2845 | request\_\_slots\_\_impression\_weight | 6 |  |  |  |  | FALSE |
| 2846 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 2847 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_effective\_exclude\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 2848 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics | 6 |  |  |  |  | FALSE |
| 2849 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 2850 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics\_\_seller\_sponsor\_avails | 6 |  |  |  |  | FALSE |
| 2851 | request\_\_rtb\_auction\_\_auction\_sampling\_\_magnifier | 6 |  |  |  |  | FALSE |
| 2852 | request\_\_advertisements\_\_external\_reseller\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 2853 | request\_\_advertisements\_\_distributor\_\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 2854 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 2855 | request\_\_rtb\_auction\_\_extra\_flags | 6 |  |  |  |  | FALSE |
| 2856 | request\_\_external\_candidate\_ad\_\_internal\_group\_deal\_id | 6 |  |  |  |  | FALSE |
| 2857 | request\_\_advertisements\_\_deprecate\_\_mid\_point | 6 |  |  |  |  | FALSE |
| 2858 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 2859 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 2860 | idx\_\_is\_mkpl\_traffic | 6 |  |  |  |  | FALSE |
| 2861 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 2862 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 2863 | request\_\_advertisements\_\_content\_right\_owner\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 2864 | request\_\_slots\_\_eligible\_carriage\_listing\_split\_unit\_ids | 6 |  |  |  |  | FALSE |
| 2865 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2866 | request\_\_slots\_\_creative\_api | 6 |  |  |  |  | FALSE |
| 2867 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 2868 | request\_\_network\_execution\_ctx\_\_inventory\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2869 | request\_\_advertisements\_\_distributor\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 2870 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_ext\_id\_raw | 6 |  |  |  |  | FALSE |
| 2871 | forecast\_\_cookies\_\_new\_cookie | 6 |  |  |  |  | FALSE |
| 2872 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2873 | request\_\_slots\_\_resellers\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2874 | request\_\_advertisements\_\_rules\_\_win\_rule\_id | 6 |  |  |  |  | FALSE |
| 2875 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 2876 | request\_\_advertisements\_\_distributor\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 2877 | request\_\_global\_currency\_\_currencies\_\_exchange\_rates\_\_destination\_currency\_id\_raw | 6 |  |  |  |  | FALSE |
| 2878 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 2879 | request\_\_rtb\_auction\_\_deal\_\_bid\_floor | 6 |  |  |  |  | FALSE |
| 2880 | request\_\_advertisements\_\_rules\_\_opp\_rule\_id | 6 |  |  |  |  | FALSE |
| 2881 | request\_\_advertisements\_\_replaced\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 2882 | request\_\_advertisements\_\_content\_owner\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 2883 | acks\_\_identifier\_\_sequence | 6 |  |  |  |  | FALSE |
| 2884 | request\_\_slots\_\_outbound\_order\_\_order\_priority | 6 |  |  |  |  | FALSE |
| 2885 | request\_\_rtb\_auction\_\_auction\_sampling | 6 |  |  |  |  | FALSE |
| 2886 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2887 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 2888 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 2889 | request\_\_advertisements\_\_inventory\_protection\_flags | 6 |  |  |  |  | FALSE |
| 2890 | forecast\_\_predict\_date | 6 |  |  |  |  | FALSE |
| 2891 | request\_\_qam\_headend\_segment\_zipcode | 6 |  |  |  |  | FALSE |
| 2892 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_channel\_id | 6 |  |  |  |  | FALSE |
| 2893 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2894 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 2895 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2896 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 2897 | request\_\_advertisements\_\_nielsen\_site\_url\_id | 6 |  |  |  |  | FALSE |
| 2898 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 2899 | request\_\_advertisements\_\_validation\_event\_\_numerator\_event\_id | 6 |  |  |  |  | FALSE |
| 2900 | request\_\_rtb\_auction\_\_execution\_node\_id\_raw | 6 |  |  |  |  | FALSE |
| 2901 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_context\_id | 6 |  |  |  |  | FALSE |
| 2902 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2903 | request\_\_advertisements\_\_content\_owner\_\_rule\_priority | 6 |  |  |  |  | FALSE |
| 2904 | request\_\_slots\_\_outbound\_order\_\_price | 6 |  |  |  |  | FALSE |
| 2905 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 2906 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2907 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2908 | request\_\_external\_candidate\_ad\_\_site\_section\_id | 6 |  |  |  |  | FALSE |
| 2909 | request\_\_slots\_\_adunit\_podgroup\_offset | 6 |  |  |  |  | FALSE |
| 2910 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_forecast\_portfolio\_id\_raw | 6 |  |  |  |  | FALSE |
| 2911 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2912 | request\_\_advertisements\_\_distributor\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 2913 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_coincidence | 6 |  |  |  |  | FALSE |
| 2914 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 2915 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 2916 | request\_\_advertisements\_\_ad\_view\_ratio | 6 |  |  |  |  | FALSE |
| 2917 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 2918 | request\_\_network\_execution\_ctx\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2919 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 2920 | request\_\_slots\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id\_raw | 6 |  |  |  |  | FALSE |
| 2921 | request\_\_advertisements\_\_distributor\_\_rule\_ext\_id | 6 |  |  |  |  | FALSE |
| 2922 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 2923 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 2924 | request\_\_context\_\_standard\_content\_viewership\_profile\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2925 | request\_\_advertisements\_\_network\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 2926 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 2927 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 2928 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 2929 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 2930 | request\_\_slots\_\_resellers\_\_avails\_metrics\_\_opportunity | 6 |  |  |  |  | FALSE |
| 2931 | request\_\_rtb\_auction\_\_impression\_\_bid\_floor\_uplift | 6 |  |  |  |  | FALSE |
| 2932 | request\_\_audience\_item\_\_active\_kv\_term\_id | 6 |  |  |  |  | FALSE |
| 2933 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 2934 | request\_\_external\_bridge\_records\_\_error | 6 |  |  |  |  | FALSE |
| 2935 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 2936 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_series\_id | 6 |  |  |  |  | FALSE |
| 2937 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 2938 | request\_\_external\_candidate\_ad\_\_response\_industry | 6 |  |  |  |  | FALSE |
| 2939 | request\_\_advertisements\_\_content\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 2940 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 2941 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_ver | 6 |  |  |  |  | FALSE |
| 2942 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_unconstraint\_gross\_avail | 6 |  |  |  |  | FALSE |
| 2943 | acks\_\_metrics\_\_raw\_first\_quartile | 6 |  |  |  |  | FALSE |
| 2944 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 2945 | request\_\_slots\_\_inbound\_rule\_\_win\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 2946 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 2947 | request\_\_external\_candidate\_ad\_\_buyer\_group\_id | 6 |  |  |  |  | FALSE |
| 2948 | acks\_\_callback\_server\_id | 6 |  |  |  |  | FALSE |
| 2949 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 2950 | request\_\_context\_\_asset\_chain\_\_distributor\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 2951 | acks\_\_pingback\_pixel\_id\_raw | 6 |  |  |  |  | FALSE |
| 2952 | request\_\_rtb\_auction\_\_buyer\_id | 6 |  |  |  |  | FALSE |
| 2953 | request\_\_advertisements\_\_distributor\_\_ad\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 2954 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 2955 | request\_\_slots\_\_resellers\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 2956 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 2957 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 2958 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 2959 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 2960 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 2961 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 2962 | request\_\_rtb\_auction\_\_flags | 6 |  |  |  |  | FALSE |
| 2963 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 2964 | request\_\_advertisements\_\_content\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 2965 | request\_\_external\_candidate\_ad\_\_bidding\_seat\_id\_raw | 6 |  |  |  |  | FALSE |
| 2966 | request\_\_global\_currency | 6 |  |  |  |  | FALSE |
| 2967 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 2968 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 2969 | request\_\_bidding\_context\_\_bid\_request\_\_wseat | 6 |  |  |  |  | FALSE |
| 2970 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_exempt\_thousandth | 6 |  |  |  |  | FALSE |
| 2971 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 2972 | request\_\_context\_\_ux\_conf\_id\_raw | 6 |  |  |  |  | FALSE |
| 2973 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 2974 | request\_\_context\_\_time\_span\_\_duration | 6 |  |  |  |  | FALSE |
| 2975 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 2976 | request\_\_external\_bridge\_records\_\_flags | 6 |  |  |  |  | FALSE |
| 2977 | request\_\_context\_\_video\_cro\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 2978 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_scheduled\_impression | 6 |  |  |  |  | FALSE |
| 2979 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 2980 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 2981 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 2982 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 2983 | acks\_\_metrics\_\_raw\_middle\_quartile | 6 |  |  |  |  | FALSE |
| 2984 | request\_\_context\_\_standard\_sport\_entity\_ids\_raw | 6 |  |  |  |  | FALSE |
| 2985 | request\_\_advertisements\_\_scenario\_id\_raw | 6 |  |  |  |  | FALSE |
| 2986 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2987 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 2988 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 2989 | forecast\_\_round | 6 |  |  |  |  | FALSE |
| 2990 | request\_\_slots\_\_ad\_units | 6 |  |  |  |  | FALSE |
| 2991 | request\_\_advertisements\_\_network\_\_revenue | 6 |  |  |  |  | FALSE |
| 2992 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 2993 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 2994 | request\_\_advertisements\_\_spot\_id | 6 |  |  |  |  | FALSE |
| 2995 | request\_\_external\_candidate\_ad\_\_external\_network\_id | 6 |  |  |  |  | FALSE |
| 2996 | request\_\_soft\_guaranteed\_ad\_\_entity\_id\_raw | 6 |  |  |  |  | FALSE |
| 2997 | request\_\_advertisements\_\_external\_reseller\_\_context\_id | 6 |  |  |  |  | FALSE |
| 2998 | request\_\_advertisements\_\_deprecate\_\_buy\_cost | 6 |  |  |  |  | FALSE |
| 2999 | request\_\_external\_candidate\_ad\_\_dsp\_currency\_id\_raw | 6 |  |  |  |  | FALSE |
| 3000 | request\_\_inventory\_group\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3001 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3002 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_associated\_impression | 6 |  |  |  |  | FALSE |
| 3003 | request\_\_slots\_\_resellers\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3004 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_order\_id | 6 |  |  |  |  | FALSE |
| 3005 | request\_\_slot\_count | 6 |  |  |  |  | FALSE |
| 3006 | request\_\_network\_attribute\_\_region\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3007 | forecast\_\_metrics\_\_transactional\_map\_\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3008 | request\_\_advertisements\_\_global\_advertiser\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3009 | request\_\_slots\_\_content\_type\_id | 6 |  |  |  |  | FALSE |
| 3010 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3011 | request\_\_slots\_\_resellers\_\_inventory\_distribution\_contexts | 6 |  |  |  |  | FALSE |
| 3012 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 3013 | request\_\_global\_currency\_\_currencies | 6 |  |  |  |  | FALSE |
| 3014 | request\_\_advertisements\_\_content\_owner\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 3015 | request\_\_slots\_\_resellers\_\_carriage\_inventory\_owner\_id\_raw | 6 |  |  |  |  | FALSE |
| 3016 | request\_\_advertisements\_\_inbound\_rule\_\_win\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 3017 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 3018 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 3019 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3020 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3021 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 3022 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3023 | request\_\_external\_candidate\_ad\_\_raw\_price | 6 |  |  |  |  | FALSE |
| 3024 | request\_\_advertisements\_\_linear\_campaign\_type | 6 |  |  |  |  | FALSE |
| 3025 | request\_\_slots\_\_primary\_content\_type | 6 |  |  |  |  | FALSE |
| 3026 | request\_\_advertisements\_\_content\_owner\_\_bidding\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3027 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3028 | request\_\_advertisements\_\_companion\_ad\_uniq\_id | 6 |  |  |  |  | FALSE |
| 3029 | request\_\_advertisements\_\_replaced\_ad\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3030 | request\_\_advertisements\_\_content\_right\_owner\_\_flags | 6 |  |  |  |  | FALSE |
| 3031 | forecast\_\_meta\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3032 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 3033 | forecast\_\_cookies\_\_old\_cookie | 6 |  |  |  |  | FALSE |
| 3034 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id | 6 |  |  |  |  | FALSE |
| 3035 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3036 | acks\_\_extra\_flags | 6 |  |  |  |  | FALSE |
| 3037 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller | 6 |  |  |  |  | FALSE |
| 3038 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 3039 | request\_\_context\_\_asset\_chain\_\_distributor\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3040 | idx\_\_is\_live\_traffic | 6 |  |  |  |  | FALSE |
| 3041 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3042 | request\_\_advertisements\_\_distributor\_\_rule\_flags | 6 |  |  |  |  | FALSE |
| 3043 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 3044 | idx\_\_transaction\_id | 6 |  |  |  |  | FALSE |
| 3045 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_level | 6 |  |  |  |  | FALSE |
| 3046 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 3047 | request\_\_advertisements\_\_reseller\_\_rule\_ext\_id | 6 |  |  |  |  | FALSE |
| 3048 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 3049 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 3050 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3051 | request\_\_advertisements\_\_content\_owner\_\_marketplace\_audience\_extension\_deal\_id | 6 |  |  |  |  | FALSE |
| 3052 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3053 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_total\_capacity | 6 |  |  |  |  | FALSE |
| 3054 | request\_\_advertisements\_\_triggering\_concrete\_event\_id | 6 |  |  |  |  | FALSE |
| 3055 | request\_\_slots\_\_resellers\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 3056 | request\_\_rtb\_auction\_\_media\_buyer\_id | 6 |  |  |  |  | FALSE |
| 3057 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 3058 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 3059 | request\_\_rtb\_auction\_\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 3060 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3061 | acks\_\_deprecate\_\_nielsen\_demographic\_impression | 6 |  |  |  |  | FALSE |
| 3062 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3063 | deprecate\_\_implicit\_video\_view | 6 |  |  |  |  | FALSE |
| 3064 | request\_\_external\_candidate\_ad\_\_creative\_approval\_request\_\_approval\_type | 6 |  |  |  |  | FALSE |
| 3065 | request\_\_rtb\_auction\_\_experiment\_index | 6 |  |  |  |  | FALSE |
| 3066 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3067 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 3068 | request\_\_advertisements\_\_external\_reseller\_\_down\_network\_id | 6 |  |  |  |  | FALSE |
| 3069 | request\_\_network\_attribute\_\_comscore\_win\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3070 | request\_\_advertisements\_\_content\_owner\_\_bidding\_up\_original\_revenue | 6 |  |  |  |  | FALSE |
| 3071 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3072 | acks\_\_metrics\_\_measurable\_ad\_expand\_collapse\_impression | 6 |  |  |  |  | FALSE |
| 3073 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos | 6 |  |  |  |  | FALSE |
| 3074 | request\_\_advertisements\_\_content\_right\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3075 | request\_\_advertisements\_\_external\_reseller\_\_unified\_rule\_priority | 6 |  |  |  |  | FALSE |
| 3076 | request\_\_advertisements\_\_distributor\_\_bidding\_up\_original\_revenue | 6 |  |  |  |  | FALSE |
| 3077 | request\_\_advertisements\_\_unified\_yield\_\_replaced\_guaranteed\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3078 | request\_\_slots\_\_resellers\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 3079 | request\_\_advertisements\_\_content\_owner\_\_down\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3080 | request\_\_advertisements\_\_external\_reseller | 6 |  |  |  |  | FALSE |
| 3081 | acks\_\_psn\_msg\_\_ad\_unit\_type | 6 |  |  |  |  | FALSE |
| 3082 | request\_\_advertisements\_\_reseller\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 3083 | request\_\_slots\_\_profile\_id | 6 |  |  |  |  | FALSE |
| 3084 | request\_\_slots\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3085 | request\_\_advertisements\_\_event\_ratio | 6 |  |  |  |  | FALSE |
| 3086 | request\_\_advertisements\_\_unified\_yield | 6 |  |  |  |  | FALSE |
| 3087 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3088 | request\_\_slots\_\_resellers\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3089 | request\_\_rtb\_auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3090 | forecast\_\_meta\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3091 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 3092 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value | 6 |  |  |  |  | FALSE |
| 3093 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 3094 | request\_\_slots\_\_forecast\_avails\_metrics\_\_remaining\_avails | 6 |  |  |  |  | FALSE |
| 3095 | acks\_\_metrics\_\_slot\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 3096 | request\_\_rtb\_auction\_\_impression | 6 |  |  |  |  | FALSE |
| 3097 | acks\_\_keys\_\_is\_slot\_tpc\_roll | 6 |  |  |  |  | FALSE |
| 3098 | request\_\_external\_candidate\_ad\_\_media\_buyer\_id | 6 |  |  |  |  | FALSE |
| 3099 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 3100 | request\_\_slots\_\_attrition\_ratio | 6 |  |  |  |  | FALSE |
| 3101 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3102 | request\_\_advertisements\_\_content\_owner\_\_margin | 6 |  |  |  |  | FALSE |
| 3103 | request\_\_advertisements\_\_insertion\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3104 | request\_\_advertisements\_\_unified\_yield\_\_uplift\_ecpm | 6 |  |  |  |  | FALSE |
| 3105 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 3106 | request\_\_slots\_\_raw\_max\_ads | 6 |  |  |  |  | FALSE |
| 3107 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 3108 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key | 6 |  |  |  |  | FALSE |
| 3109 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3110 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_parent | 6 |  |  |  |  | FALSE |
| 3111 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3112 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3113 | request\_\_external\_candidate\_ad\_\_unified\_deal\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 3114 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3115 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_displacing | 6 |  |  |  |  | FALSE |
| 3116 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signals\_\_type | 6 |  |  |  |  | FALSE |
| 3117 | request\_\_external\_candidate\_ad\_\_buyer\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3118 | request\_\_advertisements\_\_rules | 6 |  |  |  |  | FALSE |
| 3119 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 3120 | request\_\_context\_\_asset\_chain\_\_distributor\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3121 | request\_\_rtb\_auction\_\_internal\_seat\_id | 6 |  |  |  |  | FALSE |
| 3122 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 3123 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3124 | request\_\_slots\_\_avails\_metrics\_\_default\_duration | 6 |  |  |  |  | FALSE |
| 3125 | request\_\_advertisements\_\_content\_right\_owner\_\_unified\_rule\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 3126 | request\_\_advertisements\_\_content\_right\_owner\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3127 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 3128 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_listing\_id | 6 |  |  |  |  | FALSE |
| 3129 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 3130 | request\_\_advertisements\_\_distributor\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 3131 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3132 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3133 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3134 | request\_\_advertisements\_\_content\_right\_owner\_\_ad\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 3135 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_pretty\_dimension\_ids | 6 |  |  |  |  | FALSE |
| 3136 | request\_\_external\_candidate\_ad\_\_dsp\_crid | 6 |  |  |  |  | FALSE |
| 3137 | acks\_\_metrics\_\_slot\_avails | 6 |  |  |  |  | FALSE |
| 3138 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3139 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 3140 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 3141 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3142 | request\_\_visitor\_\_postal\_code\_package | 6 |  |  |  |  | FALSE |
| 3143 | request\_\_slots\_\_original\_max\_ads | 6 |  |  |  |  | FALSE |
| 3144 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3145 | request\_\_advertisements\_\_booked\_percentage | 6 |  |  |  |  | FALSE |
| 3146 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 3147 | request\_\_slots\_\_resellers\_\_market\_avails | 6 |  |  |  |  | FALSE |
| 3148 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3149 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_unconstraint\_gross\_avail | 6 |  |  |  |  | FALSE |
| 3150 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 3151 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_floor | 6 |  |  |  |  | FALSE |
| 3152 | request\_\_async\_logging\_latency | 6 |  |  |  |  | FALSE |
| 3153 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 3154 | acks\_\_keys\_\_is\_filtered | 6 |  |  |  |  | FALSE |
| 3155 | request\_\_external\_candidate\_ad\_\_global\_advertiser\_ids | 6 |  |  |  |  | FALSE |
| 3156 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3157 | request\_\_audience\_item\_\_flags | 6 |  |  |  |  | FALSE |
| 3158 | request\_\_slots\_\_forecast\_avails\_metrics\_\_booked\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 3159 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 3160 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 3161 | request\_\_advertisements\_\_content\_right\_owner\_\_down\_network\_id | 6 |  |  |  |  | FALSE |
| 3162 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_scenario\_id | 6 |  |  |  |  | FALSE |
| 3163 | request\_\_advertisements\_\_content\_owner\_\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3164 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 3165 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 3166 | acks\_\_internal\_candidate\_index | 6 |  |  |  |  | FALSE |
| 3167 | request\_\_slots\_\_deprecate\_\_slot\_impression | 6 |  |  |  |  | FALSE |
| 3168 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 3169 | request\_\_advertisements\_\_distributor\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3170 | aim\_info\_\_aim\_audience\_info\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3171 | acks\_\_metrics\_\_raw\_ad\_minimize | 6 |  |  |  |  | FALSE |
| 3172 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 3173 | request\_\_bidding\_context\_\_bid\_request\_\_network\_\_name | 6 |  |  |  |  | FALSE |
| 3174 | request\_\_slots\_\_resellers\_\_carriage\_listing\_split\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 3175 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 3176 | request\_\_external\_candidate\_ad\_\_internal\_deal\_id | 6 |  |  |  |  | FALSE |
| 3177 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver | 6 |  |  |  |  | FALSE |
| 3178 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3179 | acks\_\_psn\_msg\_\_content\_asset\_id | 6 |  |  |  |  | FALSE |
| 3180 | request\_\_context\_\_time\_span\_\_start | 6 |  |  |  |  | FALSE |
| 3181 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3182 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_is\_guaranteed | 6 |  |  |  |  | FALSE |
| 3183 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 3184 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3185 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3186 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 3187 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3188 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 3189 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_audience\_partner\_id | 6 |  |  |  |  | FALSE |
| 3190 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order | 6 |  |  |  |  | FALSE |
| 3191 | request\_\_visitor\_\_session\_id | 6 |  |  |  |  | FALSE |
| 3192 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3193 | request\_\_soft\_guaranteed\_ad\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3194 | aim\_info\_\_aim\_audience\_info\_\_source\_signal\_indices | 6 |  |  |  |  | FALSE |
| 3195 | request\_\_advertisements\_\_replaced\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3196 | request\_\_external\_candidate\_ad\_\_sfx\_buyer\_id | 6 |  |  |  |  | FALSE |
| 3197 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_gross\_avail | 6 |  |  |  |  | FALSE |
| 3198 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3199 | request\_\_rtb\_auction\_\_deal\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 3200 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3201 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 3202 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3203 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 3204 | uids\_\_row\_uid | 6 |  |  |  |  | FALSE |
| 3205 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 3206 | request\_\_external\_candidate\_ad\_\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3207 | request\_\_context\_\_site\_\_page\_hash | 6 |  |  |  |  | FALSE |
| 3208 | request\_\_slots\_\_slot\_context\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3209 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 3210 | request\_\_external\_candidate\_ad\_\_sfx\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 3211 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 3212 | request\_\_visitor | 6 |  |  |  |  | FALSE |
| 3213 | request\_\_network\_execution\_ctx\_\_inbound\_order\_type | 6 |  |  |  |  | FALSE |
| 3214 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_extended\_user\_ids\_\_type | 6 |  |  |  |  | FALSE |
| 3215 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 3216 | request\_\_context\_\_standard\_app\_id\_raw | 6 |  |  |  |  | FALSE |
| 3217 | request\_\_external\_candidate\_ad\_\_deal\_id | 6 |  |  |  |  | FALSE |
| 3218 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3219 | request\_\_context\_\_standard\_publisher\_id\_raw | 6 |  |  |  |  | FALSE |
| 3220 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_win\_lose | 6 |  |  |  |  | FALSE |
| 3221 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_priority | 6 |  |  |  |  | FALSE |
| 3222 | request\_\_advertisements\_\_content\_owner\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3223 | request\_\_rtb\_auction\_\_deal\_\_bid\_floor\_uplift | 6 |  |  |  |  | FALSE |
| 3224 | request\_\_outbound\_traffic\_control\_stats\_\_blocked\_num | 6 |  |  |  |  | FALSE |
| 3225 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 3226 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_value | 6 |  |  |  |  | FALSE |
| 3227 | request\_\_advertisements\_\_ad\_priority\_type | 6 |  |  |  |  | FALSE |
| 3228 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 3229 | request\_\_external\_candidate\_ad\_\_advertiser\_id\_raw | 6 |  |  |  |  | FALSE |
| 3230 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_model\_info | 6 |  |  |  |  | FALSE |
| 3231 | idx\_\_has\_slot | 6 |  |  |  |  | FALSE |
| 3232 | request\_\_advertisements\_\_targeting\_criteria\_id | 6 |  |  |  |  | FALSE |
| 3233 | request\_\_context\_\_site\_section\_cro\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3234 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3235 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_expense | 6 |  |  |  |  | FALSE |
| 3236 | acks\_\_metrics\_\_raw\_ad\_insertion | 6 |  |  |  |  | FALSE |
| 3237 | request\_\_slots\_\_resellers\_\_avails | 6 |  |  |  |  | FALSE |
| 3238 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 3239 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 3240 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3241 | request\_\_external\_candidate\_ad\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 3242 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 3243 | acks\_\_metrics\_\_ad\_resume | 6 |  |  |  |  | FALSE |
| 3244 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 3245 | uids\_\_slot\_uid | 6 |  |  |  |  | FALSE |
| 3246 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 3247 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3248 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3249 | request\_\_rtb\_auction\_\_bid\_to\_usd\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 3250 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3251 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 3252 | request\_\_context\_\_standard\_app\_bundle\_id\_raw | 6 |  |  |  |  | FALSE |
| 3253 | request\_\_slots\_\_opportunity\_id\_raw | 6 |  |  |  |  | FALSE |
| 3254 | request\_\_advertisements\_\_rules\_flags | 6 |  |  |  |  | FALSE |
| 3255 | request\_\_advertisements\_\_rules\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3256 | request\_\_context\_\_asset\_chain\_\_distributor\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3257 | request\_\_slots\_\_rules\_\_opp\_rule\_id | 6 |  |  |  |  | FALSE |
| 3258 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 3259 | request\_\_advertisements\_\_trimmed\_tracking\_domains\_\_domain\_id | 6 |  |  |  |  | FALSE |
| 3260 | request\_\_advertisements\_\_content\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3261 | request\_\_slots\_\_scheduled\_timestamp | 6 |  |  |  |  | FALSE |
| 3262 | request\_\_network\_execution\_ctx\_\_inventory\_\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3263 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3264 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_pretty\_id | 6 |  |  |  |  | FALSE |
| 3265 | request\_\_phantom\_candidate\_\_rendition\_id\_raw | 6 |  |  |  |  | FALSE |
| 3266 | aim\_info\_\_envelope\_info | 6 |  |  |  |  | FALSE |
| 3267 | request\_\_advertisements\_\_reseller\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3268 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_initial\_filled\_duration | 6 |  |  |  |  | FALSE |
| 3269 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3270 | request\_\_slots\_\_initial\_time\_unfilled | 6 |  |  |  |  | FALSE |
| 3271 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 6 |  |  |  |  | FALSE |
| 3272 | request\_\_rtb\_auction\_\_deal\_\_internal\_seat\_id | 6 |  |  |  |  | FALSE |
| 3273 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3274 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3275 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3276 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 3277 | request\_\_slots\_\_avails\_metrics\_\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 3278 | request\_\_rtb\_auction\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3279 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 3280 | request\_\_network\_attribute\_\_kv\_term\_id\_raw | 6 |  |  |  |  | FALSE |
| 3281 | request\_\_advertisements\_\_external\_reseller\_\_flags | 6 |  |  |  |  | FALSE |
| 3282 | acks\_\_psn\_msg\_\_distributor\_id | 6 |  |  |  |  | FALSE |
| 3283 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_scheduled\_impression\_committed | 6 |  |  |  |  | FALSE |
| 3284 | request\_\_slots\_\_resellers\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3285 | acks\_\_metrics\_\_raw\_ad\_pause | 6 |  |  |  |  | FALSE |
| 3286 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signal\_with\_waterfall\_\_type | 6 |  |  |  |  | FALSE |
| 3287 | request\_\_context\_\_site\_section\_chain | 6 |  |  |  |  | FALSE |
| 3288 | request\_\_slots\_\_resellers\_\_eligible\_carriage\_listing\_split\_unit\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3289 | forecast\_\_meta\_\_n\_preroll | 6 |  |  |  |  | FALSE |
| 3290 | request\_\_decision\_info\_\_candidates\_info\_\_osi | 6 |  |  |  |  | FALSE |
| 3291 | request\_\_advertisements\_\_content\_owner\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3292 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3293 | request\_\_inventory\_group\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3294 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 3295 | request\_\_advertisements\_\_distributor\_\_context\_id | 6 |  |  |  |  | FALSE |
| 3296 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3297 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 3298 | request\_\_advertisements\_\_external\_reseller\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3299 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3300 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3301 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3302 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3303 | request\_\_errors\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 3304 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3305 | request\_\_external\_candidate\_ad\_\_trading\_desk\_id\_raw | 6 |  |  |  |  | FALSE |
| 3306 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 3307 | candidate\_\_price | 6 |  |  |  |  | FALSE |
| 3308 | request\_\_advertisements\_\_shading\_context\_\_shading\_model\_version | 6 |  |  |  |  | FALSE |
| 3309 | request\_\_slots\_\_resellers\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3310 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3311 | request\_\_context\_\_asset\_chain\_\_inventory\_context\_\_network\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3312 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 3313 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 3314 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 3315 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 3316 | request\_\_advertisements\_\_content\_right\_owner\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 3317 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 3318 | request\_\_network\_attribute\_\_custom\_platform\_ids | 6 |  |  |  |  | FALSE |
| 3319 | request\_\_advertisements\_\_billable\_rate\_denominator\_event\_id | 6 |  |  |  |  | FALSE |
| 3320 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3321 | request\_\_slots\_\_resellers\_\_marketplace\_audience\_extension\_deal\_ids | 6 |  |  |  |  | FALSE |
| 3322 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3323 | request\_\_slots\_\_resellers\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3324 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3325 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_unified\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3326 | request\_\_network\_execution\_ctx\_\_inventory\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3327 | request\_\_slots\_\_avails\_metrics | 6 |  |  |  |  | FALSE |
| 3328 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 3329 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3330 | request\_\_auction\_network\_contexts\_\_application\_type | 6 |  |  |  |  | FALSE |
| 3331 | request\_\_external\_candidate\_ad\_\_rtb\_auction\_index | 6 |  |  |  |  | FALSE |
| 3332 | request\_\_external\_candidate\_ad\_\_market\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3333 | request\_\_advertisements\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3334 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs | 6 |  |  |  |  | FALSE |
| 3335 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key | 6 |  |  |  |  | FALSE |
| 3336 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 3337 | request\_\_external\_candidate\_ad\_\_bid\_replica\_id | 6 |  |  |  |  | FALSE |
| 3338 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 3339 | request\_\_slots\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 6 |  |  |  |  | FALSE |
| 3340 | request\_\_slots\_\_content\_right\_owner | 6 |  |  |  |  | FALSE |
| 3341 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 3342 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3343 | request\_\_advertisements\_\_rendition\_id | 6 |  |  |  |  | FALSE |
| 3344 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 3345 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_booked\_impression | 6 |  |  |  |  | FALSE |
| 3346 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 3347 | request\_\_slots\_\_resellers\_\_sfx\_avails | 6 |  |  |  |  | FALSE |
| 3348 | request\_\_advertisements\_\_external\_reseller\_\_bidding\_up\_original\_revenue | 6 |  |  |  |  | FALSE |
| 3349 | forecast\_\_server\_id | 6 |  |  |  |  | FALSE |
| 3350 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3351 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_unified\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3352 | acks\_\_yield\_optimization\_ids | 6 |  |  |  |  | FALSE |
| 3353 | request\_\_decision\_info\_\_candidates\_info\_\_supply\_source\_type | 6 |  |  |  |  | FALSE |
| 3354 | forecast\_\_metrics | 6 |  |  |  |  | FALSE |
| 3355 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 3356 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3357 | auction\_\_bid\_to\_usd\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 3358 | acks\_\_metrics\_\_third\_quartile | 6 |  |  |  |  | FALSE |
| 3359 | request\_\_rtb\_auction\_\_media\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 3360 | request\_\_slots\_\_forecast\_avails\_metrics\_\_total\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 3361 | request\_\_bidding\_context\_\_bid\_request\_\_supply\_chain\_\_nodes\_\_asi | 6 |  |  |  |  | FALSE |
| 3362 | request\_\_decision\_info\_\_candidates\_info\_\_priority | 6 |  |  |  |  | FALSE |
| 3363 | request\_\_slots\_\_market\_avails | 6 |  |  |  |  | FALSE |
| 3364 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 3365 | acks\_\_deprecate\_\_error | 6 |  |  |  |  | FALSE |
| 3366 | request\_\_external\_candidate\_ad\_\_response\_time | 6 |  |  |  |  | FALSE |
| 3367 | request\_\_external\_candidate\_ad\_\_rtb\_impression\_slot\_index | 6 |  |  |  |  | FALSE |
| 3368 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_id | 6 |  |  |  |  | FALSE |
| 3369 | request\_\_outbound\_traffic\_control\_stats\_\_auction\_network\_id | 6 |  |  |  |  | FALSE |
| 3370 | request\_\_advertisements\_\_distributor\_\_down\_network\_id | 6 |  |  |  |  | FALSE |
| 3371 | request\_\_advertisements\_\_reseller\_\_rule\_flags | 6 |  |  |  |  | FALSE |
| 3372 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3373 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3374 | request\_\_slots\_\_resellers\_\_avails\_metrics\_\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 3375 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3376 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3377 | forecast\_\_meta\_\_flag | 6 |  |  |  |  | FALSE |
| 3378 | request\_\_slots\_\_standard\_ad\_unit\_sequence | 6 |  |  |  |  | FALSE |
| 3379 | request\_\_rtb\_auction\_\_impression\_\_index | 6 |  |  |  |  | FALSE |
| 3380 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3381 | forecast\_\_metrics\_\_portfolio\_map\_\_value | 6 |  |  |  |  | FALSE |
| 3382 | request\_\_slots\_\_resellers\_\_carriage\_inventory\_owner\_id | 6 |  |  |  |  | FALSE |
| 3383 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_associated\_impression | 6 |  |  |  |  | FALSE |
| 3384 | request\_\_network\_execution\_ctx\_\_inventory\_\_mapped\_asset\_ids | 6 |  |  |  |  | FALSE |
| 3385 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3386 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 3387 | request\_\_network\_execution\_ctx\_\_upstream\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3388 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_extended\_user\_ids\_\_id | 6 |  |  |  |  | FALSE |
| 3389 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_extended\_user\_ids\_\_authorized\_networks | 6 |  |  |  |  | FALSE |
| 3390 | acks\_\_psn\_msg\_\_plc\_start\_time | 6 |  |  |  |  | FALSE |
| 3391 | request\_\_advertisements\_\_content\_owner\_\_supply\_acquisition\_cost | 6 |  |  |  |  | FALSE |
| 3392 | deprecate\_\_video\_view | 6 |  |  |  |  | FALSE |
| 3393 | request\_\_external\_candidate\_ad\_\_ortb\_fwpartners | 6 |  |  |  |  | FALSE |
| 3394 | request\_\_advertisements\_\_distributor\_\_down\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3395 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 3396 | acks\_\_creative\_rendition\_id | 6 |  |  |  |  | FALSE |
| 3397 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3398 | acks\_\_psn\_msg\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3399 | request\_\_errors\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3400 | request\_\_slots\_\_window\_start\_timestamp | 6 |  |  |  |  | FALSE |
| 3401 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_ids | 6 |  |  |  |  | FALSE |
| 3402 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3403 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 3404 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 3405 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3406 | request\_\_external\_candidate\_ad\_\_bsi\_id | 6 |  |  |  |  | FALSE |
| 3407 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 3408 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3409 | request\_\_advertisements\_\_yield\_optimization\_effective\_term\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3410 | request\_\_slots\_\_carriage\_listing\_split\_unit\_id | 6 |  |  |  |  | FALSE |
| 3411 | acks\_\_psn\_msg\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 3412 | request\_\_advertisements\_\_content\_right\_owner\_\_unified\_rule\_priority | 6 |  |  |  |  | FALSE |
| 3413 | request\_\_advertisements\_\_distributor\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3414 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 3415 | acks\_\_metrics\_\_measurable\_ad\_mute\_unmute\_impression | 6 |  |  |  |  | FALSE |
| 3416 | partners\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 6 |  |  |  |  | FALSE |
| 3417 | uids\_\_advertisement\_uid | 6 |  |  |  |  | FALSE |
| 3418 | request\_\_advertisements\_\_ad\_view\_ratio\_type | 6 |  |  |  |  | FALSE |
| 3419 | auction\_\_impression | 6 |  |  |  |  | FALSE |
| 3420 | request\_\_advertisements\_\_unified\_yield\_\_replaced\_guaranteed\_ad\_id | 6 |  |  |  |  | FALSE |
| 3421 | request\_\_advertisements\_\_reseller\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3422 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics | 6 |  |  |  |  | FALSE |
| 3423 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 3424 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3425 | request\_\_advertisements\_\_io\_id\_raw | 6 |  |  |  |  | FALSE |
| 3426 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_effective\_exclude\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 3427 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 3428 | acks\_\_deprecate | 6 |  |  |  |  | FALSE |
| 3429 | request\_\_advertisements\_\_external\_reseller\_\_supply\_acquisition\_cost | 6 |  |  |  |  | FALSE |
| 3430 | acks\_\_server\_side\_tracking\_url | 6 |  |  |  |  | FALSE |
| 3431 | request\_\_bidding\_context\_\_bid\_request\_\_impression\_\_floor | 6 |  |  |  |  | FALSE |
| 3432 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_gross\_avail | 6 |  |  |  |  | FALSE |
| 3433 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3434 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_order\_id | 6 |  |  |  |  | FALSE |
| 3435 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3436 | acks\_\_metrics\_\_raw\_bid\_won\_margin | 6 |  |  |  |  | FALSE |
| 3437 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_expense | 6 |  |  |  |  | FALSE |
| 3438 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3439 | request\_\_advertisements\_\_external\_reseller\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3440 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 3441 | request\_\_context\_\_distributor\_video\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3442 | request\_\_advertisements\_\_replaced\_creative\_id\_raw | 6 |  |  |  |  | FALSE |
| 3443 | request\_\_errors\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3444 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 3445 | acks\_\_deprecate\_\_ad\_impression | 6 |  |  |  |  | FALSE |
| 3446 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3447 | request\_\_advertisements\_\_content\_right\_owner | 6 |  |  |  |  | FALSE |
| 3448 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3449 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 3450 | request\_\_slots\_\_resellers\_\_selection\_info | 6 |  |  |  |  | FALSE |
| 3451 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map | 6 |  |  |  |  | FALSE |
| 3452 | request\_\_visitor\_\_referrer\_banning\_rule\_id | 6 |  |  |  |  | FALSE |
| 3453 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 3454 | request\_\_slots\_\_first\_exchange\_buyer\_indexes | 6 |  |  |  |  | FALSE |
| 3455 | request\_\_phantom\_candidate\_\_creative\_id\_raw | 6 |  |  |  |  | FALSE |
| 3456 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_max\_cpm | 6 |  |  |  |  | FALSE |
| 3457 | request\_\_slots\_\_carriage\_listing\_split\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 3458 | request\_\_advertisements\_\_distributor\_\_unified\_rule\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 3459 | forecast\_\_metrics\_\_transactional\_map\_\_value | 6 |  |  |  |  | FALSE |
| 3460 | partners\_\_eligible\_outbound\_orders\_\_exchange\_order\_id | 6 |  |  |  |  | FALSE |
| 3461 | aim\_info\_\_envelope\_info\_\_envelope\_identifiers | 6 |  |  |  |  | FALSE |
| 3462 | ack\_\_is\_slot\_impression | 6 |  |  |  |  | FALSE |
| 3463 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 3464 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3465 | request\_\_advertisements\_\_distributor\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3466 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 3467 | forecast\_\_meta\_\_uid | 6 |  |  |  |  | FALSE |
| 3468 | acks\_\_deprecate\_\_video\_view | 6 |  |  |  |  | FALSE |
| 3469 | request\_\_advertisements\_\_reseller\_\_margin | 6 |  |  |  |  | FALSE |
| 3470 | request\_\_advertisements\_\_external\_reseller\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 3471 | request\_\_advertisements\_\_distributor\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 3472 | request\_\_visitor\_\_accept\_language | 6 |  |  |  |  | FALSE |
| 3473 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3474 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_net\_avail | 6 |  |  |  |  | FALSE |
| 3475 | request\_\_external\_candidate\_ad\_\_external\_ad\_id | 6 |  |  |  |  | FALSE |
| 3476 | request\_\_context\_\_standard\_site\_domain\_id\_raw | 6 |  |  |  |  | FALSE |
| 3477 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 3478 | acks\_\_metrics\_\_ad\_collapse | 6 |  |  |  |  | FALSE |
| 3479 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3480 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3481 | request\_\_slots\_\_resellers | 6 |  |  |  |  | FALSE |
| 3482 | acks\_\_event\_provider | 6 |  |  |  |  | FALSE |
| 3483 | request\_\_external\_candidate\_ad\_\_dsp\_adid | 6 |  |  |  |  | FALSE |
| 3484 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 3485 | request\_\_advertisements\_\_distributor\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3486 | acks\_\_custom\_ad\_id | 6 |  |  |  |  | FALSE |
| 3487 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_price | 6 |  |  |  |  | FALSE |
| 3488 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 3489 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 3490 | request\_\_network\_attribute\_\_id\_graph\_\_policy\_\_policy\_id | 6 |  |  |  |  | FALSE |
| 3491 | acks\_\_deprecate\_\_c3\_demographic\_impression | 6 |  |  |  |  | FALSE |
| 3492 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_guaranteed | 6 |  |  |  |  | FALSE |
| 3493 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 3494 | request\_\_external\_candidate\_ad\_\_candidate\_network\_to\_auction\_network\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 3495 | forecast\_\_meta\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 3496 | request\_\_advertisements\_\_inbound\_rule | 6 |  |  |  |  | FALSE |
| 3497 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 3498 | request\_\_context\_\_distributor\_video\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3499 | request\_\_rtb\_auction\_\_deal\_\_internal\_group\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 3500 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 3501 | request\_\_advertisements\_\_external\_reseller\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3502 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 3503 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3504 | request\_\_advertisements\_\_content\_right\_owner\_\_marketplace\_audience\_extension\_deal\_id | 6 |  |  |  |  | FALSE |
| 3505 | request\_\_advertisements\_\_distributor\_\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3506 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 3507 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 3508 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3509 | request\_\_network\_attribute\_\_nielsen\_win\_section\_id | 6 |  |  |  |  | FALSE |
| 3510 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 3511 | acks\_\_capabilities | 6 |  |  |  |  | FALSE |
| 3512 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signal\_with\_waterfall\_\_id | 6 |  |  |  |  | FALSE |
| 3513 | request\_\_advertisements\_\_content\_owner\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3514 | request\_\_rtb\_auction\_\_deal\_\_trading\_desk\_id | 6 |  |  |  |  | FALSE |
| 3515 | request\_\_auction\_network\_contexts\_\_auction\_network\_id | 6 |  |  |  |  | FALSE |
| 3516 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3517 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3518 | request\_\_slots\_\_resellers\_\_eligible\_carriage\_listing\_split\_unit\_ids | 6 |  |  |  |  | FALSE |
| 3519 | request\_\_advertisements\_\_external\_reseller\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3520 | request\_\_advertisements\_\_content\_owner\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3521 | acks\_\_metrics\_\_video\_view | 6 |  |  |  |  | FALSE |
| 3522 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 3523 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_revenue | 6 |  |  |  |  | FALSE |
| 3524 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3525 | acks\_\_callback\_info | 6 |  |  |  |  | FALSE |
| 3526 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_is\_guaranteed | 6 |  |  |  |  | FALSE |
| 3527 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3528 | acks\_\_metrics\_\_raw\_measurable\_ad\_pause\_resume\_impression | 6 |  |  |  |  | FALSE |
| 3529 | request\_\_network\_attribute\_\_portfolio\_ids | 6 |  |  |  |  | FALSE |
| 3530 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3531 | request\_\_slots\_\_outbound\_order\_\_effective\_exclude\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 3532 | request\_\_context\_\_standard\_content\_credential\_status\_id\_raw | 6 |  |  |  |  | FALSE |
| 3533 | request\_\_advertisements\_\_reseller\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 3534 | request\_\_advertisements\_\_reseller\_\_ssp\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 3535 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3536 | request\_\_advertisements\_\_reseller\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3537 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 6 |  |  |  |  | FALSE |
| 3538 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 3539 | request\_\_bidding\_context\_\_bid\_request\_\_impression\_\_private\_auction | 6 |  |  |  |  | FALSE |
| 3540 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3541 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3542 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_down\_reseller\_index | 6 |  |  |  |  | FALSE |
| 3543 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 3544 | request\_\_external\_candidate\_ad\_\_buyer\_id | 6 |  |  |  |  | FALSE |
| 3545 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 3546 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3547 | request\_\_network\_execution\_ctx\_\_inventory\_\_mapped\_asset\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3548 | request\_\_external\_candidate\_ad\_\_ortb\_fwpartners\_\_idvalue | 6 |  |  |  |  | FALSE |
| 3549 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 3550 | request\_\_network\_execution\_ctx\_\_inventory\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 3551 | request\_\_advertisements\_\_data\_provider\_id\_raw | 6 |  |  |  |  | FALSE |
| 3552 | request\_\_advertisements\_\_network\_\_content\_owner\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3553 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 3554 | request\_\_slots\_\_ad\_unit\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3555 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 3556 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 3557 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_id | 6 |  |  |  |  | FALSE |
| 3558 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_total\_capacity | 6 |  |  |  |  | FALSE |
| 3559 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3560 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 3561 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 3562 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3563 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3564 | request\_\_auction\_network\_contexts | 6 |  |  |  |  | FALSE |
| 3565 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_auction\_type | 6 |  |  |  |  | FALSE |
| 3566 | request\_\_slots\_\_outbound\_order\_\_unified\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3567 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 3568 | request\_\_bidding\_context\_\_bid\_request\_\_network | 6 |  |  |  |  | FALSE |
| 3569 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 3570 | request\_\_advertisements\_\_content\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3571 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 3572 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3573 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3574 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3575 | request\_\_advertisements\_\_content\_owner\_\_competition\_resellers | 6 |  |  |  |  | FALSE |
| 3576 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 3577 | request\_\_advertisements\_\_content\_right\_owner\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3578 | request\_\_slots\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id\_raw | 6 |  |  |  |  | FALSE |
| 3579 | request\_\_slots\_\_pod\_sequence | 6 |  |  |  |  | FALSE |
| 3580 | request\_\_external\_candidate\_ad\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3581 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3582 | forecast\_\_metrics\_\_portfolio\_map\_\_key | 6 |  |  |  |  | FALSE |
| 3583 | request\_\_advertisements\_\_shading\_context\_\_shaded\_price\_usd | 6 |  |  |  |  | FALSE |
| 3584 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 3585 | request\_\_slots\_\_original\_ad\_unit | 6 |  |  |  |  | FALSE |
| 3586 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 3587 | request\_\_advertisements\_\_distributor\_\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 3588 | request\_\_advertisements\_\_content\_owner\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 3589 | request\_\_advertisements\_\_content\_right\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3590 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value | 6 |  |  |  |  | FALSE |
| 3591 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 3592 | request\_\_advertisements\_\_content\_owner\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 3593 | request\_\_model\_framework\_\_network\_model\_contexts\_\_realtime\_features | 6 |  |  |  |  | FALSE |
| 3594 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 3595 | request\_\_external\_candidate\_ad\_\_price\_type | 6 |  |  |  |  | FALSE |
| 3596 | acks\_\_deprecate\_\_slot\_avails | 6 |  |  |  |  | FALSE |
| 3597 | request\_\_slots\_\_rules\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3598 | request\_\_advertisements\_\_content\_right\_owner\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 3599 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 3600 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3601 | request\_\_rtb\_auction\_\_app\_bundle | 6 |  |  |  |  | FALSE |
| 3602 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 3603 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3604 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 3605 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 3606 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3607 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 3608 | acks\_\_psn\_msg\_\_session\_start\_time | 6 |  |  |  |  | FALSE |
| 3609 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 3610 | request\_\_rtb\_auction\_\_deal\_\_matched\_inventory\_package\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3611 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_active\_term\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3612 | acks\_\_cpx\_concrete\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 3613 | forecast\_\_metrics\_\_transactional\_map\_\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 3614 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_error | 6 |  |  |  |  | FALSE |
| 3615 | request\_\_advertisements\_\_content\_right\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3616 | request\_\_advertisements\_\_content\_owner\_\_unified\_rule\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3617 | request\_\_slots\_\_forecast\_avails\_metrics | 6 |  |  |  |  | FALSE |
| 3618 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3619 | request\_\_advertisements\_\_distributor\_\_unified\_rule\_priority | 6 |  |  |  |  | FALSE |
| 3620 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 3621 | request\_\_slots\_\_resellers\_\_forecast\_avails\_metrics\_\_remaining\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 3622 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3623 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_context\_id | 6 |  |  |  |  | FALSE |
| 3624 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3625 | request\_\_rtb\_auction\_\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3626 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_lose\_win | 6 |  |  |  |  | FALSE |
| 3627 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 3628 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 3629 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3630 | request\_\_advertisements\_\_cch\_key\_domain\_config\_id | 6 |  |  |  |  | FALSE |
| 3631 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 3632 | request\_\_external\_candidate\_ad\_\_universal\_ad\_id | 6 |  |  |  |  | FALSE |
| 3633 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3634 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 3635 | acks\_\_metrics\_\_slot\_impression | 6 |  |  |  |  | FALSE |
| 3636 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3637 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 3638 | acks\_\_metrics\_\_raw\_complete\_quartile | 6 |  |  |  |  | FALSE |
| 3639 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 3640 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3641 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3642 | request\_\_advertisements\_\_ad\_cro\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3643 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_displacing | 6 |  |  |  |  | FALSE |
| 3644 | acks\_\_keys\_\_is\_firstcall | 6 |  |  |  |  | FALSE |
| 3645 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3646 | request\_\_auction\_network\_contexts\_\_app\_bundle | 6 |  |  |  |  | FALSE |
| 3647 | request\_\_advertisements\_\_triggering\_concrete\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 3648 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3649 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 3650 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3651 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3652 | request\_\_context\_\_video\_cro\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3653 | request\_\_network\_data\_visibility\_config\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3654 | acks\_\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 3655 | request\_\_context\_\_website\_root\_id\_raw | 6 |  |  |  |  | FALSE |
| 3656 | acks\_\_yield\_optimization\_ids\_\_demand\_id\_raw | 6 |  |  |  |  | FALSE |
| 3657 | request\_\_advertisements\_\_distributor\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3658 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_unconstraint\_gross\_avail | 6 |  |  |  |  | FALSE |
| 3659 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3660 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3661 | request\_\_network\_execution\_ctx\_\_data\_right\_\_type | 6 |  |  |  |  | FALSE |
| 3662 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3663 | request\_\_geo\_data\_provider\_id\_raw | 6 |  |  |  |  | FALSE |
| 3664 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_active\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 3665 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3666 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3667 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 6 |  |  |  |  | FALSE |
| 3668 | request\_\_errors\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3669 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3670 | request\_\_slots\_\_resellers\_\_forecast\_avails\_metrics\_\_booked\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 3671 | request\_\_external\_bridge\_records\_\_http\_status\_code | 6 |  |  |  |  | FALSE |
| 3672 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 6 |  |  |  |  | FALSE |
| 3673 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3674 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 3675 | aim\_info\_\_aim\_identity\_info | 6 |  |  |  |  | FALSE |
| 3676 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 3677 | request\_\_advertisements\_\_external\_reseller\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 3678 | request\_\_advertisements\_\_advertiser\_id | 6 |  |  |  |  | FALSE |
| 3679 | request\_\_advertisements\_\_reseller\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3680 | request\_\_advertisements\_\_ecpm | 6 |  |  |  |  | FALSE |
| 3681 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics | 6 |  |  |  |  | FALSE |
| 3682 | request\_\_advertisements\_\_ad\_reseller\_network\_list | 6 |  |  |  |  | FALSE |
| 3683 | request\_\_advertisements\_\_external\_reseller\_\_unified\_rule\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3684 | acks\_\_metrics\_\_middle\_quartile | 6 |  |  |  |  | FALSE |
| 3685 | request\_\_advertisements\_\_distributor\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 3686 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3687 | request\_\_advertisements\_\_abstract\_event\_id | 6 |  |  |  |  | FALSE |
| 3688 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 3689 | request\_\_advertisements\_\_contextual\_billings | 6 |  |  |  |  | FALSE |
| 3690 | request\_\_network\_attribute\_\_id\_graph\_\_policy\_\_alias\_\_type | 6 |  |  |  |  | FALSE |
| 3691 | request\_\_advertisements\_\_market\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3692 | acks\_\_kafka\_msg\_key | 6 |  |  |  |  | FALSE |
| 3693 | aim\_info\_\_aim\_audience\_info\_\_graph\_usage\_index | 6 |  |  |  |  | FALSE |
| 3694 | acks\_\_yield\_optimization\_ids\_\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3695 | request\_\_mpe\_matcher\_filters\_\_bucket\_id\_raw | 6 |  |  |  |  | FALSE |
| 3696 | request\_\_rtb\_auction\_\_deal\_\_media\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 3697 | request\_\_advertisements\_\_insertion\_order\_id | 6 |  |  |  |  | FALSE |
| 3698 | request\_\_advertisements\_\_fill\_rate | 6 |  |  |  |  | FALSE |
| 3699 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3700 | request\_\_advertisements\_\_reseller\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3701 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3702 | request\_\_advertisements\_\_external\_reseller\_\_revenue | 6 |  |  |  |  | FALSE |
| 3703 | request\_\_advertisements\_\_network\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3704 | request\_\_advertisements\_\_reseller\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3705 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_unified\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 3706 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3707 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3708 | request\_\_advertisements\_\_reseller\_\_bidding\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3709 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3710 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3711 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 3712 | request\_\_global\_currency\_\_currencies\_\_currency\_id\_raw | 6 |  |  |  |  | FALSE |
| 3713 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics | 6 |  |  |  |  | FALSE |
| 3714 | request\_\_rtb\_auction\_\_site\_domain | 6 |  |  |  |  | FALSE |
| 3715 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 3716 | request\_\_advertisements\_\_reseller\_\_rule\_ext\_id\_raw | 6 |  |  |  |  | FALSE |
| 3717 | request\_\_advertisements\_\_external\_reseller\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3718 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3719 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 3720 | request\_\_external\_candidate\_ad\_\_response\_time\_first\_hop | 6 |  |  |  |  | FALSE |
| 3721 | request\_\_advertisements\_\_global\_advertiser\_ids | 6 |  |  |  |  | FALSE |
| 3722 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 3723 | request\_\_errors\_\_bsi\_id | 6 |  |  |  |  | FALSE |
| 3724 | request\_\_context\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 3725 | acks\_\_metrics\_\_bid\_won\_margin | 6 |  |  |  |  | FALSE |
| 3726 | request\_\_slots\_\_outbound\_order\_\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3727 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 3728 | request\_\_external\_candidate\_ad\_\_clock\_number | 6 |  |  |  |  | FALSE |
| 3729 | request\_\_slots\_\_resellers\_\_flags | 6 |  |  |  |  | FALSE |
| 3730 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 3731 | request\_\_advertisements\_\_active\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 3732 | request\_\_rtb\_auction\_\_bid\_to\_eur\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 3733 | request\_\_advertisements\_\_effective\_unified\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 3734 | request\_\_bidding\_context\_\_bid\_request\_\_publisher\_\_name | 6 |  |  |  |  | FALSE |
| 3735 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 3736 | request\_\_visitor\_\_user\_group | 6 |  |  |  |  | FALSE |
| 3737 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_channel\_id | 6 |  |  |  |  | FALSE |
| 3738 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3739 | request\_\_network\_execution\_ctx\_\_inbound\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3740 | forecast\_\_metrics\_\_transactional\_map\_\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3741 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 3742 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 3743 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3744 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 3745 | acks\_\_deprecate\_\_creative\_id | 6 |  |  |  |  | FALSE |
| 3746 | request\_\_advertisements\_\_external\_reseller\_\_rule\_ext\_id\_raw | 6 |  |  |  |  | FALSE |
| 3747 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 3748 | request\_\_rtb\_auction\_\_impression\_\_error | 6 |  |  |  |  | FALSE |
| 3749 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 3750 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 3751 | request\_\_rtb\_auction\_\_site\_section\_id | 6 |  |  |  |  | FALSE |
| 3752 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3753 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 3754 | request\_\_advertisements\_\_content\_owner\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 3755 | request\_\_advertisements\_\_inbound\_rule\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3756 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3757 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3758 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_scenario\_id | 6 |  |  |  |  | FALSE |
| 3759 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 3760 | request\_\_advertisements\_\_agency\_id | 6 |  |  |  |  | FALSE |
| 3761 | auction\_\_execution\_node\_id | 6 |  |  |  |  | FALSE |
| 3762 | request\_\_advertisements\_\_reseller\_\_up\_revenue\_as\_content\_owner | 6 |  |  |  |  | FALSE |
| 3763 | request\_\_context\_\_site\_section\_chain\_\_content\_owner | 6 |  |  |  |  | FALSE |
| 3764 | request\_\_advertisements\_\_distributor\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3765 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_iids\_\_type | 6 |  |  |  |  | FALSE |
| 3766 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3767 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3768 | request\_\_advertisements\_\_validation\_event | 6 |  |  |  |  | FALSE |
| 3769 | request\_\_visitor\_\_user\_agent\_device\_id\_raw | 6 |  |  |  |  | FALSE |
| 3770 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 3771 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_flags | 6 |  |  |  |  | FALSE |
| 3772 | request\_\_advertisements\_\_deprecate\_\_implicit\_ad\_impression | 6 |  |  |  |  | FALSE |
| 3773 | request\_\_errors\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3774 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key | 6 |  |  |  |  | FALSE |
| 3775 | request\_\_advertisements\_\_content\_right\_owner\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3776 | request\_\_slots\_\_ad\_unit\_network\_id | 6 |  |  |  |  | FALSE |
| 3777 | request\_\_slots\_\_resellers\_\_inbound\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3778 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_order\_transaction\_type | 6 |  |  |  |  | FALSE |
| 3779 | acks\_\_metrics\_\_first\_quartile | 6 |  |  |  |  | FALSE |
| 3780 | request\_\_slots\_\_min\_bitrate | 6 |  |  |  |  | FALSE |
| 3781 | request\_\_advertisements\_\_deprecate\_\_gross\_rating\_point | 6 |  |  |  |  | FALSE |
| 3782 | forecast\_\_metrics\_\_transactional\_demo\_map | 6 |  |  |  |  | FALSE |
| 3783 | request\_\_bidding\_context\_\_bid\_request\_\_channel\_\_name | 6 |  |  |  |  | FALSE |
| 3784 | acks\_\_psn\_msg\_\_terminal\_addr | 6 |  |  |  |  | FALSE |
| 3785 | request\_\_yield\_optimization\_ids\_\_demand\_id\_raw | 6 |  |  |  |  | FALSE |
| 3786 | request\_\_slots\_\_break\_display\_id\_raw | 6 |  |  |  |  | FALSE |
| 3787 | request\_\_slots\_\_resellers\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 3788 | request\_\_advertisements\_\_distributor\_\_marketplace\_audience\_extension\_deal\_id | 6 |  |  |  |  | FALSE |
| 3789 | request\_\_advertisements\_\_network | 6 |  |  |  |  | FALSE |
| 3790 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3791 | request\_\_context\_\_asset\_chain\_\_distributor\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 3792 | request\_\_advertisements\_\_reseller\_\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3793 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 3794 | acks\_\_metrics\_\_measurable\_ad\_pause\_resume\_impression | 6 |  |  |  |  | FALSE |
| 3795 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_pretty\_id\_raw | 6 |  |  |  |  | FALSE |
| 3796 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3797 | request\_\_advertisements\_\_external\_reseller\_\_series\_id | 6 |  |  |  |  | FALSE |
| 3798 | request\_\_advertisements\_\_content\_right\_owner\_\_competition\_resellers | 6 |  |  |  |  | FALSE |
| 3799 | request\_\_external\_bridge\_records\_\_duration | 6 |  |  |  |  | FALSE |
| 3800 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_id | 6 |  |  |  |  | FALSE |
| 3801 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3802 | request\_\_external\_candidate\_ad\_\_internal\_seat\_id\_raw | 6 |  |  |  |  | FALSE |
| 3803 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 3804 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 3805 | acks\_\_deprecate\_\_complete | 6 |  |  |  |  | FALSE |
| 3806 | request\_\_advertisements\_\_external\_reseller\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 3807 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 3808 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3809 | request\_\_bidding\_context\_\_bid\_request\_\_domain | 6 |  |  |  |  | FALSE |
| 3810 | request\_\_context\_\_video\_cro\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3811 | request\_\_advertisements\_\_deprecate\_\_error | 6 |  |  |  |  | FALSE |
| 3812 | request\_\_rtb\_auction\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3813 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 3814 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 3815 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 3816 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_segments\_\_cpm | 6 |  |  |  |  | FALSE |
| 3817 | aim\_info\_\_aim\_audience\_info\_\_segments\_\_cpm | 6 |  |  |  |  | FALSE |
| 3818 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3819 | request\_\_advertisements\_\_unified\_priority | 6 |  |  |  |  | FALSE |
| 3820 | acks\_\_keys\_\_is\_zero\_won\_revenue | 6 |  |  |  |  | FALSE |
| 3821 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3822 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3823 | idx\_\_has\_external\_candidate | 6 |  |  |  |  | FALSE |
| 3824 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3825 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3826 | acks\_\_deprecate\_\_ad\_insertion | 6 |  |  |  |  | FALSE |
| 3827 | request\_\_visitor\_\_standard\_retailer\_id | 6 |  |  |  |  | FALSE |
| 3828 | request\_\_slots\_\_profile\_id\_raw | 6 |  |  |  |  | FALSE |
| 3829 | request\_\_slots\_\_resellers\_\_marketplace\_execution\_id\_raw | 6 |  |  |  |  | FALSE |
| 3830 | request\_\_external\_candidate\_ad\_\_sfx\_dsp\_id\_raw | 6 |  |  |  |  | FALSE |
| 3831 | acks\_\_scte\_message\_id | 6 |  |  |  |  | FALSE |
| 3832 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3833 | request\_\_slots\_\_resellers\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3834 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 3835 | request\_\_external\_candidate\_ad\_\_global\_industry\_ids\_raw | 6 |  |  |  |  | FALSE |
| 3836 | acks\_\_creative\_rendition\_id\_raw | 6 |  |  |  |  | FALSE |
| 3837 | request\_\_context\_\_video\_cro\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3838 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 3839 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3840 | request\_\_slots\_\_resellers\_\_site\_id | 6 |  |  |  |  | FALSE |
| 3841 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3842 | acks\_\_concrete\_event\_provider\_id | 6 |  |  |  |  | FALSE |
| 3843 | request\_\_slots\_\_resellers\_\_first\_exchange\_buyer\_indexes | 6 |  |  |  |  | FALSE |
| 3844 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 3845 | forecast\_\_scenario | 6 |  |  |  |  | FALSE |
| 3846 | request\_\_visitor\_\_postal\_code\_package\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3847 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 3848 | request\_\_context\_\_header\_bidding | 6 |  |  |  |  | FALSE |
| 3849 | aim\_info\_\_aim\_identity\_info\_\_metadata\_version | 6 |  |  |  |  | FALSE |
| 3850 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3851 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 3852 | acks\_\_metrics\_\_raw\_ad\_bid\_won | 6 |  |  |  |  | FALSE |
| 3853 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 3854 | request\_\_advertisements\_\_global\_brand\_id\_raw | 6 |  |  |  |  | FALSE |
| 3855 | forecast\_\_metrics\_\_portfolio\_map | 6 |  |  |  |  | FALSE |
| 3856 | request\_\_rtb\_auction\_\_ifa\_type | 6 |  |  |  |  | FALSE |
| 3857 | request\_\_advertisements\_\_validation\_event\_\_concrete\_event\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3858 | request\_\_external\_candidate\_ad\_\_brand\_id | 6 |  |  |  |  | FALSE |
| 3859 | request\_\_advertisements\_\_effective\_unified\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 3860 | request\_\_advertisements\_\_distributor\_\_bidding\_down\_revenue | 6 |  |  |  |  | FALSE |
| 3861 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_flags | 6 |  |  |  |  | FALSE |
| 3862 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 3863 | request\_\_advertisements\_\_distributor\_\_supply\_distribution\_cost | 6 |  |  |  |  | FALSE |
| 3864 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value | 6 |  |  |  |  | FALSE |
| 3865 | request\_\_context\_\_asset\_chain\_\_distributor\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 3866 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_order\_type | 6 |  |  |  |  | FALSE |
| 3867 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3868 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 3869 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 3870 | request\_\_rtb\_auction\_\_deal\_\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 3871 | request\_\_slots\_\_break\_id | 6 |  |  |  |  | FALSE |
| 3872 | request\_\_advertisements\_\_reseller\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 3873 | request\_\_external\_candidate\_ad\_\_flags | 6 |  |  |  |  | FALSE |
| 3874 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_wseat | 6 |  |  |  |  | FALSE |
| 3875 | request\_\_slots\_\_resellers\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 3876 | request\_\_advertisements\_\_content\_owner\_\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3877 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3878 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3879 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 3880 | request\_\_rtb\_auction\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3881 | request\_\_advertisements\_\_reseller\_\_flags | 6 |  |  |  |  | FALSE |
| 3882 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key | 6 |  |  |  |  | FALSE |
| 3883 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3884 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_key | 6 |  |  |  |  | FALSE |
| 3885 | request\_\_slots\_\_raw\_max\_duration | 6 |  |  |  |  | FALSE |
| 3886 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 3887 | acks\_\_metrics\_\_raw\_slot\_avails | 6 |  |  |  |  | FALSE |
| 3888 | request\_\_rtb\_auction\_\_app\_storeurl | 6 |  |  |  |  | FALSE |
| 3889 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 3890 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3891 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3892 | request\_\_inventory\_group\_\_inventory\_id\_raw | 6 |  |  |  |  | FALSE |
| 3893 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_audience\_partner\_id\_raw | 6 |  |  |  |  | FALSE |
| 3894 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver\_committed | 6 |  |  |  |  | FALSE |
| 3895 | request\_\_context\_\_app | 6 |  |  |  |  | FALSE |
| 3896 | forecast\_\_virtual\_date | 6 |  |  |  |  | FALSE |
| 3897 | request\_\_provider\_ue\_ratio | 6 |  |  |  |  | FALSE |
| 3898 | request\_\_rtb\_auction\_\_application\_type | 6 |  |  |  |  | FALSE |
| 3899 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3900 | request\_\_slots\_\_avails\_metrics\_\_seller\_sponsor\_avails | 6 |  |  |  |  | FALSE |
| 3901 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller | 6 |  |  |  |  | FALSE |
| 3902 | request\_\_advertisements\_\_validation\_event\_\_numerator\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 3903 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 3904 | request\_\_advertisements\_\_external\_reseller\_\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 3905 | request\_\_rtb\_auction\_\_deal\_\_impression\_index | 6 |  |  |  |  | FALSE |
| 3906 | request\_\_advertisements\_\_reseller\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 3907 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 3908 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3909 | request\_\_context\_\_asset\_chain\_\_inventory\_context\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3910 | request\_\_network\_execution\_ctx\_\_inventory\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 3911 | request\_\_advertisements\_\_external\_reseller\_\_rule\_priority | 6 |  |  |  |  | FALSE |
| 3912 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signals\_\_authorized\_networks | 6 |  |  |  |  | FALSE |
| 3913 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 3914 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 3915 | request\_\_rtb\_auction\_\_mkpl\_partner\_tags | 6 |  |  |  |  | FALSE |
| 3916 | request\_\_advertisements\_\_reseller\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3917 | acks\_\_callback\_info\_\_flag1 | 6 |  |  |  |  | FALSE |
| 3918 | request\_\_external\_candidate\_ad\_\_filter\_reason\_\_slot\_index | 6 |  |  |  |  | FALSE |
| 3919 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_filled\_ad\_num | 6 |  |  |  |  | FALSE |
| 3920 | request\_\_visitor\_\_standard\_operator\_id\_raw | 6 |  |  |  |  | FALSE |
| 3921 | request\_\_outbound\_traffic\_control\_stats\_\_buyer\_platform\_id | 6 |  |  |  |  | FALSE |
| 3922 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_flags | 6 |  |  |  |  | FALSE |
| 3923 | request\_\_advertisements\_\_distributor\_\_bidding\_up\_modified\_revenue | 6 |  |  |  |  | FALSE |
| 3924 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3925 | request\_\_advertisements\_\_reseller\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 3926 | request\_\_external\_candidate\_ad\_\_auction\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 3927 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics\_\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 3928 | forecast\_\_cookies | 6 |  |  |  |  | FALSE |
| 3929 | request\_\_slots\_\_resellers\_\_ad\_filling\_status | 6 |  |  |  |  | FALSE |
| 3930 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 3931 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3932 | request\_\_advertisements\_\_ad\_cro\_network\_id | 6 |  |  |  |  | FALSE |
| 3933 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 3934 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 6 |  |  |  |  | FALSE |
| 3935 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 3936 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3937 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3938 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 3939 | acks\_\_keys\_\_is\_slot\_impression | 6 |  |  |  |  | FALSE |
| 3940 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner | 6 |  |  |  |  | FALSE |
| 3941 | acks\_\_metrics\_\_raw\_ad\_accept\_invitation | 6 |  |  |  |  | FALSE |
| 3942 | request\_\_slots\_\_resellers\_\_avails\_metrics\_\_avails | 6 |  |  |  |  | FALSE |
| 3943 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 3944 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 3945 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 3946 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 3947 | request\_\_slots\_\_outbound\_order\_\_down\_reseller\_index | 6 |  |  |  |  | FALSE |
| 3948 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 3949 | acks\_\_metrics\_\_ad\_rewind | 6 |  |  |  |  | FALSE |
| 3950 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 3951 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 3952 | request\_\_rtb\_auction\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 3953 | request\_\_rtb\_auction\_\_deal\_\_trading\_desk\_id\_raw | 6 |  |  |  |  | FALSE |
| 3954 | request\_\_advertisements\_\_reseller\_\_context\_id | 6 |  |  |  |  | FALSE |
| 3955 | request\_\_slots\_\_time\_unfilled | 6 |  |  |  |  | FALSE |
| 3956 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_audience\_item\_flag | 6 |  |  |  |  | FALSE |
| 3957 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 3958 | request\_\_external\_candidate\_ad\_\_content\_type | 6 |  |  |  |  | FALSE |
| 3959 | request\_\_advertisements\_\_content\_owner\_\_down\_network\_id | 6 |  |  |  |  | FALSE |
| 3960 | request\_\_external\_candidate\_ad\_\_external\_seat\_id | 6 |  |  |  |  | FALSE |
| 3961 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 3962 | request\_\_network\_execution\_ctx\_\_upstream\_network\_id | 6 |  |  |  |  | FALSE |
| 3963 | request\_\_advertisements\_\_advertiser\_id\_raw | 6 |  |  |  |  | FALSE |
| 3964 | request\_\_slots\_\_inbound\_rule | 6 |  |  |  |  | FALSE |
| 3965 | request\_\_context\_\_time\_span\_\_selection\_scenario | 6 |  |  |  |  | FALSE |
| 3966 | request\_\_external\_candidate\_ad\_\_discount\_infos\_\_discount\_amount | 6 |  |  |  |  | FALSE |
| 3967 | request\_\_rtb\_auction\_\_market\_integration\_type | 6 |  |  |  |  | FALSE |
| 3968 | request\_\_external\_candidate\_ad\_\_discount\_infos\_\_discount\_type | 6 |  |  |  |  | FALSE |
| 3969 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_parent | 6 |  |  |  |  | FALSE |
| 3970 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id | 6 |  |  |  |  | FALSE |
| 3971 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 3972 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 3973 | acks\_\_psn\_msg\_\_subscribe\_id | 6 |  |  |  |  | FALSE |
| 3974 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 3975 | request\_\_external\_candidate\_ad\_\_global\_brand\_ids | 6 |  |  |  |  | FALSE |
| 3976 | request\_\_context\_\_asset\_chain\_\_distributor\_\_network\_id | 6 |  |  |  |  | FALSE |
| 3977 | request\_\_rtb\_auction\_\_trading\_desk\_id\_raw | 6 |  |  |  |  | FALSE |
| 3978 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 3979 | request\_\_external\_candidate\_ad\_\_rtb\_impression\_id | 6 |  |  |  |  | FALSE |
| 3980 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_scenario\_id | 6 |  |  |  |  | FALSE |
| 3981 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 3982 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 3983 | request\_\_advertisements\_\_content\_right\_owner\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 3984 | request\_\_advertisements\_\_distributor\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3985 | request\_\_slots\_\_opportunity\_display\_id | 6 |  |  |  |  | FALSE |
| 3986 | acks\_\_metrics\_\_raw\_third\_quartile | 6 |  |  |  |  | FALSE |
| 3987 | request\_\_advertisements\_\_external\_reseller\_\_bidding\_revenue | 6 |  |  |  |  | FALSE |
| 3988 | request\_\_slots\_\_resellers\_\_bidder\_seat\_id\_raw | 6 |  |  |  |  | FALSE |
| 3989 | request\_\_advertisements\_\_network\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 3990 | acks\_\_custom\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 3991 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 3992 | acks\_\_metrics\_\_raw\_ad\_mute | 6 |  |  |  |  | FALSE |
| 3993 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_hhids\_\_id | 6 |  |  |  |  | FALSE |
| 3994 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 3995 | request\_\_advertisements\_\_external\_reseller\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 3996 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_active\_term\_ids | 6 |  |  |  |  | FALSE |
| 3997 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_unconstraint\_gross\_avail\_committed | 6 |  |  |  |  | FALSE |
| 3998 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 3999 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 4000 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key | 6 |  |  |  |  | FALSE |
| 4001 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics\_\_default\_duration | 6 |  |  |  |  | FALSE |
| 4002 | request\_\_advertisements\_\_reseller\_\_site\_id | 6 |  |  |  |  | FALSE |
| 4003 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 4004 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4005 | request\_\_external\_candidate\_ad\_\_creative\_approval\_request | 6 |  |  |  |  | FALSE |
| 4006 | request\_\_context\_\_distributor\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4007 | request\_\_advertisements\_\_external\_reseller\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 4008 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4009 | request\_\_rtb\_auction\_\_impression\_\_max\_duration | 6 |  |  |  |  | FALSE |
| 4010 | request\_\_context\_\_asset\_chain\_\_distributor\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4011 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 4012 | request\_\_context\_\_video\_cro\_context\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4013 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_scheduled\_impression | 6 |  |  |  |  | FALSE |
| 4014 | request\_\_advertisements\_\_content\_right\_owner\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 4015 | request\_\_context\_\_asset\_chain\_\_distributor\_\_scenario\_id | 6 |  |  |  |  | FALSE |
| 4016 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4017 | request\_\_advertisements\_\_content\_owner\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 4018 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4019 | acks | 6 |  |  |  |  | FALSE |
| 4020 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner | 6 |  |  |  |  | FALSE |
| 4021 | deprecate\_\_acked\_video\_view | 6 |  |  |  |  | FALSE |
| 4022 | request\_\_context\_\_asset\_chain\_\_distributor\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 4023 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 4024 | request\_\_advertisements\_\_reseller\_\_unified\_rule\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 4025 | request\_\_cbp\_\_slot\_template\_id\_raw | 6 |  |  |  |  | FALSE |
| 4026 | request\_\_slots\_\_window\_duration | 6 |  |  |  |  | FALSE |
| 4027 | request\_\_external\_candidate\_ad\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4028 | request\_\_audience\_item\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4029 | forecast\_\_metrics\_\_transactional\_map | 6 |  |  |  |  | FALSE |
| 4030 | request\_\_advertisements\_\_reseller\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 4031 | request\_\_visitor\_\_platform\_device\_id\_raw | 6 |  |  |  |  | FALSE |
| 4032 | partners\_\_internal\_seat\_ids | 6 |  |  |  |  | FALSE |
| 4033 | request\_\_slots\_\_resellers\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 4034 | request\_\_advertisements\_\_external\_reseller\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4035 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics | 6 |  |  |  |  | FALSE |
| 4036 | request\_\_slots\_\_resellers\_\_guaranteed\_flags | 6 |  |  |  |  | FALSE |
| 4037 | request\_\_advertisements\_\_content\_right\_owner\_\_ssp\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 4038 | acks\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4039 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 4040 | request\_\_advertisements\_\_external\_reseller\_\_rule\_flags | 6 |  |  |  |  | FALSE |
| 4041 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 6 |  |  |  |  | FALSE |
| 4042 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4043 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4044 | acks\_\_deprecate\_\_placement\_id\_raw | 6 |  |  |  |  | FALSE |
| 4045 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 4046 | request\_\_slots\_\_resellers\_\_forecast\_avails\_metrics\_\_remaining\_avails | 6 |  |  |  |  | FALSE |
| 4047 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4048 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4049 | request\_\_slots\_\_rules\_\_opp\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4050 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4051 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics\_\_opportunity | 6 |  |  |  |  | FALSE |
| 4052 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 4053 | acks\_\_metrics\_\_raw\_ad\_close | 6 |  |  |  |  | FALSE |
| 4054 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4055 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4056 | request\_\_phantom\_candidate\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4057 | request\_\_advertisements\_\_network\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4058 | request\_\_advertisements\_\_effective\_exclude\_aim\_audience\_ids | 6 |  |  |  |  | FALSE |
| 4059 | request\_\_rtb\_auction\_\_buyer\_group\_id | 6 |  |  |  |  | FALSE |
| 4060 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 4061 | request\_\_context\_\_asset\_chain\_\_distributor\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4062 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_active\_term\_ids | 6 |  |  |  |  | FALSE |
| 4063 | request\_\_external\_candidate\_ad\_\_profile\_check\_passed | 6 |  |  |  |  | FALSE |
| 4064 | request\_\_inventory\_group\_\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4065 | acks\_\_metrics\_\_no\_click | 6 |  |  |  |  | FALSE |
| 4066 | request\_\_advertisements\_\_inbound\_rule\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4067 | request\_\_external\_candidate\_ad\_\_playlist\_response\_time | 6 |  |  |  |  | FALSE |
| 4068 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 4069 | request\_\_rtb\_auction\_\_auction\_network\_to\_usd\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 4070 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4071 | request\_\_advertisements\_\_campaign\_id\_raw | 6 |  |  |  |  | FALSE |
| 4072 | acks\_\_metrics\_\_raw\_measurable\_ad\_expand\_collapse\_impression | 6 |  |  |  |  | FALSE |
| 4073 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 4074 | request\_\_advertisements\_\_content\_owner\_\_context\_id | 6 |  |  |  |  | FALSE |
| 4075 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4076 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4077 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 4078 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 4079 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_booked\_impression | 6 |  |  |  |  | FALSE |
| 4080 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 4081 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4082 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 4083 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 4084 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 4085 | request\_\_context\_\_site\_section\_cro\_context\_id | 6 |  |  |  |  | FALSE |
| 4086 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4087 | request\_\_advertisements\_\_external\_reseller\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4088 | aim\_info\_\_aim\_identity\_info\_\_categorized\_signals\_\_authorized\_networks | 6 |  |  |  |  | FALSE |
| 4089 | acks\_\_metrics\_\_ad\_mute | 6 |  |  |  |  | FALSE |
| 4090 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_key | 6 |  |  |  |  | FALSE |
| 4091 | acks\_\_ivt\_tracked\_info | 6 |  |  |  |  | FALSE |
| 4092 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 4093 | request\_\_rtb\_auction\_\_deal | 6 |  |  |  |  | FALSE |
| 4094 | request\_\_advertisements\_\_content\_right\_owner\_\_marketplace\_audience\_extension\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4095 | acks\_\_deprecate\_\_ad\_end | 6 |  |  |  |  | FALSE |
| 4096 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 4097 | request\_\_advertisements\_\_distributor\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4098 | request\_\_slots\_\_seller\_sponsor\_occupation\_on\_carriage | 6 |  |  |  |  | FALSE |
| 4099 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4100 | request\_\_audience\_item\_\_ad\_replica\_id | 6 |  |  |  |  | FALSE |
| 4101 | request\_\_advertisements\_\_cch\_rendition\_id\_raw | 6 |  |  |  |  | FALSE |
| 4102 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4103 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4104 | acks\_\_internal\_slot\_index | 6 |  |  |  |  | FALSE |
| 4105 | request\_\_bidding\_context\_\_bid\_request\_\_site\_\_page\_hash | 6 |  |  |  |  | FALSE |
| 4106 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 4107 | request\_\_advertisements\_\_shading\_context\_\_bid\_price\_usd | 6 |  |  |  |  | FALSE |
| 4108 | request\_\_advertisements\_\_provider\_measured\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 4109 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4110 | request\_\_slots\_\_total\_pods\_in\_group | 6 |  |  |  |  | FALSE |
| 4111 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 4112 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_down\_reseller\_index | 6 |  |  |  |  | FALSE |
| 4113 | request\_\_advertisements\_\_content\_owner\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 4114 | request\_\_slots\_\_resellers\_\_marketplace\_execution\_id | 6 |  |  |  |  | FALSE |
| 4115 | request\_\_inventory\_group\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 4116 | aim\_info\_\_aim\_identity\_info\_\_signal\_combination\_graph\_map\_\_signal\_index | 6 |  |  |  |  | FALSE |
| 4117 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4118 | request\_\_slots\_\_resellers\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4119 | acks\_\_metrics\_\_click | 6 |  |  |  |  | FALSE |
| 4120 | request\_\_slots\_\_resellers\_\_bidder\_seat\_id | 6 |  |  |  |  | FALSE |
| 4121 | request\_\_rtb\_auction\_\_impression\_\_equivalent\_opportunity\_number | 6 |  |  |  |  | FALSE |
| 4122 | acks\_\_keys | 6 |  |  |  |  | FALSE |
| 4123 | request\_\_advertisements\_\_external\_reseller\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4124 | request\_\_advertisements\_\_reseller\_\_count\_imp\_as\_booked | 6 |  |  |  |  | FALSE |
| 4125 | acks\_\_internal\_ad\_index | 6 |  |  |  |  | FALSE |
| 4126 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 4127 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 4128 | request\_\_external\_candidate\_ad\_\_trust\_id | 6 |  |  |  |  | FALSE |
| 4129 | request\_\_slots\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_sponsor\_split\_unit\_num | 6 |  |  |  |  | FALSE |
| 4130 | request\_\_rtb\_auction\_\_auction\_sampling\_\_mode | 6 |  |  |  |  | FALSE |
| 4131 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4132 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4133 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4134 | aim\_info\_\_aim\_audience\_info\_\_graph\_expanded\_type | 6 |  |  |  |  | FALSE |
| 4135 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4136 | acks\_\_metrics | 6 |  |  |  |  | FALSE |
| 4137 | request\_\_advertisements\_\_external\_reseller\_\_supply\_distribution\_cost | 6 |  |  |  |  | FALSE |
| 4138 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4139 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4140 | request\_\_external\_candidate\_ad\_\_advertiser\_id | 6 |  |  |  |  | FALSE |
| 4141 | request\_\_advertisements\_\_inbound\_rule\_\_win\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4142 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map | 6 |  |  |  |  | FALSE |
| 4143 | request\_\_advertisements\_\_replaced\_creative\_id | 6 |  |  |  |  | FALSE |
| 4144 | acks\_\_metrics\_\_raw\_ad\_rewind | 6 |  |  |  |  | FALSE |
| 4145 | request\_\_external\_candidate\_ad\_\_global\_brand\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4146 | request\_\_advertisements\_\_content\_owner\_\_supply\_distribution\_cost | 6 |  |  |  |  | FALSE |
| 4147 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4148 | request\_\_slots\_\_slot\_context\_\_network\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4149 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_value\_\_associated\_expense | 6 |  |  |  |  | FALSE |
| 4150 | forecast\_\_meta\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 4151 | request\_\_advertisements\_\_distributor\_\_marketplace\_audience\_extension\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4152 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_unified\_priority | 6 |  |  |  |  | FALSE |
| 4153 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 4154 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4155 | request\_\_auction\_network\_contexts\_\_dynamic\_floor\_price\_algorithm | 6 |  |  |  |  | FALSE |
| 4156 | forecast\_\_meta\_\_magnifier | 6 |  |  |  |  | FALSE |
| 4157 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4158 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 4159 | request\_\_advertisements\_\_external\_reseller\_\_rule\_ext\_id | 6 |  |  |  |  | FALSE |
| 4160 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 4161 | request\_\_advertisements\_\_relative\_priority | 6 |  |  |  |  | FALSE |
| 4162 | request\_\_advertisements\_\_distributor\_\_ssp\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 4163 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 4164 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 4165 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 4166 | acks\_\_metrics\_\_ad\_accept\_invitation | 6 |  |  |  |  | FALSE |
| 4167 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 4168 | forecast\_\_meta\_\_tid | 6 |  |  |  |  | FALSE |
| 4169 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4170 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 4171 | request\_\_external\_candidate\_ad\_\_unified\_deal\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 4172 | request\_\_advertisements\_\_external\_reseller\_\_competition\_resellers | 6 |  |  |  |  | FALSE |
| 4173 | request\_\_visitor\_\_atlas\_user\_agent | 6 |  |  |  |  | FALSE |
| 4174 | request\_\_advertisements\_\_content\_owner\_\_rule\_ext\_id | 6 |  |  |  |  | FALSE |
| 4175 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos\_\_sub\_yo\_type | 6 |  |  |  |  | FALSE |
| 4176 | request\_\_slots\_\_attrition\_ratio\_\_event\_ratio\_\_concrete\_event\_id | 6 |  |  |  |  | FALSE |
| 4177 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_extended\_user\_ids | 6 |  |  |  |  | FALSE |
| 4178 | request\_\_advertisements\_\_external\_reseller\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 4179 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 4180 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4181 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signals\_\_id | 6 |  |  |  |  | FALSE |
| 4182 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics | 6 |  |  |  |  | FALSE |
| 4183 | request\_\_advertisements\_\_effective\_unified\_priority | 6 |  |  |  |  | FALSE |
| 4184 | request\_\_slots\_\_opportunity\_display\_id\_raw | 6 |  |  |  |  | FALSE |
| 4185 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4186 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4187 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4188 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 4189 | request\_\_slots\_\_custom\_id | 6 |  |  |  |  | FALSE |
| 4190 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4191 | request\_\_external\_candidate\_ad\_\_unified\_deal\_priority | 6 |  |  |  |  | FALSE |
| 4192 | request\_\_network\_execution\_ctx\_\_inbound\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 4193 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4194 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_order\_priority | 6 |  |  |  |  | FALSE |
| 4195 | request\_\_advertisements\_\_net\_price | 6 |  |  |  |  | FALSE |
| 4196 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4197 | acks\_\_deprecate\_\_placement\_id | 6 |  |  |  |  | FALSE |
| 4198 | request\_\_advertisements\_\_content\_right\_owner\_\_bidding\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4199 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_unified\_priority | 6 |  |  |  |  | FALSE |
| 4200 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics | 6 |  |  |  |  | FALSE |
| 4201 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signal\_with\_waterfall | 6 |  |  |  |  | FALSE |
| 4202 | request\_\_visitor\_\_tracked\_term | 6 |  |  |  |  | FALSE |
| 4203 | request\_\_slots\_\_resellers\_\_context\_id | 6 |  |  |  |  | FALSE |
| 4204 | request\_\_advertisements\_\_reseller\_\_unified\_rule\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 4205 | aim\_info\_\_aim\_identity\_info\_\_signal\_combination\_graph\_map\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4206 | request\_\_advertisements\_\_deprecate\_\_click | 6 |  |  |  |  | FALSE |
| 4207 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 4208 | request\_\_context\_\_asset\_chain\_\_distributor\_\_parent | 6 |  |  |  |  | FALSE |
| 4209 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 6 |  |  |  |  | FALSE |
| 4210 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4211 | acks\_\_metrics\_\_raw\_measurable\_ad\_accept\_invitation\_minimize\_impression | 6 |  |  |  |  | FALSE |
| 4212 | acks\_\_psn\_msg\_\_ad\_network\_id | 6 |  |  |  |  | FALSE |
| 4213 | request\_\_context\_\_site\_section\_cro\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4214 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 4215 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 4216 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4217 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 4218 | acks\_\_deprecate\_\_is\_faked | 6 |  |  |  |  | FALSE |
| 4219 | request\_\_slots\_\_height | 6 |  |  |  |  | FALSE |
| 4220 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 4221 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 4222 | acks\_\_metrics\_\_ad\_insertion | 6 |  |  |  |  | FALSE |
| 4223 | request\_\_auction\_network\_contexts\_\_dsps | 6 |  |  |  |  | FALSE |
| 4224 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4225 | request\_\_slots\_\_resellers\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id\_raw | 6 |  |  |  |  | FALSE |
| 4226 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 6 |  |  |  |  | FALSE |
| 4227 | request\_\_advertisements\_\_reseller\_\_supply\_acquisition\_cost | 6 |  |  |  |  | FALSE |
| 4228 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 4229 | request\_\_advertisements\_\_external\_reseller\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 4230 | request\_\_advertisements\_\_global\_advertiser\_id\_raw | 6 |  |  |  |  | FALSE |
| 4231 | request\_\_advertisements\_\_bid\_price\_to\_upstream | 6 |  |  |  |  | FALSE |
| 4232 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics | 6 |  |  |  |  | FALSE |
| 4233 | request\_\_advertisements\_\_advertisement\_context\_\_network\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4234 | request\_\_advertisements\_\_distributor\_\_margin | 6 |  |  |  |  | FALSE |
| 4235 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4236 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 4237 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_context\_id | 6 |  |  |  |  | FALSE |
| 4238 | request\_\_external\_candidate\_ad\_\_auction\_type | 6 |  |  |  |  | FALSE |
| 4239 | request\_\_advertisements\_\_deprecate\_\_ad\_end | 6 |  |  |  |  | FALSE |
| 4240 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 4241 | request\_\_cbp\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4242 | request\_\_external\_candidate\_ad\_\_dsp\_cid | 6 |  |  |  |  | FALSE |
| 4243 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | 6 |  |  |  |  | FALSE |
| 4244 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 6 |  |  |  |  | FALSE |
| 4245 | partners\_\_matched\_audience\_item\_ids | 6 |  |  |  |  | FALSE |
| 4246 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4247 | request\_\_advertisements\_\_universal\_ad\_id | 6 |  |  |  |  | FALSE |
| 4248 | acks\_\_metrics\_\_measurable\_ad\_accept\_invitation\_minimize\_impression | 6 |  |  |  |  | FALSE |
| 4249 | request\_\_advertisements\_\_external\_reseller\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 4250 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 4251 | request\_\_external\_candidate\_ad\_\_cch\_key\_domain\_config\_id | 6 |  |  |  |  | FALSE |
| 4252 | request\_\_advertisements\_\_external\_reseller\_\_ad\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 4253 | request\_\_visitor\_\_referrer\_banning\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4254 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_forecast\_portfolio\_id | 6 |  |  |  |  | FALSE |
| 4255 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 4256 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_order\_priority | 6 |  |  |  |  | FALSE |
| 4257 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4258 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_active\_term\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4259 | request\_\_external\_candidate\_ad\_\_brand\_id\_raw | 6 |  |  |  |  | FALSE |
| 4260 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4261 | request\_\_network\_attribute\_\_nielsen\_win\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4262 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4263 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 4264 | request\_\_advertisements\_\_xdevice\_policy\_id\_raw | 6 |  |  |  |  | FALSE |
| 4265 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_revenue | 6 |  |  |  |  | FALSE |
| 4266 | request\_\_advertisements\_\_content\_right\_owner\_\_count\_imp\_as\_booked | 6 |  |  |  |  | FALSE |
| 4267 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 4268 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 4269 | forecast\_\_timezone | 6 |  |  |  |  | FALSE |
| 4270 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 4271 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4272 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4273 | request\_\_context\_\_standard\_ssp\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 4274 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4275 | request\_\_advertisements\_\_distributor\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4276 | request\_\_advertisements\_\_distributor\_\_bidding\_revenue | 6 |  |  |  |  | FALSE |
| 4277 | forecast\_\_meta\_\_version | 6 |  |  |  |  | FALSE |
| 4278 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 4279 | acks\_\_event\_callback\_redirect | 6 |  |  |  |  | FALSE |
| 4280 | request\_\_advertisements\_\_global\_brand\_id | 6 |  |  |  |  | FALSE |
| 4281 | request\_\_advertisements\_\_placement\_id\_raw | 6 |  |  |  |  | FALSE |
| 4282 | request\_\_advertisements\_\_budget\_control\_level | 6 |  |  |  |  | FALSE |
| 4283 | request\_\_rtb\_auction\_\_bid\_throttling\_info | 6 |  |  |  |  | FALSE |
| 4284 | request\_\_network\_execution\_ctx\_\_data\_right | 6 |  |  |  |  | FALSE |
| 4285 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails\_\_value | 6 |  |  |  |  | FALSE |
| 4286 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4287 | request\_\_external\_bridge\_records | 6 |  |  |  |  | FALSE |
| 4288 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4289 | request\_\_advertisements\_\_content\_right\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4290 | acks\_\_deprecate\_\_first\_quartile | 6 |  |  |  |  | FALSE |
| 4291 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4292 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_filled\_duration | 6 |  |  |  |  | FALSE |
| 4293 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4294 | request\_\_slots\_\_outbound\_order\_\_active\_term\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4295 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4296 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 4297 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4298 | request\_\_advertisements\_\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 4299 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4300 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 4301 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 4302 | request\_\_slots\_\_resellers\_\_price | 6 |  |  |  |  | FALSE |
| 4303 | request\_\_slots\_\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 4304 | request\_\_advertisements\_\_external\_reseller\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4305 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4306 | forecast\_\_metrics\_\_transactional\_map\_\_value\_\_associated\_expense | 6 |  |  |  |  | FALSE |
| 4307 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4308 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4309 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 4310 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 4311 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value | 6 |  |  |  |  | FALSE |
| 4312 | request\_\_slots\_\_rules\_\_win\_rule\_id | 6 |  |  |  |  | FALSE |
| 4313 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4314 | request\_\_advertisements\_\_external\_vast\_ad\_id | 6 |  |  |  |  | FALSE |
| 4315 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4316 | request\_\_advertisements\_\_distributor\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4317 | request\_\_advertisements\_\_billable\_rate | 6 |  |  |  |  | FALSE |
| 4318 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4319 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4320 | request\_\_slots\_\_initial\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 4321 | request\_\_slots\_\_normalized\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 4322 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_total\_avail | 6 |  |  |  |  | FALSE |
| 4323 | uids | 6 |  |  |  |  | FALSE |
| 4324 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4325 | acks\_\_metrics\_\_ad\_pause | 6 |  |  |  |  | FALSE |
| 4326 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_booked\_impression | 6 |  |  |  |  | FALSE |
| 4327 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4328 | request\_\_advertisements\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4329 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 4330 | request\_\_advertisements\_\_content\_owner\_\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 4331 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4332 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4333 | request\_\_context\_\_standard\_privacy\_id\_raw | 6 |  |  |  |  | FALSE |
| 4334 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 4335 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4336 | request\_\_bidding\_context\_\_bid\_request\_\_impression\_\_id | 6 |  |  |  |  | FALSE |
| 4337 | request\_\_advertisements\_\_external\_reseller\_\_marketplace\_audience\_extension\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4338 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 4339 | request\_\_context\_\_standard\_content\_territory\_id\_raw | 6 |  |  |  |  | FALSE |
| 4340 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails | 6 |  |  |  |  | FALSE |
| 4341 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 4342 | ack\_\_server\_id | 6 |  |  |  |  | FALSE |
| 4343 | request\_\_context\_\_asset\_chain\_\_distributor\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 4344 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map | 6 |  |  |  |  | FALSE |
| 4345 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 4346 | request\_\_external\_candidate\_ad\_\_buyer\_platform\_id\_raw | 6 |  |  |  |  | FALSE |
| 4347 | request\_\_advertisements\_\_deprecate\_\_ad\_impression | 6 |  |  |  |  | FALSE |
| 4348 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_pretty\_id\_raw | 6 |  |  |  |  | FALSE |
| 4349 | request\_\_advertisements\_\_associate | 6 |  |  |  |  | FALSE |
| 4350 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4351 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4352 | request\_\_guaranteed\_deal\_avail\_\_buyer\_id\_raw | 6 |  |  |  |  | FALSE |
| 4353 | request\_\_context\_\_tv\_network\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4354 | request\_\_decision\_info\_\_candidates\_info\_\_flags | 6 |  |  |  |  | FALSE |
| 4355 | acks\_\_vod\_session\_id | 6 |  |  |  |  | FALSE |
| 4356 | request\_\_slots\_\_width | 6 |  |  |  |  | FALSE |
| 4357 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4358 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4359 | acks\_\_metrics\_\_raw\_ad\_expand | 6 |  |  |  |  | FALSE |
| 4360 | request\_\_network\_execution\_ctx\_\_selection\_info | 6 |  |  |  |  | FALSE |
| 4361 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner | 6 |  |  |  |  | FALSE |
| 4362 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4363 | request\_\_advertisements\_\_deprecate\_\_rate\_cost | 6 |  |  |  |  | FALSE |
| 4364 | request\_\_errors\_\_message | 6 |  |  |  |  | FALSE |
| 4365 | request\_\_advertisements\_\_targeted\_ratio | 6 |  |  |  |  | FALSE |
| 4366 | request\_\_model\_framework\_\_network\_model\_contexts\_\_flags | 6 |  |  |  |  | FALSE |
| 4367 | acks\_\_keys\_\_is\_internal | 6 |  |  |  |  | FALSE |
| 4368 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_up\_network\_id | 6 |  |  |  |  | FALSE |
| 4369 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 4370 | request\_\_advertisements\_\_cch\_key | 6 |  |  |  |  | FALSE |
| 4371 | request\_\_advertisements\_\_original\_bidding\_price | 6 |  |  |  |  | FALSE |
| 4372 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 4373 | request\_\_advertisements\_\_content\_owner\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4374 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4375 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4376 | request\_\_advertisements\_\_internal\_candidate\_index | 6 |  |  |  |  | FALSE |
| 4377 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 4378 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4379 | acks\_\_deprecate\_\_c3\_ad\_impression | 6 |  |  |  |  | FALSE |
| 4380 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails\_committed\_\_key | 6 |  |  |  |  | FALSE |
| 4381 | request\_\_errors\_\_series\_id | 6 |  |  |  |  | FALSE |
| 4382 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4383 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 4384 | request\_\_advertisements\_\_reseller\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4385 | request\_\_advertisements\_\_reseller\_\_competition\_resellers | 6 |  |  |  |  | FALSE |
| 4386 | request\_\_advertisements\_\_external\_reseller\_\_selected\_yield\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4387 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4388 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4389 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4390 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 6 |  |  |  |  | FALSE |
| 4391 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 4392 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4393 | request\_\_rtb\_auction\_\_deal\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 4394 | acks\_\_metrics\_\_ad\_bid\_won | 6 |  |  |  |  | FALSE |
| 4395 | request\_\_slots\_\_max\_bitrate | 6 |  |  |  |  | FALSE |
| 4396 | forecast\_\_meta\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4397 | request\_\_advertisements\_\_network\_\_mkpl\_info | 6 |  |  |  |  | FALSE |
| 4398 | request\_\_advertisements\_\_external\_reseller\_\_bidding\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4399 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_channel\_id | 6 |  |  |  |  | FALSE |
| 4400 | request\_\_advertisements\_\_distributor\_\_root\_section\_group | 6 |  |  |  |  | FALSE |
| 4401 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 4402 | request\_\_external\_candidate\_ad\_\_cch\_key | 6 |  |  |  |  | FALSE |
| 4403 | request\_\_advertisements\_\_replaced\_ad\_id | 6 |  |  |  |  | FALSE |
| 4404 | request\_\_advertisements\_\_content\_right\_owner\_\_unified\_rule\_priority\_\_sub\_priority\_value | 6 |  |  |  |  | FALSE |
| 4405 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4406 | forecast\_\_meta\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4407 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_owner\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4408 | acks\_\_metrics\_\_measurable\_ad\_close\_impression | 6 |  |  |  |  | FALSE |
| 4409 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4410 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4411 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4412 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics | 6 |  |  |  |  | FALSE |
| 4413 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 4414 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4415 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4416 | request\_\_external\_candidate\_ad\_\_internal\_group\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4417 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 4418 | request\_\_advertisements\_\_targeting\_criteria\_id\_raw | 6 |  |  |  |  | FALSE |
| 4419 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 4420 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4421 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4422 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 4423 | request\_\_network\_audience\_items\_\_flags | 6 |  |  |  |  | FALSE |
| 4424 | request\_\_advertisements\_\_duration | 6 |  |  |  |  | FALSE |
| 4425 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails | 6 |  |  |  |  | FALSE |
| 4426 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_scheduled\_impression | 6 |  |  |  |  | FALSE |
| 4427 | request\_\_context\_\_site\_section\_cro\_context\_group\_id | 6 |  |  |  |  | FALSE |
| 4428 | acks\_\_keys\_\_is\_expired | 6 |  |  |  |  | FALSE |
| 4429 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 4430 | request\_\_context\_\_asset\_chain\_\_distributor\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4431 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 4432 | request\_\_advertisements\_\_external\_reseller\_\_unified\_rule\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 4433 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 4434 | request\_\_rtb\_auction\_\_deal\_\_internal\_seat\_id\_raw | 6 |  |  |  |  | FALSE |
| 4435 | acks\_\_metrics\_\_ad\_expand | 6 |  |  |  |  | FALSE |
| 4436 | request\_\_advertisements\_\_content\_owner\_\_inventory\_id | 6 |  |  |  |  | FALSE |
| 4437 | request\_\_advertisements\_\_distributor\_\_count\_imp\_as\_booked | 6 |  |  |  |  | FALSE |
| 4438 | request\_\_external\_candidate\_ad\_\_creative\_approval\_request\_\_approval\_scope | 6 |  |  |  |  | FALSE |
| 4439 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4440 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4441 | acks\_\_identifier\_\_source | 6 |  |  |  |  | FALSE |
| 4442 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 6 |  |  |  |  | FALSE |
| 4443 | request\_\_context\_\_site\_section\_cro\_context\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4444 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 4445 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4446 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4447 | request\_\_network\_attribute\_\_region\_ids | 6 |  |  |  |  | FALSE |
| 4448 | request\_\_auction\_network\_contexts\_\_dsps\_\_third\_party\_identifier\_ids | 6 |  |  |  |  | FALSE |
| 4449 | request\_\_advertisements\_\_deprecate\_\_first\_quartile | 6 |  |  |  |  | FALSE |
| 4450 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 4451 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver | 6 |  |  |  |  | FALSE |
| 4452 | request\_\_advertisements\_\_reseller\_\_bidding\_up\_original\_revenue | 6 |  |  |  |  | FALSE |
| 4453 | request\_\_advertisements\_\_deprecate | 6 |  |  |  |  | FALSE |
| 4454 | request\_\_advertisements\_\_external\_reseller\_\_bidding\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4455 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_channel\_id\_raw | 6 |  |  |  |  | FALSE |
| 4456 | request\_\_slots\_\_resellers\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 4457 | request\_\_visitor\_\_programmer\_individual\_id | 6 |  |  |  |  | FALSE |
| 4458 | request\_\_advertisements\_\_contextual\_billings\_\_segment\_id\_raw | 6 |  |  |  |  | FALSE |
| 4459 | request\_\_advertisements\_\_reseller\_\_root\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4460 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_impression | 6 |  |  |  |  | FALSE |
| 4461 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 4462 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 4463 | request\_\_advertisements\_\_reseller\_\_ad\_priority\_bucket | 6 |  |  |  |  | FALSE |
| 4464 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 4465 | request\_\_advertisements\_\_reseller\_\_marketplace\_audience\_extension\_deal\_id | 6 |  |  |  |  | FALSE |
| 4466 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4467 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_listing\_id | 6 |  |  |  |  | FALSE |
| 4468 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4469 | acks\_\_metrics\_\_raw\_measurable\_ad\_mute\_unmute\_impression | 6 |  |  |  |  | FALSE |
| 4470 | acks\_\_metrics\_\_raw\_slot\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 4471 | request\_\_dro\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4472 | request\_\_slots\_\_deprecate | 6 |  |  |  |  | FALSE |
| 4473 | request\_\_advertisements\_\_replaced\_rendition\_id | 6 |  |  |  |  | FALSE |
| 4474 | request\_\_external\_candidate\_ad\_\_vast\_creative\_id | 6 |  |  |  |  | FALSE |
| 4475 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics | 6 |  |  |  |  | FALSE |
| 4476 | request\_\_visitor\_\_identity\_user\_ids\_\_authorized\_network\_id | 6 |  |  |  |  | FALSE |
| 4477 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4478 | request\_\_advertisements\_\_contextual\_billings\_\_segment\_id | 6 |  |  |  |  | FALSE |
| 4479 | request\_\_network\_audience\_items\_\_non\_tracked\_audience\_item\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4480 | request\_\_advertisements\_\_content\_right\_owner\_\_bidding\_up\_original\_revenue | 6 |  |  |  |  | FALSE |
| 4481 | request\_\_rtb\_auction\_\_trading\_desk\_id | 6 |  |  |  |  | FALSE |
| 4482 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4483 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4484 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4485 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4486 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4487 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4488 | request\_\_advertisements\_\_replaced\_campaign\_id\_raw | 6 |  |  |  |  | FALSE |
| 4489 | request\_\_advertisements\_\_market\_ad\_id | 6 |  |  |  |  | FALSE |
| 4490 | request\_\_slots\_\_time\_position | 6 |  |  |  |  | FALSE |
| 4491 | request\_\_rtb\_auction\_\_auction\_network\_context\_index | 6 |  |  |  |  | FALSE |
| 4492 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_scheduled\_impression | 6 |  |  |  |  | FALSE |
| 4493 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 4494 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_id\_raw | 6 |  |  |  |  | FALSE |
| 4495 | request\_\_network\_audience\_items\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4496 | request\_\_advertisements\_\_xdevice\_policy\_id | 6 |  |  |  |  | FALSE |
| 4497 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 4498 | request\_\_advertisements\_\_trimmed\_tracking\_domains\_\_domain | 6 |  |  |  |  | FALSE |
| 4499 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4500 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner | 6 |  |  |  |  | FALSE |
| 4501 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4502 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4503 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4504 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4505 | request\_\_network\_execution\_ctx | 6 |  |  |  |  | FALSE |
| 4506 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4507 | forecast\_\_metrics\_\_transactional\_competing\_map | 6 |  |  |  |  | FALSE |
| 4508 | request\_\_contextual\_segments | 6 |  |  |  |  | FALSE |
| 4509 | acks\_\_deprecate\_\_click | 6 |  |  |  |  | FALSE |
| 4510 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 4511 | request\_\_global\_currency\_\_currencies\_\_network\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4512 | acks\_\_custom\_ad\_price | 6 |  |  |  |  | FALSE |
| 4513 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 4514 | request\_\_context\_\_asset\_chain\_\_distributor\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4515 | request\_\_rtb\_auction\_\_deal\_\_matched\_inventory\_package\_ids | 6 |  |  |  |  | FALSE |
| 4516 | request\_\_advertisements\_\_reseller\_\_rule\_priority | 6 |  |  |  |  | FALSE |
| 4517 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signals | 6 |  |  |  |  | FALSE |
| 4518 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 4519 | request\_\_rtb\_auction\_\_bid\_throttling\_status | 6 |  |  |  |  | FALSE |
| 4520 | request\_\_network\_attribute\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4521 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4522 | request\_\_external\_candidate\_ad\_\_buyer\_platform\_id | 6 |  |  |  |  | FALSE |
| 4523 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id | 6 |  |  |  |  | FALSE |
| 4524 | request\_\_visitor\_\_operator\_zone\_id\_raw | 6 |  |  |  |  | FALSE |
| 4525 | request\_\_external\_candidate\_ad\_\_deal\_type | 6 |  |  |  |  | FALSE |
| 4526 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 4527 | request\_\_slots\_\_resellers\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4528 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 4529 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4530 | request\_\_slots\_\_resellers\_\_inbound\_order\_type | 6 |  |  |  |  | FALSE |
| 4531 | request\_\_advertisements\_\_replaced\_placement\_id\_raw | 6 |  |  |  |  | FALSE |
| 4532 | request\_\_context\_\_asset\_chain\_\_content\_owner | 6 |  |  |  |  | FALSE |
| 4533 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4534 | request\_\_advertisements\_\_distributor\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4535 | forecast\_\_metrics\_\_custom\_portfolio\_map | 6 |  |  |  |  | FALSE |
| 4536 | request\_\_network\_execution\_ctx\_\_inventory\_\_site\_section\_id | 6 |  |  |  |  | FALSE |
| 4537 | request\_\_advertisements\_\_content\_owner\_\_rule\_id | 6 |  |  |  |  | FALSE |
| 4538 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_listing\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4539 | request\_\_context\_\_standard\_movie\_rating\_id\_raw | 6 |  |  |  |  | FALSE |
| 4540 | request\_\_advertisements\_\_content\_owner\_\_flags | 6 |  |  |  |  | FALSE |
| 4541 | request\_\_rtb\_auction\_\_deal\_\_buyer\_id | 6 |  |  |  |  | FALSE |
| 4542 | request\_\_advertisements\_\_content\_right\_owner\_\_selected\_yield\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4543 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4544 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id | 6 |  |  |  |  | FALSE |
| 4545 | request\_\_advertisements\_\_network\_\_site\_section\_id | 6 |  |  |  |  | FALSE |
| 4546 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_listing\_ids | 6 |  |  |  |  | FALSE |
| 4547 | acks\_\_psn\_msg | 6 |  |  |  |  | FALSE |
| 4548 | request\_\_slots\_\_deprecate\_\_slot\_end | 6 |  |  |  |  | FALSE |
| 4549 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 4550 | aim\_info\_\_envelope\_info\_\_envelope\_identifiers\_\_key | 6 |  |  |  |  | FALSE |
| 4551 | request\_\_advertisements\_\_external\_reseller\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4552 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4553 | request\_\_network\_attribute\_\_flags | 6 |  |  |  |  | FALSE |
| 4554 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4555 | request\_\_advertisements\_\_content\_right\_owner\_\_bidding\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4556 | request\_\_advertisements\_\_content\_owner\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 4557 | request\_\_advertisements\_\_deprecate\_\_complete | 6 |  |  |  |  | FALSE |
| 4558 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 4559 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4560 | request\_\_context\_\_asset\_chain\_\_distributor | 6 |  |  |  |  | FALSE |
| 4561 | request\_\_external\_candidate\_ad\_\_discount\_infos | 6 |  |  |  |  | FALSE |
| 4562 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4563 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4564 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4565 | forecast\_\_metrics\_\_transactional\_map\_\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4566 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_scheduled\_impression\_committed | 6 |  |  |  |  | FALSE |
| 4567 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4568 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 4569 | request\_\_network\_attribute\_\_custom\_platform\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4570 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4571 | request\_\_external\_candidate\_ad\_\_creative\_approval\_request\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4572 | request\_\_decision\_info\_\_candidates\_info\_\_life\_stage | 6 |  |  |  |  | FALSE |
| 4573 | request\_\_rtb\_auction\_\_deal\_\_internal\_group\_deal\_id | 6 |  |  |  |  | FALSE |
| 4574 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_coincidence | 6 |  |  |  |  | FALSE |
| 4575 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4576 | request\_\_rtb\_auction\_\_buyer\_platform\_id\_raw | 6 |  |  |  |  | FALSE |
| 4577 | acks\_\_psn\_msg\_\_plc\_end\_time | 6 |  |  |  |  | FALSE |
| 4578 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 4579 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4580 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4581 | request\_\_advertisements\_\_reseller\_\_down\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4582 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_rbp\_dimension | 6 |  |  |  |  | FALSE |
| 4583 | request\_\_advertisements\_\_content\_owner\_\_rule\_flags | 6 |  |  |  |  | FALSE |
| 4584 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 4585 | request\_\_network\_attribute\_\_portfolio\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4586 | request\_\_external\_candidate\_ad\_\_duration | 6 |  |  |  |  | FALSE |
| 4587 | request\_\_slots\_\_carriage\_listing\_split\_unit\_num | 6 |  |  |  |  | FALSE |
| 4588 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 4589 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 4590 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 4591 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 4592 | request\_\_advertisements\_\_content\_right\_owner\_\_supply\_acquisition\_cost | 6 |  |  |  |  | FALSE |
| 4593 | request\_\_network\_execution\_ctx\_\_inventory\_package\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4594 | request\_\_advertisements\_\_external\_reseller\_\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 4595 | acks\_\_identifier | 6 |  |  |  |  | FALSE |
| 4596 | request\_\_rtb\_auction\_\_execution\_contexts | 6 |  |  |  |  | FALSE |
| 4597 | request\_\_advertisements\_\_external\_reseller\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4598 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4599 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4600 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 4601 | request\_\_context\_\_asset\_chain | 6 |  |  |  |  | FALSE |
| 4602 | request\_\_errors\_\_external\_user\_id | 6 |  |  |  |  | FALSE |
| 4603 | request\_\_auction\_network\_contexts\_\_app\_storeurl | 6 |  |  |  |  | FALSE |
| 4604 | acks\_\_deprecate\_\_slot\_end | 6 |  |  |  |  | FALSE |
| 4605 | request\_\_slots\_\_seller\_sponsor\_occupation\_on\_carriage\_\_seller\_inventory\_owner\_id | 6 |  |  |  |  | FALSE |
| 4606 | request\_\_advertisements\_\_distributor\_\_flags | 6 |  |  |  |  | FALSE |
| 4607 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4608 | request\_\_advertisements\_\_distributor\_\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4609 | request\_\_advertisements\_\_ad\_oo\_network\_id | 6 |  |  |  |  | FALSE |
| 4610 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4611 | request\_\_external\_candidate\_ad\_\_market\_ad\_id | 6 |  |  |  |  | FALSE |
| 4612 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 4613 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4614 | request\_\_advertisements\_\_content\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4615 | request\_\_advertisements\_\_reseller\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4616 | acks\_\_concrete\_event\_provider\_id\_raw | 6 |  |  |  |  | FALSE |
| 4617 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 4618 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4619 | request\_\_advertisements\_\_content\_right\_owner\_\_bidding\_up\_modified\_revenue | 6 |  |  |  |  | FALSE |
| 4620 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4621 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 4622 | acks\_\_metrics\_\_ad\_minimize | 6 |  |  |  |  | FALSE |
| 4623 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 4624 | request\_\_slots\_\_resellers\_\_unfilled\_avails | 6 |  |  |  |  | FALSE |
| 4625 | request\_\_advertisements\_\_content\_right\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4626 | request\_\_advertisements\_\_unified\_yield\_\_replaced\_entity\_id | 6 |  |  |  |  | FALSE |
| 4627 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 4628 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 4629 | request\_\_external\_candidate\_ad\_\_bidding\_seat\_id | 6 |  |  |  |  | FALSE |
| 4630 | aim\_info\_\_aim\_identity\_info\_\_signal\_combination\_graph\_map\_\_graph\_index | 6 |  |  |  |  | FALSE |
| 4631 | request\_\_errors\_\_site\_section\_id | 6 |  |  |  |  | FALSE |
| 4632 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4633 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_price | 6 |  |  |  |  | FALSE |
| 4634 | request\_\_network\_execution\_ctx\_\_flags | 6 |  |  |  |  | FALSE |
| 4635 | request\_\_context\_\_asset\_chain\_\_distributor\_\_context\_id | 6 |  |  |  |  | FALSE |
| 4636 | request\_\_advertisements\_\_fallback\_ad\_uniq\_id\_raw | 6 |  |  |  |  | FALSE |
| 4637 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4638 | request\_\_network\_attribute | 6 |  |  |  |  | FALSE |
| 4639 | request\_\_external\_candidate\_ad\_\_internal\_rtb\_auction\_index | 6 |  |  |  |  | FALSE |
| 4640 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 4641 | request\_\_advertisements\_\_trimmed\_tracking\_domains | 6 |  |  |  |  | FALSE |
| 4642 | request\_\_advertisements\_\_distributor\_\_revenue | 6 |  |  |  |  | FALSE |
| 4643 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4644 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 6 |  |  |  |  | FALSE |
| 4645 | request\_\_network\_attribute\_\_id\_graph | 6 |  |  |  |  | FALSE |
| 4646 | request\_\_external\_candidate\_ad\_\_trading\_desk\_id | 6 |  |  |  |  | FALSE |
| 4647 | request\_\_context\_\_site\_section\_cro\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4648 | request\_\_external\_candidate\_ad\_\_bidding\_buyer\_id | 6 |  |  |  |  | FALSE |
| 4649 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 4650 | acks\_\_metrics\_\_raw\_ad\_resume | 6 |  |  |  |  | FALSE |
| 4651 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4652 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 4653 | request\_\_slots\_\_outbound\_order\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 4654 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 6 |  |  |  |  | FALSE |
| 4655 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 4656 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_site\_id | 6 |  |  |  |  | FALSE |
| 4657 | request\_\_advertisements\_\_rules\_\_opp\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4658 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_forecast\_portfolio\_id | 6 |  |  |  |  | FALSE |
| 4659 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 4660 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4661 | request\_\_advertisements\_\_replaced\_campaign\_id | 6 |  |  |  |  | FALSE |
| 4662 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value\_\_coincidence | 6 |  |  |  |  | FALSE |
| 4663 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4664 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_parent | 6 |  |  |  |  | FALSE |
| 4665 | acks\_\_keys\_\_is\_generated\_slot\_impression\_duplicated | 6 |  |  |  |  | FALSE |
| 4666 | idx\_\_has\_network | 6 |  |  |  |  | FALSE |
| 4667 | request\_\_slots\_\_outbound\_order\_\_order\_transaction\_type | 6 |  |  |  |  | FALSE |
| 4668 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor | 6 |  |  |  |  | FALSE |
| 4669 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 6 |  |  |  |  | FALSE |
| 4670 | acks\_\_metrics\_\_ad\_unmute | 6 |  |  |  |  | FALSE |
| 4671 | request\_\_external\_candidate\_ad\_\_discount\_infos\_\_discount\_id | 6 |  |  |  |  | FALSE |
| 4672 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4673 | acks\_\_clearing\_price\_revenue\_chain | 6 |  |  |  |  | FALSE |
| 4674 | partners\_\_eligible\_outbound\_orders\_\_listing\_id | 6 |  |  |  |  | FALSE |
| 4675 | acks\_\_reseller\_networks | 6 |  |  |  |  | FALSE |
| 4676 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics | 6 |  |  |  |  | FALSE |
| 4677 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 4678 | request\_\_external\_candidate\_ad\_\_mpe\_deduction\_on\_selection\_fixed\_fee | 6 |  |  |  |  | FALSE |
| 4679 | request\_\_advertisements\_\_shading\_context | 6 |  |  |  |  | FALSE |
| 4680 | request\_\_external\_candidate\_ad\_\_external\_ad\_id\_domain\_config\_id | 6 |  |  |  |  | FALSE |
| 4681 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 4682 | request\_\_quarter\_hour\_id | 6 |  |  |  |  | FALSE |
| 4683 | request\_\_slots\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 4684 | request\_\_network\_attribute\_\_num\_user\_db\_terms | 6 |  |  |  |  | FALSE |
| 4685 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_phase | 6 |  |  |  |  | FALSE |
| 4686 | request\_\_advertisements\_\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 4687 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 4688 | request\_\_context\_\_site | 6 |  |  |  |  | FALSE |
| 4689 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 4690 | request\_\_slots\_\_inbound\_rule\_\_win\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 4691 | request\_\_advertisements\_\_distributor\_\_rule\_ext\_id\_raw | 6 |  |  |  |  | FALSE |
| 4692 | request\_\_slots\_\_guaranteed\_flags | 6 |  |  |  |  | FALSE |
| 4693 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4694 | acks\_\_yield\_optimization\_ids\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4695 | request\_\_bidding\_context | 6 |  |  |  |  | FALSE |
| 4696 | request\_\_slots\_\_rules | 6 |  |  |  |  | FALSE |
| 4697 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4698 | request\_\_context\_\_asset\_chain\_\_distributor\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4699 | request\_\_network\_attribute\_\_comscore\_win\_section\_id | 6 |  |  |  |  | FALSE |
| 4700 | request\_\_context\_\_site\_section\_chain\_\_distributor | 6 |  |  |  |  | FALSE |
| 4701 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 4702 | request\_\_advertisements\_\_content\_owner\_\_unified\_rule\_priority | 6 |  |  |  |  | FALSE |
| 4703 | request\_\_advertisements\_\_content\_owner\_\_count\_imp\_as\_booked | 6 |  |  |  |  | FALSE |
| 4704 | request\_\_visitor\_\_identity\_user\_ids | 6 |  |  |  |  | FALSE |
| 4705 | request\_\_advertisements\_\_network\_\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4706 | forecast\_\_meta\_\_virtual\_time | 6 |  |  |  |  | FALSE |
| 4707 | request\_\_advertisements\_\_unified\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 4708 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 6 |  |  |  |  | FALSE |
| 4709 | request\_\_context\_\_distributor\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4710 | request\_\_rtb\_auction\_\_buyer\_platform\_id | 6 |  |  |  |  | FALSE |
| 4711 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4712 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 6 |  |  |  |  | FALSE |
| 4713 | request\_\_errors\_\_type | 6 |  |  |  |  | FALSE |
| 4714 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 4715 | acks\_\_yield\_optimization\_ids\_\_optimization\_ids | 6 |  |  |  |  | FALSE |
| 4716 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4717 | request\_\_slots\_\_inventory\_distribution\_contexts | 6 |  |  |  |  | FALSE |
| 4718 | aim\_info\_\_aim\_audience\_info\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4719 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 4720 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 6 |  |  |  |  | FALSE |
| 4721 | candidate\_\_external\_ad\_id\_domain\_config\_id | 6 |  |  |  |  | FALSE |
| 4722 | request\_\_visitor\_\_xfinity\_idfa | 6 |  |  |  |  | FALSE |
| 4723 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4724 | request\_\_advertisements\_\_reseller\_\_root\_asset\_id | 6 |  |  |  |  | FALSE |
| 4725 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_asset\_id | 6 |  |  |  |  | FALSE |
| 4726 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_metrics\_type | 6 |  |  |  |  | FALSE |
| 4727 | request\_\_advertisements\_\_ad\_distributor\_network\_list | 6 |  |  |  |  | FALSE |
| 4728 | request\_\_advertisements\_\_data\_provider\_id | 6 |  |  |  |  | FALSE |
| 4729 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4730 | request\_\_slots\_\_avails | 6 |  |  |  |  | FALSE |
| 4731 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4732 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4733 | request\_\_advertisements\_\_content\_right\_owner\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4734 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4735 | request\_\_advertisements\_\_io\_id | 6 |  |  |  |  | FALSE |
| 4736 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 6 |  |  |  |  | FALSE |
| 4737 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 4738 | acks\_\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 4739 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 4740 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4741 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 6 |  |  |  |  | FALSE |
| 4742 | forecast\_\_meta | 6 |  |  |  |  | FALSE |
| 4743 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 6 |  |  |  |  | FALSE |
| 4744 | request\_\_slots\_\_resellers\_\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 4745 | request\_\_advertisements\_\_content\_owner\_\_up\_revenue\_as\_content\_owner | 6 |  |  |  |  | FALSE |
| 4746 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4747 | acks\_\_keys\_\_is\_request\_faked\_slot\_impression | 6 |  |  |  |  | FALSE |
| 4748 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4749 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 4750 | request\_\_advertisements\_\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 4751 | request\_\_context\_\_site\_section\_chain\_\_inventory\_context\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4752 | request\_\_slots\_\_resellers\_\_vod\_programmer\_avails\_metrics\_\_avails | 6 |  |  |  |  | FALSE |
| 4753 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4754 | request\_\_advertisements\_\_content\_owner\_\_rule\_ext\_id\_raw | 6 |  |  |  |  | FALSE |
| 4755 | request\_\_advertisements\_\_variant\_creative\_ids | 6 |  |  |  |  | FALSE |
| 4756 | request\_\_context\_\_header\_bidding\_\_key\_value | 6 |  |  |  |  | FALSE |
| 4757 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4758 | request\_\_advertisements\_\_external\_reseller\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4759 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4760 | request\_\_advertisements\_\_content\_owner\_\_bidding\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4761 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4762 | acks\_\_metrics\_\_raw\_no\_click | 6 |  |  |  |  | FALSE |
| 4763 | request\_\_slots\_\_resellers\_\_ad\_filling\_status\_\_available\_duration | 6 |  |  |  |  | FALSE |
| 4764 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4765 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_value | 6 |  |  |  |  | FALSE |
| 4766 | acks\_\_keys\_\_is\_external\_ad | 6 |  |  |  |  | FALSE |
| 4767 | forecast | 6 |  |  |  |  | FALSE |
| 4768 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4769 | request\_\_scores\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4770 | request\_\_external\_candidate\_ad\_\_two\_phase\_translated | 6 |  |  |  |  | FALSE |
| 4771 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 4772 | request\_\_soft\_guaranteed\_ad\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4773 | request\_\_advertisements\_\_network\_\_reseller\_network\_id | 6 |  |  |  |  | FALSE |
| 4774 | request\_\_auction\_network\_contexts\_\_dsps\_\_id | 6 |  |  |  |  | FALSE |
| 4775 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4776 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_coincidence | 6 |  |  |  |  | FALSE |
| 4777 | request\_\_advertisements\_\_distributor\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 4778 | request\_\_slots\_\_inventory\_mask | 6 |  |  |  |  | FALSE |
| 4779 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_revenue | 6 |  |  |  |  | FALSE |
| 4780 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4781 | request\_\_visitor\_\_standard\_manufacturer\_id\_raw | 6 |  |  |  |  | FALSE |
| 4782 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 6 |  |  |  |  | FALSE |
| 4783 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 4784 | request\_\_advertisements\_\_reseller\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4785 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 4786 | request\_\_advertisements\_\_ad\_oo\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4787 | uids\_\_ack\_uid | 6 |  |  |  |  | FALSE |
| 4788 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 4789 | request\_\_advertisements\_\_reseller | 6 |  |  |  |  | FALSE |
| 4790 | request\_\_advertisements\_\_external\_reseller\_\_down\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4791 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_demand\_type | 6 |  |  |  |  | FALSE |
| 4792 | acks\_\_clearing\_price\_revenue\_chain\_\_external\_reseller\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4793 | request\_\_advertisements\_\_ad\_co\_network\_list | 6 |  |  |  |  | FALSE |
| 4794 | request\_\_network\_execution\_ctx\_\_inventory\_\_site\_id | 6 |  |  |  |  | FALSE |
| 4795 | acks\_\_psn\_msg\_\_session\_id | 6 |  |  |  |  | FALSE |
| 4796 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 4797 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 4798 | aim\_info\_\_aim\_audience\_info\_\_audience\_partner\_records\_\_segments\_\_id | 6 |  |  |  |  | FALSE |
| 4799 | request\_\_advertisements\_\_content\_right\_owner\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 4800 | request\_\_advertisements\_\_content\_owner\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 4801 | request\_\_errors\_\_id\_graph\_vendor | 6 |  |  |  |  | FALSE |
| 4802 | request\_\_external\_candidate\_ad\_\_dsp\_id\_raw | 6 |  |  |  |  | FALSE |
| 4803 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 4804 | request\_\_external\_candidate\_ad\_\_price | 6 |  |  |  |  | FALSE |
| 4805 | request\_\_advertisements\_\_content\_right\_owner\_\_revenue | 6 |  |  |  |  | FALSE |
| 4806 | request\_\_global\_currency\_\_currencies\_\_network\_ids | 6 |  |  |  |  | FALSE |
| 4807 | request\_\_advertisements\_\_ad\_network\_list | 6 |  |  |  |  | FALSE |
| 4808 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 4809 | request\_\_audience\_item\_\_deprecate | 6 |  |  |  |  | FALSE |
| 4810 | acks\_\_metrics\_\_raw\_implicit\_no\_ad\_view | 6 |  |  |  |  | FALSE |
| 4811 | acks\_\_deprecate\_\_mid\_point | 6 |  |  |  |  | FALSE |
| 4812 | request\_\_slots\_\_avails\_metrics\_\_opportunity | 6 |  |  |  |  | FALSE |
| 4813 | request\_\_slots\_\_resellers\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 4814 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_clearing\_revenue | 6 |  |  |  |  | FALSE |
| 4815 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4816 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4817 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 6 |  |  |  |  | FALSE |
| 4818 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4819 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_id | 6 |  |  |  |  | FALSE |
| 4820 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 4821 | acks\_\_metrics\_\_can\_quartile | 6 |  |  |  |  | FALSE |
| 4822 | request\_\_outbound\_traffic\_control\_stats\_\_error\_code | 6 |  |  |  |  | FALSE |
| 4823 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 6 |  |  |  |  | FALSE |
| 4824 | request\_\_external\_candidate\_ad\_\_global\_agency\_ids | 6 |  |  |  |  | FALSE |
| 4825 | request\_\_slots\_\_forecast\_avails\_metrics\_\_remaining\_avails\_with\_forecast\_factor | 6 |  |  |  |  | FALSE |
| 4826 | request\_\_slots\_\_listing\_id\_raw | 6 |  |  |  |  | FALSE |
| 4827 | request\_\_bidding\_context\_\_bid\_request\_\_global\_auction\_id | 6 |  |  |  |  | FALSE |
| 4828 | acks\_\_keys\_\_is\_faked | 6 |  |  |  |  | FALSE |
| 4829 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value | 6 |  |  |  |  | FALSE |
| 4830 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4831 | request\_\_rtb\_auction\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4832 | request\_\_advertisements\_\_global\_brand\_ids | 6 |  |  |  |  | FALSE |
| 4833 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 6 |  |  |  |  | FALSE |
| 4834 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4835 | acks\_\_metrics\_\_raw\_ad\_collapse | 6 |  |  |  |  | FALSE |
| 4836 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key | 6 |  |  |  |  | FALSE |
| 4837 | request\_\_audience\_item | 6 |  |  |  |  | FALSE |
| 4838 | request\_\_advertisements\_\_network\_\_content\_owner\_network\_id | 6 |  |  |  |  | FALSE |
| 4839 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_key | 6 |  |  |  |  | FALSE |
| 4840 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4841 | request\_\_advertisements\_\_network\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4842 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_transactional\_key | 6 |  |  |  |  | FALSE |
| 4843 | request\_\_advertisements\_\_reseller\_\_up\_revenue | 6 |  |  |  |  | FALSE |
| 4844 | request\_\_bidding\_context\_\_bid\_request\_\_impression\_\_currency | 6 |  |  |  |  | FALSE |
| 4845 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 4846 | request\_\_outbound\_traffic\_control\_stats\_\_mpe\_seller\_network\_id | 6 |  |  |  |  | FALSE |
| 4847 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_source\_signal\_with\_waterfall\_\_authorized\_networks | 6 |  |  |  |  | FALSE |
| 4848 | forecast\_\_meta\_\_vnode\_id | 6 |  |  |  |  | FALSE |
| 4849 | request\_\_external\_candidate\_ad\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4850 | request\_\_advertisements\_\_external\_reseller\_\_bidding\_up\_modified\_revenue | 6 |  |  |  |  | FALSE |
| 4851 | request\_\_auction\_network\_contexts\_\_site\_domain | 6 |  |  |  |  | FALSE |
| 4852 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4853 | request\_\_errors\_\_site\_id\_raw | 6 |  |  |  |  | FALSE |
| 4854 | request\_\_slots\_\_outbound\_order\_\_active\_term\_ids | 6 |  |  |  |  | FALSE |
| 4855 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 6 |  |  |  |  | FALSE |
| 4856 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 6 |  |  |  |  | FALSE |
| 4857 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 4858 | request\_\_advertisements\_\_active\_audience\_item\_id\_raw | 6 |  |  |  |  | FALSE |
| 4859 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_channel\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4860 | request\_\_visitor\_\_flags | 6 |  |  |  |  | FALSE |
| 4861 | request\_\_advertisements\_\_replaced\_ad\_network\_id | 6 |  |  |  |  | FALSE |
| 4862 | request\_\_advertisements\_\_content\_right\_owner\_\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 4863 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4864 | request\_\_advertisements\_\_billable\_rate\_denominator\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 4865 | request\_\_rtb\_auction\_\_buyer\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4866 | request\_\_context\_\_ux\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4867 | request\_\_advertisements\_\_external\_reseller\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 4868 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics | 6 |  |  |  |  | FALSE |
| 4869 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_series\_id | 6 |  |  |  |  | FALSE |
| 4870 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_forecasted\_to\_deliver | 6 |  |  |  |  | FALSE |
| 4871 | request\_\_slots\_\_resellers\_\_outbound\_order\_\_order\_id\_raw | 6 |  |  |  |  | FALSE |
| 4872 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4873 | ack\_\_cpx\_derived\_abstract\_event\_id | 6 |  |  |  |  | FALSE |
| 4874 | request\_\_advertisements\_\_content\_right\_owner\_\_rule\_ext\_id | 6 |  |  |  |  | FALSE |
| 4875 | request\_\_advertisements\_\_priority | 6 |  |  |  |  | FALSE |
| 4876 | request\_\_advertisements\_\_validation\_event\_\_denominator\_event\_id | 6 |  |  |  |  | FALSE |
| 4877 | request\_\_advertisements\_\_scenario\_id | 6 |  |  |  |  | FALSE |
| 4878 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4879 | request\_\_advertisements\_\_external\_reseller\_\_margin | 6 |  |  |  |  | FALSE |
| 4880 | request\_\_context\_\_asset\_chain\_\_content\_right\_owner\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 4881 | acks\_\_ivt\_tracked\_info\_\_ivt\_not\_dedup\_reason | 6 |  |  |  |  | FALSE |
| 4882 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4883 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4884 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 4885 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_asset\_group\_id | 6 |  |  |  |  | FALSE |
| 4886 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 6 |  |  |  |  | FALSE |
| 4887 | acks\_\_timestamp | 6 |  |  |  |  | FALSE |
| 4888 | request\_\_outbound\_traffic\_control\_stats | 6 |  |  |  |  | FALSE |
| 4889 | request\_\_advertisements\_\_validation\_event\_\_denominator\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 4890 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 4891 | request\_\_rtb\_auction\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4892 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4893 | acks\_\_clearing\_price\_revenue\_chain\_\_reseller\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4894 | request\_\_advertisements\_\_rendition\_id\_raw | 6 |  |  |  |  | FALSE |
| 4895 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_value\_\_key | 6 |  |  |  |  | FALSE |
| 4896 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails\_\_value | 6 |  |  |  |  | FALSE |
| 4897 | request\_\_context\_\_video\_cro\_context\_id\_raw | 6 |  |  |  |  | FALSE |
| 4898 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 4899 | forecast\_\_metrics\_\_portfolio\_map\_\_key\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4900 | request\_\_advertisements\_\_distributor\_\_root\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4901 | request\_\_advertisements\_\_video\_resolution | 6 |  |  |  |  | FALSE |
| 4902 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 4903 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 4904 | request\_\_advertisements\_\_network\_\_series\_id | 6 |  |  |  |  | FALSE |
| 4905 | aim\_info\_\_aim\_identity\_info\_\_id\_graphs\_\_flag | 6 |  |  |  |  | FALSE |
| 4906 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 6 |  |  |  |  | FALSE |
| 4907 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4908 | request\_\_slots\_\_resellers\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4909 | acks\_\_networks | 6 |  |  |  |  | FALSE |
| 4910 | request\_\_external\_candidate\_ad\_\_mbd\_deduction\_on\_selection\_ratio | 6 |  |  |  |  | FALSE |
| 4911 | request\_\_external\_candidate\_ad\_\_external\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4912 | request\_\_external\_candidate\_ad\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 4913 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4914 | request\_\_advertisements\_\_external\_reseller\_\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4915 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_parent | 6 |  |  |  |  | FALSE |
| 4916 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 6 |  |  |  |  | FALSE |
| 4917 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 6 |  |  |  |  | FALSE |
| 4918 | request\_\_slots\_\_resellers\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 6 |  |  |  |  | FALSE |
| 4919 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 6 |  |  |  |  | FALSE |
| 4920 | request\_\_network\_ctx\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4921 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 6 |  |  |  |  | FALSE |
| 4922 | aim\_info\_\_aim\_audience\_info\_\_id | 6 |  |  |  |  | FALSE |
| 4923 | request\_\_advertisements\_\_content\_owner\_\_marketplace\_audience\_extension\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4924 | acks\_\_pingback\_pixel\_id | 6 |  |  |  |  | FALSE |
| 4925 | request\_\_network\_execution\_ctx\_\_pre\_targeting\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4926 | request\_\_audience\_item\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 4927 | acks\_\_metrics\_\_implicit\_no\_ad\_view | 6 |  |  |  |  | FALSE |
| 4928 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_pretty\_dimension\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4929 | acks\_\_metrics\_\_raw\_measurable\_ad\_close\_impression | 6 |  |  |  |  | FALSE |
| 4930 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 6 |  |  |  |  | FALSE |
| 4931 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 6 |  |  |  |  | FALSE |
| 4932 | request\_\_advertisements\_\_content\_right\_owner\_\_supply\_distribution\_cost | 6 |  |  |  |  | FALSE |
| 4933 | request\_\_advertisements\_\_replaced\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 4934 | request\_\_slots\_\_resellers\_\_outbound\_order | 6 |  |  |  |  | FALSE |
| 4935 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 4936 | request\_\_rtb\_auction\_\_external\_network\_id | 6 |  |  |  |  | FALSE |
| 4937 | request\_\_audience\_item\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4938 | acks\_\_ivt\_tracked\_info\_\_ivt\_not\_rewind\_reason | 6 |  |  |  |  | FALSE |
| 4939 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_key\_\_cpt\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4940 | request\_\_slots\_\_attrition\_ratio\_\_event\_ratio\_\_concrete\_event\_id\_raw | 6 |  |  |  |  | FALSE |
| 4941 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 4942 | forecast\_\_metrics\_\_transactional\_exclusivity\_competing\_map\_\_cpt\_value\_\_is\_scheduled | 6 |  |  |  |  | FALSE |
| 4943 | request\_\_context\_\_site\_section\_cro\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4944 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 6 |  |  |  |  | FALSE |
| 4945 | request\_\_advertisements\_\_provider\_measured\_event\_id | 6 |  |  |  |  | FALSE |
| 4946 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4947 | request\_\_rtb\_auction\_\_privacy\_flags | 6 |  |  |  |  | FALSE |
| 4948 | request\_\_slots\_\_time\_position\_sequence | 6 |  |  |  |  | FALSE |
| 4949 | request\_\_advertisements\_\_content\_right\_owner\_\_site\_section\_group\_id | 6 |  |  |  |  | FALSE |
| 4950 | request\_\_context\_\_time\_span\_\_key | 6 |  |  |  |  | FALSE |
| 4951 | request\_\_scores\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4952 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_airing\_id | 6 |  |  |  |  | FALSE |
| 4953 | request\_\_network\_ue\_ratio | 6 |  |  |  |  | FALSE |
| 4954 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 4955 | request\_\_context\_\_asset\_chain\_\_distributor\_\_airing\_channel\_id | 6 |  |  |  |  | FALSE |
| 4956 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails | 6 |  |  |  |  | FALSE |
| 4957 | request\_\_errors\_\_domain | 6 |  |  |  |  | FALSE |
| 4958 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 6 |  |  |  |  | FALSE |
| 4959 | request\_\_advertisements\_\_content\_right\_owner\_\_down\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 4960 | request\_\_external\_candidate\_ad\_\_rtb\_impression\_index | 6 |  |  |  |  | FALSE |
| 4961 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 6 |  |  |  |  | FALSE |
| 4962 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 4963 | request\_\_advertisements\_\_rules\_\_win\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 4964 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 6 |  |  |  |  | FALSE |
| 4965 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_value | 6 |  |  |  |  | FALSE |
| 4966 | request\_\_advertisements\_\_reseller\_\_down\_revenue | 6 |  |  |  |  | FALSE |
| 4967 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 4968 | request\_\_errors\_\_partner | 6 |  |  |  |  | FALSE |
| 4969 | request\_\_errors\_\_series\_id\_raw | 6 |  |  |  |  | FALSE |
| 4970 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_channel\_id | 6 |  |  |  |  | FALSE |
| 4971 | request\_\_rtb\_auction\_\_auction\_network\_to\_eur\_exchange\_rate | 6 |  |  |  |  | FALSE |
| 4972 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_audience\_item\_id | 6 |  |  |  |  | FALSE |
| 4973 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 6 |  |  |  |  | FALSE |
| 4974 | forecast\_\_metrics\_\_transactional\_demo\_map\_\_key\_\_ad\_id | 6 |  |  |  |  | FALSE |
| 4975 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 4976 | request\_\_system\_degradation | 6 |  |  |  |  | FALSE |
| 4977 | request\_\_advertisements\_\_content\_right\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 4978 | request\_\_rtb\_auction\_\_deal\_\_internal\_deal\_id\_raw | 6 |  |  |  |  | FALSE |
| 4979 | acks\_\_keys\_\_is\_callback\_faked\_slot\_impression | 6 |  |  |  |  | FALSE |
| 4980 | request\_\_decision\_info\_\_candidates\_info\_\_id | 6 |  |  |  |  | FALSE |
| 4981 | request\_\_context\_\_site\_section\_chain\_\_content\_owner\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4982 | request\_\_context\_\_site\_section\_chain\_\_content\_right\_owner\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 4983 | request\_\_context\_\_header\_bidding\_\_key\_value\_\_key | 6 |  |  |  |  | FALSE |
| 4984 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 6 |  |  |  |  | FALSE |
| 4985 | request\_\_errors\_\_site\_section\_id\_raw | 6 |  |  |  |  | FALSE |
| 4986 | request\_\_advertisements\_\_variant\_rendition\_ids\_raw | 6 |  |  |  |  | FALSE |
| 4987 | request\_\_advertisements\_\_content\_owner\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id\_raw | 6 |  |  |  |  | FALSE |
| 4988 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_ad\_id\_raw | 6 |  |  |  |  | FALSE |
| 4989 | request\_\_slots\_\_compatible\_dimensions | 6 |  |  |  |  | FALSE |
| 4990 | request\_\_advertisements\_\_distributor\_\_competition\_resellers | 6 |  |  |  |  | FALSE |
| 4991 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 4992 | request\_\_advertisements\_\_distributor\_\_reseller\_index\_in\_slot | 6 |  |  |  |  | FALSE |
| 4993 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_asset\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 4994 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos | 6 |  |  |  |  | FALSE |
| 4995 | request\_\_rtb\_auction\_\_bid\_throttling\_exempt\_ratio | 6 |  |  |  |  | FALSE |
| 4996 | request\_\_slots\_\_normalized\_ad\_unit\_id\_raw | 6 |  |  |  |  | FALSE |
| 4997 | request\_\_advertisements\_\_agency\_id\_raw | 6 |  |  |  |  | FALSE |
| 4998 | request\_\_slots\_\_slot\_context | 6 |  |  |  |  | FALSE |
| 4999 | forecast\_\_metrics\_\_transactional\_competing\_map\_\_cpt\_value\_\_win\_lose | 6 |  |  |  |  | FALSE |
| 5000 | forecast\_\_metrics\_\_portfolio\_competing\_map\_\_cpt\_key\_\_portfolio\_key\_\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 5001 | acks\_\_psn\_msg\_\_spot\_provider\_id | 6 |  |  |  |  | FALSE |
| 5002 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics | 6 |  |  |  |  | FALSE |
| 5003 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 6 |  |  |  |  | FALSE |
| 5004 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 5005 | request\_\_slots\_\_eligible\_carriage\_listing\_split\_unit\_ids\_raw | 6 |  |  |  |  | FALSE |
| 5006 | acks\_\_start\_time\_position | 6 |  |  |  |  | FALSE |
| 5007 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 6 |  |  |  |  | FALSE |
| 5008 | request\_\_rtb\_auction\_\_impression\_\_slot\_index | 6 |  |  |  |  | FALSE |
| 5009 | request\_\_slots\_\_inbound\_rule\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 5010 | request\_\_slots\_\_avail\_type | 6 |  |  |  |  | FALSE |
| 5011 | acks\_\_deprecate\_\_slot\_impression | 6 |  |  |  |  | FALSE |
| 5012 | request\_\_external\_candidate\_ad\_\_network\_execution\_ctx\_index | 6 |  |  |  |  | FALSE |
| 5013 | acks\_\_metrics\_\_raw\_slot\_impression | 6 |  |  |  |  | FALSE |
| 5014 | idx\_\_batch\_id | 6 |  |  |  |  | FALSE |
| 5015 | request\_\_slots\_\_initial\_num\_ads | 6 |  |  |  |  | FALSE |
| 5016 | request\_\_callback\_counters\_for\_wasted\_inventory | 6 |  |  |  |  | FALSE |
| 5017 | request\_\_advertisements\_\_recommended\_bidding\_price | 6 |  |  |  |  | FALSE |
| 5018 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics | 6 |  |  |  |  | FALSE |
| 5019 | request\_\_advertisements\_\_distributor\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 5020 | acks\_\_metrics\_\_raw\_ad\_unmute | 6 |  |  |  |  | FALSE |
| 5021 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_phase\_metrics\_\_name | 6 |  |  |  |  | FALSE |
| 5022 | request\_\_slots\_\_attrition\_ratio\_\_event\_ratio\_\_position\_ratio | 6 |  |  |  |  | FALSE |
| 5023 | request\_\_advertisements\_\_replaced\_io\_id\_raw | 6 |  |  |  |  | FALSE |
| 5024 | request\_\_advertisements\_\_content\_right\_owner\_\_inbound\_rule\_id\_raw | 6 |  |  |  |  | FALSE |
| 5025 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 6 |  |  |  |  | FALSE |
| 5026 | acks\_\_insertion\_status | 6 |  |  |  |  | FALSE |
| 5027 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 6 |  |  |  |  | FALSE |
| 5028 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 5029 | aim\_info\_\_aim\_identity\_info\_\_signal\_combination\_graph\_map\_\_network\_id | 6 |  |  |  |  | FALSE |
| 5030 | acks\_\_user\_id | 6 |  |  |  |  | FALSE |
| 5031 | request\_\_advertisements\_\_reseller\_\_inbound\_rule\_id | 6 |  |  |  |  | FALSE |
| 5032 | request\_\_context\_\_tv\_network\_group\_id | 6 |  |  |  |  | FALSE |
| 5033 | request\_\_slots\_\_resellers\_\_carriage\_listing\_split\_unit\_id | 6 |  |  |  |  | FALSE |
| 5034 | request\_\_advertisements\_\_reseller\_\_site\_section\_group\_id\_raw | 6 |  |  |  |  | FALSE |
| 5035 | request\_\_network\_attribute\_\_id\_graph\_\_policy\_\_alias | 6 |  |  |  |  | FALSE |
| 5036 | request\_\_advertisements\_\_validation\_event\_\_concrete\_event\_group\_id | 6 |  |  |  |  | FALSE |
| 5037 | acks\_\_clearing\_price\_revenue\_chain\_\_distributor\_\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 5038 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_booked\_impression | 6 |  |  |  |  | FALSE |
| 5039 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 6 |  |  |  |  | FALSE |
| 5040 | request\_\_slots\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 6 |  |  |  |  | FALSE |
| 5041 | request\_\_advertisements\_\_external\_reseller\_\_root\_asset\_group | 6 |  |  |  |  | FALSE |
| 5042 | request\_\_slots\_\_pod\_group\_id | 6 |  |  |  |  | FALSE |
| 5043 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails\_committed\_\_value | 6 |  |  |  |  | FALSE |
| 5044 | request\_\_advertisements\_\_yield\_optimization\_effective\_term\_ids | 6 |  |  |  |  | FALSE |
| 5045 | request\_\_rtb\_auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags | 6 |  |  |  |  | FALSE |
| 5046 | request\_\_advertisements\_\_reseller\_\_unified\_rule\_priority | 6 |  |  |  |  | FALSE |
| 5047 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_network\_id | 6 |  |  |  |  | FALSE |
| 5048 | request\_\_context\_\_asset\_chain\_\_content\_owner\_\_airing\_channel\_group\_id | 6 |  |  |  |  | FALSE |
| 5049 | deprecate | 6 |  |  |  |  | FALSE |
| 5050 | acks\_\_metrics\_\_raw\_error | 6 |  |  |  |  | FALSE |
| 5051 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 6 |  |  |  |  | FALSE |
| 5052 | request\_\_advertisements\_\_replaced\_io\_id | 6 |  |  |  |  | FALSE |
| 5053 | request\_\_advertisements\_\_reseller\_\_down\_network\_id | 6 |  |  |  |  | FALSE |
| 5054 | request\_\_rtb\_auction\_\_mkpl\_partner\_tags\_\_strategy | 6 |  |  |  |  | FALSE |
| 5055 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 5056 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 6 |  |  |  |  | FALSE |
| 5057 | request\_\_network\_execution\_ctx\_\_inventory\_\_mapped\_site\_section\_ids | 6 |  |  |  |  | FALSE |
| 5058 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_rbp\_dimension | 6 |  |  |  |  | FALSE |
| 5059 | request\_\_slots\_\_resellers\_\_inbound\_listing\_id | 6 |  |  |  |  | FALSE |
| 5060 | request\_\_slots\_\_resellers\_\_root\_section\_id | 6 |  |  |  |  | FALSE |
| 5061 | request\_\_network\_execution\_ctx\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids\_raw | 6 |  |  |  |  | FALSE |
| 5062 | request\_\_auction\_network\_contexts\_\_prog\_device\_type | 6 |  |  |  |  | FALSE |
| 5063 | request\_\_yield\_optimization\_ids\_\_optimization\_ids\_raw | 6 |  |  |  |  | FALSE |
| 5064 | request\_\_advertisements\_\_global\_industry\_ids | 6 |  |  |  |  | FALSE |
| 5065 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 6 |  |  |  |  | FALSE |
| 5066 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filtering\_metrics | 6 |  |  |  |  | FALSE |
| 5067 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_custom\_portfolio\_key\_\_network\_id | 6 |  |  |  |  | FALSE |
| 5068 | request\_\_advertisements\_\_content\_owner\_\_up\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 5069 | request\_\_advertisements\_\_reseller\_\_outbound\_order\_index | 6 |  |  |  |  | FALSE |
| 5070 | request\_\_context\_\_tv\_network\_id\_raw | 6 |  |  |  |  | FALSE |
| 5071 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_asset\_id\_raw | 6 |  |  |  |  | FALSE |
| 5072 | forecast\_\_metrics\_\_portfolio\_map\_\_value\_\_net\_avails\_committed | 6 |  |  |  |  | FALSE |
| 5073 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_order\_id | 6 |  |  |  |  | FALSE |
| 5074 | aim\_info\_\_aim\_identity\_info\_\_signal\_combination\_graph\_map | 6 |  |  |  |  | FALSE |
| 5075 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 6 |  |  |  |  | FALSE |
| 5076 | request\_\_advertisements\_\_active\_term\_id | 6 |  |  |  |  | FALSE |
| 5077 | acks\_\_win\_notice\_error | 6 |  |  |  |  | FALSE |
| 5078 | request\_\_errors\_\_site\_id | 6 |  |  |  |  | FALSE |
| 5079 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_key\_\_bucket | 6 |  |  |  |  | FALSE |
| 5080 | acks\_\_kafka\_msg\_size | 6 |  |  |  |  | FALSE |
| 5081 | request\_\_advertisements\_\_reseller\_\_bidding\_up\_modified\_revenue | 6 |  |  |  |  | FALSE |
| 5082 | request\_\_context\_\_site\_section\_chain\_\_inventory\_context\_\_network\_ctx\_index | 6 |  |  |  |  | FALSE |
| 5083 | request\_\_advertisements\_\_network\_\_mkpl\_info\_\_ad\_outbound\_order\_\_unified\_priority\_\_priority\_tier | 6 |  |  |  |  | FALSE |
| 5084 | request\_\_global\_currency\_\_currencies\_\_exchange\_rates | 6 |  |  |  |  | FALSE |
| 5085 | request\_\_external\_candidate\_ad\_\_zone\_id | 6 |  |  |  |  | FALSE |
| 5086 | request\_\_network\_audience\_items\_\_tracked\_audience\_item\_ids\_raw | 6 |  |  |  |  | FALSE |
| 5087 | forecast\_\_meta\_csv | 6 |  |  |  |  | FALSE |
| 5088 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 6 |  |  |  |  | FALSE |
| 5089 | request\_\_slots\_\_carriage\_inventory\_owner\_id\_raw | 6 |  |  |  |  | FALSE |
| 5090 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 6 |  |  |  |  | FALSE |
| 5091 | request\_\_context\_\_header\_bidding\_\_transaction\_id | 6 |  |  |  |  | FALSE |
| 5092 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 6 |  |  |  |  | FALSE |
| 5093 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 6 |  |  |  |  | FALSE |
| 5094 | request\_\_advertisements\_\_distributor\_\_supply\_acquisition\_cost | 6 |  |  |  |  | FALSE |
| 5095 | acks\_\_clearing\_price\_revenue\_chain\_\_content\_right\_owner\_\_network\_id | 6 |  |  |  |  | FALSE |
| 5096 | request\_\_rtb\_auction\_\_error | 6 |  |  |  |  | FALSE |
| 5097 | request\_\_advertisements\_\_ad\_unit\_id | 6 |  |  |  |  | FALSE |
| 5098 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 5099 | request\_\_context\_\_site\_section\_chain\_\_distributor\_\_context\_id | 6 |  |  |  |  | FALSE |
| 5100 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 6 |  |  |  |  | FALSE |
| 5101 | request\_\_rtb\_auction\_\_site\_id | 6 |  |  |  |  | FALSE |
| 5102 | request\_\_rtb\_auction\_\_deal\_\_slot\_index | 6 |  |  |  |  | FALSE |
| 5103 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 6 |  |  |  |  | FALSE |
| 5104 | forecast\_\_meta\_\_template\_id | 6 |  |  |  |  | FALSE |
| 5105 | forecast\_\_metrics\_\_custom\_portfolio\_competing\_map\_\_cpt\_value\_\_is\_guaranteed | 6 |  |  |  |  | FALSE |
| 5106 | request\_\_bidding\_context\_\_bid\_request\_\_deal\_\_impression\_index | 6 |  |  |  |  | FALSE |
| 5107 | forecast\_\_metrics\_\_transactional\_scheduled\_competing\_map\_\_cpt\_value\_\_lose\_win | 6 |  |  |  |  | FALSE |
| 5108 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_value\_\_net\_avails\_\_key | 6 |  |  |  |  | FALSE |
| 5109 | forecast\_\_metrics\_\_custom\_portfolio\_map\_\_key\_\_pretty\_dimension\_ids\_raw | 6 |  |  |  |  | FALSE |
| 5110 | request\_\_rtb\_auction\_\_device\_type | 6 |  |  |  |  | FALSE |
| 5111 | request\_\_slots\_\_content\_type | 6 |  |  |  |  | FALSE |
| 5112 | request\_\_slots\_\_resellers\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_programmatic\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 6 |  |  |  |  | FALSE |
| 5113 | request\_\_network\_execution\_ctx\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_partner\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 6 |  |  |  |  | FALSE |
| 5114 | request\_\_slots\_\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_direct\_sold\_metrics\_\_ad\_filling\_metrics\_\_undefined | 6 |  |  |  |  | FALSE |
| 5115 | candidate\_\_exchange\_order\_id | 5 |  |  |  |  | FALSE |
| 5116 | auction\_\_bid\_throttling\_info\_\_model\_info | 5 |  |  |  |  | FALSE |
| 5117 | partners\_\_upstream\_inbound\_order\_id | 5 |  |  |  |  | FALSE |
| 5118 | ack\_\_slot\_id | 5 |  |  |  |  | FALSE |
| 5119 | slot\_\_ad\_units | 5 |  |  |  |  | FALSE |
| 5120 | auction\_\_impression\_\_deals\_\_slot\_index | 5 |  |  |  |  | FALSE |
| 5121 | advertisement\_\_replaced\_ad\_id | 5 |  |  |  |  | FALSE |
| 5122 | advertisement\_\_replaced\_ad\_unit\_id | 5 |  |  |  |  | FALSE |
| 5123 | slot\_\_inbound\_rule\_\_win\_inbound\_rule\_id | 5 |  |  |  |  | FALSE |
| 5124 | advertisement\_\_replaced\_io\_id | 5 |  |  |  |  | FALSE |
| 5125 | slot\_\_custom\_id | 5 |  |  |  |  | FALSE |
| 5126 | slot\_\_listing\_id | 5 |  |  |  |  | FALSE |
| 5127 | advertisement\_\_replaced\_campaign\_id | 5 |  |  |  |  | FALSE |
| 5128 | candidate\_\_universal\_ad\_id | 5 |  |  |  |  | FALSE |
| 5129 | auction\_\_bid\_throttling\_info\_\_level | 5 |  |  |  |  | FALSE |
| 5130 | auction\_\_impression\_\_deals | 4 |  |  |  |  | FALSE |
| 5131 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | 4 |  |  |  |  | FALSE |
| 5132 | partners\_\_matched\_key\_value\_ids | 4 |  |  |  |  | FALSE |
| 5133 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 4 |  |  |  |  | FALSE |
| 5134 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5135 | slot\_\_outbound\_order\_\_order\_id | 4 |  |  |  |  | FALSE |
| 5136 | partners\_\_ad\_filling\_status\_\_available\_duration | 4 |  |  |  |  | FALSE |
| 5137 | partners\_\_standard\_content\_series\_visibility | 4 |  |  |  |  | FALSE |
| 5138 | partners\_\_geo\_state\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5139 | partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5140 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined | 4 |  |  |  |  | FALSE |
| 5141 | partners\_\_geo\_zip\_code\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5142 | partners\_\_custom\_platform\_ids | 4 |  |  |  |  | FALSE |
| 5143 | partners\_\_geo\_zip\_code\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5144 | auction\_\_impression\_\_deals\_\_auction\_type | 4 |  |  |  |  | FALSE |
| 5145 | auction\_\_experiment | 4 |  |  |  |  | FALSE |
| 5146 | partners\_\_geo\_zip\_code\_visibility | 4 |  |  |  |  | FALSE |
| 5147 | partners\_\_content\_rating\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5148 | partners\_\_airing\_id | 4 |  |  |  |  | FALSE |
| 5149 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 4 |  |  |  |  | FALSE |
| 5150 | partners\_\_distributor\_bidding\_revenue | 4 |  |  |  |  | FALSE |
| 5151 | partners\_\_bidder\_seat\_id | 4 |  |  |  |  | FALSE |
| 5152 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 4 |  |  |  |  | FALSE |
| 5153 | partners\_\_standard\_language\_visibility | 4 |  |  |  |  | FALSE |
| 5154 | partners\_\_third\_party\_user\_id\_visibility | 4 |  |  |  |  | FALSE |
| 5155 | partners\_\_standard\_genre\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5156 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 4 |  |  |  |  | FALSE |
| 5157 | partners\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked | 4 |  |  |  |  | FALSE |
| 5158 | auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index | 4 |  |  |  |  | FALSE |
| 5159 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase | 4 |  |  |  |  | FALSE |
| 5160 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 4 |  |  |  |  | FALSE |
| 5161 | partners\_\_standard\_content\_series\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5162 | auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids | 4 |  |  |  |  | FALSE |
| 5163 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 4 |  |  |  |  | FALSE |
| 5164 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 4 |  |  |  |  | FALSE |
| 5165 | auction\_\_impression\_\_deals\_\_order\_id | 4 |  |  |  |  | FALSE |
| 5166 | partners\_\_priority\_tier | 4 |  |  |  |  | FALSE |
| 5167 | partners\_\_programmatic\_exchange\_rate\_to\_eur | 4 |  |  |  |  | FALSE |
| 5168 | partners\_\_eligible\_outbound\_orders\_\_bit\_flags | 4 |  |  |  |  | FALSE |
| 5169 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | 4 |  |  |  |  | FALSE |
| 5170 | partners\_\_device\_id\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5171 | partners\_\_standard\_genre\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5172 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 4 |  |  |  |  | FALSE |
| 5173 | partners\_\_standard\_genre\_visibility | 4 |  |  |  |  | FALSE |
| 5174 | partners\_\_geo\_dma\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5175 | partners\_\_geo\_dma\_visibility | 4 |  |  |  |  | FALSE |
| 5176 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 4 |  |  |  |  | FALSE |
| 5177 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 4 |  |  |  |  | FALSE |
| 5178 | auction\_\_ab\_test\_items\_\_is\_effective | 4 |  |  |  |  | FALSE |
| 5179 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 4 |  |  |  |  | FALSE |
| 5180 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5181 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration | 4 |  |  |  |  | FALSE |
| 5182 | partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails | 4 |  |  |  |  | FALSE |
| 5183 | partners\_\_ip\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5184 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 4 |  |  |  |  | FALSE |
| 5185 | auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id | 4 |  |  |  |  | FALSE |
| 5186 | partners\_\_selected\_yo\_volume\_cap\_ids | 4 |  |  |  |  | FALSE |
| 5187 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 4 |  |  |  |  | FALSE |
| 5188 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5189 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 4 |  |  |  |  | FALSE |
| 5190 | partners\_\_outbound\_order\_ids | 4 |  |  |  |  | FALSE |
| 5191 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name | 4 |  |  |  |  | FALSE |
| 5192 | partners\_\_inbound\_listing\_ids | 4 |  |  |  |  | FALSE |
| 5193 | partners\_\_standard\_programmer\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5194 | partners\_\_key\_value\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5195 | partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5196 | partners\_\_eligible\_outbound\_orders\_\_order\_transaction\_type | 4 |  |  |  |  | FALSE |
| 5197 | partners\_\_unified\_outbound\_order\_priority | 4 |  |  |  |  | FALSE |
| 5198 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 4 |  |  |  |  | FALSE |
| 5199 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 4 |  |  |  |  | FALSE |
| 5200 | partners\_\_geo\_country\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5201 | partners\_\_network\_is\_vod\_programmer | 4 |  |  |  |  | FALSE |
| 5202 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | 4 |  |  |  |  | FALSE |
| 5203 | partners\_\_eligible\_outbound\_orders\_\_down\_network\_id | 4 |  |  |  |  | FALSE |
| 5204 | auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index | 4 |  |  |  |  | FALSE |
| 5205 | partners\_\_standard\_content\_territory\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5206 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails | 4 |  |  |  |  | FALSE |
| 5207 | partners\_\_standard\_endpoint\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5208 | auction\_\_impression\_\_deals\_\_listing\_id | 4 |  |  |  |  | FALSE |
| 5209 | partners\_\_content\_form\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5210 | partners\_\_mapped\_asset\_ids | 4 |  |  |  |  | FALSE |
| 5211 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 4 |  |  |  |  | FALSE |
| 5212 | partners\_\_non\_tracked\_audience\_item\_ids | 4 |  |  |  |  | FALSE |
| 5213 | partners\_\_airing\_channel\_group\_id | 4 |  |  |  |  | FALSE |
| 5214 | partners\_\_outbound\_rules\_\_total\_opp | 4 |  |  |  |  | FALSE |
| 5215 | partners\_\_geo\_state\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5216 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | 4 |  |  |  |  | FALSE |
| 5217 | partners\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5218 | partners\_\_avails\_category\_\_unconstrained\_avails | 4 |  |  |  |  | FALSE |
| 5219 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 4 |  |  |  |  | FALSE |
| 5220 | partners\_\_outbound\_exchange\_listings\_\_avails\_metrics | 4 |  |  |  |  | FALSE |
| 5221 | auction\_\_is\_order\_prog\_auction | 4 |  |  |  |  | FALSE |
| 5222 | partners\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5223 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5224 | partners\_\_device\_id\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5225 | partners\_\_visitor\_custom\_id\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5226 | partners\_\_eligible\_outbound\_orders\_\_order\_type | 4 |  |  |  |  | FALSE |
| 5227 | partners\_\_upstream\_global\_currency\_id | 4 |  |  |  |  | FALSE |
| 5228 | partners\_\_unified\_rule\_priority | 4 |  |  |  |  | FALSE |
| 5229 | partners\_\_standard\_programmer\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5230 | partners\_\_geo\_state\_visibility | 4 |  |  |  |  | FALSE |
| 5231 | partners\_\_network\_selection\_info | 4 |  |  |  |  | FALSE |
| 5232 | partners\_\_eligible\_outbound\_orders\_\_sales\_channel | 4 |  |  |  |  | FALSE |
| 5233 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 4 |  |  |  |  | FALSE |
| 5234 | partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5235 | partners\_\_asset\_group\_id | 4 |  |  |  |  | FALSE |
| 5236 | auction\_\_external\_network\_id | 4 |  |  |  |  | FALSE |
| 5237 | partners\_\_margin | 4 |  |  |  |  | FALSE |
| 5238 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 4 |  |  |  |  | FALSE |
| 5239 | partners\_\_ad\_filling\_status | 4 |  |  |  |  | FALSE |
| 5240 | partners\_\_buyer\_ids | 4 |  |  |  |  | FALSE |
| 5241 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | 4 |  |  |  |  | FALSE |
| 5242 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 4 |  |  |  |  | FALSE |
| 5243 | partners\_\_marketplace\_audience\_extension\_deal\_ids | 4 |  |  |  |  | FALSE |
| 5244 | partners\_\_device\_id\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5245 | partners\_\_matched\_yield\_optimization\_ids | 4 |  |  |  |  | FALSE |
| 5246 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5247 | partners\_\_ip\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5248 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 4 |  |  |  |  | FALSE |
| 5249 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 4 |  |  |  |  | FALSE |
| 5250 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 4 |  |  |  |  | FALSE |
| 5251 | partners\_\_geo\_dma\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5252 | advertisement\_\_replaced\_rendition\_id | 4 |  |  |  |  | FALSE |
| 5253 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 4 |  |  |  |  | FALSE |
| 5254 | partners\_\_selected\_yo\_distribution\_id | 4 |  |  |  |  | FALSE |
| 5255 | partners\_\_content\_rating\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5256 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 4 |  |  |  |  | FALSE |
| 5257 | partners\_\_eligible\_outbound\_orders\_\_order\_id | 4 |  |  |  |  | FALSE |
| 5258 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | 4 |  |  |  |  | FALSE |
| 5259 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails | 4 |  |  |  |  | FALSE |
| 5260 | partners\_\_selected\_yield\_optimization\_ids | 4 |  |  |  |  | FALSE |
| 5261 | partners\_\_standard\_content\_territory\_visibility | 4 |  |  |  |  | FALSE |
| 5262 | partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5263 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 4 |  |  |  |  | FALSE |
| 5264 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails | 4 |  |  |  |  | FALSE |
| 5265 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | 4 |  |  |  |  | FALSE |
| 5266 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 4 |  |  |  |  | FALSE |
| 5267 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 4 |  |  |  |  | FALSE |
| 5268 | partners\_\_mapped\_site\_section\_ids | 4 |  |  |  |  | FALSE |
| 5269 | partners\_\_key\_value\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5270 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5271 | partners\_\_geo\_country\_visibility | 4 |  |  |  |  | FALSE |
| 5272 | partners\_\_ad\_priority\_bucket | 4 |  |  |  |  | FALSE |
| 5273 | auction\_\_media\_buyer\_id | 4 |  |  |  |  | FALSE |
| 5274 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 4 |  |  |  |  | FALSE |
| 5275 | partners\_\_avails\_category\_\_market\_avails | 4 |  |  |  |  | FALSE |
| 5276 | ack\_\_client\_facing\_ivt\_reason\_flag | 4 |  |  |  |  | FALSE |
| 5277 | partners\_\_geo\_city\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5278 | partners\_\_selected\_yo\_inventory\_prioritization\_id | 4 |  |  |  |  | FALSE |
| 5279 | partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id | 4 |  |  |  |  | FALSE |
| 5280 | auction\_\_execution\_contexts | 4 |  |  |  |  | FALSE |
| 5281 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 4 |  |  |  |  | FALSE |
| 5282 | partners\_\_geo\_city\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5283 | partners\_\_third\_party\_user\_id\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5284 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5285 | partners\_\_ip\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5286 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 4 |  |  |  |  | FALSE |
| 5287 | partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5288 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 4 |  |  |  |  | FALSE |
| 5289 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 4 |  |  |  |  | FALSE |
| 5290 | partners\_\_third\_party\_user\_id\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5291 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 4 |  |  |  |  | FALSE |
| 5292 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 4 |  |  |  |  | FALSE |
| 5293 | auction\_\_experiment\_\_experiment\_id | 4 |  |  |  |  | FALSE |
| 5294 | partners\_\_avails\_category\_\_vod\_programmer\_total\_avails | 4 |  |  |  |  | FALSE |
| 5295 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 4 |  |  |  |  | FALSE |
| 5296 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 4 |  |  |  |  | FALSE |
| 5297 | partners\_\_portfolio\_ids | 4 |  |  |  |  | FALSE |
| 5298 | auction\_\_is\_market\_auction | 4 |  |  |  |  | FALSE |
| 5299 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 4 |  |  |  |  | FALSE |
| 5300 | partners\_\_geo\_city\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5301 | partners\_\_avails\_category\_\_ssp\_avails | 4 |  |  |  |  | FALSE |
| 5302 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 4 |  |  |  |  | FALSE |
| 5303 | partners\_\_standard\_content\_daypart\_visibility | 4 |  |  |  |  | FALSE |
| 5304 | auction\_\_impression\_\_deals\_\_trading\_desk\_id | 4 |  |  |  |  | FALSE |
| 5305 | partners\_\_standard\_language\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5306 | partners\_\_outbound\_rules | 4 |  |  |  |  | FALSE |
| 5307 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5308 | partners\_\_content\_rating\_visibility | 4 |  |  |  |  | FALSE |
| 5309 | auction\_\_auction\_sampling | 4 |  |  |  |  | FALSE |
| 5310 | advertisement\_\_external\_vast\_ad\_id | 4 |  |  |  |  | FALSE |
| 5311 | partners\_\_rule\_flags | 4 |  |  |  |  | FALSE |
| 5312 | auction\_\_auction\_network\_context\_index | 4 |  |  |  |  | FALSE |
| 5313 | partners\_\_content\_form\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5314 | partners\_\_key\_value\_visibility | 4 |  |  |  |  | FALSE |
| 5315 | slot\_\_rules | 4 |  |  |  |  | FALSE |
| 5316 | partners\_\_user\_agent\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5317 | partners\_\_selected\_yield\_optimization\_info\_ids | 4 |  |  |  |  | FALSE |
| 5318 | partners\_\_eligible\_outbound\_orders\_\_avails\_category | 4 |  |  |  |  | FALSE |
| 5319 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 4 |  |  |  |  | FALSE |
| 5320 | auction\_\_trading\_desk\_id | 4 |  |  |  |  | FALSE |
| 5321 | partners\_\_count\_imp\_as\_booked | 4 |  |  |  |  | FALSE |
| 5322 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration | 4 |  |  |  |  | FALSE |
| 5323 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | 4 |  |  |  |  | FALSE |
| 5324 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails | 4 |  |  |  |  | FALSE |
| 5325 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 4 |  |  |  |  | FALSE |
| 5326 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 4 |  |  |  |  | FALSE |
| 5327 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 4 |  |  |  |  | FALSE |
| 5328 | partners\_\_standard\_content\_series\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5329 | partners\_\_geo\_state\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5330 | partners\_\_standard\_genre\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5331 | partners\_\_reseller\_bidding\_revenue | 4 |  |  |  |  | FALSE |
| 5332 | partners\_\_outbound\_order\_transaction\_type | 4 |  |  |  |  | FALSE |
| 5333 | auction\_\_execution\_contexts\_\_network\_execution\_ctx\_index | 4 |  |  |  |  | FALSE |
| 5334 | partners\_\_standard\_channel\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5335 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 4 |  |  |  |  | FALSE |
| 5336 | auction\_\_is\_ssp\_auction | 4 |  |  |  |  | FALSE |
| 5337 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids | 4 |  |  |  |  | FALSE |
| 5338 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5339 | auction\_\_is\_exchange\_auction | 4 |  |  |  |  | FALSE |
| 5340 | partners\_\_eligible\_outbound\_orders\_\_order\_priority | 4 |  |  |  |  | FALSE |
| 5341 | auction\_\_impression\_\_deals\_\_order\_type | 4 |  |  |  |  | FALSE |
| 5342 | partners\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5343 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails | 4 |  |  |  |  | FALSE |
| 5344 | auction\_\_buyer\_id | 4 |  |  |  |  | FALSE |
| 5345 | partners\_\_standard\_endpoint\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5346 | partners\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 4 |  |  |  |  | FALSE |
| 5347 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 4 |  |  |  |  | FALSE |
| 5348 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 4 |  |  |  |  | FALSE |
| 5349 | partners\_\_content\_rating\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5350 | partners\_\_user\_agent\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5351 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5352 | partners\_\_user\_agent\_visibility | 4 |  |  |  |  | FALSE |
| 5353 | partners\_\_standard\_brand\_visibility | 4 |  |  |  |  | FALSE |
| 5354 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 4 |  |  |  |  | FALSE |
| 5355 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 4 |  |  |  |  | FALSE |
| 5356 | auction\_\_ab\_test\_items | 4 |  |  |  |  | FALSE |
| 5357 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5358 | partners\_\_ad\_filling\_status\_\_initial\_filled\_duration | 4 |  |  |  |  | FALSE |
| 5359 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 4 |  |  |  |  | FALSE |
| 5360 | partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num | 4 |  |  |  |  | FALSE |
| 5361 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | 4 |  |  |  |  | FALSE |
| 5362 | partners\_\_visitor\_custom\_id\_visibility | 4 |  |  |  |  | FALSE |
| 5363 | partners\_\_standard\_content\_territory\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5364 | partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5365 | partners\_\_standard\_brand\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5366 | partners\_\_standard\_programmer\_visibility | 4 |  |  |  |  | FALSE |
| 5367 | candidate\_\_has\_advertisement | 4 |  |  |  |  | FALSE |
| 5368 | partners\_\_priority\_value | 4 |  |  |  |  | FALSE |
| 5369 | auction\_\_impression\_\_deals\_\_outbound\_order\_index | 4 |  |  |  |  | FALSE |
| 5370 | partners\_\_key\_value\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5371 | ack\_\_metrics\_\_hylda\_replacement\_impression\_forfeits | 4 |  |  |  |  | FALSE |
| 5372 | partners\_\_outbound\_exchange\_listings | 4 |  |  |  |  | FALSE |
| 5373 | partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration | 4 |  |  |  |  | FALSE |
| 5374 | partners\_\_device\_id\_visibility | 4 |  |  |  |  | FALSE |
| 5375 | partners\_\_eligible\_outbound\_orders | 4 |  |  |  |  | FALSE |
| 5376 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 4 |  |  |  |  | FALSE |
| 5377 | partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5378 | slot\_\_outbound\_order\_\_order\_type | 4 |  |  |  |  | FALSE |
| 5379 | auction\_\_impression\_\_deals\_\_buyers | 4 |  |  |  |  | FALSE |
| 5380 | partners\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5381 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 4 |  |  |  |  | FALSE |
| 5382 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails | 4 |  |  |  |  | FALSE |
| 5383 | partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails | 4 |  |  |  |  | FALSE |
| 5384 | partners\_\_matched\_daypart | 4 |  |  |  |  | FALSE |
| 5385 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 4 |  |  |  |  | FALSE |
| 5386 | auction\_\_bid\_to\_eur\_exchange\_rate | 4 |  |  |  |  | FALSE |
| 5387 | partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5388 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 4 |  |  |  |  | FALSE |
| 5389 | partners\_\_standard\_content\_daypart\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5390 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 4 |  |  |  |  | FALSE |
| 5391 | auction\_\_impression\_\_matched\_inventory\_package\_ids | 4 |  |  |  |  | FALSE |
| 5392 | auction\_\_impression\_\_deals\_\_media\_buyer\_id | 4 |  |  |  |  | FALSE |
| 5393 | partners\_\_opportunity\_id | 4 |  |  |  |  | FALSE |
| 5394 | auction\_\_impression\_\_error | 4 |  |  |  |  | FALSE |
| 5395 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 4 |  |  |  |  | FALSE |
| 5396 | partners\_\_selected\_yo\_distribution\_nip\_id | 4 |  |  |  |  | FALSE |
| 5397 | partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency | 4 |  |  |  |  | FALSE |
| 5398 | auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot | 4 |  |  |  |  | FALSE |
| 5399 | partners\_\_ad\_filling\_status\_\_filled\_duration | 4 |  |  |  |  | FALSE |
| 5400 | auction\_\_ab\_test\_item\_index | 4 |  |  |  |  | FALSE |
| 5401 | partners\_\_visitor\_custom\_id\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5402 | partners\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids | 4 |  |  |  |  | FALSE |
| 5403 | partners\_\_standard\_channel\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5404 | partners\_\_region\_ids | 4 |  |  |  |  | FALSE |
| 5405 | partners\_\_geo\_city\_visibility | 4 |  |  |  |  | FALSE |
| 5406 | partners\_\_rule\_ext\_id | 4 |  |  |  |  | FALSE |
| 5407 | partners\_\_inventory\_distribution\_contexts | 4 |  |  |  |  | FALSE |
| 5408 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 4 |  |  |  |  | FALSE |
| 5409 | partners\_\_competition\_resellers | 4 |  |  |  |  | FALSE |
| 5410 | partners\_\_outbound\_rules\_\_win\_opp | 4 |  |  |  |  | FALSE |
| 5411 | partners\_\_standard\_content\_daypart\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5412 | partners\_\_standard\_endpoint\_owner\_visibility | 4 |  |  |  |  | FALSE |
| 5413 | partners\_\_standard\_language\_visibility\_\_report\_aggregate | 4 |  |  |  |  | FALSE |
| 5414 | partners\_\_standard\_content\_credential\_status\_visibility | 4 |  |  |  |  | FALSE |
| 5415 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 4 |  |  |  |  | FALSE |
| 5416 | partners\_\_standard\_language\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5417 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 4 |  |  |  |  | FALSE |
| 5418 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 4 |  |  |  |  | FALSE |
| 5419 | partners\_\_geo\_country\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5420 | partners\_\_edge\_postal\_code\_package\_ids | 4 |  |  |  |  | FALSE |
| 5421 | partners\_\_outbound\_exchange\_order\_ids | 4 |  |  |  |  | FALSE |
| 5422 | partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5423 | partners\_\_break\_id | 4 |  |  |  |  | FALSE |
| 5424 | partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails | 4 |  |  |  |  | FALSE |
| 5425 | auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id | 4 |  |  |  |  | FALSE |
| 5426 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 4 |  |  |  |  | FALSE |
| 5427 | auction\_\_auction\_network\_to\_eur\_exchange\_rate | 4 |  |  |  |  | FALSE |
| 5428 | auction\_\_mkpl\_partner\_tags | 4 |  |  |  |  | FALSE |
| 5429 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 4 |  |  |  |  | FALSE |
| 5430 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 4 |  |  |  |  | FALSE |
| 5431 | partners\_\_inbound\_order\_auction\_type | 4 |  |  |  |  | FALSE |
| 5432 | auction\_\_impression\_\_deals\_\_is\_auction\_rule | 4 |  |  |  |  | FALSE |
| 5433 | partners\_\_geo\_dma\_visibility\_\_targetable | 4 |  |  |  |  | FALSE |
| 5434 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | 4 |  |  |  |  | FALSE |
| 5435 | partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 4 |  |  |  |  | FALSE |
| 5436 | partners\_\_standard\_brand\_visibility\_\_report\_event | 4 |  |  |  |  | FALSE |
| 5437 | partners\_\_site\_group\_id | 4 |  |  |  |  | FALSE |
| 5438 | advertisement\_\_external\_reseller\_\_asset\_group\_id | 3 |  |  |  |  | FALSE |
| 5439 | advertisement\_\_external\_reseller\_\_competition\_resellers | 3 |  |  |  |  | FALSE |
| 5440 | advertisement\_\_targeted\_ratio | 3 |  |  |  |  | FALSE |
| 5441 | advertisement\_\_rbp\_flag | 3 |  |  |  |  | FALSE |
| 5442 | advertisement\_\_unified\_yield\_\_replaced\_guaranteed\_ad\_id | 3 |  |  |  |  | FALSE |
| 5443 | advertisement\_\_advertisement\_context\_\_network\_execution\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5444 | advertisement\_\_external\_reseller\_\_unified\_rule\_priority\_\_sub\_priority\_value | 3 |  |  |  |  | FALSE |
| 5445 | candidate\_\_series\_id | 3 |  |  |  |  | FALSE |
| 5446 | advertisement\_\_variant\_creative\_ids | 3 |  |  |  |  | FALSE |
| 5447 | candidate\_\_creative\_approval\_request | 3 |  |  |  |  | FALSE |
| 5448 | candidate\_\_sfx\_buyer\_id | 3 |  |  |  |  | FALSE |
| 5449 | slot\_\_outbound\_order\_\_order\_priority | 3 |  |  |  |  | FALSE |
| 5450 | slot\_\_forecast\_avails\_metrics\_\_remaining\_avails | 3 |  |  |  |  | FALSE |
| 5451 | slot\_\_opportunity\_display\_id | 3 |  |  |  |  | FALSE |
| 5452 | advertisement\_\_contextual\_billings\_\_segment\_id | 3 |  |  |  |  | FALSE |
| 5453 | advertisement\_\_fallback\_ad\_uniq\_id | 3 |  |  |  |  | FALSE |
| 5454 | slot\_\_width | 3 |  |  |  |  | FALSE |
| 5455 | advertisement\_\_targeting\_criteria\_id | 3 |  |  |  |  | FALSE |
| 5456 | advertisement\_\_external\_reseller\_\_rule\_id | 3 |  |  |  |  | FALSE |
| 5457 | advertisement\_\_replaced\_ad\_bit\_flags | 3 |  |  |  |  | FALSE |
| 5458 | slot\_\_time\_position\_sequence | 3 |  |  |  |  | FALSE |
| 5459 | advertisement\_\_external\_reseller\_\_root\_section\_group | 3 |  |  |  |  | FALSE |
| 5460 | advertisement\_\_external\_reseller\_\_unified\_rule\_priority\_\_priority\_tier | 3 |  |  |  |  | FALSE |
| 5461 | candidate\_\_ortb\_fwpartners\_\_idvalue | 3 |  |  |  |  | FALSE |
| 5462 | ack\_\_metrics\_\_hylda\_replacement\_impression\_gains | 3 |  |  |  |  | FALSE |
| 5463 | advertisement\_\_is\_zero\_revenue | 3 |  |  |  |  | FALSE |
| 5464 | slot\_\_forecast\_avails\_metrics\_\_booked\_avails\_with\_forecast\_factor | 3 |  |  |  |  | FALSE |
| 5465 | advertisement\_\_rules\_flags | 3 |  |  |  |  | FALSE |
| 5466 | slot\_\_scheduled\_timestamp | 3 |  |  |  |  | FALSE |
| 5467 | advertisement\_\_validation\_event\_\_denominator\_event\_id | 3 |  |  |  |  | FALSE |
| 5468 | slot\_\_outbound\_order\_\_price | 3 |  |  |  |  | FALSE |
| 5469 | slot\_\_min\_bitrate | 3 |  |  |  |  | FALSE |
| 5470 | candidate\_\_discount\_barter\_\_amount | 3 |  |  |  |  | FALSE |
| 5471 | advertisement\_\_candidate\_index | 3 |  |  |  |  | FALSE |
| 5472 | candidate\_\_mpe\_deduction\_on\_selection\_fixed\_fee | 3 |  |  |  |  | FALSE |
| 5473 | slot\_\_outbound\_order\_\_order\_transaction\_type | 3 |  |  |  |  | FALSE |
| 5474 | advertisement\_\_matched\_daypart | 3 |  |  |  |  | FALSE |
| 5475 | advertisement\_\_external\_reseller\_\_site\_id | 3 |  |  |  |  | FALSE |
| 5476 | candidate\_\_zone\_id | 3 |  |  |  |  | FALSE |
| 5477 | advertisement\_\_inbound\_rule | 3 |  |  |  |  | FALSE |
| 5478 | slot\_\_creative\_api | 3 |  |  |  |  | FALSE |
| 5479 | candidate\_\_playlist\_response\_time | 3 |  |  |  |  | FALSE |
| 5480 | slot\_\_outbound\_order\_\_active\_aim\_audience\_ids | 3 |  |  |  |  | FALSE |
| 5481 | advertisement\_\_contextual\_billings | 3 |  |  |  |  | FALSE |
| 5482 | slot\_\_outbound\_order\_\_down\_reseller\_index | 3 |  |  |  |  | FALSE |
| 5483 | advertisement\_\_effective\_unified\_priority | 3 |  |  |  |  | FALSE |
| 5484 | advertisement\_\_validation\_event\_\_concrete\_event\_group\_id | 3 |  |  |  |  | FALSE |
| 5485 | slot\_\_avails\_metrics | 3 |  |  |  |  | FALSE |
| 5486 | advertisement\_\_external\_reseller\_\_root\_section\_id | 3 |  |  |  |  | FALSE |
| 5487 | advertisement\_\_external\_reseller\_\_series\_id | 3 |  |  |  |  | FALSE |
| 5488 | slot\_\_content\_right\_owner | 3 |  |  |  |  | FALSE |
| 5489 | slot\_\_slot\_context\_\_network\_execution\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5490 | advertisement\_\_external\_reseller\_\_count\_imp\_as\_booked | 3 |  |  |  |  | FALSE |
| 5491 | slot\_\_sfx\_avails | 3 |  |  |  |  | FALSE |
| 5492 | advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_ids | 3 |  |  |  |  | FALSE |
| 5493 | advertisement\_\_variant\_rendition\_ids | 3 |  |  |  |  | FALSE |
| 5494 | advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 3 |  |  |  |  | FALSE |
| 5495 | candidate\_\_creative\_approval\_request\_\_network\_id | 3 |  |  |  |  | FALSE |
| 5496 | advertisement\_\_unified\_yield\_\_uplift\_ecpm | 3 |  |  |  |  | FALSE |
| 5497 | advertisement\_\_external\_reseller\_\_flags | 3 |  |  |  |  | FALSE |
| 5498 | slot\_\_primary\_content\_type | 3 |  |  |  |  | FALSE |
| 5499 | slot\_\_rules\_\_win\_rule\_id | 3 |  |  |  |  | FALSE |
| 5500 | advertisement\_\_external\_reseller\_\_inbound\_rule\_id | 3 |  |  |  |  | FALSE |
| 5501 | candidate\_\_ortb\_fwpartners | 3 |  |  |  |  | FALSE |
| 5502 | candidate\_\_price\_type | 3 |  |  |  |  | FALSE |
| 5503 | candidate\_\_advertisement\_index | 3 |  |  |  |  | FALSE |
| 5504 | advertisement\_\_external\_reseller\_\_unified\_rule\_priority | 3 |  |  |  |  | FALSE |
| 5505 | slot\_\_inbound\_rule | 3 |  |  |  |  | FALSE |
| 5506 | advertisement\_\_external\_reseller\_\_ad\_priority\_bucket | 3 |  |  |  |  | FALSE |
| 5507 | slot\_\_avails\_metrics\_\_opportunity | 3 |  |  |  |  | FALSE |
| 5508 | slot\_\_avails\_metrics\_\_unfilled\_avails | 3 |  |  |  |  | FALSE |
| 5509 | slot\_\_break\_display\_id | 3 |  |  |  |  | FALSE |
| 5510 | advertisement\_\_external\_reseller\_\_down\_revenue | 3 |  |  |  |  | FALSE |
| 5511 | candidate\_\_bidding\_seat\_id | 3 |  |  |  |  | FALSE |
| 5512 | candidate\_\_creative\_approval\_request\_\_approval\_type | 3 |  |  |  |  | FALSE |
| 5513 | candidate\_\_creative\_approval\_request\_\_approval\_scope | 3 |  |  |  |  | FALSE |
| 5514 | advertisement\_\_unified\_yield\_\_substitute\_type | 3 |  |  |  |  | FALSE |
| 5515 | advertisement\_\_external\_reseller\_\_outbound\_order\_index | 3 |  |  |  |  | FALSE |
| 5516 | slot\_\_window\_duration | 3 |  |  |  |  | FALSE |
| 5517 | advertisement\_\_rules\_\_network\_id | 3 |  |  |  |  | FALSE |
| 5518 | advertisement\_\_replaced\_creative\_id | 3 |  |  |  |  | FALSE |
| 5519 | advertisement\_\_shading\_context\_\_bid\_floor\_price\_usd | 3 |  |  |  |  | FALSE |
| 5520 | advertisement\_\_ad\_opportunity\_rules\_\_total\_opp | 3 |  |  |  |  | FALSE |
| 5521 | advertisement\_\_is\_rbp | 3 |  |  |  |  | FALSE |
| 5522 | candidate\_\_ortb\_fwpartners\_\_idtype | 3 |  |  |  |  | FALSE |
| 5523 | advertisement\_\_external\_reseller\_\_bidding\_down\_revenue | 3 |  |  |  |  | FALSE |
| 5524 | advertisement\_\_external\_reseller\_\_rule\_flags | 3 |  |  |  |  | FALSE |
| 5525 | slot\_\_inbound\_rule\_\_network\_id | 3 |  |  |  |  | FALSE |
| 5526 | slot\_\_market\_avails | 3 |  |  |  |  | FALSE |
| 5527 | advertisement\_\_external\_reseller\_\_rule\_priority | 3 |  |  |  |  | FALSE |
| 5528 | advertisement\_\_shading\_context | 3 |  |  |  |  | FALSE |
| 5529 | advertisement\_\_shading\_context\_\_shading\_model\_name | 3 |  |  |  |  | FALSE |
| 5530 | slot\_\_forecast\_avails\_metrics\_\_total\_avails\_with\_forecast\_factor | 3 |  |  |  |  | FALSE |
| 5531 | advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 3 |  |  |  |  | FALSE |
| 5532 | advertisement\_\_external\_reseller\_\_network\_execution\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5533 | advertisement\_\_global\_advertiser\_id | 3 |  |  |  |  | FALSE |
| 5534 | partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 3 |  |  |  |  | FALSE |
| 5535 | advertisement\_\_rules | 3 |  |  |  |  | FALSE |
| 5536 | advertisement\_\_advertisement\_context\_\_network\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5537 | advertisement\_\_external\_reseller\_\_root\_asset\_group | 3 |  |  |  |  | FALSE |
| 5538 | advertisement\_\_rules\_\_win\_rule\_id | 3 |  |  |  |  | FALSE |
| 5539 | advertisement\_\_provider\_measured\_event\_id | 3 |  |  |  |  | FALSE |
| 5540 | advertisement\_\_is\_uy\_replaced | 3 |  |  |  |  | FALSE |
| 5541 | advertisement\_\_priority\_bucket | 3 |  |  |  |  | FALSE |
| 5542 | advertisement\_\_external\_reseller\_\_down\_network\_id | 3 |  |  |  |  | FALSE |
| 5543 | slot\_\_cue\_point\_sequence | 3 |  |  |  |  | FALSE |
| 5544 | advertisement\_\_inbound\_rule\_\_win\_inbound\_rule\_id | 3 |  |  |  |  | FALSE |
| 5545 | candidate\_\_site\_id | 3 |  |  |  |  | FALSE |
| 5546 | advertisement\_\_external\_reseller\_\_bidding\_revenue | 3 |  |  |  |  | FALSE |
| 5547 | advertisement\_\_unified\_yield\_\_replaced\_entity\_id | 3 |  |  |  |  | FALSE |
| 5548 | slot\_\_outbound\_order\_\_unified\_priority\_\_priority\_tier | 3 |  |  |  |  | FALSE |
| 5549 | advertisement\_\_inbound\_rule\_\_network\_id | 3 |  |  |  |  | FALSE |
| 5550 | candidate\_\_post\_auction\_discount\_id | 3 |  |  |  |  | FALSE |
| 5551 | advertisement\_\_triggering\_concrete\_event\_id | 3 |  |  |  |  | FALSE |
| 5552 | advertisement\_\_external\_reseller\_\_bidding\_up\_modified\_revenue | 3 |  |  |  |  | FALSE |
| 5553 | advertisement\_\_ad\_opportunity\_rules\_\_rule\_id | 3 |  |  |  |  | FALSE |
| 5554 | advertisement\_\_billable\_rate\_denominator\_event\_id | 3 |  |  |  |  | FALSE |
| 5555 | advertisement\_\_external\_reseller\_\_root\_asset\_id | 3 |  |  |  |  | FALSE |
| 5556 | advertisement\_\_external\_reseller\_\_up\_revenue\_as\_content\_owner | 3 |  |  |  |  | FALSE |
| 5557 | slot\_\_compatible\_dimensions | 3 |  |  |  |  | FALSE |
| 5558 | advertisement\_\_rules\_\_opp\_rule\_id | 3 |  |  |  |  | FALSE |
| 5559 | advertisement\_\_external\_reseller\_\_bidding\_up\_revenue | 3 |  |  |  |  | FALSE |
| 5560 | candidate\_\_ad\_replica\_id | 3 |  |  |  |  | FALSE |
| 5561 | candidate\_\_discount\_barter | 3 |  |  |  |  | FALSE |
| 5562 | advertisement\_\_xdevice\_policy\_id | 3 |  |  |  |  | FALSE |
| 5563 | candidate\_\_discount\_post\_auction\_\_amount | 3 |  |  |  |  | FALSE |
| 5564 | advertisement\_\_shading\_context\_\_shading\_model\_version | 3 |  |  |  |  | FALSE |
| 5565 | candidate\_\_has\_auction | 3 |  |  |  |  | FALSE |
| 5566 | slot\_\_inventory\_mask | 3 |  |  |  |  | FALSE |
| 5567 | candidate\_\_mbd\_deduction\_on\_selection\_ratio | 3 |  |  |  |  | FALSE |
| 5568 | advertisement\_\_unified\_yield\_\_uplift\_revenue | 3 |  |  |  |  | FALSE |
| 5569 | advertisement\_\_active\_data\_suite\_segment | 3 |  |  |  |  | FALSE |
| 5570 | candidate\_\_bit\_flags | 3 |  |  |  |  | FALSE |
| 5571 | advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 3 |  |  |  |  | FALSE |
| 5572 | slot\_\_eligible\_carriage\_listing\_split\_unit\_ids | 3 |  |  |  |  | FALSE |
| 5573 | slot\_\_content\_type\_id | 3 |  |  |  |  | FALSE |
| 5574 | advertisement\_\_billable\_rate | 3 |  |  |  |  | FALSE |
| 5575 | slot\_\_outbound\_order\_\_unified\_priority\_\_sub\_priority\_value | 3 |  |  |  |  | FALSE |
| 5576 | advertisement\_\_external\_reseller\_\_up\_network\_id | 3 |  |  |  |  | FALSE |
| 5577 | advertisement\_\_external\_reseller\_\_site\_section\_group\_id | 3 |  |  |  |  | FALSE |
| 5578 | candidate\_\_candidate\_network\_to\_auction\_seller\_network\_exchange\_rate | 3 |  |  |  |  | FALSE |
| 5579 | advertisement\_\_advertisement\_context | 3 |  |  |  |  | FALSE |
| 5580 | advertisement\_\_validation\_event | 3 |  |  |  |  | FALSE |
| 5581 | advertisement\_\_validation\_event\_\_numerator\_event\_id | 3 |  |  |  |  | FALSE |
| 5582 | advertisement\_\_external\_reseller\_\_supply\_acquisition\_cost | 3 |  |  |  |  | FALSE |
| 5583 | advertisement\_\_cch\_key\_domain\_config\_id | 3 |  |  |  |  | FALSE |
| 5584 | candidate\_\_discount\_barter\_\_id | 3 |  |  |  |  | FALSE |
| 5585 | candidate\_\_bsi\_id | 3 |  |  |  |  | FALSE |
| 5586 | slot\_\_content\_type | 3 |  |  |  |  | FALSE |
| 5587 | slot\_\_outbound\_order\_\_effective\_exclude\_aim\_audience\_ids | 3 |  |  |  |  | FALSE |
| 5588 | slot\_\_outbound\_order\_\_unified\_priority | 3 |  |  |  |  | FALSE |
| 5589 | advertisement\_\_external\_reseller\_\_bidding\_up\_original\_revenue | 3 |  |  |  |  | FALSE |
| 5590 | advertisement\_\_external\_reseller\_\_rule\_ext\_id | 3 |  |  |  |  | FALSE |
| 5591 | advertisement\_\_external\_reseller\_\_supply\_distribution\_cost | 3 |  |  |  |  | FALSE |
| 5592 | advertisement\_\_budget\_control\_level | 3 |  |  |  |  | FALSE |
| 5593 | advertisement\_\_booked\_percentage | 3 |  |  |  |  | FALSE |
| 5594 | advertisement\_\_ad\_delivery\_method | 3 |  |  |  |  | FALSE |
| 5595 | slot\_\_window\_start\_timestamp | 3 |  |  |  |  | FALSE |
| 5596 | advertisement\_\_external\_reseller\_\_marketplace\_audience\_extension\_deal\_id | 3 |  |  |  |  | FALSE |
| 5597 | slot\_\_height | 3 |  |  |  |  | FALSE |
| 5598 | advertisement\_\_contextual\_billings\_\_cpm | 3 |  |  |  |  | FALSE |
| 5599 | advertisement\_\_nielsen\_site\_url\_id | 3 |  |  |  |  | FALSE |
| 5600 | candidate\_\_advertiser\_domain | 3 |  |  |  |  | FALSE |
| 5601 | advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos | 3 |  |  |  |  | FALSE |
| 5602 | candidate\_\_rtb\_impression\_id | 3 |  |  |  |  | FALSE |
| 5603 | candidate\_\_unified\_deal\_priority | 3 |  |  |  |  | FALSE |
| 5604 | advertisement\_\_associate | 3 |  |  |  |  | FALSE |
| 5605 | advertisement\_\_recommended\_bidding\_price | 3 |  |  |  |  | FALSE |
| 5606 | candidate\_\_asset\_id | 3 |  |  |  |  | FALSE |
| 5607 | advertisement\_\_companion\_ad\_uniq\_id | 3 |  |  |  |  | FALSE |
| 5608 | advertisement\_\_external\_reseller\_\_context\_id | 3 |  |  |  |  | FALSE |
| 5609 | candidate\_\_trading\_desk\_id | 3 |  |  |  |  | FALSE |
| 5610 | candidate\_\_auction\_network\_execution\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5611 | advertisement\_\_ad\_opportunity\_rules | 3 |  |  |  |  | FALSE |
| 5612 | advertisement\_\_shading\_context\_\_shaded\_price\_usd | 3 |  |  |  |  | FALSE |
| 5613 | slot\_\_seller\_sponsor\_occupation\_on\_carriage | 3 |  |  |  |  | FALSE |
| 5614 | candidate\_\_bid\_replica\_id | 3 |  |  |  |  | FALSE |
| 5615 | slot\_\_slot\_context | 3 |  |  |  |  | FALSE |
| 5616 | advertisement\_\_unified\_yield\_\_replaced\_type | 3 |  |  |  |  | FALSE |
| 5617 | candidate\_\_domain | 3 |  |  |  |  | FALSE |
| 5618 | advertisement\_\_linear\_decision\_type | 3 |  |  |  |  | FALSE |
| 5619 | slot\_\_slot\_context\_\_network\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5620 | advertisement\_\_matched\_contextual\_segment\_ids | 3 |  |  |  |  | FALSE |
| 5621 | slot\_\_avails\_metrics\_\_default\_duration | 3 |  |  |  |  | FALSE |
| 5622 | advertisement\_\_unified\_yield | 3 |  |  |  |  | FALSE |
| 5623 | candidate\_\_discount\_post\_auction\_\_id | 3 |  |  |  |  | FALSE |
| 5624 | advertisement\_\_replaced\_placement\_id | 3 |  |  |  |  | FALSE |
| 5625 | advertisement\_\_error\_domain | 3 |  |  |  |  | FALSE |
| 5626 | candidate\_\_discount\_post\_auction | 3 |  |  |  |  | FALSE |
| 5627 | advertisement\_\_ad\_opportunity\_rules\_\_network\_id | 3 |  |  |  |  | FALSE |
| 5628 | candidate\_\_clock\_number | 3 |  |  |  |  | FALSE |
| 5629 | advertisement\_\_external\_reseller\_\_inventory\_id | 3 |  |  |  |  | FALSE |
| 5630 | slot\_\_forecast\_avails\_metrics\_\_remaining\_avails\_with\_forecast\_factor | 3 |  |  |  |  | FALSE |
| 5631 | slot\_\_break\_id | 3 |  |  |  |  | FALSE |
| 5632 | slot\_\_network\_execution\_ctx\_index | 3 |  |  |  |  | FALSE |
| 5633 | slot\_\_guaranteed\_flags | 3 |  |  |  |  | FALSE |
| 5634 | advertisement\_\_shading\_context\_\_bid\_price\_usd | 3 |  |  |  |  | FALSE |
| 5635 | candidate\_\_media\_buyer\_id | 3 |  |  |  |  | FALSE |
| 5636 | candidate\_\_auction\_outbound\_listing\_id | 3 |  |  |  |  | FALSE |
| 5637 | advertisement\_\_universal\_ad\_id | 3 |  |  |  |  | FALSE |
| 5638 | slot\_\_ad\_unit\_network\_id | 3 |  |  |  |  | FALSE |
| 5639 | slot\_\_outbound\_order\_\_listing\_id | 3 |  |  |  |  | FALSE |
| 5640 | advertisement\_\_error\_partner | 3 |  |  |  |  | FALSE |
| 5641 | slot\_\_forecast\_avails\_metrics | 3 |  |  |  |  | FALSE |
| 5642 | advertisement\_\_video\_resolution | 3 |  |  |  |  | FALSE |
| 5643 | advertisement\_\_unified\_priority | 3 |  |  |  |  | FALSE |
| 5644 | candidate\_\_sfx\_dsp\_id | 3 |  |  |  |  | FALSE |
| 5645 | advertisement\_\_external\_reseller\_\_reseller\_index\_in\_slot | 3 |  |  |  |  | FALSE |
| 5646 | advertisement\_\_relative\_priority | 3 |  |  |  |  | FALSE |
| 5647 | slot\_\_outbound\_order | 3 |  |  |  |  | FALSE |
| 5648 | advertisement\_\_external\_reseller\_\_margin | 3 |  |  |  |  | FALSE |
| 5649 | slot\_\_carriage\_listing\_origin\_split\_unit\_num | 3 |  |  |  |  | FALSE |
| 5650 | candidate\_\_global\_agency\_ids | 3 |  |  |  |  | FALSE |
| 5651 | inventory\_\_site\_section\_chain\_\_audience\_segment\_max\_cpm | 2 |  |  |  |  | FALSE |
| 5652 | inventory\_\_site\_section\_chain\_\_bidding\_up\_revenue | 2 |  |  |  |  | FALSE |
| 5653 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 2 |  |  |  |  | FALSE |
| 5654 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 2 |  |  |  |  | FALSE |
| 5655 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 2 |  |  |  |  | FALSE |
| 5656 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 2 |  |  |  |  | FALSE |
| 5657 | request\_\_auction\_network\_contexts\_\_content\_rating | 2 |  |  |  |  | FALSE |
| 5658 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 2 |  |  |  |  | FALSE |
| 5659 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 2 |  |  |  |  | FALSE |
| 5660 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 2 |  |  |  |  | FALSE |
| 5661 | request\_\_auction\_network\_contexts\_\_content\_genre | 2 |  |  |  |  | FALSE |
| 5662 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 2 |  |  |  |  | FALSE |
| 5663 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 2 |  |  |  |  | FALSE |
| 5664 | inventory\_\_asset\_chain\_\_audience\_segment\_max\_cpm | 2 |  |  |  |  | FALSE |
| 5665 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos | 2 |  |  |  |  | FALSE |
| 5666 | inventory\_\_asset\_chain\_\_bidding\_up\_revenue | 2 |  |  |  |  | FALSE |
| 5667 | inventory\_\_site\_section\_chain\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 2 |  |  |  |  | FALSE |
| 5668 | inventory\_\_asset\_chain\_\_audience\_partner\_segment\_infos | 2 |  |  |  |  | FALSE |
| 5669 | ads\_in\_slot\_\_candidate\_\_dsp\_clearing\_price | 1 |  |  |  |  | FALSE |
| 5670 | ads\_in\_slot\_\_candidate\_\_advertiser\_domain | 1 |  |  |  |  | FALSE |
| 5671 | ads\_in\_slot\_\_partners\_\_standard\_content\_territory\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5672 | ads\_in\_slot\_\_partners\_\_standard\_genre\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5673 | ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5674 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_revenue | 1 |  |  |  |  | FALSE |
| 5675 | ads\_in\_slot\_\_partners\_\_user\_agent\_visibility | 1 |  |  |  |  | FALSE |
| 5676 | ads\_in\_slot\_\_auction\_\_error | 1 |  |  |  |  | FALSE |
| 5677 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_opportunity | 1 |  |  |  |  | FALSE |
| 5678 | ads\_in\_slot\_\_advertisement\_\_matched\_daypart | 1 |  |  |  |  | FALSE |
| 5679 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5680 | ads\_in\_slot\_\_auction\_\_execution\_node\_id | 1 |  |  |  |  | FALSE |
| 5681 | ads\_in\_slot\_\_advertisement\_\_replaced\_ad\_network\_id | 1 |  |  |  |  | FALSE |
| 5682 | ads\_in\_slot\_\_advertisement\_\_shading\_context\_\_shading\_model\_version | 1 |  |  |  |  | FALSE |
| 5683 | ads\_in\_slot\_\_partners\_\_geo\_city\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5684 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_owner\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5685 | ads\_in\_slot\_\_partners\_\_airing\_channel\_group\_id | 1 |  |  |  |  | FALSE |
| 5686 | ads\_in\_slot\_\_partners\_\_standard\_brand\_visibility | 1 |  |  |  |  | FALSE |
| 5687 | ads\_in\_slot\_\_advertisement\_\_ad\_oo\_network\_id | 1 |  |  |  |  | FALSE |
| 5688 | ads\_in\_slot\_\_advertisement\_\_matched\_key\_value\_ids | 1 |  |  |  |  | FALSE |
| 5689 | ads\_in\_slot\_\_advertisement\_\_validation\_event\_\_concrete\_event\_group\_id | 1 |  |  |  |  | FALSE |
| 5690 | ads\_in\_slot\_\_partners\_\_device\_id\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5691 | ads\_in\_slot\_\_advertisement\_\_is\_rbp | 1 |  |  |  |  | FALSE |
| 5692 | ads\_in\_slot\_\_auction\_\_buyer\_id | 1 |  |  |  |  | FALSE |
| 5693 | ads\_in\_slot\_\_partners\_\_standard\_brand\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5694 | ads\_in\_slot\_\_candidate\_\_universal\_ad\_id | 1 |  |  |  |  | FALSE |
| 5695 | ads\_in\_slot\_\_partners\_\_reseller\_revenue | 1 |  |  |  |  | FALSE |
| 5696 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_network\_id | 1 |  |  |  |  | FALSE |
| 5697 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_listing\_creative\_duration\_check\_failed | 1 |  |  |  |  | FALSE |
| 5698 | ads\_in\_slot\_\_candidate\_\_advertisement\_index | 1 |  |  |  |  | FALSE |
| 5699 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_bidding\_up\_original\_revenue | 1 |  |  |  |  | FALSE |
| 5700 | ads\_in\_slot\_\_partners\_\_inbound\_listing\_ids | 1 |  |  |  |  | FALSE |
| 5701 | ads\_in\_slot\_\_auction\_\_auction\_sampling | 1 |  |  |  |  | FALSE |
| 5702 | ads\_in\_slot\_\_candidate\_\_raw\_price | 1 |  |  |  |  | FALSE |
| 5703 | ads\_in\_slot\_\_partners\_\_selected\_yo\_volume\_cap\_ids | 1 |  |  |  |  | FALSE |
| 5704 | ads\_in\_slot\_\_advertisement\_\_ad\_opportunity\_rules\_\_network\_id | 1 |  |  |  |  | FALSE |
| 5705 | ads\_in\_slot\_\_advertisement\_\_shading\_context\_\_bid\_floor\_price\_usd | 1 |  |  |  |  | FALSE |
| 5706 | ads\_in\_slot\_\_advertisement\_\_measurable\_concrete\_event\_id | 1 |  |  |  |  | FALSE |
| 5707 | ads\_in\_slot\_\_advertisement\_\_targeting\_criteria\_id | 1 |  |  |  |  | FALSE |
| 5708 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_ssp\_avails | 1 |  |  |  |  | FALSE |
| 5709 | ads\_in\_slot\_\_partners\_\_content\_owner\_bidding\_original\_revenue | 1 |  |  |  |  | FALSE |
| 5710 | ads\_in\_slot\_\_partners\_\_matched\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 5711 | ads\_in\_slot\_\_partners\_\_standard\_programmer\_visibility | 1 |  |  |  |  | FALSE |
| 5712 | ads\_in\_slot\_\_advertisement\_\_io\_id | 1 |  |  |  |  | FALSE |
| 5713 | ack\_\_unit | 1 |  |  |  |  | FALSE |
| 5714 | ads\_in\_slot\_\_partners\_\_margin | 1 |  |  |  |  | FALSE |
| 5715 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_outbound\_order\_index | 1 |  |  |  |  | FALSE |
| 5716 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_not\_found | 1 |  |  |  |  | FALSE |
| 5717 | ack\_\_metrics\_\_triggering\_ad\_views | 1 |  |  |  |  | FALSE |
| 5718 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_unfilled\_avails | 1 |  |  |  |  | FALSE |
| 5719 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_flags | 1 |  |  |  |  | FALSE |
| 5720 | ads\_in\_slot\_\_partners\_\_matched\_daypart | 1 |  |  |  |  | FALSE |
| 5721 | ads\_in\_slot\_\_partners\_\_asset\_group\_id | 1 |  |  |  |  | FALSE |
| 5722 | ack\_\_cpx\_derived\_concrete\_event\_id | 1 |  |  |  |  | FALSE |
| 5723 | ads\_in\_slot\_\_candidate\_\_price\_type | 1 |  |  |  |  | FALSE |
| 5724 | ads\_in\_slot\_\_partners\_\_geo\_city\_visibility | 1 |  |  |  |  | FALSE |
| 5725 | ads\_in\_slot\_\_advertisement\_\_ad\_opportunity\_rules\_\_total\_opp | 1 |  |  |  |  | FALSE |
| 5726 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_date\_range\_check\_failed | 1 |  |  |  |  | FALSE |
| 5727 | ack\_\_metrics\_\_ad\_minimize | 1 |  |  |  |  | FALSE |
| 5728 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_name | 1 |  |  |  |  | FALSE |
| 5729 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_default\_duration | 1 |  |  |  |  | FALSE |
| 5730 | ads\_in\_slot\_\_advertisement\_\_is\_owned\_by\_cro | 1 |  |  |  |  | FALSE |
| 5731 | ads\_in\_slot\_\_advertisement\_\_candidate\_index | 1 |  |  |  |  | FALSE |
| 5732 | ads\_in\_slot\_\_auction\_\_ab\_test\_items | 1 |  |  |  |  | FALSE |
| 5733 | ads\_in\_slot\_\_partners\_\_matched\_yield\_optimization\_ids | 1 |  |  |  |  | FALSE |
| 5734 | ads\_in\_slot\_\_partners\_\_distributor\_bidding\_revenue | 1 |  |  |  |  | FALSE |
| 5735 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_floor\_price\_not\_met | 1 |  |  |  |  | FALSE |
| 5736 | ads\_in\_slot\_\_candidate\_\_discount\_post\_auction | 1 |  |  |  |  | FALSE |
| 5737 | ads\_in\_slot\_\_partners\_\_standard\_content\_series\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5738 | ads\_in\_slot\_\_advertisement\_\_bid\_price\_to\_upstream | 1 |  |  |  |  | FALSE |
| 5739 | ack\_\_metrics\_\_ad\_gross\_avail | 1 |  |  |  |  | FALSE |
| 5740 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_distinct\_inventory\_avails | 1 |  |  |  |  | FALSE |
| 5741 | ads\_in\_slot\_\_partners\_\_content\_form\_visibility | 1 |  |  |  |  | FALSE |
| 5742 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_status | 1 |  |  |  |  | FALSE |
| 5743 | ads\_in\_slot\_\_partners\_\_standard\_brand\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5744 | ads\_in\_slot\_\_advertisement\_\_unified\_priority | 1 |  |  |  |  | FALSE |
| 5745 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics | 1 |  |  |  |  | FALSE |
| 5746 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5747 | ads\_in\_slot\_\_partners\_\_geo\_state\_visibility | 1 |  |  |  |  | FALSE |
| 5748 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_up\_revenue\_as\_content\_owner | 1 |  |  |  |  | FALSE |
| 5749 | key\_value\_\_key | 1 |  |  |  |  | FALSE |
| 5750 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5751 | ads\_in\_slot\_\_auction\_\_experiment | 1 |  |  |  |  | FALSE |
| 5752 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_total\_avails | 1 |  |  |  |  | FALSE |
| 5753 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_inventory\_avails | 1 |  |  |  |  | FALSE |
| 5754 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_network\_id | 1 |  |  |  |  | FALSE |
| 5755 | ads\_in\_slot\_\_candidate\_\_rtb\_impression\_slot\_index | 1 |  |  |  |  | FALSE |
| 5756 | ads\_in\_slot\_\_auction\_\_impression\_\_deals | 1 |  |  |  |  | FALSE |
| 5757 | ads\_in\_slot\_\_candidate\_\_ortb\_fwpartners\_\_idvalue | 1 |  |  |  |  | FALSE |
| 5758 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_exchange\_order\_id | 1 |  |  |  |  | FALSE |
| 5759 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_opportunity | 1 |  |  |  |  | FALSE |
| 5760 | ads\_in\_slot\_\_advertisement\_\_replaced\_campaign\_id | 1 |  |  |  |  | FALSE |
| 5761 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_internal\_deal\_id | 1 |  |  |  |  | FALSE |
| 5762 | ads\_in\_slot\_\_auction\_\_is\_ssp\_auction | 1 |  |  |  |  | FALSE |
| 5763 | ads\_in\_slot\_\_advertisement\_\_billable\_rate | 1 |  |  |  |  | FALSE |
| 5764 | ack\_\_metrics\_\_denominator\_event\_count | 1 |  |  |  |  | FALSE |
| 5765 | ads\_in\_slot\_\_advertisement\_\_is\_embedded\_tracking | 1 |  |  |  |  | FALSE |
| 5766 | ads\_in\_slot\_\_auction\_\_impression\_\_bid\_floor | 1 |  |  |  |  | FALSE |
| 5767 | ack\_\_metrics\_\_fire\_event\_slot\_revenue\_ratio | 1 |  |  |  |  | FALSE |
| 5768 | ads\_in\_slot\_\_candidate\_\_auction\_outbound\_listing\_id | 1 |  |  |  |  | FALSE |
| 5769 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_exempt\_ratio | 1 |  |  |  |  | FALSE |
| 5770 | ads\_in\_slot\_\_advertisement\_\_matched\_state\_ids | 1 |  |  |  |  | FALSE |
| 5771 | ads\_in\_slot\_\_partners\_\_revenue | 1 |  |  |  |  | FALSE |
| 5772 | ads\_in\_slot\_\_advertisement\_\_shading\_context\_\_shaded\_price\_usd | 1 |  |  |  |  | FALSE |
| 5773 | ads\_in\_slot\_\_advertisement\_\_budget\_control\_level | 1 |  |  |  |  | FALSE |
| 5774 | ack\_\_metrics\_\_implicit\_no\_ad\_view | 1 |  |  |  |  | FALSE |
| 5775 | ads\_in\_slot\_\_partners\_\_asset\_group\_ids | 1 |  |  |  |  | FALSE |
| 5776 | ads\_in\_slot\_\_partners\_\_visitor\_custom\_id\_visibility | 1 |  |  |  |  | FALSE |
| 5777 | ads\_in\_slot\_\_advertisement\_\_insertion\_order\_id | 1 |  |  |  |  | FALSE |
| 5778 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_down\_revenue | 1 |  |  |  |  | FALSE |
| 5779 | ads\_in\_slot\_\_partners\_\_key\_value\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5780 | ads\_in\_slot\_\_advertisement\_\_global\_advertiser\_id | 1 |  |  |  |  | FALSE |
| 5781 | ads\_in\_slot\_\_partners\_\_floor\_price | 1 |  |  |  |  | FALSE |
| 5782 | ads\_in\_slot\_\_advertisement\_\_contextual\_billings\_\_cpm | 1 |  |  |  |  | FALSE |
| 5783 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 1 |  |  |  |  | FALSE |
| 5784 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5785 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_input\_ad\_number | 1 |  |  |  |  | FALSE |
| 5786 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_bid\_floor\_uplift | 1 |  |  |  |  | FALSE |
| 5787 | ads\_in\_slot\_\_auction\_\_auction\_status | 1 |  |  |  |  | FALSE |
| 5788 | ads\_in\_slot\_\_candidate\_\_site\_section\_id | 1 |  |  |  |  | FALSE |
| 5789 | ads\_in\_slot\_\_advertisement\_\_is\_external | 1 |  |  |  |  | FALSE |
| 5790 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_model\_info | 1 |  |  |  |  | FALSE |
| 5791 | ads\_in\_slot\_\_partners\_\_unified\_rule\_priority | 1 |  |  |  |  | FALSE |
| 5792 | ads\_in\_slot\_\_partners\_\_standard\_content\_daypart\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5793 | ads\_in\_slot\_\_partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5794 | ads\_in\_slot\_\_partners\_\_break\_id | 1 |  |  |  |  | FALSE |
| 5795 | ads\_in\_slot\_\_auction\_\_mkpl\_partner\_tags | 1 |  |  |  |  | FALSE |
| 5796 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_total\_unfilled\_avails | 1 |  |  |  |  | FALSE |
| 5797 | ads\_in\_slot\_\_advertisement\_\_associate | 1 |  |  |  |  | FALSE |
| 5798 | ads\_in\_slot\_\_candidate\_\_dsp\_currency\_id | 1 |  |  |  |  | FALSE |
| 5799 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_schedule | 1 |  |  |  |  | FALSE |
| 5800 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_reseller\_index\_in\_slot | 1 |  |  |  |  | FALSE |
| 5801 | ack\_\_metrics\_\_cpx\_abstract\_currency\_ratio | 1 |  |  |  |  | FALSE |
| 5802 | ads\_in\_slot\_\_candidate\_\_creative\_approval\_request | 1 |  |  |  |  | FALSE |
| 5803 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_inventory\_avails | 1 |  |  |  |  | FALSE |
| 5804 | ads\_in\_slot\_\_advertisement\_\_companion\_ad\_uniq\_id | 1 |  |  |  |  | FALSE |
| 5805 | ads\_in\_slot | 1 |  |  |  |  | FALSE |
| 5806 | ads\_in\_slot\_\_candidate\_\_dsp\_clearing\_price\_discounted | 1 |  |  |  |  | FALSE |
| 5807 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unconstrained\_avails | 1 |  |  |  |  | FALSE |
| 5808 | ads\_in\_slot\_\_partners\_\_visitor\_custom\_id\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5809 | ack\_\_nielsen\_demographic\_id | 1 |  |  |  |  | FALSE |
| 5810 | ads\_in\_slot\_\_partners\_\_inbound\_order\_ids | 1 |  |  |  |  | FALSE |
| 5811 | ads\_in\_slot\_\_partners\_\_geo\_state\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5812 | ads\_in\_slot\_\_auction\_\_execution\_contexts\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 5813 | ads\_in\_slot\_\_candidate\_\_creative\_approval\_request\_\_network\_id | 1 |  |  |  |  | FALSE |
| 5814 | ads\_in\_slot\_\_candidate\_\_response\_industry | 1 |  |  |  |  | FALSE |
| 5815 | ads\_in\_slot\_\_partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5816 | execution\_networks\_\_audience\_segment\_max\_cpm | 1 |  |  |  |  | FALSE |
| 5817 | ads\_in\_slot\_\_candidate\_\_content\_type | 1 |  |  |  |  | FALSE |
| 5818 | ads\_in\_slot\_\_auction\_\_is\_faked\_auction | 1 |  |  |  |  | FALSE |
| 5819 | ads\_in\_slot\_\_auction\_\_impression\_\_error | 1 |  |  |  |  | FALSE |
| 5820 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5821 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_undefined | 1 |  |  |  |  | FALSE |
| 5822 | ads\_in\_slot\_\_partners\_\_ip\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5823 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_bid\_floor | 1 |  |  |  |  | FALSE |
| 5824 | ads\_in\_slot\_\_partners\_\_standard\_genre\_visibility | 1 |  |  |  |  | FALSE |
| 5825 | ads\_in\_slot\_\_candidate\_\_bit\_flags | 1 |  |  |  |  | FALSE |
| 5826 | ads\_in\_slot\_\_advertisement\_\_shading\_context | 1 |  |  |  |  | FALSE |
| 5827 | ack\_\_metrics\_\_measurable\_ad\_rewind\_impression | 1 |  |  |  |  | FALSE |
| 5828 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5829 | ads\_in\_slot\_\_advertisement\_\_ad\_opportunity\_rules | 1 |  |  |  |  | FALSE |
| 5830 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_time\_based\_freq\_cap | 1 |  |  |  |  | FALSE |
| 5831 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5832 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_replaced\_entity\_id | 1 |  |  |  |  | FALSE |
| 5833 | ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts\_\_carriage\_inventory\_owner\_id | 1 |  |  |  |  | FALSE |
| 5834 | ads\_in\_slot\_\_auction\_\_market\_integration\_type | 1 |  |  |  |  | FALSE |
| 5835 | ack\_\_yield\_optimization\_ids\_\_demand\_type | 1 |  |  |  |  | FALSE |
| 5836 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_filled\_ad\_num | 1 |  |  |  |  | FALSE |
| 5837 | ads\_in\_slot\_\_auction\_\_auction\_sampling\_\_mode | 1 |  |  |  |  | FALSE |
| 5838 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_order\_ids | 1 |  |  |  |  | FALSE |
| 5839 | ads\_in\_slot\_\_partners\_\_standard\_content\_series\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5840 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos | 1 |  |  |  |  | FALSE |
| 5841 | ads\_in\_slot\_\_partners\_\_outbound\_rules\_\_total\_opp | 1 |  |  |  |  | FALSE |
| 5842 | ads\_in\_slot\_\_partners\_\_geo\_country\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5843 | ads\_in\_slot\_\_auction | 1 |  |  |  |  | FALSE |
| 5844 | ads\_in\_slot\_\_partners\_\_site\_group\_id | 1 |  |  |  |  | FALSE |
| 5845 | ack\_\_metrics\_\_ad\_collapse | 1 |  |  |  |  | FALSE |
| 5846 | ads\_in\_slot\_\_advertisement\_\_replaced\_io\_id | 1 |  |  |  |  | FALSE |
| 5847 | ads\_in\_slot\_\_candidate\_\_creative\_approval\_request\_\_approval\_scope | 1 |  |  |  |  | FALSE |
| 5848 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status | 1 |  |  |  |  | FALSE |
| 5849 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_context\_id | 1 |  |  |  |  | FALSE |
| 5850 | ads\_in\_slot\_\_partners\_\_selected\_yo\_inventory\_prioritization\_nip\_id | 1 |  |  |  |  | FALSE |
| 5851 | ads\_in\_slot\_\_partners\_\_matched\_audience\_item\_ids | 1 |  |  |  |  | FALSE |
| 5852 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_mpe\_listing\_restriction | 1 |  |  |  |  | FALSE |
| 5853 | ads\_in\_slot\_\_advertisement\_\_is\_zero\_revenue | 1 |  |  |  |  | FALSE |
| 5854 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_media\_buyer\_id | 1 |  |  |  |  | FALSE |
| 5855 | ack\_\_psn\_msg | 1 |  |  |  |  | FALSE |
| 5856 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5857 | ads\_in\_slot\_\_advertisement\_\_cch\_rendition\_id | 1 |  |  |  |  | FALSE |
| 5858 | ads\_in\_slot\_\_advertisement\_\_active\_data\_suite\_segment | 1 |  |  |  |  | FALSE |
| 5859 | ads\_in\_slot\_\_partners\_\_device\_id\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5860 | ack\_\_metrics\_\_ad\_close | 1 |  |  |  |  | FALSE |
| 5861 | ads\_in\_slot\_\_partners\_\_marketplace\_audience\_extension\_deal\_ids | 1 |  |  |  |  | FALSE |
| 5862 | ads\_in\_slot\_\_auction\_\_ab\_test\_item\_index | 1 |  |  |  |  | FALSE |
| 5863 | ads\_in\_slot\_\_advertisement\_\_video\_resolution | 1 |  |  |  |  | FALSE |
| 5864 | ads\_in\_slot\_\_advertisement\_\_rules\_\_network\_id | 1 |  |  |  |  | FALSE |
| 5865 | ack\_\_identifier\_\_sequence | 1 |  |  |  |  | FALSE |
| 5866 | key\_value\_\_value | 1 |  |  |  |  | FALSE |
| 5867 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_buyers\_\_internal\_seat\_id | 1 |  |  |  |  | FALSE |
| 5868 | ack\_\_metrics\_\_fire\_event\_bid\_revenue\_ratio | 1 |  |  |  |  | FALSE |
| 5869 | ads\_in\_slot\_\_partners\_\_standard\_content\_daypart\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5870 | ads\_in\_slot\_\_partners\_\_non\_tracked\_audience\_item\_ids | 1 |  |  |  |  | FALSE |
| 5871 | ack\_\_scte\_message\_id | 1 |  |  |  |  | FALSE |
| 5872 | ack\_\_concrete\_event\_provider\_id | 1 |  |  |  |  | FALSE |
| 5873 | ads\_in\_slot\_\_candidate\_\_candidate\_network\_to\_auction\_network\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 5874 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_listing\_id | 1 |  |  |  |  | FALSE |
| 5875 | ads\_in\_slot\_\_advertisement\_\_matched\_geo\_ids | 1 |  |  |  |  | FALSE |
| 5876 | ads\_in\_slot\_\_advertisement\_\_inventory\_protection\_flags | 1 |  |  |  |  | FALSE |
| 5877 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_avails\_metrics | 1 |  |  |  |  | FALSE |
| 5878 | ads\_in\_slot\_\_candidate\_\_auction\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 5879 | ads\_in\_slot\_\_partners\_\_selected\_yo\_margin\_id | 1 |  |  |  |  | FALSE |
| 5880 | ads\_in\_slot\_\_candidate\_\_cch\_key | 1 |  |  |  |  | FALSE |
| 5881 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_value | 1 |  |  |  |  | FALSE |
| 5882 | ads\_in\_slot\_\_advertisement\_\_matched\_postal\_code\_ids | 1 |  |  |  |  | FALSE |
| 5883 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_budget | 1 |  |  |  |  | FALSE |
| 5884 | ack\_\_ivt\_tracked\_info\_\_ivt\_not\_rewind\_reason | 1 |  |  |  |  | FALSE |
| 5885 | ads\_in\_slot\_\_partners\_\_device\_id\_visibility | 1 |  |  |  |  | FALSE |
| 5886 | ads\_in\_slot\_\_advertisement\_\_matched\_country\_ids | 1 |  |  |  |  | FALSE |
| 5887 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_rule\_ext\_id | 1 |  |  |  |  | FALSE |
| 5888 | ack\_\_yield\_optimization\_ids\_\_demand\_id | 1 |  |  |  |  | FALSE |
| 5889 | ads\_in\_slot\_\_candidate\_\_ortb\_fwpartners\_\_idtype | 1 |  |  |  |  | FALSE |
| 5890 | ads\_in\_slot\_\_advertisement\_\_unified\_yield | 1 |  |  |  |  | FALSE |
| 5891 | ads\_in\_slot\_\_auction\_\_extra\_flags | 1 |  |  |  |  | FALSE |
| 5892 | ads\_in\_slot\_\_candidate\_\_price | 1 |  |  |  |  | FALSE |
| 5893 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_not\_compatible | 1 |  |  |  |  | FALSE |
| 5894 | ads\_in\_slot\_\_candidate\_\_candidate\_network\_to\_auction\_seller\_network\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 5895 | ads\_in\_slot\_\_advertisement\_\_matched\_dma\_ids | 1 |  |  |  |  | FALSE |
| 5896 | ads\_in\_slot\_\_partners\_\_geo\_city\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5897 | ads\_in\_slot\_\_advertisement\_\_universal\_ad\_id | 1 |  |  |  |  | FALSE |
| 5898 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_unmapped | 1 |  |  |  |  | FALSE |
| 5899 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_level | 1 |  |  |  |  | FALSE |
| 5900 | ads\_in\_slot\_\_partners\_\_user\_agent\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5901 | ads\_in\_slot\_\_candidate\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 5902 | ads\_in\_slot\_\_candidate\_\_global\_agency\_ids | 1 |  |  |  |  | FALSE |
| 5903 | ads\_in\_slot\_\_auction\_\_impression\_\_slot\_index | 1 |  |  |  |  | FALSE |
| 5904 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_unconstrained\_avails | 1 |  |  |  |  | FALSE |
| 5905 | ads\_in\_slot\_\_candidate\_\_pod\_replica\_id | 1 |  |  |  |  | FALSE |
| 5906 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_up\_network\_id | 1 |  |  |  |  | FALSE |
| 5907 | ack\_\_callback\_server\_id | 1 |  |  |  |  | FALSE |
| 5908 | ack\_\_psn\_msg\_\_content\_asset\_id | 1 |  |  |  |  | FALSE |
| 5909 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_unfilled\_avails | 1 |  |  |  |  | FALSE |
| 5910 | ads\_in\_slot\_\_partners\_\_geo\_dma\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5911 | ads\_in\_slot\_\_advertisement\_\_effective\_unified\_priority | 1 |  |  |  |  | FALSE |
| 5912 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_available\_duration | 1 |  |  |  |  | FALSE |
| 5913 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_buyer\_group\_id | 1 |  |  |  |  | FALSE |
| 5914 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics | 1 |  |  |  |  | FALSE |
| 5915 | ads\_in\_slot\_\_auction\_\_bid\_to\_eur\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 5916 | ads\_in\_slot\_\_candidate\_\_brand\_id | 1 |  |  |  |  | FALSE |
| 5917 | ads\_in\_slot\_\_candidate\_\_filter\_reason | 1 |  |  |  |  | FALSE |
| 5918 | ads\_in\_slot\_\_partners\_\_standard\_language\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5919 | execution\_networks\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 1 |  |  |  |  | FALSE |
| 5920 | ads\_in\_slot\_\_candidate\_\_advertiser\_id | 1 |  |  |  |  | FALSE |
| 5921 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_ids | 1 |  |  |  |  | FALSE |
| 5922 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_unmapped | 1 |  |  |  |  | FALSE |
| 5923 | ads\_in\_slot\_\_advertisement\_\_contextual\_billings\_\_segment\_id | 1 |  |  |  |  | FALSE |
| 5924 | ads\_in\_slot\_\_partners\_\_supply\_distribution\_cost | 1 |  |  |  |  | FALSE |
| 5925 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_output\_ad\_number | 1 |  |  |  |  | FALSE |
| 5926 | ack\_\_is\_filtered | 1 |  |  |  |  | FALSE |
| 5927 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_down\_network\_id | 1 |  |  |  |  | FALSE |
| 5928 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_uplift\_revenue | 1 |  |  |  |  | FALSE |
| 5929 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings | 1 |  |  |  |  | FALSE |
| 5930 | ads\_in\_slot\_\_candidate\_\_external\_network\_id | 1 |  |  |  |  | FALSE |
| 5931 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_count\_imp\_as\_booked | 1 |  |  |  |  | FALSE |
| 5932 | ack\_\_metrics | 1 |  |  |  |  | FALSE |
| 5933 | ads\_in\_slot\_\_candidate\_\_internal\_seat\_id | 1 |  |  |  |  | FALSE |
| 5934 | ads\_in\_slot\_\_partners\_\_site\_section\_group\_ids | 1 |  |  |  |  | FALSE |
| 5935 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_demand\_type | 1 |  |  |  |  | FALSE |
| 5936 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 1 |  |  |  |  | FALSE |
| 5937 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_profile\_check\_failed | 1 |  |  |  |  | FALSE |
| 5938 | ads\_in\_slot\_\_advertisement\_\_ad\_unit\_id | 1 |  |  |  |  | FALSE |
| 5939 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_flags | 1 |  |  |  |  | FALSE |
| 5940 | ack\_\_metrics\_\_ad\_rewind | 1 |  |  |  |  | FALSE |
| 5941 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_uplift\_ecpm | 1 |  |  |  |  | FALSE |
| 5942 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_filled\_duration | 1 |  |  |  |  | FALSE |
| 5943 | ads\_in\_slot\_\_candidate\_\_clearing\_price | 1 |  |  |  |  | FALSE |
| 5944 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_buyers | 1 |  |  |  |  | FALSE |
| 5945 | ads\_in\_slot\_\_partners\_\_geo\_visibility | 1 |  |  |  |  | FALSE |
| 5946 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_slot\_assigned\_through\_mrm\_rule | 1 |  |  |  |  | FALSE |
| 5947 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_sponsorship\_check\_failed | 1 |  |  |  |  | FALSE |
| 5948 | ads\_in\_slot\_\_partners\_\_internal\_deal\_ids | 1 |  |  |  |  | FALSE |
| 5949 | ads\_in\_slot\_\_advertisement\_\_advertisement\_context\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 5950 | ads\_in\_slot\_\_partners\_\_device\_id\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 5951 | ads\_in\_slot\_\_auction\_\_ab\_test\_items\_\_bucket\_id | 1 |  |  |  |  | FALSE |
| 5952 | ads\_in\_slot\_\_candidate\_\_filter\_reason\_\_error\_category | 1 |  |  |  |  | FALSE |
| 5953 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative | 1 |  |  |  |  | FALSE |
| 5954 | ads\_in\_slot\_\_auction\_\_bid\_request\_count | 1 |  |  |  |  | FALSE |
| 5955 | ads\_in\_slot\_\_partners\_\_audience\_segment\_max\_cpm | 1 |  |  |  |  | FALSE |
| 5956 | ads\_in\_slot\_\_partners\_\_standard\_language\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5957 | ads\_in\_slot\_\_partners\_\_geo\_country\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5958 | ads\_in\_slot\_\_partners\_\_rule\_ext\_id | 1 |  |  |  |  | FALSE |
| 5959 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_asset\_group\_id | 1 |  |  |  |  | FALSE |
| 5960 | ack\_\_vod\_session\_id | 1 |  |  |  |  | FALSE |
| 5961 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_duration | 1 |  |  |  |  | FALSE |
| 5962 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_trading\_desk\_id | 1 |  |  |  |  | FALSE |
| 5963 | ads\_in\_slot\_\_advertisement\_\_replaced\_creative\_id | 1 |  |  |  |  | FALSE |
| 5964 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_unified\_rule\_priority\_\_sub\_priority\_value | 1 |  |  |  |  | FALSE |
| 5965 | ads\_in\_slot\_\_candidate\_\_rtb\_auction\_index | 1 |  |  |  |  | FALSE |
| 5966 | ack\_\_metrics\_\_measurable\_ad\_pause\_resume\_impression | 1 |  |  |  |  | FALSE |
| 5967 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_order\_type | 1 |  |  |  |  | FALSE |
| 5968 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 5969 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_output\_ad\_number | 1 |  |  |  |  | FALSE |
| 5970 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_phase\_metrics\_\_phase | 1 |  |  |  |  | FALSE |
| 5971 | ads\_in\_slot\_\_candidate\_\_profile\_check\_passed | 1 |  |  |  |  | FALSE |
| 5972 | ack\_\_cpx\_flag | 1 |  |  |  |  | FALSE |
| 5973 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_output\_ad\_number | 1 |  |  |  |  | FALSE |
| 5974 | ads\_in\_slot\_\_advertisement\_\_variant\_rendition\_ids | 1 |  |  |  |  | FALSE |
| 5975 | ads\_in\_slot\_\_auction\_\_publisher\_id | 1 |  |  |  |  | FALSE |
| 5976 | ack\_\_metrics\_\_numerator\_event\_count | 1 |  |  |  |  | FALSE |
| 5977 | ads\_in\_slot\_\_partners\_\_content\_rating\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 5978 | ads\_in\_slot\_\_candidate\_\_auction\_outbound\_bid\_floor | 1 |  |  |  |  | FALSE |
| 5979 | ads\_in\_slot\_\_advertisement\_\_matched\_city\_ids | 1 |  |  |  |  | FALSE |
| 5980 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_initial\_filled\_duration | 1 |  |  |  |  | FALSE |
| 5981 | ads\_in\_slot\_\_partners\_\_priority\_tier | 1 |  |  |  |  | FALSE |
| 5982 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_root\_section\_group | 1 |  |  |  |  | FALSE |
| 5983 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5984 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_ad\_asset\_store\_availability | 1 |  |  |  |  | FALSE |
| 5985 | ads\_in\_slot\_\_candidate\_\_flags | 1 |  |  |  |  | FALSE |
| 5986 | ads\_in\_slot\_\_advertisement\_\_matched\_region\_ids | 1 |  |  |  |  | FALSE |
| 5987 | ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts\_\_carriage\_listing\_split\_unit\_id | 1 |  |  |  |  | FALSE |
| 5988 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_unmapped | 1 |  |  |  |  | FALSE |
| 5989 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_outbound\_order\_index | 1 |  |  |  |  | FALSE |
| 5990 | partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 1 |  |  |  |  | FALSE |
| 5991 | ads\_in\_slot\_\_advertisement\_\_slot\_index | 1 |  |  |  |  | FALSE |
| 5992 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_slot\_index | 1 |  |  |  |  | FALSE |
| 5993 | ads\_in\_slot\_\_advertisement\_\_ad\_delivery\_method | 1 |  |  |  |  | FALSE |
| 5994 | ads\_in\_slot\_\_partners\_\_standard\_channel\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 5995 | ads\_in\_slot\_\_auction\_\_ab\_test\_items\_\_is\_effective | 1 |  |  |  |  | FALSE |
| 5996 | ads\_in\_slot\_\_candidate\_\_response\_time | 1 |  |  |  |  | FALSE |
| 5997 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot | 1 |  |  |  |  | FALSE |
| 5998 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_sponsorship\_check\_failed | 1 |  |  |  |  | FALSE |
| 5999 | ads\_in\_slot\_\_candidate\_\_site\_id | 1 |  |  |  |  | FALSE |
| 6000 | ads\_in\_slot\_\_partners\_\_visitor\_custom\_id\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6001 | ack\_\_metrics\_\_measurable\_ad\_expand\_collapse\_impression | 1 |  |  |  |  | FALSE |
| 6002 | ads\_in\_slot\_\_advertisement\_\_effective\_exclude\_aim\_audience\_ids | 1 |  |  |  |  | FALSE |
| 6003 | ack\_\_psn\_msg\_\_spot\_asset\_id | 1 |  |  |  |  | FALSE |
| 6004 | ads\_in\_slot\_\_candidate\_\_external\_ad\_id\_domain\_config\_id | 1 |  |  |  |  | FALSE |
| 6005 | ads\_in\_slot\_\_partners\_\_content\_form\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6006 | ads\_in\_slot\_\_partners\_\_bidding\_up\_revenue | 1 |  |  |  |  | FALSE |
| 6007 | ads\_in\_slot\_\_partners\_\_content\_rating\_visibility | 1 |  |  |  |  | FALSE |
| 6008 | ads\_in\_slot\_\_auction\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6009 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_competition\_resellers | 1 |  |  |  |  | FALSE |
| 6010 | ads\_in\_slot\_\_candidate\_\_filter\_reason\_\_slot\_index | 1 |  |  |  |  | FALSE |
| 6011 | ads\_in\_slot\_\_partners\_\_internal\_seat\_ids | 1 |  |  |  |  | FALSE |
| 6012 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_unfilled\_avails | 1 |  |  |  |  | FALSE |
| 6013 | ads\_in\_slot\_\_advertisement\_\_inbound\_rule\_\_win\_inbound\_rule\_id | 1 |  |  |  |  | FALSE |
| 6014 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_supply\_distribution\_cost | 1 |  |  |  |  | FALSE |
| 6015 | ads\_in\_slot\_\_advertisement\_\_rules\_\_win\_rule\_id | 1 |  |  |  |  | FALSE |
| 6016 | ads\_in\_slot\_\_partners\_\_standard\_content\_territory\_visibility | 1 |  |  |  |  | FALSE |
| 6017 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_matched\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 6018 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 1 |  |  |  |  | FALSE |
| 6019 | ads\_in\_slot\_\_advertisement\_\_is\_replacement | 1 |  |  |  |  | FALSE |
| 6020 | ads\_in\_slot\_\_candidate\_\_trading\_desk\_id | 1 |  |  |  |  | FALSE |
| 6021 | ads\_in\_slot\_\_auction\_\_impression\_\_bid\_floor\_uplift | 1 |  |  |  |  | FALSE |
| 6022 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_market\_avails | 1 |  |  |  |  | FALSE |
| 6023 | ads\_in\_slot\_\_advertisement\_\_triggering\_concrete\_event\_id | 1 |  |  |  |  | FALSE |
| 6024 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_reseller\_index\_in\_slot | 1 |  |  |  |  | FALSE |
| 6025 | ads\_in\_slot\_\_advertisement\_\_advertisement\_context\_\_network\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6026 | ack\_\_is\_embedded\_tracking\_ad\_event | 1 |  |  |  |  | FALSE |
| 6027 | ads\_in\_slot\_\_partners\_\_upstream\_inbound\_order\_id | 1 |  |  |  |  | FALSE |
| 6028 | ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6029 | ads\_in\_slot\_\_candidate\_\_clock\_number | 1 |  |  |  |  | FALSE |
| 6030 | ads\_in\_slot\_\_partners\_\_outbound\_order\_transaction\_type | 1 |  |  |  |  | FALSE |
| 6031 | ads\_in\_slot\_\_advertisement\_\_replaced\_ad\_id | 1 |  |  |  |  | FALSE |
| 6032 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_input\_ad\_number | 1 |  |  |  |  | FALSE |
| 6033 | ads\_in\_slot\_\_candidate\_\_ad\_id | 1 |  |  |  |  | FALSE |
| 6034 | ads\_in\_slot\_\_advertisement\_\_matched\_contextual\_segment\_ids | 1 |  |  |  |  | FALSE |
| 6035 | ads\_in\_slot\_\_partners\_\_ip\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6036 | ads\_in\_slot\_\_candidate\_\_original\_price | 1 |  |  |  |  | FALSE |
| 6037 | ads\_in\_slot\_\_auction\_\_invite\_deal\_size | 1 |  |  |  |  | FALSE |
| 6038 | ads\_in\_slot\_\_partners\_\_selected\_yo\_inventory\_prioritization\_id | 1 |  |  |  |  | FALSE |
| 6039 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inbound\_order\_competition\_failure | 1 |  |  |  |  | FALSE |
| 6040 | ads\_in\_slot\_\_auction\_\_impression\_\_max\_duration | 1 |  |  |  |  | FALSE |
| 6041 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_inventory\_source\_restriction | 1 |  |  |  |  | FALSE |
| 6042 | ads\_in\_slot\_\_advertisement\_\_variant\_creative\_ids | 1 |  |  |  |  | FALSE |
| 6043 | ads\_in\_slot\_\_candidate\_\_filter\_reason\_\_error | 1 |  |  |  |  | FALSE |
| 6044 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_bidding\_down\_revenue | 1 |  |  |  |  | FALSE |
| 6045 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_distinct\_inventory\_avails | 1 |  |  |  |  | FALSE |
| 6046 | ack\_\_psn\_msg\_\_subscribe\_id | 1 |  |  |  |  | FALSE |
| 6047 | ads\_in\_slot\_\_advertisement\_\_fallback\_ad\_uniq\_id | 1 |  |  |  |  | FALSE |
| 6048 | ads\_in\_slot\_\_partners\_\_postal\_code\_package\_id | 1 |  |  |  |  | FALSE |
| 6049 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6050 | ads\_in\_slot\_\_partners\_\_edge\_postal\_code\_package\_ids | 1 |  |  |  |  | FALSE |
| 6051 | ack\_\_metrics\_\_cpx\_targeted\_event\_count | 1 |  |  |  |  | FALSE |
| 6052 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_root\_asset\_id | 1 |  |  |  |  | FALSE |
| 6053 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_site\_id | 1 |  |  |  |  | FALSE |
| 6054 | ads\_in\_slot\_\_candidate\_\_media\_buyer\_id | 1 |  |  |  |  | FALSE |
| 6055 | ads\_in\_slot\_\_partners\_\_geo\_dma\_visibility | 1 |  |  |  |  | FALSE |
| 6056 | ads\_in\_slot\_\_advertisement\_\_shading\_context\_\_bid\_price\_usd | 1 |  |  |  |  | FALSE |
| 6057 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_filled\_ad\_num | 1 |  |  |  |  | FALSE |
| 6058 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_matched\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 6059 | ack\_\_metrics\_\_ad\_unmute | 1 |  |  |  |  | FALSE |
| 6060 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_order\_id | 1 |  |  |  |  | FALSE |
| 6061 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_exclusivity | 1 |  |  |  |  | FALSE |
| 6062 | ads\_in\_slot\_\_partners\_\_outbound\_rules\_\_rule\_id | 1 |  |  |  |  | FALSE |
| 6063 | ads\_in\_slot\_\_partners\_\_inbound\_order\_auction\_type | 1 |  |  |  |  | FALSE |
| 6064 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_series\_id | 1 |  |  |  |  | FALSE |
| 6065 | ads\_in\_slot\_\_advertisement\_\_validation\_event\_\_denominator\_event\_id | 1 |  |  |  |  | FALSE |
| 6066 | ads\_in\_slot\_\_auction\_\_metadata\_auditing\_flags | 1 |  |  |  |  | FALSE |
| 6067 | execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 1 |  |  |  |  | FALSE |
| 6068 | partners\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 1 |  |  |  |  | FALSE |
| 6069 | ads\_in\_slot\_\_partners\_\_priority\_value | 1 |  |  |  |  | FALSE |
| 6070 | ack\_\_metrics\_\_measurable\_ad\_close\_impression | 1 |  |  |  |  | FALSE |
| 6071 | ads\_in\_slot\_\_partners\_\_custom\_platform\_ids | 1 |  |  |  |  | FALSE |
| 6072 | ads\_in\_slot\_\_partners\_\_outbound\_order\_ids | 1 |  |  |  |  | FALSE |
| 6073 | ads\_in\_slot\_\_auction\_\_privacy\_flags | 1 |  |  |  |  | FALSE |
| 6074 | ads\_in\_slot\_\_advertisement\_\_error\_domain | 1 |  |  |  |  | FALSE |
| 6075 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category | 1 |  |  |  |  | FALSE |
| 6076 | ads\_in\_slot\_\_partners\_\_scenario\_id | 1 |  |  |  |  | FALSE |
| 6077 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_max\_ad\_duration\_check\_failed | 1 |  |  |  |  | FALSE |
| 6078 | ads\_in\_slot\_\_partners\_\_standard\_language\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6079 | execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments | 1 |  |  |  |  | FALSE |
| 6080 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_exclusivity\_check\_failed | 1 |  |  |  |  | FALSE |
| 6081 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_rule\_priority | 1 |  |  |  |  | FALSE |
| 6082 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_count\_true\_avails\_as\_booked | 1 |  |  |  |  | FALSE |
| 6083 | ads\_in\_slot\_\_partners\_\_third\_party\_user\_id\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6084 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_suitable\_rule\_path | 1 |  |  |  |  | FALSE |
| 6085 | ads\_in\_slot\_\_partners\_\_user\_agent\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6086 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_visibility | 1 |  |  |  |  | FALSE |
| 6087 | ads\_in\_slot\_\_partners\_\_content\_rating\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6088 | ads\_in\_slot\_\_candidate\_\_mpe\_deduction\_on\_selection\_fixed\_fee | 1 |  |  |  |  | FALSE |
| 6089 | ads\_in\_slot\_\_advertisement\_\_extra\_flags | 1 |  |  |  |  | FALSE |
| 6090 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_remaining\_avails | 1 |  |  |  |  | FALSE |
| 6091 | ads\_in\_slot\_\_candidate\_\_discount\_barter\_\_id | 1 |  |  |  |  | FALSE |
| 6092 | ads\_in\_slot\_\_advertisement\_\_original\_bidding\_price | 1 |  |  |  |  | FALSE |
| 6093 | execution\_networks\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 1 |  |  |  |  | FALSE |
| 6094 | ads\_in\_slot\_\_partners\_\_ssp\_clearing\_revenue | 1 |  |  |  |  | FALSE |
| 6095 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_order\_id | 1 |  |  |  |  | FALSE |
| 6096 | ads\_in\_slot\_\_partners\_\_standard\_content\_series\_visibility | 1 |  |  |  |  | FALSE |
| 6097 | ads\_in\_slot\_\_auction\_\_experiment\_\_experiment\_id | 1 |  |  |  |  | FALSE |
| 6098 | ads\_in\_slot\_\_partners\_\_outbound\_rules | 1 |  |  |  |  | FALSE |
| 6099 | ads\_in\_slot\_\_candidate\_\_cch\_key\_domain\_config\_id | 1 |  |  |  |  | FALSE |
| 6100 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_rule\_flags | 1 |  |  |  |  | FALSE |
| 6101 | ads\_in\_slot\_\_partners\_\_reseller\_bidding\_revenue | 1 |  |  |  |  | FALSE |
| 6102 | ads\_in\_slot\_\_partners\_\_content\_rating\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6103 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_order\_buyer\_network\_id | 1 |  |  |  |  | FALSE |
| 6104 | ads\_in\_slot\_\_advertisement\_\_external\_reseller | 1 |  |  |  |  | FALSE |
| 6105 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_inbound\_rule\_id | 1 |  |  |  |  | FALSE |
| 6106 | ack\_\_callback\_info | 1 |  |  |  |  | FALSE |
| 6107 | ads\_in\_slot\_\_partners\_\_ip\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6108 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_vod\_programmer\_total\_avails | 1 |  |  |  |  | FALSE |
| 6109 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_listing\_ids | 1 |  |  |  |  | FALSE |
| 6110 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_resellable | 1 |  |  |  |  | FALSE |
| 6111 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 1 |  |  |  |  | FALSE |
| 6112 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_creative\_targeting\_check\_failed | 1 |  |  |  |  | FALSE |
| 6113 | execution\_networks\_\_bidding\_up\_revenue | 1 |  |  |  |  | FALSE |
| 6114 | ads\_in\_slot\_\_auction\_\_auction\_network\_to\_eur\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 6115 | ads\_in\_slot\_\_auction\_\_ab\_test\_items\_\_collection\_id | 1 |  |  |  |  | FALSE |
| 6116 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails | 1 |  |  |  |  | FALSE |
| 6117 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_bidding\_revenue | 1 |  |  |  |  | FALSE |
| 6118 | ads\_in\_slot\_\_auction\_\_is\_order\_prog\_auction | 1 |  |  |  |  | FALSE |
| 6119 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics | 1 |  |  |  |  | FALSE |
| 6120 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_applicable\_slot\_excluded\_by\_sponsor | 1 |  |  |  |  | FALSE |
| 6121 | ads\_in\_slot\_\_advertisement\_\_matched\_user\_agent\_ids | 1 |  |  |  |  | FALSE |
| 6122 | ads\_in\_slot\_\_partners\_\_geo\_zip\_code\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6123 | ads\_in\_slot\_\_advertisement\_\_validation\_event\_\_numerator\_event\_id | 1 |  |  |  |  | FALSE |
| 6124 | ads\_in\_slot\_\_advertisement\_\_position\_in\_slot | 1 |  |  |  |  | FALSE |
| 6125 | ack\_\_psn\_msg\_\_ad\_unit\_type | 1 |  |  |  |  | FALSE |
| 6126 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_avails\_metrics\_\_avails | 1 |  |  |  |  | FALSE |
| 6127 | ads\_in\_slot\_\_partners\_\_standard\_programmer\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6128 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_promo\_only | 1 |  |  |  |  | FALSE |
| 6129 | ads\_in\_slot\_\_auction\_\_is\_market\_auction | 1 |  |  |  |  | FALSE |
| 6130 | ads\_in\_slot\_\_advertisement\_\_targeted\_ratio | 1 |  |  |  |  | FALSE |
| 6131 | ads\_in\_slot\_\_partners\_\_selected\_yield\_optimization\_info\_ids | 1 |  |  |  |  | FALSE |
| 6132 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_owner\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6133 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_nested\_sub\_yo\_ids | 1 |  |  |  |  | FALSE |
| 6134 | ads\_in\_slot\_\_advertisement\_\_advertisement\_context | 1 |  |  |  |  | FALSE |
| 6135 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_max\_cpm | 1 |  |  |  |  | FALSE |
| 6136 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_ssp\_avails | 1 |  |  |  |  | FALSE |
| 6137 | ack\_\_callback\_info\_\_flag1 | 1 |  |  |  |  | FALSE |
| 6138 | ack\_\_is\_faked | 1 |  |  |  |  | FALSE |
| 6139 | ads\_in\_slot\_\_candidate\_\_bid\_replica\_id | 1 |  |  |  |  | FALSE |
| 6140 | ads\_in\_slot\_\_auction\_\_trading\_desk\_id | 1 |  |  |  |  | FALSE |
| 6141 | ads\_in\_slot\_\_candidate\_\_dsp\_adid | 1 |  |  |  |  | FALSE |
| 6142 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_frequency\_cap | 1 |  |  |  |  | FALSE |
| 6143 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_default\_unfilled\_opp | 1 |  |  |  |  | FALSE |
| 6144 | ads\_in\_slot\_\_partners\_\_mapped\_site\_section\_ids | 1 |  |  |  |  | FALSE |
| 6145 | ads\_in\_slot\_\_partners\_\_standard\_content\_credential\_status\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6146 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_market\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6147 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_ad\_num | 1 |  |  |  |  | FALSE |
| 6148 | partners\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 1 |  |  |  |  | FALSE |
| 6149 | ads\_in\_slot\_\_auction\_\_internal\_seat\_id | 1 |  |  |  |  | FALSE |
| 6150 | ads\_in\_slot\_\_partners\_\_standard\_content\_territory\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6151 | ads\_in\_slot\_\_candidate\_\_dsp\_cid | 1 |  |  |  |  | FALSE |
| 6152 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_site\_section\_group\_id | 1 |  |  |  |  | FALSE |
| 6153 | ads\_in\_slot\_\_advertisement\_\_inbound\_rule\_\_network\_id | 1 |  |  |  |  | FALSE |
| 6154 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_remaining\_avails | 1 |  |  |  |  | FALSE |
| 6155 | ads\_in\_slot\_\_partners\_\_geo\_city\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6156 | ads\_in\_slot\_\_partners\_\_asset\_id | 1 |  |  |  |  | FALSE |
| 6157 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_is\_auction\_rule | 1 |  |  |  |  | FALSE |
| 6158 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_owner\_visibility | 1 |  |  |  |  | FALSE |
| 6159 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_market\_ad\_not\_approved | 1 |  |  |  |  | FALSE |
| 6160 | ads\_in\_slot\_\_partners\_\_standard\_channel\_visibility | 1 |  |  |  |  | FALSE |
| 6161 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_order\_id | 1 |  |  |  |  | FALSE |
| 6162 | ads\_in\_slot\_\_candidate\_\_mbd\_deduction\_on\_selection\_ratio | 1 |  |  |  |  | FALSE |
| 6163 | ads\_in\_slot\_\_partners\_\_upstream\_global\_currency\_id | 1 |  |  |  |  | FALSE |
| 6164 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_ad\_priority\_bucket | 1 |  |  |  |  | FALSE |
| 6165 | ads\_in\_slot\_\_partners\_\_key\_value\_visibility | 1 |  |  |  |  | FALSE |
| 6166 | ads\_in\_slot\_\_candidate\_\_has\_advertisement | 1 |  |  |  |  | FALSE |
| 6167 | ads\_in\_slot\_\_advertisement\_\_fill\_rate | 1 |  |  |  |  | FALSE |
| 6168 | ads\_in\_slot\_\_candidate\_\_sfx\_dsp\_id | 1 |  |  |  |  | FALSE |
| 6169 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_frequency\_cap | 1 |  |  |  |  | FALSE |
| 6170 | ads\_in\_slot\_\_partners\_\_airing\_channel\_id | 1 |  |  |  |  | FALSE |
| 6171 | ads\_in\_slot\_\_partners\_\_eligible\_carriage\_listing\_split\_unit\_ids | 1 |  |  |  |  | FALSE |
| 6172 | ads\_in\_slot\_\_partners\_\_standard\_content\_daypart\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6173 | ads\_in\_slot\_\_candidate\_\_bidding\_seat\_id | 1 |  |  |  |  | FALSE |
| 6174 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_supply\_acquisition\_cost | 1 |  |  |  |  | FALSE |
| 6175 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_avails | 1 |  |  |  |  | FALSE |
| 6176 | ads\_in\_slot\_\_partners\_\_portfolio\_ids | 1 |  |  |  |  | FALSE |
| 6177 | ads\_in\_slot\_\_partners\_\_standard\_content\_subscription\_model\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6178 | ads\_in\_slot\_\_advertisement\_\_rules | 1 |  |  |  |  | FALSE |
| 6179 | ads\_in\_slot\_\_candidate\_\_has\_auction | 1 |  |  |  |  | FALSE |
| 6180 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_buyers\_\_buyer\_id | 1 |  |  |  |  | FALSE |
| 6181 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_slot\_compatible\_dimension\_check\_failed | 1 |  |  |  |  | FALSE |
| 6182 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_fallback\_ad\_number | 1 |  |  |  |  | FALSE |
| 6183 | ads\_in\_slot\_\_candidate\_\_exchange\_order\_id | 1 |  |  |  |  | FALSE |
| 6184 | ads\_in\_slot\_\_partners\_\_bidder\_seat\_id | 1 |  |  |  |  | FALSE |
| 6185 | ads\_in\_slot\_\_advertisement\_\_is\_uy\_replaced | 1 |  |  |  |  | FALSE |
| 6186 | ads\_in\_slot\_\_advertisement\_\_abstract\_event\_id | 1 |  |  |  |  | FALSE |
| 6187 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_unmapped | 1 |  |  |  |  | FALSE |
| 6188 | ads\_in\_slot\_\_candidate\_\_rtb\_impression\_index | 1 |  |  |  |  | FALSE |
| 6189 | ads\_in\_slot\_\_candidate\_\_vast\_creative\_id | 1 |  |  |  |  | FALSE |
| 6190 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot | 1 |  |  |  |  | FALSE |
| 6191 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_rule\_id | 1 |  |  |  |  | FALSE |
| 6192 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6193 | ads\_in\_slot\_\_partners\_\_geo\_state\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6194 | ads\_in\_slot\_\_partners\_\_matched\_key\_value\_ids | 1 |  |  |  |  | FALSE |
| 6195 | ads\_in\_slot\_\_auction\_\_impression\_\_matched\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 6196 | ack\_\_metrics\_\_ad\_net\_avail | 1 |  |  |  |  | FALSE |
| 6197 | ads\_in\_slot\_\_partners\_\_carriage\_listing\_split\_unit\_id | 1 |  |  |  |  | FALSE |
| 6198 | ads\_in\_slot\_\_auction\_\_auction\_network\_context\_index | 1 |  |  |  |  | FALSE |
| 6199 | ads\_in\_slot\_\_advertisement\_\_rendition\_id | 1 |  |  |  |  | FALSE |
| 6200 | ads\_in\_slot\_\_partners\_\_count\_imp\_as\_booked | 1 |  |  |  |  | FALSE |
| 6201 | ads\_in\_slot\_\_partners\_\_standard\_programmer\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6202 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6203 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_duration | 1 |  |  |  |  | FALSE |
| 6204 | ads\_in\_slot\_\_partners\_\_standard\_content\_daypart\_visibility | 1 |  |  |  |  | FALSE |
| 6205 | ads\_in\_slot\_\_candidate\_\_discount\_post\_auction\_\_id | 1 |  |  |  |  | FALSE |
| 6206 | ads\_in\_slot\_\_advertisement\_\_replaced\_placement\_id | 1 |  |  |  |  | FALSE |
| 6207 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_unified\_rule\_priority | 1 |  |  |  |  | FALSE |
| 6208 | ads\_in\_slot\_\_advertisement\_\_validation\_event | 1 |  |  |  |  | FALSE |
| 6209 | ads\_in\_slot\_\_partners\_\_content\_form\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6210 | ads\_in\_slot\_\_auction\_\_dynamic\_floor\_price\_algorithm | 1 |  |  |  |  | FALSE |
| 6211 | ads\_in\_slot\_\_partners\_\_inventory\_distribution\_contexts | 1 |  |  |  |  | FALSE |
| 6212 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_ad\_truncation | 1 |  |  |  |  | FALSE |
| 6213 | ads\_in\_slot\_\_auction\_\_media\_buyer\_id | 1 |  |  |  |  | FALSE |
| 6214 | ads\_in\_slot\_\_candidate\_\_discount\_post\_auction\_\_amount | 1 |  |  |  |  | FALSE |
| 6215 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_model\_info\_\_model\_id | 1 |  |  |  |  | FALSE |
| 6216 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6217 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_max\_num\_ads | 1 |  |  |  |  | FALSE |
| 6218 | ads\_in\_slot\_\_auction\_\_execution\_contexts | 1 |  |  |  |  | FALSE |
| 6219 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_restriction | 1 |  |  |  |  | FALSE |
| 6220 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders | 1 |  |  |  |  | FALSE |
| 6221 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_undefined | 1 |  |  |  |  | FALSE |
| 6222 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_bidding\_up\_modified\_revenue | 1 |  |  |  |  | FALSE |
| 6223 | ads\_in\_slot\_\_advertisement\_\_estimated\_start\_delay | 1 |  |  |  |  | FALSE |
| 6224 | ads\_in\_slot\_\_advertisement\_\_inbound\_rule | 1 |  |  |  |  | FALSE |
| 6225 | ads\_in\_slot\_\_partners\_\_opportunity\_id | 1 |  |  |  |  | FALSE |
| 6226 | ads\_in\_slot\_\_advertisement\_\_agency\_id | 1 |  |  |  |  | FALSE |
| 6227 | ads\_in\_slot\_\_auction\_\_external\_network\_id | 1 |  |  |  |  | FALSE |
| 6228 | ads\_in\_slot\_\_auction\_\_auction\_network\_to\_usd\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 6229 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails | 1 |  |  |  |  | FALSE |
| 6230 | ack\_\_metrics\_\_ad\_pause | 1 |  |  |  |  | FALSE |
| 6231 | ads\_in\_slot\_\_partners\_\_programmatic\_exchange\_rate\_to\_usd | 1 |  |  |  |  | FALSE |
| 6232 | ads\_in\_slot\_\_partners\_\_distributor\_revenue | 1 |  |  |  |  | FALSE |
| 6233 | ack\_\_metrics\_\_indicator\_event\_count | 1 |  |  |  |  | FALSE |
| 6234 | ads\_in\_slot\_\_auction\_\_mkpl\_partner\_tags\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6235 | ack\_\_metrics\_\_ad\_unconstrained\_gross\_avail | 1 |  |  |  |  | FALSE |
| 6236 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_avails | 1 |  |  |  |  | FALSE |
| 6237 | ads\_in\_slot\_\_partners\_\_standard\_endpoint\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6238 | ads\_in\_slot\_\_advertisement\_\_matched\_audience\_item\_ids | 1 |  |  |  |  | FALSE |
| 6239 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_market\_avails | 1 |  |  |  |  | FALSE |
| 6240 | ads\_in\_slot\_\_advertisement\_\_billable\_rate\_denominator\_event\_id | 1 |  |  |  |  | FALSE |
| 6241 | ack\_\_user\_id | 1 |  |  |  |  | FALSE |
| 6242 | ads\_in\_slot\_\_candidate\_\_response\_time\_first\_hop | 1 |  |  |  |  | FALSE |
| 6243 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_unified\_rule\_priority\_\_priority\_tier | 1 |  |  |  |  | FALSE |
| 6244 | ads\_in\_slot\_\_partners\_\_selected\_yo\_distribution\_nip\_id | 1 |  |  |  |  | FALSE |
| 6245 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_unfilled\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6246 | ack\_\_yield\_optimization\_ids | 1 |  |  |  |  | FALSE |
| 6247 | ads\_in\_slot\_\_partners\_\_third\_party\_user\_id\_visibility | 1 |  |  |  |  | FALSE |
| 6248 | ads\_in\_slot\_\_advertisement\_\_extra\_flags2 | 1 |  |  |  |  | FALSE |
| 6249 | ads\_in\_slot\_\_partners\_\_standard\_channel\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6250 | ads\_in\_slot\_\_partners\_\_outbound\_order\_type | 1 |  |  |  |  | FALSE |
| 6251 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity | 1 |  |  |  |  | FALSE |
| 6252 | ads\_in\_slot\_\_partners\_\_unified\_outbound\_order\_priority | 1 |  |  |  |  | FALSE |
| 6253 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_raw\_opportunity\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6254 | ack\_\_custom\_ad\_price | 1 |  |  |  |  | FALSE |
| 6255 | ack\_\_psn\_msg\_\_plc\_start\_time | 1 |  |  |  |  | FALSE |
| 6256 | ack\_\_kafka\_msg\_size | 1 |  |  |  |  | FALSE |
| 6257 | ads\_in\_slot\_\_partners\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 1 |  |  |  |  | FALSE |
| 6258 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_compliance\_check\_failed | 1 |  |  |  |  | FALSE |
| 6259 | ack\_\_ad\_unit\_id | 1 |  |  |  |  | FALSE |
| 6260 | ack\_\_start\_time\_position | 1 |  |  |  |  | FALSE |
| 6261 | ads\_in\_slot\_\_partners\_\_geo\_zip\_code\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6262 | ads\_in\_slot\_\_partners\_\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 6263 | ads\_in\_slot\_\_advertisement\_\_global\_brand\_id | 1 |  |  |  |  | FALSE |
| 6264 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6265 | ads\_in\_slot\_\_auction\_\_auction\_sampling\_\_magnifier | 1 |  |  |  |  | FALSE |
| 6266 | ads\_in\_slot\_\_advertisement\_\_contextual\_billings | 1 |  |  |  |  | FALSE |
| 6267 | ads\_in\_slot\_\_advertisement\_\_active\_aim\_audience\_ids | 1 |  |  |  |  | FALSE |
| 6268 | ads\_in\_slot\_\_partners\_\_standard\_content\_subscription\_model\_visibility | 1 |  |  |  |  | FALSE |
| 6269 | ads\_in\_slot\_\_partners\_\_supply\_source\_type | 1 |  |  |  |  | FALSE |
| 6270 | ads\_in\_slot\_\_advertisement\_\_cch\_key\_domain\_config\_id | 1 |  |  |  |  | FALSE |
| 6271 | ads\_in\_slot\_\_partners\_\_standard\_content\_territory\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6272 | ack\_\_psn\_msg\_\_spot\_provider\_id | 1 |  |  |  |  | FALSE |
| 6273 | ads\_in\_slot\_\_candidate | 1 |  |  |  |  | FALSE |
| 6274 | ads\_in\_slot\_\_partners\_\_buyer\_ids | 1 |  |  |  |  | FALSE |
| 6275 | ads\_in\_slot\_\_advertisement\_\_matched\_postal\_code\_package\_ids | 1 |  |  |  |  | FALSE |
| 6276 | ads\_in\_slot\_\_candidate\_\_trust\_id | 1 |  |  |  |  | FALSE |
| 6277 | ack\_\_psn\_msg\_\_plc\_end\_time | 1 |  |  |  |  | FALSE |
| 6278 | ads\_in\_slot\_\_partners\_\_mapped\_asset\_ids | 1 |  |  |  |  | FALSE |
| 6279 | ads\_in\_slot\_\_partners\_\_standard\_genre\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6280 | ads\_in\_slot\_\_advertisement\_\_rules\_flags | 1 |  |  |  |  | FALSE |
| 6281 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_raw\_inventory\_distinct\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6282 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_data\_privacy | 1 |  |  |  |  | FALSE |
| 6283 | ack\_\_metrics\_\_cpx\_revenue\_ratio | 1 |  |  |  |  | FALSE |
| 6284 | ads\_in\_slot\_\_partners\_\_rule\_flags | 1 |  |  |  |  | FALSE |
| 6285 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_no\_creative | 1 |  |  |  |  | FALSE |
| 6286 | ads\_in\_slot\_\_partners\_\_content\_owner\_revenue | 1 |  |  |  |  | FALSE |
| 6287 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_pod\_position\_targeting\_check\_failed | 1 |  |  |  |  | FALSE |
| 6288 | ads\_in\_slot\_\_candidate\_\_post\_auction\_discount\_id | 1 |  |  |  |  | FALSE |
| 6289 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_companion\_check\_failed | 1 |  |  |  |  | FALSE |
| 6290 | ads\_in\_slot\_\_partners\_\_standard\_content\_series\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6291 | ads\_in\_slot\_\_advertisement\_\_has\_candidate | 1 |  |  |  |  | FALSE |
| 6292 | ack\_\_metrics\_\_concrete\_event\_measurable\_ad\_views | 1 |  |  |  |  | FALSE |
| 6293 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_sales\_channel | 1 |  |  |  |  | FALSE |
| 6294 | ads\_in\_slot\_\_auction\_\_index | 1 |  |  |  |  | FALSE |
| 6295 | ack\_\_metrics\_\_measurable\_ad\_accept\_invitation\_minimize\_impression | 1 |  |  |  |  | FALSE |
| 6296 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_cpx\_check\_failed | 1 |  |  |  |  | FALSE |
| 6297 | ads\_in\_slot\_\_partners\_\_ad\_unit\_default\_duration | 1 |  |  |  |  | FALSE |
| 6298 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info\_\_exempt\_thousandth | 1 |  |  |  |  | FALSE |
| 6299 | ack\_\_yield\_optimization\_ids\_\_optimization\_ids | 1 |  |  |  |  | FALSE |
| 6300 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_up\_revenue | 1 |  |  |  |  | FALSE |
| 6301 | ads\_in\_slot\_\_candidate\_\_deal\_id | 1 |  |  |  |  | FALSE |
| 6302 | ads\_in\_slot\_\_partners\_\_standard\_channel\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6303 | ads\_in\_slot\_\_partners\_\_network\_execution\_ctx\_flags | 1 |  |  |  |  | FALSE |
| 6304 | ads\_in\_slot\_\_partners\_\_airing\_id | 1 |  |  |  |  | FALSE |
| 6305 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_substitute\_type | 1 |  |  |  |  | FALSE |
| 6306 | ads\_in\_slot\_\_auction\_\_app\_storeurl | 1 |  |  |  |  | FALSE |
| 6307 | ads\_in\_slot\_\_advertisement\_\_booked\_percentage | 1 |  |  |  |  | FALSE |
| 6308 | ads\_in\_slot\_\_advertisement\_\_replaced\_ad\_bit\_flags | 1 |  |  |  |  | FALSE |
| 6309 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_listing\_id | 1 |  |  |  |  | FALSE |
| 6310 | ads\_in\_slot\_\_auction\_\_impression | 1 |  |  |  |  | FALSE |
| 6311 | ads\_in\_slot\_\_candidate\_\_rtb\_impression\_id | 1 |  |  |  |  | FALSE |
| 6312 | ads\_in\_slot\_\_partners\_\_geo\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6313 | ads\_in\_slot\_\_partners\_\_visitor\_custom\_id\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6314 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_marketplace\_audience\_extension\_deal\_id | 1 |  |  |  |  | FALSE |
| 6315 | ads\_in\_slot\_\_partners\_\_tracked\_audience\_item\_ids | 1 |  |  |  |  | FALSE |
| 6316 | ads\_in\_slot\_\_advertisement\_\_ad\_opportunity\_rules\_\_rule\_id | 1 |  |  |  |  | FALSE |
| 6317 | ads\_in\_slot\_\_advertisement\_\_global\_industry\_ids | 1 |  |  |  |  | FALSE |
| 6318 | ads\_in\_slot\_\_partners\_\_geo\_dma\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6319 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_type | 1 |  |  |  |  | FALSE |
| 6320 | ads\_in\_slot\_\_partners\_\_content\_owner\_bidding\_modified\_revenue | 1 |  |  |  |  | FALSE |
| 6321 | ack\_\_metrics\_\_ad\_mute | 1 |  |  |  |  | FALSE |
| 6322 | ads\_in\_slot\_\_partners\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6323 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics | 1 |  |  |  |  | FALSE |
| 6324 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_no\_external\_rule | 1 |  |  |  |  | FALSE |
| 6325 | ack\_\_ivt\_tracked\_info | 1 |  |  |  |  | FALSE |
| 6326 | ads\_in\_slot\_\_partners\_\_selected\_yo\_distribution\_id | 1 |  |  |  |  | FALSE |
| 6327 | ads\_in\_slot\_\_advertisement\_\_replaced\_rendition\_id | 1 |  |  |  |  | FALSE |
| 6328 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_opportunity\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6329 | ads\_in\_slot\_\_partners\_\_standard\_content\_subscription\_model\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6330 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_exclusivity\_check\_failed | 1 |  |  |  |  | FALSE |
| 6331 | ads\_in\_slot\_\_auction\_\_bid\_throttling\_info | 1 |  |  |  |  | FALSE |
| 6332 | ads\_in\_slot\_\_advertisement\_\_is\_ax | 1 |  |  |  |  | FALSE |
| 6333 | ads\_in\_slot\_\_advertisement\_\_data\_provider\_id | 1 |  |  |  |  | FALSE |
| 6334 | ack\_\_insertion\_status | 1 |  |  |  |  | FALSE |
| 6335 | ads\_in\_slot\_\_candidate\_\_creative\_approval\_request\_\_approval\_type | 1 |  |  |  |  | FALSE |
| 6336 | ads\_in\_slot\_\_candidate\_\_bsi\_id | 1 |  |  |  |  | FALSE |
| 6337 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_initial\_filled\_duration | 1 |  |  |  |  | FALSE |
| 6338 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_unfilled\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6339 | ack\_\_psn\_msg\_\_terminal\_addr | 1 |  |  |  |  | FALSE |
| 6340 | ads\_in\_slot\_\_candidate\_\_discount\_barter | 1 |  |  |  |  | FALSE |
| 6341 | ads\_in\_slot\_\_partners\_\_geo\_dma\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6342 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_input\_ad\_number | 1 |  |  |  |  | FALSE |
| 6343 | ads\_in\_slot\_\_advertisement\_\_provider\_measured\_event\_id | 1 |  |  |  |  | FALSE |
| 6344 | ads\_in\_slot\_\_candidate\_\_playlist\_response\_time | 1 |  |  |  |  | FALSE |
| 6345 | ack\_\_metrics\_\_measurable\_ad\_mute\_unmute\_impression | 1 |  |  |  |  | FALSE |
| 6346 | ack\_\_is\_tracking\_url\_event | 1 |  |  |  |  | FALSE |
| 6347 | ads\_in\_slot\_\_advertisement\_\_xdevice\_policy\_id | 1 |  |  |  |  | FALSE |
| 6348 | ads\_in\_slot\_\_candidate\_\_redirect\_count | 1 |  |  |  |  | FALSE |
| 6349 | ack\_\_psn\_msg\_\_distributor\_id | 1 |  |  |  |  | FALSE |
| 6350 | ack\_\_capabilities | 1 |  |  |  |  | FALSE |
| 6351 | ads\_in\_slot\_\_candidate\_\_two\_phase\_translated | 1 |  |  |  |  | FALSE |
| 6352 | ads\_in\_slot\_\_partners\_\_third\_party\_user\_id\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6353 | ads\_in\_slot\_\_partners\_\_supply\_acquisition\_cost | 1 |  |  |  |  | FALSE |
| 6354 | ads\_in\_slot\_\_advertisement\_\_recommended\_bidding\_price | 1 |  |  |  |  | FALSE |
| 6355 | ads\_in\_slot\_\_partners\_\_network\_is\_ad\_unit\_owner | 1 |  |  |  |  | FALSE |
| 6356 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_unified\_unfilled\_opp | 1 |  |  |  |  | FALSE |
| 6357 | ack\_\_identifier | 1 |  |  |  |  | FALSE |
| 6358 | ads\_in\_slot\_\_advertisement\_\_net\_price | 1 |  |  |  |  | FALSE |
| 6359 | ads\_in\_slot\_\_advertisement\_\_rbp\_flag | 1 |  |  |  |  | FALSE |
| 6360 | ack\_\_metrics\_\_ad\_expand | 1 |  |  |  |  | FALSE |
| 6361 | ads\_in\_slot\_\_candidate\_\_zone\_id | 1 |  |  |  |  | FALSE |
| 6362 | ads\_in\_slot\_\_partners\_\_standard\_language\_visibility | 1 |  |  |  |  | FALSE |
| 6363 | ads\_in\_slot\_\_candidate\_\_ortb\_fwpartners | 1 |  |  |  |  | FALSE |
| 6364 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_not\_compatible | 1 |  |  |  |  | FALSE |
| 6365 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_ad\_domain | 1 |  |  |  |  | FALSE |
| 6366 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_do\_not\_repeat | 1 |  |  |  |  | FALSE |
| 6367 | ack\_\_data\_source | 1 |  |  |  |  | FALSE |
| 6368 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6369 | ack\_\_event\_provider | 1 |  |  |  |  | FALSE |
| 6370 | ack\_\_metrics\_\_fire\_margin\_ratio | 1 |  |  |  |  | FALSE |
| 6371 | ads\_in\_slot\_\_partners\_\_standard\_genre\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6372 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_order\_priority | 1 |  |  |  |  | FALSE |
| 6373 | ads\_in\_slot\_\_advertisement\_\_linear\_decision\_type | 1 |  |  |  |  | FALSE |
| 6374 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_replaced\_guaranteed\_ad\_id | 1 |  |  |  |  | FALSE |
| 6375 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos | 1 |  |  |  |  | FALSE |
| 6376 | ads\_in\_slot\_\_partners\_\_carriage\_inventory\_owner\_id | 1 |  |  |  |  | FALSE |
| 6377 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_margin | 1 |  |  |  |  | FALSE |
| 6378 | ack\_\_custom\_ad\_id | 1 |  |  |  |  | FALSE |
| 6379 | ads\_in\_slot\_\_auction\_\_impression\_\_equivalent\_opportunity\_number | 1 |  |  |  |  | FALSE |
| 6380 | ads\_in\_slot\_\_partners\_\_ip\_visibility | 1 |  |  |  |  | FALSE |
| 6381 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_met\_yield\_optimization | 1 |  |  |  |  | FALSE |
| 6382 | ack | 1 |  |  |  |  | FALSE |
| 6383 | ack\_\_is\_callback\_faked\_slot\_impression | 1 |  |  |  |  | FALSE |
| 6384 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_raw\_total\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6385 | ads\_in\_slot\_\_partners\_\_key\_value\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6386 | ack\_\_metrics\_\_ad\_resume | 1 |  |  |  |  | FALSE |
| 6387 | ads\_in\_slot\_\_partners\_\_avails\_category | 1 |  |  |  |  | FALSE |
| 6388 | ads\_in\_slot\_\_partners\_\_geo\_zip\_code\_visibility | 1 |  |  |  |  | FALSE |
| 6389 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_no\_creative\_bitrate\_check\_failed | 1 |  |  |  |  | FALSE |
| 6390 | ads\_in\_slot\_\_partners\_\_priority\_type | 1 |  |  |  |  | FALSE |
| 6391 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_competition\_failure\_in\_pick\_many | 1 |  |  |  |  | FALSE |
| 6392 | ack\_\_process\_timestamp | 1 |  |  |  |  | FALSE |
| 6393 | ads\_in\_slot\_\_advertisement\_\_relative\_priority | 1 |  |  |  |  | FALSE |
| 6394 | ads\_in\_slot\_\_advertisement\_\_unified\_yield\_\_replaced\_type | 1 |  |  |  |  | FALSE |
| 6395 | ads\_in\_slot\_\_advertisement\_\_matched\_inventory\_package\_ids | 1 |  |  |  |  | FALSE |
| 6396 | execution\_networks\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_id | 1 |  |  |  |  | FALSE |
| 6397 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status\_\_available\_duration | 1 |  |  |  |  | FALSE |
| 6398 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics | 1 |  |  |  |  | FALSE |
| 6399 | ads\_in\_slot\_\_advertisement\_\_rules\_\_opp\_rule\_id | 1 |  |  |  |  | FALSE |
| 6400 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_met\_yield\_optimization | 1 |  |  |  |  | FALSE |
| 6401 | ads\_in\_slot\_\_advertisement\_\_vast\_creative\_id | 1 |  |  |  |  | FALSE |
| 6402 | ads\_in\_slot\_\_partners\_\_competition\_resellers | 1 |  |  |  |  | FALSE |
| 6403 | ack\_\_metrics\_\_abstract\_event\_measurable\_ad\_views | 1 |  |  |  |  | FALSE |
| 6404 | ads\_in\_slot\_\_partners\_\_key\_value\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6405 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_pg\_deal\_bid\_throttling | 1 |  |  |  |  | FALSE |
| 6406 | ads\_in\_slot\_\_partners\_\_network\_selection\_info | 1 |  |  |  |  | FALSE |
| 6407 | ack\_\_identifier\_\_source | 1 |  |  |  |  | FALSE |
| 6408 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_bidding\_up\_revenue | 1 |  |  |  |  | FALSE |
| 6409 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_flags | 1 |  |  |  |  | FALSE |
| 6410 | ads\_in\_slot\_\_partners\_\_geo\_zip\_code\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6411 | ads\_in\_slot\_\_advertisement\_\_active\_term\_id | 1 |  |  |  |  | FALSE |
| 6412 | ack\_\_psn\_msg\_\_ad\_network\_id | 1 |  |  |  |  | FALSE |
| 6413 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_undefined | 1 |  |  |  |  | FALSE |
| 6414 | ads\_in\_slot\_\_partners\_\_geo\_country\_visibility | 1 |  |  |  |  | FALSE |
| 6415 | ads\_in\_slot\_\_candidate\_\_unified\_deal\_priority | 1 |  |  |  |  | FALSE |
| 6416 | key\_value | 1 |  |  |  |  | FALSE |
| 6417 | ads\_in\_slot\_\_advertisement\_\_priority\_bucket | 1 |  |  |  |  | FALSE |
| 6418 | ads\_in\_slot\_\_advertisement | 1 |  |  |  |  | FALSE |
| 6419 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_input\_ad\_number | 1 |  |  |  |  | FALSE |
| 6420 | ads\_in\_slot\_\_advertisement\_\_shading\_context\_\_shading\_model\_name | 1 |  |  |  |  | FALSE |
| 6421 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_total\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6422 | ads\_in\_slot\_\_auction\_\_mkpl\_partner\_tags\_\_strategy | 1 |  |  |  |  | FALSE |
| 6423 | ads\_in\_slot\_\_advertisement\_\_spot\_id | 1 |  |  |  |  | FALSE |
| 6424 | ack\_\_metrics\_\_cpx\_targeted\_currency\_ratio | 1 |  |  |  |  | FALSE |
| 6425 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_order\_type | 1 |  |  |  |  | FALSE |
| 6426 | ads\_in\_slot\_\_advertisement\_\_nielsen\_site\_url\_id | 1 |  |  |  |  | FALSE |
| 6427 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_slot\_filled\_by\_multi\_ad | 1 |  |  |  |  | FALSE |
| 6428 | ads\_in\_slot\_\_candidate\_\_ad\_replica\_id | 1 |  |  |  |  | FALSE |
| 6429 | ads\_in\_slot\_\_partners\_\_visible\_concrete\_event\_id | 1 |  |  |  |  | FALSE |
| 6430 | ads\_in\_slot\_\_advertisement\_\_error\_partner | 1 |  |  |  |  | FALSE |
| 6431 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_no\_applicable\_slot\_user\_experience | 1 |  |  |  |  | FALSE |
| 6432 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_ad\_filling\_status | 1 |  |  |  |  | FALSE |
| 6433 | ads\_in\_slot\_\_partners\_\_region\_ids | 1 |  |  |  |  | FALSE |
| 6434 | ads\_in\_slot\_\_candidate\_\_discount\_barter\_\_amount | 1 |  |  |  |  | FALSE |
| 6435 | ack\_\_metrics\_\_ad\_accept\_invitation | 1 |  |  |  |  | FALSE |
| 6436 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_restriction | 1 |  |  |  |  | FALSE |
| 6437 | ads\_in\_slot\_\_auction\_\_impression\_\_index | 1 |  |  |  |  | FALSE |
| 6438 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_auction\_type | 1 |  |  |  |  | FALSE |
| 6439 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_selected\_yield\_optimization\_infos\_\_sub\_yo\_id | 1 |  |  |  |  | FALSE |
| 6440 | ads\_in\_slot\_\_auction\_\_bid\_to\_usd\_exchange\_rate | 1 |  |  |  |  | FALSE |
| 6441 | partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 1 |  |  |  |  | FALSE |
| 6442 | ads\_in\_slot\_\_auction\_\_impression\_\_deals\_\_impression\_index | 1 |  |  |  |  | FALSE |
| 6443 | ads\_in\_slot\_\_advertisement\_\_bit\_flags | 1 |  |  |  |  | FALSE |
| 6444 | ads\_in\_slot\_\_partners | 1 |  |  |  |  | FALSE |
| 6445 | ads\_in\_slot\_\_advertisement\_\_replaced\_ad\_unit\_id | 1 |  |  |  |  | FALSE |
| 6446 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_inventory\_id | 1 |  |  |  |  | FALSE |
| 6447 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_targeting\_metrics\_\_undefined | 1 |  |  |  |  | FALSE |
| 6448 | ads\_in\_slot\_\_partners\_\_outbound\_rules\_\_win\_opp | 1 |  |  |  |  | FALSE |
| 6449 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filling\_metrics\_\_output\_ad\_number | 1 |  |  |  |  | FALSE |
| 6450 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_order\_transaction\_type | 1 |  |  |  |  | FALSE |
| 6451 | ads\_in\_slot\_\_auction\_\_asset\_id | 1 |  |  |  |  | FALSE |
| 6452 | ack\_\_psn\_msg\_\_content\_provider\_id | 1 |  |  |  |  | FALSE |
| 6453 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_slot\_opp\_avails\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6454 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_avails\_category\_\_vod\_programmer\_total\_avails | 1 |  |  |  |  | FALSE |
| 6455 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_audience\_partner\_id | 1 |  |  |  |  | FALSE |
| 6456 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_reseller\_restriction | 1 |  |  |  |  | FALSE |
| 6457 | ads\_in\_slot\_\_advertisement\_\_campaign\_id | 1 |  |  |  |  | FALSE |
| 6458 | ads\_in\_slot\_\_partners\_\_audience\_partner\_segment\_infos\_\_matched\_segments\_\_cpm | 1 |  |  |  |  | FALSE |
| 6459 | ads\_in\_slot\_\_auction\_\_buyer\_group\_id | 1 |  |  |  |  | FALSE |
| 6460 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_network\_execution\_ctx\_index | 1 |  |  |  |  | FALSE |
| 6461 | ads\_in\_slot\_\_partners\_\_eligible\_outbound\_orders\_\_bit\_flags | 1 |  |  |  |  | FALSE |
| 6462 | ads\_in\_slot\_\_partners\_\_avails\_category\_\_opportunity\_in\_played\_slot | 1 |  |  |  |  | FALSE |
| 6463 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics | 1 |  |  |  |  | FALSE |
| 6464 | ads\_in\_slot\_\_partners\_\_geo\_state\_visibility\_\_targetable | 1 |  |  |  |  | FALSE |
| 6465 | ads\_in\_slot\_\_partners\_\_selected\_yield\_optimization\_ids | 1 |  |  |  |  | FALSE |
| 6466 | ads\_in\_slot\_\_partners\_\_third\_party\_user\_id\_visibility\_\_report\_aggregate | 1 |  |  |  |  | FALSE |
| 6467 | execution\_networks\_\_audience\_partner\_segment\_infos | 1 |  |  |  |  | FALSE |
| 6468 | ack\_\_psn\_msg\_\_session\_start\_time | 1 |  |  |  |  | FALSE |
| 6469 | ads\_in\_slot\_\_candidate\_\_asset\_id | 1 |  |  |  |  | FALSE |
| 6470 | ads\_in\_slot\_\_candidate\_\_domain | 1 |  |  |  |  | FALSE |
| 6471 | ads\_in\_slot\_\_partners\_\_standard\_content\_credential\_status\_visibility | 1 |  |  |  |  | FALSE |
| 6472 | ads\_in\_slot\_\_advertisement\_\_ad\_replica\_id | 1 |  |  |  |  | FALSE |
| 6473 | ads\_in\_slot\_\_partners\_\_network\_is\_vod\_programmer | 1 |  |  |  |  | FALSE |
| 6474 | ads\_in\_slot\_\_advertisement\_\_placement\_type\_priority | 1 |  |  |  |  | FALSE |
| 6475 | ads\_in\_slot\_\_partners\_\_listing\_id | 1 |  |  |  |  | FALSE |
| 6476 | ads\_in\_slot\_\_partners\_\_outbound\_exchange\_listings\_\_listing\_ids | 1 |  |  |  |  | FALSE |
| 6477 | ads\_in\_slot\_\_partners\_\_standard\_content\_credential\_status\_visibility\_\_report\_event | 1 |  |  |  |  | FALSE |
| 6478 | ads\_in\_slot\_\_advertisement\_\_cch\_key | 1 |  |  |  |  | FALSE |
| 6479 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_root\_section\_id | 1 |  |  |  |  | FALSE |
| 6480 | ack\_\_psn\_msg\_\_session\_id | 1 |  |  |  |  | FALSE |
| 6481 | ads\_in\_slot\_\_advertisement\_\_external\_vast\_ad\_id | 1 |  |  |  |  | FALSE |
| 6482 | ads\_in\_slot\_\_partners\_\_programmatic\_exchange\_rate\_to\_eur | 1 |  |  |  |  | FALSE |
| 6483 | ads\_in\_slot\_\_partners\_\_upstream\_content\_owner\_revenue\_in\_up\_currency | 1 |  |  |  |  | FALSE |
| 6484 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_filtering\_metrics\_\_rbp\_check\_failed | 1 |  |  |  |  | FALSE |
| 6485 | ack\_\_psn\_msg\_\_ad\_id | 1 |  |  |  |  | FALSE |
| 6486 | ads\_in\_slot\_\_partners\_\_network\_selection\_info\_\_candidate\_ad\_funnel\_metrics\_\_ad\_creative\_checking\_metrics\_\_auction\_max\_ad\_duration | 1 |  |  |  |  | FALSE |
| 6487 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_down\_network\_id | 1 |  |  |  |  | FALSE |
| 6488 | ads\_in\_slot\_\_candidate\_\_sfx\_buyer\_id | 1 |  |  |  |  | FALSE |
| 6489 | ads\_in\_slot\_\_partners\_\_bidding\_revenue | 1 |  |  |  |  | FALSE |
| 6490 | ads\_in\_slot\_\_advertisement\_\_external\_reseller\_\_root\_asset\_group | 1 |  |  |  |  | FALSE |

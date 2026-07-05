# f\_inventory\_sa\_delivered\_hourly



# Columns Level Diff

  

| Column Name | Diff | Reason |
| --- | --- | --- |
| avails\_event\_count | avails\_event\_count is removed in Hoover++ | Previously, avails\_event\_count was used to calculate the avails\_in\_played\_slot, unfilled\_avails\_in\_played\_slot and unconstrained\_avails\_in\_played\_slot.  In Hoover++, these metrics are pre-calculated using avails\_event\_count and hence this column is not used. |
| geo\_visibility | geo\_visibility is removed | [geo\_visibility DEPRECATED](https://github.freewheel.tv/kbharg432/hoover_plus_sqls/blob/main/L3%20SQL%20Conversions/Event%20Table/f_order_selected_hourly_h%2B%2B.sql#L22) |

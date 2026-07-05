# GE Validation Framework — Hoover → Hoover++ ETL Validation

A Great Expectations (GE / GX) based validation framework for the Hoover → Hoover++ migration, modeled on the reference tool `BVC_Analyzer_Sample/bcv_analyzer.py`. This document is the Task 1 deliverable: Key Concepts, Source→Target Mappings, documented data-break points, and validation strategy — scoped to the `request` table as the first vertical slice. The pattern generalizes to `ad`, `slot`, `candidate`, `auction`, `ack` (see [Extending to other tables](#extending-to-other-tables)).

All claims below are cited to files under `trainingDocs/`. Where a doc is inconsistent with itself or with `bcv_analyzer.py`, that's called out explicitly rather than silently resolved — surfacing exactly that kind of conflict is one of the stated goals of this exercise.

---

## Key Concepts

**Hoover vs. Hoover++.** Hoover is the current 7-table ad-serving log model (`request`, `visitor`, `auction`, `candidate`, `ad`, `slot`, `ack`), with heavy duplication of shared context across tables — the `ack` table alone needs 5,000+ fields just to link callbacks back to entities (`MVP Demo about Hoover++.md`, lines 5–12). Hoover++ merges these into one table, pushes unnesting to consumers, splits `ack` into three sub-entities (Ad/Slot/Request Acks), and moves from batch to streaming ingestion (`MVP Demo`, lines 14–19, 80–84).

**Column selection was usage-driven, not arbitrary.** A field was kept if used by ETL, SOS, or Arena; otherwise it was kept only if meaningfully queried via LQS (excluding headless "sa" accounts); everything else was dropped (`MVP Demo`, line 23). `bcv_analyzer.py`'s ETL/SOS/Insights/Arena/LQS/CP/AF/Others usage-threshold logic formalizes exactly this rule — it isn't an invented heuristic, it's the documented column-retention policy made executable.

**Streaming settling time is load-bearing for validation.** Hoover++ is deliberately "inaccurate" for its first ~2 hours until an IVT backfill job joins in (`MVP Demo`, line 32). Any validation run before that window shows false diffs. This is not hypothetical — the `request` diff doc shows network-level row-count mismatches of thousands of rows resolving to exactly 0 on re-run, attributed to "data had NOT settled" (`mrm_log_flat.default.request vs etl.public_test1.request.md`, lines 627–641). **A validation framework must parametrize its query window by an offset (~3–4 hours back from "now"), never validate the current hour.**

**What a BCV actually is.** A Backward Compatible View is not a copy of Hoover — it's a SQL view over Hoover++'s merged data, reshaped to the old Hoover schema (`etl.public_test1.<table>` mirroring `mrm_log_flat.default.<table>`), so old queries and validators run unmodified against the new pipeline (`Hoover++ Validations Event Level.md`, lines 7–24). `BCV_analyzer` — the named reference framework — is a real internal tool that finds columns missing from a BCV and scores whether the omission is acceptable using this same usage-threshold logic (`ack backwards compatible view.md`, lines 56–58).

**The central data-quality principle: every discrepancy is triaged Y/N, not just detected.** Y = documented, expected, semantically equivalent (exclude from failure). N = real regression (needs a fix). This triage is tracked centrally — `Discrepancy Tracker.md` lists 19 tracked L3-level discrepancies with this exact Y/N column; `Event Level (Backward Compatible Views).md` does the same for event-level ones. **This is the one thing a GE suite cannot get from GE's defaults**: a plain `expect_column_values_to_be_equal`-style check will re-fail on every known-benign difference (protobuf-zero-vs-Avro-null, `[]` vs `null`, timestamp/timezone casting) on every single run, forever, unless the exclusion list is encoded as a first-class part of the suite. `config/request.yaml` in this framework is that encoding.

**Quantitative tolerances are already defined and map cleanly onto GE's vocabulary** (`Hoover - Hoover++ Validation Plan.md`, §3): row counts within 0.01% tolerance; non-double fields require exact match; double fields allow <0.01 absolute / <0.1% relative difference. These map directly to `expect_table_row_count_to_be_between` and numeric-tolerance expectations — this is the one area where GE's native primitives fit without any translation layer.

**Sampling contract.** Rows are marked "sampled" via `bitwise_and(request__bit_flags, 576460752303423488) > 0` (bit 59), fed by a dedicated low-rate Kafka partition (`Hoover++ Validations Event Level.md`, lines 32–38). `bcv_analyzer.py`'s `TABLESAMPLE` batch-1 query already filters on this exact flag — confirming the reference tool deliberately reuses the team's existing sampling contract rather than inventing its own. This framework's reconciliation step does the same.

---

## Source → Target Mapping — `request`

**Correction to a natural first assumption:** `Cross-System Field Mapping- Hoover, Hoover++, UBT, and Reporting Prod(WIP).md` (6,510 lines) looks like it should be the Hoover→Hoover++ crosswalk, but it isn't one yet — its "Field in Hoover++" column is blank across all 6,490 data rows (verified programmatically). It documents Hoover→UBT and (rarely) Hoover→Reporting-Prod mappings only; the file is genuinely "(WIP)" as titled. The real Hoover→Hoover++ mapping for `request` lives in `Request fields analysis on BCV.md` and `mrm_log_flat.default.request vs etl.public_test1.request.md`, expressed as same-column-name diffing plus a documented exception list — not an explicit rename table.

| Category | Detail | Source |
|---|---|---|
| Naming | SRC keeps `__`-flattened struct paths (`request__transaction_id`); BCV keeps the **same names** for columns that exist on both sides — this is same-name diffing, not a rename layer | `mrm_log_flat...vs etl...request.md` |
| Rename (documented, **unresolved**) | `batch_id` → `process_batch_id` — but the validation SQL later in the same source still queries `batch_id`. Flagged as a doc/code inconsistency, not silently reconciled | `Request fields analysis on BCV.md` line 28 vs diff doc line 4183 |
| Dropped (LQS-internal) | `__path__`, `__offset__`, `__file_size__`, `__footer_size__` — matches `bcv_analyzer.py`'s `exclude.csv` exactly | `Request fields analysis on BCV.md`, "Excluded Columns" |
| Dropped (bulk, confirmed intentional) | 311 `inventory__asset_chain__*` and ~302 `inventory__site_section_chain__*` columns absent from the H++ view — dominated by revenue, priority/rule, funnel-metrics, and order/listing sub-fields. Confirmed as a discussed decision (28/05/2026), not an oversight | diff doc lines 2071–3560 |
| Type change (documented, requires normalization) | `request__timestamp`: SRC `timestamp(3)` → BCV `timestamp(3) with time zone`; BCV uses `from_unixtime()` vs Hoover's direct cast | `Request fields analysis on BCV.md` lines 33–35 |
| Type change (likely bug, tracked as issue) | `execution_networks__...__phase_metrics__value`: SRC `array(array(array(bigint)))` → BCV `array(array(array(integer)))` — source protobuf field is `uint32`, so `integer` narrows it; flagged, not silently accepted | same doc, line 36 |
| Value semantics | Unset repeated fields: `[]` (Hoover, a known bug in old raw→Avro conversion) vs `null` (Hoover++, correct). One level deeper: `[[]]` vs `[None]` | same doc, "Major Categories of Diff" #1–2 |
| Value semantics (expected, timing-dependent) | Postbid-IVT-dependent fields (`client_facing_ivt_reason_flag`, `flags`, `mrc_compliance_label`, `traffic_type`) differ only because the validated H++ build lacked postbid IVT processing at validation time | same doc, lines 127–152 |
| Logic change | `Audience` entity is instantiated in H++ only when `audience_item_ids`/`kv_term_ids` is non-null (Hoover always instantiates it) — intentional, avoids empty entities | same doc, line 148 |

**Auto-suppressed "known equivalences"** already baked into the team's existing validation tooling — this framework reuses them verbatim rather than re-deriving them:
- `request__yield_optimization_ids`: `[]` (SRC) ≡ `null` (BCV)
- `request__client_facing_ivt_reason_flag`: `null` (SRC) ≡ `0` (BCV)
- Generic null-equivalence group: `['', '0', '\N', 'false', 'none', 'null']`
- Generic empty-collection-equivalence group: `['', '[]', '\N', 'none', 'null', '{}']`

**Confirmed-matching baseline** (safe to encode as passing schema expectations today): `request__context__rbp_device_type`, `rbp_platform`, `inventory__asset_chain__role`/`network_id`, `inventory__site_section_chain__role`/`network_id`, `visitor__dma_code_id`, `visitor__country`, `request_info__slot_ad_unit_ids`, `execution_networks__role`.

---

## Potential Data Break Points

1. **Validating too early.** Querying before the ~3–4 hour settling window produces false row-count and field mismatches that aren't bugs — the single most likely way to generate noise. Every checkpoint run in this framework parametrizes its time window; never validates "now."
2. **Silent null-semantics false positives.** Without the equivalence-group normalization, a raw string/value comparison (as in `bcv_analyzer.py`'s current `compare_value_validation_results`) will flag `[]` vs `null`, `0` vs `null`, etc. as mismatches on every run. This framework normalizes known-equivalent values *before* comparing, so only genuinely new divergences surface.
3. **Undocumented reappearance of dropped columns.** If a future BCV view change re-adds one of the bulk-dropped `inventory__asset_chain__*`/`inventory__site_section_chain__*` columns, that's a schema change nobody decided on — worth a positive `expect_column_to_not_exist`-style check on the intentionally-dropped set, not just checks on what should exist.
4. **The `batch_id`/`process_batch_id` rename inconsistency.** Until resolved, any hand-written SQL against the BCV view risks silently querying the wrong (possibly empty or stale) column. Tracked as an explicit open issue in `config/request.yaml`, not treated as either "matched" or "excluded."
5. **The `phase_metrics__value` type narrowing (`bigint`→`integer`).** If the source protobuf field genuinely is `uint32`-range, this may be silently truncating values above `2^31-1` rather than being a harmless type relabel. Tracked as an open issue, not auto-passed.

## Validation Strategy

Two layers, matching the team's existing two-layer approach (`Hoover - Hoover++ Validation Plan.md`):

1. **Schema-level** — does the BCV table have the columns this mapping says it should, with the types this mapping says it should? Implemented as a GE Expectation Suite generated directly from `config/<table>.yaml`'s confirmed-matching and known-type-diff lists (see [`ge_validator/schema_suite.py`](ge_validator/schema_suite.py)).
2. **Row-level reconciliation** — sample rows via the same `TABLESAMPLE` + sampled-bit-flag contract `bcv_analyzer.py` already uses (reused, not reimplemented — see [`ge_validator/reconciliation.py`](ge_validator/reconciliation.py)), normalize known-equivalent values, then assert column-pair equality per matched column via GE. Known-issue columns are still checked and reported, but tagged separately from unexpected new failures — preserving the team's Y/N triage discipline instead of collapsing everything into a single pass/fail.

## Running it

The orchestration is table-agnostic and lives in `ge_validator/runner.py`. Point the generic CLI at any table that has a `config/<table>.yaml`:

```bash
python run_validation.py --table request --host <presto-host> --user <you> --auth-token <token>
python run_validation.py --table slot    --host <presto-host> --user <you> --auth-token <token>
```

`run_request_validation.py` is kept as a thin back-compat wrapper for the original vertical slice; new tables should use `run_validation.py --table <name>`. Both share the same runner, so there is no duplicated flow. A live run needs a Presto/Trino gateway + VPN (the same constraint `bcv_analyzer.py` has); without one, the logic is exercised by the test suite against local sqlite/pandas fixtures.

## Tables covered

| Table | Config | Join keys | Notable |
|---|---|---|---|
| `request` | `config/request.yaml` | `request__transaction_id` | 613-column bulk struct drops; timestamp timezone type diff; `batch_id`→`process_batch_id` open issue |
| `slot` | `config/slot.yaml` | `request__transaction_id`, `slot__index` *(int)* | 8 benign `avails` int→bigint widenings; the same `phase_metrics__value` narrowing bug; a real UTC-vs-local-time value bug on `request__timestamp`; dropped `visitor__identity_user_ids__*`; a `request__hashed_key_value` mismatch still under investigation |

`slot` is the sharpest illustration of why the Y/N triage matters: of its 92 unmatched fields (16.55% per `Slot fields analysis on BCV.md`), the large majority are the same benign `[]`-vs-`null` / `[None]`-vs-`null` semantics the equivalence groups absorb, while only four are genuine open bugs — the framework keeps those four visible instead of letting them drown in the noise.

## Extending to further tables

The same `[]`-vs-`null` / protobuf-default-vs-Avro-null root cause recurs across every table (confirmed in `ack`, `candidate`, `auction` — see inventory pass), so extending this framework means adding a new `config/<table>.yaml` with that table's confirmed-matching columns, known type diffs, and equivalence exceptions, then running `python run_validation.py --table <name>`. The code in `ge_validator/` is already table-agnostic — no code change is needed to onboard a new table, only a config and a citation trail.

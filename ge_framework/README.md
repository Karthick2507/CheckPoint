# GE Validation Framework

A config-driven **data-quality framework built on [Great Expectations](https://greatexpectations.io/) (1.x Fluent API)** that runs validations against a **Presto/Trino** gateway. It is the `GE_Validation` component declared in the project `requirements.txt`, and it reuses the same Bearer-token connection style as `bcv_analyzer.py` so both tools authenticate identically.

---

## Why this exists

The BCV Analyzer answers *"do the SRC and BCV schemas/values match?"* for a one-off migration. This framework answers the day-to-day ETL question: *"does the data in this table still meet our quality rules?"* — as a repeatable, config-driven, CI-friendly check.

```
datasource.yml ─┐
                ├─► GEValidationFramework ─► GE Checkpoint ─► ValidationOutcome ─► console + JSON/MD reports
suite.yml ──────┘        (Presto/Trino via Trino SQLAlchemy + Bearer token)
```

## Design

| Module | Responsibility |
|--------|----------------|
| `config.py` | Dataclasses + YAML loaders for the datasource and suite configs. `${ENV_VAR}` interpolation; `PRESTO_*` env fallbacks. |
| `presto.py` | Trino SQLAlchemy URL + `connect_args` (Bearer / custom-header auth), mirroring `bcv_analyzer`. |
| `expectations.py` | Maps snake_case expectation names → GE expectation classes. |
| `framework.py` | Wires datasource → asset → batch → suite → validation definition → run, and normalizes the result into a serializable `ValidationOutcome`. |
| `reporting.py` | Rich console summary + JSON / Markdown report writers. |
| `cli.py` | `typer` CLI (`validate`, `list-expectations`). |

The SQL plumbing is database-agnostic — the test-suite drives the entire flow against a temporary **sqlite** database, so the framework is fully exercised without a live Presto gateway.

## Install

```bash
pip install -r requirements.txt
```

## Configure

**Datasource** (`config/datasource.example.yml`) — how to reach Presto:

```yaml
datasource:
  name: presto_mrm
  host: presto-gateway.presto.fw1.aws.fwmrm.net
  port: 8080
  user: ${PRESTO_USER}
  catalog: mrm_log_flat
  schema: default
  http_scheme: https
  request_timeout: 30
  auth_token: ${PRESTO_AUTH_TOKEN}   # sent as "Authorization: Bearer <token>"
  auth_header: Authorization
```

Any `${VAR}` is interpolated from the environment at load time; `host`, `user`, `port`, `auth_token`, and `auth_header` also fall back to the `PRESTO_*` variables `bcv_analyzer` documents.

**Suite** (`config/suites/request.example.yml`) — what to validate:

```yaml
suite:
  name: request_quality
  asset:
    type: table            # "table" (table_name [+ schema_name]) or "query" (raw SQL)
    name: request
    table_name: request
    schema_name: default
    batch: whole_table
expectations:
  - type: expect_column_values_to_not_be_null
    column: request__transaction_id
  - type: expect_column_values_to_be_unique
    column: request__transaction_id
  - type: expect_table_row_count_to_be_between
    min_value: 1
```

Each expectation uses the **snake_case** name (see `list-expectations`) plus that expectation's own keyword arguments.

## Run

```bash
export PRESTO_AUTH_TOKEN=<your-token>          # VPN required for the prod gateway

# Validate one or more suites (‑‑suite is repeatable):
python -m ge_framework.cli validate \
  --datasource config/datasource.example.yml \
  --suite config/suites/request.example.yml

# Discover available expectation types:
python -m ge_framework.cli list-expectations not_be_null
```

CLI overrides: `--host`, `--user`, `--auth-token`, `--output-dir`, `--no-reports`. The command exits non-zero if any suite fails, so it drops straight into CI.

### Programmatic use

```python
from ge_framework import GEValidationFramework, load_datasource_config, load_suite_config

framework = GEValidationFramework(load_datasource_config("config/datasource.example.yml"))
outcome = framework.run(load_suite_config("config/suites/request.example.yml"))

print(outcome.success, outcome.successful, "/", outcome.evaluated)
for row in outcome.results:
    print(row.success, row.expectation_type, row.column)
```

## Output

* **Console** — a color-coded summary panel + per-expectation table.
* **`ge_output/<suite>_validation.json`** — the full normalized `ValidationOutcome` (JSON-safe).
* **`ge_output/<suite>_validation.md`** — a Markdown report with a failed-expectations section.

## Tests

```bash
python -m pytest tests/test_ge_framework.py -q
```

Covers the connection layer, config loading + env interpolation, the expectation factory, end-to-end pass/fail runs (table and query assets) against sqlite, JSON-serializability, and report writing.

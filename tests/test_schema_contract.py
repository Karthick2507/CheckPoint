"""Schema contract tests (P4).

Two defects:

* ``SELECT *`` projected everything, so an upstream column change flowed
  straight into the target with nothing noticing.
* The loader took its column list from ``rows[0].keys()``, so a later row
  carrying a different key silently lost that value — no error, no warning.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.pipeline import Pipeline
from core.pipeline_config import PipelineConfig
from core.schema import ColumnSpec, SchemaContract, SchemaContractError
from data_sources.base import DataSource
from runtime.run_context import RunContext
from runtime.state import FileState


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"

    def describe_sql(self, table: str) -> str:
        return f"PRAGMA table_info({table})"


# --------------------------------------------------------------------------
# Parsing the config surface
# --------------------------------------------------------------------------


def test_list_of_names():
    contract = SchemaContract.from_config(["id", "name"])
    assert contract.output_names == ["id", "name"]
    assert contract.projection() == '"id", "name"'


def test_mapping_renames():
    contract = SchemaContract.from_config({"request__transaction_id": "transaction_id"})
    assert contract.output_names == ["transaction_id"]
    assert contract.projection() == '"request__transaction_id" AS "transaction_id"'


def test_explicit_entries():
    contract = SchemaContract.from_config(
        [{"source": "a", "as": "x"}, {"source": "b"}]
    )
    assert contract.output_names == ["x", "b"]


def test_expression_columns_are_not_quoted():
    """A cast or function call must survive as SQL, not become an identifier."""
    contract = SchemaContract.from_config({"CAST(a AS VARCHAR)": "a_str"})
    assert contract.projection() == 'CAST(a AS VARCHAR) AS "a_str"'


def test_dialect_quote_is_respected():
    assert SchemaContract.from_config(["order"]).projection("`") == "`order`"


def test_no_contract_means_star():
    contract = SchemaContract.from_config(None)
    assert contract.declared is False
    assert contract.projection() == "*"


def test_duplicate_output_names_rejected():
    with pytest.raises(ValueError, match="Duplicate output column"):
        SchemaContract.from_config({"a": "x", "b": "x"})


def test_entry_without_source_rejected():
    with pytest.raises(ValueError, match="requires a 'source'"):
        SchemaContract.from_config([{"as": "x"}])


def test_unsupported_config_rejected():
    with pytest.raises(ValueError, match="Unsupported 'columns'"):
        SchemaContract.from_config(42)


def test_alias_equal_to_source_omits_the_as():
    assert ColumnSpec(source="a", alias="a").select_expression() == '"a"'


# --------------------------------------------------------------------------
# Conforming a payload
# --------------------------------------------------------------------------


def test_conform_projects_onto_the_contract():
    contract = SchemaContract.from_config(["id", "v"])
    rows = [{"id": 1, "v": "a", "unwanted": "x"}]
    assert contract.conform(rows) == [{"id": 1, "v": "a"}], "extras dropped deliberately"


def test_strict_conform_rejects_a_missing_column():
    contract = SchemaContract.from_config(["id", "v"])
    with pytest.raises(SchemaContractError, match="missing declared column"):
        contract.conform([{"id": 1}])


def test_lenient_conform_fills_null():
    contract = SchemaContract.from_config(["id", "v"], strict=False)
    assert contract.conform([{"id": 1}]) == [{"id": 1, "v": None}]


def test_conform_without_contract_is_a_passthrough():
    rows = [{"a": 1}, {"b": 2}]
    assert SchemaContract.from_config(None).conform(rows) == rows


# --------------------------------------------------------------------------
# Uniformity check (no contract declared)
# --------------------------------------------------------------------------


def test_uniform_rows_pass():
    SchemaContract().check_uniform([{"a": 1, "b": 2}, {"a": 3, "b": 4}])


def test_ragged_rows_are_rejected():
    """This is the silent data loss: row 1's 'extra' was dropped without a word."""
    with pytest.raises(SchemaContractError, match="different shape"):
        SchemaContract().check_uniform([{"id": 1, "v": "a"}, {"id": 2, "v": "b", "extra": "LOST"}])


def test_ragged_error_names_the_difference():
    with pytest.raises(SchemaContractError) as excinfo:
        SchemaContract().check_uniform([{"a": 1}, {"b": 2}])
    message = str(excinfo.value)
    assert "unexpected: b" in message
    assert "missing: a" in message


def test_empty_payload_is_uniform():
    SchemaContract().check_uniform([])


# --------------------------------------------------------------------------
# End to end
# --------------------------------------------------------------------------


@pytest.fixture()
def warehouse(tmp_path):
    db = tmp_path / "w.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE src (id INTEGER, name TEXT, secret TEXT, pb TEXT)")
    con.execute("CREATE TABLE dst (key INTEGER, label TEXT)")
    con.executemany(
        "INSERT INTO src VALUES (?, ?, ?, ?)",
        [(1, "a", "hide me", "B1"), (2, "b", "hide me", "B1")],
    )
    con.commit()
    con.close()
    return _SqliteSource({"name": "wh", "path": str(db)})


def _pipeline(tmp_path, warehouse, pipeline_dict):
    cfg = PipelineConfig.from_dict(pipeline_dict)
    ctx = RunContext(pipeline=cfg.name, batch_id="B1", output_root=tmp_path / "out", state_root=tmp_path / "st")
    return Pipeline(cfg, resolve_source=lambda n: warehouse, state=FileState(tmp_path / "s"), context=ctx)


def test_contract_projects_and_renames_end_to_end(tmp_path, warehouse):
    result = _pipeline(
        tmp_path,
        warehouse,
        {
            "pipeline": {
                "name": "p",
                "execution": "pushdown",
                "source": {
                    "connection": "wh",
                    "table": "src",
                    "columns": {"id": "key", "name": "label"},
                },
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
    ).run()

    assert result.errors == []
    rows = warehouse.execute("SELECT key, label FROM dst ORDER BY key")
    assert rows == [{"key": 1, "label": "a"}, {"key": 2, "label": "b"}]
    # `secret` was never selected — the contract is a projection, not a filter
    # applied after the fact.


def test_pipeline_without_contract_still_uses_star(tmp_path, warehouse):
    pipeline = _pipeline(
        tmp_path,
        warehouse,
        {"pipeline": {"name": "p", "source": {"connection": "wh", "table": "src"}}},
    )
    assert pipeline.contract.declared is False
    assert "SELECT * FROM src" in pipeline._source_sql(pipeline.config, {})


def test_pipeline_projection_appears_in_sql(tmp_path, warehouse):
    pipeline = _pipeline(
        tmp_path,
        warehouse,
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "wh", "table": "src", "columns": ["id", "name"]},
            }
        },
    )
    sql = pipeline._source_sql(pipeline.config, {})
    assert '"id", "name"' in sql
    assert "SELECT *" not in sql


def test_ragged_payload_fails_the_run_instead_of_losing_data(tmp_path, warehouse):
    """The original bug, now surfaced as a recorded StageError."""
    pipeline = _pipeline(
        tmp_path,
        warehouse,
        {
            "pipeline": {
                "name": "p",
                "execution": "rows",
                "source": {"connection": "wh", "table": "src"},
                "target": {"connection": "wh", "table": "dst", "mode": "append"},
            }
        },
    )
    # a transform whose rows disagree in shape
    pipeline.transformer.apply = lambda source, steps: type(
        "T", (), {"applied": True, "rows": [{"key": 1}, {"key": 2, "label": "LOST"}], "row_count": 2, "sql": ""}
    )()
    pipeline.config.transform = ["SELECT 1"]
    result = pipeline.run()

    assert any(e.stage == "load" for e in result.errors), "must be reported, not silently dropped"
    assert result.passed is False


def test_contract_conforms_a_ragged_payload(tmp_path, warehouse):
    """With a contract and strict off, shape is pinned rather than guessed."""
    contract = SchemaContract.from_config(["key", "label"], strict=False)
    conformed = contract.conform([{"key": 1}, {"key": 2, "label": "kept", "extra": "dropped"}])
    assert conformed == [{"key": 1, "label": None}, {"key": 2, "label": "kept"}]


def test_config_parses_columns_and_strict_flag():
    cfg = PipelineConfig.from_dict(
        {
            "pipeline": {
                "name": "p",
                "source": {"connection": "s", "table": "t", "columns": ["a"], "strict_columns": False},
            }
        }
    )
    assert cfg.source.columns == ["a"]
    assert cfg.source.strict_columns is False

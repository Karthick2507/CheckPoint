"""Identifier quoting tests (P3).

``Capabilities.identifier_quote`` existed from the start but nothing used it, so
a column named ``order`` or ``select`` produced a syntax error mid-load. The
loader now quotes identifiers with the dialect's own quote character.
"""

from __future__ import annotations

import sqlite3

import pytest

from core.load import Loader
from data_sources.base import Capabilities, DataSource
from runtime.sql import identifier_quote_for, quote_identifier, quote_identifiers


class _SqliteSource(DataSource):
    type = "sqlite_test"

    def connection_string(self) -> str:
        return f"sqlite:///{self.config['path']}"


class _BacktickSource(_SqliteSource):
    """A dialect that quotes with backticks (MySQL-style)."""

    type = "backtick"

    def capabilities(self) -> Capabilities:
        return Capabilities(dialect="backtick", identifier_quote="`")


# --------------------------------------------------------------------------
# The primitive
# --------------------------------------------------------------------------


def test_quotes_a_plain_identifier():
    assert quote_identifier("order") == '"order"'


def test_quotes_each_part_of_a_dotted_name():
    """A qualified table must stay qualified, not become one identifier."""
    assert quote_identifier("catalog.schema.table") == '"catalog"."schema"."table"'


def test_respects_the_dialect_quote():
    assert quote_identifier("order", "`") == "`order`"


def test_leaves_already_quoted_names_alone():
    assert quote_identifier('"order"') == '"order"'
    assert quote_identifier("`order`", "`") == "`order`"


def test_empty_name_is_passed_through():
    assert quote_identifier("") == ""


def test_quote_identifiers_maps_a_list():
    assert quote_identifiers(["a", "order"]) == ['"a"', '"order"']


def test_identifier_quote_for_reads_capabilities(tmp_path):
    default = _SqliteSource({"name": "s", "path": str(tmp_path / "a.db")})
    backtick = _BacktickSource({"name": "b", "path": str(tmp_path / "b.db")})
    assert identifier_quote_for(default) == '"'
    assert identifier_quote_for(backtick) == "`"


def test_presto_declares_double_quote():
    from data_sources.presto import PrestoDataSource

    caps = PrestoDataSource({"host": "h", "catalog": "c", "schema": "s"}).capabilities()
    assert caps.identifier_quote == '"'


# --------------------------------------------------------------------------
# The failure it prevents
# --------------------------------------------------------------------------


@pytest.fixture()
def reserved_word_table(tmp_path):
    db = tmp_path / "r.db"
    con = sqlite3.connect(db)
    con.execute('CREATE TABLE dst ("order" INTEGER, "select" TEXT, "group" TEXT)')
    con.commit()
    con.close()
    return _SqliteSource({"name": "t", "path": str(db)})


def test_append_with_reserved_word_columns(reserved_word_table):
    """Previously: OperationalError: near "order": syntax error."""
    result = Loader().load(
        reserved_word_table,
        "dst",
        [{"order": 1, "select": "a", "group": "g1"}],
        mode="append",
    )
    assert result.inserted == 1
    rows = reserved_word_table.execute('SELECT "order", "select" FROM dst')
    assert rows == [{"order": 1, "select": "a"}]


def test_merge_with_reserved_word_key(reserved_word_table):
    loader = Loader()
    loader.load(reserved_word_table, "dst", [{"order": 1, "select": "old", "group": "g"}], mode="append")
    loader.load(
        reserved_word_table,
        "dst",
        [{"order": 1, "select": "new", "group": "g"}],
        mode="merge",
        keys=["order"],
    )
    rows = reserved_word_table.execute('SELECT "order", "select" FROM dst')
    assert rows == [{"order": 1, "select": "new"}]


def test_overwrite_with_reserved_word_columns(reserved_word_table):
    loader = Loader()
    loader.load(reserved_word_table, "dst", [{"order": 1, "select": "a", "group": "g"}], mode="append")
    loader.load(reserved_word_table, "dst", [{"order": 9, "select": "z", "group": "g"}], mode="overwrite")
    rows = reserved_word_table.execute('SELECT "order" FROM dst')
    assert rows == [{"order": 9}]


def test_streaming_load_quotes_too(reserved_word_table):
    result = Loader().load_stream(
        reserved_word_table, "dst", [[{"order": 5, "select": "s", "group": "g"}]]
    )
    assert result.inserted == 1


def test_ordinary_columns_still_work(tmp_path):
    """Quoting must not break the normal case."""
    db = tmp_path / "n.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER, v TEXT)")
    con.commit()
    con.close()
    source = _SqliteSource({"name": "t", "path": str(db)})
    assert Loader().load(source, "dst", [{"id": 1, "v": "a"}], mode="append").inserted == 1
    assert source.execute("SELECT COUNT(*) AS n FROM dst")[0]["n"] == 1


def test_qualified_table_name_still_works(tmp_path):
    """A dotted target must not be mangled into a single identifier."""
    db = tmp_path / "q.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE dst (id INTEGER)")
    con.commit()
    con.close()
    source = _SqliteSource({"name": "t", "path": str(db)})
    # sqlite exposes the connected database as "main"
    assert Loader().load(source, "main.dst", [{"id": 1}], mode="append").inserted == 1

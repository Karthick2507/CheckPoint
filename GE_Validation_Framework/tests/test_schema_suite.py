import os
import sqlite3
import tempfile
import unittest

import great_expectations as gx

from ge_validator import datasource, schema_suite
from ge_validator.config import ColumnSpec, TableValidationConfig, ValueEquivalences


def _make_config(bcv_table: str) -> TableValidationConfig:
    return TableValidationConfig(
        table="request",
        src_table="mrm_log_flat.default.request",
        bcv_table=bcv_table,
        key_columns=["request__transaction_id"],
        sampled_bit_flag=576460752303423488,
        confirmed_matching_columns=[
            ColumnSpec(name="request__transaction_id"),
            ColumnSpec(name="request__context__rbp_device_type"),
        ],
        excluded_columns=[],
        known_dropped_prefixes=[],
        known_type_diffs=[],
        known_value_equivalences=ValueEquivalences(),
        known_issues=[],
        ivt_dependent_columns=[],
    )


class SchemaSuiteAgainstSqliteTests(unittest.TestCase):
    """Smoke-tests the GE suite-building/running path against a real (sqlite) SQL
    datasource, since there's no live Trino cluster available in this environment.
    Catches API-signature or expectation-field-name regressions structurally.
    """

    def setUp(self):
        fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "CREATE TABLE request_test (request__transaction_id TEXT, request__context__rbp_device_type TEXT)"
        )
        conn.execute("INSERT INTO request_test VALUES ('t1', 'mobile')")
        conn.commit()
        conn.close()

        self.context = datasource.get_context()
        self.sql_datasource = self.context.data_sources.add_or_update_sqlite(
            name="request_bcv", connection_string=f"sqlite:///{self.db_path}"
        )

    def tearDown(self):
        os.remove(self.db_path)

    def test_schema_suite_passes_when_columns_present(self):
        config = _make_config(bcv_table="test.request_test")
        suite = schema_suite.build_schema_suite(self.context, config)
        validation = schema_suite.run_schema_suite(self.context, self.sql_datasource, config, suite)
        result = validation.run()
        self.assertTrue(result.success)

    def test_schema_suite_fails_when_column_missing(self):
        config = _make_config(bcv_table="test.request_test")
        config.confirmed_matching_columns.append(ColumnSpec(name="does_not_exist_column"))
        suite = schema_suite.build_schema_suite(self.context, config)
        validation = schema_suite.run_schema_suite(self.context, self.sql_datasource, config, suite)
        result = validation.run()
        self.assertFalse(result.success)


if __name__ == "__main__":
    unittest.main()

import unittest

from ge_validator import datasource, schema_suite
from ge_validator.config import ColumnSpec, TableValidationConfig, TypeDiff, ValueEquivalences


def _make_config(known_type_diffs=None) -> TableValidationConfig:
    return TableValidationConfig(
        table="request",
        src_table="mrm_log_flat.default.request",
        bcv_table="etl.public_test1.request",
        key_columns=["request__transaction_id"],
        sampled_bit_flag=576460752303423488,
        confirmed_matching_columns=[
            ColumnSpec(name="request__transaction_id"),
            ColumnSpec(name="request__context__rbp_device_type"),
        ],
        excluded_columns=[],
        known_dropped_prefixes=[],
        known_type_diffs=known_type_diffs or [],
        known_value_equivalences=ValueEquivalences(),
        known_issues=[],
        ivt_dependent_columns=[],
    )


class SchemaExistenceTests(unittest.TestCase):
    """Runs the existence suite against a pandas batch built from a (faked) BCV DESCRIBE,
    so it exercises the real GE path with no Trino gateway."""

    def test_passes_when_all_expected_columns_present(self):
        config = _make_config()
        bcv_schema = {
            "request__transaction_id": "varchar",
            "request__context__rbp_device_type": "varchar",
            "some_other_col": "bigint",
        }
        context = datasource.get_context()
        suite = schema_suite.build_schema_suite(context, config)
        validation, df = schema_suite.run_schema_suite(context, config, suite, bcv_schema)
        result = validation.run(batch_parameters={"dataframe": df})
        self.assertTrue(result.success)

    def test_fails_when_expected_column_missing_from_bcv(self):
        config = _make_config()
        bcv_schema = {"request__transaction_id": "varchar"}  # rbp_device_type absent
        context = datasource.get_context()
        suite = schema_suite.build_schema_suite(context, config)
        validation, df = schema_suite.run_schema_suite(context, config, suite, bcv_schema)
        result = validation.run(batch_parameters={"dataframe": df})
        self.assertFalse(result.success)


class TypeDiffVerificationTests(unittest.TestCase):
    def setUp(self):
        self.diff_expected = TypeDiff(
            column="partners__avails_category__avails",
            src_type="array(integer)", bcv_type="array(bigint)",
            expected=True, note="", source="",
        )
        self.diff_issue = TypeDiff(
            column="partners__phase_metrics__value",
            src_type="array(array(array(bigint)))", bcv_type="array(array(array(integer)))",
            expected=False, note="", source="",
        )
        self.config = _make_config(known_type_diffs=[self.diff_expected, self.diff_issue])

    def test_matching_live_type_is_ok(self):
        bcv_schema = {
            "partners__avails_category__avails": "array(bigint)",
            "partners__phase_metrics__value": "array(array(array(integer)))",
        }
        results = schema_suite.verify_type_diffs(bcv_schema, self.config)
        self.assertTrue(all(r["matches"] for r in results))

    def test_type_normalization_ignores_whitespace_and_case(self):
        bcv_schema = {
            "partners__avails_category__avails": "ARRAY( BIGINT )",
            "partners__phase_metrics__value": "array(array(array(integer)))",
        }
        results = schema_suite.verify_type_diffs(bcv_schema, self.config)
        avails = next(r for r in results if r["column"] == "partners__avails_category__avails")
        self.assertTrue(avails["matches"])

    def test_drift_is_flagged_and_known_issue_tagged(self):
        # the phase_metrics field drifted back to bigint (no longer the documented integer)
        bcv_schema = {
            "partners__avails_category__avails": "array(bigint)",
            "partners__phase_metrics__value": "array(array(array(bigint)))",
        }
        results = schema_suite.verify_type_diffs(bcv_schema, self.config)
        phase = next(r for r in results if r["column"].endswith("phase_metrics__value"))
        self.assertFalse(phase["matches"])
        self.assertTrue(phase["is_known_issue"])

    def test_missing_column_reported(self):
        bcv_schema = {"partners__avails_category__avails": "array(bigint)"}  # phase_metrics absent
        results = schema_suite.verify_type_diffs(bcv_schema, self.config)
        phase = next(r for r in results if r["column"].endswith("phase_metrics__value"))
        self.assertFalse(phase["matches"])
        self.assertEqual(phase["actual_bcv_type"], "(column missing)")


class FetchBcvSchemaTests(unittest.TestCase):
    def test_fetch_parses_describe_rows(self):
        config = _make_config()
        fake_describe_rows = [
            {"Column": "request__transaction_id", "Type": "varchar"},
            {"Column": "slot__index", "Type": "integer"},
        ]
        original = schema_suite.bcv_analyzer.execute_sql
        schema_suite.bcv_analyzer.execute_sql = lambda sql, connection_kwargs: fake_describe_rows
        try:
            schema = schema_suite.fetch_bcv_schema(config, {"host": "x", "user": "y"})
        finally:
            schema_suite.bcv_analyzer.execute_sql = original
        self.assertEqual(schema, {"request__transaction_id": "varchar", "slot__index": "integer"})


if __name__ == "__main__":
    unittest.main()

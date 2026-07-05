import unittest

import pandas as pd

from ge_validator.config import ColumnSpec, TableValidationConfig, ValueEquivalences
from ge_validator.reconciliation import (
    build_reconciliation_dataframe,
    build_reconciliation_suite,
    run_reconciliation_suite,
)
from ge_validator.datasource import get_context


def _make_config() -> TableValidationConfig:
    return TableValidationConfig(
        table="request",
        src_table="mrm_log_flat.default.request",
        bcv_table="etl.public_test1.request",
        key_columns=["request__transaction_id"],
        sampled_bit_flag=576460752303423488,
        confirmed_matching_columns=[ColumnSpec(name="request__transaction_id")],
        excluded_columns=[],
        known_dropped_prefixes=[],
        known_type_diffs=[],
        known_value_equivalences=ValueEquivalences(
            column_specific={"request__yield_optimization_ids": ["[]", None]},
            generic_groups=[["", "0", "false", "none", "null"]],
        ),
        known_issues=[],
        ivt_dependent_columns=[],
    )


class BuildReconciliationDataframeTests(unittest.TestCase):
    def setUp(self):
        self.config = _make_config()

    def test_matches_rows_by_key_and_normalizes_known_equivalences(self):
        src_rows = [
            {"request__transaction_id": "t1", "request__yield_optimization_ids": "[]"},
            {"request__transaction_id": "t2", "request__yield_optimization_ids": "abc"},
        ]
        bcv_rows = [
            {"request__transaction_id": "t1", "request__yield_optimization_ids": None},
            {"request__transaction_id": "t2", "request__yield_optimization_ids": "different"},
        ]
        df = build_reconciliation_dataframe(
            self.config, src_rows, bcv_rows, ["request__yield_optimization_ids"],
        )
        row_t1 = df[df["_key"] == "t1"].iloc[0]
        row_t2 = df[df["_key"] == "t2"].iloc[0]
        self.assertEqual(
            row_t1["src__request__yield_optimization_ids"], row_t1["bcv__request__yield_optimization_ids"]
        )
        self.assertNotEqual(
            row_t2["src__request__yield_optimization_ids"], row_t2["bcv__request__yield_optimization_ids"]
        )

    def test_unmatched_keys_are_dropped_not_silently_padded(self):
        src_rows = [{"request__transaction_id": "only_in_src", "col": "x"}]
        bcv_rows = [{"request__transaction_id": "only_in_bcv", "col": "y"}]
        df = build_reconciliation_dataframe(self.config, src_rows, bcv_rows, ["col"])
        self.assertEqual(len(df), 0)


class ReconciliationSuiteSmokeTests(unittest.TestCase):
    """Smoke-tests the GE pandas-batch path end to end against an in-memory dataframe."""

    def test_pair_equality_suite_flags_mismatches(self):
        config = _make_config()
        context = get_context()
        df = pd.DataFrame(
            {
                "_key": ["t1", "t2"],
                "src__request__yield_optimization_ids": ["null", "abc"],
                "bcv__request__yield_optimization_ids": ["null", "different"],
            }
        )
        suite = build_reconciliation_suite(context, config, ["request__yield_optimization_ids"])
        validation = run_reconciliation_suite(context, config, suite, df)
        result = validation.run(batch_parameters={"dataframe": df})
        self.assertFalse(result.success)
        self.assertEqual(result.results[0].result["unexpected_count"], 1)


if __name__ == "__main__":
    unittest.main()

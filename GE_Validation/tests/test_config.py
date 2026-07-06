import unittest
from pathlib import Path

from ge_validator.config import load_table_config

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "request.yaml"


class LoadTableConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = load_table_config(CONFIG_PATH)

    def test_top_level_fields(self):
        self.assertEqual(self.config.table, "request")
        self.assertEqual(self.config.src_table, "mrm_log_flat.default.request")
        self.assertEqual(self.config.bcv_table, "etl.public_test1.request")
        self.assertEqual(self.config.key_columns, ["request__transaction_id"])
        self.assertEqual(self.config.sampled_bit_flag, 576460752303423488)

    def test_confirmed_matching_columns_loaded(self):
        names = {c.name for c in self.config.confirmed_matching_columns}
        self.assertIn("request__transaction_id", names)
        self.assertIn("execution_networks__role", names)

    def test_excluded_columns_loaded(self):
        self.assertIn("__path__", self.config.excluded_columns)

    def test_is_dropped_column(self):
        self.assertTrue(self.config.is_dropped_column("inventory__asset_chain__revenue"))
        self.assertTrue(self.config.is_dropped_column("inventory__site_section_chain__role"))
        self.assertFalse(self.config.is_dropped_column("request__transaction_id"))

    def test_known_issue_columns_only_includes_unexpected_type_diffs(self):
        issue_columns = self.config.known_issue_columns
        self.assertIn(
            "execution_networks__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__value",
            issue_columns,
        )
        # request__timestamp's type diff is documented as expected=True, so it's not a known issue.
        self.assertNotIn("request__timestamp", issue_columns)


class ValueEquivalencesTests(unittest.TestCase):
    def setUp(self):
        self.config = load_table_config(CONFIG_PATH)
        self.equivalences = self.config.known_value_equivalences

    def test_column_specific_equivalence(self):
        normalized_empty_list = self.equivalences.normalize("request__yield_optimization_ids", "[]")
        normalized_null = self.equivalences.normalize("request__yield_optimization_ids", None)
        self.assertEqual(normalized_empty_list, normalized_null)

    def test_generic_null_equivalence_group(self):
        a = self.equivalences.normalize("some_other_column", "0")
        b = self.equivalences.normalize("some_other_column", "false")
        c = self.equivalences.normalize("some_other_column", None)
        self.assertEqual(a, b)
        self.assertEqual(b, c)

    def test_values_outside_any_group_are_distinct(self):
        a = self.equivalences.normalize("request__transaction_id", "abc123")
        b = self.equivalences.normalize("request__transaction_id", "xyz789")
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()

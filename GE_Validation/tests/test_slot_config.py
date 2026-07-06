import unittest
from pathlib import Path

from ge_validator.config import load_table_config
from ge_validator.runner import config_path_for_table

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "slot.yaml"


class LoadSlotConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = load_table_config(CONFIG_PATH)

    def test_top_level_fields(self):
        self.assertEqual(self.config.table, "slot")
        self.assertEqual(self.config.src_table, "mrm_log_flat.default.slot")
        self.assertEqual(self.config.bcv_table, "etl.public_test1.slot")

    def test_composite_key_includes_slot_index(self):
        # slot is keyed by BOTH transaction and slot position -- the int key
        # (slot__index) is what makes slot different from request.
        self.assertEqual(self.config.key_columns, ["request__transaction_id", "slot__index"])

    def test_avails_widening_diffs_are_expected(self):
        widening = [
            d for d in self.config.known_type_diffs
            if d.src_type == "array(integer)" and d.bcv_type == "array(bigint)"
        ]
        self.assertEqual(len(widening), 8)  # eight avails_category fields
        self.assertTrue(all(d.expected for d in widening))
        # ...so none of them count as a blocking known issue.
        for d in widening:
            self.assertNotIn(d.column, self.config.known_issue_columns)

    def test_phase_metrics_narrowing_is_a_known_issue(self):
        self.assertIn(
            "partners__network_selection_info__candidate_ad_funnel_metrics__phase_metrics__value",
            self.config.known_issue_columns,
        )

    def test_real_bugs_are_tracked_not_normalized(self):
        issue_ids = {i.id for i in self.config.known_issues}
        # the four genuine (YES / CHECKING) problems from the doc, kept as open issues
        self.assertIn("request_timestamp_local_timezone", issue_ids)
        self.assertIn("visitor_identity_user_ids_dropped", issue_ids)
        self.assertIn("request_hashed_key_value_mismatch", issue_ids)
        self.assertIn("phase_metrics_value_type_narrowing", issue_ids)

    def test_no_bulk_dropped_prefixes(self):
        # slot, unlike request, has no documented bulk struct drops.
        self.assertEqual(self.config.known_dropped_prefixes, [])
        self.assertFalse(self.config.is_dropped_column("partners__avails_category__avails"))

    def test_empty_collection_equivalence_covers_slot_null_diffs(self):
        eq = self.config.known_value_equivalences
        # the doc's huge "[] vs null" / "[None] vs null" lists collapse via the generic group
        self.assertEqual(eq.normalize("any_column", "[]"), eq.normalize("any_column", None))


class ConfigPathResolutionTests(unittest.TestCase):
    def test_config_path_for_table_points_at_yaml(self):
        self.assertTrue(str(config_path_for_table("slot")).endswith("config/slot.yaml"))
        self.assertTrue(config_path_for_table("slot").exists())
        self.assertTrue(config_path_for_table("request").exists())


if __name__ == "__main__":
    unittest.main()

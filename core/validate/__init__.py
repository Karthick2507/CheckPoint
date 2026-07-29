"""Validation layer — Great Expectations, source-agnostic.

Runs config-driven expectation suites against any ``DataSource``.

    from data_sources import create_data_source, load_connection_config
    from core.validate import GEValidationFramework, load_suite_config

    ds = create_data_source(load_connection_config("config/connections/mrm_presto.example.yml"))
    outcome = GEValidationFramework(ds).run(load_suite_config("config/suites/request_quality.example.yml"))
"""

from core.validate.expectations import build_expectation, expectation_class_name
from core.validate.framework import (
    ExpectationResultRow,
    GEValidationFramework,
    ValidationOutcome,
)
from core.validate.reporting import (
    render_console,
    write_json_report,
    write_markdown_report,
    write_reports,
)
from core.validate.suite_config import (
    AssetConfig,
    ExpectationConfig,
    SuiteConfig,
    load_suite_config,
)

__all__ = [
    "GEValidationFramework",
    "ValidationOutcome",
    "ExpectationResultRow",
    "AssetConfig",
    "ExpectationConfig",
    "SuiteConfig",
    "load_suite_config",
    "build_expectation",
    "expectation_class_name",
    "render_console",
    "write_json_report",
    "write_markdown_report",
    "write_reports",
]

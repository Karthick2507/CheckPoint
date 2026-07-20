"""GE Validation — a config-driven Great Expectations data-quality framework.

This package provides the ``GE_Validation`` component referenced in
``requirements.txt``. It runs Great Expectations (1.x Fluent API) validations
against a Presto/Trino gateway, reusing the same Bearer-token connection style
as ``bcv_analyzer.py``.

Public API::

    from ge_framework import (
        DatasourceConfig,
        SuiteConfig,
        load_datasource_config,
        load_suite_config,
        GEValidationFramework,
    )
"""

from ge_framework.config import (
    AssetConfig,
    DatasourceConfig,
    ExpectationConfig,
    SuiteConfig,
    load_datasource_config,
    load_suite_config,
)
from ge_framework.expectations import build_expectation, expectation_class_name
from ge_framework.framework import GEValidationFramework, ValidationOutcome
from ge_framework.presto import build_connect_args, build_connection_string

__all__ = [
    "AssetConfig",
    "DatasourceConfig",
    "ExpectationConfig",
    "SuiteConfig",
    "load_datasource_config",
    "load_suite_config",
    "build_expectation",
    "expectation_class_name",
    "GEValidationFramework",
    "ValidationOutcome",
    "build_connect_args",
    "build_connection_string",
]

__version__ = "0.1.0"

from __future__ import annotations

import great_expectations as gx
import great_expectations.expectations as gxe
from great_expectations.data_context import AbstractDataContext
from great_expectations.datasource.fluent import SQLDatasource

from ge_validator.config import TableValidationConfig


def build_schema_suite(context: AbstractDataContext, config: TableValidationConfig) -> gx.ExpectationSuite:
    """Schema expectations derived from config's confirmed-matching and known-type-diff lists.

    Deliberately does NOT assert on config.known_dropped_prefixes columns (they're
    documented as intentionally absent) nor on config.excluded_columns (never
    surfaced in the BCV at all) -- asserting their absence would just be re-testing
    a decision already made, not validating anything.
    """
    suite = context.suites.add(gx.ExpectationSuite(name=f"{config.table}_schema_suite"))

    for column in config.confirmed_matching_columns:
        suite.add_expectation(gxe.ExpectColumnToExist(column=column.name))
        if column.type:
            suite.add_expectation(gxe.ExpectColumnValuesToBeOfType(column=column.name, type_=column.type))

    for diff in config.known_type_diffs:
        # Column must still exist on the BCV side; asserted type is the BCV type,
        # since src_type vs bcv_type is exactly the documented, expected difference.
        suite.add_expectation(gxe.ExpectColumnToExist(column=diff.column))
        suite.add_expectation(gxe.ExpectColumnValuesToBeOfType(column=diff.column, type_=diff.bcv_type))

    suite.add_expectation(gxe.ExpectTableRowCountToBeBetween(min_value=1))
    return suite


def run_schema_suite(
    context: AbstractDataContext,
    datasource: SQLDatasource,
    config: TableValidationConfig,
    suite: gx.ExpectationSuite,
) -> gx.core.validation_definition.ValidationDefinition:
    bcv_table_name = config.bcv_table.split(".")[-1]
    asset = datasource.add_table_asset(name=f"{config.table}_bcv_asset", table_name=bcv_table_name)
    batch_definition = asset.add_batch_definition_whole_table(f"{config.table}_bcv_full")

    validation_definition = context.validation_definitions.add(
        gx.ValidationDefinition(
            name=f"{config.table}_schema_validation",
            data=batch_definition,
            suite=suite,
        )
    )
    return validation_definition

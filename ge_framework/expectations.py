"""Turn config dicts into Great Expectations expectation objects.

Config uses the snake_case expectation name (e.g. ``expect_column_values_to_not_be_null``)
which maps to the CamelCase class exported by ``great_expectations.expectations``
(``ExpectColumnValuesToNotBeNull``). Remaining keys become constructor kwargs.
"""

from __future__ import annotations

from typing import Any

import great_expectations.expectations as gxe

from ge_framework.config import ExpectationConfig


def expectation_class_name(exp_type: str) -> str:
    """Convert a snake_case expectation type to its GE class name.

    ``expect_column_values_to_not_be_null`` -> ``ExpectColumnValuesToNotBeNull``.
    """
    parts = [part for part in exp_type.strip().split("_") if part]
    if not parts:
        raise ValueError("Expectation type must not be empty")
    return "".join(part.capitalize() for part in parts)


def build_expectation(cfg: ExpectationConfig) -> gxe.Expectation:
    """Instantiate the GE expectation described by ``cfg``.

    Raises a helpful ``ValueError`` when the type is unknown or the kwargs do
    not match the expectation's schema, so config mistakes fail fast.
    """
    class_name = expectation_class_name(cfg.type)
    expectation_cls = getattr(gxe, class_name, None)
    if expectation_cls is None:
        raise ValueError(
            f"Unknown expectation type {cfg.type!r} (resolved to class {class_name!r}). "
            "See https://greatexpectations.io/expectations for available expectations."
        )
    try:
        return expectation_cls(**cfg.kwargs)
    except Exception as exc:  # pydantic ValidationError, TypeError, ...
        raise ValueError(f"Invalid arguments for expectation {cfg.type!r}: {exc}") from exc


def build_expectations(configs: list[ExpectationConfig]) -> list[gxe.Expectation]:
    """Build a list of expectations, preserving order."""
    return [build_expectation(cfg) for cfg in configs]

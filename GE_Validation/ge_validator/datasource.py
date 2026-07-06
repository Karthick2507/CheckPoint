from __future__ import annotations

import great_expectations as gx
from great_expectations.data_context import AbstractDataContext


def get_context() -> AbstractDataContext:
    return gx.get_context(mode="ephemeral")

"""Custom quality checks beyond native Great Expectations.

Native GE covers completeness and uniqueness; this package adds the four
dimensions that need warehouse-aware logic:

* :class:`~quality.freshness.FreshnessCheck` — data recency
* :class:`~quality.volume_drift.VolumeDriftCheck` — row-count drift vs baseline
* :class:`~quality.schema_drift.SchemaDriftCheck` — column set vs baseline
* :class:`~quality.referential.ReferentialIntegrityCheck` — orphan child keys

Each returns a :class:`~quality.base.CheckResult` and runs warn-and-continue.
"""

from quality.base import CheckResult, QualityCheck, normalize_columns
from quality.freshness import FreshnessCheck
from quality.referential import ReferentialIntegrityCheck
from quality.schema_drift import SchemaDriftCheck
from quality.volume_drift import VolumeDriftCheck

# Registry so checks can be built from pipeline YAML by name.
CHECK_TYPES: dict[str, type[QualityCheck]] = {
    "freshness": FreshnessCheck,
    "volume_drift": VolumeDriftCheck,
    "schema_drift": SchemaDriftCheck,
    "referential_integrity": ReferentialIntegrityCheck,
}

__all__ = [
    "CheckResult",
    "QualityCheck",
    "normalize_columns",
    "FreshnessCheck",
    "VolumeDriftCheck",
    "SchemaDriftCheck",
    "ReferentialIntegrityCheck",
    "CHECK_TYPES",
]

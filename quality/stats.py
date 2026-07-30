"""Robust statistics for drift detection.

A mean baseline is the wrong tool here. One anomalous run drags the centre
toward itself, so the next comparison is measured against a value the data
never really had — and after a few bad runs the anomaly *is* the baseline.
Median (for the centre) and MAD (for spread) are the standard robust
alternatives: both ignore a minority of outliers entirely.
"""

from __future__ import annotations

from statistics import median
from typing import Sequence

# Scale factor making MAD a consistent estimator of the standard deviation for
# normally distributed data, so a MAD-based z-score reads on the familiar scale.
_MAD_TO_SIGMA = 1.4826


def median_value(values: Sequence[float]) -> float | None:
    """Median of ``values``, or ``None`` when empty."""
    return float(median(values)) if values else None


def mad(values: Sequence[float]) -> float:
    """Median absolute deviation — spread that ignores outliers."""
    if not values:
        return 0.0
    centre = median(values)
    return float(median([abs(value - centre) for value in values]))


def relative_deviation(observed: float, centre: float) -> float | None:
    """``|observed - centre| / centre``; ``None`` when centre is zero.

    A zero centre has no meaningful relative scale — the caller must decide
    what "drift from nothing" means rather than silently dividing.
    """
    if centre == 0:
        return None
    return abs(observed - centre) / abs(centre)


def robust_z_score(observed: float, values: Sequence[float]) -> float | None:
    """Outlier score in sigma-equivalents, or ``None`` if spread is zero."""
    if not values:
        return None
    spread = mad(values) * _MAD_TO_SIGMA
    if spread == 0:
        return None
    return (observed - float(median(values))) / spread

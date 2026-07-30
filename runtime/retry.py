"""Retry transient source failures.

A Presto gateway blip, a dropped socket, or a momentary 503 should not fail a
whole pipeline run — the previous BCV tool retried its batches and this
framework had lost that. Retries are **conservative by design**:

* Only errors that look transient are retried. A missing table or a syntax
  error will never succeed on attempt two, and retrying it just wastes minutes
  before reporting the same failure.
* Only **reads** retry by default. Re-issuing a write that may have partially
  applied is how duplicates get created; the caller opts in per call site.
* Backoff is exponential with jitter so a fleet of pipelines recovering from a
  gateway restart does not stampede it.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Iterable, TypeVar

T = TypeVar("T")

# Substrings that indicate a failure worth retrying. Matched case-insensitively
# against the exception text, which is the only portable signal across DBAPIs.
TRANSIENT_MARKERS: tuple[str, ...] = (
    "timeout",
    "timed out",
    "connection reset",
    "connection aborted",
    "connection refused",
    "broken pipe",
    "temporarily unavailable",
    "service unavailable",
    "too many requests",
    "server closed the connection",
    "eof occurred",
    "remote end closed",
    "502",
    "503",
    "504",
    "gateway",
)

# Failures that are definitively the query's fault: never retry these.
PERMANENT_MARKERS: tuple[str, ...] = (
    "syntax error",
    "does not exist",
    "not found",
    "no such table",
    "no such column",
    "permission denied",
    "access denied",
    "unauthorized",
    "forbidden",
)


@dataclass
class RetryPolicy:
    """How often and how fast to retry."""

    attempts: int = 3
    initial_delay: float = 1.0
    multiplier: float = 2.0
    max_delay: float = 30.0
    jitter: float = 0.1

    def delay_for(self, attempt: int) -> float:
        """Delay before ``attempt`` (1-based), with jitter."""
        base = min(self.initial_delay * (self.multiplier ** (attempt - 1)), self.max_delay)
        return base + random.uniform(0, self.jitter * base)


DEFAULT_POLICY = RetryPolicy()


def is_transient(exc: BaseException, markers: Iterable[str] = TRANSIENT_MARKERS) -> bool:
    """Whether ``exc`` looks worth retrying.

    A permanent marker wins: ``"table not found"`` must not be retried merely
    because the message also happens to mention a gateway.
    """
    text = f"{type(exc).__name__}: {exc}".lower()
    if any(marker in text for marker in PERMANENT_MARKERS):
        return False
    return any(marker in text for marker in markers)


def with_retry(
    operation: Callable[[], T],
    policy: RetryPolicy | None = None,
    description: str = "operation",
    on_retry: Callable[[int, BaseException, float], None] | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Run ``operation``, retrying transient failures per ``policy``.

    The final failure is re-raised unchanged so the caller's error handling and
    the run's StageError reporting see the real exception.
    """
    policy = policy or DEFAULT_POLICY
    attempts = max(1, policy.attempts)
    last: BaseException | None = None

    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except Exception as exc:
            last = exc
            if attempt >= attempts or not is_transient(exc):
                raise
            delay = policy.delay_for(attempt)
            if on_retry is not None:
                on_retry(attempt, exc, delay)
            sleep(delay)

    raise last  # pragma: no cover - loop always returns or raises

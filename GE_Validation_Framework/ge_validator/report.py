from __future__ import annotations

from dataclasses import dataclass

from ge_validator.config import TableValidationConfig


@dataclass
class ExpectationOutcome:
    expectation_type: str
    column: str | None
    success: bool
    is_known_issue: bool


def summarize(result, config: TableValidationConfig) -> list[ExpectationOutcome]:
    """Turn a GE ValidationDefinitionResult into outcomes tagged against config's
    known_issue_columns, so a failing known issue is reported distinctly from an
    unexpected new failure -- preserving the team's Y/N discrepancy triage
    (see README's "central data-quality principle") instead of collapsing
    everything into a single pass/fail.
    """
    outcomes = []
    for expectation_result in result.results:
        kwargs = expectation_result.expectation_config.kwargs
        column = kwargs.get("column") or kwargs.get("column_A")
        outcomes.append(
            ExpectationOutcome(
                expectation_type=expectation_result.expectation_config.type,
                column=column,
                success=expectation_result.success,
                is_known_issue=column in config.known_issue_columns if column else False,
            )
        )
    return outcomes


def print_summary(title: str, outcomes: list[ExpectationOutcome]) -> None:
    unexpected_failures = [o for o in outcomes if not o.success and not o.is_known_issue]
    known_issue_results = [o for o in outcomes if o.is_known_issue]

    print(f"\n== {title} ==")
    print(f"Total expectations: {len(outcomes)}")
    print(f"Passed: {sum(1 for o in outcomes if o.success)}")
    print(f"Unexpected failures: {len(unexpected_failures)}")
    for outcome in unexpected_failures:
        print(f"  FAIL  {outcome.expectation_type:45s} column={outcome.column}")

    if known_issue_results:
        print(f"Known issues (tracked, not blocking): {len(known_issue_results)}")
        for outcome in known_issue_results:
            status = "still failing" if not outcome.success else "now passing (config may be stale)"
            print(f"  KNOWN {outcome.expectation_type:45s} column={outcome.column} -- {status}")

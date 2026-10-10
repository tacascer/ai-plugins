# Testing Principles

Testing Principles is a topic in Tim skills for Codex and Claude Code for classifying and auditing tests and designing testable production code. It applies a language-agnostic curriculum based on Vladimir Khorikov's *Unit Testing: Principles, Practices, and Patterns* while preserving repository conventions and reporting missing evidence plainly.

## Workflows

- `classify-tests` explains a test's scope, assertion style, dependencies, boundary, and quality dimensions.
- `audit-tests` reviews existing tests and reports material findings with evidence and uncertainty.
- `design-for-testing` walks through behavior boundaries, test types, dependency treatment, and whether interfaces or test doubles are justified. It explains the evidence behind each decision, preserves production contracts and wiring, and guides authorized testability refactors without requiring test authoring. Ordinary test-writing requests do not activate it.

`design-for-testing` replaces the former `write-tests` workflow; use the new name for explicit invocations.

Classification labels describe a test; they do not grade it. A unit test may be brittle, and an integration test may provide excellent protection against regressions.

Each workflow description is intended to activate its skill automatically for a
matching request. Live automatic-selection behavior is still awaiting the model
checks in the collection's initial verification record. Use the qualified skill
name when selection must be explicit:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Classify | `$tim-skills:classify-tests` | `/tim-skills:classify-tests` |
| Audit | `$tim-skills:audit-tests` | `/tim-skills:audit-tests` |
| Design | `$tim-skills:design-for-testing` | `/tim-skills:design-for-testing` |

For local Claude development, load the complete Tim skills package for one session:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/tim-skills
```

Collection installation commands and their publication status are documented in
the repository-level README.

## Curriculum

Start with [the framework](../../references/testing-principles/framework.md), then read the reference relevant to the task:

- [classification](../../references/testing-principles/classification.md)
- [quality](../../references/testing-principles/quality.md)
- [dependencies and test doubles](../../references/testing-principles/dependencies.md)
- [designing production test seams](../../references/testing-principles/test-seams.md)
- [testing logging behavior](../../references/testing-principles/logging.md)
- [reporting](../../references/testing-principles/reporting.md)
- [sources and provenance](../../references/testing-principles/sources.md)

A [worked decision walkthrough](../../examples/testing-principles/design-decisions.md) connects test scope, doubles, and interfaces in one production design. Original contrast examples cover [behavior and boundaries](../../examples/testing-principles/behavior-boundaries.md), [test doubles](../../examples/testing-principles/test-doubles.md), [integration boundaries](../../examples/testing-principles/integration-boundaries.md), and [production test seams](../../examples/testing-principles/test-seams.md). See also [logging decisions](../../examples/testing-principles/logging.md). No particular language, test framework, mocking library, database, or coverage tool is required.

## Interpretation

Recommendations favor meaningful behavior, isolation between tests, and assertions that survive behavior-preserving refactoring. Dependency treatment follows ownership and observability: use real managed dependencies in integration tests when practical, and use mocks for externally visible effects at unmanaged boundaries. When the boundary or ownership is unknown, report the conditional result and the fact needed to resolve it.

The material is original guidance informed by the sources listed in [sources and provenance](../../references/testing-principles/sources.md). The plugin is not affiliated with or endorsed by the book's author or publisher.

## Evaluation

The [evaluation guide](../../evals/testing-principles/README.md) defines balanced semantic cases,
activation telemetry, hidden grader expectations, and two deliberately defective
source fixtures for design assessment. The initial verification record is stored at
`docs/verification/2026-09-11-initial.md` in the collection repository. It
separates structural and discovery evidence from model activation, reasoning,
and agent-authored executable-test evidence for the former workflow. Those results
do not validate the renamed design workflow. Do not infer behavioral validation
from a passing manifest check.

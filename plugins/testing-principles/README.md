# Testing Principles

Testing Principles is a shared Codex and Claude Code plugin for classifying and auditing tests, designing production test seams, and writing tests. It applies a language-agnostic curriculum based on Vladimir Khorikov's *Unit Testing: Principles, Practices, and Patterns* while preserving repository conventions and reporting missing evidence plainly.

## Workflows

- `classify-tests` explains a test's scope, assertion style, dependencies, boundary, and quality dimensions.
- `audit-tests` reviews existing tests and reports material findings with evidence and uncertainty.
- `write-tests` designs production code for testability and creates or changes idiomatic tests, including regression tests that demonstrate a known failure. It favors minimal seams and checks that production wiring exercises the tested behavior.

Classification labels describe a test; they do not grade it. A unit test may be brittle, and an integration test may provide excellent protection against regressions.

Each workflow description is intended to activate its skill automatically for a
matching request. Live automatic-selection behavior is still awaiting the model
checks in the collection's initial verification record. Use the qualified skill
name when selection must be explicit:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Classify | `$testing-principles:classify-tests` | `/testing-principles:classify-tests` |
| Audit | `$testing-principles:audit-tests` | `/testing-principles:audit-tests` |
| Write | `$testing-principles:write-tests` | `/testing-principles:write-tests` |

For local Claude development, load this directory for one session:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/testing-principles
```

Collection installation commands and their publication status are documented in
the repository-level README.

## Curriculum

Start with [the framework](references/framework.md), then read the reference relevant to the task:

- [classification](references/classification.md)
- [quality](references/quality.md)
- [dependencies and test doubles](references/dependencies.md)
- [designing production test seams](references/test-seams.md)
- [reporting](references/reporting.md)
- [sources and provenance](references/sources.md)

Original contrast examples cover [behavior and boundaries](examples/behavior-boundaries.md), [test doubles](examples/test-doubles.md), [integration boundaries](examples/integration-boundaries.md), and [production test seams](examples/test-seams.md). No particular language, test framework, mocking library, database, or coverage tool is required.

## Interpretation

Recommendations favor meaningful behavior, isolation between tests, and assertions that survive behavior-preserving refactoring. Dependency treatment follows ownership and observability: use real managed dependencies in integration tests when practical, and use mocks for externally visible effects at unmanaged boundaries. When the boundary or ownership is unknown, report the conditional result and the fact needed to resolve it.

The material is original guidance informed by the sources listed in [sources and provenance](references/sources.md). The plugin is not affiliated with or endorsed by the book's author or publisher.

## Evaluation

The [evaluation guide](evals/README.md) defines balanced semantic cases,
activation telemetry, hidden grader expectations, and two deliberately defective
executable fixtures. The initial verification record is stored at
`docs/verification/2026-09-11-initial.md` in the collection repository. It
separates structural and discovery evidence from model activation, reasoning,
and agent-authored executable-test evidence. Do not infer behavioral validation
from a passing manifest check.

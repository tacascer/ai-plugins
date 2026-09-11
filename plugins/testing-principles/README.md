# Testing Principles

Testing Principles is a shared Codex and Claude Code plugin for classifying, auditing, and writing tests. It applies a language-agnostic curriculum based on Vladimir Khorikov's *Unit Testing: Principles, Practices, and Patterns* while preserving repository conventions and reporting missing evidence plainly.

## Workflows

- `classify-tests` explains a test's scope, assertion style, dependencies, boundary, and quality dimensions.
- `audit-tests` reviews existing tests and reports material findings with evidence and uncertainty.
- `write-tests` creates or changes idiomatic tests, including regression tests that demonstrate a known failure.

Classification labels describe a test; they do not grade it. A unit test may be brittle, and an integration test may provide excellent protection against regressions.

## Curriculum

Start with [the framework](references/framework.md), then read the reference relevant to the task:

- [classification](references/classification.md)
- [quality](references/quality.md)
- [dependencies and test doubles](references/dependencies.md)
- [reporting](references/reporting.md)
- [sources and provenance](references/sources.md)

Original contrast examples cover [behavior and boundaries](examples/behavior-boundaries.md), [test doubles](examples/test-doubles.md), and [integration boundaries](examples/integration-boundaries.md). No particular language, test framework, mocking library, database, or coverage tool is required.

## Interpretation

Recommendations favor meaningful behavior, isolation between tests, and assertions that survive behavior-preserving refactoring. Dependency treatment follows ownership and observability: use real managed dependencies in integration tests when practical, and use mocks for externally visible effects at unmanaged boundaries. When the boundary or ownership is unknown, report the conditional result and the fact needed to resolve it.

The material is original guidance informed by the sources listed in [sources and provenance](references/sources.md). The plugin is not affiliated with or endorsed by the book's author or publisher.

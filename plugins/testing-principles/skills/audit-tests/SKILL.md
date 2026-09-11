---
name: audit-tests
description: Use when reviewing existing tests, assessing test quality or coverage adequacy, or identifying brittle assertions and inappropriate test doubles.
---

# Audit Tests

Judge whether tests protect meaningful behavior with proportionate cost. Evidence and uncertainty take priority over broad rules or numerical scores.

## Procedure

1. Identify the requested audit scope. Keep a read-only review read-only unless the user authorizes changes.
2. Discover repository conventions and read [classification](../../references/classification.md), [quality](../../references/quality.md), and [dependencies](../../references/dependencies.md).
3. Inspect the relevant tests, fixtures, production behavior, consumers, and architecture evidence. State the tested boundary before judging assertions or doubles.
4. Rank material findings by impact. For each, identify the test and line, protected behavior, classification evidence, affected quality pillar, confidence, and missing facts.
5. Propose a precise change that preserves useful coverage: retain, improve, relocate, consolidate, or remove only when evidence supports it. Use [reporting](../../references/reporting.md) for the result shape.

Ask what meaningful fault each test detects and whether its assertions survive behavior-preserving refactoring. Treat timings as measured only when observed. Examine fixture clarity and upkeep rather than judging maintainability from line count alone.

Coverage percentage locates executed or unexecuted code; it does not establish adequacy. Do not require one test per method. Neither mandate nor forbid mocks: identify stub input, outgoing mock behavior, ownership, and observers. See [test-double examples](../../examples/test-doubles.md) and [integration examples](../../examples/integration-boundaries.md).

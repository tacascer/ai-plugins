---
name: write-tests
description: Use when creating or modifying tests, including regression tests for a bug fix, and when choosing test scope, assertions, fixtures, or test doubles.
---

# Write Tests

Write the smallest idiomatic test that demonstrates the requested behavior at a deliberate boundary and provides credible fault detection.

## Procedure

1. Identify the requested behavior, client, system boundary, and known failure. Do not invent a requirement when code and intent conflict.
2. Discover the repository's test framework, commands, naming, fixtures, and nearby patterns.
3. Read [classification](../../references/classification.md), [dependencies](../../references/dependencies.md), and [quality](../../references/quality.md). Choose scope from the behavior, feedback needs, and dependency boundary.
4. Prefer output or observable state. Use a stub to supply input without verifying its query; use a mock only for an outgoing effect observable at an unmanaged boundary. Keep unknown ownership as an explicit decision branch.
5. Write an idiomatic test focused on a meaningful fault. A behavior may span several classes. Avoid exposing internals or duplicating production logic merely to make an assertion.
6. Run the narrow relevant check, then the proportionate surrounding checks. For a regression test, capture its failure for the reported defect before the fix and its pass after the fix. If the current state cannot safely reproduce the failure, say that the regression was not demonstrated and report the passing evidence separately.
7. Audit the result against all four quality pillars and report commands and results with [reporting](../../references/reporting.md).

When a request combines review and modification, use this authoring procedure and apply the audit rubric before completion. Adapt to unfamiliar languages through repository tools and documentation; do not impose a framework. Use [behavior examples](../../examples/behavior-boundaries.md) and [test-double examples](../../examples/test-doubles.md) as decision contrasts.

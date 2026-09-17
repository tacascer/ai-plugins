---
name: write-tests
description: Use when creating or modifying tests, designing production code for testability or test seams, refactoring hard-to-test code, or choosing test scope, assertions, fixtures, or test doubles.
---

# Design Test Seams and Write Tests

Design production code with clear responsibilities and controllable boundaries, then write the smallest idiomatic tests that demonstrate meaningful behavior. A seam is a place to supply an input or substitute a dependency without changing the behavior being tested. Use an existing seam when it is sufficient.

## Procedure

1. Identify the requested behavior, client, system boundary, and known failure. Discover repository conventions for production composition, test frameworks, commands, naming, and fixtures. Do not invent a requirement when code and intent conflict.
2. Read [classification](../../references/classification.md), [dependencies](../../references/dependencies.md), and [quality](../../references/quality.md). Choose scope from behavior, feedback needs, and dependency ownership; a behavior may span several real classes.
3. Inspect production testability before adding doubles: identify hidden inputs, internally constructed I/O dependencies, and decisions mixed with effects. Read [test seams](../../references/test-seams.md) when designing or changing production boundaries. State the obstacle, smallest useful seam (or why none is needed), and how production will use it.
4. Within the requested scope, design explicit inputs, boundary injection, or separation of decisions from I/O where they improve control and clarity. Preserve public contracts, error behavior, and production wiring. Before refactoring existing behavior, capture it through the nearest practical boundary; if that is blocked, explain the evidence gap and make the smallest seam change needed to enable verification. A design-only request ends with the proposed design and checks; a tests-only constraint does not authorize production edits.
5. Write an idiomatic test focused on a meaningful fault. Prefer output or observable state. Use a stub to supply input without verifying its query; use a mock for an outgoing effect observable at an unmanaged boundary. Keep unknown ownership as an explicit decision branch. Avoid exposing internals, duplicating production logic, or adding abstractions solely to mock each collaborator.
6. Verify the seam's behavior and its actual production composition. Use real managed dependencies in integration checks when practical; isolated tests of injected objects alone do not verify wiring. Run narrow relevant checks, then proportionate surrounding checks. For a regression, capture failure for the reported defect before the fix and pass after it. If failure cannot safely be reproduced, report the passing evidence separately and say the regression was not demonstrated.
7. Audit all four quality pillars and report commands and results with [reporting](../../references/reporting.md). Include any production seam changed, the preserved contract, composition evidence, and remaining fidelity gaps.

For combined review and modification, use this procedure and apply the audit rubric before completion. Adapt through repository tools and documentation; do not impose a framework. Use [seam examples](../../examples/test-seams.md), [behavior examples](../../examples/behavior-boundaries.md), and [test-double examples](../../examples/test-doubles.md) as decision contrasts.

When logging is involved, read [testing logging behavior](../../references/logging.md). Identify the consumer and contract before asserting or removing log checks; distinguish incidental diagnostics from required events, use explicit seams, and preserve uncertainty about unknown consumers.

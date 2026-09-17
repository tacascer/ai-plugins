---
name: design-for-testing
description: Use when designing production code for testability, choosing test seams or dependency boundaries, or refactoring code with hidden inputs, internally constructed I/O, or decisions tangled with effects.
---

# Design for Testing

Make production behavior easy to exercise through clear responsibilities, explicit inputs, and controllable boundaries. A seam supplies an input or substitutes a dependency without replacing the behavior being checked. Keep an existing design when it is already testable.

This workflow produces a production design and verification approach. Ordinary requests to write tests, choose assertion syntax, or build fixtures do not by themselves call for this skill. Use `audit-tests` to review existing tests and `classify-tests` to explain their scope.

## Procedure

1. Identify the behavior, client, public boundary, and requested scope. Inspect repository conventions for composition and dependency lifetimes. Distinguish a design proposal from an authorized production refactor; test-only work does not authorize production edits.
2. Identify obstacles: ambient time, randomness or configuration, internal I/O construction, shared mutable state, or decisions mixed with effects. Read [test seams](../../references/test-seams.md). For each obstacle, explain what needs control or observation. If existing inputs and outcomes suffice, recommend no new seam.
3. Choose the smallest useful design: explicit values, a boundary collaborator, or cohesive decision logic separated from I/O. Prefer existing idiomatic functions and concrete collaborators. Keep deterministic internal collaborators real; avoid interfaces per helper, public debug accessors, and test-mode branches.
4. Trace production composition through the proposed boundary. Preserve entrypoints, dependency lifetimes, transactions, effect ordering, exception propagation, and input-acquisition timing. Describe where real adapters are supplied and how the normal entrypoint reaches the same logic future tests will exercise.
5. Describe verification at each meaningful boundary using [dependencies](../../references/dependencies.md) and [quality](../../references/quality.md). Identify observable outcomes, controlled inputs, real managed-dependency integration when practical, externally observed unmanaged effects, and a check through normal production composition. Keep unknown ownership conditional. Substitute-only checks do not prove adapter or wiring fidelity.
6. For an authorized refactor, establish a behavior baseline through the nearest practical boundary before moving responsibilities. If no safe baseline exists, state the gap and identify the minimum enabling seam. Apply the design within scope and run available relevant checks. Test authoring follows the task's separate development workflow; this skill does not require writing tests to complete a design.

## Deliverable

Report the behavior and boundary, obstacle (or why none exists), proposed seam and production wiring, preserved contracts, and verification approach. Separate proposed checks from commands actually run and observed results. Name unresolved ownership, baseline, adapter, or composition evidence; never present a proposed check as a demonstrated regression.

Use [seam examples](../../examples/test-seams.md) for design contrasts. For logging boundaries, read [testing logging behavior](../../references/logging.md): identify the consumer and contract, preserve required events, and use explicit seams for incidental diagnostics.

---
name: design-for-testing
description: Use when choosing test types and dependency treatment for a production design, deciding whether interfaces or test doubles are warranted, or refactoring code with hidden inputs, internally constructed I/O, or decisions tangled with effects.
---

# Design for Testing

Walk through Vladimir Khorikov's testing frameworks to choose coverage and production boundaries. Explain how each relevant fact leads to a decision; keep an already testable design. Read [the framework](../../references/framework.md) for the classical interpretation and [sources](../../references/sources.md) for attribution limits.

This produces a design and verification approach. Ordinary test-writing requests alone do not activate it. Use `audit-tests` for reviews and `classify-tests` for classification of existing tests. A design request does not authorize production edits or require test authoring.

## Guided decisions

Inspect available code and conventions first. Explain supported decisions as you go; ask focused questions only for missing facts that change the recommendation. If facts remain unavailable, give conditional branches and name what resolves them. This is not a mandatory questionnaire or approval gate.

1. **Establish behavior and boundary.** Identify the client, promised outcome, and components inside the system. Distinguish observable behavior from implementation details. Name testability obstacles, if any, separately from behavior defects.
2. **Map dependencies.** Use [dependencies](../../references/dependencies.md) to determine shared/private, in/out of process, and, for out-of-process dependencies, managed/unmanaged. Cite ownership, external consumers, and fixture lifecycle evidence; technology names alone do not settle these axes.
3. **Choose coverage.** Use [classification](../../references/classification.md) to propose unit, integration, and any useful end-to-end checks. Explain the cohesive behavior, isolation, feedback-speed assumptions, and boundaries each exercises. Several real classes can form one unit. Cover decisions directly and meaningful application paths with real managed dependencies when practical. Add a broad entrypoint check when it protects wiring or behavior missing from narrower coverage. Classify output, state, and communication assertions separately from scope. Proposed speed and isolation remain unverified without evidence.
4. **Choose dependency treatment.** Keep deterministic internal collaborators real. For necessary substitutes, explain that test double is the umbrella term: stubs supply inputs; mocks verify observable outgoing effects; spies record interactions; fakes simplify implementations. Choose by use, not library name. Assert results of stub inputs, not query counts. Explain why an outgoing interaction is externally observable before verifying it. Identify lost adapter or provider fidelity.
5. **Decide on interfaces and seams.** Follow [test seams](../../references/test-seams.md#decide-whether-an-interface-is-needed). Evaluate existing inputs and concrete collaborators, separating decisions from I/O, and only then a needed interface. State introduce, reuse, or no new interface and why. Trace real production composition; preserve lifetimes, transactions, effect ordering, exceptions, and input-acquisition timing. For an authorized refactor, establish a behavior baseline before moving responsibilities; name any gap and the minimum enabling seam.
6. **Check value and summarize.** Apply the four [quality pillars](../../references/quality.md): regression protection, refactoring resistance, feedback speed, and maintainability. Explain the distinct fault each proposed check detects and unnecessary duplication it avoids.

## Deliverable

For each meaningful behavior, report the boundary, proposed test scope and rationale, assertion style and outcome, real dependencies or double roles, interface/seam decision, and missing evidence. Include production wiring and preserved contracts. Separate proposed verification from commands run and observed results; design completion does not demonstrate a regression test.

See the [worked decision walkthrough](../../examples/design-decisions.md) and [seam examples](../../examples/test-seams.md). For logging consumers and contracts, read [logging](../../references/logging.md).

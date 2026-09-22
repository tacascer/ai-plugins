# Designing production test seams

A useful seam gives control over a relevant input or effect while keeping the production behavior under test real. Testability is a production design concern: make responsibilities and dependencies explicit without turning every implementation detail into an extension point.

## Choose the smallest useful change

Describe the behavior to protect, what prevents exercising it, the proposed seam, and the check that will exercise its production use. If the behavior is already easy to exercise, keep the design.

| Observed obstacle | Candidate seam | Evidence to retain |
| --- | --- | --- |
| Logic reads an ambient value such as the current time, randomness, or configuration | Pass a value when one snapshot is the contract; pass a small callable/provider when repeated acquisition matters | Deterministic results plus a check that production supplies the intended value at the intended point |
| A function constructs a network, database, or filesystem client internally | Supply the boundary dependency through the repository's normal constructor, function parameter, or composition mechanism | Observable application behavior and a check through the real adapter and production composition |
| Business decisions are tangled with reads and writes | Extract cohesive decision logic operating on data; leave orchestration responsible for I/O | Direct decision tests and integration coverage that orchestration actually uses those decisions |
| Several deterministic internal helpers collaborate | Usually no new seam; exercise them together | Assertions on the enclosing behavior that survive helper rearrangement |

Choose idiomatic functions, values, concrete collaborators, or existing interfaces before introducing a new abstraction. An interface is useful when it expresses a real boundary contract; one per class is not a testability requirement. Keep test fixtures, recorders, and fake implementations in test support.

## Decide whether an interface is needed

An interface is a production design choice; a test double is a test dependency's role. Dependency injection can use a value, callable, or concrete collaborator without introducing a new interface, trait, or protocol.

| Evidence | Decision | Reason |
| --- | --- | --- |
| Existing inputs and observable outputs already permit exercising the behavior | No new seam or interface | Additional indirection adds no control or coverage |
| Deterministic internal collaborators implement one cohesive behavior | Keep them real | Class boundaries need not become test boundaries |
| Decisions and managed database I/O are intertwined | Separate decisions operating on data from orchestration; retain concrete persistence where suitable | Unit checks cover decisions; real-database integration checks cover persistence without a repository interface solely for mocking |
| An existing callable or collaborator parameter supports necessary substitution | Reuse it | A second wrapper is unnecessary unless it supplies a missing contract |
| An unmanaged boundary needs substitution and the language or existing architecture requires a declared contract | Introduce a narrow interface at that boundary | A production adapter and test substitute can exercise the observable contract without contacting the live provider |
| Actual alternative production implementations share a meaningful contract | An interface may express that abstraction | Justify it with existing variation rather than hypothetical future implementations |

These are reasons to assess a design, not instructions to remove existing repository abstractions. Respect architectural constraints and authorized scope. For each proposed interface, name the contract, the consumer, the implementations or substitution need, and why simpler inputs or existing collaborators do not suffice. Keep doubles in test support.

Khorikov's [repository-interface discussion](https://enterprisecraftsmanship.com/posts/interfaces-for-repositories/) motivates isolating domain decisions and testing owned persistence directly. The language-neutral decision table is this plugin's application of that reasoning; see [provenance](sources.md).

## Preserve production semantics

Keep existing entrypoints working and route them through the same logic exercised by tests. Wire real dependencies through normal application setup. An injected component that the production entrypoint bypasses is not evidence that production behavior is covered.

For existing code, run existing behavior checks and add focused characterization at an accessible boundary before moving responsibilities. Characterization records current behavior; it does not establish that a known defect is correct. If dependencies prevent a safe baseline, state that limitation, introduce only the minimum enabling seam, and then verify the resulting path. Distinguish this evidence from a demonstrated before/after regression.

Preserve dependency lifetime, transaction boundaries, effect order, exception propagation, and input-acquisition timing where they affect behavior. For example, replacing repeated reads with a single snapshot or moving a send across a commit can change behavior even when isolated decision tests pass. Do not redesign unrelated temporal storage or scheduling just to control a clock input.

## Pair control with fidelity

Direct tests should execute the actual production decision logic and assert independently specified outcomes. Keep meaningful internal collaborators real. A stubbed read may make a decision deterministic, but query counts and helper calls usually describe replaceable steps.

Integration checks should cover the application path with real managed dependencies when practical, using isolated data. Verify externally observed outgoing contracts at unmanaged boundaries with an appropriate mock, spy, or recording endpoint. A recording endpoint can exercise a real client adapter but does not establish compatibility with a live provider by itself. When ownership is unknown, follow both branches in [dependencies](dependencies.md).

Cover production composition with a focused check through the normal entrypoint or factory: real decision logic, intended adapters, and safe test configuration. It may share a test with application integration coverage. Check outcomes rather than constructor-call expectations. If environment constraints prevent this, report exactly which wiring or adapter behavior remains unverified.

## Stop at the useful boundary

Avoid public debug accessors, private-method assertions, test-mode switches that bypass real behavior, and broad monkeypatching as a substitute for a maintainable seam. A targeted patch can help characterize legacy behavior when production edits are prohibited; record its coupling and fidelity limits rather than presenting it as production design.

A request to design test seams can be satisfied before tests exist by describing the proposed production boundary and verification approach. A request restricted to writing tests should use existing boundaries and explain any recommended production change without silently making it.

See [seam examples](../examples/test-seams.md) for a concrete before/after contrast.

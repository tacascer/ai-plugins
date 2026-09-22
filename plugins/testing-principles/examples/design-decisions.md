# Worked design decisions: registration

## Context and boundary

Registration reads account data from an exclusively owned PostgreSQL database, applies eligibility rules implemented by three deterministic classes, queries an independently owned read-only risk service, persists acceptance, commits, and sends one welcome email through an external provider. Only Registration exposes the database data. Risk and mail collaborators are already parameters; decisions and database I/O are mixed in one handler.

The client wants a registration outcome and the promised notification. Eligibility is also a cohesive decision boundary. Neither boundary promises a particular helper-call sequence. Here, one email means one send per successful invocation; delivery across retries or crashes needs a separately specified contract.

## Dependency evidence

| Dependency | Facts | Treatment |
| --- | --- | --- |
| Eligibility classes | In process; construct fresh instances per test | Keep real together; no interface per class |
| PostgreSQL | Out of process; exclusively owned with no direct external readers, so managed | Use real PostgreSQL with isolated data for application integration checks |
| Risk service | Out of process; independently owned, so unmanaged; supplies query input | Reuse risk parameter with stub responses; assert resulting registration behavior |
| Mail provider | Out of process; independently observed sends, so unmanaged | Reuse sender parameter with a spy serving a mock role; verify the promised send |

Shared/private depends on fixture lifecycle, not these production ownership facts. Isolated data is a proposal until setup and cleanup are verified. If other applications later read database writes directly, reassess the relevant contract as externally observed.

## Coverage and interface decisions

| Behavior or risk | Proposed scope and assertion | Interface decision and rationale |
| --- | --- | --- |
| Eligibility rules, including rejection edges | Intended unit tests: output-based checks across all three real classes; cohesive behavior, planned isolation, speed unverified | Extract decisions accepting account data. No new interface: explicit inputs and outputs suffice |
| Acceptance persists and failed commits prevent sending | Integration through Registration with real PostgreSQL, risk stub, and mail recorder; state plus communication assertions | Retain concrete persistence and reuse existing parameters. Mocking repository calls would omit persistence and transaction faults |
| Risk refusal changes the result | Controlled stub input; assert refusal and absence of promised-success effects at the application boundary | Reuse the risk seam. A mocking library supplying responses still serves a stub role; lookup count is not the contract |
| Successful registration sends once after commit | Integration with the same real database and sender recorder; verify recipient, payload, and count, with committed state observable from another connection when sending | The spy serves a mock role because the outgoing effect is promised to an external observer |
| HTTP routing and normal composition reach these behaviors | One broad end-to-end integration path through the normal server factory and HTTP entrypoint, real database and client adapters, safe local risk/mail endpoints | Configure existing adapters. This protects wiring absent from direct handler checks; local endpoints do not prove live-provider compatibility |

Test double is the umbrella term. A simplified working risk service is a fake used as a stub when it supplies responses; a recording mail endpoint is a fake used as a mock when assertions verify outgoing effects. Those roles do not turn the real-database path into a unit test. Output, state, and communication describe assertions, independently of scope.

If the sender were internally constructed and the language required a declared type for substitution, a narrow sender interface could be justified at the unmanaged boundary. Here it would duplicate an existing seam. An interface may also represent actual alternative production implementations; speculative future implementations are not evidence of a current need.

## Production path and value

Keep the normal handler responsible for acquisition and effects, invoking the extracted decisions. Preserve dependency lifetimes, transaction scope, risk-query timing, commit-before-send ordering, and exception behavior. Establish a practical behavior baseline before an authorized extraction. Design-only work makes no code changes.

Decision checks target rule faults with low fixture cost; application checks target persistence and ordering faults; the broad path targets routing and wiring faults. Assertions on results and external contracts should resist helper refactoring. These are inferred benefits: no timings, executed regressions, or observed refactors exist yet. Reuse an application check for composition where it already reaches the normal entrypoint rather than adding redundant coverage.

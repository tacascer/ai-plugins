---
name: ask-tim
description: Ask which Tim skill or short flow fits your situation.
disable-model-invocation: true
---

# Ask Tim

Choose among the workflows supplied by **Tim skills**. Recommend a next step,
explain why it fits, and leave invoking it to the user.

## Choose the route

1. Establish the outcome the user wants and the decision blocking it. Inspect
   available context for facts; ask a focused question only when the missing
   answer would change the recommendation.
2. Use the map below to shortlist candidates. Before explaining a candidate's
   behavior, recommending it, or ruling out a plausible alternative, read its
   linked `SKILL.md`. The map is orientation; the skill body owns its scope.
   Read candidates as reference material for routing, without starting their
   procedures. If a candidate file is unavailable, say that its fit cannot be
   verified from this installation rather than inventing its behavior.
3. Lead with the skill that addresses the main unresolved decision. Add a short
   ordered flow only when each additional skill answers a distinct need. Explain
   the dependency or trigger for each next step; a topic mention alone does not
   justify another workflow.
4. Return the recommendation, a brief reason, and a ready-to-use invocation
   containing the user's task. Use `$tim-skills:<skill-name>` in Codex or
   `/tim-skills:<skill-name>` in Claude Code. If the platform is unknown, label
   both forms. Stop after routing; the user chooses when to start the workflow.

When no Tim skill fits, say so and suggest handling the task directly or
clarifying its scope. Keep recommendations within this plugin. A routing request
alone authorizes neither application edits nor installation of missing skills.

## Workflow map

### Testing

- [design-for-testing](../design-for-testing/SKILL.md): choose coverage,
  dependency treatment, and production seams for a concrete design or
  testability obstacle. Ordinary test authoring alone does not call for it.
- [audit-tests](../audit-tests/SKILL.md): assess existing tests, coverage
  adequacy, brittle assertions, and test doubles.
- [classify-tests](../classify-tests/SKILL.md): explain existing tests' scope,
  assertion style, isolation, and dependency roles.

### Time modeling

- [design-time-models](../design-time-models/SKILL.md): choose temporal
  representations, scheduling semantics, and conversion policies.
- [audit-time-models](../audit-time-models/SKILL.md): investigate existing
  temporal storage, scheduling, and time-zone behavior against intended rules.

Incidental timestamps in prose do not call for either workflow.

### Observability

- [design-observability](../design-observability/SKILL.md): choose structured
  event contracts, listener boundaries, signal mappings, and delivery policy.
- [implement-observability](../implement-observability/SKILL.md): implement
  logs, metrics, or traces through the event/listener boundary and wire
  OpenTelemetry and export in code.
- [audit-observability](../audit-observability/SKILL.md): investigate existing
  event production, signal meaning, missing or duplicate signals, and delivery.

For a concrete implementation request with settled contracts, start with
`implement-observability`. Suggest `design-observability` first only if an
unresolved architecture decision blocks the requested implementation. Standalone
vendor administration does not call for these application workflows.

### Business domain models

- [design-domain-model](../design-domain-model/SKILL.md): choose business
  rules, ownership, invariants, aggregates, and business-event interactions.
- [audit-domain-model](../audit-domain-model/SKILL.md): assess those existing
  models and integrations for evidenced risks.

Here, domain means the business domain; DNS configuration is outside this scope.

### Rust

- [design-rust](../design-rust/SKILL.md): choose Rust boundaries, ownership,
  APIs, concurrency, library treatment, or other patterns for concrete behavior.
- [audit-rust](../audit-rust/SKILL.md): assess existing Rust patterns and their
  correctness or maintainability against a concrete contract.

Formatting and routine edits to Rust files do not themselves call for either.

### GraphQL

- [design-graphql](../design-graphql/SKILL.md): design Relay-compatible server
  identification, refetching, connections, and pagination contracts.
- [audit-graphql](../audit-graphql/SKILL.md): assess existing server schemas
  and resolver behavior for Relay compatibility.

Unrelated REST work and client-only presentation are outside this scope.

## Overlapping topics

Choose by the requested outcome, rather than the implementation language or
similar vocabulary. Examples of short flows, when both needs are present:

- A Rust scheduler whose wall-clock and time-zone policy is unresolved:
  `design-time-models`, then `design-rust` if translating that policy into Rust
  types or execution requires a separate design decision.
- Telemetry whose event ownership is undecided before implementation:
  `design-observability`, then `implement-observability` to build the agreed
  boundary. A review-only request starts at `audit-observability`.
- Existing tests with questionable assertions and an internally constructed
  network client: `audit-tests`, then `design-for-testing` if the audit shows
  that a production seam is needed. A classification-only request starts and
  ends with `classify-tests`.

These are conditional routes, not a mandatory lifecycle. Preserve the user's
requested scope and the selected skills' authorization boundaries.

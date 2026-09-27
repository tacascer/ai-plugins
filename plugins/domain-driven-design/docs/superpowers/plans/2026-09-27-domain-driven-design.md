# Domain-Driven Design Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a language-agnostic DDD plugin for new designs and existing-system audits, including dedicated event-driven design guidance.

**Architecture:** Two skills share a selectively loaded reference library and original examples. Scenario evaluations exercise decisions and activation separately; the existing repository tools validate packaging.

**Tech Stack:** Markdown skills and references, JSON manifests and evaluation cases, existing Python/PyYAML repository tooling. No new runtime dependencies.

**Spec:** [Approved design](../specs/2026-09-27-domain-driven-design-design.md).

## Global Constraints

- Work in the existing isolated worktree `/home/tacascer/Projects/ai-plugins/.worktrees/domain-driven-design`, branch `feat/domain-driven-design`.
- Package: `plugins/domain-driven-design/`; version: `0.1.0`.
- Skills: `design-domain-model` and `audit-domain-model`.
- Give equal weight to new design and existing-system assessment and evolution.
- Audits remain read-only unless changes are also requested.
- Keep all plugin content inside its own directory; do not duplicate guidance by platform.
- User configuration, installation, and NixOS changes are outside this delivery.
- Use original prose and examples; distinguish verified book guidance from supplementary synthesis.
- Native validation supplements repository checks; neither proves model behavior.
- Before every commit, run all three repository checks listed under Verification below.

## Review Focus

- Incomplete business rules: ask the responsible domain expert rather than invent policy (Task 1, `design-missing-rule`).
- Partial repository access: bound findings to observed evidence and state limitations (Task 1, `audit-partial-evidence`).
- Mixed producer/consumer versions: preserve compatibility during migration (Task 2, `audit-event-evolution`).
- Local telemetry mistaken for durable business integration: distinguish consumers and delivery obligations (Task 2, `audit-telemetry-delivery`).
- Sound simple code: permit no-change findings and avoid pattern-driven rewrites (Task 1, `audit-sound-simple`).

## File map and verification

All paths below beginning with `references/`, `skills/`, `examples/`, `evals/`, or
`docs/` are relative to `plugins/domain-driven-design/`.

Task 1 owns the strategic/tactical references, common procedure, reporting,
source map, two skills, manifests, package README, initial examples/evaluations,
and repository inventory integration. Task 2 extends these with event-driven
design, evolution, and an audit fixture. Task 3 owns evaluation execution and the
final verification record. No repository scripts or test interfaces change.

Run from the worktree root before each commit:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

Expected: unittest reports `OK` (baseline: 30 tests); the other commands exit zero.
Regenerate catalogs with `.venv/bin/python -m scripts.catalogs` after changing
inventory or manifests. Generated files are `.agents/plugins/marketplace.json`
and `.claude-plugin/marketplace.json`. Stage explicit paths and use conventional
commits. Existing structural tests suffice; do not add tests for prose wording.

## Task 1: Deliver strategic and tactical design/audit workflows

**Create:** `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `README.md`;
`skills/design-domain-model/SKILL.md`, `skills/audit-domain-model/SKILL.md`;
`references/principles.md`, `references/strategic-design.md`,
`references/tactical-design.md`, `references/reporting.md`, `references/sources.md`;
`examples/domain-decisions.md`; `evals/cases.json`, `evals/README.md`.

**Modify:** repository `README.md`, `catalogs/plugins.json`, generated catalogs.

**Interfaces:** Consumes the approved spec and existing time-modeling package
conventions. Produces the two plugin-qualified skill identities, shared reference
paths, and evaluation schema used by Tasks 2 and 3. Cases are JSON objects with
`id`, `mode`, `invocation`, `prompt`, `context`, `expected_activation`,
`required_findings`, and `forbidden_findings`, as in time-modeling's cases.

- [ ] **1. Verify source grounding.** Consult accessible publisher or author material for strategic and tactical topics. Populate `sources.md` with source links, supported topics, access limits, and separate authoring conventions. A contents page establishes coverage, not detailed claims. If central advice cannot be verified, request relevant source material rather than present it as confirmed book content.
- [ ] **2. Author ten evaluation cases before the workflow prose.** Use the exact IDs and semantic assertions below; keep expected results outside submitted prompts/context.

| ID | Required outcome | Forbidden outcome |
| --- | --- | --- |
| `design-simple-logic` | Prefer proportionate simple implementation for supplied CRUD rules | Mandate aggregates or event sourcing |
| `design-context-language` | Separate conflicting meanings of the same business term | Force one universal entity |
| `audit-context-boundaries` | Distinguish business subdomains, model scope, and deployment | One service per aggregate as a rule |
| `audit-invariant` | Identify the supplied cross-transaction invariant violation and its consequence | Criticize only naming or folder layout |
| `design-context-integration` | Assign ownership and justify model translation | Share persistence entities by default |
| `design-missing-rule` | Ask the domain expert the policy question that changes the design | Invent that policy |
| `audit-sound-simple` | Recommend no change for the adequate implementation | Require DDD abstractions without benefit |
| `audit-partial-evidence` | State access limits and qualify suspected problems | Claim unseen code is defective |
| `design-eventstorming` | Propose stakeholder discovery and label candidate models provisional | Present agent guesses as expert agreement |
| `negative-dns-domain` | No DDD workflow activation for a DNS configuration request | Treat DNS domains as bounded contexts |

- [ ] **3. Define the evaluation protocol.** Follow `plugins/time-modeling/evals/README.md`: submit only prompt/context, keep graders hidden, isolate runtime content, and record semantics and activation separately. Use explicit invocation for `design-missing-rule` and `audit-partial-evidence`; other initial cases exercise implicit selection. Expected identities are `domain-driven-design:design-domain-model`, `domain-driven-design:audit-domain-model`, or an empty list for the negative case. Before authoring skills, attempt a small no-plugin baseline on simple logic, invariant, and missing-rule cases if isolated inference is available; preserve unavailable outcomes without pretending a failure occurred.
- [ ] **4. Write the shared guidance and examples.** Cover subdomain classification, context-scoped language, ownership/context relationships, EventStorming, invariants, aggregates, entities/value objects, and the implementation/architecture choices in the spec. `principles.md` routes by task; `reporting.md` defines evidence, assumptions, trade-offs, open questions, corrections, and proposed versus executed checks. Examples contrast simple logic with invariant-rich modeling using original scenarios.
- [ ] **5. Write both skill entry points.** Follow the spec's ordered procedures, selective reference loading, proportional output, and audit authorization boundaries. Descriptions must cover business-event tasks as well as domain models. Keep design outputs actionable and audit findings supported by locations or supplied scenario evidence.
- [ ] **6. Package and register.** Follow the time-modeling manifest shapes with name `domain-driven-design`, version `0.1.0`, display name `Domain-Driven Design`, and author `tacascer`. Describe practical design/audit guidance, including event-driven systems. Document explicit Codex/Claude invocation and honest evaluation status. Append the inventory entry, update the root README, and regenerate catalogs. Add only links whose targets exist at this stage.
- [ ] **7. Verify and commit.** Run the full Verification commands. Review the ten cases against the authored guidance; label this static review, not model evaluation. Commit `feat(domain-driven-design): add strategic and tactical workflows`.

## Task 2: Add event-driven decisions, evolution, and evidence fixtures

**Create:** `references/event-driven-design.md`, `references/evolution.md`,
`examples/event-driven-decisions.md`, `evals/fixtures/order-flow/README.md`,
`evals/fixtures/order-flow/order_flow.py`, `evals/fixtures/order-flow/contracts.json`.

**Modify:** `references/principles.md`, `references/sources.md`, both skill entry
points, package `README.md`, `evals/cases.json`, `evals/README.md`.

**Interfaces:** Consumes Task 1's two workflows and case schema. Produces two
additional routed references and a stdlib-only audit fixture copied into isolated
evaluation workspaces. The fixture is evidence for review, not production code.

- [ ] **1. Extend source mapping.** Verify advice concerning communication patterns, evolution, and event-driven architecture against accessible primary sources, particularly chapters 9, 11, and 15. Clearly label supplementary reliability guidance and avoid unsupported detailed attribution.
- [ ] **2. Add eleven cases before extending guidance.** Make `audit-publication-gap` an explicit invocation; others use implicit selection. Use the same schema and grading isolation as Task 1.

| ID | Required outcome | Forbidden outcome |
| --- | --- | --- |
| `design-event-semantics` | Distinguish request intent, business facts, and external contracts | Relabel a directed command as an event to disguise intent |
| `audit-event-leakage` | Identify consumer dependence on internal persistence shape | Assume serialization is a stable integration contract |
| `design-event-content` | Compare notification and carried state for supplied consumer needs | Always send full internal objects |
| `audit-distributed-decisions` | Trace dispersed business decisions and explain functional coupling | Claim asynchronous transport removes all coupling |
| `audit-publication-gap` | Cite fixture's state/publication gap and propose proportionate coordination | Claim the broker makes the database write atomic |
| `audit-duplicate-ordering` | Address duplicate effects and scoped out-of-order delivery | Promise exactly-once business effects from transport alone |
| `design-compensation` | Specify workflow ownership, partial failure, and compensation limits | Treat compensation as guaranteed global rollback |
| `design-pattern-independence` | Assess CQRS and event sourcing separately | Require both whenever messaging is used |
| `audit-event-evolution` | Plan compatible old/new consumer coexistence and verification | Replace all contracts atomically without evidence that this is possible |
| `audit-telemetry-delivery` | Distinguish best-effort telemetry from required business delivery | Treat local logging as reliable integration |
| `design-domain-evolution` | Revisit boundaries and investment after changed business importance | Freeze subdomain classification permanently |

- [ ] **3. Build the original order-flow fixture.** Document order acceptance and single-fulfillment requirements in the fixture README without identifying defects. `order_flow.py` visibly commits acceptance before publishing, and its consumer exposes duplicate and ordering behavior. `contracts.json` shows a message exposing persistence fields. Keep contracts and code consistent and use stable symbols for grader citations. Route the publication, duplicate/ordering, and leakage audit cases to copies of these files; do not expose grader expectations with them.
- [ ] **4. Author the two references and examples.** Implement every event-driven bullet and evolution requirement from the spec, including temporal/functional/implementation coupling, event content, choreography/sagas/process managers, publication consistency, retries, ordering, compensation, incremental changes, and contract coexistence. Keep microservices and data mesh contextual. Contrast viable choices and business consequences, including when asynchronous integration is unnecessary.
- [ ] **5. Integrate routing and output.** Link the new references from principles and both skills. Make producer/consumer responsibilities, consistency and recovery part of relevant design outputs and evidence tracing part of event audits. Update sources, README, and evaluation documentation to reflect all 21 cases.
- [ ] **6. Verify and commit.** Run Verification commands, compile the fixture with `.venv/bin/python -m py_compile plugins/domain-driven-design/evals/fixtures/order-flow/order_flow.py`, and check every rubric against its supplied scenario or fixture. Compilation checks fixture syntax only. Commit `feat(domain-driven-design): add event-driven design and evolution guidance`.

## Task 3: Evaluate behavior and record delivery evidence

**Create:** `docs/verification/2026-09-27-initial.md`.

**Modify as evidence requires:** skill descriptions, references, examples, cases,
and package README. Keep raw runs under ignored `.eval-runs/`.

**Interfaces:** Consumes all 21 cases and the runtime package. Produces a committed
verification record with exact commands, tool versions, per-case outcomes for
attempted inference, limitations, and actual availability of each check.

- [ ] **1. Inspect available native tools and isolated loading.** Use supported session-only loading or disposable configuration. Do not install the plugin into user configuration. If no grader-isolated model run is available, record that constraint and continue with structural verification; do not label behavior passing.
- [ ] **2. Execute cases on an available isolated harness.** Copy only manifests, skills, references, and examples into the runtime package; give fixture cases only their designated fixture files. Exclude docs, README, evaluation cases, and the original checkout. Submit each case's prompt/context once. Record platform/version/model/time, exact input, transcript, observed activation identities, selection match, and semantic pass/fail/unverified. Unknown activation stays unknown. Keep any earlier baseline distinct.
- [ ] **3. Correct demonstrated content defects.** Change only guidance or cases implicated by evidence; preserve failed attempts and rerun affected cases after correction. Grade meaning rather than exact wording. Do not infer correctness of unexecuted cases or another platform from successful runs.
- [ ] **4. Run structural and available supplemental checks.** Run Verification commands. Where available, run `claude plugin validate --strict plugins/domain-driven-design` and the installed Codex plugin validator according to its actual interface. Record unavailability and distinguish supplemental schema checks from semantics. Inspect generated catalog entries for both platforms.
- [ ] **5. Record evidence and finish.** Write the verification record and link it from README; list pending checks precisely. Review the full branch diff against the spec, confirm plugin containment, source limits, both workflows, all references, and all 21 cases. Run Verification after final edits, then commit `docs(domain-driven-design): record plugin verification`. Leave publication or PR creation to a user request.

## Plan review and execution handoff

Self-review: the three tasks cover every spec component, including contextual
microservices/data-mesh guidance and all fifteen evaluation categories. The five
Review Focus conditions each have a named case. No runtime API or repository
validator change is required; task interfaces are file paths, skill identities,
and the existing case schema.

Recommended execution: native implementation in this session followed by a fresh
whole-branch reviewer. The references and workflows share terminology closely,
so maintaining one implementation context should reduce inconsistency. The user
must review this plan and select native or subagent-driven execution before work
starts.

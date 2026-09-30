# GraphQL Design Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a language-agnostic GraphQL design and audit plugin with Relay compatibility as its required baseline.

**Architecture:** Two shared skills route to focused references and original examples. Package metadata supports Codex and Claude without duplicating content; evaluation prompts and fixtures assess selection and reasoning separately from structural checks.

**Tech Stack:** Markdown skills/references, JSON manifests/catalogs/evaluations, existing Python repository validators, stdlib Python audit fixtures.

**Spec:** [Approved design](../specs/2026-09-30-graphql-design-design.md).

## Global Constraints

- Package name `graphql-design`; skills `design-graphql` and `audit-graphql`.
- Matching Codex and Claude manifests, initial version `0.1.0`.
- Relay compatibility is the required baseline, including without a Relay client.
- Both workflows are language- and framework-agnostic; no sibling dependency.
- All plugin content stays under `plugins/graphql-design/`.
- Audits are read-only unless fixes are separately requested; guidance alone does not authorize application edits or installations.
- Distinguish formal requirements, optional features, and engineering recommendations.
- No user configuration changes, application scaffolding, or general mutation/federation/subscription curriculum.
- Use the existing `feat/graphql-design` worktree; conventional commits only.
- Structural validation cannot establish exhaustive platform conformance or live agent behavior.

## Review Focus

- No Relay client: retain required contracts (`design-no-relay-client`, Task 1).
- Valid unconventional choices: accept non-base64 IDs, forward-only connections, and non-Node edge values (`audit-valid-options`, Task 1).
- Schema-only access: bound conclusions and mark runtime behavior unverified (`audit-schema-only`, Task 1).
- Boundary counts: accept zero, reject negative sizes, and distinguish empty-page cursors from page flags (`audit-count-boundaries`, Task 2).
- Directional asymmetry: preserve ordering while respecting permitted opposite-direction flag concessions (`audit-page-flags`, Task 2).

## File map and shared verification

Paths below are relative to `plugins/graphql-design/` unless prefixed with
`repository`. Tasks use existing repository interfaces; no tooling changes or
prose-string unit tests are needed. Before Task 1, read the applicable
skill-authoring and plugin-creation skills; preserve this approved scope.

Run from the worktree root before every commit:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

Expected: unittest reports `OK` (current baseline: 30 tests); other checks exit
zero. After inventory/manifest edits first run `.venv/bin/python -m scripts.catalogs`.
Stage explicit paths. Do not interpret a successful structural check as a passed
semantic evaluation. Author semantic cases before guidance and attempt baseline
inference only when an isolated harness is available; unavailable is not failed.

## Task 1: Deliver the two workflows and shared Relay guidance

**Create:** `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `README.md`,
`skills/design-graphql/SKILL.md`, `skills/audit-graphql/SKILL.md`,
`references/principles.md`, `references/identification.md`,
`references/connections.md`, `references/reporting.md`, `references/sources.md`,
`examples/design-decisions.md`, `evals/cases.json`, `evals/README.md`.

**Modify:** repository `README.md`, `catalogs/plugins.json`,
`.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`.

**Interfaces:** Consumes the approved spec and existing time-modeling manifest
shapes. Produces `graphql-design:design-graphql` and
`graphql-design:audit-graphql`; references above are the stable routing targets.
Evaluation cases use the existing JSON array schema: `id`, `mode`, `invocation`,
`prompt`, `context`, `expected_activation`, `required_findings`,
`forbidden_findings`, and optional `fixture_paths`. Modes are `design`, `audit`,
or `negative`; invocation is `explicit` or `implicit`. Expected activation is an
array of plugin-qualified identities, empty for negative cases.

- [ ] **1. Verify the source map.** Read the guide and linked formal identification/connection specifications. Record exact URLs, access date, accessible version, and any limits in `sources.md`. Map formal rules to sections; label independent engineering advice. Use original synthesis, not upstream prose or the Star Wars example.
- [ ] **2. Author these ten cases before workflow prose.** Use explicit invocation for `design-missing-order` and `audit-schema-only`; all others exercise implicit selection. Provide enough concrete schema or scenario data to judge each outcome.

| ID | Required outcome | Forbidden outcome |
| --- | --- | --- |
| `design-no-relay-client` | Propose Node lookup and connection contracts for a catalog with refetchable items and paginated collections | Drop baseline because clients currently use plain fetch |
| `design-missing-order` | Ask for missing business ordering, or present a conditional proposal | Invent a confirmed ordering policy |
| `design-migration` | Preserve existing clients while adding required identity and pagination contracts | Recommend an unexplained breaking replacement |
| `audit-node-shape` | Identify extra Node interface fields and wrong node argument/return shape in supplied SDL | Treat resemblance to example SDL as full compatibility |
| `audit-valid-options` | Accept a complete forward-only design with opaque non-base64 IDs and a scalar edge value | Require base64, both directions, or Node for every edge |
| `audit-schema-only` | Report schema findings separately from unknown runtime behavior | Claim runtime conformance from SDL alone |
| `audit-plural-identifiers` | Identify reordered/omitted results for a supplied plural lookup | Require every server to expose a plural lookup |
| `audit-sound-design` | No violations for the supplied compliant contracts and trace evidence | Invent defects or claim independent execution |
| `negative-rest` | No workflow activation for an unrelated REST route rename | Redesign it as GraphQL |
| `negative-client-style` | No workflow activation for a client-only CSS change | Audit server contracts without relevance |

- [ ] **3. Define grading isolation.** Follow the existing domain-driven-design evaluation protocol. Submit only prompt/context and designated fixture files. Keep expected identities and findings hidden; exclude docs, evaluation files, and the original checkout from runtime access. Record semantics and activation separately; unknown activation stays unknown. Attempt no-plugin baseline for the first and valid-options cases only if an isolated harness is available, recording unavailable runs honestly.
- [ ] **4. Write the references and design example.** Principles routes by decision. Identification covers exact Node/root shape, globally unique opaque identity, refetch availability, within-query field stability, and optional plural lookup correspondence. Connections covers reserved names, edges, cursor serialization, nullable choices, supported argument pairs, filtering then first then last, negative-size errors, zero/empty pages, stable forward/backward order, and direction-dependent flags. Distinguish unmatched cursor algorithm behavior from malformed-cursor application policy; do not invent a mandatory error. Reporting defines evidence, consequences, uncertainty, practical corrections, and proposed versus executed checks. Use an original library catalog SDL/query example; explain auth and ordering policy only as relevant engineering guidance.
- [ ] **5. Author both skills.** Implement the ordered procedures in the spec with selective reference loading. Design outputs SDL, resolver contracts, rationale, verification scenarios, and migration where relevant. Audit separates formal violations, engineering advice, and evidence gaps; includes location, trigger, consequence, and correction. Descriptions select relevant GraphQL server tasks and exclude client-only presentation work. No additional approval ritual is imposed on skill users.
- [ ] **6. Package and register.** Use name `graphql-design`, version `0.1.0`, display name `GraphQL Design`, and author `tacascer`. Adapt time-modeling's supported manifest fields. Document both qualified invocations, scope, source attribution, and unverified live behavior in README. Append `{"name":"graphql-design","path":"plugins/graphql-design"}` to repository inventory, add root README entries, and regenerate catalogs. Add only existing local link targets.
- [ ] **7. Check and commit.** Run shared verification, inspect both generated entries, and statically map each case to the guidance. This mapping is not model evidence. Commit `feat(graphql-design): add Relay design and audit workflows`.

## Task 2: Add behavioral audit fixtures and boundary evaluations

**Create:** `examples/audit-findings.md`,
`evals/fixtures/library-api/README.md`,
`evals/fixtures/library-api/schema.graphql`,
`evals/fixtures/library-api/resolvers.py`.

**Modify:** `evals/cases.json`, `evals/README.md`, package `README.md`, and focused
references only if case review reveals a missing approved requirement.

**Interfaces:** Consumes Task 1's case schema and references. Produces a small,
intentionally flawed stdlib-only resolver fixture for static audit, not a running
GraphQL server. Define `node(object_id, principal)`, `object_id(kind, local_id)`,
and `connection(items, first=None, after=None, last=None, before=None)` as the
stable evidence symbols; items contain `id` and `title`. State this adapter model
in the fixture README. No framework dependency or production service is added.

- [ ] **1. Author these ten additional cases.** `audit-identity-collision` and `audit-backward-order` use explicit invocation; others are implicit. Fixture cases receive only the three fixture files. Use self-contained prose traces for cases whose conditions are not represented in the fixture, avoiding invented line anchors.

| ID | Required outcome | Forbidden outcome |
| --- | --- | --- |
| `audit-identity-collision` | Trace fixture IDs reused across Book and Author to ambiguous refetching | Treat local primary-key uniqueness as global uniqueness |
| `audit-backward-order` | Locate fixture reversal of backward results and propose preserved order | Endorse reversing public edge order |
| `audit-page-flags` | Detect always-false primary-direction flags in fixture; accept permitted opposite-direction false flags | Require exact expensive opposite-direction discovery universally |
| `audit-count-boundaries` | Detect fixture accepting negative slicing; explain valid zero size and empty cursor boundaries | Reject zero or always mark empty pages as having no neighbors |
| `audit-refetch-missing` | Recognize null for an unavailable/deleted object in supplied trace | Require non-null lookup or fabricate a transport error requirement |
| `audit-field-stability` | Detect conflicting fields for the same identity within one query | Claim fields must remain immutable across separate requests |
| `audit-cursor-bounds` | Apply matched cursor bounds exclusively and distinguish a well-formed unmatched cursor from malformed input policy | Invent spec-mandated rejection for every unmatched cursor |
| `audit-combined-slicing` | Explain cursor filtering then first then last; note combination is discouraged | Claim the spec prohibits combining first and last |
| `audit-auth-refetch` | Trace fixture lookup bypassing supplied ownership policy; label security guidance separately | Claim Relay itself defines the application's authorization rules |
| `audit-read-only` | Report fixture corrections without editing supplied files | Apply fixes during an audit-only request |

- [ ] **2. Build the library fixture.** Supply schema with Book and Author implementing Node, library relationship connections, and the required PageInfo shape. Python maps type/local identifiers to local IDs only, looks up objects without enforcing the documented principal policy, reverses backward results, accepts Python negative slicing, and reports constant false flags. Seed enough ordered items to demonstrate each boundary. Document business requirements and the absence of a GraphQL executor without revealing grader expectations.
- [ ] **3. Add the audit example.** Show findings grounded in fixture symbols with reproducing input, consequence, smallest correction, and evidence limits. Explain which errors SDL inspection misses. Keep this worked answer out of evaluation runtime copies as well as fixture inputs; link it from package README. Evaluation runtime copies include only the independent design example.
- [ ] **4. Verify fixture and rubric consistency.** Run `.venv/bin/python -m py_compile plugins/graphql-design/evals/fixtures/library-api/resolvers.py`. Inspect or directly call the functions with the case inputs to confirm the intended defects exist; record these as fixture checks, not live GraphQL tests. Ensure every required finding has supplied evidence and valid cases remain valid.
- [ ] **5. Check and commit.** Run shared verification; confirm 20 unique case IDs and valid fixture paths. Commit `test(graphql-design): add behavioral audit evaluations`.

## Task 3: Evaluate and record delivery evidence

**Create:** `docs/verification/2026-09-30-initial.md`.

**Modify:** package README and only content implicated by evaluation evidence.

**Interfaces:** Consumes the 20 cases and runtime package. Produces a verification
record separating repository checks, native checks, static case review, fixture
execution, live semantic results, and observed activation. Raw transcripts stay
under ignored repository `.eval-runs/`.

- [ ] **1. Inspect available validation and inference tools.** Read the relevant skill-authoring and plugin-creation guidance at implementation time. Use supported disposable/session-only loading; do not install into user configuration. Discover actual native validator interfaces. If isolated inference is unavailable, record the reason and continue unaffected checks.
- [ ] **2. Run isolated evaluations where available.** Expose only manifests, skills, references, the independent design example, and designated fixture copies; exclude `examples/audit-findings.md` because it reveals fixture answers. Execute the 20 cases once per available chosen platform/model; record exact input, time, tool versions/model, transcript location, activation evidence, semantic verdict, and limits. Do not expose hidden rubrics or original repository access. Separate no-plugin baseline from plugin runs; one platform's results do not establish another's.
- [ ] **3. Correct demonstrated defects.** Change only guidance or cases implicated by evidence; retain original failures and rerun affected cases. Mark unexecuted cases unverified rather than passing by inspection. Avoid setup retry loops without a concrete change.
- [ ] **4. Run packaging checks.** Run shared verification and available native validators, including `claude plugin validate --strict plugins/graphql-design` if supported and the discovered Codex validator's actual interface. Record unavailable checks precisely; inspect both marketplace entries and the full branch diff against the approved scope.
- [ ] **5. Record and commit results.** Write the verification record with exact outcomes, link it from README, and rerun shared verification after final edits. Commit `docs(graphql-design): record plugin verification`. Publication, PR creation, and user installation require a separate request.

## Self-review and handoff

The three tasks cover both workflows, all specified contracts, migration and
error behavior, original examples, packaging, and separate validation layers.
The five Review Focus conditions each have a named evaluation case. Fixture
functions are stable evidence anchors, not a new product API. No repository
validator change or prose-mirroring test is planned.

Status: user approved the plan and selected subagent-driven execution on 2026-09-30.
Recommended execution: native, because the three tasks share a small curriculum
and case schema and do not benefit from separate implementer contexts. Native
execution means the current agent implements tasks, followed by an independent
whole-branch review; subagent-driven execution provides per-task implementation
and review at higher coordination cost.

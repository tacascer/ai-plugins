# Rust Patterns Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver practical Rust pattern and library guidance for design and audit, grounded in *Zero to Production in Rust* and useful current alternatives.

**Architecture:** Two short skill entry points route to one shared, selectively loaded reference library. Original examples and isolated scenario evaluations exercise decisions and audit evidence; existing repository tooling validates packaging.

**Tech Stack:** Markdown, JSON manifests and evaluation cases, existing Python/PyYAML validators. Rust snippets and small audit fixtures; no new repository runtime dependencies.

**Spec:** [Approved Rust Patterns design](../specs/2026-09-28-rust-patterns-design.md).

## Global Constraints

- Dedicated worktree: `/home/tacascer/Projects/ai-plugins/.worktrees/rust-patterns`; branch: `feat/rust-patterns`.
- Package: `plugins/rust-patterns/`; initial version: `0.1.0`.
- Skills: `design-rust` and `audit-rust`, equally supported on Codex and Claude.
- Organize content by engineering decision rather than by book chapter or a broad production-readiness checklist.
- Audits are read-only unless the user separately requests changes.
- Respect existing dependencies, runtime, framework, build tools, and explicit architecture constraints.
- Use original condensed prose and examples with attribution; do not bundle the PDF.
- Verify current alternatives against primary sources and distinguish them from book-derived guidance.
- Keep all plugin content inside its package; no platform-specific curriculum copies or mandatory sibling-plugin dependencies.
- No user installation, NixOS changes, application implementation, deployment, or publication in this plan.
- Run all required repository checks before every commit; structural checks do not establish model behavior.

## Review Focus

- Existing sound choices: no preference-driven rewrites or mandatory crate adoption (Task 1: `audit-sound-simple`, `design-existing-stack`).
- Unknown APIs or inaccessible docs: state uncertainty without inventing features or versions (Task 1: `design-unavailable-docs`).
- Cancellation with external effects: distinguish stopping a future from undoing an accepted operation (Task 1: `audit-cancellation`).
- Partial audit access: qualify suspected defects and avoid fabricated runtime evidence (Task 1: `audit-partial-evidence`).
- Bypassed validation: include deserialization and mutation paths, not just a smart constructor (Task 1: `audit-validation-bypass`).

## File map and common verification

Paths below are relative to `plugins/rust-patterns/` unless marked repository-wide.

| Task | Files and responsibility |
| --- | --- |
| 1 | `references/sources.md`; `evals/cases.json`, `evals/README.md`; `evals/fixtures/rust-review/{README.md,types.rs,async_work.rs,http.rs,persistence.rs,telemetry.rs}`: evidence, behavioral contracts, and audit inputs |
| 2 | `references/{index,types,errors,async-state,configuration,persistence,http,observability,authentication,testing,reporting}.md`; `examples/{type-and-error-boundaries,async-and-io-decisions}.md`: compact shared guidance and original examples |
| 3 | `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `skills/design-rust/SKILL.md`, `skills/audit-rust/SKILL.md`, package `README.md`; repository inventory, README, and generated catalogs: public workflows and package integration |
| 4 | `docs/verification/2026-09-28-initial.md`; evidence-driven corrections to earlier files: verification and honest delivery status |

Do not change repository scripts or add prose-matching Python tests. Existing
structural tests cover this unchanged packaging contract. Read applicable
skill-authoring and plugin-creation instructions at execution time, after plan
approval; repository contribution rules override generic installation defaults.

Run from the worktree root before every commit:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

Expected: all 30 existing tests pass, other commands exit zero. Add checks only
if an implementation changes an existing tooling contract. After inventory or
manifest changes, first run `.venv/bin/python -m scripts.catalogs` to regenerate
repository `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json`.
Before registration, the validator may not inspect draft package content;
explicitly review draft JSON, links, and case uniqueness. Stage exact paths and
use conventional commits.

## Task 1: Establish source evidence and behavioral evaluation contracts

**Files:** Create Task 1 files in the file map.

**Interfaces:** Consume the approved spec, supplied PDF, official library
documentation, and existing `plugins/domain-driven-design/evals/` conventions.
Produce source entries with topic, URL, access date, version where relevant,
supported advice, and attribution category. Produce a JSON array of cases with
`id`, `mode`, `invocation`, `prompt`, `context`, `expected_activation`,
`required_findings`, `forbidden_findings`, and optional `fixture_paths`.

- [x] **1. Verify source claims.** Read relevant portions of the supplied book for the nine approved topics. The temporary extraction at `/tmp/zero-to-production.txt` may be reused if present; otherwise fetch the spec's source and extract outside the package. A contents entry establishes topic coverage only. Record verified principles and original synthesis separately in `sources.md`.
- [x] **2. Research meaningful alternatives.** Consult official docs and upstream repositories for the book's library choices and possible alternatives. Initial research candidates: Axum versus Actix Web; SQLx versus Diesel; `config` versus Figment; proptest versus quickcheck; Wiremock for external HTTP. These are research candidates, not predetermined recommendations. Include an alternative only with a concrete decision criterion, current primary evidence, and version caveats; omit irrelevant or unsupported comparisons. Consult current primary authentication guidance before stating password/session advice. Record access limits explicitly.
- [x] **3. Author the following 20 cases before skill prose.** Set `mode` to `design`, `audit`, or `negative`; expected activation is the corresponding `rust-patterns:design-rust`, `rust-patterns:audit-rust`, or empty array. Use explicit invocation for `design-unavailable-docs` and `audit-partial-evidence`; remaining cases exercise implicit selection. Each context must supply enough facts to justify its rubric.

| ID | Required result | Forbidden conclusion |
| --- | --- | --- |
| `design-validated-type` | Choose a boundary type with fallible conversion for a repeated nonempty-identifier invariant | Invent additional business rules |
| `audit-validation-bypass` | Trace a deserialization path that constructs an invalid supposedly validated value | Claim a private field alone enforces all construction paths |
| `design-error-boundaries` | Preserve typed caller decisions and contextual operator diagnostics at appropriate layers | Blanket rule that all errors use one crate/type |
| `design-existing-stack` | Adapt to the supplied Actix/Diesel stack when it meets requirements | Migrate solely to match preferred examples |
| `design-build-tooling` | Use supplied Bazel targets and dependency metadata | Replace the build with Cargo |
| `design-library-alternative` | Explain a meaningful SQL query-interface trade-off, citing primary docs for specific claims | Assert one library is universally best |
| `design-unavailable-docs` | State uncertainty and give pattern-level guidance for unknown versions | Invent APIs, flags, or verification |
| `design-config-validation` | Validate typed config at startup and keep secrets out of diagnostics | Print credentials or assume deserialization proves domain validity |
| `design-integration-testing` | Exercise production composition and owned persistence while controlling external HTTP | Mock all internal collaborators or require a repository trait merely for mocks |
| `audit-blocking-work` | Locate blocking work on an async runtime and explain the scheduling consequence | Claim moving work off-thread automatically bounds concurrency |
| `audit-cancellation` | Explain why a timeout cannot prove a remote side effect was undone | Promise cancellation gives rollback or exactly-once effects |
| `audit-shared-state` | Identify a lock held over external await and justify an appropriate correction | Mandate an async mutex for every shared value |
| `audit-http-client` | Locate per-operation client construction and explain lost reuse in the repeated workload | Fabricate measured latency |
| `audit-transaction` | Trace writes that violate the supplied all-or-nothing contract on failure | Claim an HTTP request is automatically a database transaction |
| `audit-migration` | Explain old-reader/new-schema coexistence for the supplied rolling deployment | Require simultaneous replacement without supporting constraints |
| `audit-telemetry-secrets` | Identify secret capture and suggest narrow field exclusion | Remove all useful request context |
| `audit-auth-work` | Address expensive credential work and secret-safe boundaries using current evidence | Treat historical parameters as verified current defaults |
| `audit-partial-evidence` | Bound findings to visible paths and distinguish uncertainty | Invent file locations, test runs, or unseen defects |
| `audit-sound-simple` | Accept the supplied suitable standard-library implementation | Demand wrappers, traits, or crates without benefit |
| `negative-format-only` | No design/audit activation for a request solely to run the existing formatter | Turn formatting into a pattern audit |

- [x] **4. Build the audit fixture inputs.** Use an original document-processing service scenario. `types.rs` exposes a validated `DocumentName` plus a bypassing derived deserialization path; `async_work.rs` exposes blocking work, a lock across await, and a timeout around an external operation; `http.rs` creates a client per repeated operation; `persistence.rs` writes two records without the required atomic boundary; `telemetry.rs` captures a credential-bearing argument. Use stable symbols cited in hidden rubrics. README supplies requirements, snippet dependency context, and intentional partial-project limits without revealing defects. Route matching cases through `fixture_paths`; other cases can supply self-contained prose or snippets. Do not represent this as a buildable service.
- [x] **5. Define isolated evaluation.** Follow the existing evaluation README: expose only prompt/context and designated fixture copies, keep rubrics hidden, use disposable runtime/configuration, separate observed activation from semantic outcomes, and preserve exact inputs and results. Before skills exist, attempt no-plugin baselines for `design-error-boundaries`, `audit-validation-bypass`, and `audit-sound-simple` if isolated inference is available. Unavailable inference is not a failed baseline.
- [x] **6. Check and commit the evidence contracts.** Parse cases with Python; assert exactly 20 unique IDs and expected identity sets. Verify each required finding follows from supplied evidence and that prompts/fixtures contain no grader instructions. Check each research entry supports its proposed claim. Run common verification; commit `docs(rust-patterns): define sources and evaluation contracts`.

## Task 2: Write the compact pattern reference library

**Files:** Create Task 2 references/examples; extend `references/sources.md` only
for evidence used by this content. Modify cases only to repair evidenced input or
rubric defects, retaining the approved coverage.

**Interfaces:** Consume Task 1 evidence and rubrics. Produce exact reference
paths from the file map, selectively routed by `references/index.md`. Each
pattern entry states problem, applicability, shape, options, trade-offs, pitfalls,
review questions, and a small example only where it clarifies the choice.

- [x] **1. Write types, errors, and configuration references.** Cover all corresponding spec table decisions; explicitly inspect construction through serialization and mutation, distinguish caller decisions from boundary diagnostics, and state when plain values or standard-library mechanisms suffice. Link claims to relevant source notes.
- [x] **2. Write async/state, persistence, and HTTP references.** Cover task ownership, blocking, cancellation, timeouts, synchronization, client/pool reuse, transaction scope, migration compatibility, and handlers/middleware. Explain that cancellation and local transactions do not undo arbitrary remote effects. Include only useful verified alternatives and preserve existing stack choices.
- [x] **3. Write observability, authentication, and testing references.** Preserve secret-safe diagnostics and async span context; discuss established credential/session library boundaries and expensive work; select tests by behavior and dependency ownership. Honor explicit event/listener architecture when present. Do not introduce broad deployment curricula or pretend these references certify security.
- [x] **4. Write the two original example collections.** Use document-processing examples to illustrate validated conversion, typed/opaque error boundaries, shared state, timeouts, transaction scope, and client reuse. Include a suitable simple implementation. Declare dependency context for API-specific snippets; mark incomplete sketches illustrative. Do not reproduce book application code.
- [x] **5. Write routing and reporting contracts.** `index.md` maps each decision to a focused reference; `reporting.md` defines design output (decision, rationale, trade-offs, failure behavior, verification, assumptions) and audit output (priority, location, trigger, consequence, evidence, minimal correction, coverage limits). Reference deep sibling workflows by name only where useful, without required installation or escaping local links.
- [x] **6. Review against cases and commit.** Map all 20 cases to supporting guidance or activation requirements reserved for Task 3. Review current-source/version caveats and remove redundant prose. Check authored local links resolve within the plugin. Run common verification; commit `feat(rust-patterns): add practical pattern and library references`.

## Task 3: Expose and register design and audit workflows

**Files:** Create both manifests, both skills, and package README. Modify
repository `catalogs/plugins.json`, `README.md`, and both generated catalogs.

**Interfaces:** Consume Task 2 routing/reporting paths. Produce
`rust-patterns:design-rust` and `rust-patterns:audit-rust` with the spec's ordered
procedures. Use existing domain-driven-design manifest shapes, author `tacascer`,
repository `https://github.com/tacascer/ai-plugins`, skills path `./skills/`,
display name `Rust Patterns`, and matching version `0.1.0`.

- [x] **1. Write both entry points.** Frontmatter names match their directories; descriptions identify actual design/audit intent rather than all Rust tasks. Inspect local dependencies and build tools before selecting references. Preserve no-change outcomes, uncertainty handling, no implementation from advice-only requests, and absence of new approval rituals.
- [x] **2. Package the public workflows.** Create manifests using supported fields; describe practical pattern/library decisions. README explains purpose, source attribution, independent use, explicit Codex `$rust-patterns:...` and Claude `/rust-patterns:...` invocation, and honest evaluation status. Link only files that exist.
- [x] **3. Integrate the inventory.** Append `{"name":"rust-patterns","path":"plugins/rust-patterns"}`; add the package and invocation guidance to repository README; regenerate both catalogs with the common command. Do not alter unrelated plugin versions or user configuration.
- [x] **4. Verify and commit.** Run common verification now that the registered package is traversed. Inspect both generated entries and all local links. Confirm 20 cases, skill identities, and trigger boundaries. Commit `feat(rust-patterns): register design and audit workflows`.

## Task 4: Evaluate the plugin and record verification limits

**Files:** Create `docs/verification/2026-09-28-initial.md`; update package README
and only guidance/cases implicated by observed defects. Store raw runs under
repository ignored `.eval-runs/`.

**Interfaces:** Consume the completed package and all 20 cases. Produce evidence
for each attempted check: command, tool/version, inputs, observed results, and
limits. Semantic verdicts are `pass`, `fail`, or `unverified`; activation is
recorded independently and remains unknown without decisive invocation evidence.

- [x] **1. Establish available isolated checks.** Inspect native tool availability and actual supported loading interfaces. Use disposable configuration/session loading, never install into the user's configuration. If isolated model evaluation is unavailable, record why and continue structural checks without claiming semantic success.
- [ ] **2. Run the 20 cases on an available isolated harness.** Copy only manifests, skills, references, examples, and each case's designated fixtures into the model-visible workspace. Exclude original checkout, README, docs, evals, and hidden expectations. Record exact prompt, model, platform/version, timestamp, transcript, activation evidence, and semantic verdict. One initial attempt per case/platform; rerun only for a concrete correction, preserving prior results. **Skipped by user direction:** all 20 cases were prepared and statically checked, but both Claude attempts of the same case stopped before inference; the other 19 were not submitted. The user authorized the Anthropic destination and payload, then chose to stop Claude testing after authentication failed. No other provider was substituted; all model outcomes remain unverified.
- [ ] **3. Correct demonstrated defects.** Review failures against source evidence and the spec. Fix implicated guidance or invalid fixtures/rubrics; rerun affected cases. Do not infer success for other platforms or unexecuted cases. **Not exercised:** a static Tokio example defect was corrected, but no semantic run exposed a case defect or supported a rerun; further Claude testing was declined.
- [x] **4. Run final packaging checks.** Run common verification. Where available, run `claude plugin validate --strict plugins/rust-patterns` and the installed Codex validator using its actual interface. Record missing tools rather than substituting Python validation as exhaustive schema validation. Check snippet syntax or compilation only where a complete example and dependency environment support it; label illustrative fragments accurately.
- [x] **5. Record and review delivery.** Write the verification record and link it from README. Separate structural success, static case review, native validation, and model outcomes. Review the complete branch against the spec, source attribution, package containment, and both workflow boundaries. Run common verification after final edits; commit `docs(rust-patterns): record plugin verification`. Leave PR creation and publication to a user request. **Complete locally:** the record is committed; independent whole-branch review found one lifecycle coverage gap, corrected in `dd7abd5` and accepted by scoped re-review. No review findings remain. Live model results are still unverified.

## Self-review and execution handoff

Coverage: all nine topic areas, both workflows, current-alternative research,
original examples, source attribution, independent packaging, registration, and
verification map to explicit tasks. All five Review Focus conditions have named
evaluation cases. Interfaces are shared paths, qualified skill names, and the
existing JSON case schema; no new tooling API is introduced.

Status: implemented locally through the four task commits. Source/contracts,
reference guidance, entry points, registration, verification record, and local
package checks are delivered. Live semantic and automatic-selection evaluation
remains unverified: two Claude attempts loaded the plugin but subscription
authentication stopped inference. The user authorized the Anthropic destination
and plugin/prompt payload; the root-context retry was approved, then failed
before model tokens. The user then chose to stop Claude testing, and no other
provider was substituted. Independent whole-branch review
and the scoped correction review are complete with no outstanding findings.
PR creation and publication remain outside this plan.

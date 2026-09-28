# Rust Patterns plugin design

Date: 2026-09-28

Status: conversational design approved; written spec awaiting user review.

## Intent and success criteria

Create an independently installable `rust-patterns` plugin for Codex and Claude
Code. Help agents design and audit Rust code by selecting commonly useful
patterns and libraries, grounded in Luca Palmieri's *Zero to Production in Rust*
and extended with current alternatives where they offer meaningful trade-offs.

The user selected equally supported design and audit workflows, Rust-specific
guidance adaptable to the project's stack, and concise patterns and library
advice. The user explicitly redirected the original production-service design
toward this practical focus. Organize content by engineering decision rather
than by book chapter or a broad production-readiness checklist.

Success means an agent can choose a proportionate pattern, explain why it fits,
identify relevant library options, and audit concrete misuse without prescribing
unnecessary dependencies or migrations. Existing sound code can receive a
no-change assessment. Guidance must remain useful with different web frameworks,
databases, and build systems, including projects that do not use Cargo as their
primary build command.

## Package and boundaries

All authored content belongs under `plugins/rust-patterns/`. Provide matching
Codex and Claude manifests at initial version `0.1.0`, two shared skills, focused
references, original examples, evaluation cases, and documentation. Register the
completed package in `catalogs/plugins.json`, regenerate both platform catalogs,
and update the collection README.

The plugin provides guidance and review. It does not scaffold applications,
install libraries, implement fixes, configure users' environments, or deploy
services. Audits are read-only unless the user separately requests changes.
Detailed operational guidance belongs here only when it explains a Rust pattern
or library decision. This is not an exhaustive Rust language or unsafe-code guide.

The plugin works independently. Existing testing, observability, time-modeling,
and domain-design plugins may provide deeper guidance when available; they are
not mandatory dependencies. Respect project conventions and explicitly supplied
architecture constraints when illustrating overlapping concerns.

## Workflows

### design-rust

Activate for requests to choose or design Rust patterns, library usage, or code
boundaries. Do not claim every task involving a Rust file.

1. Establish the concrete behavior, constraints, and decision under discussion.
2. Inspect relevant code, dependency versions/features, runtime, and build tools.
3. Read only references applicable to the decision.
4. Compare the simplest adequate option with meaningful alternatives. Include
   standard-library solutions where sufficient.
5. Recommend a pattern and library treatment, explain ownership and data flow,
   identify failure behavior, and suggest verification of the resulting contract.

Output a concise proposal with relevant existing-code anchors, rationale,
trade-offs, a small example when helpful, and unresolved assumptions. Do not
require an architecture document or extra approval ritual for every invocation;
follow the user's surrounding workflow.

### audit-rust

Activate for requests to review existing Rust patterns and library usage.

1. Establish scope and inspect the project's actual dependency and runtime setup.
2. Trace relevant production paths and the tests that exercise their behavior.
3. Evaluate applicability before applying a pattern's review questions.
4. Report concrete findings in priority order: code location, trigger, consequence,
   evidence, and the smallest useful correction.
5. Separate confirmed findings from hypotheses and missing evidence. State
   coverage limits and report no findings when the inspected design is sound.

A different library preference, lack of an abstraction, or difference from the
book's sample application is not by itself a defect. Never imply compilation,
test execution, runtime behavior, or security properties were verified unless
there is corresponding evidence.

## Shared reference structure

Use a short index to route each workflow to focused decision references:

| Topic | Decisions to cover |
| --- | --- |
| Types and boundaries | Validated newtypes, private constructors, `TryFrom`, borrowing and ownership, boundary conversion, avoiding redundant wrappers |
| Errors | Typed recoverable errors, opaque application errors, source chains and context, boundary responses, panic versus recoverable failure |
| Async and state | Task ownership, blocking work, cancellation and timeouts, shared state, synchronization, connection/client reuse |
| Configuration and serialization | Typed configuration, parsing and validation, `serde` boundaries, secret handling |
| Persistence | Query interfaces, pools, transaction scope, migrations and compatibility, compile-time versus runtime checks |
| HTTP | Handlers/extractors, application state, reusable clients, middleware boundaries, status and timeout handling |
| Observability | Structured context, spans across async work, sensitive fields, initialization and reporting ownership |
| Authentication | Credential and session types, established library boundaries, expensive password operations and async runtimes |
| Testing | Production composition, isolated state, real managed dependencies, controlled external services, property-based tests |

Each pattern entry gives the problem, applicability, recommended shape, library
options, trade-offs, common mistakes, review questions, and a small original
example where code clarifies the decision. Explain mechanisms instead of listing
crate names. Keep the skills short and put detailed advice in references.

Book-associated examples include `serde`, `thiserror`, `anyhow`, `tokio`,
`tracing`, `sqlx`, and `reqwest`. These are starting points for research, not
mandatory dependencies. Alternatives such as other HTTP frameworks, persistence
libraries, configuration tools, and test libraries must pass the evidence policy
below before inclusion. Do not create an exhaustive ecosystem catalog.

## Sources and current alternatives

Use the supplied
[PDF](https://github.com/rustaccato/e-books/blob/main/Zero%20to%20Production%20in%20Rust.pdf)
and the [author's site](https://www.zero2prod.com/) as source anchors. The supplied
PDF's contents were inspected during brainstorming; chapter-level reading and
claim verification remain part of content authoring. Do not imply the supplied
edition is the latest edition.

Write original condensed guidance and examples with attribution. Do not bundle
the PDF or reproduce its prose, chapter walkthrough, or newsletter application.
Maintain source notes distinguishing book-derived principles from independently
researched alternatives and engineering synthesis.

For each alternative included, consult official documentation or the maintained
upstream repository, record its source and access date, and explain the concrete
condition under which it is useful. Do not claim universal superiority or
popularity without evidence. Verify version-sensitive APIs and feature flags
against the relevant version; examples must declare their dependency context or
be clearly labeled illustrative. Authentication recommendations also require
current primary guidance rather than treating historical defaults as current.

During skill use, inspect installed dependency versions before giving specific
API advice. Prefer changes compatible with the project's stack. If documentation
is unavailable or a version cannot be established, state the uncertainty and
keep the recommendation at the pattern level rather than inventing an API.

## Examples and evaluation

Provide small original examples that contrast useful patterns with concrete
failure modes. Include cases where a simple existing implementation is adequate.
Examples explain decisions; they are not a runnable application scaffold.

Evaluate both selection and behavior, with model-visible inputs separate from
grader expectations. Cases must cover:

- Correct design/audit selection and unrelated prompts that should not activate.
- Validated types and suitable typed versus opaque error boundaries.
- Blocking work, task lifecycle, and misuse of shared state in async code.
- HTTP client reuse, transaction boundaries, and external failure handling.
- Sensitive data and context handling in telemetry.
- Respect for existing frameworks, libraries, and non-Cargo build tooling.
- Useful current alternatives with evidence and version-aware caveats.
- Missing documentation or incomplete audit evidence.
- Sound code requiring no change; no migration based on preference alone.
- No application edits from a design or audit request alone.

Small audit fixtures must allow findings to be anchored in actual code. Keep
evaluation expectations focused on behavior and reasoning, not exact prose or
preferred crate names. Record model, inputs, observed results, and limits for
any live evaluations performed; otherwise mark them unverified.

## Validation and delivery

Work only in the dedicated `feat/rust-patterns` worktree. Before each commit,
run the required repository checks:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

After adding inventory or manifest metadata, regenerate catalogs with
`.venv/bin/python -m scripts.catalogs` before checking them. Native Codex and
Claude validators are supplemental checks when available. Python structural
validation does not establish exhaustive platform-schema conformance, automatic
selection, or semantic quality.

This commit contains only the written design. After user review and approval of
this spec, invoke the writing-plans skill, produce an implementation plan, and
obtain the required plan review and execution-method selection before creating
the plugin content.

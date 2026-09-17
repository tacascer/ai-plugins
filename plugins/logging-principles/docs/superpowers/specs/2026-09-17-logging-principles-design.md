# Logging Principles plugin design

Date: 2026-09-17
Status: Design approved in conversation; written specification awaiting review.

## Purpose and scope

Create `logging-principles`, a language-neutral guidance plugin for Codex and
Claude Code with `design-logging` and `audit-logging` workflows. Help agents make
justified diagnostic decisions and identify actionable problems in existing code.
Provide instructions, shared references, original examples, and evaluation cases.
Runtime instrumentation, service integrations, hooks, installation, publication,
and user configuration are outside this contribution.

## Source and interpretation

The primary source is sobolevn's
[Do not log](https://sobolevn.me/2020/03/do-not-log), published March 11, 2020.
Link and attribute it without reproducing its prose, code, or screenshots. State
that the plugin is not affiliated with or endorsed by the author.

Source-derived principles:

- Prevent invalid states where practical; represent expected failures explicitly.
- Match important failures to error reporting and business outcomes to monitoring.
- Treat logging as a fallible side effect and a maintained infrastructure subsystem.
- Retained logs need structured context, consistent severity and formatting,
  useful state history, and careful handling of sensitive information.
- Preserve justified logging, including on-premise diagnosis and startup failures.
  The article challenges habitual overlogging, not every use of logs.

The workflow structure, reporting format, evaluation methodology, and safeguards
below are plugin design choices. Label these separately from the author's views.
Do not turn the article's illustrative libraries into mandatory dependencies or
its programming style into a requirement to introduce monads in every language.
Keep source synthesis concise; examples and procedures must be original.

## Package architecture

All plugin-owned content belongs under `plugins/logging-principles/`:

```text
.codex-plugin/plugin.json
.claude-plugin/plugin.json
README.md
skills/design-logging/SKILL.md
skills/audit-logging/SKILL.md
references/principles.md
references/reporting.md
references/sources.md
examples/logging-decisions.md
evals/README.md
evals/cases.json
docs/superpowers/specs/2026-09-17-logging-principles-design.md
docs/verification/2026-09-17-initial.md
```

Both manifests use `logging-principles`, version `0.1.0`, and a nonempty
consistent description. Skills link to the same shared references; no copies of
curriculum are maintained per platform. Principles owns the decision procedure;
reporting owns evidence and output conventions; sources owns attribution and
boundaries between source material and extensions. Examples illustrate these
rules without defining competing ones.

Register the plugin in `catalogs/plugins.json`, regenerate both platform catalogs,
and add its entry to the repository README. Leave other plugins untouched.
The specification stays plugin-local to satisfy repository containment rules.

## Design workflow

`design-logging` applies when designing or changing application logging,
failure reporting, or related diagnostic choices. It is not a general-purpose
observability platform design workflow.

1. Inspect relevant requirements, code paths, failure handling, diagnostic
   facilities, deployment constraints, and repository conventions.
2. Identify the operational question, signal consumer, expected response, and
   failure significance. Trace the proposed signal from its origin to its
   consumer before recommending a mechanism.
3. Choose a proportionate mechanism using the shared principles. Explain why it
   meets the need and what information the consumer requires.
4. For retained logging, specify event purpose, structured fields, severity,
   emission boundary, sensitive-data exclusions, and relevant delivery failures.
   Address ownership and operating costs when infrastructure changes are proposed.
5. Report the concrete recommendation, rationale, verification scenarios, and
   unresolved assumptions. Ask only for missing decisions that affect the result.

Use the project's existing tools and language conventions when suitable.
Do not require a vendor, a new infrastructure stack, or a rewrite to implement
functional abstractions. The workflow does not authorize changes beyond the
user's request or override applicable implementation processes.

## Audit workflow

`audit-logging` applies to reviews and investigations of existing logging and
related failure-reporting behavior. It remains read-only unless edits are requested.

1. Trace representative log sites through callers, failure handling, configuration,
   and consumers. Inspect available operational requirements and tests.
2. Assess whether each signal serves a demonstrated need and whether its context,
   severity, emission placement, and handling are suitable for that need.
3. Report prioritized findings with file and line evidence, a concrete trigger,
   consequence, and proportionate correction. Separately identify justified logs
   that should remain when their removal is a plausible mistaken recommendation.
4. Distinguish confirmed defects, conditional concerns, and missing evidence.
   State the examined scope and say when no material issue is established.

A logger call alone is not evidence of a defect. Before recommending removal,
verify that the proposed alternative covers the diagnostic need and deployment
constraints. Do not infer monitoring coverage from a library dependency alone.

## Shared safeguards and reporting

These practical safeguards are plugin extensions:

- Never convert a caught failure into silent success while reducing logging.
  Preserve propagation, recovery, retry, or explicit result semantics.
- Do not remove required audit records as diagnostic noise. If their purpose is
  unclear, identify that uncertainty before recommending a change.
- Minimize sensitive context in error reporting as well as logs. Do not recommend
  indiscriminate local-variable capture or claim legal compliance from a checklist.
- Discuss logging failures according to the application's actual contract; do
  not impose universal fail-open or fail-closed behavior.
- A replacement signal must be usable in the relevant environment, including
  startup and disconnected deployments. Missing evidence remains explicit.

Reports distinguish inspected facts, recommendations, assumptions, and checks
actually executed. Keep output proportional to the task. Skill descriptions
support selection for their specific workflows; incidental uses of words such as
log, monitoring, or error do not establish relevance. Explicit invocation uses
`logging-principles:design-logging` or `logging-principles:audit-logging` with the
platform's normal syntax.

## Examples and behavioral evaluation

Create original contrasting examples with a diagnostic need, code or deployment
context, and a justified decision. Use the existing repository evaluation format;
no new general-purpose runner is required.

Evaluation cases must cover:

- Catch-and-log handling that hides an important failure.
- Expected failures with explicit recovery or result handling.
- Business malfunction without an exception.
- Unnecessary logging in otherwise pure computation.
- Retained structured diagnostics with useful context and consistent severity.
- Sensitive data in both logs and proposed error-reporting replacements.
- Startup failure and disconnected on-premise diagnosis where logs must remain.
- Required audit records that must not be removed as noise.
- Missing information about consumers or monitoring coverage.
- An unrelated request that should activate neither workflow.

Include both workflows, implicit selection, and explicit invocation. Separate
model-visible prompts and context from grader-only workflow identities, required
behaviors, and forbidden recommendations. Grade meaning rather than exact prose.
Record activation and semantic correctness separately. Keep raw transcripts in
ignored `.eval-runs/`; mark unexecuted or unobservable behavior unverified.

## Validation and acceptance

The implementation is ready for review when manifests, skills, references,
examples, evaluation cases, and README agree on scope and identity; local links
resolve within the plugin; catalogs match inventory; and evaluation expectations
cover both harmful overlogging and harmful removal of useful signals.

After inventory or manifest changes, regenerate catalogs:

```bash
.venv/bin/python -m scripts.catalogs
```

Before committing, run the required repository checks:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

Record results and limitations in plugin-local verification documentation.
Native platform validators are supplemental. The repository Python validator
checks supported structure, not exhaustive platform schemas or model behavior.
Documentation-only specification checks do not establish plugin readiness.

## Delivery and review gates

Use the existing isolated worktree on `codex/logging-principles`. Commit this
specification using a conventional documentation commit after required checks.
Review the document for placeholders, contradictions, ambiguous requirements,
and scope drift. Request review of the written specification before invoking
`writing-plans`; implementation follows the approved specification and plan.

# Logging Principles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver the approved logging-principles plugin with two workflows, shared guidance, original examples, behavioral evaluations, and both marketplace registrations.

**Architecture:** Codex and Claude manifests expose the same skills directory. Design and audit skills consume shared principles and reporting conventions. The package contains authored guidance only; existing repository tools validate packaging and generate catalogs.

**Tech Stack:** Markdown with YAML skill frontmatter, JSON manifests and evaluation cases, existing Python unittest/catalog/validation tooling with PyYAML.

**Spec:** [Approved design](../specs/2026-09-17-logging-principles-design.md).

## Global Constraints

- Both manifests use `logging-principles`, version `0.1.0`, and a nonempty consistent description.
- All plugin-owned content belongs under `plugins/logging-principles/`.
- No copies of curriculum are maintained per platform.
- Runtime instrumentation, service integrations, hooks, installation, publication, and user configuration are outside this contribution.
- Use the existing repository evaluation format; no new general-purpose runner is required.
- Native platform validators are supplemental.
- The repository Python validator checks supported structure, not exhaustive platform schemas or model behavior.
- Use the existing isolated worktree on `codex/logging-principles`.
- Audit remains read-only unless edits are requested.
- Attribute the article; author original guidance and examples without reproducing its prose, code, or screenshots.

## File responsibilities

Paths below are relative to `plugins/logging-principles/` unless explicitly rooted at the repository.

| Files | Responsibility |
| --- | --- |
| `references/principles.md` | Shared diagnostic decision procedure and safeguards |
| `references/reporting.md` | Design/audit output and evidence conventions |
| `references/sources.md` | Attribution and separation of source arguments from extensions |
| `examples/logging-decisions.md` | Original contrasting worked decisions |
| `evals/cases.json`, `evals/README.md` | Behavioral oracles and isolated evaluation procedure |
| `skills/design-logging/SKILL.md` | Design activation and procedure |
| `skills/audit-logging/SKILL.md` | Audit activation and procedure |
| `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json` | Platform metadata over shared skills |
| `README.md` | Scope, invocation, resources, and verification status |
| `docs/verification/2026-09-17-initial.md` | Executed checks and limitations |
| Repository `catalogs/plugins.json` | New package inventory entry |
| Repository `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json` | Generated catalogs; confirm renderer paths before staging |
| Repository `README.md` | Package overview and invocation examples |

## Task 1: Deliver shared guidance and behavioral oracles

**Interfaces:** Consumes the approved specification. Produces shared reference paths used by both skills and an evaluation array using `id`, `mode`, `invocation`, `prompt`, `context`, `expected_activation`, `required_findings`, and `forbidden_findings`.

**Files:** Create the three references, examples file, and two evaluation files listed above.

- [x] **Step 1: Read authoring and evaluation conventions.**

Read applicable skill-authoring guidance before authoring skills or evaluation cases. Inspect `plugins/time-modeling/evals/cases.json` and its evaluation guide for the existing field contract and isolation method. Do not change repository tooling or add tests that assert prose wording.

- [x] **Step 2: Write 15 behavioral cases before authoring the guidance.**

Create one case per row below. Modes map to `logging-principles:design-logging` and `logging-principles:audit-logging`; `none` maps to an empty activation array. Only the two missing-consumer cases use explicit invocation. All other cases use implicit prompts. Use the stated context as model input; keep required and forbidden conclusions exclusively in grader fields.

| ID | Mode | Model-visible scenario | Required conclusion | Forbidden conclusion |
| --- | --- | --- | --- | --- |
| `design-important-failure` | design | Payment capture fails; caller must learn it failed; proposal catches, logs, and returns success | Preserve failed outcome and actionable error reporting | Catch, log, and return success |
| `audit-important-failure` | audit | Capture code catches an error, logs it, and returns success | Identify hidden failure and correct the return/propagation contract | Merely remove the log and keep success |
| `design-expected-failure` | design | Optional cache lookup returns a miss; caller falls back correctly | Preserve explicit miss and fallback; no mandatory alert per miss | Treat every miss as critical |
| `audit-expected-failure` | audit | Correct cache fallback emits an error for every normal miss | Identify severity/noise mismatch while preserving fallback | Remove fallback or claim all failures can be ignored |
| `design-business-signal` | design | Checkout rejects valid carts without exceptions; operators need detection | Monitor the business outcome and define actionable response | Exception reporting alone detects the condition |
| `audit-pure-computation` | audit | Deterministic price calculation logs each intermediate value; no consumer is identified | Explain side-effect costs and establish need before retaining diagnostics | Mandate a monadic rewrite |
| `design-retained-context` | design | Support needs to reconstruct a failed import using job ID and stage history; no payload data is needed | Propose structured, minimal, purposeful context and severity | Dump full payloads or ban all logs |
| `audit-justified-logs` | audit | Rotated structured import logs record job ID and stage, have documented severity, and are used by support | Recognize useful diagnostics; no defect from logging alone | Demand removal without another usable signal |
| `audit-sensitive-logs` | audit | Error log contains passwords and raw request bodies | Remove sensitive context while preserving diagnostic value | Copy the payload into an error tracker |
| `design-sensitive-reporting` | design | Proposed error tracker captures all locals including credentials | Minimize and filter context in the tracker too | Claim legal compliance from filtering alone |
| `audit-startup` | audit | Configuration fails before remote telemetry initializes; stderr is the only diagnostic | Preserve a startup diagnostic path | Replace stderr solely with unavailable telemetry |
| `design-disconnected` | design | On-premise system is offline; support receives local diagnostic bundles | Retain usable local diagnostics with bounded operating needs | Require an always-online vendor |
| `audit-required-records` | audit | Required access audit records share a logging transport with debug diagnostics | Preserve required records and distinguish their purpose | Delete required records as overlogging |
| `design-missing-consumer` | design | User explicitly invokes design-logging; desired diagnostic consumers and current telemetry coverage are unknown | State uncertainty and ask for the decision that changes the recommendation | Invent monitoring coverage or prescribe universal removal |
| `audit-missing-consumer` | audit | User explicitly invokes audit-logging; log sites exist but consumers are undocumented | Separate missing evidence from proven uselessness | Equate undocumented consumers with no consumers |

Add a sixteenth case, `unrelated-release-notes`, mode `none`, implicit invocation: the user asks to shorten release notes containing the phrase “logging improvement.” Require a concise prose edit and forbid an unsolicited logging audit.

Every case forbids claiming checks were run without evidence. Require nonempty prompt/context strings and nonempty grader lists. Do not require fabricated file references when cases supply only abstract context.

- [x] **Step 3: Write the shared principles reference.**

Use the specification's source-derived principles as a concise attributed synthesis. Add an original decision table with columns: operational need, existing mechanism, proposed signal, consumer/action, and evidence still needed. Cover expected failures, important failures, business outcomes, justified logs, and unknown requirements. Explain signal flow from emission to consumer, costs of fallible side effects and infrastructure, structured fields and severity consistency, and useful state history. Separate practical extensions: preserve failure semantics, required audit records, context minimization in all destinations, environment coverage, and application-specific handling of diagnostic failures. Do not prescribe vendors, monads, or universal fail-open/fail-closed behavior.

- [x] **Step 4: Write reporting, attribution, and original examples.**

Reporting provides these compact templates:

```text
Design: operational need; consumer/action; chosen mechanism and rationale;
retained event fields/severity/boundary; failure behavior; proposed checks;
assumptions and unresolved decisions.
Audit: prioritized finding; concrete trigger and consequence; file/line evidence;
proportionate correction; confidence; retained useful logs; examined scope.
```

Sources links `https://sobolevn.me/2020/03/do-not-log`, names the author and publication date, identifies the source-derived topics, and explicitly labels workflow/evaluation design and safeguards as extensions. State non-affiliation. Examples contrast hidden payment failure, optional cache miss, silent checkout malfunction, useful import history, startup/disconnected diagnostics, and sensitive-data handling. Each gives the need, decision, and reason an attractive alternative fails. Examples are authored scenarios, not claims of executed tests.

- [x] **Step 5: Write evaluation instructions and review the oracle coverage.**

Submit only `prompt` and `context` in fresh disposable workspaces under ignored `.eval-runs/`. Expose a runtime copy of manifests, skills, references, and examples; exclude `evals/`, `docs/`, the README, and the original checkout. Translate explicit names to `$` forms in Codex and `/` forms in Claude. Keep grader expectations inaccessible. Record exact submission, platform/version/model, timestamp, transcript path, activation telemetry, expected-set match, semantic verdict, and unavailable checks. Grade semantics independently from activation; use `unknown` for insufficient activation telemetry and `unverified` for unavailable inference. Optional baselines omit unavailable explicit invocation and document the difference. Review all 16 cases against the guidance without calling author review a model test.

## Task 2: Deliver workflows, manifests, and registration

**Interfaces:** Skills consume `../../references/principles.md`, `../../references/reporting.md`, and `../../examples/logging-decisions.md`. Both manifests expose `./skills/`. Catalog generation consumes repository inventory plus manifests.

**Files:** Create the two skill files, two manifests, and plugin README. Modify repository inventory, generated catalogs, and repository README.

- [x] **Step 1: Read applicable plugin-creator and skill-authoring instructions.**

Follow repository packaging conventions over personal marketplace defaults. Do not install, publish, or edit user configuration. Use skill-authoring evaluation procedures only with grader isolation and truthful reporting of unavailable model runs.

- [x] **Step 2: Write precise skill frontmatter and procedures.**

```yaml
---
name: design-logging
description: Use when designing or changing application logging, failure reporting, or diagnostic signals and choosing how operational needs should be observed.
---
```

```yaml
---
name: audit-logging
description: Use when reviewing or investigating existing logging and failure-reporting behavior, including unnecessary logs, missing diagnostic context, and unsafe signal removal.
---
```

Design follows the spec's five steps: inspect context, identify question/consumer/action, choose the mechanism, specify retained logging, and report checks and uncertainty. Audit follows its four steps: trace sites through consumers, assess purpose and placement, report evidenced corrections and useful logs, then separate confirmed issues from missing evidence. Both link shared rules instead of duplicating them. Preserve read-only audit behavior and existing implementation authorization boundaries. Exclude incidental log mentions and general observability-platform architecture from activation scope.

- [x] **Step 3: Create both manifests using this common metadata.**

```json
{
  "name": "logging-principles",
  "version": "0.1.0",
  "description": "Design and audit purposeful logging and failure reporting.",
  "author": {"name": "tacascer"},
  "repository": "https://github.com/tacascer/ai-plugins",
  "skills": "./skills/"
}
```

Add this interface object only to the Codex manifest:

```json
{
  "displayName": "Logging Principles",
  "shortDescription": "Design and audit purposeful logging.",
  "longDescription": "Language-neutral guidance for choosing diagnostic signals and reviewing logging while preserving useful operational evidence.",
  "developerName": "tacascer",
  "category": "Productivity",
  "capabilities": ["Interactive"],
  "defaultPrompt": ["Audit my logging for unnecessary noise and missing diagnostic value."]
}
```

- [x] **Step 4: Write README and register the package.**

README includes scope, source attribution/non-affiliation, both workflows, read-only audit behavior, shared resource links, and verification status. Show `$logging-principles:design-logging` and `$logging-principles:audit-logging` for Codex and the corresponding `/` forms for Claude. Refer to collection installation documentation in prose, respecting plugin-local link containment. Add the package to the repository README overview and invocation examples. Append this inventory entry without changing existing entries:

```json
{"name": "logging-principles", "path": "plugins/logging-principles"}
```

- [x] **Step 5: Regenerate catalogs and inspect generated additions.**

```bash
.venv/bin/python -m scripts.catalogs
```

Confirm renderer output paths from `scripts/catalogs.py`. Both catalog diffs must add only the new package; existing packages remain unchanged.

## Task 3: Verify and commit the complete plugin

**Interfaces:** Consumes all authored content and registration. Produces plugin-local verification evidence and a conventional commit. No runtime code or new repository test framework is introduced.

**Files:** Create `docs/verification/2026-09-17-initial.md`; update this plan's checkboxes as work completes.

- [x] **Step 1: Validate the evaluation artifact.**

```bash
.venv/bin/python - <<'PY'
import json
from collections import Counter
from pathlib import Path
cases = json.loads(Path('plugins/logging-principles/evals/cases.json').read_text())
assert len(cases) == 16
assert len({case['id'] for case in cases}) == 16
assert Counter(c['mode'] for c in cases) == {'design': 7, 'audit': 8, 'none': 1}
assert Counter(c['invocation'] for c in cases) == {'implicit': 14, 'explicit': 2}
for case in cases:
    for key in ('prompt', 'context'):
        assert isinstance(case[key], str) and case[key].strip()
    for key in ('required_findings', 'forbidden_findings'):
        assert case[key] and all(isinstance(x, str) and x.strip() for x in case[key])
    expected = [] if case['mode'] == 'none' else [f"logging-principles:{case['mode']}-logging"]
    assert case['expected_activation'] == expected
print('16 evaluation cases: consistent fields and workflow identities')
PY
```

This checks artifact consistency, not skill behavior.

- [x] **Step 2: Collect available platform and model evidence.**

Discover installed tooling and record versions. Use available native validators as supplemental checks. Attempt fresh isolated behavioral runs when supported without installation or user configuration changes. Preserve grader isolation, record activation separately from semantics, and retain failures. If loading, authentication, or model execution is unavailable, record the exact limitation and mark behavior unverified. Do not claim semantic red/green results from structural tests.

- [x] **Step 3: Write verification evidence and review the diff.**

Record executed commands, tool versions, outcomes, and unavailable checks. Link the record from README and evaluation guide. Review all spec requirements, both workflow scopes, attribution boundaries, retained diagnostics, privacy safeguards, examples, and hidden oracles. Confirm no unrelated package or tooling edits. Update this plan's completed checkboxes; do not mark unavailable behavioral checks as passed.

- [x] **Step 4: Run required checks on the complete package.**

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
git diff --check
```

Require zero exit codes before commit. The existing baseline has 30 tests. Registered-plugin validation checks authored local links and metadata but does not establish runtime behavior. Resolve failures, then rerun affected checks; do not broaden testing without a concrete reason.

- [x] **Step 5: Stage scoped files and commit.**

Stage `plugins/logging-principles/`, repository `README.md`, `catalogs/plugins.json`, and the exact generated catalog paths confirmed in Task 2. Inspect the staged diff and ensure it includes no unrelated edits.

```bash
git diff --cached --check
git diff --cached --stat
git commit -m 'feat: add logging-principles plugin'
git status --short --branch
```

Report the commit, both workflows, checks, and material verification limits. Do not merge, publish, or install.

## Plan self-review

Task 1 covers source boundaries, shared rules, original examples, reporting, and
all specified behavioral scenarios. Task 2 covers both workflows, platform
manifests, inventory/catalog registration, and collection documentation. Task 3
covers evidence, structural checks, review, and delivery. Shared paths and
workflow identities agree across tasks. The 16 cases contain seven design,
eight audit, and one negative-selection case. No runtime-code tests or tooling
changes are required for this guidance package.

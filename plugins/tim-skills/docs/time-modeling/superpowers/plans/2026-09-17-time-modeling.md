# Time Modeling Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Deliver the approved time-modeling plugin with two shared workflows, original guidance, behavioral evaluation cases, and registration in both repository catalogs.

**Architecture:** Both platform manifests expose the same skill directory. Two task-specific skills consume a shared principles reference and reporting conventions. Plugin-owned examples and evaluations document expected reasoning without adding a runtime service or changing repository tooling.

**Tech Stack:** Markdown and YAML frontmatter, JSON manifests and evaluation cases, existing Python unittest/catalog/validation tooling with PyYAML.

**Spec:** [Approved design](../specs/2026-09-16-time-modeling-design.md).

## Global Constraints

- Both manifests use the name `time-modeling`, initial version `0.1.0`, and a nonempty description.
- Shared skills and references are not copied per platform.
- Keep all plugin-owned material under `plugins/time-modeling/`.
- Installation, publication, and user configuration changes are outside this contribution.
- No new general-purpose evaluation runner is required.
- Native validators are supplemental; repository Python validation is not exhaustive platform-schema validation.
- Work in the dedicated worktree on `codex/time-modeling`.
- Do not modify unrelated plugin content or introduce platform-specific configuration.

## Execution context

Run commands from `/home/tacascer/Projects/ai-plugins/.worktrees/time-modeling`.
The worktree already contains `.venv/bin/python` and the declared PyYAML dependency.
Read AGENTS.md, CONTRIBUTING.md, and the approved spec before executing.
The main checkout must remain unchanged.

The spec has an existing unstaged editorial insertion, `Please review the spec`,
before the recent-past bullet. Preserve that user edit; it does not alter the
approved technical requirement. Stage implementation files explicitly rather
than including the spec unintentionally.

This is an authored-content package, not a runtime-code change. Use semantic
cases to assess the instructions and the existing repository checks to assess
packaging. Do not add tests that merely assert prose contains particular words.
Structural success does not establish model behavior.

## File responsibilities

All paths below are repository-relative unless explicitly stated otherwise.

| File | Responsibility |
| --- | --- |
| `plugins/time-modeling/evals/cases.json` | Model inputs and separate grader expectations |
| `plugins/time-modeling/evals/README.md` | Safe case submission, grading, evidence records |
| `plugins/time-modeling/references/principles.md` | Single shared rule set and decision procedure |
| `plugins/time-modeling/references/reporting.md` | Evidence, uncertainty, design/audit output formats |
| `plugins/time-modeling/references/sources.md` | Attribution and section-to-rule mapping |
| `plugins/time-modeling/examples/time-models.md` | Original contrasting decisions and outcomes |
| `plugins/time-modeling/skills/design-time-models/SKILL.md` | Design workflow and activation description |
| `plugins/time-modeling/skills/audit-time-models/SKILL.md` | Audit workflow and activation description |
| `plugins/time-modeling/.codex-plugin/plugin.json` | Codex discovery metadata |
| `plugins/time-modeling/.claude-plugin/plugin.json` | Claude discovery metadata |
| `plugins/time-modeling/README.md` | User-facing scope, invocation, resource map, verification limits |
| `plugins/time-modeling/docs/verification/2026-09-17-initial.md` | Actual commands, outcomes, and unavailable checks |
| `catalogs/plugins.json` | Add plugin inventory entry after the existing entry |
| `.agents/plugins/marketplace.json` | Generated Codex catalog |
| `.claude-plugin/marketplace.json` | Generated Claude catalog |
| `README.md` | Add this plugin to collection overview and workflow guidance |

## Task 1: Define behavioral cases and shared curriculum

**Interfaces:** Consumes the approved spec and primary source. Produces the
principles/reporting/sources/example documents consumed by both skills, plus the
semantic oracle used during final review. No runtime interface is introduced.

- [x] **Step 1: Read the source and label provenance.**

Use the article linked in the spec. Map rules to its sections: Interlude:
requirements; Option 3; Principle of preserving supplied data; Representation vs
information; A possible option 4; Ambiguous and skipped times; Recurrent events;
Time zone boundary changes and splits; Past vs recent past; Conclusion. Separate
our workflow/reporting choices from the source's reasoning. Do not copy article
code or treat its hypothetical policy scenario as history. Write an original,
concise synthesis with attribution, respecting the source's reproduction limits.

- [x] **Step 2: Author the evaluation cases before the skills.**

Use the existing case-object interface:

```json
{
  "id": "audit-recorded-instant",
  "mode": "audit",
  "invocation": "implicit",
  "prompt": "Review how this service stores its event timestamps.",
  "context": "The server obtains an instant directly from its clock when a job finishes and stores it in UTC. Only elapsed durations and chronological ordering are required. No user-entered local date/time is converted.",
  "expected_activation": ["time-modeling:audit-time-models"],
  "required_findings": ["UTC fits the recorded-instant requirement", "No defect is established by the absence of a local time or zone"],
  "forbidden_findings": ["Every timestamp requires local time and a zone", "The implementation was executed and verified"]
}
```

Create the following 16 cases. The first six rows each yield an independent
design case and audit case using the same scenario. Design prompts ask for the
model and policy; audit prompts ask for review of the stated implementation.
Every case needs concrete context, required findings, and forbidden findings.

| Case stem | Concrete scenario | Required reasoning | Forbidden conclusion |
| --- | --- | --- | --- |
| `recorded-instant` | Server records a job-completion instant; ordering and elapsed time are the only requirements | Recognize valid UTC storage | Require local fields universally |
| `local-commitment` | Appointment promises 09:00 in an organizer-selected named zone; only its initial UTC conversion is retained | Preserve intended input and explain information loss | Treat UTC alone as sufficient |
| `rule-update` | Synthetic rules change a future appointment's offset from +02:00 to +01:00; local start is 09:00 and cached UTC is 07:00Z | Derive 08:00Z while retaining 09:00; refresh dependent scheduling data | Rewrite local start to 08:00 or require old rules when source local fields remain |
| `gap-overlap` | Synthetic transition maps a selected local value to zero or two instants; later rules can change the mapping | Specify a deliberate policy and revalidate on updates | Assume one instant or silently prescribe a universal lenient policy |
| `recurrence` | Weekly 09:00 meeting anchored to a named zone; attendees span zones | Resolve each occurrence from the coordinating zone | Add a fixed UTC duration as an unconditional solution |
| `missing-requirements` | Field `starts_at` contains UTC; no product requirement or conversion path is supplied | Present conditional alternatives and identify the missing invariant | Invent a confirmed defect or platform behavior |
| `audit-offset-only` | Appointment stores 09:00+02:00 without a zone; future rule changes matter | Offset alone does not identify applicable future rules | Treat offset as zone identity |
| `design-location-intent` | An appointment must follow venue-local time; location-to-zone assignment can change | Preserve the location that defines intent and consider reassignment | Require a geographic service for every temporal model |
| `audit-recent-past` | Yesterday's local event was converted with stale rules and its input discarded | Recognize lost source information and uncertainty | Past values are necessarily correct |
| `unrelated-release-notes` | User requests prose release notes; context contains a UTC timestamp | No time-modeling activation expected | Start an unsolicited temporal audit |

Use `expected_activation: []` and `mode: "none"` for the unrelated case.
Use `mode: "design"` or `"audit"` otherwise. Make both missing-requirements
cases explicit, naming the intended workflow in their prompt; all other cases
are implicit. Document translating explicit names to each platform's syntax.
Use synthetic transitions to avoid dependence on currently installed tzdb rules.

- [x] **Step 3: Author evaluation instructions.**

In `evals/README.md`, instruct evaluators to send only `prompt` and `context` to
the model. Keep activation expectations and semantic findings in the grader.
Record case ID, platform/version/model, timestamp, exact submitted prompt,
transcript location, observed workflow identities, activation evidence, semantic
verdict, and unavailable checks. Activation is `yes`, `no`, or `unknown` from
telemetry, independent of expected-set matching. Semantic verdict is `pass`,
`fail`, or `unverified`; explain unknown/unverified outcomes. Keep transcripts
under ignored `.eval-runs/`. A manual record format suffices; do not add a runner
or new schema dependency.

- [x] **Step 4: Author references and original examples.**

`principles.md` implements the approved rule set, using a decision table for
source meaning, required invariant, derived data, and change behavior. Make
optional fields and conditional recommendations explicit. Separate natural
instants, local commitments, and cases with insufficient requirements.

`reporting.md` defines two short result templates:

```text
Design: intended invariant; source/derived fields; conversion/update flow;
applicable policies; proposed checks; assumptions and unresolved decisions.
Audit: finding and consequence; concrete trigger; file/line evidence;
proportionate correction; confidence and missing evidence.
```

`sources.md` maps the rule topics to article sections using HTTPS links and
identifies workflow structure and evaluation conventions as plugin design.
`examples/time-models.md` contrasts a job-completion timestamp, an appointment
under synthetic rule changes, a gap/overlap choice, recurrence, and insufficient
requirements. Give expected outcomes without claiming execution.

- [x] **Step 5: Review content against the 16 independent oracles.**

Check that the rules allow both valid UTC and local-time cases, preserve
uncertainty, and cover every spec topic. Check local links against actual files.
Review cases for accidental disclosure of expectations in prompts and for
unsupported requirements. Do not count this author review as a model evaluation.

## Task 2: Deliver both workflows and package registration

**Interfaces:** Both skills consume `../../references/principles.md`,
`../../references/reporting.md`, and optionally
`../../examples/time-models.md`. Both manifests expose `./skills/`.
Catalog generation consumes the plugin entry and manifests without tooling edits.

- [x] **Step 1: Read applicable authoring instructions.**

Apply the available plugin-creator and skill-authoring skills before writing the
manifests and skill files. Repository/user instructions override personal
marketplace installation defaults: register only in this repository's inventory.
No installs, publication, or user configuration changes are authorized.

- [x] **Step 2: Write the two skills with precise activation frontmatter.**

```yaml
---
name: design-time-models
description: Use when designing or changing temporal storage, scheduling models, time conversions, or behavior after time-zone rule updates.
---
```

```yaml
---
name: audit-time-models
description: Use when reviewing or investigating existing date/time storage, scheduling, time-zone conversions, or failures caused by changing time-zone rules.
---
```

The design procedure follows the spec's four steps: inspect context and intent,
read shared rules, propose the model and update/error behavior, then state
validation and unresolved decisions. The audit procedure traces the actual data
flow, compares requirements, reports evidenced findings and corrections, and
separates confirmed from conditional conclusions. Link shared guidance instead
of repeating it. Audit stays read-only unless changes are separately authorized.
Both workflows follow repository conventions and report unexecuted checks as such.

- [x] **Step 3: Write manifests and README.**

Use this common metadata for both manifests:

```json
{
  "name": "time-modeling",
  "version": "0.1.0",
  "description": "Design and audit temporal data models while preserving time intent.",
  "author": {"name": "tacascer"},
  "repository": "https://github.com/tacascer/ai-plugins",
  "skills": "./skills/"
}
```

For Codex, follow the existing interface shape with `displayName: "Time Modeling"`,
`shortDescription: "Design and audit temporal data models."`, a nonempty
`longDescription`, `developerName: "tacascer"`, `category: "Productivity"`,
`capabilities: ["Interactive"]`, and
`defaultPrompt: ["Audit my date/time model for lost intent and rule-change risks."]`.

README explains the two workflows, supported invocation forms, shared resources,
attribution/non-affiliation, scope, and actual verification status. Explicit forms
are `$time-modeling:design-time-models` and `$time-modeling:audit-time-models`
for Codex, and `/time-modeling:design-time-models` and
`/time-modeling:audit-time-models` for Claude. Link only inside this plugin or to
HTTPS sources. Refer to collection installation documentation in prose.

- [x] **Step 4: Register the package and update collection documentation.**

Append this object without altering the existing entry:

```json
{"name": "time-modeling", "path": "plugins/time-modeling"}
```

Update the collection README overview and add the plugin's two workflows to its
usage guidance. Preserve existing installation/publication caveats. Generate
catalogs with:

```bash
.venv/bin/python -m scripts.catalogs
```

Inspect both generated diffs: only `time-modeling` should be added.

## Task 3: Verify, review, and commit the complete plugin

**Interfaces:** Consumes all authored files and the catalog registration. Produces
verification evidence and a scoped conventional commit. No additional runtime or
repository tooling is introduced.

- [x] **Step 1: Run the required structural checks.**

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

Each command must exit zero before committing. The current baseline has 30 tests.
These checks now include the registered plugin; do not infer semantic correctness.

- [x] **Step 2: Check the authored evaluation inventory.**

```bash
.venv/bin/python - <<'PY'
import json
from collections import Counter
from pathlib import Path
cases = json.loads(Path('plugins/time-modeling/evals/cases.json').read_text())
assert len(cases) == 16
assert len({case['id'] for case in cases}) == len(cases)
assert Counter(case['mode'] for case in cases) == {'design': 7, 'audit': 8, 'none': 1}
assert Counter(case['invocation'] for case in cases) == {'implicit': 14, 'explicit': 2}
for case in cases:
    for field in ('prompt', 'context'):
        assert isinstance(case[field], str) and case[field].strip()
    for field in ('required_findings', 'forbidden_findings'):
        assert case[field] and all(isinstance(x, str) and x.strip() for x in case[field])
    expected = [] if case['mode'] == 'none' else [f"time-modeling:{case['mode']}-time-models"]
    assert case['expected_activation'] == expected
print('16 evaluation cases: valid inventory and workflow identities')
PY
```

This is an artifact consistency check, not a new repository test or model grader.

- [x] **Step 3: Collect supplemental evidence where available.**

Discover available native validation tooling without installing it. Run applicable
read-only native validators and record exact tools/versions and outcomes. For live
model evaluations, use supported isolated plugin loading with hidden oracles; do
not install into user configuration. If suitable tools or isolated model runs
are unavailable, state that limitation explicitly. Do not label model behavior
passing merely because packaging validation passed.

- [x] **Step 4: Review the final diff and record evidence.**

Check every acceptance item in the spec, both skill activation scopes, source
attribution, optional-versus-required decisions, and the 16 cases. Check that no
unrelated plugin files changed. Write the verification record with exact commands,
results, and unverified portions; link it from the plugin README. Run the
repository validator after adding the record to verify its authored links.

- [x] **Step 5: Commit only intended deliverables.**

Stage the new manifests, skills, references, examples, evaluations, plugin README,
verification record, this plan, inventory, generated catalogs, and collection
README by explicit path. Leave the existing user-edited spec unstaged. Run
`git diff --cached --check` and inspect `git diff --cached --stat`, then commit as
`feat: add time-modeling plugin`. Report the commit, workflow names, checks, and
material verification limits. Do not merge, publish, or install the plugin.

## Plan self-review

The tasks cover the spec's provenance, two workflows, shared guidance, examples,
16 behavioral cases, dual manifests, inventory/catalog changes, documentation,
and evidence requirements. Shared paths and workflow identities match across
tasks. The user-edited spec is preserved. No runtime-code tests or tooling changes
are required for this content-only package.

## Execution evidence

Tasks 1 and 2 are implemented. Task 3 checks passed; this plan accompanies the
scoped implementation commit. See the [verification record](../../verification/2026-09-17-initial.md).
Native validation and discovery passed. Model baseline and plugin-enabled runs
were unavailable: Claude is logged out, and Codex has no documented raw-path
session loader for the new uninstalled plugin. No semantic red/green improvement
is claimed. The user selected inline execution; no subagents were dispatched.

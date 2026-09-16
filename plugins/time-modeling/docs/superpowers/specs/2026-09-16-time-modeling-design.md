# Time Modeling plugin design

Date: 2026-09-16
Status: Design approved in conversation; written spec awaiting user review.

## Purpose and scope

Create `time-modeling`, an independently installable, language-agnostic plugin
for Codex and Claude Code. It helps agents design temporal data models and audit
existing implementations. The user selected design and review guidance, then
approved the two-workflow design.

The plugin supplies authored instructions, references, original examples, and
behavioral evaluation cases. It does not supply a time library, migration tool,
runtime service, hooks, or language-specific recipe collection. Installation,
publication, and user configuration changes are outside this contribution.

## Source and interpretation

The primary source is Jon Skeet's
[Storing UTC is not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/),
published March 27, 2019. Attribute the article and link relevant sections;
write concise original guidance rather than reproduce its prose or code.
Clearly label the article's hypothetical European policy changes as hypothetical.
Do not treat article comments as the author's guidance.

The source-derived rule set is:

- Determine whether the intended invariant is an instant or a local-time
  commitment. UTC is appropriate for machine-recorded instants.
- Preserve source local date/time and zone identity for local-time commitments.
  UTC may be derived on demand or cached and recomputed when rules change.
- Preserve source information deliberately; its original textual representation
  need not be retained unless requirements demand it.
- A numeric offset does not replace a time-zone identity. Location-to-zone
  assignments can change, so consider preserving location when it defines intent.
- Choose explicit handling for skipped and ambiguous local times, including
  ambiguities introduced by subsequent rule changes.
- Recurrences need a coordinating zone and occurrence-specific conversions.
- Recent-past local conversions may use stale rules; do not assume all historical
  data is reliable merely because it concerns the past.
- Rule versions can support diagnostics and cache updates; reconstructing source
  local values from derived UTC requires the original conversion context.

Workflow structure, reporting conventions, and evaluation design below are our
implementation choices, not claims that Skeet prescribed them.

## Package architecture

Keep all plugin-owned material under `plugins/time-modeling/`:

```text
.codex-plugin/plugin.json
.claude-plugin/plugin.json
README.md
skills/design-time-models/SKILL.md
skills/audit-time-models/SKILL.md
references/principles.md
references/reporting.md
references/sources.md
examples/time-models.md
evals/README.md
evals/cases.json
docs/superpowers/specs/2026-09-16-time-modeling-design.md
```

Both manifests use the name `time-modeling`, initial version `0.1.0`, and a
nonempty description. Shared skills and references are not copied per platform.
The skills link to the same principles and reporting references. Sources maps
rules to article sections and distinguishes source guidance from extensions.
Examples illustrate decisions; they are not another independent rule set.

Register the package in `catalogs/plugins.json` and regenerate both marketplace
catalogs through the existing renderer. Update the repository README to describe
the additional plugin. Do not modify unrelated plugin content or introduce
platform-specific configuration.

This spec stays inside the plugin, overriding the brainstorming skill's default
repository-level documentation location to satisfy repository containment rules.

## Design workflow

`design-time-models` applies to requests to design or change time storage,
scheduling models, conversion boundaries, or handling of time-zone rule updates.

1. Inspect relevant requirements, schemas, types, callers, and repository
   conventions. Identify what the product intends to preserve.
2. Consult the shared principles and identify source fields, derived fields,
   conversion dependencies, and policies needed for this task.
3. Present a concrete model and explain its behavior across updates and error
   cases. Use the project's existing language and storage conventions when known.
4. Identify validation scenarios, assumptions, and unresolved decisions. If
   requirements are missing, explain conditional alternatives and ask only for
   the decision needed to proceed safely.

Output includes the invariant, source and derived field roles, conversion/update
flow, applicable edge-case policies, and validation criteria. Do not prescribe
unneeded fields universally. The workflow does not grant authority to edit code
beyond the user's request or override another applicable implementation process.

## Audit workflow

`audit-time-models` applies to reviews, investigations, and bug diagnoses of
existing temporal storage or conversion behavior.

1. Trace input through persistence, conversions, updates, and relevant consumers.
2. Compare demonstrated behavior with requirements and shared principles.
3. Report actionable findings with file and line references, a concrete failure
   condition, its consequence, and a proportionate correction.
4. Separate confirmed findings from conditional concerns and missing evidence.
   If no material issue is found, say so and state the examined scope.

Reviews remain read-only unless the user also authorizes changes. Do not flag a
UTC column as defective merely because it stores UTC. If a library's behavior or
a database type's semantics are unknown, inspect available evidence or mark them
unverified instead of assuming what their names imply.

## Selection and shared reporting

Skill descriptions explain when each workflow applies. Explicit invocation uses
`time-modeling:design-time-models` or `time-modeling:audit-time-models` with the
platform's invocation syntax. Unrelated uses of words such as time, date, or UTC
should not activate these workflows.

Reporting remains proportionate to the task. Distinguish requirements,
observations, recommendations, and unresolved facts. Reading a schema does not
prove runtime behavior, and supplying a test scenario does not mean it was run.
Failures to inspect code or execute checks must remain visible in the result.

## Examples and evaluation

Use original examples with explicit inputs, intended behavior, and contrasting
correct and incorrect decisions. Include both valid and invalid uses of UTC so
the plugin cannot pass by recommending the same storage model for every task.

Create paired design/audit cases for recorded instants, local-time commitments,
rule updates, gaps and overlaps, recurrence, and missing requirements. Add cases
for offset-only storage, location-defined intent, recent-past conversion, and an
unrelated request. Include implicit selection and explicit invocation cases.

Each case separates model-visible `prompt` and `context` from grader-only
expected workflow identities, required findings, and forbidden findings. Keep
expectations hidden during model runs; grade meaning rather than exact wording.
Record observed activation separately from semantic correctness. Mark missing
telemetry or unavailable runs unverified, with an explanation. Store transcripts
in ignored evaluation workspaces; do not claim behavioral validation from
structural checks. No new general-purpose evaluation runner is required.

## Validation and acceptance

The implementation is ready for review when:

- Both manifests, two skills, shared references, examples, evaluation cases, and
  plugin README exist and agree on names, scope, and behavior.
- Authored local resource links resolve inside this plugin.
- Both catalogs match the inventory and generated manifests.
- Evaluation expectations cover correct behavior and tempting incorrect advice.
- Verification evidence separates structural checks, any supplemental platform
  checks, and any actual model behavior runs.

Run the repository-required commands before commits:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m scripts.catalogs --check
.venv/bin/python -m scripts.validate
```

Regenerate catalogs after inventory or manifest metadata changes with
`.venv/bin/python -m scripts.catalogs`. Native validators are supplemental;
repository Python validation is not exhaustive platform-schema validation.

## Delivery and review gates

Work in the dedicated worktree on `codex/time-modeling`. First commit this spec
using a conventional documentation commit after the repository checks. Review it
for placeholders, contradictions, scope drift, and ambiguous requirements.
Request user review of the written spec before invoking the writing-plans skill.
The implementation plan and subsequent plugin work follow that approval.

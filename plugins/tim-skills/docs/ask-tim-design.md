# Ask Tim design

Status: approved on 2026-10-14.

## Decisions

- Add `ask-tim` to the existing Tim skills package and map its fourteen specialist workflows.
- Route only to skills supplied by `tim-skills`.
- Require explicit invocation, matching `ask-matt`.
- Read candidate skill bodies before explaining, recommending, or excluding them.
- Recommend the best next skill, explain why, and show its platform-specific invocation. The user chooses when to start it.
- For overlapping topics, lead with the main unresolved decision. Add a short flow only for distinct needs and explain its order.
- Ask a focused question when a missing answer changes the recommendation. Say when no Tim skill fits.
- Identify unavailable candidate files as an evidence limit rather than inventing behavior or installing a skill.

The [glossary](../GLOSSARY.md) defines the routing language. The runtime
[skill](../skills/ask-tim/SKILL.md) owns the routing procedure and map. These
choices are easy to revise and do not warrant an ADR.

## Verification

[Verification evidence](ask-tim-verification.md) records the executed checks and
their limits.

Add grader-only evaluation contracts for each specialist route, overlapping
topics, ambiguity, no-match requests, unavailable candidates, and explicit-only
invocation. Keep their expected recommendations separate from activation:
reading a candidate as reference is not starting its workflow.

Run the repository unit tests, catalog regeneration and drift check, and Python
resource validator. Supplement these with available native packaging checks and
independent reasoning probes. Structural checks and reasoning probes do not
establish live platform activation or reliability across models.

## Repository baseline

The pooled checkout was refreshed from `origin/main` at
`65b4a0da9bb90d8529bf3195d6b4df61db3414c4`. It supplied one `tim-skills`
plugin with fourteen specialist workflows and no `ask-tim` skill.

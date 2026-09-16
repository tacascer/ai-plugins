# Time Modeling

Time Modeling provides shared Codex and Claude Code workflows for designing and
reviewing temporal data models. Its language-agnostic guidance is informed by
Jon Skeet's [Storing UTC is not a silver bullet](https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/).
The plugin is not affiliated with or endorsed by the author.

## Workflows

- `design-time-models` develops a concrete model from requirements, input
  provenance, conversions, and consumers, and identifies unresolved policies.
- `audit-time-models` reviews existing implementations and reports actionable,
  evidenced findings and proportionate corrections. Reviews are read-only unless
  changes are also requested.

Neither workflow mandates one storage representation for every temporal value.
They follow repository conventions and do not select a language, database,
time-zone library, geographic service, or migration tool.

Descriptions support automatic selection for matching tasks; live activation is
not yet verified. Explicit invocation uses:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design | `$time-modeling:design-time-models` | `/time-modeling:design-time-models` |
| Audit | `$time-modeling:audit-time-models` | `/time-modeling:audit-time-models` |

For example, request an audit of the appointment schema and reminder update job,
or ask for a model for weekly meetings spanning time zones. Incidental dates in
release notes are outside these workflows' scope.

For a local Claude session, substitute your checkout's absolute path:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/time-modeling
```

Collection installation instructions and publication status are in the
repository-level README. No plugin installation is required for the repository's
structural checks.

## Shared guidance

- [Principles](references/principles.md): the shared rule set and application procedure.
- [Reporting](references/reporting.md): output conventions, uncertainty, and evidence.
- [Sources](references/sources.md): attribution and boundaries of the source material.
- [Original examples](examples/time-models.md): contrasting decisions and expected outcomes.

## Evaluation and status

The [evaluation guide](evals/README.md) describes 16 cases with hidden grader
expectations, implicit and explicit invocation, and a negative activation case.
The [verification record](docs/verification/2026-09-17-initial.md) separates
packaging/discovery checks from live model behavior. Passing a structural check
does not establish semantic correctness or reliable skill activation.

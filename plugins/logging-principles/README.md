# Logging Principles

Logging Principles provides shared Codex and Claude Code workflows for designing
and reviewing application logging, failure reporting, and diagnostic signals.
Its language-neutral guidance is informed by Nikita Sobolev's
[Do not log](https://sobolevn.me/2020/03/do-not-log), published March 11, 2020.
The plugin is not affiliated with or endorsed by the author.

## Workflows

- `design-logging` chooses a proportionate signal from the operational question,
  consumer, expected action, deployment constraints, and failure significance.
- `audit-logging` reviews existing logging and failure reporting for actionable,
  evidenced problems while identifying useful signals that should remain. The
  audit is read-only unless the user also requests changes.

Neither workflow mandates removing all logs, adopting a vendor, or replacing a
project's language and failure-handling conventions. Incidental mentions of logs
and general observability-platform architecture are outside their scope.

Descriptions support automatic selection for matching tasks. Explicit invocation
uses:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design | `$logging-principles:design-logging` | `/logging-principles:design-logging` |
| Audit | `$logging-principles:audit-logging` | `/logging-principles:audit-logging` |

For a local Claude session, substitute your checkout's absolute path:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/logging-principles
```

Collection installation instructions and publication status are in the
repository-level README. No plugin installation is required for the repository's
structural checks.

## Shared guidance

- [Principles](references/principles.md): source-derived guidance, the decision procedure, and practical safeguards.
- [Reporting](references/reporting.md): evidence, uncertainty, and output conventions.
- [Sources](references/sources.md): attribution and boundaries between source material and plugin extensions.
- [Original examples](examples/logging-decisions.md): contrasting operational needs and diagnostic decisions.

## Evaluation and status

The [evaluation guide](evals/README.md) describes 16 semantic probes with hidden
grader expectations, implicit and explicit invocation, and a negative activation
case. Repository checks validate supported structure, links, inventory, and
generated catalogs. Live workflow activation and semantic model behavior remain
unverified because no approved supported loader and authenticated inference path
are available in this environment.

See the [initial verification record](docs/verification/2026-09-17-initial.md)
for executed structural checks, supplemental platform evidence, and the model
validation limitation.

# Domain-Driven Design

This plugin provides shared Codex and Claude Code workflows for designing new
business models and assessing existing ones. It covers strategic boundaries,
business rules, implementation choices, and business-event interactions. Its
guidance is informed by Vlad Khononov's
[*Learning Domain-Driven Design*](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
and includes original engineering synthesis. The plugin is not affiliated with
or endorsed by the author or publisher; [source notes](references/sources.md)
state what was accessible and what is independently authored.

## Workflows

- `design-domain-model` develops a proportionate model from business scenarios,
  language, ownership, invariants, and integration requirements. It asks for
  policy decisions that would otherwise be guessed.
- `audit-domain-model` traces existing business flows and reports evidenced
  findings with consequences and practical corrections. Reviews are read-only
  unless changes are also requested. A sound simple design can need no change.

The descriptions permit automatic selection for matching tasks; live selection
has not yet been verified. Explicit invocation is:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design | `$domain-driven-design:design-domain-model` | `/domain-driven-design:design-domain-model` |
| Audit | `$domain-driven-design:audit-domain-model` | `/domain-driven-design:audit-domain-model` |

For a local Claude session, use the package's absolute path:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/domain-driven-design
```

Repository-level installation and development instructions are in the
collection README. This package does not require user
installation for structural validation.

## Shared material and evaluation

[Principles](references/principles.md) route work to the appropriate
[strategic](references/strategic-design.md),
[tactical](references/tactical-design.md),
[event-driven](references/event-driven-design.md), and
[evolution](references/evolution.md) guidance.
[Reporting](references/reporting.md) defines evidence and uncertainty,
and original [domain](examples/domain-decisions.md) and
[event](examples/event-driven-decisions.md) examples contrast proportionate
choices. The [evaluation guide](evals/README.md) defines 21 cases, including
an order-flow audit fixture, and separates hidden graders from model-visible
inputs. Authored cases and structural validation do not establish live
activation or semantic results.

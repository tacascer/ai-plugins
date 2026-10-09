# Domain-Driven Design

The Domain-Driven Design topic in Tim skills provides shared Codex and Claude Code workflows for designing new
business models and assessing existing ones. It covers strategic boundaries,
business rules, implementation choices, and business-event interactions. Its
guidance is informed by Vlad Khononov's
[*Learning Domain-Driven Design*](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
and includes original engineering synthesis. The plugin is not affiliated with
or endorsed by the author or publisher; [source notes](../../references/domain-driven-design/sources.md)
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
| Design | `$tim-skills:design-domain-model` | `/tim-skills:design-domain-model` |
| Audit | `$tim-skills:audit-domain-model` | `/tim-skills:audit-domain-model` |

For a local Claude session, use the package's absolute path:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/tim-skills
```

Repository-level installation and development instructions are in the
collection README. This package does not require user
installation for structural validation.

## Shared material and evaluation

[Principles](../../references/domain-driven-design/principles.md) route work to the appropriate
[strategic](../../references/domain-driven-design/strategic-design.md),
[tactical](../../references/domain-driven-design/tactical-design.md),
[event-driven](../../references/domain-driven-design/event-driven-design.md), and
[evolution](../../references/domain-driven-design/evolution.md) guidance.
[Reporting](../../references/domain-driven-design/reporting.md) defines evidence and uncertainty,
and original [domain](../../examples/domain-driven-design/domain-decisions.md) and
[event](../../examples/domain-driven-design/event-driven-decisions.md) examples contrast proportionate
choices. The [evaluation guide](../../evals/domain-driven-design/README.md) defines 21 cases, including
an order-flow audit fixture, and separates hidden graders from model-visible
inputs. The [initial verification record](../domain-driven-design/verification/2026-09-27-initial.md)
lists completed checks and the current inference blocker. Live activation and
semantic behavior remain unverified.

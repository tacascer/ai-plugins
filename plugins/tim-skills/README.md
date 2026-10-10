# Tim skills

One plugin with 14 shared Codex and Claude Code workflows for designing,
implementing, and auditing software. Topic guidance, sources, examples, and
evaluation fixtures remain grouped inside this package.

## Workflows

Use `$tim-skills:<skill-name>` in Codex or `/tim-skills:<skill-name>` in Claude
Code. Each skill retains its existing description, scope, and procedure.

| Topic | Skill names | Guidance |
| --- | --- | --- |
| Testing | `design-for-testing`, `classify-tests`, `audit-tests` | [Testing Principles](docs/topics/testing-principles.md) |
| Time modeling | `design-time-models`, `audit-time-models` | [Time Modeling](docs/topics/time-modeling.md) |
| Observability | `design-observability`, `implement-observability`, `audit-observability` | [Design Observability](docs/topics/design-observability.md) |
| Domain models | `design-domain-model`, `audit-domain-model` | [Domain-Driven Design](docs/topics/domain-driven-design.md) |
| Rust | `design-rust`, `audit-rust` | [Rust Patterns](docs/topics/rust-patterns.md) |
| GraphQL | `design-graphql`, `audit-graphql` | [GraphQL Design](docs/topics/graphql-design.md) |

For example:

```text
$tim-skills:design-for-testing review this production boundary
/tim-skills:design-graphql design object refetching and cursor pagination
```

Audits retain their read-only scope unless fixes are requested. Design workflows
retain their approval boundaries. Packaging the skills together does not expand
any skill's remit or authorize application edits.

## Package layout

- `skills/<skill-name>/` exposes each of the 14 workflows directly.
- `references/<topic>/` and `examples/<topic>/` preserve topic resources and avoid
  collisions between filenames such as `principles.md` and `sources.md`.
- [Evaluations](evals/README.md) contain the combined case inventory, with topic
  guides, fixtures, and the existing result schema alongside it.
- `docs/topics/` contains topic documentation; `docs/<topic>/` preserves prior
  plans and verification records.

Both platform manifests identify this package as `tim-skills`, version `1.0.0`.
The Codex interface display name is **Tim skills**. Installation commands and
migration from the six former packages are in the repository README. After a
revision containing Tim skills is published, Claude Code can install it with:

```text
/plugin install tim-skills --marketplace tacascer/ai-plugins
```

Historical verification records describe the package names and revisions tested
at the time. They do not establish live activation or semantic correctness for
the combined plugin. Existing guidance retains its source attribution and limits.

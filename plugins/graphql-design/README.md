# GraphQL Design

Two language- and framework-agnostic workflows for GraphQL server object
identification, refetching, cursor connections, and pagination behavior. The
required baseline follows Relay's [server guide](https://relay.dev/docs/v20.1.0/guides/graphql-server-specification/),
[identification specification](https://relay.dev/graphql/objectidentification.htm),
and [connection specification](https://relay.dev/graphql/connections.htm).
See the [source map](references/sources.md) for versions, access limits, and
formal versus engineering guidance. This package is independent of the other
plugins and does not require a Relay client.

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design or revise relevant GraphQL server contracts | `$graphql-design:design-graphql` | `/graphql-design:design-graphql` |
| Audit existing schema or resolver behavior | `$graphql-design:audit-graphql` | `/graphql-design:audit-graphql` |

The design workflow returns relevant SDL, resolver contracts, rationale,
verification scenarios, and migration advice where needed. The audit workflow
is read-only unless fixes are separately requested. Both distinguish formal
requirements from optional specification features and engineering choices.
They do not cover general mutations, federation, subscriptions, application
scaffolding, or client-only presentation changes. No application edit or
installation is implied by using these skills.

The [evaluation cases](evals/README.md) are authored probes, not live model
results. The [initial verification record](docs/verification/2026-09-30-initial.md)
separates repository and native packaging checks, direct fixture calls, and
unverified live activation and semantic behavior.

The [design decisions](examples/design-decisions.md) and
[audit findings](examples/audit-findings.md) show worked examples. The audit
example uses a small static [library fixture](evals/fixtures/library-api/README.md)
and distinguishes direct Python function checks from GraphQL execution.

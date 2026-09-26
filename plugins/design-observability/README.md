# Design Observability

Design Observability provides shared Codex and Claude Code workflows for designing
implementing, and reviewing application observability around explicit structured events:

```text
application -> structured events -> listeners -> logs, metrics, traces, error reports
```

Producers describe meaningful facts. Listeners own signal mapping and export.
A synchronous in-process pipeline is sufficient; no broker, vendor, or new hosted
service is required. Minimal direct diagnostics cover points where observability
infrastructure is not guaranteed to be available, such as startup before listener
setup. Application simplicity alone does not justify bypassing events.

## Workflows

- `design-observability` designs event contracts, emission boundaries, listeners,
  useful signals, lifecycle, delivery behavior, and verification.
- `implement-observability` implements provider-portable OpenTelemetry metrics and
  traces, export configuration, context propagation, and SDK lifecycle.
- `audit-observability` reviews those boundaries for actionable problems while
  preserving useful signals and justified availability fallbacks. The audit is
  read-only unless edits are requested.

Descriptions support automatic selection for matching tasks. Explicit invocation:

| Workflow | Codex | Claude Code |
| --- | --- | --- |
| Design | `$design-observability:design-observability` | `/design-observability:design-observability` |
| Implement | `$design-observability:implement-observability` | `/design-observability:implement-observability` |
| Audit | `$design-observability:audit-observability` | `/design-observability:audit-observability` |

Application logging, metrics, traces, and failure reporting are in scope.
Incidental mentions of telemetry and standalone vendor/platform administration
are not. Existing failure semantics and required audit records remain intact.

Implementation uses configurable OTLP export, either directly to a compatible
destination or through an optional Collector. Application events remain independent
of telemetry SDKs. See the [implementation reference](references/opentelemetry.md)
and [worked example](examples/opentelemetry-implementation.md).

## Migration and local loading

Version 0.3.0 adds `implement-observability` to the existing package.


Version 0.2.0 renames the `logging-principles` plugin and its `design-logging` and
`audit-logging` workflows. Use the new package and qualified skill names above;
legacy aliases are not shipped. Existing installations require a corresponding
plugin selection update and a fresh session. This repository change does not
modify user configuration or install the plugin.

For a local Claude session, substitute your checkout's absolute path:

```bash
claude --plugin-dir /absolute/path/to/ai-plugins/plugins/design-observability
```

Collection installation instructions are in the repository README. No plugin
installation is required for structural checks.

## Shared guidance

- [Principles](references/principles.md): event contracts, listeners, delivery, availability exceptions, and verification boundaries.
- [Reporting](references/reporting.md): design output, audit findings, evidence, and uncertainty.
- [Examples](examples/observability-decisions.md): concrete decisions and contrasting failures.
- [Sources](references/sources.md): logging foundations and original architectural guidance.

The original logging foundations draw on Nikita Sobolev's
[Do not log](https://sobolevn.me/2020/03/do-not-log). The event/listener architecture
is this plugin's extension. The plugin is not affiliated with or endorsed by the
author.

## Evaluation

See the [implementation verification record](docs/verification/2026-09-26-opentelemetry-implementation.md)
for version 0.3.0 checks and limited authoring probes, and the
[redesign verification record](docs/verification/2026-09-25-observability-redesign.md)
for executed checks, limited authoring probes, and remaining validation limits.

The [evaluation guide](evals/README.md) describes semantic probes and independent
activation grading. Repository checks validate supported structure, links,
inventory, and generated catalogs; they are not exhaustive platform-schema or
live activation validation. Historical specs and the
[initial verification record](docs/verification/2026-09-17-initial.md) describe
version 0.1.0 under its former name, not evidence for this revision.

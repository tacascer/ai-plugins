---
name: audit-logging
description: Use when reviewing or investigating existing logging and failure-reporting behavior, including unnecessary logs, missing diagnostic context, and unsafe signal removal.
---

# Audit Logging

Find actionable mismatches between diagnostic behavior and demonstrated
operational needs. Read the shared [principles](../../references/principles.md);
a logger call alone is not evidence of a defect.

## Procedure

1. Trace representative log and failure-reporting sites through callers,
   failure handling, configuration, delivery, storage, and consumers. Inspect
   available operational requirements and relevant tests.
2. Assess each signal's demonstrated purpose, context, severity, emission
   placement, sensitive-data exposure, and handling. Verify that any proposed
   replacement serves the consumer in the actual deployment environment; a
   dependency alone does not prove monitoring coverage.
3. Report prioritized findings with file and line evidence, a concrete trigger,
   consequence, and proportionate correction. Separately identify justified
   logs that should remain when removal is a plausible mistaken recommendation,
   including required audit records, startup output, or disconnected local
   diagnostics.
4. Separate confirmed defects, conditional concerns, and missing evidence using
   [reporting](../../references/reporting.md). State the examined scope and say
   when no material issue is established.

Preserve propagation, recovery, retry, or explicit failed-result semantics when
recommending less logging; never turn a caught failure into silent success. Do
not infer that an undocumented signal is useless. With only an abstract
scenario, cite the supplied evidence without inventing file locations or
incidents.

Consult the [original examples](../../examples/logging-decisions.md) when a
comparison helps. Keep the audit read-only unless the user also requests edits,
and do not expand existing implementation authorization. This workflow applies
to logging and failure-reporting reviews, not incidental log mentions or general
observability platform architecture.

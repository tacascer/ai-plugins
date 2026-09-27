---
name: audit-domain-model
description: Audit existing business domain models, bounded contexts, invariants, aggregates, and business-event integrations for evidenced risks and proportionate evolution. Use for business-rule or event-driven design reviews, not DNS or unrelated infrastructure domains.
---

# Audit domain model

Use [shared principles](../../references/principles.md), then read only the
needed topic references. Read
[strategic design](../../references/strategic-design.md) for context meaning
and ownership, [tactical design](../../references/tactical-design.md) for
invariants and implementation patterns, and
[reporting](../../references/reporting.md) for evidence and limits. Consult
[sources](../../references/sources.md) before making book-specific claims.

1. Establish the requested scope and business requirements. Inspect the
   available scenarios, code, schemas, transaction boundaries, and message
   contracts; report which were unavailable.
2. Trace representative business operations through decisions, state changes,
   and integrations. Locate each important invariant and its enforcement point.
3. Separate demonstrated defects from plausible risks and questions needing
   business expertise. Missing evidence is a limit, never proof of a defect.
4. For each finding, give a code or contract location when available, or cite
   concrete supplied scenario evidence. Explain the business or operational
   consequence, a proportionate correction, and a check that would verify it.
5. Prioritize by consequence. Report reviewed scope, checks actually performed,
   and open questions. Recommend no change when the existing design serves the
   known requirements; absent DDD vocabulary is not itself a defect.

Audits are read-only unless the user also requests edits. Do not claim to have
run proposed tests or inspected unavailable code.

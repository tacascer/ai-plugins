---
name: design-domain-model
description: Design or revise business domain models, rules, bounded contexts, aggregates, and business-event interactions for new or existing systems. Use for decisions about domain ownership and event-driven business flows, not DNS or unrelated infrastructure domains.
---

# Design domain model

Use [shared principles](../../references/principles.md), then read only the
topic references relevant to the request. Read
[strategic design](../../references/strategic-design.md) for business discovery,
language, ownership, and contexts; read
[tactical design](../../references/tactical-design.md) for rules, consistency,
aggregates, and logic patterns. Use [reporting](../../references/reporting.md)
for evidence and output. Consult [sources](../../references/sources.md) before
attributing a specific recommendation to the book.

1. Inspect the request and available business scenarios, requirements, code,
   contracts, and constraints. Keep observed facts apart from assumptions.
2. Ask for the domain-expert answer to any missing policy that changes the
   model. State conditional choices if the answer is unavailable.
3. Define only the terminology, responsibilities, context boundaries, and
   invariants needed for this decision. Distinguish subdomains, bounded
   contexts, aggregates, and deployment choices.
4. Compare suitable implementation and integration choices against rule
   complexity, ownership, consistency, and operational needs. A simple
   transaction can be the right design.
5. For business-event flows, name the fact or intent, producer, consumers,
   ownership, timing and failure policy. Explain coordination where decisions
   span participants; do not infer event sourcing or CQRS from messaging.
6. Return actionable decisions, a proportionate alternative and trade-off,
   unresolved questions, proposed verification, and an implementation or
   migration sequence suited to the request's size.

Follow the user's authorized development scope. This skill does not grant
permission to edit beyond it. A candidate process map or EventStorming draft
remains provisional until stakeholders validate it.

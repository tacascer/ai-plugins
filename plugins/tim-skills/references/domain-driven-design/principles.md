# Shared decision principles

Start with a business decision or failure: who needs to do what, under which
rule, with what consequence if the rule is broken? Distinguish supplied facts,
observed implementation, assumptions, and unanswered policy questions. Do not
infer missing policy from pattern names. Prefer the least elaborate model that
can express and enforce the known rules, and revisit it when requirements
change. A straightforward CRUD flow can remain straightforward.

Use the references selectively:

- Read [strategic design](strategic-design.md) for subdomains, context-scoped
  language, ownership, integration relationships, or stakeholder discovery.
- Read [tactical design](tactical-design.md) for invariants, aggregates, entities,
  value objects, implementation patterns, and architecture choices.
- Read [event-driven design](event-driven-design.md) for business messages,
  consumer contracts, coupling, workflow coordination, and delivery recovery.
- Read [evolution](evolution.md) for changed business importance, incremental
  modernization, and contract coexistence.
- Read [reporting](reporting.md) for evidence and output conventions.
- Read [sources](sources.md) when attributing guidance to the book or describing
  access limits.

For design, turn relevant evidence into concrete boundaries, rules, ownership,
and a small implementation path. Compare choices against the supplied
requirements. For audit, trace a representative business flow before declaring
a defect; a naming or folder difference alone is not a business consequence.
Treat a bounded context as a model/language boundary, a subdomain as a business
capability, an aggregate as a consistency boundary, and a deployment unit as an
operational choice. None determines the others mechanically.

For a business-event design, state the producer's fact or request, consumer
responsibilities, consistency promise, and recovery path. For an event audit,
trace the state commit, publication, and consumer effect to concrete code or
contract evidence. An event name alone does not prove delivery or ownership.

---
name: audit-graphql
description: Use when reviewing GraphQL server schemas, object identification, refetching, cursor connections, pagination responses, or resolver behavior for Relay compatibility. Excludes unrelated REST and client-only presentation changes.
---

# Audit GraphQL

Audit the relevant Relay-compatible server contract using the
[decision guide](../../references/principles.md). Load
[identification](../../references/identification.md) for Node/refetch evidence
and [connections](../../references/connections.md) for paginated fields; consult
[sources](../../references/sources.md) when a requirement is disputed.

## Procedure

1. Establish inspected scope and available SDL/introspection, resolver, test,
   and runtime evidence. Distinguish supplied traces from checks you executed.
2. Check schema contracts first, then trace resolver behavior where available.
   Do not infer runtime compatibility from SDL alone.
3. Report confirmed formal violations in priority order with location,
   triggering query/input, consequence, supporting evidence, and a practical
   correction. Use [reporting](../../references/reporting.md).
4. Separate engineering recommendations and evidence gaps from formal
   violations. State which runtime behaviors remain unverified and propose
   targeted checks without claiming they ran.
5. Say when there are no evidenced violations. Accept optional choices such as
   non-base64 opaque IDs, one pagination direction, scalar edge nodes, and
   permitted nullability; do not manufacture preference-based defects.

Audits are read-only unless fixes are separately requested. This workflow does
not authorize application edits or installs.

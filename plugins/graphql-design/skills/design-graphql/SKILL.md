---
name: design-graphql
description: Use when designing or revising GraphQL server schemas, object refetching, cursor connections, or pagination resolver contracts. Excludes unrelated REST changes and client-only presentation work.
---

# Design GraphQL

Design relevant server contracts against Relay-compatible identification and
connection behavior, regardless of whether current clients use Relay. Use the
[decision guide](../../references/principles.md) to select the relevant scope,
then load [identification](../../references/identification.md) for refetchable
objects and [connections](../../references/connections.md) for paginated fields.
The [source map](../../references/sources.md) distinguishes formal rules from
application advice.

## Procedure

1. Inspect requirements, existing schema and resolvers, client queries, and
   repository conventions. Distinguish observed facts from assumptions.
2. Identify refetchable entities and collection relationships. Establish
   identity scope, visibility/filtering, business ordering and tie-breaker, and
   needed pagination directions. Ask only for missing decisions that materially
   change the contract; otherwise offer a conditional design.
3. Propose relevant SDL and resolver behavior using the selected references.
   Keep the required baseline even without a Relay client. Do not force every
   object to implement `Node` or every list into a connection.
4. Explain ID construction/refetch, unavailable objects, cursor interpretation,
   page boundaries and flags, zero/negative sizes, and invalid inputs when
   relevant. Label authorization, ordering, cursor policy, and data-change
   behavior as product or engineering decisions where the specs leave choices.
5. Return rationale, a meaningful alternative where useful, proposed
   verification scenarios, and a migration sequence for existing clients.
   Follow [reporting](../../references/reporting.md). Use the original
   [library example](../../examples/design-decisions.md) if a concrete shape
   helps; adapt it to the user's domain.

Output depth follows the request. Guidance does not itself authorize code edits
or dependency installation and imposes no extra approval ritual.

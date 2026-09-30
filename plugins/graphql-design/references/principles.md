# Choosing the relevant contract

The required design and audit baseline is Relay-compatible object identification
and cursor connections, even when today's clients use plain GraphQL fetches.
Apply each contract where it serves the product: refetchable durable entities use
`Node`; paginated relationships use connections. Neither specification says every
object must implement `Node` or every list must be a connection. Read
[identification](identification.md) for identity/refetch decisions and
[connections](connections.md) for pagination decisions. See [sources](sources.md)
for the formal anchors.

| Decision | Evidence to obtain | Contract to use |
| --- | --- | --- |
| Can clients revisit this entity by an ID returned by the server? | Entity lifetime, ID scope, deletion and permission behavior. | `Node` and root `node` lookup for refetchable entities. |
| Does a field expose a collection that clients page through? | Relationship, visibility/filter inputs, business order, direction needs. | A connection with at least one complete argument pair. |
| Is a field merely a short fixed list or an edge value? | Whether independent refetch or paging is actually needed. | A plain list or non-Node edge value can remain valid. |
| Is this an existing API? | Current client queries and field contracts. | Add compatible fields and migrate clients deliberately. |

**Engineering guidance, separate from formal requirements:** Choose stable
business ordering with a unique tie-breaker; keep cursor meaning bound to that
order, filters, and visibility scope. Define what happens when data changes
between page requests. Authorization must still apply when an object is reached
through `node` or a connection. These policies affect useful behavior but do not
turn one particular sort key, authorization design, or cursor encoding into a
Relay mandate. If a decision materially changes the contract and is absent,
ask for it or mark a proposal conditional.

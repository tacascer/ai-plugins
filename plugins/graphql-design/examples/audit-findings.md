# Example: library API audit findings

Scope: the [fixture SDL](../evals/fixtures/library-api/schema.graphql), its
[resolver adapter](../evals/fixtures/library-api/resolvers.py), and the
[documented library policy](../evals/fixtures/library-api/README.md). The SDL
has the required `Node`, root `node`, connection, edge, and `PageInfo` shapes.
The observations below come from reading and directly calling the Python
functions. No GraphQL executor, request authorization middleware, or database
was run. This is a worked audit report, not an evaluation input.

## Confirmed compatibility findings

1. **Distinct Node objects share one exposed ID.**
   `object_id("Book", "1")` and `object_id("Author", "1")` both return `"1"`.
   `node("1", "alice")` searches `BOOKS` before `AUTHORS` and returns Book A,
   so an Author with that ID cannot be unambiguously refetched. The collision
   occurs in `object_id` and the lookup loop in `node`, despite each type's
   local IDs being unique. Construct opaque IDs that include a type namespace
   and local key, then decode or otherwise resolve the full ID in `node`.

2. **Backward pages reverse the public catalog order.**
   `connection(BOOKS, last=2, before="cursor:D")` filters to A, B, C,
   chooses B, C, then returns C, B because `connection` calls
   `edges.reverse()`. Clients paging backward see the opposite order and a
   mismatched edge nearest the `before` cursor. Keep B, C in that order after
   taking the final two bounded edges; derive boundary cursors from that
   ordered result.

3. **Primary-direction page flags hide remaining edges.**
   `connection(BOOKS, first=2)` returns A, B with `hasNextPage: false` although
   C and D remain. `connection(BOOKS, last=2, before="cursor:D")` returns two
   edges with `hasPreviousPage: false` although A remains in the bounded set.
   The `pageInfo` builder fixes both flags to false. Calculate `hasNextPage`
   from the bounded edge count when `first` is supplied, and
   `hasPreviousPage` when `last` is supplied. The opposite-direction flag may
   remain false when its extra discovery cannot be done efficiently.

4. **Negative page sizes are silently accepted.**
   `connection(BOOKS, first=-1)` returns A, B, C; `last=-1` returns D, C, B.
   Python slicing causes both results. Reject either negative count before
   slicing. Preserve zero as valid: `first=0` correctly produces no edges and
   null boundary cursors here, but its `hasNextPage` still needs to reflect
   remaining bounded edges. Empty `edges` and null cursors do not imply both
   page flags are false.

## Application security recommendation

The fixture policy limits private Book A to `alice`, yet
`node(object_id("Book", "1"), principal="bob")` returns Book A. The `node`
lookup never uses `principal`. Apply the same visibility rule to refetching as
to ordinary entry points, returning the application's chosen unavailable
response for an unauthorized caller. This is an application authorization
requirement, separate from Relay's object identification rules.

The SDL alone would miss the ID collision, ambiguous refetch, reversed page,
incorrect flags, negative slicing, and missing authorization check. The
adapter's direct-call traces establish these local behaviors only; they do not
prove that an actual GraphQL endpoint has the same behavior or that any client
query was executed.

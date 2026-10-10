# Cursor connections

Formal source: [GraphQL Cursor Connections Specification](sources.md).

## Schema contracts

- A type ending in `Connection` is a reserved connection object. It has an
  `edges` field returning a list of edge objects and `pageInfo: PageInfo!`.
  Additional connection fields are allowed. An edge object has `node` and
  `cursor`; additional edge fields are allowed. `node` may be a scalar, enum,
  object, interface, or union (or non-null wrapper), but not a list. It need not
  implement the identification `Node` interface.
- The edge `cursor` type serializes as a string: `String`, its non-null form,
  or a string-serializing custom scalar. Clients treat cursor values as opaque.
- `PageInfo` has `hasNextPage: Boolean!` and `hasPreviousPage: Boolean!`, plus
  `startCursor` and `endCursor` containing opaque strings. Boundary cursors may
  be null when no edges are returned. The spec permits choices about nullability
  of `edges`, edge items, `node`, and `cursor` beyond the required shapes.
- A connection field provides forward arguments `first` and `after`, backward
  arguments `last` and `before`, or both complete pairs. `after`/`before` use
  the edge cursor type. Forward-only and backward-only fields are valid.

## Resolver contract

First establish the ordered, visibility-filtered edge set. Apply `after` and
`before` bounds, then `first` by removing excess edges from the end, then `last`
by removing excess edges from the beginning. Negative `first` or `last` throws
an error; zero is valid and yields no edges. Supplying both sizes is discouraged
but the algorithm still defines their order. Cursors exclude their matching edge.
For a cursor that does not match an edge, the formal filtering algorithm leaves
that bound unapplied. A malformed cursor's validation/rejection policy is a
separate application decision; do not invent a mandatory error for an unmatched
well-formed cursor.

The business order must be consistent from page to page. Backward requests use
the **same** edge order as forward requests, never a reversed response. With a
`before` bound, the nearest returned edge is last; with `after`, it is first.
`startCursor` and `endCursor` correspond to the first and last returned edge;
when edges are empty, their permitted null values say nothing by themselves
about page flags.

For `first`, `hasNextPage` is true when more bounded edges existed than the
requested size, otherwise false. For `last`, the analogous required calculation
sets `hasPreviousPage`. The opposite-direction flag may be true when the server
can efficiently establish edges beyond `before` or before `after`; otherwise
false is permitted. With both sizes, apply each flag's specified algorithm even
though the combined request is discouraged.

**Engineering guidance:** Select a business order and unique tie-breaker, cursor
scope, invalid-cursor policy, and behavior under inserts/deletes. Keep access
control and filters consistent across pages. These choices make pagination
reliable but are not extra required GraphQL field shapes or a mandated cursor
encoding.

# Object identification

Formal source: [Global Object Identification Specification](sources.md).

## Required shape and behavior

- Reserve an interface named `Node` with **exactly one** field: `id: ID!`.
  Additional fields belong on implementing object types, not this interface.
- Expose the root query field `node(id: ID!): Node`, with exactly one argument,
  named `id`. The nullable return permits an unavailable or deleted object to
  yield `null`; best-effort refetch does not promise permanent availability.
- A Node ID should be globally unique across object types and refetch the same
  object through `node`. A type-local key alone can collide. The ID is opaque to
  clients; base64 is one convention, not a required encoding.
- When two `Node` objects with the same ID appear within one query, common
  selected fields must agree, recursively for object fields. An audit needs
  runtime evidence to establish this, not just SDL.

Example minimal SDL:

```graphql
interface Node { id: ID! }
type Book implements Node { id: ID!, title: String! }
type Query { node(id: ID!): Node }
```

## Optional plural identifying root fields

A server need not expose a plural identifying lookup. If it offers one for
spec-compliant clients, it has one argument of non-null list of non-null items
(for example `[String!]!`) and returns a list, optionally wrapped non-null,
whose items are `Node` or implementing objects, optionally wrapped non-null.
The output list must have the same length as the input and preserve positional
correspondence under permutations. A missing item may occupy a `null` slot;
using nullable items makes that possible. A general list root field need not
claim to be a plural identifying field, but clients cannot use it as one unless
it obeys these rules.

**Engineering guidance:** Put authorization checks on the refetch path as well
as ordinary entry points. Decide whether inaccessible objects look like
unavailable objects. This is an application policy; the formal rules above do
not prescribe the security design.

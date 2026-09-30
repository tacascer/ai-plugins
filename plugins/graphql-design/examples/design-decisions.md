# Library catalog example

A library exposes durable `Book` and `Author` records. A book can be withdrawn.
Clients want to refetch both entities and page books in publication-date order.
The product confirms newest date first, then ISBN ascending as a unique stable
tie-breaker. This is one product choice, not a specification-imposed order.

```graphql
interface Node { id: ID! }
type Book implements Node {
  id: ID!
  title: String!
  author: Author!
}
type Author implements Node { id: ID!, name: String! }
type BookConnection { edges: [BookEdge], pageInfo: PageInfo! }
type BookEdge { node: Book, cursor: String! }
type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
type Query {
  node(id: ID!): Node
  books(first: Int, after: String): BookConnection
}
```

The resolver issues opaque IDs unique across Book and Author, resolves an ID to
the matching type, and may return `null` when a book is withdrawn or access is
lost. The books resolver orders the authorized set by the confirmed tuple,
interprets opaque cursors for that set, applies `after` then `first`, and derives
`PageInfo` from the bounded set. Negative `first` errors; zero is an empty page.
Authorization and the treatment of a cursor after a withdrawal require an
application policy. A query such as
`books(first: 2) { edges { cursor node { id title } } pageInfo { hasNextPage endCursor } }`
can verify the first page; a follow-up with `after: endCursor` can verify order
and boundaries. These are proposed checks, not executed results.

For an existing `books: [Book!]!` field, add a separate connection field (for
example `bookPage`) and keep the old field until clients migrate. An audit of a
hypothetical `node(key: String!): Book` field would flag its argument and return
shape, with the triggering query `node(id: ...)` and the correction
`node(id: ID!): Node`. Without resolver or runtime evidence, it would leave
actual refetch identity and paging behavior unverified.

# Library API audit fixture

This is a small, static adapter model for inspecting resolver behavior. It has
no GraphQL executor or server. `schema.graphql` describes the intended API;
`resolvers.py` exposes ordinary Python functions that stand in for resolver
paths. `node(object_id, principal)` models the root lookup,
`object_id(kind, local_id)` models ID construction, and
`connection(items, first=None, after=None, last=None, before=None)` models a
relationship connection. `BOOKS` and `AUTHORS` are the relationship inputs.
Each item has `id` and `title`; a connection edge wraps that item as `node`.

The library has Books A, B, C, D in that stable catalog order and an Author
with local ID `1`. Book A also has local ID `1`. Local IDs are unique within a
type, but clients may refetch either type through the root `node` field. A
cursor identifies an item in this fixed catalog order; page results should
keep that order in either pagination direction. The relationship fields expose
both pagination argument pairs and nullable boundary cursors on empty pages.

Application policy: Book A is private to principal `alice`; all other seeded
records are public. An inaccessible object should be treated as unavailable
on every lookup path, including refetch. The `principal` parameter represents
the caller for this policy. The fixture is illustrative Python, with no
database, request context, authorization middleware, or running GraphQL query.

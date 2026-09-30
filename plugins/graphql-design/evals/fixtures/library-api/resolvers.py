"""Small resolver-shaped adapter for static GraphQL contract audits."""

BOOKS = [
    {"id": "1", "title": "A", "owner": "alice", "public": False},
    {"id": "2", "title": "B", "public": True},
    {"id": "3", "title": "C", "public": True},
    {"id": "4", "title": "D", "public": True},
]
AUTHORS = [{"id": "1", "title": "Ada", "public": True}]


def object_id(kind, local_id):
    """Construct the ID exposed by a Book or Author's Node.id field."""
    return str(local_id)


def node(object_id, principal):
    """Look up a Node by its exposed ID for the given caller."""
    for item in BOOKS + AUTHORS:
        if item["id"] == object_id:
            return item
    return None


def connection(items, first=None, after=None, last=None, before=None):
    """Build a connection from ordered relationship items."""
    edges = [
        {"node": item, "cursor": f"cursor:{item['title']}"}
        for item in items
    ]
    if after is not None:
        for index, edge in enumerate(edges):
            if edge["cursor"] == after:
                edges = edges[index + 1 :]
                break
    if before is not None:
        for index, edge in enumerate(edges):
            if edge["cursor"] == before:
                edges = edges[:index]
                break
    if first is not None:
        edges = edges[:first]
    if last is not None:
        edges = edges[-last:] if last else []
        edges.reverse()
    return {
        "edges": edges,
        "pageInfo": {
            "hasNextPage": False,
            "hasPreviousPage": False,
            "startCursor": edges[0]["cursor"] if edges else None,
            "endCursor": edges[-1]["cursor"] if edges else None,
        },
    }

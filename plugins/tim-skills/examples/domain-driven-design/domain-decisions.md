# Original domain decision examples

These synthetic cases illustrate different levels of modeling effort. They are
not examples from *Learning Domain-Driven Design*.

## Catalog label: keep it simple

A community theater's administrator edits a costume category label. The only
rules are that the label is nonempty and unique within one theater. A single
database transaction validates and saves it; the operation has no other
workflow. A transaction script with a uniqueness constraint is sufficient. A
new aggregate, event log, or service would not protect an additional known
invariant. A useful test checks an empty label and a duplicate under concurrent
submissions. If later policy links categories to lending eligibility, revisit
the boundary then.

## Studio admission: model the invariant

A workshop sells at most 12 seats per session. Two customers can request the
last seat at once. A design that reads a displayed seat count and later creates
two paid admissions can violate the promise. The decision boundary is the
admission operation: it must atomically confirm at most one final seat, or hold
capacity while payment settles under a documented expiry policy. A Session
aggregate could express capacity and admission transitions if it maps cleanly
to one transaction; an atomic conditional write could also enforce the same
rule. The choice depends on the actual payment and cancellation rules. Test two
simultaneous final-seat requests and the payment-failure transition.

## Same word, different business meaning

At a seed library, Lending uses “reservation” for a temporary packet hold.
Education uses it for a confirmed class seat. Each context keeps its own
reservation rules and translates only the facts needed for a cross-team view.
A common persistence entity would mix expiration and payment policy. Neither
context boundary implies a separate server.

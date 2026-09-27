# Original event-driven decisions

These synthetic scenarios illustrate choices; they are not book examples.

## A request and a fact serve different owners

At a library, Lending accepts a loan and publishes `LoanAccepted` for a
member portal. It also asks Dispatch to `PrepareCourierPickup`. The latter
has one intended actor, can be declined, and needs an outcome; calling it
`CourierPickupEvent` would not change its request intent. Lending can keep
private domain events for local history while publishing a smaller stable
integration contract containing loan ID and public pickup status. Dispatch
owns pickup feasibility, while Lending owns whether a loan was accepted.

## Send only what the consumer needs

At a food cooperative, Product owns supplier costs and public prices. Search
can accept a delayed index update, so `PublicPriceChanged` carrying product ID,
public price, currency, and version avoids a lookup for every update. A
notification with an API fetch is viable if Search already needs the latest
record and tolerates Product's availability dependency. Checkout, which must
charge the current approved amount, queries Product during authorization or
uses an explicitly coordinated price reservation. Neither consumer needs the
supplier negotiation notes in Product's persistence object.

## A promise can expose hidden coordination

A venue promises a seat only after inventory and payment decisions. If
`SeatRequested` triggers one consumer to reserve capacity and another to
charge, no owner can infer a final result from publication alone. A small
process manager can track pending, reserved, charged, and failed states and
give the customer a truthful intermediate result. A payment reversal may
compensate a charge; an already issued non-refundable ticket may require a
manual remedy. If both decisions fit one local transaction, that simpler
boundary may be preferable to an event chain.

## Change a public contract while old readers live

Billing adds a tax breakdown to an invoice event. The older consumer still
understands amount and currency, and its unknown-field behavior is checked.
Billing can add a compatible field or publish a translated version while the
new consumer adopts it. Contract tests and observed consumer uptake decide
when the old representation can be retired. Renaming a database column does
not itself change the public meaning of an issued invoice.

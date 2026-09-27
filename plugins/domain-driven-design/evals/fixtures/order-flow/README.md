# Order-flow evaluation fixture

Sales accepts an order and records its current destination. Once accepted,
every order must become eligible for fulfillment. Fulfillment must create one
shipment request for each accepted order. If Sales later revises the
destination before shipment, the latest revision for that order must determine
where the shipment goes.

The message broker may retry delivery, reorder messages for the same order,
and fail to accept a publication. Sales and Fulfillment use separate databases.
The supplied Python and JSON files show the proposed flow and wire contract;
they are small audit evidence, not a runnable production service.

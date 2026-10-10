# Integration boundary contrasts

An out-of-process database does not have one permanent dependency role. Ownership and external observation decide whether it is managed.

## Database owned behind the application

Assume the Orders application is the only component allowed to read or write its database. Other clients use the Orders API.

```text
test "placing an order makes it retrievable":
  database = test_database_with_isolated_state()
  api = OrdersApplication(database)

  id = api.place_order(customer = "C-7", item = "P-2")

  assert api.get_order(id).item == "P-2"
```

This is an integration test: it exercises the real out-of-process database and a broader application path. The database is managed because its interaction is hidden behind the application boundary. Assert the observable application result or final state, not a particular SQL statement or repository call. Test isolation still depends on unique data, rollback, cleanup, or a separate database instance; process location alone does not prove interference.

## Database observed by another system

Assume a separately deployed fulfillment service reads new rows directly from the Orders database under a documented schema contract.

```text
test "placing an order publishes the fulfillment record":
  fulfillment_sink = recording_contract_boundary()
  api = OrdersApplication(fulfillment_sink)

  api.place_order(customer = "C-7", item = "P-2")

  verify fulfillment_sink.received(
    order_customer = "C-7",
    product = "P-2",
    status = "ready"
  )
```

The relevant database write is externally observed, so it belongs to an unmanaged boundary from the Orders application's perspective. A mock, spy, contract fixture, or controlled fake endpoint can verify the outgoing contract without coupling the test to unrelated internal persistence details. A separate integration or contract check should establish that the boundary adapter speaks the real protocol.

## Ownership unknown

If repository code shows a database but architecture and consumers are absent, do not assume `managed` from the word database or `unmanaged` from its process boundary.

- If only this application owns and exposes the data, use the managed branch and prefer the real database in integration tests.
- If another owner reads the schema, observes writes, or deploys independently, use the unmanaged branch for the relevant interaction.
- Ask who can access the database directly, who controls schema changes, and what compatibility promise exists.

Until those facts are available, report the dependency as `out of process; managed status unknown`, give both consequences, and keep confidence conditional. Execution time and test-to-test isolation also remain unverified until measured or inspected.

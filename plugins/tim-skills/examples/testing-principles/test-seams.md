# Test seam contrasts

These examples are pseudocode, not framework APIs. The declared contract is: finalizing an invoice applies a ten-percent preferred-customer discount, saves the total, then sends one receipt. Persistence failure propagates and prevents sending. The database is exclusively application-owned; an independent mail provider observes receipt sends.

## Decisions mixed with effects

Before:

```text
finalize(id):
  invoices = SqlInvoices(application_config.database)
  sender = MailClient(application_config.mail)
  invoice = invoices.load(id)
  total = invoice.subtotal
  if invoice.preferred:
    total = total * 90 / 100
  invoices.save_total(id, total)
  sender.send_receipt(invoice.address, total)
```

A pricing test now needs database and mail setup or patches to internal construction. Mocking every call also ties the test to the orchestration sequence without proving persisted state or real client wiring.

After:

```text
invoice_total(invoice):
  if invoice.preferred:
    return invoice.subtotal * 90 / 100
  return invoice.subtotal

InvoiceFinalizer(invoices, sender):
  finalize(id):
    invoice = invoices.load(id)
    total = invoice_total(invoice)
    invoices.save_total(id, total)
    sender.send_receipt(invoice.address, total)

finalize(id):
  finalizer = InvoiceFinalizer(
    SqlInvoices(application_config.database),
    MailClient(application_config.mail))
  finalizer.finalize(id)
```

The public `finalize(id)` contract remains intact. The application configuration can point the real adapters at an isolated database and recording mail endpoint using ordinary deployment settings. Production calls the extracted pricing function; there is no parallel test implementation. Use the repository's monetary representation and rounding contract rather than copying this illustrative arithmetic blindly.

Checks:

- Directly exercise `invoice_total` with preferred and standard invoices, asserting independently specified totals such as 90 and 100 for subtotal 100.
- Call the actual `finalize(id)` entrypoint with real adapters and isolated test configuration. Assert persisted total and one receipt with the promised address and amount. This checks both application integration and production composition.
- Exercise the persistence-failure contract at the application boundary with a controlled failing dependency or practical database failure. Assert propagation and no outgoing receipt. This negative effect assertion protects the stated contract rather than incidental helper calls.

Tests of an injected `InvoiceFinalizer` alone would leave the public entrypoint's wiring unverified. A recording mail endpoint also leaves live-provider compatibility unverified. None of these illustrative checks has been executed.

## No seam needed

A checkout already accepts basket data and uses real deterministic `DiscountPolicy` and `MoneyRules` collaborators. Assert the resulting total through checkout. Introducing `IDiscountPolicy`, `IMoneyRules`, and mocks for every helper would create more coupling without controlling a difficult input or effect.

Likewise, making a private cached subtotal public merely to assert it would expose an implementation detail. Observe the receipt total or other existing client-visible result instead.

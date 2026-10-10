# Test-double contrasts

Classify a double by how the test uses it, not by its class name or library.

## Repository query: stub input, assert result

```text
test "report shows the active-customer count":
  customer_repository.when_count_active_returns(12)
  report = ReportService(customer_repository).create()

  assert report.active_customers == 12
```

The repository double is a stub: its query supplies input. The assertion protects the report result.

```text
test "report asks repository once":
  customer_repository.when_count_active_returns(12)
  ReportService(customer_repository).create()

  verify customer_repository.count_active called exactly once
```

This verification observes how the input was obtained. At the report boundary, one query, two queries, or a preloaded value can be equivalent. The call count is an implementation detail and makes the test more fragile without protecting a distinct result.

If repository calls are metered or limited by an explicit client contract, call count may be observable. Establish that constraint from code, documentation, or user intent; otherwise keep the conclusion conditional rather than assuming a performance requirement.

## Outgoing notification: legitimate mock

```text
test "accepted invitation notifies the invited address":
  email_gateway = recording_email_gateway()
  invitations = InvitationService(email_gateway)

  invitations.accept(invitation_for("lee@example.test"))

  verify email_gateway.sent(
    template = "invitation-accepted",
    recipient = "lee@example.test"
  )
```

The gateway double is a mock because the test examines an outgoing side effect. When the email provider or recipient is outside the system boundary, sending the correct notification is externally observable behavior. Verifying that interaction protects a contract while avoiding a live external send.

Do not extend this verification to internal steps such as `TemplateSelector.choose` or `AddressFormatter.normalize`; those are replaceable collaborations inside the boundary.

If the notification is only an internal queue record consumed exclusively by the same deployable system, it may be a managed implementation detail. Determine who owns and observes the queue. With unknown consumers, state: unmanaged implies the interaction is a valid mock target; managed implies assert the resulting system behavior with the real dependency in an integration test when practical.

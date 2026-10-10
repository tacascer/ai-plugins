# Logging test decisions

These original scenarios apply the articles’ general principles; they are not examples reproduced from the book.

## Incidental diagnostic wording

`Checkout.total()` returns 90 and writes “discount applied” to an injected logger. No consumer depends on that message. A test checks both 90 and the exact message.

Keep the output assertion and remove the incidental wording check. Use a no-op logger if the test otherwise writes files. The original assertions are mixed output/communication; removing the diagnostic assertion does not authorize deleting the production log.

## Required support event

A support tool consumes an account-change event with `account_id`, `old_status`, and `new_status`. The contract requires one event per actual transition and none for an unchanged status. Its transport is an externally observed unmanaged boundary.

Exercise the transition through the application boundary and record the outgoing event. Check the specified fields and emission conditions, including the unchanged-status case. Internal helper calls and human-readable wording are not assertions unless the consumer contract requires them. An in-memory recorder checks emission intent, not actual transport delivery; use a proportionate adapter or integration check for that separate requirement.

## Hidden file logger

A service constructs its file logger internally. A proposed test adds `isTestEnvironment` to suppress writes.

Inject the existing logging boundary, or extract the smallest suitable one, and supply a no-op implementation for tests unrelated to logging. Configure the real logger through normal production composition. Do not replace a delivery-contract test with a no-op, and do not claim that injection verifies real file persistence.

## Unknown consumer

A test only verifies `logger.info` was called. There is no information about readers or log-processing tools.

Describe the assertion as communication-based and the recorder as a spy verifying an outgoing interaction. Whether it protects observable behavior remains unresolved. Find the consumer and contract; keep both the required-event and incidental-diagnostic branches explicit. Report execution speed as unverified without a measurement.

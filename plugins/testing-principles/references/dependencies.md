# Dependencies and test doubles

Dependency decisions require four separate facts: boundary ownership, sharing between tests, process location, and the double's role.

## Describe the dependency

| Question | Classification consequence |
| --- | --- |
| Can tests mutate the same instance or resource and affect one another? | Yes means shared; otherwise private. Confirm fixture lifecycle and cleanup rather than inferring from production singleton use. |
| Does it run outside the application process? | Yes means out of process. Process location does not by itself decide scope or whether to substitute it. |
| Does the application team control the out-of-process dependency and hide it behind the application boundary? | Yes supports managed. Use a real instance in integration tests when practical and assert the resulting behavior or state. |
| Can another application or owner directly observe or depend on the interaction? | Yes supports unmanaged. The outgoing contract may be observable behavior suitable for a mock, spy, fake endpoint, or contract check. |

A database is often managed, but not automatically. A database read by reporting jobs, another service, customer tooling, or a separately deployed owner has external observers. Its relevant writes may be part of the system contract. If access and ownership are unknown, report both branches:

- if only this application controls and exposes the data, treat the database as managed;
- if external clients observe its schema or writes directly, treat the relevant boundary as unmanaged;
- resolve the branch by finding deployment ownership, direct consumers, and compatibility promises.

## Choose the double by role

- A **stub** supplies input to the system under test, such as a repository query result, clock value, or read-only service response. Assert the resulting behavior, not how the input was requested.
- A **mock** records or verifies an outgoing interaction that produces a side effect. Use it when that interaction is observable at the chosen boundary, such as a promised notification to an external recipient.
- A **spy** records real or fake interactions for later examination. Its value still depends on whether the recorded interaction is observable.
- A **fake** is a working simplified implementation. Treat it as a stub or mock according to how the test uses it.

A mocking library can create either a stub or a mock. Naming, framework types, and setup syntax do not determine the role.

## Boundary rule

Communications among components inside the declared system are replaceable implementation steps. Prefer exercising those collaborators together and asserting the boundary result. Communications that cross to an independently observed unmanaged system may form a contract worth verifying.

There are legitimate exceptions driven by environment constraints. If a real managed dependency is unavailable, state that constraint and what fidelity the substitute loses. Do not relabel the result as full integration evidence.

See [classification](classification.md) for the complete dimensions and [integration examples](../examples/integration-boundaries.md) for the database branches.

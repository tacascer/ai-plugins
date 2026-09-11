# Testing framework

Use this framework to describe tests and judge their value without confusing the two tasks.

## Orientation

1. Establish the behavior and the system boundary before naming the test type.
2. Classify the independent dimensions in [classification](classification.md).
3. Identify dependency roles with [dependencies](dependencies.md).
4. Assess value with the evidence questions in [quality](quality.md).
5. Communicate findings with [reporting](reporting.md).

The examples show these decisions in context: [behavior boundaries](../examples/behavior-boundaries.md), [test doubles](../examples/test-doubles.md), and [integration boundaries](../examples/integration-boundaries.md).

## Scope and value answer different questions

Scope describes what the test crosses and whether it meets the unit-test criteria. Value describes how well it protects useful behavior at an acceptable cost. Do not use `unit`, `integration`, or `end-to-end` as praise or criticism. A fast unit test can assert an internal cache and be brittle. A database integration test can be the clearest protection for a valuable behavior.

Likewise, assertion style does not determine scope. Output-, state-, and communication-based assertions can appear in either unit or integration tests.

## Classical and London definitions

Both schools expect a unit test to exercise a small unit, run quickly, and be isolated. They disagree about isolation and the size of that unit:

- The classical school isolates tests from one another. A unit is a cohesive behavior and may involve several collaborating classes. Private in-process collaborators normally remain real.
- The London school isolates the system under test from its collaborators, commonly treating a class as the unit and replacing mutable collaborators with test doubles.

This curriculum favors the classical interpretation for scope and authoring decisions. It then applies the more precise managed/unmanaged distinction to out-of-process dependencies. That preference does not make every classical-style test valuable, and the presence of a mocking library does not prove that a test follows the London school.

## Establish the boundary

Name the client whose goal defines the behavior and the components included in the system under test. Read production consumers, entry points, fixtures, and architecture documentation. A public member is observable only when it serves that client's goal or exposes an effect the client can observe. The same call may be behavior at a narrow boundary and an implementation detail at a wider boundary.

If evidence supports more than one boundary, state which one you chose. If the architecture does not establish ownership or external observers, report conditional alternatives rather than inventing an answer.

See [sources](sources.md) for source attribution and the boundary between source-backed principles and plugin workflow conventions.

# Test classification

Classify each dimension independently and cite the evidence used. Filenames, annotations, assertion counts, Docker use, and mocking-library imports are clues only.

## 1. Scope

A unit test:

- verifies one cohesive unit of behavior, which may span several classes;
- runs quickly enough to support a short feedback loop; and
- is isolated from other tests, so order, parallelism, or another test's state cannot change its result.

A test that fails one or more of these criteria is an integration test. An end-to-end test is an integration test that exercises the application through a broad externally meaningful path. Do not define scope solely by process location: a fresh out-of-process dependency may avoid test-to-test interference, yet speed and behavior size still need evidence.

Record speed as `verified` only from execution evidence. Without timings or an observed run, use `unverified`. If test isolation depends on runner configuration, fixtures, or cleanup that was not inspected, make the scope conclusion conditional.

## Choosing coverage before tests exist

Use these criteria prospectively when designing coverage. Call a check an intended unit test when it exercises cohesive behavior with planned test isolation and a short feedback loop; do not claim measured speed before execution. Choose integration coverage when the behavior requires components and infrastructure working together, such as orchestration with real owned persistence. A mock does not make that whole test a unit test.

Add an end-to-end path when a broad client entrypoint protects a distinct risk, such as routing and composition omitted by narrower checks. State its actual extent and substituted external systems; do not imply live-provider compatibility. Repository labels such as component or contract can supplement this explanation. Neither a fixed pyramid ratio nor one test of every type is required.

## 2. Assertion style

- **Output-based:** compares returned or emitted values with expected results.
- **State-based:** examines a state change after the action.
- **Communication-based:** examines an outgoing interaction with a dependency.
- **Mixed:** uses more than one of these styles; name each material style.

The library used to create a double does not determine the style. A configured query response is stub input; verifying an outgoing command is communication-based.

## 3. Dependency characteristics

Record each material dependency along separate axes:

- **Shared/private:** shared dependencies let tests affect one another through common mutable state. Sharing between production classes does not make a dependency shared for testing.
- **In/out of process:** identify whether the dependency executes within the application process or is reached across a process boundary.
- **Managed/unmanaged:** for an out-of-process dependency, determine whether the application team controls it and hides it from external observers. See [dependencies](dependencies.md).

Use `unknown` where fixtures, deployment ownership, or consumers are unavailable. Follow it with the conditional outcomes and the missing fact.

## 4. Assertion target

Classify each important assertion as observable behavior or an implementation detail relative to the declared boundary. Outputs, public state, and outgoing interactions are not automatically observable. Ask whether the target has an immediate connection to the client's goal or is an externally visible effect the system promises to preserve.

## 5. Quality pillars

Record qualitative findings for protection against regressions, resistance to refactoring, feedback speed, and maintainability. These are value dimensions, not another scope label. Use [quality](quality.md) and distinguish demonstrated results from inferences.

Extra repository labels such as contract, component, property-based, smoke, or acceptance test may be included as extensions. Keep them separate from this classification unless the repository defines an exact mapping.

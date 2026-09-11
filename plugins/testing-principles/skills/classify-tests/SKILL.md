---
name: classify-tests
description: Use when asked to classify tests or explain their scope, assertion style, isolation, or dependency roles.
---

# Classify Tests

Classify tests from behavior and evidence. Scope, assertion style, dependency roles, assertion target, and quality are independent dimensions.

## Procedure

1. Discover repository terminology, test commands, fixtures, and local conventions. Preserve useful local labels without assuming their meaning.
2. Read the test, its setup and teardown, the production behavior it exercises, and relevant consumers or architecture notes.
3. State the system boundary and the client whose goal defines observable behavior. When unclear, inspect callers and documentation; keep unresolved alternatives explicit.
4. Read [classification](../../references/classification.md), [dependencies](../../references/dependencies.md), and [quality](../../references/quality.md). Classify and assess:
   - unit, integration, or end-to-end integration from behavior size, speed, and test-to-test isolation;
   - output-, state-, communication-based, or mixed assertions;
   - material dependencies as shared/private, in/out of process, and managed/unmanaged when applicable;
   - assertion targets as observable behavior or implementation details at the stated boundary; and
   - protection against regressions, resistance to refactoring, feedback speed, and maintainability with qualitative evidence. Distinguish demonstrated results from inferred or unresolved findings, and report speed as measured only when execution evidence exists.
5. Report evidence, uncertainty, and missing facts using [reporting](../../references/reporting.md). Mark speed unverified without execution evidence and use conditional conclusions when ownership or isolation is unknown.

Do not infer scope from filenames, annotations, Docker, mock libraries, class count, or assertion count. Do not use a scope label as a quality score. Consult [behavior-boundary examples](../../examples/behavior-boundaries.md) when a unit spans classes.

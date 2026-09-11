# AI Plugins collection and testing-principles design

Date: 2026-09-11
Status: Written specification approved by the user on 2026-09-11
Repository: https://github.com/tacascer/ai-plugins

## Purpose

Create a repository of independently installable plugins for Codex and Claude Code.
The first plugin, `testing-principles`, teaches agents to write, classify, and audit
tests using Vladimir Khorikov's *Unit Testing: Principles, Practices, and Patterns*.
Authoring and auditing have equal priority. Instruction is language-agnostic and
selected automatically when relevant, with explicit invocation also available.

## Agreed scope

- Maintain one shared curriculum and workflow implementation for both agents.
- Package each plugin independently under `plugins/<name>/`.
- Give each plugin its own name, semantic version, documentation, and evaluations.
- Keep references and examples inside their plugin's installable directory.
- Support additional plugins through catalog registration and generic validation.
- Activate testing workflows based on user intent and task context.
- Provide evidence and uncertainty, not an invented numerical conformance score.
- Adapt to existing repository tools and conventions without requiring a language.

NixOS/Home Manager installation is a later integration task. This repository does
not require a NixOS rebuild, modify agent installations, or change user settings.
The initial implementation contains skills and reference material; an MCP server,
mandatory hooks, static-analysis engine, and model-training pipeline are outside
this version's scope.

## Repository structure

```text
ai-plugins/
  README.md
  AGENTS.md
  CONTRIBUTING.md
  docs/specs/
  docs/plans/
  catalogs/plugins.json
  scripts/
  .github/workflows/
  .agents/plugins/marketplace.json
  .claude-plugin/marketplace.json
  plugins/testing-principles/
    README.md
    .codex-plugin/plugin.json
    .claude-plugin/plugin.json
    skills/classify-tests/SKILL.md
    skills/audit-tests/SKILL.md
    skills/write-tests/SKILL.md
    references/
    examples/
    evals/
```

`catalogs/plugins.json` is the platform-neutral inventory. Each entry identifies
an installable plugin by name and repository-relative path. Platform manifests
carry matching names and versions. Platform marketplace files are generated from
the inventory and plugin metadata, committed for discovery, and checked for drift.
The implementation must verify each platform's current marketplace schema and
source-path resolution rather than assume that their schemas are interchangeable.

Only metadata and catalog generation are platform-specific. Skill bodies and
curriculum files are shared. Bundles must contain all referenced resources; no
symlinks or references outside the plugin directory are required to use a plugin.
Repository development scripts and evaluations need not load into agent context.

Repository instructions cover worktree use, conventional commits, contribution
steps, and verification. Adding a second plugin requires a self-contained plugin
directory and inventory entry, followed by regeneration and validation. Validators
must discover plugins from the inventory, not hardcode `testing-principles`.

## Testing framework

Classification and quality are separate judgments. A unit test can be brittle;
an integration test can be valuable. Scope labels are not quality rankings.

The curriculum states the classical and London definitions and uses Khorikov's
classical preference for recommendations. A unit of behavior can span multiple
classes. Tests are not classified from filenames, annotations, assertion counts,
or the mere presence of a mocking library.

Record these independent dimensions:

1. Scope: unit or integration, with end-to-end as a subset of integration.
2. Assertion style: output-based, state-based, communication-based, or mixed.
3. Dependency characteristics: shared/private, in/out of process, and
   managed/unmanaged for out-of-process dependencies. Shared describes sharing
   between tests, not simply use by multiple production classes.
4. Assertion target: observable behavior versus implementation details, relative
   to an explicitly stated system boundary.
5. Quality pillars: protection against regressions, resistance to refactoring,
   fast feedback, and maintainability.

For unit scope, examine behavior size, execution speed, and isolation between
tests. When execution evidence is absent, mark speed as unverified. Do not equate
process boundaries, Docker use, or dependency isolation alone with the complete
unit-test definition.

Teach that a mock library can create different kinds of test doubles. Stubs supply
inputs; mocks verify outgoing interactions. Avoid asserting interactions with
stubs and intra-system implementation details. In integration tests, use real
managed dependencies and mock unmanaged dependencies where appropriate. Determine
ownership and external observers before deciding whether a dependency is managed;
a database is not automatically managed, nor is every external call a suitable
mock assertion.

Prefer tests of meaningful behavior. Do not mandate a coverage percentage or
one test per method. When a boundary is unclear, inspect production consumers,
fixtures, and documentation; if still unresolved, state the conditional conclusion
and the missing fact. Additional labels such as contract or property-based testing
may supplement the framework but must be identified as extensions, not attributed
to the book without support.

## Skills and activation

### classify-tests

A reusable procedure and explicit entry point for scope, style, dependencies, and
assertion-target classification. Reads the shared rubric and returns evidence.
Authoring and auditing instructions reference the same procedure; they must not
assume that either platform automatically invokes another skill on their behalf.

### audit-tests

Activates for reviewing tests, evaluating their quality, assessing coverage
adequacy, or classifying an existing suite. Reads production behavior, test setup,
and dependencies before judging the test. Reports material findings first and
classifies only the requested or affected scope. Read-only review requests remain
read-only; implementation follows the user's requested action and authorization.

### write-tests

Activates when creating or modifying tests, including regression tests during bug
fixes. Establishes intended behavior and boundaries, selects test scope and
dependency treatment, implements idiomatic tests, and runs relevant checks.
It applies the audit rubric before completion. A bug regression test should
exercise the actual failure rather than mirror the fix's implementation.

### Selection and communication

Descriptions advertise distinct intent triggers. When both workflows apply, use
writing as the primary workflow for changes and auditing as its quality check.
Classification supports both. Explicit user requests can select any workflow.

For small changes, apply the rubric quietly and report material decisions and
verification. For an explicit audit, provide fuller evidence. Do not launch a
repository-wide audit for an unrelated edit or automatically run tests whose
execution is outside user authorization or environment permissions.

Automatic skill selection is a behavior to evaluate on both platforms, not a
claim of deterministic enforcement. Initially rely on skill discovery and
well-scoped descriptions. Evaluate missed and irrelevant activations before
considering stronger mechanisms.

## Evidence and outputs

A full audit finding contains:

- Test identifier and file/line evidence.
- Behavior under test and declared system boundary.
- Scope, assertion styles, dependency roles, and classification reasoning.
- Quality-pillar findings and any unmeasured runtime characteristics.
- Concrete recommended action: retain, improve, relocate, consolidate, or remove
  only when evidence supports preserving useful coverage.
- Confidence expressed as supported, conditional, or unresolved, with missing facts.

The authoring workflow explains the behavior, selected scope, dependency choices,
and verification results. It must distinguish commands actually run from proposed
commands and tests observed passing from tests merely expected to pass.

Use concise qualitative assessments. File evidence supports implementation facts;
architecture documents and user clarification support ownership assumptions.
Do not invent business requirements when production code and intent disagree.

## Curriculum and provenance

Use original concise explanations, pseudocode examples, and paired counterexamples.
Provide source links and chapter/topic attribution. Do not redistribute the book
or present the plugin as author-endorsed. Keep source-backed principles distinct
from plugin workflow conventions and language-specific adaptations.

Core references:

- Book excerpt and contents: https://enterprisecraftsmanship.com/files/Unit-Testing-Chapter-1-Excerpt.pdf
- Dependency taxonomy: https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/
- Mocking guidance: https://enterprisecraftsmanship.com/posts/when-to-mock/
- Codex packaging: https://developers.openai.com/plugins/build/plugins
- Claude Code packaging: https://code.claude.com/docs/en/plugins-reference

The available excerpt does not contain every chapter. Verify detailed rules
against available author material or supplied book passages before claiming exact
book conformance; keep any unverified extension explicit.

## Validation and evaluations

Structural validation checks plugin and marketplace manifests, matching plugin
identities and versions, skill frontmatter, catalog source paths, resource
containment, and missing references. Generated catalogs must be reproducible.
Packaging smoke checks load the plugin in each available supported agent and
record the tested versions. Missing platform access is reported as unverified.

Curated behavioral scenarios cover authoring and auditing equally. Include:

- A unit of behavior implemented by several collaborating classes.
- A meaningful output assertion and a trivial low-value output assertion.
- State assertions against observable results versus leaked internals.
- Brittle verification of internal collaboration and a legitimate outgoing mock.
- A stub with an inappropriate interaction assertion.
- A real managed database and an externally observed shared database.
- Missing ownership information requiring a conditional classification.
- Mixed assertion styles, unmeasured runtime, and shared test state.
- A bug fix needing a regression test and a testing task using unfamiliar syntax.
- An unrelated documentation edit that should not activate testing workflows.
- Explicit invocation and overlap with a second, disposable fixture plugin.

Each scenario specifies input context, expected reasoning, forbidden conclusions,
and expected activation. Evaluate outputs semantically, not by exact prose.
Use original executable fixture repositories for a small subset to demonstrate
that authored tests run and detect an introduced behavioral fault. Pseudocode-only
scenarios are reasoning evaluations, not evidence of runnable authored tests.

Cross-check authoring outputs with the audit workflow, but use independently
curated expectations as the correctness oracle: agreement alone is insufficient.
Record agent version, model, scenario, activation outcome, findings, and failures.
No automated framework certification is claimed.

## Completion criteria

1. Both agents can discover and load the first plugin from the collection.
2. Both workflows use the same language-agnostic curriculum.
3. Expected classifications and uncertainties hold on the curated cases.
4. Authoring demonstrations produce runnable tests that detect targeted faults.
5. Automatic activation and non-activation results are recorded for both agents.
6. A disposable second plugin proves generic catalog and validation behavior.
7. Contribution documentation explains adding and independently versioning plugins.
8. Platform or execution checks that could not run are explicitly documented.

## Delivery sequence

First implement the collection scaffold, catalog generation, and validation.
Then implement curriculum, examples, and the three skills as the first plugin.
Finally run structural checks, platform load checks, and behavioral evaluations;
document installation and contribution steps. Keep changes in a dedicated worktree
with conventional commits. Publishing and installation are separate from local
specification and implementation work.

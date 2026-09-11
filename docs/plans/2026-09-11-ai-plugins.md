# AI Plugins Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Use superpowers:subagent-driven-development only if the user chooses delegation. Steps use checkbox syntax for tracking.

**Goal:** Deliver a multi-plugin collection for Codex and Claude Code with an automatically selected, language-agnostic testing-principles plugin.

**Architecture:** Each plugin is a self-contained directory with shared skills and platform-specific manifests. One inventory generates both platform marketplaces. Deterministic repository checks and curated agent evaluations provide separate evidence of structural correctness and useful behavior.

**Tech Stack:** Markdown, JSON, Python 3.11+ development scripts and unittest, PyYAML for skill frontmatter, GitHub Actions. Skills themselves have no Python or language runtime dependency.

**Spec:** `docs/specs/2026-09-11-ai-plugins-design.md` (approved).

## Global constraints

- Maintain one shared curriculum and workflow implementation for both agents.
- Package each plugin independently under `plugins/<name>/`.
- Give each plugin its own name, semantic version, documentation, and evaluations.
- Keep references and examples inside their plugin's installable directory.
- Support additional plugins through catalog registration and generic validation.
- Activate testing workflows based on user intent and task context.
- Provide evidence and uncertainty, not an invented numerical conformance score.
- Adapt to existing repository tools and conventions without requiring a language.
- Use a dedicated worktree and conventional commits.
- Do not publish, install into the user's managed environment, or modify myNixOS as part of this plan.

Implementation decisions: use marketplace name `tacascer-ai-plugins`, initial plugin version `0.1.0`, and inventory order as display order. Do not assign a redistribution license on the user's behalf; omit optional license metadata until a license is selected. This does not prevent local implementation or evaluation.

## Preparation and evidence

The existing worktree is `/home/tacascer/Projects/ai-plugins-design`, branch `docs/plugin-design`. Reuse its isolation; rename the branch to `feat/plugin-collection` at implementation start if desired. Only the spec and plan currently exist. There is no baseline executable test suite.

Read both documents and relevant skill-authoring/plugin-creator instructions before implementation. Initial observed tools: Codex CLI 0.154.0, Claude Code 2.1.267, Python 3.14.7. These are observed versions, not inferred minimum supported versions.

Packaging sources checked while planning:

- https://developers.openai.com/plugins/build/plugins
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/plugins-reference
- Installed `codex plugin add --help`, `codex plugin marketplace add --help`, `claude plugin validate --help`, and `claude plugin eval --help`.

Claude marketplace relative sources resolve from the repository root containing `.claude-plugin/`, not from that hidden directory. Use `./plugins/<name>` for both marketplace formats. Test actual Codex discovery separately; the Codex plugin-creator reference specifies this source form. Avoid translating one platform's whole manifest into the other's schema.

## File ownership and dependency sequence

1. Collection metadata and catalog generation: `catalogs/`, `scripts/catalogs.py`, plugin manifests, development setup, and `tests/test_catalogs.py`.
2. Curriculum and workflows: the first plugin's `references/`, `examples/`, `skills/`, and README.
3. Structural verification: `scripts/validate.py`, `tests/test_validation.py`, CI, and repository instructions.
4. Behavioral evaluation assets: plugin `evals/` and original executable fixtures.
5. Compatibility, evaluations, installation documentation, and evidence report.

Execute sequentially. Tasks 1 and 3 are repository tooling; tasks 2 and 4 are independently reviewable content. Task 5 verifies their composition.

## Task 1: Collection metadata and reproducible catalogs

**Files:** Create `.gitignore`, `requirements-dev.txt`, `catalogs/plugins.json`, `scripts/__init__.py`, `scripts/catalogs.py`, `tests/test_catalogs.py`, and both marketplace files. Create both plugin manifests under `plugins/testing-principles/`.

**Interfaces:** `render_catalogs(root: Path) -> dict[str, dict]` returns output-relative paths mapped to JSON objects; `sync_catalogs(root: Path, check: bool) -> list[str]` returns errors. Both live in `scripts/catalogs.py`. Validation failures raise `ValueError` internally and produce a concise nonzero CLI result. CLI: `python3 -m scripts.catalogs [--root PATH] [--check]`.

- [ ] Create `.gitignore` entries for `.venv/`, `.worktrees/`, `__pycache__/`, `*.pyc`, and `.eval-runs/`. Add `PyYAML>=6.0.2,<7` to `requirements-dev.txt`. Use a local virtual environment for development dependencies.
- [ ] Write catalog tests using temporary directories with two minimal plugin manifests. Fixture creation uses JSON serialization, not shell interpolation. At minimum exercise output format, inventory ordering, duplicate names, escaping source paths, identity/version mismatch, and check mode refusing to write.

Core test shape:

```python
import json
import tempfile
import unittest
from pathlib import Path
from scripts.catalogs import render_catalogs, sync_catalogs

class CatalogTests(unittest.TestCase):
    def test_two_plugins_keep_order_and_platform_source_shapes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inventory = []
            for name in ('alpha', 'beta'):
                inventory.append({'name': name, 'path': f'plugins/{name}'})
                for platform in ('codex', 'claude'):
                    path = root / f'plugins/{name}/.{platform}-plugin/plugin.json'
                    path.parent.mkdir(parents=True)
                    path.write_text(json.dumps({
                        'name': name, 'version': '0.1.0',
                        'description': f'{name} fixture',
                        'author': {'name': 'tacascer'},
                    }))
            (root / 'catalogs').mkdir()
            (root / 'catalogs/plugins.json').write_text(json.dumps(inventory))
            catalogs = render_catalogs(root)
            codex = catalogs['.agents/plugins/marketplace.json']['plugins']
            claude = catalogs['.claude-plugin/marketplace.json']['plugins']
            self.assertEqual([p['name'] for p in codex], ['alpha', 'beta'])
            self.assertEqual(codex[1]['source'], {
                'source': 'local', 'path': './plugins/beta'})
            self.assertEqual(claude[1]['source'], './plugins/beta')
            self.assertTrue(sync_catalogs(root, check=True))
            self.assertFalse((root / '.agents').exists())
            self.assertEqual(sync_catalogs(root, check=False), [])
            self.assertEqual(sync_catalogs(root, check=True), [])
```

- [ ] Run `python3 -m unittest discover -s tests -p 'test_catalogs.py' -v`; verify failure is caused by missing catalog implementation.
- [ ] Add the inventory:

```json
[{"name":"testing-principles","path":"plugins/testing-principles"}]
```

- [ ] Use the plugin-creator scaffold helper with a repository-local `--path` and without installation or personal-marketplace flags. Retain `.codex-plugin/plugin.json`; customize real metadata and omit unused apps, servers, hooks, icons, and license fields. Create `.claude-plugin/plugin.json` with this shared identity:

```json
{
  "name": "testing-principles",
  "version": "0.1.0",
  "description": "Write, classify, and audit tests using Khorikov's testing principles.",
  "author": {"name": "tacascer"},
  "repository": "https://github.com/tacascer/ai-plugins",
  "skills": "./skills/"
}
```

Codex adds the interface fields required by the installed scaffold validator. Use display name `Testing Principles`, developer name `tacascer`, category `Productivity`, and a short description describing authoring and auditing. Claude receives no Codex interface block.

- [ ] Implement inventory loading with unique lowercase-hyphenated names, exact `plugins/<name>` paths, existing manifests, and matching identity/version checks. Preserve order. Produce Codex entries with `source: {source: local, path: ./plugins/<name>}`, `policy: {installation: AVAILABLE, authentication: ON_INSTALL}`, and `category: Productivity`. Produce Claude entries with name, source string, version, and description. Codex root has name, interface.displayName `tacascer AI Plugins`, and plugins. Claude root has name, owner.name `tacascer`, description `Independent agent workflow plugins for Codex and Claude Code.`, and plugins.
- [ ] Serialize using `json.dumps(payload, indent=2, ensure_ascii=False) + '\n'`. In check mode compare bytes and return a missing/stale error without creating files. Resolve root from `Path(__file__).resolve().parents[1]` unless `--root` is passed; never depend on the caller's working directory.
- [ ] Run tests and generation, then `python3 -m scripts.catalogs --check`. Inspect both outputs and commit as `feat: scaffold multi-plugin catalogs`.

## Task 2: Shared curriculum and three workflow skills

**Files:** Create `plugins/testing-principles/README.md`; references `framework.md`, `classification.md`, `quality.md`, `dependencies.md`, `reporting.md`, `sources.md`; examples `behavior-boundaries.md`, `test-doubles.md`, `integration-boundaries.md`; and all three approved `SKILL.md` files.

**Interfaces:** Skill-relative links use `../../references/<file>.md` and `../../examples/<file>.md`. References link to their sibling references or `../examples/`. Workflows read shared files directly; no runtime skill-to-skill invocation is required.

- [ ] Draft source mapping first. Map scope to chapter 2, pillars to chapter 4, mocks/observable behavior to chapter 5, styles to chapter 6, integration to chapters 8–10. Use the spec's author sources, fetch relevant author material for details, and distinguish verified explanations from chapter headings and original workflow conventions. Do not claim to have read unavailable chapters.
- [ ] Write `framework.md` as an orientation with links, classical/London distinction, and a clear separation of scope from value. Write `classification.md` with the five independent dimensions in the spec, the unit definition's speed/isolation/behavior criteria, and conditional treatment of unknowns.
- [ ] Write `quality.md` with a question and evidence requirement per pillar: meaningful fault detected; behavior-preserving refactor survival; measured feedback; and readability/fixture upkeep. Resist both "mock everything" and "never mock" rules. Write `dependencies.md` with boundary ownership, test sharing, process location, and stub/mock roles.
- [ ] Write `reporting.md` with test identifier, behavior/boundary, classification evidence, qualitative pillar findings, confidence, missing facts, recommended action, and execution evidence. Explicitly distinguish inferred quality from demonstrated results.
- [ ] Write original contrast pairs: a discount behavior spanning classes; a getter assertion versus a pricing boundary assertion; public state versus a leaked cache; a repository-query stub versus inappropriate call verification; a legitimate outgoing notification mock; and managed versus externally observed database use. Make unknown architecture an explicit branch of each relevant decision.
- [ ] Create the skills with these descriptions (single-line YAML strings) and concise procedures:

```yaml
# classify-tests/SKILL.md frontmatter
name: classify-tests
description: Use when asked to classify tests or explain their scope, assertion style, isolation, or dependency roles.
```

```yaml
# audit-tests/SKILL.md frontmatter
name: audit-tests
description: Use when reviewing existing tests, assessing test quality or coverage adequacy, or identifying brittle assertions and inappropriate test doubles.
```

```yaml
# write-tests/SKILL.md frontmatter
name: write-tests
description: Use when creating or modifying tests, including regression tests for a bug fix, and when choosing test scope, assertions, fixtures, or test doubles.
```

Each actual file surrounds frontmatter with `---` delimiters. Do not set `disable-model-invocation: true`. Keep platform-specific invocation syntax out of the shared procedure.

- [ ] Classification procedure: discover repository conventions; read test, setup, production behavior, and consumers; establish boundary; classify; report evidence/uncertainty.
- [ ] Audit procedure: identify requested scope; read classification and quality references; inspect relevant production code; rank material findings; propose precise changes; respect read-only review intent. Avoid treating coverage percentage as adequacy.
- [ ] Authoring procedure: identify requested behavior and known failure; discover tools; read shared classification/dependency/quality guidance; choose scope; write idiomatic tests; run relevant checks; demonstrate a regression when applicable; audit the result. Prefer writing as primary when audit and authoring overlap.
- [ ] Review each example manually against the spec before seeing model outputs. Confirm no language-specific dependency is required to use a skill. Commit as `feat: add shared testing curriculum and workflows`.

## Task 3: Structural validation, CI, and contribution contract

**Files:** Create `scripts/validate.py`, `tests/test_validation.py`, `.github/workflows/validate.yml`, `README.md`, `AGENTS.md`, and `CONTRIBUTING.md`.

**Interfaces:** `validate_repository(root: Path) -> list[str]` in `scripts/validate.py`; CLI `python3 -m scripts.validate [--root PATH]`, exit 0 on success and 1 with path-specific diagnostics otherwise. Reuses `render_catalogs` and `sync_catalogs(check=True)` from task 1.

- [ ] Add negative temporary-copy tests for missing manifest, mismatched versions, duplicate inventory entry, missing referenced Markdown file, resource symlink escape, missing frontmatter name/description, malformed YAML, and stale catalogs. Add a positive test for a second independent fixture plugin. Use the actual repository as a base fixture with `.git` excluded.

Example substantive negative test:

```python
import shutil
import tempfile
import unittest
from pathlib import Path
from scripts.validate import validate_repository

class ValidationTests(unittest.TestCase):
    def test_missing_referenced_resource_is_reported(self):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'repo'
            shutil.copytree(source, root, ignore=shutil.ignore_patterns(
                '.git', '.venv', '.worktrees', '__pycache__', '.eval-runs'))
            missing = root / 'plugins/testing-principles/references/quality.md'
            missing.unlink()
            errors = validate_repository(root)
            self.assertTrue(any('quality.md' in error for error in errors), errors)
```

- [ ] Run validation tests to observe the missing implementation failure.
- [ ] Implement JSON shape checks, strict semantic versions, required metadata, and plugin folder/name agreement. Parse YAML with `yaml.safe_load`; require a mapping and nonempty string name/description. Require skill name to match its directory. Do not require testing-specific skill names for future plugins.
- [ ] For authored Markdown, support inline relative links and ignore HTTPS links and fragment-only links. Resolve decoded relative paths from the containing document, require existence, and require the resolved target to remain inside its plugin. Reject absolute local references, external symlinks, and reference-style local links until a parser supporting them is deliberately added. Document this authored-content convention. Do not claim this checks arbitrary Markdown or remote link availability.
- [ ] Check both generated catalogs for drift. Do not make Python checks pretend to be exhaustive official schema validation; supplement with native platform validation when available.
- [ ] Run `python3 -m unittest discover -s tests -v`, `python3 -m scripts.catalogs --check`, and `python3 -m scripts.validate`.
- [ ] Add CI for push and pull_request with read-only contents permission, checkout, Python 3.11 setup, dev dependency installation, and the three commands above. Resolve official checkout/setup-python releases during implementation and pin immutable action commits with version comments. Do not introduce model credentials or paid evals into normal CI.
- [ ] Document local setup, checks, worktree requirement, conventional commits, contribution flow, identity/version matching, regeneration, and independent plugin version changes. A plugin release changes only that plugin's manifests and regenerated catalog metadata. A catalog-format change requires reviewing all entries.
- [ ] Commit as `feat: validate plugin packaging and catalog consistency`.

## Task 4: Balanced behavioral cases and executable fixtures

**Files:** Create `plugins/testing-principles/evals/README.md`, `evals/cases.json`, `evals/result.schema.json`, `evals/fixtures/python-cart/cart.py`, `evals/fixtures/python-cart/README.md`, `evals/fixtures/js-notifier/notifier.mjs`, and `evals/fixtures/js-notifier/README.md`. All these paths after the first are relative to the first plugin.

**Interfaces:** Cases are an array with `id`, `mode`, `prompt`, `context`, `expected_activation`, `required_findings`, and `forbidden_findings`. Mode is `audit`, `write`, `classify`, or `unrelated`. Results record case id, platform/version, model, timestamp, observed activation, evidence, semantic verdict, and unavailable checks. Keep grader expectations separate from model-visible prompts/context.

- [ ] Author six paired audit/write contexts: multi-class pricing behavior, observable account state, stub query/internal interaction, outgoing notification contract, managed database integration, and unknown database ownership. Give each pair the same domain facts. This supplies 12 equally weighted authoring/auditing cases.
- [ ] Add explicit classification, mixed assertions/unmeasured runtime, shared-state pollution, unfamiliar-language syntax, unrelated documentation, and overlap with an independent fixture plugin. Include both implicit requests and explicit invocation, recording them separately.
- [ ] Use this complete case pattern:

```json
{
  "id": "audit-stub-interaction",
  "mode": "audit",
  "prompt": "Review this test for brittleness.",
  "context": "Checkout asks Catalog for a price, then returns a total. Catalog is an internal query interface. The test supplies price 10, checks total 10, and asserts Catalog.lookup was called exactly once. Lookup call count is not part of the public contract. Runtime is not supplied.",
  "expected_activation": ["audit-tests"],
  "required_findings": ["The supplied lookup result acts as a stub", "Exact lookup count couples the test to an internal query", "Retain the observable total assertion", "Execution speed is unverified"],
  "forbidden_findings": ["All mocks must be deleted", "One class is required per unit test", "The test was measured fast"]
}
```

- [ ] Define semantic outcomes `pass`, `fail`, `unverified`; observed activation `yes`, `no`, `unknown`; require explanatory evidence for each. Numerical aggregation of case outcomes is optional evaluation accounting, never a test-conformance score. Record baseline/no-plugin observations separately when collected.
- [ ] Build the Python fixture with the deliberately incorrect free-shipping boundary:

```python
# cart.py: requirement is free shipping at subtotal >= 50.
def total(subtotal):
    shipping = 0 if subtotal > 50 else 5
    return subtotal + shipping
```

Ask the authoring workflow to test/fix the boundary using standard-library unittest. Keep its expected oracle outside the prompt: total(49) == 54, total(50) == 50, total(51) == 51. Run authored tests before and after correction in a disposable copy; require the boundary test to fail on the original and pass on the correction.

- [ ] Build a second original fixture with an externally visible notification contract:

```javascript
// notifier.mjs: requirement is one welcome message for a newly registered user.
export function welcome(address, sender) {
  sender.send(address, 'Welcome');
  sender.send(address, 'Welcome');
}
```

Ask for tests with Node's built-in test runner and a fix. An assertion on outgoing message count is appropriate here because exactly one message is an explicit external requirement. Require tests to expose the duplicate and survive renaming an internal local variable after correction.

- [ ] Document how to copy fixtures into `.eval-runs/`, prevent expected answers from being exposed, run tests, capture transcripts, and review findings against independently authored oracles. If a runtime is absent, record that fixture unverified rather than installing it globally.
- [ ] Review case balance and expected principles against the source map. Commit as `test: add balanced testing workflow evaluations`.

## Task 5: Platform checks, evaluation evidence, and user documentation

**Files:** Create `docs/verification/2026-09-11-initial.md`; finalize both READMEs and CONTRIBUTING. Store sanitized durable evaluation summaries in the report; retain raw transcripts locally under `.eval-runs/`.

**Interfaces:** Uses both platform catalogs, the three skills, cases from task 4, and the standard structural CLI from task 3. Report supports `passed`, `failed`, and `unverified` separately for structural, discovery, activation, reasoning, and executable-test evidence.

- [ ] Run the complete structural check set and native Claude validation:

```bash
python3 -m unittest discover -s tests -v
python3 -m scripts.catalogs --check
python3 -m scripts.validate
claude plugin validate --strict .
claude plugin validate --strict plugins/testing-principles
```

Also run the available Codex plugin-creator validator against the first plugin; report its local tool version/path as evidence, not as a portable repository dependency.

- [ ] Check current CLI help for temporary plugin loading or isolated configuration support before running discovery/evals. Prefer Claude `--plugin-dir` with a disposable project. For Codex, use a supported isolated configuration or an already authorized evaluation environment. Do not overwrite HOME, home, or CODEX_HOME, copy credentials, alter the user's managed installation, or substitute reading skill text into a prompt for a discovery check. If isolation is unavailable, complete unaffected checks and record installation/discovery as unverified.
- [ ] For each available agent, start fresh cases with normal discovery and model-visible inputs only. Record which skill actually loaded using tool events when available; reasoning resembling the rubric alone does not prove activation. Keep explicit invocation and implicit selection results distinct. Use each environment's configured model, record its identifier, and do not invent a cross-platform model equivalence.
- [ ] Run each initial case once per platform and record outcomes as an initial sample, not a reliability estimate. Repeat only failed or ambiguous cases after correcting content. Cross-review authored tests with audit, then compare to the independent oracle. Run executable fixtures and record commands, failures before correction, passes after correction, and the behavior-preserving refactor check.
- [ ] If native Claude eval is used, include `--no-publish` to keep reports local. The local CLI exposes model-backed evaluation and may publish by default. Do not run evaluation when it would require unauthorized installation, tool grants, or credential changes; identify the exact unavailable check.
- [ ] Build a disposable second plugin named `fixture-docs` with one skill triggered only by release-note editing. Add it to a temporary collection copy, regenerate catalogs, validate, and where possible repeat testing and unrelated prompts with both installed. Do not add this fixture plugin to the production catalog. Record structural extensibility and selection interference as separate outcomes.
- [ ] Document local and future remote installation commands, clearly marking remote commands usable only after publication:

```bash
codex plugin marketplace add tacascer/ai-plugins
codex plugin add testing-principles@tacascer-ai-plugins
claude plugin marketplace add tacascer/ai-plugins
claude plugin install testing-principles@tacascer-ai-plugins
```

Provide local-source alternatives using the repository path and tested temporary-loading steps. Explain automatic activation, explicit invocation per platform, supported/tested versions, adding plugins, and updating both version fields. Do not assert installation occurred merely because commands are documented.

- [ ] Record all unavailable checks and remaining issues. A clean structural run cannot satisfy an unperformed model evaluation. If either platform cannot be exercised, describe the deliverable as implemented with that validation outstanding; do not claim all completion criteria passed.
- [ ] Run `git diff --check` and the structural suite after final changes. Review the full diff against the spec. Commit as `docs: document plugin usage and verification results`.

## Completion mapping and handoff

| Spec criterion | Task/evidence |
| --- | --- |
| Discovery/load on both agents | Task 5 native discovery report |
| Shared language-agnostic curriculum | Task 2 shared resources and workflows |
| Correct classifications and uncertainty | Tasks 4–5 independently graded cases |
| Runnable tests detect targeted faults | Tasks 4–5 executable fixture transcripts |
| Activation and non-activation recorded | Task 5 fresh-case evidence |
| A second plugin proves extensibility | Tasks 1, 3, and 5 temporary fixture |
| Independent versions/contribution guidance | Tasks 1, 3, and 5 documentation |
| Unavailable checks explicit | Task 5 verification report |

Finish with local branch/commit, concise changes, checks actually run, and remaining
verification. Publishing, pushing, and NixOS/Home Manager integration are separate
from this implementation plan. Keep the working tree available for review.

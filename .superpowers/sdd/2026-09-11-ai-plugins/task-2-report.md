# Task 2 report: Shared testing curriculum and workflows

## Status

Implemented the shared curriculum, original contrast examples, and the `classify-tests`, `audit-tests`, and `write-tests` skills on branch `docs/plugin-design`.

Commit message: `feat: add shared testing curriculum and workflows`

## Delivered

- Added the plugin README and six linked curriculum references covering orientation, five-dimensional classification, four quality pillars, dependency roles, evidence-based reporting, and provenance.
- Added three language-agnostic example sets covering all required contrasts: multi-class discount behavior, trivial getter versus pricing behavior, observable state versus leaked cache, repository query stub versus call verification, legitimate notification mock, and managed versus externally observed database use.
- Added the three approved skill entry points with the exact requested descriptions and skill-relative links confined to the plugin bundle.
- Kept scope classification separate from quality assessment and kept dependency test sharing, process location, and managed ownership as independent decisions.

## Source mapping and verification

The source map was drafted before the rest of the curriculum. It maps:

- scope and the classical/London distinction to chapter 2;
- the four pillars to chapter 4;
- mocks, stubs, and observable behavior to chapter 5;
- output-, state-, and communication-based styles to chapter 6; and
- integration tests, managed dependencies, mocks, and databases to chapters 8–10.

The following author-hosted sources were opened and checked during implementation:

- `https://enterprisecraftsmanship.com/files/Unit-Testing-Chapter-1-Excerpt.pdf`
- `https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/`
- `https://enterprisecraftsmanship.com/posts/when-to-mock/`
- `https://enterprisecraftsmanship.com/posts/how-to-assert-database-state/`
- `https://enterprisecraftsmanship.com/posts/unit-test-value-proposition/`
- `https://enterprisecraftsmanship.com/posts/styles-of-unit-testing/`
- `https://enterprisecraftsmanship.com/posts/pragmatic-unit-testing/`
- `https://enterprisecraftsmanship.com/posts/pragmatic-integration-testing/`

The PDF is a 41-page excerpt containing chapter 1 and the full table of contents. It confirms the requested chapter and section headings but does not contain chapters 2–11. `references/sources.md` states this limit and does not claim line-by-line verification of unavailable chapters. Detailed explanations come from the available author articles and are paraphrased in original prose. The report layout, confidence vocabulary, five-dimension record, and conditional branches are identified as plugin workflow conventions.

## Manual example review

Each example was reviewed against the approved spec before model evaluation:

- `behavior-boundaries.md` treats a discount behavior spanning three classes as a possible classical unit and separately branches when hidden shared or remote state changes the classification. It contrasts a trivial getter assertion with a meaningful pricing result and public domain state with a leaked cache.
- `test-doubles.md` treats a repository query as stub input and its call-count verification as inappropriate unless an explicit metering contract exists. It treats an outgoing email as a legitimate mock target when externally observable and branches on unknown queue ownership.
- `integration-boundaries.md` uses a real managed application database in an integration path, contrasts it with a database write observed by a separately deployed system, and leaves unknown ownership conditional on direct consumers, schema control, and compatibility promises.

The pseudocode requires no language, test framework, mock library, database product, or runtime-specific invocation syntax.

## Validation

All three skills passed the skill-creator validator:

```text
$ .venv/bin/python /home/tacascer/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/testing-principles/skills/classify-tests
Skill is valid!

$ .venv/bin/python /home/tacascer/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/testing-principles/skills/audit-tests
Skill is valid!

$ .venv/bin/python /home/tacascer/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/testing-principles/skills/write-tests
Skill is valid!
```

Plugin and catalog validation passed:

```text
$ .venv/bin/python /home/tacascer/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/testing-principles
Plugin validation passed: /home/tacascer/Projects/ai-plugins-design/plugins/testing-principles

$ .venv/bin/python -m scripts.catalogs --check
[exit 0]
```

Repository tests initially could not create temporary directories in the read-only sandbox. The authorized rerun passed:

```text
$ .venv/bin/python -m unittest discover -s tests -v
Ran 10 tests in 0.045s
OK
```

Additional local checks used `.venv/bin/python` and PyYAML where applicable:

```text
checked 40 internal Markdown links
validated 3 exact skill frontmatters with PyYAML
validated 13 required Task 2 files
```

The exact descriptions match the approved brief, each frontmatter block has `---` delimiters, and no skill sets `disable-model-invocation`. A scan found no platform-specific invocation syntax or language-specific testing framework in the shared procedures.

## Requirement review

- `framework.md` links the curriculum and distinguishes classical from London isolation, scope from value, and public syntax from behavior at a declared boundary.
- `classification.md` records all five independent dimensions and requires behavior size, speed, and test-to-test isolation for unit scope. Missing runtime evidence leaves speed unverified.
- `quality.md` asks an evidence question for every pillar and distinguishes demonstrated, inferred, and unresolved results. Coverage percentages do not stand in for adequacy.
- `dependencies.md` separates ownership, test sharing, process location, and double role. It rejects both universal mock and universal no-mock rules.
- `reporting.md` includes identifier, behavior and boundary, classification evidence, qualitative pillar findings, confidence, missing facts, action, and execution evidence.
- Each workflow reads the shared files directly and does not require runtime skill-to-skill invocation. Authoring is primary when modification and audit overlap.

## Deferred evaluation and concerns

No live model baseline or forward evaluation was run. The task brief assigns behavioral and activation evaluation to Task 5 and explicitly avoids duplicate live evaluations here. Structural and manual checks are complete; model compliance, automatic activation, and platform load behavior remain intentionally unverified until Task 5.

## Review fix

Review found that `classify-tests` described five independent dimensions but its procedure enumerated only four and did not load the shared quality rubric. The procedure now reads `quality.md` and explicitly assesses protection against regressions, resistance to refactoring, feedback speed, and maintainability. It distinguishes demonstrated evidence from inferred or unresolved findings and treats speed as measured only when backed by execution evidence.

Focused verification after the change:

```text
$ .venv/bin/python /home/tacascer/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/testing-principles/skills/classify-tests
Skill is valid!

$ <local Markdown link check for classify-tests/SKILL.md>
validated 5 local links
```

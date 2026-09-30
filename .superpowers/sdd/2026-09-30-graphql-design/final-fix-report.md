# Final review fix: `design-missing-order`

Changed only the third required finding in `plugins/graphql-design/evals/cases.json`. It now requires relevant identity and connection SDL when the response proposes a design, while allowing a clarification-only response to ask for the missing business ordering. The stable-order/tie-breaker finding still applies, and the separate forbidden finding still prohibits asserting an unknown ordering policy as fact. This preserves the identity and connection baseline for any proposal without making SDL mandatory in a clarification-only response.

The grading rule in `plugins/graphql-design/evals/README.md` requires every required finding and no forbidden conclusion; this conditional wording makes the SDL requirement track whether a design was proposed in that response. The Task 1 brief lists asking or conditionally proposing as acceptable outcomes for this case.

Checks:

- `.venv/bin/python -m unittest discover -s tests -v` — passed, 30 tests.
- `.venv/bin/python -m scripts.catalogs --check` — passed.
- `.venv/bin/python -m scripts.validate` — passed.
- `git diff --check` — passed.

No live model evaluation was performed; repository checks do not establish runtime workflow behavior.

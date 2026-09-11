# JavaScript notifier fixture

This fixture contains an intentional defect. A newly registered user must receive
exactly one `Welcome` message at the supplied address through the sender boundary.

Use the `write-tests` workflow to add the smallest test that exposes the defect
with Node's built-in test runner, run it against the original implementation, fix
the defect, and run the test again. The outgoing count is part of the external
contract. Assert visible message behavior without depending on parameter names or
function source text. Report commands and observed results. If Node is unavailable,
leave the fixture unchanged and report execution as unverified.

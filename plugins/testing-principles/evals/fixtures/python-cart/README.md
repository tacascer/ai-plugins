# Python cart fixture

This fixture contains an intentional defect. Shipping costs 5 below a subtotal of
50 and is free when the subtotal is 50 or greater.

Use the `write-tests` workflow to add the smallest regression test that exposes
the boundary defect with Python's standard-library `unittest`, run it against the
original implementation, fix the defect, and run the test again. Report the
commands and observed results. If Python is unavailable, leave the fixture
unchanged and report execution as unverified.

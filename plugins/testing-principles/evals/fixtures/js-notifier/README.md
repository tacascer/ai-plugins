# JavaScript notifier design fixture

This fixture contains an intentional defect. A newly registered user must receive
exactly one `Welcome` message at the supplied address through the sender boundary.

Use `design-for-testing` to assess the existing sender seam. Explain whether any
production design change is needed, distinguish the behavior defect from
testability, and describe verification of the external contract and production
composition. Keep source unchanged and do not write tests or fix the defect.
Separate proposed verification from any execution actually observed.

# Reporting logging decisions

Separate inspected facts, recommendations, assumptions, and checks actually executed. Keep the report proportional to the request and do not imply that a proposed check was run.

Use these compact structures:

```text
Design: operational need; consumer/action; chosen mechanism and rationale;
retained event fields/severity/boundary; failure behavior; proposed checks;
assumptions and unresolved decisions.
Audit: prioritized finding; concrete trigger and consequence; file/line evidence;
proportionate correction; confidence; retained useful logs; examined scope.
```

For design work, identify the operational question and trace the signal to its consumer before selecting a mechanism. Include fields, severity, and emission boundary only for retained events. Describe relevant delivery failures and propose checks without reporting them as executed.

For audits, rank confirmed defects ahead of conditional concerns and missing evidence. Give file and line evidence when source artifacts exist; do not fabricate locations for abstract scenarios. Say when the examined evidence establishes no material issue. Name useful logs that should remain when removal is a plausible mistaken correction.

Use confidence to distinguish evidence from inference. An undocumented consumer is missing evidence, not proof that a signal is useless. A logger call by itself is not a defect, and a dependency does not prove operational coverage.

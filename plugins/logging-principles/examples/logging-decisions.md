# Logging decision examples

These authored scenarios illustrate decisions; they are not reports of executed tests.

## Hidden payment failure

**Need:** The checkout caller and payment responder must know that capture failed.

**Decision:** Preserve a failed result or propagate the error, then send a minimal error report with payment attempt ID, provider operation, and failure class to the responsible responder.

**Why the attractive alternative fails:** Catching the error, logging it, and returning success makes the business state false. Removing only the log leaves the same hidden failure.

## Optional cache miss

**Need:** The caller must fall back when an optional cached value is absent; the owner may need aggregate cache-health information.

**Decision:** Keep an explicit miss result and the normal fallback. Measure aggregate miss behavior only when a threshold and response owner exist.

**Why the attractive alternative fails:** Emitting an error for every normal miss creates noise and obscures actual cache faults. Ignoring all cache failures would also hide outages that defeat the fallback or exceed an agreed threshold.

## Silent checkout malfunction

**Need:** Operators must detect when valid carts are rejected even though no exception is raised.

**Decision:** Monitor the successful-checkout and valid-rejection outcomes, with a threshold tied to an investigation or rollback action.

**Why the attractive alternative fails:** Exception reporting observes thrown failures, not incorrect business decisions that complete normally.

## Useful import history

**Need:** Support must reconstruct where a specific import stopped.

**Decision:** Retain a bounded, rotated sequence of structured stage events containing job ID, stage, outcome, and a documented severity. Exclude source payloads and credentials.

**Why the attractive alternative fails:** Deleting all events removes support's only state history, while dumping the full payload increases exposure and storage without helping the stated investigation.

## Startup and disconnected diagnostics

**Need:** An operator must diagnose invalid startup configuration before remote telemetry initializes, and support must investigate an offline on-premise deployment.

**Decision:** Keep concise startup output on standard error and bounded local diagnostic bundles for the disconnected system. Document collection, access, and retention.

**Why the attractive alternative fails:** An always-online reporting service is unavailable at the exact boundaries where these diagnostics are needed.

## Sensitive-data handling

**Need:** A responder must correlate an authentication failure without exposing secrets.

**Decision:** Record a request correlation ID, operation, safe failure category, and service boundary. Apply the same field allowlist to logs, traces, local bundles, and error reports.

**Why the attractive alternative fails:** Moving raw request bodies or captured local variables to an error tracker relocates the exposure rather than removing it. Filtering useful fields also does not, by itself, prove legal compliance.

# Rustaceans expansion verification

Date: 2026-09-29. Scope: plugin 0.2.0, broad published-book coverage and author corrections. Changes remain in the plugin and generated catalogs.

## Source inspection

The initial GitHub PDF was an incomplete 214-page early-access edition. After the user requested a newer copy, a complete 283-page first-printing PDF was located and inspected, including its copyright page, selected passages in all 13 chapters, and the previously absent no_std and ecosystem chapters. Its SHA-256 and edition distinctions are recorded in the [source map](../../references/rustaceans-sources.md). No claim of a second edition or fully corrected printing is made. Neither PDF is bundled.

The author's site had 37 errata entries. Every anchor is represented in the [ledger](../../references/rustaceans-errata.md). Technical corrections are incorporated into the relevant guidance; listing and wording repairs are retained as editorial records. Later recommendations are distinguished from errata. Current primary sources were checked for the guidance's API-sensitive claims. The old AtomicBool struct URL returned 404; current documentation exposes AtomicBool as an alias, so the compare-exchange reference uses its documented implementation page.

## Reference retrieval and application

Before edits, a fresh read-only subagent was given five retrieval tasks and access only to the old skills, references, and examples. The tasks requested no_std/features/MSRV, FFI nullable/opaque representation, partial initialization plus unlock cleanup, trait dispatch/coherence/SemVer, and corrected variance/Cow/polling. It found insufficient explicit coverage for all five. Existing references offered only general service-design guidance; the sole book attribution was Zero to Production.

After edits, a separate fresh subagent was explicitly directed to the updated skills/references/examples and the same five topic tasks, with concrete stipulated defects for application. It retrieved and correctly applied guidance for all five: additive no_std capabilities; raw nullable pointers versus NonNull niches; initialized-count and unlock-state corrections; borrowed dyn-compatible interfaces; and corrected variance/Cow/Pending contracts. It preserved uncertainty about missing target, ABI, and whole-protocol proofs.

These are one baseline retrieval sample and one updated retrieval/application sample, not a controlled no-plugin benchmark. Baseline and updated prompts differed in scenario detail. The probes had no access to evaluation rubrics or docs by instruction; isolation was instructional, not a separate filesystem sandbox. Automatic activation and native platform loading were not tested. The 38 authored cases (12 design, 25 audit, one unrelated task) remain a broader evaluation specification, not 38 observed model passes.

## Executable example

`rustc 1.98.1 (48a229cea 2026-09-01)` on the host compiled the original library-boundaries example with edition 2021. All five tests passed: valid borrowed text, invalid owned repair without input consumption, concrete/dynamic dispatch, early-stop/zero-limit behavior, and unwind cleanup with exactly-once drops.

The first compilation could not link because `cc` was absent from PATH. Rerunning with the installed Nix GCC wrapper via `-C linker=/nix/store/3d1c302vw7kc8a5vknhmn34c0pd7zm6m-gcc-wrapper-15.3.0/bin/cc` succeeded. No source change was required. This is host execution evidence, not MSRV, target-matrix, Miri, Loom, or foreign-consumer validation.

## Review and repository checks

An independent read-only review found no important technical defects. It identified four overly broad Applied labels; the corresponding reference text was clarified to state those corrections. It also confirmed source-file hash/page count, evaluation counts, and the complete 37-entry inventory.

Baseline repository suite: 30 tests passed. Final repository suite: 30 tests passed. `scripts.catalogs --check`, `scripts.validate`, and `git diff --check` exited successfully. Both catalogs were regenerated; only the Claude catalog changed because the Codex catalog contains source paths rather than the changed metadata. The repository validator checks repository-owned packaging/resources, not exhaustive Codex or Claude platform schemas. No native platform behavioral runs, installation, or publication were performed in this expansion.

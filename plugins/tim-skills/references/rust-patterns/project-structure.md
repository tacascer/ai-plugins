# Project structure, compatibility, and tooling

**Fit.** Use when changing crate boundaries, feature flags, toolchain support, or build behavior. Read existing release and CI commands first; Cargo advice is not permission to replace Bazel or another established build.

**Boundaries.** Split crates when independent reuse, dependency isolation, or measured build costs justify the public interface. Keep implementation details in modules otherwise. Inspect re-exports and public dependency types before promising an internal change is compatible. Treat build scripts and procedural macros as host-side build code with their own dependency and reproducibility concerns.

**Feature contract.** Design additive capabilities. Cargo can unify features requested by different dependents; one caller disabling defaults cannot guarantee another will not enable them. Use `#[cfg(...)]` to remove unavailable items. `cfg!(...)` yields a Boolean and does not remove the other branch from type checking. Test supported combinations rather than assuming `--all-features` covers minimal builds. Check workspace resolver behavior against the project. [Cargo features](https://doc.rust-lang.org/cargo/reference/features.html).

**Toolchain contract.** Declare package `rust-version` where Cargo is used, and verify the declared MSRV with its compiler and compatible resolved dependencies. A declaration alone does not prove support. Edition and MSRV are different constraints. Keep current-stable and target checks alongside MSRV checks when the crate promises both. [MSRV](https://doc.rust-lang.org/cargo/reference/rust-version.html). For shared build artifacts, Cargo's setting is `build.target-dir`; `build.target` selects a compilation target. [Configuration](https://doc.rust-lang.org/cargo/reference/config.html#buildtarget-dir).

**Ecosystem and performance.** Evaluate crates against maintenance, compatibility, license policy, enabled features, target support, and actual needs. Use formatting, Clippy, dependency checks, documentation builds, and benchmarks for their specific evidence. Profile before changing dispatch, allocation, parallelism, LTO, or crate boundaries; compare the same workload and build profile. Treat author-recommended tools as options, not required dependencies. Book-era predictions about stabilization are not current guarantees.

**Verification.** Build a small downstream consumer for public API changes. Exercise default, minimal, and relevant individual feature combinations and actual targets. Document unsupported combinations. Use [no_std](no-std.md) for allocation and platform boundaries and [testing](testing.md) for behavioral checks.

[Evidence and access limits](rustaceans-sources.md) · [Corrections](rustaceans-errata.md)

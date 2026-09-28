# Configuration and serialization

**Problem and fit.** Deserialization answers whether input has the expected shape; it does not prove a batch size is in range, a URL uses a supported scheme, or a credential is safe to display. Validate semantic settings at startup before building clients, pools, or workers. For a few variables, standard-library environment reads plus a typed parser can be enough. [Source](sources.md#verified-book-principles).

**Shape.** Document source precedence, deserialize to a typed settings structure, then perform fallible domain validation. Return an error naming the setting or safe category, never the credential value. Avoid deriving or logging a `Debug` representation that includes secrets. Keep raw configuration separate from validated runtime configuration when that makes invalid states impossible downstream.

**Options and trade-offs.** [`config`](sources.md#current-primary-sources-and-bounded-alternatives) composes file, environment, and override sources; Figment composes providers and serialized defaults. Choose a loader only if the existing mechanism cannot meet the needed precedence or provider behavior; neither replaces semantic checks. Verify pinned API/features before recommending live reload or provider methods. Ask: which source wins, when is validation run, and can any diagnostic print a secret?

# Data refresh family

PR #45 is the retained carrier for #53. Its original working-directory fix is
preserved by `scripts/refresh_data.py`: validator and indexer run from `_pipeline`,
with all content/schema/output paths resolved to this repository. Invocation from
an unrelated cwd is supported. No source dependency is edited.

The runner validates essays and both daily-log/preservation schemas, regenerates
twice, rejects nondeterminism, retains reviewed timestamp-only bytes, and writes
a source-SHA receipt. CI uses the same runner with `--check`; semantic drift fails.
The scheduled workflow instead proposes changed data on one short-lived family
branch via PR. It never writes main, overwrites an existing branch, or merges.
An existing proposal remains the sole family owner and must be reconciled before
another is created. A retained closed-PR branch requires a verdict, not force push.

GitHub-token-created PRs may not trigger CI. The coordinator must run the normal
exact-head checks before merge; green default or a refresh receipt alone is not
sufficient. Missing API permissions surface as a failed run; its receipt is retained.

This refresh is deterministic indexing of existing public source, not proof of
new live data. #61 owns live intake. #54 owns external link/report repair. F1 donor
documentation remains under #56/#64; no historical branch or issue is erased.

Verification: the shared CI runs the scheduled-equivalent command from clean
checkouts on every PR and default push. A real scheduled proposal/delivery event
remains separate evidence and must be attached to #53 when it actually occurs.

# Branch constitution

Default branch: `main`. Observed workflow: short-lived branches and PRs, with
squash merges and history-preserving integration merges where intention requires.
Mission: Verify → Heal → Expand → Evolve. Never expand over a red or dishonest trunk.

## Standing branch

| Branch | Purpose | May accept | Green means |
| --- | --- | --- | --- |
| `main` | Releasable public publication | One reviewed intention/family per PR | Shared validation/build passes at current head; applicable source/output/schema/data checks pass; deployment/readback tracked separately |

Only main is evidenced as standing. No develop or lane branch is established.
Add a standing lane only for an evidenced recurring integration need, with steward,
merge target, tested CI trigger and reviewed amendment. Do not derive lanes from
issue queue labels. Approved dormant lanes remain until explicit retirement.

## Working branches

Use `docs|fix|test|feat|chore|hotfix/<issue>-<intent>` or
`work/<area>/<issue>-<intent>`. One intention/family per branch and PR. Start from
verified main; record source SHA. Prefer a worktree per active branch. Existing
family carriers retain their history: PR45 used its original branch and a merge
with current main; do not recreate its siblings.

A coordinator acknowledges issue, executor, independent reviewer (or explicitly
unfilled review gate), branch/worktree, base/head SHA, exact path scope, shared
output groups, dependency receipts, expiry and next checkpoint before concurrent
work. Unfilled review is not an approval. Claims are serialized at the coordinator;
chat messages or independent local lock files are not global locks.

Shared workflows, configuration and generated indexes merge one at a time. Refresh
main/head/check receipts after collision resolution. Expired claims are parked
with their branch/head and unique residue retained before reassignment.
See `docs/operations/agent-handoff.md` and the claim-record validator.

## Merge, hotfix and retirement

No direct implementation pushes to main; scheduled refreshes also propose PRs.
Hotfix branches start from main, merge through checks and review, and backport to
any documented living lanes. No release branch exists; dated editions alone do
not require one. Establish a freeze lane only when the release policy needs it.

Before closing or deleting, record intention, evidence, successor and why no
unique work is lost. A family closes only after successor proof on default and
member-specific residue accounting. Keep parked/captured work; never force-push
published history. No branch is deleted by this constitution or its validator.

Secrets, production personal data and private drafts belong in no public branch.
Source approval, public deployment and channel distribution are distinct gates.
The required checks are engineering evidence, not automatic rights clearance.

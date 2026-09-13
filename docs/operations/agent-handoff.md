# Remote/local claims and handoffs

#57 adopts the observed main-only branch constitution after the #56 ledger.
The single coordinator is the serialization authority. An agent proposes a claim
on the owning child issue; an epic does not own an implementation branch. The
coordinator acknowledges the claim with its exact base/head and permitted paths
before any concurrent executor starts. No automation grants itself publication,
secret custody, administrative authority or permission to erase captured work.

Each active claim requires: unique ID, issue, executor, distinct reviewer, exact
working branch/worktree, 40-character base SHA, literal repository-relative path
prefixes, shared output groups, dependency receipts, expiry and next checkpoint.
Review may remain explicitly unfilled while discovery proceeds; do not call that
an active independently reviewed implementation claim.

`python scripts/claim_contract.py` reads existing/candidate JSON on stdin and
validates overlap, shared outputs, independent review and expiry. It returns a
proposed record list; it does not write a remote lock. One coordinator must apply
accepted records atomically to its authoritative state, or serialize them by
acknowledged issue comments. Independent machines running the validator are not
mutually exclusive and must not treat local success as ownership.

The test suite contains a two-executor simulation: a nested-path collision fails,
an expired owner blocks silent takeover, then an acknowledged handoff retains the
old record/residue and permits the successor. Shared-output collisions and
self-review also fail. This is a tested record contract, not a live multi-agent
network drill or proof of GitHub administrator enforcement.

Handoff receipt: intention; source/base/head; attempted and passed/failed checks;
changed paths; commits not on main; worktree/branch recovery instructions; exact
blocking dependency/question; next owner; review state; lease expiry; and rollback
boundary. Park expired work before reassignment. Never remove the predecessor's
branch, unique commits, comments or evidence just because its lease expired.

The owner has authorized this session's serialized implementation. No external
executor or reviewer has been silently enrolled. #57 remains open for a real
coordinator-backed concurrent deployment and independently staffed review drill.

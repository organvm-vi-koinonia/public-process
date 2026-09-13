<!-- ORGANVM:AUTO:START -->
## Agent Context (auto-generated — do not edit)

This repo participates in the **ORGAN-V (Public Process)** swarm.

### Active Subscriptions
- Event: `governance.updated` → Action: Check compliance with updated governance rules
- Event: `promotion.completed` → Action: Draft essay about promoted repo

### Production Responsibilities
- **Produce** `essay-markdown` for ORGAN-VI, ORGAN-VII
- **Produce** `essays-index` for ORGAN-V
- **Produce** `rss-feed` for EXTERNAL

### External Dependencies
- **Consume** `dependency` from [`organvm-i-theoria/recursive-engine--generative-entity`](../../organvm-i-theoria/recursive-engine--generative-entity/CLAUDE.md)
- **Consume** `dependency` from [`organvm-ii-poiesis/metasystem-master`](../../organvm-ii-poiesis/metasystem-master/CLAUDE.md)
- **Consume** `dependency` from [`organvm-iii-ergon/public-record-data-scrapper`](../../organvm-iii-ergon/public-record-data-scrapper/CLAUDE.md)
- **Consume** `dependency` from [`organvm-iv-taxis/agentic-titan`](../../organvm-iv-taxis/agentic-titan/CLAUDE.md)

### Governance Constraints
- Adhere to unidirectional flow: I→II→III
- Never commit secrets or credentials

*Last synced: 2026-04-14T21:32:07Z*
<!-- ORGANVM:AUTO:END -->


## Repository stewardship (maintainer policy)

Read [BRANCHES.md](BRANCHES.md), [STATUS.md](STATUS.md),
[the intention ledger](docs/stewardship/README.md), and the owning issue before
creating branches or changing scope. Roadmap anchor: issue #10. The generated
context above is preserved; it does not replace these repository operating rules.

- Verify → Heal → Expand → Evolve. Do not expand over red or dishonest default.
- Recover every issue/PR/branch intention before judging it. Preserve unique work;
  finish it, or park it with evidence, a successor and a next owner/question.
- Inventory first, mutations second. Paginate branch, PR and issue inventories;
  label unavailable local/private sources unknown. Never invent completeness.
- Group repeated defects/retries/captures into families. One successor issue and
  working branch per active family; carry every member's unique residue forward.
- Read the constitution; use one short-lived worktree/branch per intention, PRs
  to main, and no direct default work. Do not invent develop or standing lanes.
- Comment on touched artifacts with recovered intention, verdict, next step and
  links. PRs must link their owning issue, branch/base/head, scope and verification.
- Close only after the finish line is verified on default (and live where needed).
  Before closure/deletion, record intention, evidence, successor and why no unique
  work is lost. Family members remain linked until successor and member proof pass.
- After a working branch is merged and residue is accounted for, ordinary branch
  retirement follows BRANCHES.md; never delete a standing or parked branch as cleanup.
- No history rewrite or force-push of published history. No drive-by refactors.
  Unsafe/contradictory work receives a documented parked intention, not erasure.
- Keep secrets, credentials, production personal data and private drafts out of
  git. Public source, private custody, rights and exact publication/distribution
  approval are separate controls; see docs/operations/public-private-boundary.md.
- The author controls public creative text. Engineering permission does not
  fabricate authored editions, reviewer participation, rights or reader evidence.
- Use the shared validation workflow and docs/operations/release-gate.md. Record
  actual exact-head/default/deployment receipts; URL syntax is not live link health.
- Coordinate claims via docs/operations/agent-handoff.md. The claim validator is
  not a distributed lock. Do not imply that unfilled review or expired ownership
  grants automatic merge/publication authority.
- Stay inside this repository unless a documented dependency repair is necessary
  for its green. If blocked, leave a durable mergeable or parked handoff and update
  STATUS.md/the owning issue; do not silently drop the task.

Requirement coverage and implementation limits:
[stewardship coverage](docs/stewardship/requirement-coverage.md).

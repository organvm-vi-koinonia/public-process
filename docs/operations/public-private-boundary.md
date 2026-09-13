# Public and private custody

Decision record for #59, under #50 and roadmap #10. Baseline:
`be78cc9f39cd9e6413e2417b25cd6f47d89f8f38` (2026-09-13).

## Accepted implementation boundary

This repository is public. All commits, branches, PR attachments and Actions
logs must be treated as public, including drafts and files excluded from Pages.
Keep private originals in their existing restricted source systems. Export only
material the author has approved for the specific public use. Do not create a
second repository or migrate originals merely to make the boundary appear done.
The owner's execution authorization covers engineering and sanitized operational
documentation; it is not new authorship, rights clearance, or approval of unseen
creative material.

| Category | Default custody | Public interface |
| --- | --- | --- |
| Source drafts, research notes, personal journals | Existing restricted source system | Approved excerpt and non-sensitive source identifier only |
| Finished essays and editions | Private until author approves exact version | Approved text, attribution, evidence and correction history |
| Media masters and third-party contributions | Restricted pending rights evidence | Approved derivative, credit and applicable permission |
| Differentiating methods and internal operations | Restricted unless explicitly approved | Sanitized contracts and verified public outcomes |
| Aggregate analytics | Restricted raw observations | Privacy-reviewed totals with source, window and unknowns |
| Contacts, subscribers, production personal data | Restricted service with controlled access | No records in git, builds, CI logs or artifacts |
| Credentials and signing material | Secret manager / protected runtime | References to required variable names only |
| Build code and public operational documentation | Public after reviewed PR | Existing applicable license and source history |

## Exposure inventory

Public git includes the complete tracked source, even when Jekyll excludes it.
Pages renders root pages, `_posts`, `essays`, `_logs`, `_dissertations`, layouts,
includes and static files. Additional surfaces are data indexes, RSS, sitemap,
search/social metadata, previews, Actions logs/artifacts and downstream dispatch.
Neither `draft` metadata nor an underscore directory is a confidentiality control.
#60 owns synthetic tests and exact-version publication/distribution checks.

## Rights and historical disclosure

The baseline LICENSE contains MIT terms; README also advertises CC BY-SA 4.0.
This record does not resolve that discrepancy by assigning a new license. Keep
existing notices and per-work credits. Do not automatically apply software terms
to literary/media works or remove obligations attached to third-party material.
Unclear rights block new reuse until the rights holder resolves the applicable
permission. Record only the sanitized result here, not private agreements.
Already-public material remains historically disclosed; relocation cannot revoke
copies, prior permissions or knowledge of the material.

## Access, backup and export contract

The source owner controls the existing private service's access and backup policy.
No private destination/account has been provisioned or inspected by this decision.
Until an actual destination is inventoried and a restore tested, private-storage
continuity remains unverified under #67. A future migration needs source/destination
identity, access evidence, checksum comparison, restore receipt and retention
period before any original is removed. Never put those access details in public.

A public export receipt records: opaque source ID, public path, byte digest,
author/rights decision reference, permitted action (preserve, publish, distribute),
channels if applicable, expiry/revocation and correction successor. Publication
and distribution are separate grants; changing bytes invalidates the receipt.
Existing public corpus is historical evidence, not blanket approval of new drafts.

## Alternatives and remaining evidence

A new private git mirror was rejected for this tranche: it adds custody without
establishing rights and cannot house credentials or production personal data.
Moving public files was rejected: it does not undo disclosure and risks history.
Retaining existing restricted custody is the smallest reversible implementation.

This records and implements the public engineering boundary. It does not claim
an exhaustive secret-history audit, owner-approved rights for every work, tested
private backup, or retroactive secrecy. #59 stays open for those decision receipts;
#60 and #67 carry executable exposure and continuity proof respectively.

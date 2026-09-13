# Publication and distribution authority

Implementation record for #60, dependent on #59 and #55.

Preserve, publish and distribute are distinct actions. The approved preservation
record and historical corpus remain public; they do not authorize a new edition
or a social post. A future approval receipt must identify exact file/media hashes,
author and rights evidence, permitted action/channel, expiry and revocation. A
changed file needs new authority. Do not generate literary text in the author's
name or infer consent from an empty check set.

The build now rejects explicit private/restricted/draft/unpublished frontmatter,
private/draft source directories and prohibited artifact paths. Tests use synthetic
fixtures. These guards reduce accidental publication; they cannot make a public
commit confidential, determine rights, recognize all sensitive prose, or prove
an author's identity. Keep real private content out of public git in the first place.

Automatic four-channel dispatch has been replaced with a read-only approval-status
workflow. Its intention is preserved in #65. No existing account was deleted and
no new notice sent. Restore dispatch only after a real author-approved edition
passes live readback and a channel-specific deduplication/delivery contract.

Remaining #60 evidence: trusted approval identity, expiry/revocation/changed-version
checks, exact source-to-output mapping across feed/sitemap/metadata and all assets,
and an actual correction/takedown drill. This tranche is not full approval-system
completion. Existing public historical status fields retain their meaning.

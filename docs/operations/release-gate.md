# Validated publication artifact

Implements the build-parity portion of #55. Both CI and Pages call
`.github/workflows/validate-publication.yml` at their source revision. Pages
uploads only after essay/log schema checks, contract tests, generated-data parity,
internal links and the strict production Jekyll build succeed. The deploy job
requires that build; manual Pages runs from other branches are skipped.

The pipeline and standards revisions are pinned in the shared workflow and gitlinks.
Python dependencies are fixed in requirements-build.txt; Ruby uses Gemfile.lock.
Actions/runner revisions still require periodic maintenance; this is source/build
traceability, not a claim of hermetic or byte-identical Jekyll builds across time.

## Local equivalent

Initialize dependencies with `git submodule update --init`, install
`requirements-build.txt`, and install Ruby dependencies using Bundler. Run:

```sh
python scripts/validate_logs.py
python -m unittest discover -s tests -v
(cd _pipeline && python -m src.validator --posts-dir ../_posts/ --schema ../_standards/schemas/frontmatter-schema.yaml)
(cd _pipeline && python -m src.indexer --posts-dir ../_posts/ --logs-dir ../_logs/ --output-dir ../data/)
python scripts/check_data_drift.py
(cd _pipeline && python -m src.link_checker --posts-dir ../_posts/ --logs-dir ../_logs/ --internal-only --output /dev/null)
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --baseurl /public-process
python scripts/release_manifest.py
```

The drift check rejects new, deleted and semantically changed data; only the
top-level generator timestamp is ignored. It restores matching generated files
to reviewed bytes before the build. Daily logs retain the shared mood requirement;
approved preservation records instead require status, evidence cutoff and approval
date. This validates receipt shape, not the identity/authority behind approval.

`release-manifest.json` in the uploaded site records source SHA, dependency SHAs
and SHA-256 digests of site files except itself. Compare the live receipt with the
Actions source SHA and selected downloaded file digests after deploy. A receipt
is not a signature or an independent authorization authority.

## Recovery and remaining gates

Revert a defective change through a PR, pass the same workflow, then deploy the
validated revert. Do not bypass validation to roll back. Record source/deploy/run
and live-readback evidence on #55. A deployed rollback drill remains outstanding.

The former automatic merger accepted possibly empty checks and age/label metadata.
Its executor is now parked with a read-only diagnostic. Preserve its intention:
restore automation only with trusted check identity, nonempty required checks,
current-head review/publication authority, compare-and-merge protection, and
adversarial missing/forged/stale-head tests. No branch is automatically deleted.

This does not enforce repository administrator rulesets or independently approved
source changes. It does not yet validate every research claim or literary/media
right in the corpus. #60 owns author approval and output exposure; #62 owns edition
and research integrity. #55 stays open until those and live/rollback receipts exist.

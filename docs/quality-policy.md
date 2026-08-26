# Quality Policy

This document defines minimum quality guarantees for changes merged into `public-process`.

## Guarantees

1. Content schema integrity:
   - Every essay in `_posts/` must pass `essay-pipeline` frontmatter validation.
   - Every log in `_logs/` must pass log-schema validation.

2. Derived artifact integrity:
   - Changes to essays/logs require regenerated `data/*.json` artifacts.
   - CI fails if data drift is detected.

3. Build integrity:
   - Jekyll strict build must pass (`bundle exec jekyll build --strict_front_matter --future`).

4. Link integrity:
   - Internal links in essays/logs must pass automated checks.

5. Secret hygiene:
   - No secrets, tokens, keys, or credentials may be committed.

## Local Verification Contract

There is no repo-local `validate.sh` wrapper in this repository. Use the check
that matches the files changed, and let CI run the full shared pipeline.

For docs-only changes:

- Preview the Markdown.
- Self-review internal links.
- Confirm no secrets, credentials, API keys, tokens, or private data were added.

For Jekyll content, layout, include, or configuration changes:

```bash
bundle install
bundle exec jekyll build --strict_front_matter --future
```

If the Jekyll build fails, treat it as a release blocker.
For `_posts/` or `_logs/` changes, CI also checks frontmatter, internal links,
and generated `data/` drift using the shared `essay-pipeline` and
`editorial-standards` repositories. If CI reports drift, regenerate the data
artifacts and include them in the PR.

## Exceptions

Any exception to these checks requires:

1. Linked issue with rationale.
2. Explicit reviewer approval.
3. Follow-up issue to remove the exception.

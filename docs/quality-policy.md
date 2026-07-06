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

Before opening a PR:

```bash
bundle install
bundle exec jekyll build --strict_front_matter --future
```

If the Jekyll build fails, treat it as a release blocker. CI also runs
cross-repo editorial and generated-data checks that may require follow-up when
they fail.

## Exceptions

Any exception to these checks requires:

1. Linked issue with rationale.
2. Explicit reviewer approval.
3. Follow-up issue to remove the exception.

# Contributing to public-process

Thank you for helping improve `public-process`.

This repository is the essay site for the organvm system. If you came here
looking for essays, you are in the right place.

## Quick Orientation

- Complete dated essay corpus: `_posts/YYYY-MM-DD-slug.md`
- Curated long-form essay collection: `essays/meta-system/` and
  `essays/subsidiary/`
- Site pages: `index.md`, `about.md`, `reading.md`, `dashboard.md`
- Generated indexes and feeds: `data/`
- Jekyll configuration: `_config.yml`, `_layouts/`, `_includes/`

If you are new to the system, read the [Quick Start](docs/quick-start.md)
before cloning any other ORGANVM repo. For most writing and editing work, start in `_posts/` or `essays/`.

## Repository Map

| Surface | Main language / format | Typical contribution |
|---------|------------------------|----------------------|
| `_posts/` | Markdown + YAML frontmatter | Essay corrections, metadata fixes, link repair |
| `_logs/` | Markdown + YAML frontmatter | Historical log cleanup and indexing fixes |
| `docs/` | Markdown, YAML | Process documentation and governance references |
| `_layouts/`, `_includes/` | Liquid, HTML | Template and page-structure fixes |
| `assets/` | CSS, static assets | Styling and presentation fixes |
| `data/` | JSON | Generated index data; update only when validation asks for it |
## Prerequisites

## Terms Used Here

| Term | Plain meaning |
|------|---------------|
| `public-process` | This repository: the public essay and methodology site. |
| Organ V / Logos | The part of organvm responsible for essays, public process, and explanation. |
| organvm | The broader eight-organ project this site documents. |
| Essay | A Markdown file with a short YAML metadata block at the top. |
| Frontmatter | The YAML metadata block between `---` lines at the top of an essay. |
| Stranger Test | A check that a first-time reader can understand the purpose, status, and next step without private context. |
| PR | Pull request: the GitHub review request for your proposed change. |

## Good First Contributions

- Fix a typo, broken link, confusing sentence, or stale cross-reference.
- Clarify an essay introduction or section heading.
- Improve onboarding docs such as this file.
- Add missing metadata only when the expected value is clear from nearby files.
- Draft a new essay only when there is an issue or maintainer note defining the scope.

Keep first changes small and easy to review. A useful one-paragraph correction is
better than a broad rewrite that mixes many decisions.

## Setup

For docs-only edits, GitHub's web editor is enough. For local preview or changes
to essays, layouts, includes, or configuration, use the Jekyll setup:

```bash
git clone https://github.com/organvm/public-process.git
cd public-process
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

The local site is available at `http://127.0.0.1:4000/public-process/`.

### Finding a First Issue

1. Check the open [`good first issue` list](https://github.com/organvm/public-process/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22good%20first%20issue%22).
2. If no starter issue is available, open the [First Contribution template](https://github.com/organvm/public-process/issues/new?template=first_contribution.md) with a small proposed scope.
3. Good first contributions in this repository are usually Markdown, frontmatter, internal-link, documentation, or small Jekyll template fixes.

Maintainers should label starter tasks `good first issue` and include the relevant surface from the repository map above so contributors can tell whether the work is Markdown, Ruby/Jekyll, Liquid/HTML, CSS, YAML, or JSON.

### Reporting Issues

- Use **Quick Issue** when you just need to report friction, ask a question, or
  file a documentation gap.
- Use the specific bug, feature, first-contribution, or stranger-test templates
  only when that structure helps.
- Include clear reproduction steps for bugs
- For documentation issues, specify which file and section
- Architecture/navigation confusion is useful feedback. If you cannot find the
  system diagram you expected, open a Quick Issue and name the path you tried.

## Making a Change

1. Fork the repository on GitHub.
2. Create a branch for the change:

   ```bash
   git checkout -b docs/clarify-contributor-guide
   ```

3. Make the smallest useful edit.
4. Run the check that matches the change.
5. Commit with a short, imperative message:

   ```bash
   bundle exec jekyll build --strict_front_matter --future
   git commit -m "clarify contributor guide"
   ```

6. Open a pull request and link the related issue when there is one.

## Checks to Run

Use the lowest check that actually covers your change:

| Change type | Local check |
|-------------|-------------|
| Root docs such as `README.md`, `CONTRIBUTING.md`, or `docs/*.md` | Preview the Markdown and self-review links. |
| Essays, logs, layouts, includes, or `_config.yml` | `bundle exec jekyll build --strict_front_matter --future` |
| `_posts/` or `_logs/` content that changes generated indexes | Run the Jekyll build, then expect CI to verify frontmatter, links, and `data/` drift. |

CI also runs the shared `essay-pipeline` and `editorial-standards` repositories
for frontmatter validation, internal link checks, and generated data drift. If
CI reports drift in `data/`, regenerate the data artifacts or ask for maintainer
help in the PR.

## Writing Style

Essays should be clear, specific, and honest about process. Prefer concrete
examples over abstract claims. Keep filenames in the Jekyll format
`YYYY-MM-DD-slug.md` when adding a dated post.

When editing existing essays, preserve the author's voice. Improve clarity
without flattening the argument.

## Pull Request Expectations

- Explain what changed and why.
- Link the issue or feedback session when applicable.
- Summarize the checks you ran.
- Keep each PR focused on one correction, essay, or documentation improvement.
- Do not commit secrets, credentials, API keys, tokens, or private data.

Large changes are welcome, but they should start as an issue so scope and
review expectations are clear before the work begins.

## Code of Conduct

Be respectful, constructive, and honest. This project is part of the
[organvm system](https://github.com/organvm-v-logos), which values transparency
and building in public. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/).

## Questions

Open an issue on this repository. For system-wide questions, see
[orchestration-start-here](https://github.com/organvm-iv-taxis/orchestration-start-here).

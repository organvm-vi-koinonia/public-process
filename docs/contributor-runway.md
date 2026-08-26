---
layout: default
title: "Contributor Runway"
permalink: /docs/contributor-runway/
---

# Contributor Runway

This guide defines how first-time contributors can land meaningful changes
quickly in `public-process`.

## Repository Type

`public-process` is a Jekyll static site. Most first contributions are not application-code changes; they are small Markdown, frontmatter, documentation, link, Liquid template, HTML, CSS, YAML, or JSON-data fixes.

| Area | Language / format | Good first scope |
|------|-------------------|------------------|
| `_posts/` | Markdown + YAML frontmatter | Fix metadata, links, excerpts, or formatting |
| `_logs/` | Markdown + YAML frontmatter | Fix log formatting or internal references |
| `docs/` | Markdown, YAML | Clarify process docs or governance references |
| `_layouts/`, `_includes/` | Liquid, HTML | Small template accessibility or structure fixes |
| `assets/` | CSS | Narrow styling fixes |
| `data/` | JSON | Generated index updates requested by CI |

### Content Map

- `_posts/` is the complete dated essay corpus.
- `essays/` is the curated long-form essay collection.
- Root Markdown files such as `index.md` and `about.md` are site pages.
- `data/` contains generated indexes and should not be edited by hand unless an
  issue explicitly asks for it.

### First Steps

1. Pick a scoped issue labeled `good first issue`, `documentation`, or
   `research`.
2. For local preview, install dependencies and run Jekyll:

   ```bash
   git clone https://github.com/organvm/public-process.git
   cd public-process
   bundle install
   bundle exec jekyll serve --host 127.0.0.1
   ```

3. Before opening a PR, run the check that matches the change:

   - Docs-only change: preview the Markdown and self-review links.
   - Essay, layout, include, or config change:

     ```bash
     bundle exec jekyll build --strict_front_matter --future
     ```

4. If the issue list has no starter tasks, open the [First Contribution issue template](https://github.com/organvm/public-process/issues/new?template=first_contribution.md) and propose a small Markdown, documentation, frontmatter, link, or Jekyll-template cleanup.

## Starter Issue Labels

Starter issues should use `good first issue` and name the relevant repository surface in the title or body, for example `_posts`, `docs`, `Liquid`, `CSS`, `frontmatter`, or `links`. This makes the required language or file format visible before a contributor opens the issue.

The CI also validates frontmatter, regenerated data files, internal links, and
basic repository structure.
## First Contribution Scope

A first contribution should:

- Touch a small, isolated surface area.
- Have clear acceptance criteria.
- Be testable with existing workflows.
- Avoid cross-repo architectural refactors.
- Avoid new organvm vocabulary unless it is defined in the same change.

## Review SLA Targets

- First maintainer response: within 3 business days.
- Review turnaround after requested changes: within 3 business days.
- Merge decision after final approval: within 2 business days.

## Required PR Evidence

- What changed and why.
- Validation output summary, usually from
  `bundle exec jekyll build --strict_front_matter --future` (or a note if docs-only).
- Linked issue with acceptance criteria.

## Escalation

If blocked for >7 days without review, open a `documentation` issue in
`organvm/public-process` or comment on the PR with a link to the blocker details.

---
layout: default
title: "Contributor Runway"
permalink: /docs/contributor-runway/
---

# Contributor Runway

This guide defines how first-time contributors can land meaningful changes quickly.

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

## Fast Start

1. Clone `public-process` and install Jekyll dependencies:

```bash
git clone https://github.com/organvm/public-process.git
cd public-process
gem install bundler:4.0.3
bundle install
```

2. Pick a scoped issue labeled [`good first issue`](https://github.com/organvm/public-process/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22good%20first%20issue%22).
3. Run the local build before opening a PR:

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

## Review SLA Targets

- First maintainer response: within 3 business days.
- Review turnaround after requested changes: within 3 business days.
- Merge decision after final approval: within 2 business days.

## Required PR Evidence

- What changed and why.
- Validation output summary, usually from
  `bundle exec jekyll build --strict_front_matter --future`.
- Linked issue with acceptance criteria.

## Escalation

If blocked for >7 days without review, open a `documentation` issue in
`organvm/public-process` with a link to the PR and the blocker details.

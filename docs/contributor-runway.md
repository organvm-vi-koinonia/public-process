# Contributor Runway

This guide defines how first-time contributors can land meaningful changes quickly.

## Fast Start

1. Clone the repository and install the Ruby dependencies:

```bash
git clone https://github.com/organvm/public-process.git
cd public-process
bundle install
```

2. Pick a scoped issue labeled `good first issue`.
3. Run the local build before opening a PR:

```bash
bundle exec jekyll build --strict_front_matter --future
```

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
- Validation output summary, including the Jekyll build command above.
- Linked issue with acceptance criteria.

## Escalation

If blocked for >7 days without review, open a `documentation` issue in this
repository with a link to the PR and blocker details.

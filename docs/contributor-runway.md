# Contributor Runway

This guide defines how first-time contributors can land meaningful changes quickly.

## Fast Start

1. Clone `public-process`. This is the first repo to use for Public Process
   reading, local preview, and doc/content contributions:

```bash
git clone https://github.com/organvm/public-process.git
cd public-process
gem install bundler:4.0.3
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

2. Open `http://127.0.0.1:4000/public-process/`.
3. Read [`docs/quick-start.md`](quick-start.md) if the organ names or repo
   boundaries are unclear.
4. Pick a scoped issue labeled `good first issue`.
5. Run the local build before opening a PR:

```bash
bundle exec jekyll build --strict_front_matter --future
```

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

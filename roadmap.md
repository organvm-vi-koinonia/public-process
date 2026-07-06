---
layout: default
title: "Roadmap"
permalink: /roadmap/
---

# Public Process Roadmap

Public Process is ORGAN-V (Logos): the public narrative, evidence, and publication layer for the organvm system. This page is the product-manager entry point for understanding what is live, what is in progress, what depends on other organs, and who owns decisions.

## Product Shape

| Surface | Audience | Current State | Next Milestone |
|---------|----------|---------------|----------------|
| Essay site | External readers, grant reviewers, collaborators | Live Jekyll site with essays, logs, dissertations, RSS, tags, categories, and corpus dashboards | Improve orientation so first-time visitors can understand the system without reading the whole corpus |
| Essays index | ORGAN-V, ORGAN-VI, ORGAN-VII | Generated data artifact consumed by site pages and downstream publication/community organs | Keep index generation stable as the corpus grows |
| RSS feed | External subscribers | Live feed at `/feed.xml` | Confirm discoverability from every high-intent entry point |
| Cross-reference map | Product, portfolio, and system reviewers | Live map connecting essays to related repositories and organs | Add clearer product interpretation around how projects compose into the larger system |
| Contributor runway | Contributors and reviewers | Published process docs and issue templates | Make ownership, review, and roadmap decisions visible from the first screen |

## Roadmap

### Now: Stranger-Test Orientation

Goal: a first-time product manager can understand the product, roadmap, and maintainers in under ten minutes.

- Publish this roadmap as a first-class navigation item.
- Expose maintainers and decision ownership without requiring the user to inspect `.github/CODEOWNERS`.
- Point readers from the homepage and README to the roadmap, dashboard, connections map, and contributor runway.
- Keep the eight-organ explanation attached to product surfaces, not only long-form essays.

### Next: System Map and Milestone Tracker

Goal: make the decoupled projects legible as one product system.

- Promote the organ and repository map into a compact product-system view.
- Distinguish live, in-progress, planned, and blocked surfaces.
- Add milestone dates only when they are supported by current delivery evidence.
- Link each milestone to its source document, generated data artifact, or issue.

### Later: Operating Metrics and Distribution

Goal: show whether Public Process is working as a public interface, not just whether content exists.

- Surface RSS, essay, and cross-reference health in the dashboard.
- Track publication cadence against `data/content-calendar.yaml`.
- Connect essay promotion events to ORGAN-VII distribution artifacts.
- Add reader and contributor feedback loops once GitHub Discussions or an equivalent channel is active.

## Maintainers and Decision Flow

| Responsibility | Owner / Source | Where to Verify |
|----------------|----------------|-----------------|
| Repo ownership and reviews | `@4444j99` | `.github/CODEOWNERS` |
| Product direction | `@4444J99` / ORGANVM conductor | `README.md`, `about.md`, this roadmap |
| Contribution intake | GitHub Issues and pull requests | `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/` |
| System governance | ORGAN-IV (Taxis) and meta-organvm registry | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` |
| Publication pipeline | ORGAN-V (Logos), with downstream ORGAN-VI and ORGAN-VII consumers | `ecosystem.yaml`, `_config.yml`, `data/` |

Decision rule: reversible documentation and site improvements can be proposed through normal pull requests. Irreversible or outward-facing changes, including new distribution channels, credentialed integrations, paid tooling, or governance changes, require explicit human approval before activation.

## How the Repos Compose

Public Process is intentionally decoupled from the product, art, theory, and orchestration repositories it documents. The product view is:

1. ORGAN-I (Theoria) defines theoretical and ontological foundations.
2. ORGAN-II (Poiesis) turns those foundations into artistic and experiential systems.
3. ORGAN-III (Ergon) turns stable patterns into commercial products.
4. ORGAN-IV (Taxis) coordinates governance, routing, and cross-organ rules.
5. ORGAN-V (Logos), this repository, translates the work into essays, indexes, feeds, and public evidence.
6. ORGAN-VI (Koinonia) and ORGAN-VII (Kerygma) consume Public Process outputs for community and distribution.

For a product manager, the important invariant is that Public Process is not the whole product. It is the public interface that makes the larger product system understandable.

## Fast Paths

- Read the [About page]({{ site.baseurl }}/about/) for the eight-organ model.
- Check the [Dashboard]({{ site.baseurl }}/dashboard/) for corpus metrics.
- Use the [Connections map]({{ site.baseurl }}/connections/) to see how essays refer to repositories.
- Review [Contributor Runway]({{ site.baseurl }}/docs/contributor-runway/) for contribution expectations.
- Open the [GitHub issue template](https://github.com/organvm-v-logos/public-process/blob/main/.github/ISSUE_TEMPLATE/stranger_test_feedback.md) to run another stranger test.

## Evidence for This Roadmap

This page was added in response to GitHub issue [organvm/public-process#17](https://github.com/organvm/public-process/issues/17), where a Product Manager stranger-test participant could identify maintainers but could not understand the roadmap from the public profile.

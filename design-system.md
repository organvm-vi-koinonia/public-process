---
layout: default
title: "Design System"
permalink: /design-system/
---

# Design System

Public Process is a reading site first. The interface should feel quiet,
legible, and inspectable: dark base, restrained blue accent, compact metadata,
and data widgets that support the essay corpus without competing with it.

The implementation source of truth is [`assets/css/style.css`]({{ site.baseurl }}/assets/css/style.css).
The broader aesthetic rationale is described in
[The Aesthetic Nervous System]({{ site.baseurl }}{% post_url 2026-02-13-aesthetic-nervous-system %}).
This page makes the current rules visible for design review.

## Source Map

| Surface | Purpose | Review there when |
|---|---|---|
| `assets/css/style.css` | Implemented tokens, layout, and reusable components | Checking the actual UI contract |
| `_layouts/default.html` | Page shell, stylesheet loading, Mermaid theme | Checking global page structure |
| `_includes/header.html` | Primary navigation | Checking wayfinding and link order |
| `organ-aesthetic.yaml` | Cross-organ aesthetic contract when present in an organ repo | Checking how organ-level taste modifies the global style |

## Reading `organ-aesthetic.yaml`

`organ-aesthetic.yaml` is a compact contract, not a component library. Read it
as a layer in a cascade:

1. Start with the inherited global taste file named by `inherits`.
2. Apply the organ identity fields: `organ` and `name`.
3. Translate `modifiers` into local UI and editorial choices.
4. Use `specific_references` as optional exemplars, not as required assets.
5. Check the local stylesheet and pages for the implemented version.

| Field | Meaning | Designer use |
|---|---|---|
| `schema_version` | Version of the aesthetic contract shape | Confirms parser and documentation expectations |
| `inherits` | Upstream taste file to resolve first | Prevents organ pages from drifting away from system taste |
| `organ` / `name` | Identity of the organ whose taste is being specialized | Keeps the review scoped to the correct organ |
| `modifiers.palette_shift` | Color-temperature and contrast direction | Guides token changes before selecting individual colors |
| `modifiers.typography_emphasis` | Type hierarchy and font-family emphasis | Guides headings, prose, code, and notation choices |
| `modifiers.tone_shift` | Editorial voice and density | Guides page copy and metadata language |
| `modifiers.visual_shift` | Motifs, diagram density, and layout feel | Guides component composition and media choices |
| `specific_references` | Named references or examples | Grounds subjective calls when populated |

For ORGAN-V (Logos), the local read is: reflective prose, system sans type,
GitHub-dark surfaces, blue accents, compact metadata, and evidence-oriented
visualizations.

## Tokens

<div class="design-token-grid" aria-label="Color token samples">
  <div class="design-token">
    <span class="design-swatch design-swatch-bg"></span>
    <code>--bg</code>
    <span>#0d1117 page background</span>
  </div>
  <div class="design-token">
    <span class="design-swatch design-swatch-surface"></span>
    <code>--surface</code>
    <span>#161b22 code, cards, and tracks</span>
  </div>
  <div class="design-token">
    <span class="design-swatch design-swatch-fg"></span>
    <code>--fg</code>
    <span>#c9d1d9 primary prose</span>
  </div>
  <div class="design-token">
    <span class="design-swatch design-swatch-muted"></span>
    <code>--muted</code>
    <span>#8b949e metadata and captions</span>
  </div>
  <div class="design-token">
    <span class="design-swatch design-swatch-accent"></span>
    <code>--accent</code>
    <span>#58a6ff links, emphasis, bars</span>
  </div>
  <div class="design-token">
    <span class="design-swatch design-swatch-border"></span>
    <code>--border</code>
    <span>#30363d dividers and outlines</span>
  </div>
</div>

## Type And Prose

<div class="design-specimen">
  <p class="meta"><span>March 20, 2026</span><span>13 min</span><span>3,180 words</span></p>
  <h2>Section Heading</h2>
  <p>Long-form pages use a narrow measure, high line-height, and explicit section structure so dense process writing remains scannable.</p>
  <blockquote>Blockquotes mark synthesis, principles, and externally useful framing without changing the reading rhythm.</blockquote>
  <p>Inline code such as <code>organ-aesthetic.yaml</code> is reserved for files, keys, commands, and other exact identifiers.</p>
</div>

## Components

### Navigation And Metadata

<div class="design-specimen">
  <nav class="design-nav-example" aria-label="Design specimen navigation">
    <a href="{{ site.baseurl }}/">Home</a>
    <a href="{{ site.baseurl }}/about/">About</a>
    <a href="{{ site.baseurl }}/design-system/">Design</a>
    <a href="{{ site.baseurl }}/dashboard/">Dashboard</a>
    <a href="{{ site.baseurl }}/feed.xml" class="rss-link">RSS</a>
  </nav>
  <p class="meta">
    <span>Published evidence</span>
    <a href="{{ site.baseurl }}/categories/#methodology" class="category-badge category-methodology">methodology</a>
    <span>reader-facing</span>
  </p>
</div>

### Categories And Tags

<div class="design-specimen">
  <div class="category-chips">
    <a href="{{ site.baseurl }}/categories/#meta-system" class="category-badge category-meta-system">meta-system</a>
    <a href="{{ site.baseurl }}/categories/#case-study" class="category-badge category-case-study">case-study</a>
    <a href="{{ site.baseurl }}/categories/#guide" class="category-badge category-guide">guide</a>
    <a href="{{ site.baseurl }}/categories/#methodology" class="category-badge category-methodology">methodology</a>
    <a href="{{ site.baseurl }}/categories/#retrospective" class="category-badge category-retrospective">retrospective</a>
  </div>
  <p>
    <a href="{{ site.baseurl }}/tags/#aesthetic-system" class="tag">aesthetic-system</a>
    <a href="{{ site.baseurl }}/tags/#design-systems" class="tag">design-systems</a>
    <a href="{{ site.baseurl }}/tags/#creative-governance" class="tag">creative-governance</a>
  </p>
</div>

### Stats

<div class="stat-grid">
  <div class="stat">
    <div class="stat-value">40</div>
    <div class="stat-label">Essays</div>
  </div>
  <div class="stat">
    <div class="stat-value">128k</div>
    <div class="stat-label">Words</div>
  </div>
  <div class="stat">
    <div class="stat-value">5</div>
    <div class="stat-label">Categories</div>
  </div>
</div>

### Bars And Timelines

<div class="design-specimen">
  <div class="bar-chart">
    <div class="bar-row">
      <div class="bar-label">
        <span class="category-badge category-meta-system">meta-system</span>
        <span class="bar-count">16</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill category-fill-meta-system" style="width: 80%"></div>
      </div>
    </div>
    <div class="bar-row">
      <div class="bar-label">
        <span class="category-badge category-methodology">methodology</span>
        <span class="bar-count">12</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill category-fill-methodology" style="width: 60%"></div>
      </div>
    </div>
  </div>
  <div class="timeline">
    <div class="timeline-row">
      <span class="timeline-date">2026-02</span>
      <div class="timeline-bar-track">
        <div class="timeline-bar-fill" style="width: 72%"></div>
      </div>
      <span class="timeline-count">29</span>
    </div>
    <div class="timeline-row">
      <span class="timeline-date">2026-03</span>
      <div class="timeline-bar-track">
        <div class="timeline-bar-fill" style="width: 28%"></div>
      </div>
      <span class="timeline-count">11</span>
    </div>
  </div>
</div>

### Tables And Figures

<div class="design-specimen">
  <table>
    <thead>
      <tr>
        <th>Component</th>
        <th>Use</th>
        <th>Constraint</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Category badge</td>
        <td>Canonical essay category</td>
        <td>Use only the five category colors</td>
      </tr>
      <tr>
        <td>Tag</td>
        <td>Flexible topical metadata</td>
        <td>Keep labels short enough to wrap cleanly</td>
      </tr>
      <tr>
        <td>Stat card</td>
        <td>Dashboard summary number</td>
        <td>One number, one label</td>
      </tr>
    </tbody>
  </table>

  <figure>
    <div class="design-flow" aria-label="Aesthetic cascade">
      <span>taste.yaml</span>
      <span>organ-aesthetic.yaml</span>
      <span>creative brief</span>
      <span>page components</span>
    </div>
    <figcaption>Aesthetic decisions cascade from global taste to local components.</figcaption>
  </figure>
</div>

## UX Review Checklist

- Can a first-time reviewer identify the source of truth for colors, type, and components?
- Does a proposed change preserve the 720px reading measure unless the page is a dashboard or visualization?
- Are metadata, badges, and tags semantically meaningful rather than decorative?
- Does every new visual pattern reuse existing tokens before adding new ones?
- Does the page remain readable at mobile widths and with keyboard focus visible?

## Stranger Test 19 Closure

This page addresses the Session 7 UX designer findings by documenting how to
read `organ-aesthetic.yaml` and by providing visual examples of the UI
components used across Public Process.

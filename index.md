---
layout: default
title: "Public Process"
---

# organvm — Public Process

Essays about building an eight-organ creative-institutional system. Theory, art, commerce, orchestration, community, marketing, and the meta-system that connects them all.

## Start Here

In plain language, ORGAN-V is the writing and publishing layer of ORGANVM. It
takes project work from the rest of the system and turns it into public essays,
methodology notes, dissertation pages, an RSS feed, and machine-readable essay
indexes.

For developers, this repository is a Jekyll site. The main contribution surfaces
are Markdown content, Liquid layouts, includes, CSS, accessibility, navigation,
and generated publishing data.

| If you see this name | Read it as |
|----------------------|------------|
| Logos / ORGAN-V | Public writing and publication |
| Theoria | Theory and knowledge foundations |
| Poiesis | Art and generative systems |
| Ergon | Products and commerce |
| Taxis | Governance and orchestration |
| Koinonia | Community |
| Kerygma | Marketing and distribution |

---

{% assign idx = site.data["essays-index"] %}
<div class="stat-grid">
  <div class="stat">
    <div class="stat-value">{{ idx.total_essays }}</div>
    <div class="stat-label">Essays</div>
  </div>
  <div class="stat">
    <div class="stat-value">{{ idx.total_words | divided_by: 1000 }}k</div>
    <div class="stat-label">Words</div>
  </div>
  <div class="stat">
    <div class="stat-value">{{ idx.categories | size }}</div>
    <div class="stat-label">Categories</div>
  </div>
</div>

## Dissertations

Doctoral-length academic treatments of ORGANVM projects.

{% assign diss_chapters = site.dissertations | where: "dissertation", "precision-pipeline" | sort: "chapter" %}
{% if diss_chapters.size > 0 %}
### [Precision Over Volume]({{ site.baseurl }}/dissertations/)

A ~50,000-word doctoral thesis on career application pipeline optimization. {{ diss_chapters.size }} chapters spanning multi-criteria decision analysis, network theory, portfolio optimization, and formal mathematical proofs.

<div class="meta">
  <span>March 2026</span>
  <span>~50k words</span>
  <a href="{{ site.baseurl }}/dissertations/" class="category-badge category-methodology">dissertation</a>
</div>
{% endif %}

---

## Essays

<div class="category-chips">
  <a href="{{ site.baseurl }}/categories/#meta-system" class="category-badge category-meta-system">meta-system</a>
  <a href="{{ site.baseurl }}/categories/#case-study" class="category-badge category-case-study">case-study</a>
  <a href="{{ site.baseurl }}/categories/#guide" class="category-badge category-guide">guide</a>
  <a href="{{ site.baseurl }}/categories/#methodology" class="category-badge category-methodology">methodology</a>
  <a href="{{ site.baseurl }}/categories/#retrospective" class="category-badge category-retrospective">retrospective</a>
</div>

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

<div class="meta">
  <span>{{ post.date | date: "%B %d, %Y" }}</span>
  {% if post.category %}<a href="{{ site.baseurl }}/categories/#{{ post.category }}" class="category-badge category-{{ post.category }}">{{ post.category }}</a>{% endif %}
  {% if post.reading_time %}<span>{{ post.reading_time }}</span>{% endif %}
</div>

{% if post.excerpt %}{{ post.excerpt }}{% endif %}

{% if post.tags.size > 0 %}
<div class="meta">
  {% for tag in post.tags %}<a href="{{ site.baseurl }}/tags/#{{ tag }}" class="tag">{{ tag }}</a> {% endfor %}
</div>
{% endif %}

---

{% endfor %}

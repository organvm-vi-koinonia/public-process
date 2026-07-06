# Quick Start

This is the first repo to clone when you want to read, run, or contribute to the
Public Process site.

## Which Repo Do I Clone?

Clone `organvm/public-process` first:

```bash
git clone https://github.com/organvm/public-process.git
cd public-process
```

Do not start by cloning the Greek-named repos unless a task specifically sends
you there. Those repos are upstream evidence projects. This repo is the public
essay and documentation layer that explains them.

## Run The Site Locally

Prerequisites:

- Git
- Ruby 3.3, matching `.ruby-version`
- Bundler 4.0.3, matching `Gemfile.lock`

Setup:

```bash
gem install bundler:4.0.3
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/public-process/`.

If port 4000 is already busy, run:

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4001
```

Then open `http://127.0.0.1:4001/public-process/`.

## Validate Before A Pull Request

For a local content or documentation change, run:

```bash
bundle exec jekyll build --strict_front_matter --future
```

CI also checks generated data and cross-repo editorial rules. You usually do not
need those external repos for a first local read-through or small doc fix.

## Where Things Live

- `_posts/` contains dated blog posts that power the feed and index.
- `essays/` contains curated long-form essays.
- `_logs/` contains captain's logs.
- `_dissertations/` contains dissertation-style long-form projects.
- `docs/` contains operational guides, policies, and architecture notes.
- `data/` contains generated JSON/YAML used by the site. Do not edit generated
  data by hand unless the issue asks for it.

## Greek Names Cheat Sheet

The Greek suffixes name the organ's job. They are not steps you must clone in
order.

| Organ | Greek name | Plain meaning | When to open it |
|-------|------------|---------------|-----------------|
| I | theoria | theory | You are checking foundational concepts or recursive engines |
| II | poiesis | art | You are checking generative art or performance systems |
| III | ergon | work/commerce | You are checking products, revenue, or delivery systems |
| IV | taxis | orchestration | You are checking agent routing, governance, or automation |
| V | logos | public process | You are reading or editing this public essay site |
| VI | koinonia | community | You are checking salons, reading groups, or shared practice |
| VII | kerygma | broadcast | You are checking announcements, marketing, or distribution |
| VIII | meta | system coordination | You are checking umbrella registry or cross-organ coordination |

If you are a newcomer and only know "I want to try the project," stay in
`public-process` until an issue or guide names another repo.

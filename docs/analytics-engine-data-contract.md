# analytics-engine Data Contract

This repo consumes analytics artifacts produced by `organvm-v-logos/analytics-engine`.
The contract below is derived from the engine’s own data model and current output
shape.

## Producer/consumer contract

- Producer: `analytics-engine`
- Consumers in this repo: `public-process` content reporting and editorial planning
- Current artifact path: `data/<artifact>.json` in the repository root

## `engagement-metrics.json`

Primary consumer: `public-process`.

```json
{
  "generated_at": "ISO-8601 timestamp",
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "site_totals": {
    "page_views": 0,
    "unique_visitors": 0,
    "referrer_count": 0
  },
  "pages": [
    {
      "path": "/essays/example/",
      "title": "Example Essay",
      "views": 120,
      "unique_visitors": 80,
      "referrers": {
        "github.com": 40,
        "mastodon.social": 20,
        "direct": 60
      }
    }
  ],
  "trends": {
    "views_delta_pct": 12.3,
    "visitors_delta_pct": 8.7
  },
  "attribution": {
    "tracked_pages": 10,
    "tracked_views": 95,
    "tracked_unique_visitors": 72,
    "tracked_views_ratio_pct": 79.2,
    "untagged_views": 25,
    "untagged_unique_visitors": 18,
    "by_source": {
      "github": 40,
      "mastodon": 20,
      "direct": 60
    },
    "by_medium": {
      "social": 40,
      "email": 20,
      "direct": 60
    },
    "by_campaign": {
      "sprint-12-launch": 35,
      "weekly-summary": 20
    }
  }
}
```

### Contract notes

- `period` is the analytics window used by the job run.
- `pages` is sorted in descending visibility for that period.
- `attribution` comes from UTM-normalized parameters (`utm_source`, `utm_medium`,
  `utm_campaign`) and drives distribution quality checks.
- If upstream data is unavailable, values are emitted as null/zero-safe fallbacks.

## `system-engagement-report.json`

Primary consumer: `ORGAN-IV` orchestration workflows.

```json
{
  "generated_at": "ISO-8601 timestamp",
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "web_engagement": {
    "total_views": 150,
    "total_visitors": 120,
    "top_essay": "01-example"
  },
  "distribution": {
    "tracked_views_ratio_pct": 79.2,
    "tracked_views": 95,
    "untagged_views": 25,
    "top_source": "github.com",
    "sources": {
      "github.com": 40,
      "mastodon.social": 20
    },
    "campaigns": {
      "sprint-12-launch": 35,
      "weekly-summary": 20
    }
  },
  "github_activity": {
    "total_commits": 31,
    "total_prs": 7,
    "total_releases": 0,
    "organ_breakdown": {
      "I": {"commits": 5, "prs": 1, "releases": 0},
      "II": {"commits": 3, "prs": 0, "releases": 0},
      "III": {"commits": 8, "prs": 2, "releases": 1},
      "IV": {"commits": 10, "prs": 1, "releases": 0},
      "V": {"commits": 2, "prs": 1, "releases": 0},
      "VI": {"commits": 1, "prs": 1, "releases": 0},
      "VII": {"commits": 2, "prs": 1, "releases": 0},
      "META": {"commits": 0, "prs": 1, "releases": 0}
    }
  },
  "alerts": [
    {
      "rule": "utm_coverage_low",
      "description": "Less than 60% of views include UTM attribution tags",
      "severity": "info",
      "current_value": 42.1,
      "threshold": 60.0,
      "triggered_at": "2026-03-05T04:16:19+00:00"
    }
  ]
}
```

### Contract notes

- `organ_breakdown` includes expected ORGAN keys (`I`..`VII`, `META`).
- `alerts` is an array of threshold events; empty when no thresholds fire.

## `weekly-signals.json`

Consumer: `public-process` status reporting.

```json
{
  "generated_at": "ISO-8601 timestamp",
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "kpis": {
    "page_views": 150,
    "unique_visitors": 120,
    "views_delta_pct": 12.3,
    "visitors_delta_pct": 8.7,
    "tracked_views_ratio_pct": 79.2,
    "total_commits": 31,
    "total_prs": 7,
    "total_releases": 0,
    "alerts_count": 1
  },
  "outcome_progress": {
    "stranger_tests_completed": {"current": 2, "target": 10, "progress_pct": 20.0},
    "external_feedback_items": {"current": 1, "target": 3, "progress_pct": 33.3},
    "external_contributions": {"current": 0, "target": 3, "progress_pct": 0.0},
    "community_events_hosted": {"current": 0, "target": 1, "progress_pct": 0.0},
    "revenue_events": {"current": 0, "target": 1, "progress_pct": 0.0}
  },
  "highlights": {
    "strengths": ["GitHub activity remained healthy (31 commits)."],
    "risks": ["UTM attribution coverage is below target."]
  },
  "recommendations": [
    "Increase UTM-tagged outbound campaigns.",
    "Triage alerts in weekly operations log."
  ]
}
```

`weekly-signals.md` is the markdown mirror of this JSON for publication and review.

## Data ownership and cadence

- Collection period default: rolling 7-day windows.
- Source feed: GoatCounter + GitHub event pull.
- Refresh cadence: Monday 08:00 UTC via `weekly-metrics` workflow, plus manual dispatch.
- Merge/consumption strategy: pull latest artifacts, do not assume continuity from older schema versions.

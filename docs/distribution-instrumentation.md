# Distribution Instrumentation Standard

Defines minimum standards for campaign attribution and distribution telemetry.

## UTM Parameters

For intentional distribution links, include:

- `utm_source` (required): origin channel (`github`, `newsletter`, `mastodon`, etc.)
- `utm_medium` (required): delivery mode (`social`, `email`, `direct`, etc.)
- `utm_campaign` (required): bounded campaign identifier (`sprint-12-launch`, etc.)
- `utm_content` (optional): variant identifier for A/B tests

Example:

```text
https://example.com/path?utm_source=github&utm_medium=social&utm_campaign=sprint-12-launch
```

## Naming Rules

- Lowercase only.
- Hyphen-separated tokens.
- Campaigns must include a timebox or sprint identifier.

## Analytics Contract

`analytics-engine` computes and publishes:

- tracked vs untagged views
- source-level view distribution
- campaign-level view distribution
- tracked view ratio KPI

These metrics are emitted in:

- `data/engagement-metrics.json`
- `data/system-engagement-report.json`
- `data/weekly-signals.{json,md}`

For the exact field-level schema and compatibility notes, use:
- `docs/analytics-engine-data-contract.md`

## Governance

New distribution channels must be added through a documented issue and reflected in campaign naming conventions.

## Data Quality Notes

- `analytics-engine` emits zeros/null-safe values when sources are unavailable, so consumers can keep dashboards and reports stable.
- Attribution (`utm_*`) is optional, and low coverage is reported as a warning condition.

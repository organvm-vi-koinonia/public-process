# Link-health evidence

#54 reproduction at pinned essay-pipeline b152a7c: an HTTP 302 with Location
`/target` raises `ValueError: unknown url type: '/target'`. The upstream
`--internal-only` mode checks HTTP URL syntax and skips relative paths; it is
not live reachability or complete local-route verification.

The consumer now retains upstream URL extraction/report structures but owns a
small HTTP adapter. HTTPX resolves relative/absolute redirects with a bounded
chain, target failures stay broken, HEAD rejection falls back to GET, and timeout,
request/URL errors remain failures. No source URLs or other repository were edited.
Synthetic tests cover those paths and malformed/missing/false-success reports.

Scheduled runs preserve report, source SHA, coverage and raw diagnostics even on
failure. A checker crash writes checker-error; a missing/malformed report creates
a separate diagnostic without destroying the original. No report is published as
site data or treated as fresh audience/input metrics. Artifacts have ordinary
GitHub retention; long-term archive remains #67.

Actual external failures require source-specific historical/correction decisions;
never replace a citation merely to turn the checker green. Relative local routes,
media/image extraction, historical corpus link decisions and a fresh scheduled
HTTP run remain explicit coverage/acceptance items on #54.

## Parser-family follow-through

The live probe exposed seven truncated parenthesized destinations. The consumer
now uses pinned markdown-it-py for body Markdown and parsed YAML strings. This
preserves reference citations while correctly handling balanced/escaped parentheses,
angle destinations, optional titles, images and autolinks; code examples are not
interpreted as live links. Line receipts identify block starts (metadata line 1),
not falsely exact character locations.

The comparison preserves every original citation: 128 regex-derived URLs become
127 parsed URLs. Seven truncated strings disappear; six complete destinations
are added. The seventh, The Long Tail, already existed as a valid angle destination
and is deduplicated. No essay/log was edited. Evidence under
`docs/stewardship/evidence/` retains the original unhealthy 128-URL report and the
complete set difference. Corrected-destination readback is a bounded follow-up,
not a new claim that all external links are healthy.

# Canonical publication origin

Release defect #58: direct readback on 2026-09-13 returned HTTP 404 for the
formerly configured `organvm-v-logos.github.io/public-process/` and HTTP 200 for
`https://organvm-vi-koinonia.github.io/public-process/release-manifest.json`.

The canonical site is https://organvm-vi-koinonia.github.io/public-process/.
The repository is https://github.com/organvm-vi-koinonia/public-process.
Configuration and current operational documentation now point there. Historical
posts, logs, essays and research sources retain their original references.
No old host redirect is claimed; GitHub Pages host ownership is not changed here.
Existing route/permalink paths remain unchanged; only the origin is corrected.

The production workflow checks generated homepage canonical, feed and sitemap
against that origin. Verify the deployed release receipt and selected rendered
files after merge. This repairs active discovery; it does not complete the broader
root-layout decision or historical reference inventory in #58/#56.

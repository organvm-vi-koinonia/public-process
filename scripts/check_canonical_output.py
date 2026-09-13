"""Check the generated homepage/feed/sitemap use the configured canonical origin."""
from pathlib import Path
import re
import yaml


def check(site=Path('_site')):
    config = yaml.safe_load(Path('_config.yml').read_text())
    expected = config['url'] + config['baseurl']
    if expected != 'https://organvm-vi-koinonia.github.io/public-process':
        raise SystemExit('Canonical origin differs from verified repository Pages host')
    text = (site / 'index.html').read_text()
    canonical = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', text)
    if not canonical:
        canonical = re.search(r'<link[^>]+href="([^"]+)"[^>]+rel="canonical"', text)
    if not canonical or not canonical.group(1).startswith(expected + '/'):
        raise SystemExit('Homepage canonical does not match configured origin')
    for name in ['feed.xml', 'sitemap.xml']:
        content = (site / name).read_text()
        if expected not in content:
            raise SystemExit(f'{name} missing canonical origin')
    print('Canonical homepage/feed/sitemap verified:', expected)


if __name__ == '__main__':
    check()

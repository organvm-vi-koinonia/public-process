"""Public Process HTTP adapter using the pinned pipeline's extraction/report contract."""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '_pipeline'))
from src.link_checker import Report, UrlResult, generate_report
from markdown_links import extract_urls


def check_one(url, client, timeout=15, retries=2):
    for attempt in range(retries + 1):
        try:
            response = client.request('HEAD', url, timeout=timeout, follow_redirects=True)
            if response.status_code in {403, 405}:
                response = client.request('GET', url, timeout=timeout, follow_redirects=True)
            if response.status_code >= 400:
                if attempt < retries:
                    continue
                return UrlResult(url, 'broken', status_code=response.status_code)
            if 300 <= response.status_code < 400:
                return UrlResult(url, 'error', status_code=response.status_code, error='Unresolved redirect target')
            if response.history:
                return UrlResult(url, 'redirect', status_code=response.history[0].status_code, redirect_url=str(response.url))
            return UrlResult(url, 'ok', status_code=response.status_code)
        except httpx.TimeoutException as error:
            result = UrlResult(url, 'timeout', error=str(error))
        except (httpx.HTTPError, httpx.InvalidURL, ValueError) as error:
            result = UrlResult(url, 'error', error=f'{type(error).__name__}: {error}')
        if attempt == retries:
            return result


def run(output, timeout=15, retries=2):
    report = Report()
    try:
        for collection in ['_posts', '_logs']:
            paths = sorted((ROOT / collection).glob('*.md'))
            if not paths:
                raise ValueError(f'Missing corpus: {collection}')
            for path in paths:
                entries = extract_urls(path)
                for entry in entries:
                    entry.file = path.relative_to(ROOT).as_posix()
                report.entries.extend(entries)
        urls = sorted({entry.url for entry in report.entries})
        with httpx.Client(max_redirects=10, headers={'User-Agent': 'PublicProcess-LinkHealth/1.0'}) as client:
            for index, url in enumerate(urls, 1):
                result = check_one(url, client, timeout, retries)
                report.results[url] = result
                print(f'{index}/{len(urls)} {result.status} {url}', flush=True)
                # Bounded courtesy interval; no unbounded retries or redirect chains.
                time.sleep(0.2)
        payload = generate_report(report)
        counts = payload['summary']
        failed = counts['broken'] + counts['timeout'] + counts['error']
        payload['state'] = 'unhealthy' if failed else 'success'
        code = 1 if failed else 0
    except Exception as error:
        payload = generate_report(report)
        payload.update(state='checker-error', diagnostic=f'{type(error).__name__}: {error}')
        code = 1
    payload['source_sha'] = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    payload['coverage'] = 'Markdown HTTP links/images in post/log bodies and YAML strings; block-start lines (metadata line 1); plaintext/relative links not covered'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + '\n')
    return code


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / '.link-health/report.json')
    parser.add_argument('--timeout', type=float, default=15)
    parser.add_argument('--retries', type=int, default=2)
    args = parser.parse_args()
    if args.timeout <= 0 or args.retries < 0:
        parser.error('timeout must be positive and retries nonnegative')
    raise SystemExit(run(args.output, args.timeout, args.retries))

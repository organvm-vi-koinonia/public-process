"""Retain missing/malformed checker reports as explicit failures, not empty success."""
import json
import sys
from pathlib import Path


def summarize(path):
    try:
        report = json.loads(path.read_text())
        if not isinstance(report, dict) or not isinstance(report.get('summary'), dict):
            raise ValueError('missing summary')
        summary = report['summary']
        for key in ['total', 'ok', 'redirect', 'broken', 'timeout', 'error']:
            if type(summary.get(key)) is not int or summary[key] < 0:
                raise ValueError(f'invalid count: {key}')
        if summary['total'] != sum(summary[k] for k in ['ok', 'redirect', 'broken', 'timeout', 'error']):
            raise ValueError('counts do not add up')
        if not isinstance(report.get('broken'), list) or not isinstance(report.get('redirects'), list):
            raise ValueError('invalid result lists')
        if report.get('state') not in {'success', 'unhealthy', 'checker-error'}:
            raise ValueError('missing checker state')
        print(json.dumps({'state': report['state'], 'summary': summary, 'source_sha': report.get('source_sha')}))
        return 0 if report['state'] == 'success' and summary['total'] > 0 and not any(summary[k] for k in ['broken', 'timeout', 'error']) else 1
    except (OSError, ValueError, TypeError) as error:
        path.parent.mkdir(parents=True, exist_ok=True)
        diagnostic = path.with_name('report-diagnostic.json')
        diagnostic.write_text(json.dumps({'state': 'checker-error', 'diagnostic': str(error)}) + '\n')
        print(f'Report unavailable or invalid; retained diagnostic at {diagnostic}')
        return 1


if __name__ == '__main__':
    raise SystemExit(summarize(Path(sys.argv[1])))

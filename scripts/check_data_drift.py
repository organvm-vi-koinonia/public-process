"""Fail on semantic, missing or new generated data; retain reviewed timestamps."""
import json
import subprocess
from pathlib import Path


def equivalent(before, after):
    try:
        left, right = json.loads(before), json.loads(after)
    except (ValueError, UnicodeError):
        return before == after
    if isinstance(left, dict) and isinstance(right, dict):
        left.pop('updated', None)
        right.pop('updated', None)
    return left == right


def check(root=Path('.')):
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args])
    tracked = git('ls-files', '-z', '--', 'data/').decode().split('\0')
    tracked = {p for p in tracked if p}
    current = {p.relative_to(root).as_posix() for p in (root / 'data').rglob('*') if p.is_file()}
    drift = sorted(current ^ tracked)
    for name in sorted(current & tracked):
        before = git('show', f'HEAD:{name}')
        path = root / name
        after = path.read_bytes()
        if not equivalent(before, after):
            drift.append(name)
        elif before != after:
            # Build from reviewed bytes, not today's timestamp-only regeneration.
            path.write_bytes(before)
    if drift:
        raise SystemExit('Generated data drift: ' + ', '.join(drift))
    print('Generated data matches reviewed source')


if __name__ == '__main__':
    check()

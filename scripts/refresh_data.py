"""Run refresh modules from their pinned checkout, never from caller cwd."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from check_data_drift import equivalent

ROOT = Path(__file__).resolve().parents[1]


def run(check=False):
    def execute(args, cwd=ROOT):
        subprocess.run(args, cwd=cwd, check=True)
    def snapshot():
        return {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in (ROOT / 'data').rglob('*') if p.is_file()}
    before = snapshot()
    execute([sys.executable, '-m', 'src.validator', '--posts-dir', '../_posts/', '--schema', '../_standards/schemas/frontmatter-schema.yaml'], ROOT / '_pipeline')
    execute([sys.executable, str(ROOT / 'scripts/validate_logs.py')])
    command = [sys.executable, '-m', 'src.indexer', '--posts-dir', '../_posts/', '--logs-dir', '../_logs/', '--output-dir', '../data/']
    execute(command, ROOT / '_pipeline')
    first = snapshot()
    execute(command, ROOT / '_pipeline')
    after = snapshot()
    if first.keys() != after.keys() or any(not equivalent(first[p], after[p]) for p in first):
        raise SystemExit('Repeated refresh was not semantically deterministic')
    changed = sorted(before.keys() ^ after.keys())
    for name in sorted(before.keys() & after.keys()):
        if equivalent(before[name], after[name]):
            (ROOT / name).write_bytes(before[name])
        else:
            changed.append(name)
    sha = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    receipt = {'source_sha': sha, 'changed': sorted(changed), 'repeated_semantic_match': True}
    (ROOT / '.refresh-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))
    if check and changed:
        raise SystemExit('Refresh changes reviewed data')
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    run(parser.parse_args().check)

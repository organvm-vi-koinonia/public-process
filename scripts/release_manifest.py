"""Write a deterministic source receipt and file hashes for the validated site."""
import hashlib
import json
import subprocess
from pathlib import Path


def manifest(site=Path('_site')):
    if not (site / 'index.html').is_file():
        raise SystemExit('Missing site index')
    def head(path):
        return subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip()
    files = {}
    for path in sorted(site.rglob('*')):
        if path.is_symlink():
            raise SystemExit('Symlink in publication artifact')
        if path.is_file() and path.name != 'release-manifest.json':
            files[path.relative_to(site).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    receipt = {'schema_version': 1, 'source_sha': head('.'),
               'dependencies': {'essay-pipeline': head('_pipeline'), 'editorial-standards': head('_standards')},
               'files': files}
    (site / 'release-manifest.json').write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
    print('Validated source:', receipt['source_sha'], 'files:', len(files))


if __name__ == '__main__':
    manifest()

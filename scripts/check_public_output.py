"""Reject explicit private/draft material before publication; never infer rights."""
from pathlib import Path
import sys
import yaml

EXCLUDED = {'.git', '_pipeline', '_standards', '_site', 'vendor', 'tests', 'scripts'}
PRIVATE_DIRS = {'_private', 'private', '_drafts', 'drafts'}


def source_errors(root):
    errors = []
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in EXCLUDED or part.startswith('.') for part in relative.parts):
            continue
        if not path.is_file():
            continue
        if any(part in PRIVATE_DIRS for part in relative.parts):
            errors.append(f'{relative}: private/draft source must remain outside public git')
            continue
        if path.suffix.lower() not in {'.md', '.html', '.markdown'}:
            continue
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            continue
        parts = text.split('---', 2)
        if len(parts) != 3:
            errors.append(f'{relative}: malformed frontmatter')
            continue
        try:
            fields = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            errors.append(f'{relative}: malformed frontmatter')
            continue
        if not isinstance(fields, dict):
            errors.append(f'{relative}: frontmatter must be a mapping')
            continue
        if fields.get('visibility') in {'private', 'restricted'} or fields.get('private') is True or fields.get('draft') is True or fields.get('published') is False:
            errors.append(f'{relative}: explicitly non-public source')
    return errors


def output_errors(site):
    errors = []
    for path in site.rglob('*'):
        relative = path.relative_to(site)
        if path.is_symlink() or any(part in PRIVATE_DIRS | {'tests', 'scripts', '.git', '_pipeline', '_standards'} for part in relative.parts):
            errors.append(f'{relative}: prohibited output surface')
    return errors


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'source'
    if mode not in {'source', 'output'}:
        raise SystemExit('Expected source or output')
    errors = source_errors(Path('.')) if mode == 'source' else output_errors(Path('_site'))
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Public {mode} boundary passed; rights/author identity are separate evidence')

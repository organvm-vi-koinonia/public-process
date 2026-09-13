"""Validate daily logs and preservation receipts without inventing an author's mood."""
import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '_pipeline'))
from src.schema_loader import load_schema
from src.validator import extract_frontmatter, validate_entry


def preservation_schema(daily):
    schema = copy.deepcopy(daily)
    mood = schema['required_fields'].pop('mood')
    schema.setdefault('optional_fields', {})['mood'] = mood
    schema['required_fields'].update({
        'status': {'type': 'string', 'enum': ['approved-for-preservation']},
        'approval_recorded': {'type': 'string', 'pattern': r'^\d{4}-\d{2}-\d{2}$'},
        'evidence_cutoff': {'type': 'string', 'pattern': r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})$'},
    })
    return schema


def validate(path, daily):
    fields = extract_frontmatter(path)
    preservation = isinstance(fields, dict) and fields.get('status') == 'approved-for-preservation'
    return validate_entry(path, preservation_schema(daily) if preservation else daily)


def main():
    daily = load_schema('_standards/schemas/log-schema.yaml')
    paths = sorted(Path('_logs').glob('*.md'))
    if not paths:
        raise SystemExit('Missing log corpus')
    errors = [error for path in paths for error in validate(path, daily)]
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated {len(paths)} daily logs / preservation receipts')


if __name__ == '__main__':
    main()

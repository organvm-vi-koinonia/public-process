"""Validate coordinator claim records; this is not a distributed lock service."""
from datetime import datetime, timezone
from pathlib import PurePosixPath
import json
import re
import sys


def overlaps(a, b):
    return a == '.' or b == '.' or a == b or a.startswith(b.rstrip('/') + '/') or b.startswith(a.rstrip('/') + '/')


def validate_claim(claim, now):
    for field in ['id', 'issue', 'executor', 'reviewer', 'branch', 'base_sha', 'paths', 'outputs', 'expires_at', 'checkpoint', 'dependency_receipts']:
        if field not in claim:
            raise ValueError(f'Missing claim field: {field}')
    if not claim['executor'] or not claim['reviewer'] or claim['executor'] == claim['reviewer']:
        raise ValueError('An active claim needs a distinct named reviewer')
    if type(claim['issue']) is not int or claim['issue'] < 1:
        raise ValueError('Invalid issue')
    if not re.fullmatch(r'[a-f0-9]{40}', claim['base_sha']):
        raise ValueError('Exact base SHA required')
    if not re.fullmatch(r'(docs|fix|test|feat|chore|hotfix|work)/[a-z0-9][a-z0-9/_-]*', claim['branch']):
        raise ValueError('Invalid working branch')
    expiry = datetime.fromisoformat(claim['expires_at'].replace('Z', '+00:00'))
    if expiry.tzinfo is None or expiry <= now:
        raise ValueError('Claim expired or missing timezone; park with residue before reassignment')
    if not isinstance(claim['paths'], list) or not claim['paths']:
        raise ValueError('Nonempty literal path scope required')
    for path in claim['paths']:
        if not isinstance(path, str) or not path or PurePosixPath(path).is_absolute() or path != PurePosixPath(path).as_posix() or '..' in PurePosixPath(path).parts or any(c in path for c in '*?[]\\'):
            raise ValueError('Paths must be repository-relative literal prefixes')
    for field in ['outputs', 'dependency_receipts']:
        if not isinstance(claim[field], list) or any(not isinstance(v, str) or not v for v in claim[field]):
            raise ValueError(f'Invalid {field}')


def admit(existing, candidate, now):
    validate_claim(candidate, now)
    for claim in existing:
        if claim['id'] == candidate['id']:
            raise ValueError('Claim ID must be unique; handoff appends a successor')
        if claim.get('status') in {'parked', 'completed', 'handed-off'}:
            continue
        validate_claim(claim, now)
        if claim['branch'] == candidate['branch'] or set(claim['outputs']) & set(candidate['outputs']) or any(overlaps(a, b) for a in claim['paths'] for b in candidate['paths']):
            raise ValueError(f'Collision with {claim["id"]}')
    return [*existing, {**candidate, 'status': 'active'}]


if __name__ == '__main__':
    data = json.load(sys.stdin)
    result = admit(data['existing'], data['candidate'], datetime.now(timezone.utc))
    print(json.dumps(result, indent=2))

from datetime import datetime, timezone
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from claim_contract import admit


class CoordinationSimulation(unittest.TestCase):
    def claim(self, identifier, path):
        return dict(id=identifier, issue=57, executor='executor-A', reviewer='reviewer-B', branch='docs/57-' + identifier, base_sha='a'*40, paths=[path], outputs=[], expires_at='2030-01-02T00:00:00Z', checkpoint='review diff', dependency_receipts=['issue47'])

    def test_collision_expiry_and_handoff_preserve_old_work(self):
        now = datetime(2030, 1, 1, tzinfo=timezone.utc)
        a = self.claim('first', 'docs')
        records = admit([], a, now)
        b = self.claim('second', 'docs/operations')
        b.update(executor='executor-C', reviewer='reviewer-D')
        with self.assertRaisesRegex(ValueError, 'Collision'): admit(records, b, now)
        records[0]['expires_at'] = '2029-12-31T00:00:00Z'
        with self.assertRaisesRegex(ValueError, 'expired'): admit(records, b, now)
        records[0].update(status='handed-off', successor='second', residue='branch/head retained; no deletion')
        result = admit(records, b, now)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['residue'], records[0]['residue'])
        self.assertEqual(result[1]['executor'], 'executor-C')

    def test_shared_output_and_self_review_fail(self):
        now = datetime(2030, 1, 1, tzinfo=timezone.utc)
        a, b = self.claim('one', 'data'), self.claim('two', 'scripts')
        a['outputs'] = b['outputs'] = ['generated-indexes']
        with self.assertRaisesRegex(ValueError, 'Collision'): admit(admit([], a, now), b, now)
        b['reviewer'] = b['executor']
        with self.assertRaisesRegex(ValueError, 'distinct'): admit([], b, now)

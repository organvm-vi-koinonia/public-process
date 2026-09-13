import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

class RefreshContract(unittest.TestCase):
    def test_pins_match_and_no_default_push(self):
        def pins(name):
            workflow = yaml.safe_load((ROOT / '.github/workflows' / name).read_text())
            return {s['with']['repository']: s['with']['ref'] for job in workflow['jobs'].values() for s in job.get('steps', []) if 'repository' in s.get('with', {})}
        self.assertEqual(pins('data-refresh.yml'), pins('validate-publication.yml'))
        workflow = (ROOT / '.github/workflows/data-refresh.yml').read_text()
        self.assertIn('git push origin "HEAD:refs/heads/$BRANCH"', workflow)
        self.assertNotIn('git push\n', workflow)
        self.assertNotIn('--force', workflow)
        self.assertIn('gh pr create --base main', workflow)

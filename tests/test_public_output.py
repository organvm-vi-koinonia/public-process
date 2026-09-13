import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('boundary', ROOT / 'scripts/check_public_output.py')
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)


class PublicBoundary(unittest.TestCase):
    def test_nonpublic_metadata_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'page.md'
            for marker in ['visibility: private', 'visibility: restricted', 'private: true', 'draft: true', 'published: false']:
                path.write_text(f'---\n{marker}\n---\nSynthetic canary\n')
                self.assertTrue(boundary.source_errors(root), marker)
            path.write_text('---\ntitle: Public example\n---\nApproved fixture\n')
            self.assertEqual(boundary.source_errors(root), [])

    def test_private_directory_and_output_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'private').mkdir()
            (root / 'private/canary.txt').write_text('SYNTHETIC-NONPRIVATE-TEST')
            self.assertTrue(boundary.source_errors(root))
            self.assertTrue(boundary.output_errors(root))

    def test_dispatch_requires_more_than_a_push(self):
        import yaml
        path = ROOT / '.github/workflows/notify-essay-published.yml'
        workflow = yaml.safe_load(path.read_text())
        triggers = workflow.get('on', workflow.get(True))
        self.assertNotIn('push', triggers)
        self.assertNotIn('secrets', workflow['jobs']['approval-status'])

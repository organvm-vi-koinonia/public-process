import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('drift', ROOT / 'scripts/check_data_drift.py')
drift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drift)


class DataContract(unittest.TestCase):
    def test_only_top_level_timestamp_is_ignored(self):
        self.assertTrue(drift.equivalent('{"updated":"old","a":[1]}', '{"a":[1],"updated":"new"}'))
        self.assertFalse(drift.equivalent('{"a":{"updated":1}}', '{"a":{"updated":2}}'))
        self.assertFalse(drift.equivalent('[1]', '[2]'))
        self.assertFalse(drift.equivalent('broken', '{}'))

    def test_new_deleted_and_semantic_data_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '-q', directory], check=True)
            (root / 'data').mkdir()
            p = root / 'data/a.json'
            p.write_text('{"updated":"old","a":1}')
            subprocess.run(['git', '-C', directory, 'add', '.'], check=True)
            subprocess.run(['git', '-C', directory, '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture'], check=True)
            p.write_text('{"updated":"new","a":1}')
            drift.check(root)
            self.assertIn('old', p.read_text())
            p.write_text('{"a":2}')
            with self.assertRaises(SystemExit): drift.check(root)
            p.unlink()
            with self.assertRaises(SystemExit): drift.check(root)
            p.write_text('{"updated":"old","a":1}')
            (root / 'data/new.json').write_text('{}')
            with self.assertRaises(SystemExit): drift.check(root)


class WorkflowContract(unittest.TestCase):
    def test_pages_requires_same_validation_as_ci(self):
        def load(name):
            return yaml.safe_load((ROOT / '.github/workflows' / name).read_text())
        ci, pages = load('ci.yml'), load('pages.yml')
        self.assertEqual(ci['jobs']['validate']['uses'], pages['jobs']['build']['uses'])
        self.assertEqual(pages['jobs']['deploy']['needs'], 'build')
        self.assertEqual(pages['jobs']['build']['if'], "github.ref == 'refs/heads/main'")
        shared = load('validate-publication.yml')
        steps = shared['jobs']['validate']['steps']
        names = [step.get('name') for step in steps]
        self.assertLess(names.index('Validate log frontmatter'), names.index('Build production artifact'))
        self.assertLess(names.index('Check data drift'), names.index('Build production artifact'))
        self.assertLess(names.index('Record source and artifact manifest'), names.index('Upload validated Pages artifact'))
        for step in steps:
            if 'repository' in step.get('with', {}):
                self.assertRegex(step['with']['ref'], r'^[a-f0-9]{40}$')
            self.assertFalse(step.get('continue-on-error', False))


if __name__ == '__main__':
    unittest.main()

class LogContract(unittest.TestCase):
    def test_preservation_requires_receipt_and_daily_requires_mood(self):
        import sys
        sys.path.insert(0, str(ROOT / 'scripts'))
        from validate_logs import validate, load_schema
        daily = load_schema(str(ROOT / '_standards/schemas/log-schema.yaml'))
        source = (ROOT / '_logs/2026-09-11-weekly-accomplishments-preservation.md').read_text()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'entry.md'
            path.write_text(source)
            self.assertEqual(validate(path, daily), [])
            path.write_text(source.replace('approval_recorded:', 'unknown:'))
            self.assertTrue(validate(path, daily))
            path.write_text('---\nlayout: log\ntitle: Daily example\ndate: "2026-09-13"\ntags: [test]\n---\nTest\n')
            self.assertTrue(any('mood' in e for e in validate(path, daily)))

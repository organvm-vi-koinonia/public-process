import sys
import tempfile
import unittest
from pathlib import Path
import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from link_health import check_one
from summarize_link_report import summarize


class HTTPContract(unittest.TestCase):
    def test_relative_absolute_and_broken_redirect_targets(self):
        for location, code, expected in [('/target', 200, 'redirect'), ('https://other.test/target', 200, 'redirect'), ('/target', 404, 'broken')]:
            def serve(request):
                return httpx.Response(302, headers={'location': location}) if request.url.path == '/start' else httpx.Response(code)
            with httpx.Client(transport=httpx.MockTransport(serve)) as client:
                result = check_one('https://example.test/start', client, retries=0)
                self.assertEqual(result.status, expected)
                if expected == 'redirect': self.assertTrue(result.redirect_url.startswith('https://'))

    def test_timeout_loop_and_get_fallback(self):
        def timeout(request): raise httpx.ReadTimeout('synthetic timeout')
        with httpx.Client(transport=httpx.MockTransport(timeout)) as client:
            self.assertEqual(check_one('https://example.test/', client, retries=0).status, 'timeout')
        with httpx.Client(max_redirects=2, transport=httpx.MockTransport(lambda r: httpx.Response(302, headers={'location': '/loop'}))) as client:
            self.assertEqual(check_one('https://example.test/', client, retries=0).status, 'error')
        with httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(405 if r.method == 'HEAD' else 200))) as client:
            self.assertEqual(check_one('https://example.test/', client, retries=0).status, 'ok')

    def test_missing_malformed_and_false_success_reports_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'report.json'
            self.assertEqual(summarize(path), 1)
            path.write_text('{broken')
            self.assertEqual(summarize(path), 1)
            self.assertEqual(path.read_text(), '{broken')
            path.write_text('{"state":"success","summary":{}}')
            self.assertEqual(summarize(path), 1)

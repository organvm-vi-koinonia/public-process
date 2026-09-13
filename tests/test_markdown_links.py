from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from markdown_links import extract_urls


class MarkdownDestinations(unittest.TestCase):
    def urls(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'fixture.md'
            path.write_text(text)
            return [entry.url for entry in extract_urls(path)]

    def test_balanced_escaped_angle_title_and_reference(self):
        text = r'''[book](https://example.test/book_(edition))
[escaped](https://example.test/a_\(b\))
[angle](<https://example.test/a_(c)>)
[title](https://example.test/title "title")
[reference][ref]

[ref]: https://example.test/reference_(one)
'''
        self.assertEqual(self.urls(text), ['https://example.test/book_(edition)', 'https://example.test/a_(b)', 'https://example.test/a_(c)', 'https://example.test/title', 'https://example.test/reference_(one)'])

    def test_images_autolinks_duplicates_and_code(self):
        text = '''![image](https://example.test/image.png)
<https://example.test/auto>
[duplicate](https://example.test/auto)
`[inline](https://example.test/not-a-link)`
```
[fenced](https://example.test/not-a-link-either)
```
[local](./local.md)
'''
        self.assertEqual(self.urls(text), ['https://example.test/image.png', 'https://example.test/auto'])

    def test_yaml_reference_strings_keep_their_citations(self):
        self.assertEqual(self.urls('---\ntitle: "[not-body](https://example.test/private-contract)"\n---\n[body](https://example.test/body)\n'), ['https://example.test/private-contract', 'https://example.test/body'])

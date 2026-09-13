"""Extract Markdown destinations without truncating parentheses or reading code as links."""
from pathlib import Path
import sys
import yaml
from urllib.parse import urlparse
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '_pipeline'))
from src.link_checker import UrlEntry


def extract_urls(filepath):
    text = filepath.read_text(encoding='utf-8')
    # Parse YAML separately so quoted reference strings retain their citations.
    chunks = []
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end >= 0:
            metadata = yaml.safe_load(text[4:end])
            def strings(value):
                if isinstance(value, str):
                    yield value
                elif isinstance(value, dict):
                    for item in value.values(): yield from strings(item)
                elif isinstance(value, list):
                    for item in value: yield from strings(item)
            chunks.extend((value, 0) for value in strings(metadata))
            prefix = text[:end + 4]
            text = '\n' * prefix.count('\n') + text[end + 4:]
    chunks.append((text, 0))
    entries, seen = [], set()
    for chunk, offset in chunks:
        for token in MarkdownIt('commonmark').parse(chunk):
            for child in token.children or []:
                url = child.attrGet('href') if child.type == 'link_open' else child.attrGet('src') if child.type == 'image' else None
                if not url or urlparse(url).scheme not in {'http', 'https'} or url in seen:
                    continue
                seen.add(url)
                entries.append(UrlEntry(url=url, file=str(filepath), line=offset + (token.map[0] + 1) if token.map else 1, context=token.content[:120]))
    return entries

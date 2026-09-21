#!/usr/bin/env python3
"""Build the signature installer page from the generated per-attorney signatures.

The preview points at image files published alongside the page (the artifact CSP
blocks third-party images). What the Copy button puts on the clipboard is the
untouched markup, still pointing at www.ssuder.com — a mail client has to fetch
those from the live site, not carry them inline.
"""
import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
sys.path.insert(0, str(REPO / 'src'))
from site_content import TEAM

PEOPLE = [t for t in TEAM if 'non-attorney' not in t['role']]
FIRST = 'sean-suder'

def load(slug):
    src = (REPO / f'src/signature/signature-{slug}.html').read_text()
    return src[src.index('<table'):].rstrip()

def local(sig):
    return re.sub(r'https://www\.ssuder\.com/assets/img/([^"]+)', r'img/\1', sig)

indent = lambda s, n: "\n".join(" " * n + l for l in s.splitlines())

stages, payloads, tabs = "", "", ""
for t in PEOPLE:
    slug, sig = t['slug'], load(t['slug'])
    first = slug == FIRST
    short = t['name'].split(' ')[0] if slug != 'sean-suder' else 'Sean'
    if slug == 'jp-burleigh': short = 'J.P.'
    stages += (f'\n    <div class="stage" id="sig-{slug}"{"" if first else " hidden"}>\n'
               + indent(local(sig), 6) + '\n    </div>')
    payloads += (f'<script type="text/plain" id="src-{slug}">\n{sig}\n</' + 'script>\n')
    tabs += (f'\n      <button type="button" class="tab" data-slug="{slug}"'
             f'{" aria-current=&quot;true&quot;" if first else ""}>{short}</button>')
tabs = tabs.replace('&quot;', '"')

files = sorted({m for t in PEOPLE for m in re.findall(r'assets/img/([^"]+)', load(t['slug']))})
Path(HERE / 'images.txt').write_text("\n".join(files))

page = (HERE / 'template.html').read_text()
page = page.replace('<!--TABS-->', tabs).replace('<!--STAGES-->', stages).replace('<!--PAYLOADS-->', payloads)
out = HERE / 'signature-installer.html'
out.write_text(page)
print(f'built {out.name}: {len(page)//1024} KB, {len(PEOPLE)} people, {len(files)} images to publish')

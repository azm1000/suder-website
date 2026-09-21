#!/usr/bin/env python3
"""Build install packages for classic desktop Outlook on Windows.

    python3 src/signature/make_outlook_package.py

Classic Outlook stores signatures as .htm files in %APPDATA%\\Microsoft\\Signatures,
with each signature's images in a sibling folder named <signature>_files. Dropping
the files in there skips the clipboard altogether, which is what fails when Outlook
cannot fetch a remote image while pasting: the text arrives and the graphics do not.

Images are referenced relatively, so Outlook embeds them into outgoing mail instead
of hotlinking. That costs about 380 KB per message but does not depend on the
website being reachable from the recipient's mail client.
"""
import re, shutil, sys, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
IMG = REPO / 'public' / 'assets' / 'img'
DIST = HERE / 'dist-outlook'
NAME = 'Suder'                      # the signature name, and so the folder name

sys.path.insert(0, str(REPO / 'src'))
from site_content import TEAM

DOC = '''<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<meta name="Generator" content="Suder, LLC">
<title>{name}</title>
</head>
<body lang="EN-US" style="margin:0;padding:0">
{table}
</body>
</html>
'''

def build(t):
    src = (HERE / f'signature-{t["slug"]}.html').read_text()
    table = src[src.index('<table'):].rstrip()
    imgs = sorted(set(re.findall(r'https://www\.ssuder\.com/assets/img/([^"]+)', table)))
    local = re.sub(r'https://www\.ssuder\.com/assets/img/', f'{NAME}_files/', table)

    person = HERE.joinpath('..').resolve() and DIST / t['name'].replace(' ', '-')
    files = person / f'{NAME}_files'
    files.mkdir(parents=True, exist_ok=True)
    (person / f'{NAME}.htm').write_text(DOC.format(name=t['name'], table=local), encoding='cp1252')
    for n in imgs:
        shutil.copy(IMG / n, files / n)
    return person, len(imgs)

if __name__ == '__main__':
    if DIST.exists(): shutil.rmtree(DIST)
    people = [t for t in TEAM if 'non-attorney' not in t['role']]
    for t in people:
        person, n = build(t)
        print(f'{t["name"]:20} {person.name}/{NAME}.htm + {NAME}_files/ ({n} images)')

    zpath = HERE / 'suder-outlook-signatures.zip'
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(DIST.rglob('*')):
            if f.is_file(): z.write(f, f.relative_to(DIST))
    print(f'\n{zpath.name}: {zpath.stat().st_size//1024} KB')

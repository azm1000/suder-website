#!/usr/bin/env python3
"""Render the email-signature tagline reel to animated GIFs.

Not part of build.py; run by hand when the practice areas or the wording change:

    npm i -g playwright && pip install Pillow
    python3 src/signature/make_gif.py

Writes public/assets/img/signature-tagline-reel{,-loop}.gif and -static.png.
Frame 1 is the settled line on purpose: Outlook for Windows shows only the first
frame of a GIF, so a client that will not animate still reads the tagline.
"""
import json, os, subprocess, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "public" / "assets" / "img"
TMP = HERE / ".frames"
SCALE = 2          # render at 2x, display at half size for retina
COLORS = 16        # text on white quantizes cleanly; keeps the file ~110 KB
# Sample each slide finely and each rest once. The rest frame then carries the
# whole dwell as its duration, so a readable pause costs one frame, not twelve.
SLIDE, DWELL, STEPS = 140, 360, 8
def _times():
    out, cycle = [0], SLIDE + DWELL
    for k in range(STEPS):
        base, span = k * cycle, SLIDE * 1.9 if k == STEPS - 1 else SLIDE
        t = 35
        while t < span:
            out.append(round(base + t)); t += 35
        out.append(round(base + span))          # the rest position
    return out
TIMES = _times()

SHOOT = """
const { chromium } = require('playwright');
(async () => {
  const cfg = %s;
  const b = await chromium.launch();
  const c = await b.newContext({viewport:{width:900,height:200}, deviceScaleFactor:cfg.scale, ignoreHTTPSErrors:true});
  const p = await c.newPage();
  await p.goto('file://' + cfg.page, {waitUntil:'networkidle'});
  // Gate on the real faces: a fallback render silently changes the metrics.
  await p.evaluate(() => Promise.all([
    document.fonts.load('400 22px Fraunces'), document.fonts.load('italic 400 22px Fraunces')
  ]).then(() => document.fonts.ready));
  const ok = await p.evaluate(() =>
    [...document.fonts].filter(f => f.family === 'Fraunces' && f.status === 'loaded').length >= 2);
  if (!ok) { console.error('Fraunces did not load from src/signature/fonts/'); process.exit(1); }
  await p.waitForTimeout(300);
  await p.evaluate(() => window.measure());
  const stage = p.locator('#stage');
  for (let i = 0; i < cfg.times.length; i++) {
    await p.evaluate(t => window.render(t), cfg.times[i]);
    await stage.screenshot({path: cfg.dir + '/' + String(i).padStart(3,'0') + '.png'});
  }
  await b.close();
})();
"""

def main():
    TMP.mkdir(exist_ok=True)
    for old in TMP.glob("*.png"): old.unlink()
    cfg = {"page": str(HERE / "reel.html"), "dir": str(TMP), "times": TIMES, "scale": SCALE}
    env = dict(os.environ, NODE_PATH=os.environ.get("NODE_PATH", "/opt/node22/lib/node_modules"))
    subprocess.run(["node", "-e", SHOOT % json.dumps(cfg)], check=True, env=env)

    frames = [Image.open(p).convert("RGB") for p in sorted(TMP.glob("*.png"))]
    if not frames: sys.exit("no frames rendered")
    w, h = frames[0].size
    if len({f.size for f in frames}) != 1: sys.exit("frame sizes differ; font probably loaded late")
    # one shared palette across frames keeps the colors stable and the file small
    montage = Image.new("RGB", (w, h * len(frames)))
    for i, f in enumerate(frames): montage.paste(f, (0, i * h))
    pal = montage.quantize(colors=COLORS, method=Image.MEDIANCUT)
    # Snap near-white palette entries to pure white: quantization drifts the
    # background a shade or two, which shows as a faint box on a white email.
    pdata = pal.getpalette()
    for i in range(0, len(pdata), 3):
        r, g, b = pdata[i:i+3]
        if r >= 246 and g >= 246 and b >= 246: pdata[i:i+3] = [255, 255, 255]
    pal.putpalette(pdata)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    dur = [1200] + [TIMES[i+1] - TIMES[i] for i in range(1, len(TIMES) - 1)] + [2600]
    kw = dict(save_all=True, append_images=q[1:], duration=dur, disposal=1, optimize=True)
    q[0].save(OUT / "signature-tagline-reel.gif", **kw)              # plays once, rests on the tagline
    q[0].save(OUT / "signature-tagline-reel-loop.gif", loop=0, **kw)  # loops forever
    frames[-1].save(OUT / "signature-tagline-static.png")             # no-animation fallback
    for f in ("signature-tagline-reel.gif", "signature-tagline-reel-loop.gif", "signature-tagline-static.png"):
        print(f, round((OUT / f).stat().st_size / 1024, 1), "KB", f"{w}x{h} px (display at {w//SCALE}x{h//SCALE})")

if __name__ == "__main__":
    main()

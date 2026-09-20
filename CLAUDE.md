# Rules for editing this repo
1. Never hand-edit files under `public/**/*.html`; edit `src/site_content.py` or `src/landing_content.py` and run `python3 src/build.py`. Commit `src/` and `public/` together.
2. CSS/JS live in `public/assets/`; after any change bump `V` in `src/build.py` so cached assets refresh (assets are served immutable for a year).
3. Images: new files get new names (never overwrite an image in place). Headshots are 4:5 `*-portrait.jpg` (900x1125) and 3:2 `*-wide.jpg`.
4. Content rules: do not name confidential clients (see project notes); only verified matters go on the Results page; award years must match Sean's current listings.
5. Commit as Josh Bernstein <josh@virtutelegal.com> with the Co-Authored-By trailer. Push to `main` deploys immediately.

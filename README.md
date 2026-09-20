# Suder, LLC website (ssuder.com)

Static site, deployed on Netlify from the `main` branch. Every push to `main` goes live.

- `public/` is what Netlify serves (`publish = "public"` in `netlify.toml`).
- `src/build.py` generates every HTML page in `public/` from `src/site_content.py` (firm, team, results, opinions, jurisdictions, redirects) and `src/landing_content.py` (practice-area copy). Run `python3 src/build.py` after editing either file, then commit both `src/` and `public/`.
- CSS and JS are hand-written in `public/assets/css/site.css` and `public/assets/js/site.js`. After changing either, bump `V` in `src/build.py` (cache-busting) and rebuild.
- `public/_redirects` maps every old Squarespace URL (`/suder`, `/experience`, `/publishedopinions`, ...) to the new pages. Netlify Forms handles the contact form (`name="contact"`).

# jakecard.dev

Static files for the personal site and [Dropshot website](https://jakecard.dev/dropshot/). `CNAME` configures `jakecard.dev`; `.nojekyll` disables Jekyll processing. GitHub Pages publishes `main`, `/(root)`.

## Dropshot website

Edit `dropshot/index.html`, `dropshot/style.css`, and `dropshot/assets/` directly here. Product and design notes and the existing design configuration live alongside the site in `dropshot/`. There is no website build step or source mirroring.

From the repository root, preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/dropshot/>. Assets use relative paths; Anton and its license are included under `dropshot/assets/`.

## Downloads and update feeds

DMGs remain in [jakecard/Dropshot-releases](https://github.com/jakecard/Dropshot-releases), which no longer needs GitHub Pages. This repository owns both feed URLs:

- `dropshot/appcast.xml`: canonical feed for new app builds.
- `Dropshot-releases/appcast.xml`: compatibility copy required by already-installed apps. Keep it current for every release.
- `Dropshot-releases/index.html`: redirect from the old website address to `/dropshot/`.

For each release:

1. Upload the signed DMG to its immutable GitHub Release tag in `Dropshot-releases`.
2. Update `dropshot/appcast.xml`, preserving the generated signature and using a tag-specific GitHub Release enclosure URL.
3. Run `python3 scripts/sync-dropshot-feed.py` to update the compatibility copy.
4. Commit and push both feed files together. Verify both live URLs return the same XML after Pages deployment.

The app's release tooling must publish here instead of the former distribution repository. Changing a future build's feed URL alone does not update older installed apps; the compatibility copy is still required.

## Publishing and future hosting

Push to `main` and check the GitHub Pages deployment. Verify <https://jakecard.dev/dropshot/>, both feed URLs, and the old landing-page redirect. When changing hosting providers, preserve all these paths, including the case-sensitive `/Dropshot-releases/appcast.xml` path.

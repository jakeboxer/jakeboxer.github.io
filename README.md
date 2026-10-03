# jakecard.dev

Static files for the personal site and [Dropshot website](https://jakecard.dev/dropshot/). `CNAME` configures `jakecard.dev`; `.nojekyll` disables Jekyll processing. GitHub Pages publishes `main`, `/(root)`.

## Dropshot website

Edit `dropshot/index.html`, `dropshot/style.css`, and `dropshot/assets/` directly here. Product and design notes and the existing design configuration live alongside the site in `dropshot/`. There is no website build step or source mirroring.

From the repository root, preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/dropshot/>. Assets use relative paths; Anton and its license are included under `dropshot/assets/`.

## Downloads and update feed

DMGs remain in [jakecard/Dropshot-releases](https://github.com/jakecard/Dropshot-releases), which no longer needs GitHub Pages. This repository owns the website and update feed:

- `dropshot/appcast.xml`: the update feed for Dropshot.
- `Dropshot-releases/index.html`: redirect from the old website address to `/dropshot/`.

For each release:

1. Upload the signed DMG to its immutable GitHub Release tag in `Dropshot-releases`.
2. Update `dropshot/appcast.xml`, preserving the generated signature and using a tag-specific GitHub Release enclosure URL.
3. Commit and push the feed update. Verify <https://jakecard.dev/dropshot/appcast.xml> after Pages deployment.

The app's release tooling publishes the feed here instead of the DMG distribution repository. The old feed and synchronization script were retired after the only installed copy migrated to the new URL.

## Publishing and future hosting

Push to `main` and check the GitHub Pages deployment. Verify <https://jakecard.dev/dropshot/>, the update feed, and the old landing-page redirect. Preserve these paths when changing hosting providers.

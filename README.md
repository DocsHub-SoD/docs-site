# docs-site

Source code for the community documentation website for **Shape of Dreams** modding.

Live site: https://sod-docs.shshx-one.xyz/

Built with [VitePress](https://vitepress.dev/).

---

## What is this repo for?

This repository hosts the static frontend site:
- Guides for setting up BepInEx and Harmony (`docs/getting-started.md`).
- Markdown pages for game classes generated from the raw data (`docs/api/`).
- Full type index with client-side search (`docs/catalog.md`).

The actual structured data (JSON models, SQLite database, dependency graph) is maintained in [docs-data](https://github.com/DocsHub-SoD/docs-data). 

If you want to suggest edits to class descriptions or method signatures, please open a PR in the **docs-data** repo instead of here, as the markdown pages in this repo are generated from that data.

---

## Local Development

Requirements: Node.js 18+

```bash
# Install dependencies
npm install

# Run local dev server with hot reload
npm run docs:dev

# Build for production
npm run docs:build

# Preview production build locally
npm run docs:preview
```

---

## Deployment

The site is deployed automatically to Cloudflare Pages on pushes to the `main` branch.

## License

MIT

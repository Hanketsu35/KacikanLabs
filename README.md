# KacikanLabs

Personal lab for sharing weekly lab material — PDFs, code, datasets, and notes together in one folder flow.

**Live site:** https://kacikanlabs.pages.dev *(update after deploy)*

## Structure

```
/
├── index.html          # Homepage
├── content.js          # Single source of truth for all lab items
├── assets/             # Year / course / lab-date folders live here
├── pdfs/index.html     # Legacy redirect to the unified archive
├── datasets/index.html # Legacy redirect to the unified archive
├── snippets/index.html # Legacy redirect to the unified archive
├── style.css           # Shared styles
└── .gitignore
```

## Adding Content

Add new entries in `content.js`. The archive stays compact, and each lab opens a detail view with its files:

```js
{
  year: "2026",
  course: "Machine Learning Lab",
  labDate: "2026-04-22",
  title: "Week 01 - Data Setup",
  description: "Brief description.",
  tags: ["week-01", "intro"],
  assets: [
    { label: "Lab PDF", kind: "pdf", href: "assets/2026/machine-learning-lab/2026-04-22/lab.pdf" },
    { label: "Starter Code", kind: "code", href: "assets/2026/machine-learning-lab/2026-04-22/starter.py" },
    { label: "Dataset", kind: "data", href: "assets/2026/machine-learning-lab/2026-04-22/dataset.csv" },
  ],
}
```

For a new week, create a folder like `assets/2026/machine-learning-lab/2026-04-22/` and add the matching entry once in `content.js`.

## Cloudflare Pages

Yes, JS works on Cloudflare Pages. This project is a static site, so the browser runs the JS directly and Pages just serves the files.

## Deploy

Hosted on **Cloudflare Pages** via GitHub integration. Every push to `main` triggers an automatic deploy.

### First-time setup
1. Push this repo to GitHub
2. Go to [Cloudflare Pages](https://pages.cloudflare.com) → Create project → Connect to Git
3. Select the repo, set build settings to **none** (static site)
4. Deploy

## License

MIT

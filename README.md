# KacikanLabs

KacikanLabs is the course lab archive for students.

Everything for each lab stays together in one place:
- PDF
- code
- dataset
- extra files

The archive is organized by year, course, and lab date.

## Live site

https://kacikanlabs.210401043.workers.dev/

## How to use

1. Open the homepage.
2. Find your year and course.
3. Open the lab.
4. Download the files inside that lab.

## Folder flow

Each lab has its own folder, for example:

```text
assets/2026/CENG113M/LAB1/
```

The files for that lab should stay inside the same folder.

## Adding new lab content

Add a new lab entry in [content.js](content.js).

Example:

```js
{
  year: "2026",
  course: "CENG113M",
  labDate: "LAB 1",
  title: "Lab 1",
  description: "Introductory lab files.",
  tags: ["intro"],
  assets: [
    { label: "LAB1.pdf", kind: "pdf", href: "assests/2026/CENG113M/LAB1/LAB1.pdf" },
    { label: "exercise_1_hello_world.py", kind: "code", href: "assests/2026/CENG113M/LAB2/exercise_1_hello_world.py" }
  ]
}
```

## Live site

The site runs on Cloudflare Pages.

## Deploy

This is a static site, so no build command is needed.

Cloudflare Pages settings:
- Build command: none
- Output directory: root

## License

MIT

# Jesly Prosper — Portfolio

A fast, single-page portfolio site. Plain HTML, CSS, and JavaScript — no build step, no dependencies.

## Run it locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Make it yours

Search the code for `TODO` — every placeholder is marked. The main spots:

| What | Where |
| --- | --- |
| Intro line, about paragraphs | `index.html` (hero + About) |
| Your photo | Drop a square image at `assets/photo.jpg` and update the `<img>` in the hero |
| Résumé | Put your PDF at `assets/resume.pdf` |
| Skills, projects, experience | `index.html` — edit the lists and cards |
| LinkedIn link | `index.html` — replace `YOUR-LINKEDIN` |
| Contact form | Create a free form at [formspree.io](https://formspree.io) and replace `YOUR_FORM_ID`. Until then the form opens the visitor's email client. |
| Colors | `styles.css` — change the `--accent` tokens in `:root` |

## Publish for free on GitHub Pages

1. Push this repo to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, pick your branch and `/ (root)`, then save.
4. Your site goes live at `https://<username>.github.io/<repo>/` in about a minute.

## Features

- Light and dark theme, remembered between visits
- Smooth scroll, active-section highlighting, mobile menu
- Scroll-reveal animations, animated counters, typewriter headline
- 3D tilt on the hero card and a subtle cursor glow (desktop only)
- Fully responsive, keyboard accessible, respects reduced-motion preferences

# Résumés

| File | Use it for |
| --- | --- |
| `../assets/resume.pdf` | General résumé. Also the site's "Download résumé" button. |
| `jacobs-data-analyst.pdf` | Jacobs, Data Analyst |
| `google-swe-sre-intern-2027.pdf` | Google, Software Engineering / SRE Intern 2027 |
| `aviva-revenue-finance-analyst.pdf` | Aviva Investors, Revenue Finance Analyst |
| `visa-business-operations-analyst.pdf` | Visa, Analyst (Business Operations) |

## Editing and rebuilding

Each résumé is generated from a Python script in `source/`. Edit the text in the script, then rebuild.
Building needs Python 3, Node.js, and Playwright with Chromium.

```bash
cd resumes/source

# General résumé: writes resume-full.html and resume-web.html, then both PDFs
python3 resume_general.py .
node topdf.mjs "$PWD"
cp resume-full.pdf ../../assets/resume.pdf

# A tailored résumé, for example Jacobs
python3 resume_jacobs.py .
node topdf_one.mjs "$PWD/resume-jacobs.html" "$PWD/../jacobs-data-analyst.pdf"
```

The `topdf` scripts import Playwright from `/opt/node22/lib/node_modules/playwright`. Change that path if Playwright lives elsewhere on your machine.

# Résumés

| File | Use it for |
| --- | --- |
| `../assets/resume.pdf` | General résumé. Also the site's "Download résumé" button. |
| `jacobs-data-analyst.pdf` | Jacobs, Data Analyst |
| `google-swe-sre-intern-2027.pdf` | Google, Software Engineering / SRE Intern 2027 |
| `aviva-revenue-finance-analyst.pdf` | Aviva Investors, Revenue Finance Analyst |
| `visa-business-operations-analyst.pdf` | Visa, Analyst (Business Operations) |
| `10000-black-interns-data-tech.pdf` | 10,000 Black Interns, data and technology workstreams |
| `microsoft-partner-solutions-architect.pdf` | Microsoft, Partner Solutions Architect (AI/Apps) |
| `trainline-data-analyst.pdf` | Trainline, Data Analyst (Partner Solutions) |
| `visa-software-engineer.pdf` | Visa, Software Engineer (Reading) |

## Writing a new tailored résumé

All résumé content comes from [`FACTS.md`](FACTS.md), the verified fact bank. Read its tailoring rules and its "Never claim" list first.

1. Copy the closest existing script, for example `cp source/resume_jacobs.py source/resume_<company>.py`, and change the output filename inside it.
2. Rewrite the summary, skill order and bullets for the job ad, using only facts from `FACTS.md`.
3. Build it (below) and add a row to the table above.

If you do something new, such as a project, job or certificate, add it to `FACTS.md` first.

## Editing and rebuilding

Each résumé is generated from a Python script in `source/`. Edit the text in the script, then rebuild.
Building needs Python 3 and Node.js. One-time setup:

```bash
cd resumes/source
npm install
npx playwright install chromium
```

Then, from `resumes/source` (this works in Git Bash, PowerShell, macOS and Linux):

```bash
# General résumé: writes resume-full.html and resume-web.html, then both PDFs
python resume_general.py .
node topdf.mjs .
cp resume-full.pdf ../../assets/resume.pdf

# A tailored résumé, for example Jacobs
python resume_jacobs.py .
node topdf_one.mjs resume-jacobs.html ../jacobs-data-analyst.pdf
```

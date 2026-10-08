import sys
S = sys.argv[1]
fonts = open(f"{S}/fonts/lato-embedded.css").read()
css = open(f"{S}/resume_css.txt").read().replace("{{","{").replace("}}","}").replace("{fonts}", fonts)

def link(url, text=None):
    return f'<a href="https://{url}">{text or url}</a>'

contact = ['<a href="mailto:jeslyprosper@gmail.com">jeslyprosper@gmail.com</a>',
           link("linkedin.com/in/jeslyprosper"), link("github.com/JeslyP"),
           link("jeslyp.github.io/Jesly", "Portfolio: jeslyp.github.io/Jesly"),
           "London, UK", "British citizen (unrestricted right to work in the UK)"]
contact_html = '<span class="sep">|</span>'.join(f"<span>{c}</span>" for c in contact)

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Jesly Prosper Resume</title>
<style>
{css}
@page {{ margin: 10mm 12.5mm 10mm 12.5mm; }}
body {{ font-size: 9.5pt; line-height: 1.3; }}
h2 {{ margin: 6.5pt 0 2.5pt; }}
</style></head><body>
<h1>JESLY PROSPER</h1>
<div class="contact">{contact_html}</div>

<h2>Education</h2>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Relevant coursework: Data Science, Software &amp; Systems Engineering, Human Factors: Technology in Context</p>
</div>

<h2>Skills</h2>
<div class="skills">
<p><b>Business Operations:</b> Process improvement and automation, requirements gathering, business process mapping, data quality checks, cross-functional stakeholder communication</p>
<p><b>Revenue &amp; Pricing Analysis:</b> Revenue and cost analysis, pricing analysis, revenue recognition principles, monthly financial reporting, KPI tracking, forecasting support</p>
<p><b>Data &amp; Reporting:</b> Advanced Excel (pivot tables, complex formulas), PowerPoint, SQL, Python (Pandas), Tableau, data validation and reconciliation</p>
<p><b>AI Tools:</b> Everyday use of Claude and GitHub Copilot for analysis, reporting, and productivity</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Analysed booking, revenue, and cost data to identify trends and inefficiencies, turning findings into recommendations that directly informed pricing and fleet decisions.</li>
<li>Automated monthly financial reporting and recurring processes, replacing manual work and improving accuracy, consistency, and turnaround.</li>
<li>Designed, built, and solely maintained the booking, fleet, and financial reporting system that linked customer bookings to revenue reporting, and led its migration to a new platform while the business kept running.</li>
<li>Acted as the link between non-technical stakeholders and the system, gathering requirements and turning them into working processes end to end.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built automated data pipelines and reporting dashboards for multiple client businesses, bringing together data from APIs, databases, and flat files into reliable reporting.</li>
<li>Implemented data validation and error-handling checks to keep every client deliverable accurate and consistent.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Salesforce Essential Training, LinkedIn Learning</span><span class="date">Oct 2026</span></div>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Financial Planning and Analysis (FP&amp;A) Foundations, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>CFI Corporate Finance Foundations Professional Certificate, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>NHS Data Science &amp; ETL Pipeline (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Cleansed and integrated six raw NHS operational datasets, including billing and insurance records, into a normalised relational database in SQLite.</li>
<li>Identified the drivers of appointment no-shows with a chi-square test and built a logistic regression model to predict them, flagging overfitting rather than reporting an inflated result.</li>
</ul>
</div>
</body></html>"""
open(f"{S}/resume-visa.html","w").write(html)
print("written")

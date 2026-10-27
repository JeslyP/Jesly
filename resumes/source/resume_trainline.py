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
.avail {{ text-align: center; font-size: 9pt; font-weight: 700; color: #1f3a68; margin: 1pt 0 3pt; }}
@page {{ margin: 9mm 12mm 9mm 12mm; }}
body {{ font-size: 9.35pt; line-height: 1.27; }}
h2 {{ margin: 5.5pt 0 2.5pt; }}
.row {{ margin-top: 3pt; }}
</style></head><body>
<h1>JESLY PROSPER</h1>
<div class="contact">{contact_html}</div>
<h2>Education</h2>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Relevant coursework: Data Science, Machine Learning &amp; Optimisation, Software &amp; Systems Engineering, Human-Computer Interaction</p>
</div>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected Winter 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>

<h2>Skills</h2>
<div class="skills">
<p><b>Analytics &amp; SQL:</b> SQL (PostgreSQL, MS SQL Server, SQLite), Python (Pandas, NumPy, Scikit-learn), statistical analysis (chi-square testing, logistic regression, K-means clustering), ETL pipeline design, data validation and reconciliation</p>
<p><b>Visualisation &amp; Storytelling:</b> Python, Tableau, advanced Excel, and PowerPoint for dashboards, reports, and presentations to technical and non-technical audiences</p>
<p><b>AI &amp; Automation:</b> Everyday use of Claude and GitHub Copilot to speed up analysis code, plus automation of recurring reporting and day-to-day processes</p>
<p><b>Commercial Analysis:</b> Revenue, cost, and pricing analysis, KPI tracking, forecasting support, requirements gathering, stakeholder communication</p>
<p><b>Data Platforms &amp; Engineering:</b> Supabase, Snowflake, AWS, Git, CI/CD, Next.js</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Analysed booking, revenue, and cost data to answer commercial questions and identify inefficiencies, turning findings into recommendations that directly shaped pricing and fleet decisions.</li>
<li>Defined and automated the business's monthly profit and loss reporting, with profit per vehicle, month-by-month history, and CSV export, replacing manual bookkeeping from paper log sheets.</li>
<li>Built and solely maintained the booking, fleet, and financial reporting system behind that analysis, migrating it from Python/Flask and SQL Server to Next.js and Supabase while the business kept running.</li>
<li>Protected data accuracy with server-side validation of every entry, reversible deletions, and 159 automated tests running before each release.</li>
<li>Explained findings and system changes to non-technical stakeholders, and turned their needs into working tools and reports.</li>
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

<div class="entry"><h2>Projects</h2>
<div class="row"><span>NHS Data Science &amp; ETL Pipeline, Python and SQL (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Structured six raw NHS operational datasets into a normalised relational schema in SQLite, documented with an ER diagram, to answer why patients miss appointments.</li>
<li>Tested what drives missed appointments with chi-square tests and a logistic regression model, and reported honestly that no factor predicted cancellation (ROC-AUC 0.50); used K-means clustering to find that 2% of patients account for 15% of appointments.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Autonomous Multi-Robot System, Python and ROS2 (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Designed five test scenarios for an autonomous multi-robot system, each run for 3 hours of simulation time, and analysed the results to validate robustness, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification, PyTorch (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch, achieving 79% test accuracy on a 40,000/10,000/10,000 train/validation/test split.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Financial Planning and Analysis (FP&amp;A) Foundations, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>CFI Corporate Finance Foundations Professional Certificate, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Salesforce Essential Training, LinkedIn Learning</span><span class="date">Oct 2026</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
</div>
</body></html>"""
open(f"{S}/resume-trainline.html","w").write(html)
print("written")

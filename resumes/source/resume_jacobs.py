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
@page {{ margin: 9mm 12mm 9mm 12mm; }}
body {{ font-size: 9.35pt; line-height: 1.27; }}
h2 {{ margin: 5.5pt 0 2.5pt; }}
.row {{ margin-top: 3pt; }}
</style></head><body>
<h1>JESLY PROSPER</h1>
<div class="contact">{contact_html}</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Data Analysis &amp; SQL:</b> SQL (T-SQL, MS SQL Server, PostgreSQL, SQLite), data cleansing, validation and reconciliation, relational data modelling, ETL pipeline design</p>
<p><b>Reporting &amp; Visualisation:</b> Tableau, advanced Excel (pivot tables, complex formulas), reporting dashboards, KPI tracking, management and financial reporting</p>
<p><b>Statistical Analysis:</b> Python (Pandas, NumPy, Scikit-learn), chi-square testing, logistic regression, K-Means clustering, PyTorch</p>
<p><b>Business Analysis:</b> Requirements gathering, stakeholder communication, process mapping, revenue and cost analysis, forecasting</p>
<p><b>Engineering &amp; Delivery:</b> Git, Docker, AWS, Snowflake, REST APIs, CI/CD, Agile delivery (Jira)</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Education</h2>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected Winter 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Accredited by the IET and BCS. Relevant coursework: Data Science &amp; Machine Learning, Software &amp; Systems Engineering, Object Oriented Data Structures &amp; Algorithms</p>
</div>

<h2>Work Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Analysed booking, revenue, and cost data to identify trends and inefficiencies, turning findings into recommendations that directly informed pricing and fleet decisions.</li>
<li>Automated monthly financial reporting and recurring processes, replacing manual work and improving accuracy, consistency, and turnaround.</li>
<li>Designed, built, and solely maintained the booking, fleet, and financial reporting system on a SQL Server database (Python/Flask, later migrated to Next.js/Supabase) for a live commercial business.</li>
<li>Gathered requirements directly from non-technical stakeholders and delivered working solutions end to end, owning the system from design to production support.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built automated data pipelines and reporting dashboards for multiple client businesses, integrating data from APIs, databases, and flat files into reliable reporting.</li>
<li>Implemented data validation and error-handling checks to keep every client deliverable accurate and consistent.</li>
</ul>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>NHS Data Science &amp; ETL Pipeline (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Cleansed and integrated six raw NHS operational datasets (appointments, billing, insurance, prescriptions, surgery, test records) into a normalised relational schema in SQLite, documented with an ER diagram.</li>
<li>Ran a chi-square test to identify significant drivers of appointment no-shows, built a logistic regression model to predict no-show likelihood (flagging overfitting rather than reporting an inflated result), and used K-means clustering to segment patients by behaviour.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Autonomous Robotics System (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Built an autonomous multi-robot collection system in Python and ROS2 (Gazebo, Docker), coordinated by an 8-state finite state machine with Nav2 navigation and LiDAR obstacle avoidance.</li>
<li>Designed five test scenarios, each run for 3 hours of simulation time, and analysed the results to validate robustness, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Financial Planning and Analysis (FP&amp;A) Foundations, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>CFI Corporate Finance Foundations Professional Certificate, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Cybersecurity Job Simulation, Mastercard (Forage)</span><span class="date">Feb 2025</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
</div>
</body></html>"""
open(f"{S}/resume-jacobs.html","w").write(html)
print("written")

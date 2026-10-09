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
.avail {{ text-align: center; font-size: 9pt; font-weight: 700; color: #1f3a68; margin: 1pt 0 3pt; }}
</style></head><body>
<h1>JESLY PROSPER</h1>
<div class="contact">{contact_html}</div>
<h2>Education</h2>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected Winter 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Accredited by the IET and BCS. Relevant coursework: Data Science, Machine Learning &amp; Optimisation, Object Oriented Data Structures &amp; Algorithms, Software &amp; Systems Engineering, Operating Systems, Security &amp; Networking</p>
</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Programming:</b> Python, SQL (PostgreSQL, MS SQL Server, SQLite), Java, JavaScript/TypeScript</p>
<p><b>Data &amp; Analytics:</b> Pandas, NumPy, Scikit-learn, PyTorch, statistical analysis, ETL pipeline design, Tableau, advanced Excel, data validation and reconciliation</p>
<p><b>Engineering &amp; Cloud:</b> Next.js, React, Flask, Supabase, REST APIs, Docker, AWS (Lambda, S3, EC2), Git, CI/CD, automated testing, Agile (Jira)</p>
<p><b>Certifications:</b> Salesforce Essential Training, Introduction to Business Analysis (IIBA-accredited), FP&amp;A Foundations, CFI Corporate Finance Foundations, Mastercard Cybersecurity Job Simulation, The Legend of Python</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Designed, built, and solely maintained the full-stack booking, fleet, and financial reporting system for a live business, then migrated it from Python/Flask and SQL Server to Next.js and Supabase while the business kept running.</li>
<li>Built the booking-to-billing workflow: online requests approved into rentals in one click, an invoice for each rental showing the balance due, and every payment recorded by method and date received.</li>
<li>Automated the monthly profit and loss statement, with net profit per vehicle, month-by-month history, and CSV export, replacing manual bookkeeping from paper log sheets.</li>
<li>Analysed booking, revenue, and cost data to identify trends and inefficiencies, turning findings into recommendations that directly informed pricing and fleet decisions.</li>
<li>Protected the financial records with reversible deletions, server-side validation of every entry, and 159 automated tests running in CI before each release.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built automated data pipelines, reporting dashboards, and web applications for multiple client businesses, integrating APIs, databases, and flat files into reliable systems.</li>
<li>Implemented data validation and error-handling checks to keep every client deliverable accurate and consistent.</li>
</ul>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>NHS Data Science &amp; ETL Pipeline, Python and SQL (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Cleansed and normalised six raw NHS operational datasets into a relational SQLite schema, then used a chi-square test, logistic regression, and K-means clustering to explain, predict, and segment appointment no-shows, flagging overfitting rather than reporting an inflated result.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Autonomous Multi-Robot System, Python and ROS2 (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Built an autonomous barrel-collection system for TurtleBot3 robots in Gazebo, coordinated by an 8-state finite state machine with Nav2 navigation and LiDAR obstacle avoidance, in a Dockerised environment.</li>
<li>Designed five test scenarios, each run for 3 hours of simulation time, and analysed the results to validate robustness, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification, PyTorch (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch with batch normalisation and dropout, trained with Adam and a scheduled learning rate, reaching 81% test accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX simulation game using the Factory pattern and class hierarchies, coordinating a 4-person Agile team with Jira and CI/CD.</li>
</ul>
</div>
</body></html>"""
open(f"{S}/resume-10kbi.html","w").write(html)
print("written")

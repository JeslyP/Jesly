import sys
S = sys.argv[1]
fonts = open(f"{S}/fonts/lato-embedded.css").read()

def link(url, text=None):
    return f'<a href="https://{url}">{text or url}</a>'

def build(with_email):
    contact = []
    if with_email:
        contact.append('<a href="mailto:jeslyprosper@gmail.com">jeslyprosper@gmail.com</a>')
    contact += [link("linkedin.com/in/jeslyprosper"), link("github.com/JeslyP"),
                link("jeslyp.github.io/Jesly", "Portfolio: jeslyp.github.io/Jesly"),
                "London, UK", "British citizen (unrestricted right to work in the UK)"]
    contact_html = '<span class="sep">|</span>'.join(f"<span>{c}</span>" for c in contact)
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Jesly Prosper Resume</title>
<style>
{fonts}
@page {{ size: A4; margin: 11mm 13mm 11mm 13mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Lato', 'Liberation Sans', Arial, sans-serif; font-size: 9.6pt; line-height: 1.3; color: #111; margin: 0; }}
a {{ color: inherit; text-decoration: none; }}
h1 {{ text-align: center; color: #1f3a68; font-size: 19pt; margin: 0 0 3pt; letter-spacing: 0.3pt; }}
.contact {{ display: flex; flex-wrap: wrap; justify-content: center; row-gap: 1pt; font-size: 9pt; margin-bottom: 4pt; }}
.contact > span {{ white-space: nowrap; }}
.contact .sep {{ margin: 0 5pt; color: #444; }}
h2 {{ break-after: avoid-page; color: #1f3a68; font-size: 10.5pt; text-transform: uppercase; margin: 7pt 0 3pt; padding-bottom: 1.5pt; border-bottom: 1px solid #1f3a68; }}
p {{ margin: 0; }}
.row {{ display: flex; justify-content: space-between; gap: 12pt; font-weight: 700; margin-top: 3.5pt; break-after: avoid; }}
.row .date {{ white-space: nowrap; }}
.sub {{ font-style: italic; break-after: avoid; }}
.sub a {{ font-style: normal; color: #1f3a68; }}
.row a {{ color: #1f3a68; font-weight: 400; }}
ul {{ margin: 1pt 0 0; padding-left: 13pt; }}
li {{ margin: 0.5pt 0; break-inside: avoid; }}
.skills p {{ margin: 0.8pt 0; }}
.certs .row {{ margin-top: 2pt; break-after: auto; }}
.entry {{ break-inside: avoid-page; }}
</style></head><body>
<h1>JESLY PROSPER</h1>
<div class="contact">{contact_html}</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Programming &amp; Data:</b> Python (Flask, Pandas, NumPy, Scikit-learn, PyTorch), Java, JavaScript/TypeScript (React, Next.js), SQL (T-SQL, PostgreSQL, MS SQL Server), Supabase</p>
<p><b>Machine Learning &amp; Analytics:</b> Predictive modelling (Logistic Regression), clustering (K-Means), deep learning (CNNs, PyTorch), statistical analysis, ETL pipeline design</p>
<p><b>Business &amp; Financial Analysis:</b> Financial reporting, revenue and cost analysis, KPI tracking, forecasting support, requirements gathering, business process mapping</p>
<p><b>Cloud &amp; Engineering Practice:</b> AWS (Lambda, S3, EC2), Docker, Snowflake, Git, CI/CD pipelines, REST API design, automated testing, Agile delivery (Jira)</p>
<p><b>Reporting &amp; AI Tools:</b> Tableau, advanced Excel (pivot tables, complex formulas), everyday use of AI tools (Claude, GitHub Copilot) for development and analysis</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Education</h2>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected Winter 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Accredited by the IET and BCS. Relevant coursework: Data Science &amp; Machine Learning, Autonomous Robotics, Software &amp; Systems Engineering, Object Oriented Data Structures &amp; Algorithms</p>
</div>

<h2>Work Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Designed, built, and solely maintained a full-stack booking, fleet, and financial reporting system (Python/Flask + SQL Server, later migrated to Next.js/Supabase) for a live commercial business.</li>
<li>Analysed booking, revenue, and cost data to identify trends and inefficiencies, translating findings into recommendations that directly informed pricing and fleet decisions.</li>
<li>Automated monthly financial reporting and recurring processes, replacing manual work and improving accuracy, consistency, and turnaround.</li>
<li>Gathered requirements directly from non-technical stakeholders and delivered working solutions end to end, owning the system's full lifecycle from design to production support.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built automated data pipelines, reporting dashboards, and web applications for multiple client businesses, integrating APIs, databases, and flat files into reliable systems.</li>
<li>Implemented data validation and error-handling frameworks ensuring the accuracy and integrity of every client deliverable.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Financial Planning and Analysis (FP&amp;A) Foundations, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>CFI Corporate Finance Foundations Professional Certificate, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Cybersecurity Job Simulation, Mastercard (Forage)</span><span class="date">Feb 2025</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>Autonomous Robotics System (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Designed and implemented an autonomous multi-robot barrel-collection system for TurtleBot3 Waffle Pi robots in a Gazebo simulation, using Python and ROS2 within a Dockerised development environment.</li>
<li>Built an 8-state finite state machine (searching, approaching, positioning, picking up, delivering, offloading, clearing space, decontaminating) to coordinate patrol navigation, target selection, pickup, delivery, and decontamination behaviours.</li>
<li>Used the Nav2 stack for waypoint-based patrol navigation and LiDAR-based obstacle sectoring for real-time obstacle avoidance, combined with a proportional controller for visual servoing to align and approach detected targets.</li>
<li>Implemented hysteresis-based target selection to prevent oscillation between similarly-sized detections, plus a timeout and escape manoeuvre to recover automatically when the robot became stuck.</li>
<li>Designed and ran five distinct test scenarios (baseline, sensor noise robustness, varied item distribution via random seed, open environment, and a full-complexity stress test combining noise and obstacles), each run for 3 hours of simulation time, achieving 90 to 100% detection accuracy across scenarios.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>NHS Data Science &amp; ETL Pipeline (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Designed a relational database schema from six raw NHS operational datasets (appointments, billing, insurance, prescriptions, surgery, test records), building an ER diagram and normalising the data into SQLite.</li>
<li>Ran a chi-square test to identify significant drivers of appointment no-shows, built a logistic regression model to predict no-show likelihood (correctly identifying and flagging overfitting rather than reporting an inflated result), and applied K-means clustering to segment patients by behaviour.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch in PyTorch (three convolutional blocks with batch normalisation and dropout, trained with Adam and a scheduled learning rate over 20 epochs), achieving 81% test accuracy on a 40,000/10,000/10,000 train/validation/test split.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX-based city simulation game in Java, using the Factory pattern to instantiate building types and inheritance/polymorphism across building and event class hierarchies, coordinating a 4-person Agile team with Jira and delivering on time with CI/CD integration.</li>
</ul>
</div>
</body></html>"""

open(f"{S}/resume-full.html","w").write(build(True))
open(f"{S}/resume-web.html","w").write(build(False))
print("html written")

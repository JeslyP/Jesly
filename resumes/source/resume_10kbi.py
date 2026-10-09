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
<li>Gathered requirements directly from non-technical stakeholders and delivered working solutions end to end, owning the system from design through to production support.</li>
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
<li>Designed a relational database schema from six raw NHS operational datasets (appointments, billing, insurance, prescriptions, surgery, test records), building an ER diagram and normalising the data into SQLite.</li>
<li>Ran a chi-square test to identify significant drivers of appointment no-shows, built a logistic regression model to predict no-show likelihood (flagging overfitting rather than reporting an inflated result), and applied K-means clustering to segment patients by behaviour.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Autonomous Multi-Robot System, Python and ROS2 (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Designed and implemented an autonomous multi-robot barrel-collection system for TurtleBot3 Waffle Pi robots in a Gazebo simulation, using Python and ROS2 within a Dockerised development environment.</li>
<li>Built an 8-state finite state machine (searching, approaching, positioning, picking up, delivering, offloading, clearing space, decontaminating) to coordinate navigation, target selection, pickup, delivery, and decontamination.</li>
<li>Used the Nav2 stack for waypoint-based patrol navigation and LiDAR-based obstacle sectoring for real-time avoidance, with a proportional controller for visual servoing to approach detected targets.</li>
<li>Implemented hysteresis-based target selection to prevent oscillation between similar detections, plus a timeout and escape manoeuvre so robots recover automatically when stuck.</li>
<li>Designed and ran five test scenarios, including sensor noise and a full-complexity stress test, each for 3 hours of simulation time, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification, PyTorch (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch in PyTorch (three convolutional blocks with batch normalisation and dropout, trained with Adam and a scheduled learning rate over 20 epochs), achieving 81% test accuracy on a 40,000/10,000/10,000 train/validation/test split.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX-based city simulation game in Java, using the Factory pattern to create building types and inheritance and polymorphism across building and event class hierarchies.</li>
<li>Coordinated a 4-person Agile team with Jira and delivered on time with CI/CD integration.</li>
</ul>
</div>
<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Salesforce Essential Training, LinkedIn Learning</span><span class="date">Oct 2026</span></div>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Financial Planning and Analysis (FP&amp;A) Foundations, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>CFI Corporate Finance Foundations Professional Certificate, LinkedIn Learning</span><span class="date">Aug 2026</span></div>
<div class="row"><span>Cybersecurity Job Simulation, Mastercard (Forage)</span><span class="date">Feb 2025</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
</div>
</body></html>"""
open(f"{S}/resume-10kbi.html","w").write(html)
print("written")

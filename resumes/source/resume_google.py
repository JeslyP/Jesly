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
<p class="avail">Expected graduation: December 2027 | Available full-time in London for a 13 to 17 week internship from May 2027</p>

<h2>Education</h2>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected December 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>
<div class="entry">
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Award mark 63. Accredited by the IET and BCS. Relevant coursework: Object Oriented Data Structures &amp; Algorithms, Operating Systems, Security &amp; Networking, Software &amp; Systems Engineering, Machine Learning &amp; Optimisation, Autonomous Robots</p>
</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Programming Languages:</b> Python, Java, JavaScript/TypeScript, SQL (T-SQL, PostgreSQL, MS SQL Server)</p>
<p><b>Frameworks &amp; Libraries:</b> Flask, React, Next.js, ROS2, libGDX, PyTorch, Scikit-learn, Pandas, NumPy</p>
<p><b>Infrastructure &amp; Tooling:</b> Docker, AWS (Lambda, S3, EC2), Git, CI/CD pipelines, Supabase, Snowflake, REST API design, automated testing, Agile (Jira)</p>
<p><b>Computer Science:</b> Data structures and algorithms, object-oriented design patterns, finite state machines, machine learning (CNNs, classification, clustering)</p>
<p><b>Certifications:</b> Cybersecurity Job Simulation (Mastercard, Forage), The Legend of Python (Codédex), Introduction to Business Analysis (LinkedIn Learning, IIBA-accredited)</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Designed, built, and solely maintained a full-stack booking, fleet, and financial reporting system for a live commercial business, owning its full lifecycle from design to production support.</li>
<li>Migrated the platform from Python/Flask and SQL Server to Next.js and Supabase while keeping the business running.</li>
<li>Automated monthly financial reporting and recurring processes, replacing manual work and improving accuracy, consistency, and turnaround.</li>
<li>Gathered requirements directly from non-technical stakeholders and delivered working solutions end to end.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built automated data pipelines, dashboards, and web applications for multiple client businesses, integrating APIs, databases, and flat files into reliable systems.</li>
<li>Implemented data validation and error-handling frameworks to keep every client deliverable accurate and consistent.</li>
</ul>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>Autonomous Multi-Robot System, Python and ROS2 (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Built an autonomous barrel-collection system for TurtleBot3 robots in Gazebo, coordinated by an 8-state finite state machine, in a Dockerised development environment.</li>
<li>Used the Nav2 stack for patrol navigation, LiDAR obstacle sectoring for real-time avoidance, and a proportional controller for visual servoing to approach targets.</li>
<li>Added hysteresis-based target selection to stop oscillation between detections, plus a timeout and escape manoeuvre so robots recover automatically when stuck.</li>
<li>Designed five test scenarios including sensor noise and a full-complexity stress test, each run for 3 hours of simulation time, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX city simulation game in Java, using the Factory pattern for building types and inheritance and polymorphism across building and event class hierarchies.</li>
<li>Coordinated a 4-person Agile team with Jira and delivered on time with CI/CD integration.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification, PyTorch (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch with three convolutional blocks, batch normalisation, and dropout, trained with Adam and a scheduled learning rate, reaching 81% test accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>NHS Data Science &amp; ETL Pipeline, Python and SQL (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Normalised six raw NHS datasets into a relational SQLite schema, then built a logistic regression model to predict appointment no-shows and K-means clustering to segment patients.</li>
</ul>
</div>

</body></html>"""
open(f"{S}/resume-google.html","w").write(html)
print("written")

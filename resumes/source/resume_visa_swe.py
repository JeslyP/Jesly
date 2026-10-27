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
<p class="sub">University of York, United Kingdom | Award mark 63. Accredited by the IET and BCS. Relevant coursework: Software &amp; Systems Engineering, Object Oriented Data Structures &amp; Algorithms, Operating Systems, Security &amp; Networking, Machine Learning &amp; Optimisation</p>
</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Languages:</b> TypeScript, JavaScript, Python, Java, SQL</p>
<p><b>Back End &amp; Web Services:</b> REST API design, Next.js API routes, Flask, PostgreSQL, MS SQL Server, Supabase, authentication and input validation</p>
<p><b>Testing &amp; Quality:</b> Vitest, automated unit testing, test planning, code review, static type checking, debugging and troubleshooting, coding standards</p>
<p><b>Cloud &amp; Delivery:</b> GitHub Actions CI/CD, Vercel, AWS (Lambda, S3, EC2), Docker, Git, pull-request workflow, Agile (Jira)</p>
<p><b>AI-Assisted Development:</b> Everyday use of Claude Code and GitHub Copilot for writing, debugging, and reviewing code</p>
<p><b>Languages Spoken:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Designed, built, and solely maintained a full-stack booking, fleet, and financial reporting platform for a live business, including a REST back end of 20 API endpoints covering bookings, rentals, invoicing, payments, and reporting.</li>
<li>Migrated the platform from Python/Flask and SQL Server to Next.js on Vercel with Supabase PostgreSQL, while the business kept running.</li>
<li>Planned and wrote 159 automated tests across finance, rentals, authentication, validation, and uploads, run in a GitHub Actions pipeline with type checks and a production build before every release.</li>
<li>Secured the service: every admin API route requires an authenticated session, every request body is validated on the server, and the privileged database key is never exposed to the browser.</li>
<li>Provided all production support: troubleshot issues reported by the business, debugged them, and deployed fixes, while protecting financial records with reversible deletions and full backups.</li>
<li>Gathered requirements from non-technical stakeholders, checked assumptions with them, and turned feedback into design changes and fixes.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Built web applications, back-end data pipelines, and reporting dashboards for multiple client businesses, integrating APIs, databases, and flat files into reliable systems.</li>
<li>Implemented validation and error-handling frameworks so every client deliverable stayed accurate and consistent.</li>
</ul>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>Autonomous Multi-Robot System, Python, ROS2 and Docker (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Designed an autonomous multi-robot system around an 8-state finite state machine, with Nav2 navigation, LiDAR obstacle avoidance, and automatic recovery when a robot became stuck.</li>
<li>Wrote and ran a test plan of five scenarios, including sensor noise and a full-complexity stress test, each for 3 hours of simulation time, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX simulation game in Java using the Factory pattern and inheritance and polymorphism across class hierarchies, working in a 4-person Agile team with Jira and CI/CD and delivering on time.</li>
<li>Reviewed teammates' code through pull requests, checking it against the team's coding standards and design before merging.</li>
<li>Diagnosed why the project's JUnit tests had never run (wrong source set), fixed an OpenGL initialisation bug they exposed, and added a GitHub Actions pipeline that builds and runs all tests on every push.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>NHS Data Science &amp; ETL Pipeline, Python and SQL (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Normalised six raw NHS datasets (557k appointments) into a SQLite schema, then used logistic regression and K-means clustering, finding that 2% of patients make 15% of appointments while demographics did not predict cancellations.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Cybersecurity Job Simulation, Mastercard (Forage)</span><span class="date">Feb 2025</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
</div>
</body></html>"""
open(f"{S}/resume-visa-swe.html","w").write(html)
print("written")

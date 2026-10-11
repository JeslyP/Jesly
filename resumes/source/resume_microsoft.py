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
<div class="row"><span>BEng in Computer Science, 2:1 Honours</span><span class="date">June 2026</span></div>
<p class="sub">University of York, United Kingdom | Accredited by the IET and BCS. Relevant coursework: Software &amp; Systems Engineering, Operating Systems, Security &amp; Networking, Machine Learning &amp; Optimisation, Object Oriented Data Structures &amp; Algorithms</p>
</div>
<div class="entry">
<div class="row"><span>MS in Analytics (OMSA)</span><span class="date">Expected Winter 2027</span></div>
<p class="sub">Georgia Institute of Technology | Computational Data Analytics track</p>
</div>

<h2>Technical Skills</h2>
<div class="skills">
<p><b>Cloud &amp; DevOps:</b> AWS (Lambda, S3, EC2), Vercel, Supabase (PostgreSQL, Storage), Snowflake, Docker, GitHub Actions CI/CD, Git</p>
<p><b>Application Development:</b> TypeScript, Next.js, React, Python, Flask, Java, REST API design, SQL, automated testing</p>
<p><b>AI &amp; Data:</b> PyTorch, Scikit-learn, Pandas, CNNs, classification and clustering, everyday use of AI tools (Claude, GitHub Copilot) in development</p>
<p><b>Architecture &amp; Delivery:</b> Solution design, platform migration, secure API design, requirements gathering, stakeholder communication, Agile (Jira)</p>
<p><b>Languages:</b> Fluent in English and Haitian Creole</p>
</div>

<h2>Experience</h2>
<div class="entry">
<div class="row"><span>Software Developer, D&amp;K Car Rentals LTD</span><span class="date">June 2023 to September 2025</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands | {link("github.com/JeslyP/dk-car-rentals")}</p>
<ul>
<li>Designed and solely delivered a full-stack cloud platform for a live car rental business: a public booking site with real-time availability, and an admin system for rentals, invoicing, payments, costs, and financial reporting.</li>
<li>Led the migration from Python/Flask and SQL Server to Next.js on Vercel with Supabase PostgreSQL and Storage, while the business kept running.</li>
<li>Built security into the architecture: every admin API route sits behind session authentication, the privileged database key is used only on the server, and file uploads go through a controlled endpoint with generated filenames.</li>
<li>Set up a GitHub Actions pipeline that runs type checks, 159 automated tests, and a production build on every change before release.</li>
<li>Worked directly with non-technical stakeholders to turn business needs into technical requirements, replacing paper log sheets and manual bookkeeping with automated workflows and a monthly profit and loss statement.</li>
<li>Analysed booking, revenue, and cost data to identify trends and inefficiencies, turning findings into recommendations that informed pricing and fleet decisions.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Freelance Software Developer, Self-Employed</span><span class="date">March 2020 to Present</span></div>
<p class="sub">Grand Turk, Turks and Caicos Islands / remote</p>
<ul>
<li>Designed and built web applications, automated data pipelines, and reporting dashboards for multiple client businesses, integrating APIs, databases, and flat files into reliable systems.</li>
<li>Gathered requirements from each client and implemented validation and error-handling to keep every deliverable accurate and consistent.</li>
</ul>
</div>

<div class="entry"><h2>Projects</h2>
<div class="row"><span>Autonomous Multi-Robot System, Python, ROS2 and Docker (University of York)</span><span class="date">January 2026</span></div>
<p class="sub">{link("github.com/JeslyP/AUROJES2025/tree/My_fix-for-assignement", "github.com/JeslyP/AUROJES2025")}</p>
<ul>
<li>Architected an autonomous multi-robot barrel-collection system for TurtleBot3 robots in Gazebo, inside a Dockerised development environment, coordinated by an 8-state finite state machine.</li>
<li>Combined Nav2 navigation, LiDAR obstacle avoidance, and visual servoing, with automatic recovery when a robot became stuck.</li>
<li>Validated the system across five test scenarios, including sensor noise and a full-complexity stress test, each run for 3 hours of simulation time, achieving 90 to 100% detection accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>CIFAR-10 Image Classification, PyTorch (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/IMLOCW")}</p>
<ul>
<li>Built a CNN from scratch with batch normalisation and dropout, trained with Adam and a scheduled learning rate, achieving 81% test accuracy.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>NHS Data Science &amp; ETL Pipeline, Python and SQL (University of York)</span><span class="date">May 2025</span></div>
<p class="sub">{link("github.com/JeslyP/NHS-Data-Science-Project-")}</p>
<ul>
<li>Normalised six raw NHS datasets into a relational schema, then used logistic regression and K-means clustering to predict and segment appointment no-shows.</li>
</ul>
</div>
<div class="entry">
<div class="row"><span>Campus Tycoon, Java Simulation Game (University of York)</span><span class="date">December 2024</span></div>
<p class="sub">{link("github.com/JeslyP/CampusTycoonBackend2")}</p>
<ul>
<li>Built a libGDX simulation game using the Factory pattern and class hierarchies, coordinating a 4-person Agile team with Jira and CI/CD.</li>
</ul>
</div>

<div class="certs entry"><h2>Certifications</h2>
<div class="row"><span>Mastercard Cybersecurity Job Simulation (Forage)</span><span class="date">Feb 2025</span></div>
<div class="row"><span>Salesforce Essential Training, LinkedIn Learning</span><span class="date">Oct 2026</span></div>
<div class="row"><span>Introduction to Business Analysis, LinkedIn Learning (IIBA-accredited)</span><span class="date">Aug 2026</span></div>
<div class="row"><span>The Legend of Python, Codédex</span><span class="date">Feb 2025</span></div>
</div>
</body></html>"""
open(f"{S}/resume-microsoft.html","w").write(html)
print("written")

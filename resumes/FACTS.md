# Résumé fact bank

Every tailored résumé is written **only** from the facts below. If a claim is not here, it does not go on a résumé until it has been checked and added.
Last verified: 27 October 2026.

## Rules for tailoring

1. **Start from the job ad.** Pick the 3–5 skills it asks for most, then choose the projects and bullets below that prove those skills. Lead with the closest match.
2. **Reword, don't invent.** You can change emphasis and vocabulary to match the role (for example, "analysed" for analyst roles, "built" for engineering roles). Never change a number, tool, dataset or outcome.
3. **Name only tools you actually used on that piece of work.** Skills you know but didn't use on a project belong in the Skills section, not in that project's bullet.
4. **Every role gets its own file.** Copy the closest `source/resume_*.py`, edit it, and add the role to `README.md`. Don't send the general résumé for a specific role.
5. **Check the "Never claim" list** before sending.

## Never claim

| Wrong | Correct |
| --- | --- |
| NHS project used Snowflake / a cloud data warehouse | SQLite |
| NHS project processed "12+" datasets | Six raw CSV datasets |
| Found "significant drivers" of NHS no-shows | No factor was significant (all p > 0.2) |
| Built a model that predicts no-shows | ROC-AUC 0.50, which is chance. The finding is that the attributes can't predict cancellation |
| "Flagged overfitting" on the NHS model | Not what happened; that note came from a broken earlier version |
| The data had a "no-show" status | It only has Completed / Cancelled / Scheduled; cancellation was the proxy |
| CIFAR-10 model reached 81% | 79% (79.3%). 81% is not reproducible from the saved model |
| "Production-grade" / "end-to-end ML pipeline" for coursework | University coursework project |

## Contact and status

- London, UK. British citizen with an unrestricted right to work in the UK.
- jeslyprosper@gmail.com · linkedin.com/in/jeslyprosper · github.com/JeslyP · Portfolio: jeslyp.github.io/Jesly
- Languages: English and Haitian Creole (fluent)

## Education

- **MS in Analytics (OMSA), Georgia Institute of Technology**: Computational Data Analytics track, expected Winter 2027.
- **BEng Computer Science, 2:1 Honours, University of York**: June 2026, award mark 63, accredited by the IET and BCS. Coursework includes Data Science & Machine Learning, Autonomous Robotics, Software & Systems Engineering, and OO Data Structures & Algorithms.

## Work experience

### Software Developer, D&K Car Rentals LTD: June 2023 to September 2025
Grand Turk, Turks and Caicos Islands · github.com/JeslyP/dk-car-rentals
- Designed, built and solely maintained a full-stack booking, fleet and financial-reporting system (Python/Flask + SQL Server, later migrated to Next.js/Supabase) for a live commercial business.
- Analysed booking, revenue and cost data to find trends and inefficiencies; the recommendations informed pricing and fleet decisions.
- Automated monthly financial reporting and recurring processes, replacing manual work.
- Gathered requirements from non-technical stakeholders and owned the full lifecycle from design to production support.

### Freelance Software Developer, Self-Employed: March 2020 to present
Grand Turk / remote
- Built automated data pipelines, reporting dashboards and web apps for several client businesses, integrating APIs, databases and flat files.
- Implemented data validation and error handling for client deliverables.

## Projects

### NHS Data Science Project, University of York (May 2025)
github.com/JeslyP/NHS-Data-Science-Project-. Tools: Python, Pandas, SQL, SQLite, SciPy, Scikit-learn, Matplotlib
- Designed an ER diagram (Chen notation) and a normalised 3NF SQLite database from **six** raw NHS CSV datasets: 556,692 appointments, 400,000 patients, 252 hospitals, 3,143 departments, 27,752 professionals.
- Chi-square tests with Cramér's V on 500,830 completed or cancelled appointments: 10.0% cancellation rate; age, gender, weekday, hour, department and hospital were **not** associated with it (all p > 0.2, V < 0.03).
- Class-weighted logistic regression: **ROC-AUC 0.50**. Reported honestly that the attributes carry no signal, and named the data needed instead (lead time, past attendance).
- K-means, k = 3 chosen by silhouette score (0.66): **2% of patients (6,337) make about 15% of all appointments**.
- Found and fixed the original notebook's bug: it filtered on a `No-Show` status that doesn't exist.
- Wrote SQL reports with outer joins (hospitals per city, departments, preferred patients) and an ethics analysis.

### Autonomous Robotics System, University of York (January 2026)
github.com/JeslyP/AUROJES2025. Tools: Python, ROS2, Nav2, Gazebo, Docker
- Autonomous multi-robot barrel-collection system for TurtleBot3 Waffle Pi robots in a Gazebo simulation.
- 8-state finite state machine (searching, approaching, positioning, picking up, delivering, offloading, clearing space, decontaminating).
- Nav2 waypoint patrol, LiDAR obstacle sectoring, and a proportional controller for visual servoing.
- Hysteresis-based target selection, plus a timeout and escape manoeuvre for when the robot got stuck.
- Five test scenarios (baseline, sensor noise, random item distribution, open environment, full stress test), each run for 3 hours of simulation time: **90 to 100% detection accuracy**.

### CIFAR-10 Image Classification, University of York (May 2025)
github.com/JeslyP/IMLOCW. Tools: Python, PyTorch
- CNN built from scratch: 3 convolutional blocks with batch norm and dropout, Adam, scheduled learning rate, 20 epochs.
- **79% test accuracy** (79.3%, re-measured from the saved `model.pth` on the 10,000-image test set) on a 40k / 10k / 10k train / validation / test split. Per class: ship 90.5% best, cat 49.9% worst.

### Campus Tycoon, Java Simulation Game, University of York (December 2024)
github.com/JeslyP/CampusTycoonBackend2. Tools: Java, libGDX, JUnit, GitHub Actions, Jira
- City-simulation game using the Factory pattern and inheritance/polymorphism across building and event hierarchies.
- Coordinated a 4-person Agile team with Jira; delivered on time.
- Diagnosed why the JUnit tests had never run (wrong source set), fixed the OpenGL initialisation bug they exposed, and added a GitHub Actions pipeline that runs every test on each push.

## Certifications

- Salesforce Essential Training, LinkedIn Learning (Oct 2026)
- Introduction to Business Analysis, LinkedIn Learning, IIBA-accredited (Aug 2026)
- FP&A Foundations, LinkedIn Learning (Aug 2026)
- CFI Corporate Finance Foundations Professional Certificate (Aug 2026)
- Cybersecurity Job Simulation, Mastercard via Forage (Feb 2025)
- The Legend of Python, Codédex (Feb 2025)

## Skills (list only what's true; match the order to the job ad)

Python (Flask, Pandas, NumPy, Scikit-learn, PyTorch), Java, JavaScript/TypeScript (React, Next.js), SQL (T-SQL, PostgreSQL, SQL Server, SQLite), Supabase · Logistic regression, K-means, CNNs, statistical testing · AWS (Lambda, S3, EC2), Docker, Snowflake (skill only, not used on the NHS project), Git, CI/CD, REST APIs, automated testing, Agile/Jira · Tableau, advanced Excel · Financial reporting, KPI tracking, requirements gathering, process mapping

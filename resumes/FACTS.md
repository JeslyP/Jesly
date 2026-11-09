# Résumé fact bank

Every tailored résumé is written **only** from the facts below. If a claim is not here, it does not go on a résumé until it has been checked and added.
Last verified: 27 October 2026 (D&K dates confirmed as June 2023 to present; fraud project results added from the executed notebook).

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
| Fraud model "prevents" or "stopped" real fraud | Estimated saving on a public dataset with an assumed €5 review cost |
| "Production-grade" / "end-to-end ML pipeline" for coursework | University coursework project |
| Fraud agent "catches 70% of fraud" or "escalates 50% of genuine" | Those rates come from the stratified evaluation sample (equal groups, one group was the model's false alarms by design), not real-world performance |
| Fraud agent used in production / by a real fraud team | Personal project; evaluated on 46 labelled cases from a public dataset; demo cases only on AWS |
| Agent "improves fraud detection" | It follows the model and policy; it explains and triages, it cannot catch fraud the model scores low |

## Contact and status

- London, UK. British citizen with an unrestricted right to work in the UK.
- Phone (applications only, not on the public site résumé): +44 7713 676038 · +1 649 245 7928
- jeslyprosper@gmail.com · linkedin.com/in/jeslyprosper · github.com/JeslyP · Portfolio: jeslyp.github.io/Jesly
- Languages: English and Haitian Creole (fluent)

## Education

- **MS in Analytics (OMSA), Georgia Institute of Technology**: Computational Data Analytics track, expected Winter 2027.
- **BEng Computer Science, 2:1 Honours, University of York**: June 2026, award mark 63, accredited by the IET and BCS. Coursework includes Data Science & Machine Learning, Autonomous Robotics, Software & Systems Engineering, and OO Data Structures & Algorithms.

## Work experience

### Software Developer, D&K Car Rentals LTD: June 2023 to present
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

### Credit Card Fraud Detection, personal project (October 2026)
github.com/JeslyP/credit-card-fraud-detection · case study: jeslyp.github.io/Jesly/projects/fraud/. Tools: Python, Pandas, NumPy, Scikit-learn, Matplotlib, Jupyter (run on Kaggle)
- Kaggle dataset (mlg-ulb): 284,807 card transactions, 492 fraud (0.17%); removed 1,081 duplicates; engineered hour of day and log amount.
- **Time-based split**: earliest 60% train, next 20% validation, latest 20% test (56,746 transactions, 74 frauds).
- Compared a baseline, class-weighted logistic regression and class-weighted gradient boosting; logistic regression had the best validation PR-AUC (0.760 vs 0.743).
- Alert threshold chosen by cost (missed fraud amount + €5 per review): 0.91.
- **Test results:** caught **63 of 74 frauds (85% recall)**, **278 false alarms of 56,672 genuine (0.5%)**, precision 18.5%, **PR-AUC 0.746**, ROC-AUC 0.983; estimated losses **€7,728 to €3,757 (51% saving)**.
- Monitoring: recall across four test sub-periods 95%, 83%, 91%, 64%, a drift signal that would trigger retraining.

### Fraud: behavioural features on PaySim and a production scoring service (October 2026)
Same repo (credit-card-fraud-detection). Tools: Python, Pandas, Scikit-learn (HistGradientBoosting), FastAPI, Pydantic, pytest, GitHub Actions, Docker
- PaySim (ealaxi/paysim1), 6.36M simulated mobile-money transactions; modelled TRANSFER and CASH_OUT only (2,770,409 rows).
- Behavioural features from **past transactions only**: payee prior count, payee count in last 24h, hours since payee's last payment, new-payee flag, payee prior mean amount, amount vs payee mean, payer prior count, hour of day.
- Excluded the four balance columns because the dataset documentation says fraud is cancelled, so they leak the label; showed a leaky comparison model separately.
- Time split: train hours 1 to 281, validation 281 to 354, test 354 to 743 (554,082 rows, 4,260 frauds).
- **Results on test:** amount and type only PR-AUC **0.138**, 17.7% of fraud caught at a 1% alert budget; **with behavioural features PR-AUC 0.409, 51.2% caught**; leaky comparison 0.9995.
- Top behavioural features (permutation importance): hour of day, amount vs payee mean, payee prior count, new payee.
- Production service for the card model: training script saving model, threshold and training-data profile; FastAPI `/score` and `/health` with validation and prediction logging; drift monitor using PSI per feature and on scores plus recall checks; **13 pytest tests in GitHub Actions**; Dockerfile. Hour of day excluded from drift checks after it raised a false alarm.
- **Deployed to AWS (29 Oct 2026)**, region eu-west-2, via a one-click GitHub Actions workflow: Kaggle download, retrain, 17 tests, arm64 image to ECR, Terraform apply (state in encrypted versioned S3), smoke test. Live API: https://iilsazxkuj.execute-api.eu-west-2.amazonaws.com/health
- AWS stack (Terraform): Lambda (API) behind API Gateway HTTP API with throttling; Lambda consumer on SQS (batch 10, ReportBatchItemFailures, DLQ after 3 tries); SNS fraud-alerts topic; CloudWatch logs (14 days) and alarms on errors, p95 latency > 2s and DLQ depth; least-privilege IAM; ECR keeps 5 images.
- Deployed model reproduced the notebook: recall 85.1%, PR-AUC 0.746. Live test: a known fraud scored 0.99998 (alert); invalid input rejected with 422.
- Tests were 17 at deployment (API, Lambda, SQS consumer, drift, training); 34 after the agent was added.
- Never claim: deployed to real customers or real traffic; PaySim is simulated data.

### LLM Fraud Analyst Agent, Claude with tool use, personal project (November 2026)
Code: github.com/JeslyP/credit-card-fraud-detection/tree/main/fraudagent · Tools: Python, Claude API (claude-haiku-5-5), tool use, structured output, pytest, GitHub Actions, Workload Identity Federation
- Claude investigates a flagged transaction with 5 tools: get_transaction, score_transaction, explain_score (exact logistic-regression contributions), find_similar_cases (25 nearest training transactions), get_review_policy; answers through a structured submit_recommendation tool (escalate / monitor / clear, summary, evidence, injection flag).
- Guardrail in code re-applies the written policy; if the agent is less cautious, the policy wins and the case is flagged. Fails safe to policy if the agent cannot finish in 8 turns. A human always makes the final decision.
- Customer/merchant notes are marked untrusted; evaluation includes prompt-injection attacks.
- **Evaluation (3 Nov 2026), 46 labelled cases from the unseen test period:** 100% valid structured output (46/46); 100% of model probabilities quoted correctly; 98% agreement with policy before the guardrail (45/46); 1 guardrail override; 6 of 6 prompt injections resisted and reported, 0 false injection reports; 6.0 tool calls, 4.7 s average (6.0 s p95), about 4,490 input / 918 output tokens per case. Sample: 10 caught fraud, 10 missed fraud, 10 false alarms, 10 clean genuine, 6 injection.
- The one override (EVAL-014) was a real fraud scored 0.4574: the policy tool showed the monitor cut-off rounded to 0.46, so the agent recommended clear; true cut-off 0.455, so the guardrail changed it to monitor. Fixed the tool to show exact cut-offs and added a regression test.
- Keyless CI: the evaluation and deploy workflows log in to Claude with Workload Identity Federation (GitHub OIDC token exchanged for a short-lived Anthropic token; rule pinned to the repo and main branch by immutable IDs, workflow_dispatch only, Developer role, one workspace). No Claude API key stored.
- Demo page live since 3 Nov 2026: https://iilsazxkuj.execute-api.eu-west-2.amazonaws.com/demo (agent reviews of 18 demo cases, recorded during deployment with keyless Claude login). DEMO-017 and DEMO-018 are real frauds with prompt-injection notes that Jes planted as tests; never describe them as written by a real fraudster.
- Repo tests: 40 (pytest), agent tests run offline with a scripted fake Claude client.
- Claude Skill (fraud-case-review, Nov 2026): packages the review for the Claude app; NumPy-only script with the model as plain numbers, a weighted sample of past transactions (all frauds plus 25% of genuine, each weighted 4) for similar cases, demo cases without labels. Built from the real model in GitHub Actions; same scores and reasons as the deployed agent (parity test); similar-case counts are estimates (DEMO-018: about 13 of 25 vs 16 in the agent). Uploaded and enabled in Jes's Claude account.

### Marketplace App, Microsoft Power Apps (personal project)
- Built a low-code marketplace app in Power Apps, using Power Automate flows (learned through Microsoft's free Power Automate modules).


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

Python (Flask, Pandas, NumPy, Scikit-learn, PyTorch), Java, JavaScript/TypeScript (React, Next.js), SQL (T-SQL, PostgreSQL, SQL Server, SQLite), Supabase · Logistic regression, K-means, CNNs, statistical testing · AWS (Lambda, S3, EC2), Docker, Snowflake (skill only, not used on the NHS project), Git, CI/CD, REST APIs, automated testing, Agile/Jira · Tableau, Power BI, advanced Excel, PowerPoint, Power Apps, Power Automate · Financial reporting, KPI tracking, requirements gathering, process mapping

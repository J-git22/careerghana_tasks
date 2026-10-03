# Task 1: Career Quiz CLI Tool

An interactive, command-line quiz that asks users about their interests and problem-solving style to recommend a personalized technology career path.

---

## Features
- **7 Multiple-Choice Questions:** Covers real-world developer scenarios, debugging instincts, technical interests, tooling preferences, and work culture.
- **Categorized Scoring Logic:** Matches answers across 5 career paths:
  1. Software Engineering / Full-Stack Development
  2. Data Science / Machine Learning
  3. Cybersecurity Analyst / Security Engineering
  4. DevOps & Cloud Engineering
  5. Product Design & UI/UX Development
- **Detailed Results Breakdown:** Provides percentage match, visual progress bars, job description, essential skills to learn, and concrete first steps.
- **Input Validation:** Gracefully handles invalid inputs and standard EOF/interrupt signals.
- **Pure Standard Library:** Built with Python 3, requiring no external packages.

---

## How to Run

Navigate to the `task_1_career_quiz` folder and run:

```bash
python career_quiz.py
```

Or run directly with the full path:

```bash
python "c:\Users\yevug\OneDrive\Desktop\Python Dev Internship\task_1_career_quiz\career_quiz.py"
```

---

## Example Run

```text
====================================================================
           🌟 TECH CAREER PATH QUIZ (CLI) 🌟
====================================================================
 Answer 7 questions about your interests and problem-solving style
 to receive a personalized tech career recommendation!
====================================================================

1. What kind of project excites you most when starting from scratch?
   [A] Building an interactive web or mobile application from end to end.
   [B] Analyzing a large dataset to discover trends and train a predictive model.
   [C] Analyzing a system for security loopholes and hardening its defenses.
   [D] Automating server provisioning and orchestrating cloud containers.
   [E] Designing an intuitive user journey and crafting polished UI components.

👉 Your answer (A-E): A

2. When you encounter a bug or unexpected behavior, where do you look first?
   [A] Step through the source code with a debugger to trace the logical flow.
   [B] Inspect feature distributions, missing values, or statistical discrepancies.
   [C] Review network packet traces, access control logs, and authentication tokens.
   [D] Check server logs, CPU/memory metrics, and container deployment configs.
   [E] Examine user interaction feedback, accessibility tags, and layout responsiveness.

👉 Your answer (A-E): A

3. Which technical reading topic would you pick for personal study?
   [A] Clean Architecture and Software Design Patterns.
   [B] Practical Machine Learning and Statistical Inference.
   [C] Offensive Security, Penetration Testing, and Cryptography.
   [D] Site Reliability Engineering and Infrastructure as Code.
   [E] Human-Computer Interaction and Design Systems.

👉 Your answer (A-E): A

4. Which of these tasks sounds most fulfilling on a workday?
   [A] Refactoring a sluggish API to make it 5x faster and easier to maintain.
   [B] Evaluating classifier metrics (F1-score, ROC AUC) and tuning hyperparameters.
   [C] Conducting a security audit and discovering an unpatched SQL injection.
   [D] Setting up an automated deployment pipeline with automated rollback.
   [E] Testing a prototype with real users and refining the onboarding flow.

👉 Your answer (A-E): D

5. Which set of tools are you most excited to master?
   [A] VS Code, Git, Python/TypeScript, and debugging toolkits.
   [B] Jupyter Notebooks, Pandas, Scikit-Learn, and SQL workbench.
   [C] Wireshark, Burp Suite, Nmap, and Kali Linux utilities.
   [D] Docker, Kubernetes, Terraform, and GitHub Actions.
   [E] Figma, Adobe XD, Tailwind CSS, and Storybook.

👉 Your answer (A-E): A

6. How do you define a job well done at the end of a sprint?
   [A] Features shipped with clean code, thorough unit tests, and no regressions.
   [B] Accurate data insights that provide actionable strategic direction.
   [C] Zero vulnerabilities detected and system assets fully protected.
   [D] Zero deployment downtime and blazing-fast release turnaround.
   [E] Users report that the interface is delightful, intuitive, and accessible.

👉 Your answer (A-E): A

7. Which team role matches your ideal working style?
   [A] Core builder collaborating with developers to implement functional requirements.
   [B] Data detective answering high-stakes business questions with evidence.
   [C] Vigilant guardian protecting user privacy and organization infrastructure.
   [D] Enablement engineer creating reliable pipelines that empower all teams.
   [E] User advocate translating empathy into seamless digital experiences.

👉 Your answer (A-E): B

====================================================================
                     📊 YOUR RESULTS 📊
====================================================================

🏆 RECOMMENDED CAREER: SOFTWARE ENGINEER / FULL-STACK DEVELOPER
--------------------------------------------------------------------
📝 Overview:
   You enjoy building complete systems, writing elegant code, and solving complex architectural problems. You thrive when creating web apps, backend APIs, or software tools from the ground up.

🛠️  Key Skills:
   • Python / JavaScript / Go
   • Data Structures & Algorithms
   • System Architecture
   • Git & Version Control
   • REST / GraphQL APIs

🚀 Recommended Next Steps:
1. Deepen object-oriented programming and algorithmic thinking.
2. Build and deploy a full-stack project (e.g. FastAPI + React/Vue).
3. Contribute to open-source repositories and study good design patterns.

📈 Match Breakdown:
--------------------------------------------------------------------
   Software Engineer              | ████████████████████ | 5/7 ( 71%)
   Data Scientist                 | ████░░░░░░░░░░░░░░░░ | 1/7 ( 14%)
   DevOps & Cloud Engineer        | ████░░░░░░░░░░░░░░░░ | 1/7 ( 14%)
   Cybersecurity Analyst          | ░░░░░░░░░░░░░░░░░░░░ | 0/7 (  0%)
   Product Designer & UI/UX Devel | ░░░░░░░░░░░░░░░░░░░░ | 0/7 (  0%)
====================================================================
```

# Python Development Internship — Task Bank Solutions (All 5 Tasks)

This repository contains complete, production-grade solutions for all 5 tasks in the **Python Development Intern Task Bank**. Every deliverable specified in the requirements has been implemented, thoroughly tested, and documented.

---

## Repository Structure

```text
Python Dev Internship/
│
├── task_1_career_quiz/
│   ├── career_quiz.py          # Interactive 7-question career quiz CLI
│   └── README.md               # Documentation and full example terminal run
│
├── task_2_resume_checker/
│   ├── resume_checker.py       # ATS-style resume vs job keywords analyzer
│   ├── sample_resume.txt       # Realistic developer intern resume input
│   ├── sample_job_keywords.txt # Target job description keywords
│   └── sample_output.txt       # Generated keyword match and gap analysis report
│
├── task_3_career_predictor/
│   ├── career_predictor.py     # Decision Tree ML classifier script
│   ├── dataset.csv             # 45-sample training dataset (skills -> category)
│   └── writeup.md              # Plain-language beginner explanation of the model
│
├── task_4_job_cleaner/
│   ├── job_cleaner.py          # Pandas data cleaning and standardization pipeline
│   ├── messy_jobs.csv          # Raw messy CSV with formatting flaws
│   └── cleaned_jobs.csv        # Standardized, deduplicated, clean output CSV
│
├── task_5_tip_generator/
│   ├── tip_generator.py        # Random daily career coach tip generator
│   └── sample_output.txt       # Example formatted output card
│
└── README.md                   # Master project overview (this file)
```

---

## Requirements & Environment

- **Python Version:** Python 3.10+ (tested on Python 3.11.9)
- **External Dependencies:** Only needed for Tasks 3 & 4 (`pandas`, `scikit-learn`). Tasks 1, 2, and 5 use the Python standard library.

Install required dependencies:

```bash
pip install pandas scikit-learn
```

---

## Tasks Summary & Running Instructions

### Task 1: Career Quiz CLI Tool
- **Description:** An interactive CLI quiz asking 7 multiple-choice questions assessing problem-solving instincts, technical preferences, and work styles to recommend a tech career path (*Software Engineering*, *Data Science / AI*, *Cybersecurity*, *Cloud & DevOps*, *UI/UX & Product*).
- **Deliverables:** Working script + README with an example run.
- **Run Command:**
  ```bash
  python task_1_career_quiz/career_quiz.py
  ```

---

### Task 2: Resume Keyword Checker
- **Description:** Compares a resume against a target job posting keyword list using regex word boundaries, computes match percentage, identifies present and missing skills, and generates an ATS compatibility report.
- **Deliverables:** Working script + sample input (`sample_resume.txt`, `sample_job_keywords.txt`) + sample output (`sample_output.txt`).
- **Run Command:**
  ```bash
  python task_2_resume_checker/resume_checker.py
  ```

---

### Task 3: Career Path Predictor — Your First ML Model
- **Description:** A Decision Tree machine learning model trained on a 45-row skills dataset that predicts a career track (*Software Engineering*, *Data Science*, *Cybersecurity*, *UI/UX Design*) based on 5 skill ratings (1-5 scale) with 91.7% test accuracy.
- **Deliverables:** Working script + dataset (`dataset.csv`) + beginner-friendly write-up (`writeup.md`).
- **Run Command (Interactive):**
  ```bash
  python task_3_career_predictor/career_predictor.py
  ```
- **Run Command (CLI Flags):**
  ```bash
  python task_3_career_predictor/career_predictor.py --coding 5 --math 2 --security 1 --design 1 --cloud 3
  ```

---

### Task 4: Job Listings Data Cleaner
- **Description:** A Pandas pipeline that cleans messy job listings by trimming whitespace, fixing irregular title and location casing, deduplicating records, parsing mixed salary formats into standardized USD numbers, normalizing mixed date formats into ISO 8601 (`YYYY-MM-DD`), and filling missing values.
- **Deliverables:** Cleaning script + before/after CSV files (`messy_jobs.csv`, `cleaned_jobs.csv`).
- **Run Command:**
  ```bash
  python task_4_job_cleaner/job_cleaner.py
  ```

---

### Task 5: Daily Career Tip Generator
- **Description:** A mini daily "career coach" that randomly selects from a curated collection of 20+ motivational quotes and actionable engineering tips, rendering a stylized ASCII terminal card. Includes category filtering and an email dispatch simulation bonus.
- **Deliverables:** Working script + example output (`sample_output.txt`).
- **Run Command:**
  ```bash
  python task_5_tip_generator/tip_generator.py
  ```
- **Run Command with Bonus Features:**
  ```bash
  # Filter by category:
  python task_5_tip_generator/tip_generator.py --category "Coding"

  # Email dispatch simulation:
  python task_5_tip_generator/tip_generator.py --email intern@example.com
  ```

#!/usr/bin/env python3
"""
Task 1: Career Quiz CLI Tool
An interactive command-line quiz that asks users about their interests,
problem-solving style, and preferences to recommend a career path in technology.
"""

import sys
from typing import Dict, List, Tuple

# Ensure UTF-8 output encoding on Windows terminals if possible
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


CAREER_PATHS = {
    "SE": {
        "title": "Software Engineer / Full-Stack Developer",
        "description": (
            "You enjoy building complete systems, writing elegant code, and solving complex architectural problems. "
            "You thrive when creating web apps, backend APIs, or software tools from the ground up."
        ),
        "key_skills": ["Python / JavaScript / Go", "Data Structures & Algorithms", "System Architecture", "Git & Version Control", "REST / GraphQL APIs"],
        "recommended_first_steps": (
            "1. Deepen object-oriented programming and algorithmic thinking.\n"
            "2. Build and deploy a full-stack project (e.g. FastAPI + React/Vue).\n"
            "3. Contribute to open-source repositories and study good design patterns."
        ),
    },
    "DS": {
        "title": "Data Scientist / Machine Learning Engineer",
        "description": (
            "You are fascinated by patterns in data, statistical rigor, and machine learning models. "
            "You love asking questions of datasets and transforming raw numbers into predictive insights."
        ),
        "key_skills": ["Python (Pandas, NumPy)", "Machine Learning (Scikit-Learn, PyTorch)", "SQL & Relational Databases", "Statistics & Probability", "Data Visualization"],
        "recommended_first_steps": (
            "1. Master data manipulation and exploratory data analysis using Pandas.\n"
            "2. Train standard ML models (Decision Trees, Regressions, Random Forests).\n"
            "3. Build data stories and participate in beginner Kaggle competitions."
        ),
    },
    "SEC": {
        "title": "Cybersecurity Analyst / Ethical Hacker",
        "description": (
            "You are inquisitive, detail-oriented, and enjoy thinking like an attacker to build unshakeable defenses. "
            "Network protocols, cryptography, and vulnerability research strongly appeal to you."
        ),
        "key_skills": ["Network Protocols (TCP/IP, DNS, SSL/TLS)", "Linux Command Line", "Penetration Testing Tools", "Security Auditing", "Python for Automation"],
        "recommended_first_steps": (
            "1. Learn network fundamentals and security basics (CompTIA Security+ style).\n"
            "2. Complete beginner rooms on TryHackMe and Hack The Box.\n"
            "3. Master the OWASP Top 10 vulnerabilities."
        ),
    },
    "OPS": {
        "title": "DevOps & Cloud Platform Engineer",
        "description": (
            "You love automation, reliability, and modern cloud infrastructure. "
            "Connecting development workflows to scalable cloud platforms excites you."
        ),
        "key_skills": ["Docker & Containerization", "CI/CD Pipelines (GitHub Actions)", "Cloud Platforms (AWS/GCP/Azure)", "Linux System Administration", "Terraform / IaC"],
        "recommended_first_steps": (
            "1. Master Linux command line and shell scripting.\n"
            "2. Containerize existing applications using Docker.\n"
            "3. Build CI/CD pipelines to automate testing and deployments."
        ),
    },
    "UX": {
        "title": "Product Designer & UI/UX Developer",
        "description": (
            "You care deeply about user experience, visual aesthetics, and empathy for the human using technology. "
            "Bridging the gap between user psychology and software implementation is your passion."
        ),
        "key_skills": ["Figma & Wireframing", "User Research & Usability Testing", "HTML5, Modern CSS & Tailwind", "Design Systems", "Interactive Prototyping"],
        "recommended_first_steps": (
            "1. Learn core UX principles (heuristics, user journeys, accessibility).\n"
            "2. Practice designing responsive interfaces in Figma.\n"
            "3. Implement designs with clean, responsive HTML/CSS/JavaScript."
        ),
    },
}

QUESTIONS: List[Dict] = [
    {
        "question": "1. What kind of project excites you most when starting from scratch?",
        "options": [
            ("A", "Building an interactive web or mobile application from end to end.", "SE"),
            ("B", "Analyzing a large dataset to discover trends and train a predictive model.", "DS"),
            ("C", "Analyzing a system for security loopholes and hardening its defenses.", "SEC"),
            ("D", "Automating server provisioning and orchestrating cloud containers.", "OPS"),
            ("E", "Designing an intuitive user journey and crafting polished UI components.", "UX"),
        ],
    },
    {
        "question": "2. When you encounter a bug or unexpected behavior, where do you look first?",
        "options": [
            ("A", "Step through the source code with a debugger to trace the logical flow.", "SE"),
            ("B", "Inspect feature distributions, missing values, or statistical discrepancies.", "DS"),
            ("C", "Review network packet traces, access control logs, and authentication tokens.", "SEC"),
            ("D", "Check server logs, CPU/memory metrics, and container deployment configs.", "OPS"),
            ("E", "Examine user interaction feedback, accessibility tags, and layout responsiveness.", "UX"),
        ],
    },
    {
        "question": "3. Which technical reading topic would you pick for personal study?",
        "options": [
            ("A", "Clean Architecture and Software Design Patterns.", "SE"),
            ("B", "Practical Machine Learning and Statistical Inference.", "DS"),
            ("C", "Offensive Security, Penetration Testing, and Cryptography.", "SEC"),
            ("D", "Site Reliability Engineering and Infrastructure as Code.", "OPS"),
            ("E", "Human-Computer Interaction and Design Systems.", "UX"),
        ],
    },
    {
        "question": "4. Which of these tasks sounds most fulfilling on a workday?",
        "options": [
            ("A", "Refactoring a sluggish API to make it 5x faster and easier to maintain.", "SE"),
            ("B", "Evaluating classifier metrics (F1-score, ROC AUC) and tuning hyperparameters.", "DS"),
            ("C", "Conducting a security audit and discovering an unpatched SQL injection.", "SEC"),
            ("D", "Setting up an automated deployment pipeline with automated rollback.", "OPS"),
            ("E", "Testing a prototype with real users and refining the onboarding flow.", "UX"),
        ],
    },
    {
        "question": "5. Which set of tools are you most excited to master?",
        "options": [
            ("A", "VS Code, Git, Python/TypeScript, and debugging toolkits.", "SE"),
            ("B", "Jupyter Notebooks, Pandas, Scikit-Learn, and SQL workbench.", "DS"),
            ("C", "Wireshark, Burp Suite, Nmap, and Kali Linux utilities.", "SEC"),
            ("D", "Docker, Kubernetes, Terraform, and GitHub Actions.", "OPS"),
            ("E", "Figma, Adobe XD, Tailwind CSS, and Storybook.", "UX"),
        ],
    },
    {
        "question": "6. How do you define a job well done at the end of a sprint?",
        "options": [
            ("A", "Features shipped with clean code, thorough unit tests, and no regressions.", "SE"),
            ("B", "Accurate data insights that provide actionable strategic direction.", "DS"),
            ("C", "Zero vulnerabilities detected and system assets fully protected.", "SEC"),
            ("D", "Zero deployment downtime and blazing-fast release turnaround.", "OPS"),
            ("E", "Users report that the interface is delightful, intuitive, and accessible.", "UX"),
        ],
    },
    {
        "question": "7. Which team role matches your ideal working style?",
        "options": [
            ("A", "Core builder collaborating with developers to implement functional requirements.", "SE"),
            ("B", "Data detective answering high-stakes business questions with evidence.", "DS"),
            ("C", "Vigilant guardian protecting user privacy and organization infrastructure.", "SEC"),
            ("D", "Enablement engineer creating reliable pipelines that empower all teams.", "OPS"),
            ("E", "User advocate translating empathy into seamless digital experiences.", "UX"),
        ],
    },
]


def display_banner() -> None:
    print("=" * 68)
    print("                 TECH CAREER PATH QUIZ (CLI)")
    print("=" * 68)
    print(" Answer 7 questions about your interests and problem-solving style")
    print(" to receive a personalized tech career recommendation!")
    print("=" * 68)


def prompt_question(q_index: int, q_data: Dict) -> str:
    print(f"\n{q_data['question']}")
    for opt, text, _ in q_data["options"]:
        print(f"   [{opt}] {text}")

    valid = {opt for opt, _, _ in q_data["options"]}
    while True:
        try:
            choice = input("\n>> Your answer (A-E): ").strip().upper()
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz exited. See you next time!")
            sys.exit(0)

        if choice in valid:
            return choice
        print(f"   [!] Invalid choice '{choice}'. Please select from: {', '.join(sorted(valid))}")


def run_quiz() -> Tuple[Dict[str, int], str]:
    scores = {key: 0 for key in CAREER_PATHS}

    for idx, q_data in enumerate(QUESTIONS, start=1):
        choice = prompt_question(idx, q_data)
        for opt, _, cat in q_data["options"]:
            if opt == choice:
                scores[cat] += 1
                break

    # Winning category
    top_cat = max(scores, key=lambda k: (scores[k], k))
    return scores, top_cat


def show_results(scores: Dict[str, int], top_cat: str) -> None:
    total_q = len(QUESTIONS)
    top_info = CAREER_PATHS[top_cat]

    print("\n" + "=" * 68)
    print("                         YOUR RESULTS")
    print("=" * 68)
    print(f"\nRECOMMENDED CAREER: {top_info['title'].upper()}")
    print("-" * 68)
    print(f"Overview:\n   {top_info['description']}\n")

    print("Key Skills:")
    for skill in top_info["key_skills"]:
        print(f"   * {skill}")

    print(f"\nRecommended Next Steps:\n{top_info['recommended_first_steps']}\n")

    print("Match Breakdown:")
    print("-" * 68)
    for cat, count in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_q) * 100
        bar = "#" * (count * 4) + "-" * ((total_q - count) * 4)
        role = CAREER_PATHS[cat]["title"].split("/")[0].strip()
        print(f"   {role:<30} | [{bar}] | {count}/{total_q} ({pct:3.0f}%)")
    print("=" * 68 + "\n")


def main() -> None:
    display_banner()
    scores, top_cat = run_quiz()
    show_results(scores, top_cat)


if __name__ == "__main__":
    main()

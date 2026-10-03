#!/usr/bin/env python3
"""
Task 5: Daily Career Tip Generator
A mini daily 'career coach' script that randomly selects and displays
curated career tips and motivational quotes in a clean, formatted terminal card.
Also includes bonus features: category filtering, viewing all tips, and email simulation.
"""

import argparse
import datetime
import random
import sys
from pathlib import Path
from typing import Dict, List, Optional

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


CAREER_TIPS: List[Dict[str, str]] = [
    {
        "id": 1,
        "category": "Coding & Craftsmanship",
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson",
        "actionable_tip": "Before typing code, sketch the logic on paper or write pseudocode comments. Clear thinking produces fewer bugs and cleaner architecture."
    },
    {
        "id": 2,
        "category": "Coding & Craftsmanship",
        "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "author": "Martin Fowler",
        "actionable_tip": "Prioritize descriptive variable names, small single-responsibility functions, and readable control flows over clever one-liners."
    },
    {
        "id": 3,
        "category": "Growth Mindset",
        "quote": "The only way to go fast, is to go well.",
        "author": "Robert C. Martin (Uncle Bob)",
        "actionable_tip": "Never rush by skipping automated tests or documentation. Investing 15 minutes in a test suite saves days of debugging down the road."
    },
    {
        "id": 4,
        "category": "Interviews & Job Search",
        "quote": "Show, don't just tell. Code speaks louder than adjectives.",
        "author": "Tech Hiring Wisdom",
        "actionable_tip": "On your resume and portfolio, quantify your achievements with real metrics (e.g. 'Improved query latency by 35% using database indexes')."
    },
    {
        "id": 5,
        "category": "Debugging & Resilience",
        "quote": "The most effective debugging tool is still careful thought, coupled with judiciously placed print statements.",
        "author": "Brian Kernighan",
        "actionable_tip": "When stuck on an error, systematically isolate variables. Reproduce it in a minimal test script rather than guessing randomly."
    },
    {
        "id": 6,
        "category": "Continuous Learning",
        "quote": "In technology, what you know today is a foundation, but your ability to learn tomorrow is your superpower.",
        "author": "Satya Nadella",
        "actionable_tip": "Dedicate 30 minutes every morning or evening to reading documentation, release notes, or engineering blogs like Netflix Tech Blog or Uber Eng."
    },
    {
        "id": 7,
        "category": "Networking & Community",
        "quote": "Your network is your net worth in software engineering.",
        "author": "Career Coach Insight",
        "actionable_tip": "Engage in tech communities (GitHub, Discord, local meetups). Share what you learn publicly—even beginner tutorials help others and establish your voice."
    },
    {
        "id": 8,
        "category": "Productivity & Focus",
        "quote": "Simplicity is prerequisite for reliability.",
        "author": "Edsger W. Dijkstra",
        "actionable_tip": "Avoid over-engineering. Do not add complex frameworks, microservices, or premature optimizations until proven necessary by profiling."
    },
    {
        "id": 9,
        "category": "Git & Collaboration",
        "quote": "Commit early, commit often, and write meaningful commit messages.",
        "author": "Version Control Best Practice",
        "actionable_tip": "Follow conventional commit standards (e.g. 'feat: add user authentication endpoint' or 'fix: resolve null check on profile payload')."
    },
    {
        "id": 10,
        "category": "Growth Mindset",
        "quote": "Mistakes are the portals of discovery.",
        "author": "James Joyce",
        "actionable_tip": "Treat every production bug or broken build as a post-mortem learning opportunity. Document the root cause and automate prevention."
    },
    {
        "id": 11,
        "category": "Interviews & Job Search",
        "quote": "Interviewers evaluate your thought process far more than memorized syntax.",
        "author": "Senior Engineering Lead",
        "actionable_tip": "During coding interviews, communicate your thoughts aloud constantly. Explain trade-offs, time complexities (Big-O), and edge cases upfront."
    },
    {
        "id": 12,
        "category": "Teamwork & Communication",
        "quote": "Great software is rarely built by lone wolves; it is crafted by empathetic teams.",
        "author": "Camille Fournier",
        "actionable_tip": "Be kind and constructive in code reviews. Ask clarifying questions instead of giving harsh directives, and praise good solutions."
    },
    {
        "id": 13,
        "category": "Career Growth",
        "quote": "Take ownership not just of your tasks, but of the end-to-end outcome.",
        "author": "Staff Engineer Advice",
        "actionable_tip": "Follow up after pushing a feature: verify telemetry, check error logs, and ensure real users are successfully adopting your changes."
    },
    {
        "id": 14,
        "category": "Coding & Craftsmanship",
        "quote": "Make it work, make it right, make it fast.",
        "author": "Kent Beck",
        "actionable_tip": "Step 1: Get a baseline functioning implementation. Step 2: Refactor for clarity and test coverage. Step 3: Optimize only bottlenecks that matter."
    },
    {
        "id": 15,
        "category": "Productivity & Focus",
        "quote": "Deep work is the ability to focus without distraction on a cognitively demanding task.",
        "author": "Cal Newport",
        "actionable_tip": "Block out uninterrupted 90-minute focus blocks for coding. Close email, mute notifications, and let flow state take over."
    },
    {
        "id": 16,
        "category": "Continuous Learning",
        "quote": "Don't just copy-paste solutions from StackOverflow or AI. Understand every line.",
        "author": "Software Craftsmanship Rule",
        "actionable_tip": "Whenever you receive a code snippet, explain it to yourself line-by-line. If there is a function you haven't seen before, look up its official docs."
    },
    {
        "id": 17,
        "category": "Interviews & Job Search",
        "quote": "A portfolio of 2 well-tested, deployed applications beats 20 unfinished tutorial repos.",
        "author": "Technical Recruiter Consensus",
        "actionable_tip": "Polish a flagship repository with a thorough README, architectural diagram, live deployment link, and clear installation instructions."
    },
    {
        "id": 18,
        "category": "Growth Mindset",
        "quote": "Imposter syndrome is common among high achievers; it means you care about your craft.",
        "author": "Mental Health in Tech",
        "actionable_tip": "Maintain a 'brag sheet' or 'done list' recording every feature you built, problem you solved, and positive feedback you received."
    },
    {
        "id": 19,
        "category": "Teamwork & Communication",
        "quote": "The best documentation is written for your future self six months from now.",
        "author": "Developer Proverb",
        "actionable_tip": "Write comments explaining WHY a non-obvious business logic decision was made, rather than repeating WHAT the syntax does."
    },
    {
        "id": 20,
        "category": "Career Growth",
        "quote": "Say 'yes' to challenges slightly outside your comfort zone.",
        "author": "Tech Leadership Principle",
        "actionable_tip": "Volunteer to investigate an unfamiliar service or draft a technical RFC. That stretch zone is where career leaps happen."
    }
]


def wrap_text(text: str, width: int = 66) -> List[str]:
    """Wraps text into lines that fit within specified width."""
    words = text.split()
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(word) + (1 if current_line else 0) <= width:
            current_line.append(word)
            current_len += len(word) + (1 if len(current_line) > 1 else 0)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)

    if current_line:
        lines.append(" ".join(current_line))
    return lines


def format_card(tip: Dict[str, str], date_str: Optional[str] = None) -> str:
    """Formats a career tip into a stylized ASCII box card."""
    if date_str is None:
        date_str = datetime.date.today().strftime("%B %d, %Y")

    card_width = 72
    inner_width = card_width - 4

    top_border = "+" + "=" * (card_width - 2) + "+"
    bottom_border = "+" + "=" * (card_width - 2) + "+"
    divider = "|" + "-" * (card_width - 2) + "|"

    header_title = "DAILY CAREER COACH & MOTIVATION"
    category_line = f"Category: {tip['category']}  |  Tip #{tip['id']}"

    output = [
        top_border,
        f"|  {header_title.center(inner_width)}  |",
        f"|  {date_str.center(inner_width)}  |",
        divider,
        f"|  {category_line:<{inner_width}}  |",
        divider,
        f"|{' ' * (card_width - 2)}|",
    ]

    # Quote lines
    quote_text = f'"{tip["quote"]}"'
    for q_line in wrap_text(quote_text, inner_width - 4):
        output.append(f"|    {q_line:<{inner_width - 2}}|")

    author_line = f"— {tip['author']}"
    output.append(f"|    {author_line:>{inner_width - 4}}  |")
    output.append(f"|{' ' * (card_width - 2)}|")
    output.append(divider)

    # Actionable tip
    output.append(f"|  TODAY'S ACTIONABLE CHALLENGE:{' ' * (inner_width - 28)}|")
    for tip_line in wrap_text(tip["actionable_tip"], inner_width - 4):
        output.append(f"|    • {tip_line:<{inner_width - 4}}|")

    output.append(f"|{' ' * (card_width - 2)}|")
    output.append(bottom_border)

    return "\n".join(output)


def simulate_send_email(tip: Dict[str, str], recipient: str) -> None:
    """Simulates or formats an email dispatch of the daily career tip."""
    subject = f"Daily Career Coach Tip: {tip['category']}"
    print(f"\n[EMAIL BONUS MODE]")
    print(f"Simulating dispatch to: <{recipient}>")
    print(f"Subject: {subject}")
    print(f"Body:")
    print("-" * 50)
    print(f"Hello!\n\nHere is your daily career insight for today:\n")
    print(f'"{tip["quote"]}"\n— {tip["author"]}\n')
    print(f"Actionable Tip:\n{tip['actionable_tip']}\n")
    print("Keep advancing your engineering journey!")
    print("-" * 50)
    print("[SUCCESS] Email payload compiled and simulation complete.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Daily Career Tip Generator - A mini daily career coach for aspiring engineers."
    )
    parser.add_argument(
        "--category",
        "-c",
        type=str,
        default=None,
        help="Filter tip by category (e.g. 'Coding', 'Mindset', 'Interviews', 'Networking', 'Productivity')",
    )
    parser.add_argument(
        "--list-all",
        action="store_true",
        help="List all available career tips in the database",
    )
    parser.add_argument(
        "--email",
        type=str,
        default=None,
        help="Simulate sending daily career tip to an email address (Bonus feature)",
    )
    parser.add_argument(
        "--save",
        "-s",
        type=Path,
        default=None,
        help="Save generated output to specified file (default: None)",
    )

    args = parser.parse_args()

    if args.list_all:
        print(f"\nCurated Career Tips Database ({len(CAREER_TIPS)} total tips):\n")
        for tip in CAREER_TIPS:
            print(f"[{tip['id']:2d}] [{tip['category']}] \"{tip['quote']}\" — {tip['author']}")
        return

    # Filter by category if requested
    pool = CAREER_TIPS
    if args.category:
        filtered = [
            t for t in CAREER_TIPS
            if args.category.lower() in t["category"].lower()
        ]
        if filtered:
            pool = filtered
        else:
            print(f"Notice: No tips matched category '{args.category}'. Selecting from full collection.")

    selected_tip = random.choice(pool)
    card_output = format_card(selected_tip)

    print("\n" + card_output + "\n")

    # Email simulation bonus
    if args.email:
        simulate_send_email(selected_tip, args.email)

    # Save to file if specified
    if args.save:
        try:
            with open(args.save, "w", encoding="utf-8") as f:
                f.write(card_output + "\n")
                if args.email:
                    f.write(f"\n(Dispatched to: {args.email})\n")
            print(f"[OK] Output saved to: {args.save}")
        except Exception as e:
            print(f"Error saving to file: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

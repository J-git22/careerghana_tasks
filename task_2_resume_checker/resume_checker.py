#!/usr/bin/env python3
"""
Task 2: Resume Keyword Checker
A tool that reads a resume text file, compares it against a list of keywords
from a job posting, and prints which keywords are present and missing,
along with match statistics.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def load_file_lines(file_path: Path) -> List[str]:
    """Reads non-empty, non-comment lines from a text file."""
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = []
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                lines.append(stripped)
        return lines


def read_text(file_path: Path) -> str:
    """Reads the full content of a text file."""
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def analyze_resume(resume_text: str, keywords: List[str]) -> Tuple[List[Tuple[str, int]], List[str]]:
    """
    Checks each keyword against the resume text using case-insensitive
    word boundary matching. Returns (present_keywords_with_counts, missing_keywords).
    Handles singular/plural variations (e.g. API / APIs).
    """
    present = []
    missing = []

    for kw in keywords:
        # Build regex patterns: primary keyword, plus singular variant if ends with 's'
        patterns = [rf"\b{re.escape(kw)}\b"]
        if kw.endswith("s") and len(kw) > 3:
            patterns.append(rf"\b{re.escape(kw[:-1])}\b")
        elif not kw.endswith("s"):
            patterns.append(rf"\b{re.escape(kw)}s\b")

        combined_pattern = "|".join(patterns)
        matches = re.findall(combined_pattern, resume_text, flags=re.IGNORECASE)
        count = len(matches)

        if count > 0:
            present.append((kw, count))
        else:
            missing.append(kw)

    # Sort present by frequency descending, then alphabetically
    present.sort(key=lambda x: (-x[1], x[0].lower()))
    missing.sort(key=lambda x: x.lower())
    return present, missing


def format_report(resume_path: Path, keywords_path: Path, present: List[Tuple[str, int]], missing: List[str]) -> str:
    """Formats the resume keyword check into a clean, human-readable report."""
    total_keywords = len(present) + len(missing)
    matched_count = len(present)
    missing_count = len(missing)
    match_pct = (matched_count / total_keywords * 100) if total_keywords > 0 else 0.0

    if match_pct >= 80:
        rating = "EXCELLENT MATCH (Strong candidate for this role)"
    elif match_pct >= 60:
        rating = "GOOD MATCH (Meets most core qualifications)"
    elif match_pct >= 40:
        rating = "MODERATE MATCH (Consider tailoring resume to highlight missing skills)"
    else:
        rating = "LOW MATCH (Significant keyword gap detected)"

    lines = [
        "=" * 70,
        "                    RESUME KEYWORD CHECKER REPORT",
        "=" * 70,
        f"Resume File:   {resume_path.name}",
        f"Keywords File: {keywords_path.name}",
        f"Total Keywords Analyzed: {total_keywords}",
        f"Keywords Found:          {matched_count} ({match_pct:.1f}%)",
        f"Keywords Missing:        {missing_count} ({100 - match_pct:.1f}%)",
        f"Compatibility Rating:    {rating}",
        "-" * 70,
        "",
        f"[+] FOUND KEYWORDS ({matched_count}):",
        "    The following skills/technologies from the job posting are on the resume:",
    ]

    if present:
        for kw, count in present:
            times = f"({count} occurrence{'s' if count != 1 else ''})"
            lines.append(f"    [X] {kw:<24} {times}")
    else:
        lines.append("    (None found)")

    lines.append("")
    lines.append(f"[-] MISSING KEYWORDS ({missing_count}):")
    lines.append("    The following skills/technologies from the job posting were NOT found:")

    if missing:
        for kw in missing:
            lines.append(f"    [ ] {kw}")
    else:
        lines.append("    (All keywords are present! Outstanding match!)")

    lines.append("")
    lines.append("=" * 70)
    lines.append("RECOMMENDATION / ACTIONABLE ADVICE:")
    if missing:
        lines.append(f"• If you have experience with any of the {missing_count} missing keywords above,")
        lines.append("  make sure to explicitly include them in your skills, project bullet points,")
        lines.append("  or experience descriptions to improve your ATS (Applicant Tracking System) score.")
    else:
        lines.append("• Your resume covers 100% of the target job keywords!")
    lines.append("=" * 70)

    return "\n".join(lines)


def main() -> None:
    default_base = Path(__file__).resolve().parent
    default_resume = default_base / "sample_resume.txt"
    default_keywords = default_base / "sample_job_keywords.txt"
    default_output = default_base / "sample_output.txt"

    parser = argparse.ArgumentParser(
        description="Check whether a resume contains target keywords from a job posting."
    )
    parser.add_argument(
        "--resume",
        "-r",
        type=Path,
        default=default_resume,
        help="Path to resume text file (default: sample_resume.txt)",
    )
    parser.add_argument(
        "--keywords",
        "-k",
        type=Path,
        default=default_keywords,
        help="Path to job keywords list file (default: sample_job_keywords.txt)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=default_output,
        help="Path to save report output file (default: sample_output.txt)",
    )

    args = parser.parse_args()

    print(f"Loading resume from:   {args.resume}")
    print(f"Loading keywords from: {args.keywords}")

    try:
        resume_text = read_text(args.resume)
        keywords = load_file_lines(args.keywords)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not keywords:
        print("Error: Keywords file is empty.", file=sys.stderr)
        sys.exit(1)

    present, missing = analyze_resume(resume_text, keywords)
    report = format_report(args.resume, args.keywords, present, missing)

    # Print to console
    print("\n" + report)

    # Save to output file
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as out_f:
                out_f.write(report + "\n")
            print(f"\n[OK] Report successfully written to: {args.output}")
        except Exception as e:
            print(f"Warning: Could not save output to file: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Task 4: Job Listings Data Cleaner
Reads a messy job listings CSV with inconsistent formatting, casing,
whitespace, dates, salaries, and missing values, cleans and standardizes it,
and outputs a clean CSV.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ACRONYMS = {"AI", "ML", "UI", "UX", "QA", "API", "REST", "SQL", "AWS", "GCP", "IT", "HR", "IOS", "FT", "PT", "DC"}


def clean_title(title: str) -> str:
    """Standardizes job title casing while preserving common tech acronyms."""
    if pd.isna(title):
        return "Unknown Role"

    words = str(title).strip().split()
    cleaned_words = []
    for w in words:
        cleaned_w = re.sub(r"[^\w/]", "", w).upper()
        if w.startswith("(") and w.endswith(")"):
            inner = w[1:-1]
            if "/" in inner:
                parts = [clean_title(p) for p in inner.split("/")]
                cleaned_words.append(f"({'/'.join(parts)})")
            else:
                cleaned_words.append(f"({clean_title(inner)})")
        elif "/" in w:
            # Handle combinations like UI/UX
            parts = [clean_title(p) for p in w.split("/")]
            cleaned_words.append("/".join(parts))
        elif cleaned_w in ACRONYMS:
            cleaned_words.append(cleaned_w)
        else:
            cleaned_words.append(w.capitalize())

    result = " ".join(cleaned_words)
    # Common replacements
    result = (
        result.replace("Ui/Ux", "UI/UX")
        .replace("Ai", "AI")
        .replace("Qa", "QA")
        .replace("Ios", "iOS")
        .replace("IOS", "iOS")
        .replace("Devops", "DevOps")
    )
    return result


def clean_location(loc: str) -> str:
    """Standardizes location strings (e.g. 'new york, ny' -> 'New York, NY', 'remote' -> 'Remote')."""
    if pd.isna(loc):
        return "Not Specified"

    loc = str(loc).strip()
    if loc.lower() == "remote":
        return "Remote"

    if "," in loc:
        parts = loc.split(",", 1)
        city = parts[0].strip().title()
        state = parts[1].strip().upper()
        return f"{city}, {state}"

    return loc.title()


def clean_job_type(jtype: str) -> str:
    """Standardizes job type into canonical values."""
    if pd.isna(jtype):
        return "Full-Time"

    norm = str(jtype).strip().lower().replace("-", " ").replace("  ", " ")
    if norm in ("full time", "ft", "fulltime"):
        return "Full-Time"
    elif norm in ("part time", "pt", "parttime"):
        return "Part-Time"
    elif "contract" in norm:
        return "Contract"
    elif "intern" in norm:
        return "Internship"
    return str(jtype).strip().title()


def parse_salary_range(val: str) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    """
    Parses messy salary representations into (min_salary, max_salary, avg_salary)
    in annual USD integers.
    Handles:
      - "$110,000 - $130,000" -> 110000, 130000, 120000
      - "$130k - $160k"        -> 130000, 160000, 145000
      - "$140,000 / yr"        -> 140000, 140000, 140000
      - "$35/hr"               -> 72800,  72800,  72800 (assuming standard 2080 annual hrs)
      - "Competitive", "DOE"   -> None, None, None
    """
    if pd.isna(val):
        return None, None, None

    text = str(val).strip().lower()

    # Non-numeric competitive / DOE
    if any(term in text for term in ("competitive", "doe", "negotiable", "tbd")):
        return None, None, None

    # Hourly rate: e.g. "$35/hr"
    hourly_match = re.search(r"\$?(\d+(?:\.\d+)?)\s*/?\s*hr", text)
    if hourly_match:
        hourly_rate = float(hourly_match.group(1))
        annual_val = int(hourly_rate * 2080)
        return annual_val, annual_val, annual_val

    # Standardize 'k' suffix: $95k -> 95000
    text = re.sub(r"(\d+)\s*k\b", r"\g<1>000", text)
    # Remove commas and dollar signs
    text = text.replace(",", "").replace("$", "")

    # Look for number pairs
    nums = [int(n) for n in re.findall(r"\d+", text)]
    if len(nums) >= 2:
        min_s = min(nums[0], nums[1])
        max_s = max(nums[0], nums[1])
        avg_s = int((min_s + max_s) / 2)
        return min_s, max_s, avg_s
    elif len(nums) == 1:
        return nums[0], nums[0], nums[0]

    return None, None, None


def clean_job_listings(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Reads messy CSV, executes full standardization pipeline, and outputs cleaned CSV."""
    if not input_path.is_file():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df_raw = pd.read_csv(input_path)
    initial_count = len(df_raw)
    print(f"Loaded raw dataset from: {input_path.name}")
    print(f"Initial shape: {initial_count} rows, {df_raw.shape[1]} columns\n")

    df = df_raw.copy()

    # 1. Standardize column names (strip whitespace, lowercase, snake_case)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # 2. Strip whitespace from all string columns
    for col in df.columns:
        if df[col].dtype == object or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].astype(str).str.strip()
            # Restore genuine NaNs
            df[col] = df[col].replace({"nan": None, "": None})

    # 3. Deduplicate listings based on job_title, company_name, and location
    df["title_norm"] = df["job_title"].str.lower()
    df["company_norm"] = df["company_name"].str.lower()
    df["loc_norm"] = df["location"].str.lower()
    df = df.drop_duplicates(subset=["title_norm", "company_norm", "loc_norm"]).copy()
    df = df.drop(columns=["title_norm", "company_norm", "loc_norm"])
    dropped_dupes = initial_count - len(df)

    # 4. Standardize Job Titles and Company Names
    df["job_title"] = df["job_title"].apply(clean_title)
    df["company_name"] = df["company_name"].apply(lambda c: c.title() if pd.notna(c) else "Confidential")

    # 5. Standardize Locations
    df["location"] = df["location"].apply(clean_location)

    # 6. Standardize Job Types
    df["job_type"] = df["job_type"].apply(clean_job_type)

    # 7. Parse and decompose salary range into structured integer fields
    salaries = df["salary_range"].apply(parse_salary_range)
    df["min_salary_usd"] = [s[0] for s in salaries]
    df["max_salary_usd"] = [s[1] for s in salaries]
    df["avg_salary_usd"] = [s[2] for s in salaries]

    # Cast salary fields to nullable integer type Int64
    df["min_salary_usd"] = df["min_salary_usd"].astype("Int64")
    df["max_salary_usd"] = df["max_salary_usd"].astype("Int64")
    df["avg_salary_usd"] = df["avg_salary_usd"].astype("Int64")

    # 8. Standardize posted dates to ISO format (YYYY-MM-DD)
    df["posted_date"] = pd.to_datetime(df["posted_date"], format="mixed", errors="coerce").dt.strftime("%Y-%m-%d")
    df["posted_date"] = df["posted_date"].fillna("2026-08-01")

    # 9. Clean department column
    df["department"] = df["department"].fillna("General / Not Specified")
    df["department"] = df["department"].apply(lambda d: clean_title(d) if d else "General / Not Specified")

    # 10. Reorder columns for clean delivery
    ordered_cols = [
        "job_id",
        "job_title",
        "company_name",
        "department",
        "location",
        "job_type",
        "min_salary_usd",
        "max_salary_usd",
        "avg_salary_usd",
        "posted_date",
    ]
    cleaned_df = df[ordered_cols].sort_values("job_id").reset_index(drop=True)

    # Save to clean CSV
    cleaned_df.to_csv(output_path, index=False)

    print("=" * 72)
    print("                      CLEANING AUDIT REPORT")
    print("=" * 72)
    print(f"Raw Input Rows:      {initial_count}")
    print(f"Duplicate Rows Cut:  {dropped_dupes}")
    print(f"Clean Rows Exported: {len(cleaned_df)}")
    print(f"Output File:         {output_path.name}")
    print("-" * 72)
    print("Summary of Cleaned Data Sample:")
    display_cols = ["job_id", "job_title", "company_name", "location", "job_type", "avg_salary_usd", "posted_date"]
    print(cleaned_df[display_cols].head(8).to_string(index=False))
    print("=" * 72 + "\n")

    return cleaned_df


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    default_input = base_dir / "messy_jobs.csv"
    default_output = base_dir / "cleaned_jobs.csv"

    parser = argparse.ArgumentParser(description="Clean and standardize messy job listing CSV data.")
    parser.add_argument("--input", "-i", type=Path, default=default_input, help="Input messy CSV file")
    parser.add_argument("--output", "-o", type=Path, default=default_output, help="Output cleaned CSV file")

    args = parser.parse_args()
    clean_job_listings(args.input, args.output)


if __name__ == "__main__":
    main()

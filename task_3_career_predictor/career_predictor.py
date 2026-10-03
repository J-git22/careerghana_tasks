#!/usr/bin/env python3
"""
Task 3: Career Path Predictor — Your First ML Model
Uses a Decision Tree classifier trained on skills/interests data to predict
the most suitable tech career category for a candidate.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

FEATURE_COLUMNS = [
    "coding",
    "math_statistics",
    "networking_security",
    "visual_design",
    "cloud_sysadmin",
]

FEATURE_LABELS = {
    "coding": "Coding & Software Logic (1-5)",
    "math_statistics": "Math, Statistics & Data (1-5)",
    "networking_security": "Networking & Cybersecurity (1-5)",
    "visual_design": "UI/UX & Visual Design (1-5)",
    "cloud_sysadmin": "Cloud, Linux & DevOps (1-5)",
}


def load_and_train_model(dataset_path: Path) -> Tuple[DecisionTreeClassifier, float, pd.DataFrame]:
    """
    Loads dataset from CSV, splits into train/test sets, and trains
    a Decision Tree Classifier. Returns (trained_model, test_accuracy, raw_df).
    """
    if not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset file not found at: {dataset_path}")

    df = pd.read_csv(dataset_path)

    # Validate schema
    required_cols = FEATURE_COLUMNS + ["career_category"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column in dataset: '{col}'")

    X = df[FEATURE_COLUMNS]
    y = df["career_category"]

    # Stratified train/test split to ensure balanced representation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # Train Decision Tree
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    return model, acc, df


def display_model_summary(model: DecisionTreeClassifier, accuracy: float, df: pd.DataFrame) -> None:
    """Displays training metrics, class distributions, and feature importances."""
    print("=" * 68)
    print("        CAREER PATH PREDICTOR - MACHINE LEARNING MODEL")
    print("=" * 68)
    print(f"Dataset:            {len(df)} total profile samples")
    print(f"Features:           {', '.join(FEATURE_COLUMNS)}")
    print(f"Target Categories:  {', '.join(sorted(df['career_category'].unique()))}")
    print(f"Test Accuracy:      {accuracy * 100:.1f}% on holdout test set")
    print("-" * 68)
    print("Feature Importance (how much each skill influences the tree):")
    importances = model.feature_importances_
    sorted_idx = importances.argsort()[::-1]
    for idx in sorted_idx:
        feat_name = FEATURE_COLUMNS[idx]
        imp_score = importances[idx]
        bar = "#" * int(imp_score * 30)
        print(f"   {feat_name:<22} | [{bar:<30}] {imp_score * 100:5.1f}%")
    print("=" * 68)


def prompt_user_skills() -> Dict[str, int]:
    """Prompts user interactively to rate their skill levels on 1 to 5 scale."""
    print("\nPlease rate your interest / skill level for each domain (1 = Novice, 5 = Expert):")
    user_skills = {}
    for feat in FEATURE_COLUMNS:
        label = FEATURE_LABELS[feat]
        while True:
            try:
                raw_input = input(f"   >> {label}: ").strip()
                val = int(raw_input)
                if 1 <= val <= 5:
                    user_skills[feat] = val
                    break
                print("      [!] Please enter an integer between 1 and 5.")
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled. Exiting.")
                sys.exit(0)
            except ValueError:
                print("      [!] Invalid input. Please enter a number from 1 to 5.")
    return user_skills


def predict_career(model: DecisionTreeClassifier, skills: Dict[str, int]) -> Tuple[str, Dict[str, float]]:
    """Runs inference on a skill dictionary and returns prediction + probability breakdown."""
    input_df = pd.DataFrame([skills])[FEATURE_COLUMNS]
    predicted_category = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    classes = model.classes_

    prob_dict = {classes[i]: probabilities[i] for i in range(len(classes))}
    return predicted_category, prob_dict


def display_prediction(predicted_career: str, prob_dict: Dict[str, float], skills: Dict[str, int]) -> None:
    """Formats and prints the predicted career result with probability distribution."""
    print("\n" + "=" * 68)
    print("                       PREDICTION RESULT")
    print("=" * 68)
    print(f"Input Profile:      {skills}")
    print(f"Predicted Career:   >>> {predicted_career.upper()} <<<")
    print("-" * 68)
    print("Model Confidence Breakdown:")
    for cat, prob in sorted(prob_dict.items(), key=lambda x: -x[1]):
        pct = prob * 100
        bar = "#" * int(prob * 25)
        print(f"   {cat:<24} | [{bar:<25}] {pct:5.1f}%")
    print("=" * 68 + "\n")


def main() -> None:
    dataset_file = Path(__file__).resolve().parent / "dataset.csv"

    parser = argparse.ArgumentParser(
        description="Predict suitable career category based on top skills using a Decision Tree ML model."
    )
    parser.add_argument("--coding", type=int, choices=range(1, 6), help="Coding proficiency (1-5)")
    parser.add_argument("--math", type=int, choices=range(1, 6), help="Math & Statistics proficiency (1-5)")
    parser.add_argument("--security", type=int, choices=range(1, 6), help="Networking & Security proficiency (1-5)")
    parser.add_argument("--design", type=int, choices=range(1, 6), help="UI/UX & Visual Design (1-5)")
    parser.add_argument("--cloud", type=int, choices=range(1, 6), help="Cloud & DevOps proficiency (1-5)")
    parser.add_argument("--eval-only", action="store_true", help="Print model evaluation metrics and exit")

    args = parser.parse_args()

    # Load and train
    model, accuracy, df = load_and_train_model(dataset_file)
    display_model_summary(model, accuracy, df)

    if args.eval_only:
        return

    # Check if all features supplied via CLI
    cli_features_provided = all(
        v is not None for v in [args.coding, args.math, args.security, args.design, args.cloud]
    )

    if cli_features_provided:
        user_skills = {
            "coding": args.coding,
            "math_statistics": args.math,
            "networking_security": args.security,
            "visual_design": args.design,
            "cloud_sysadmin": args.cloud,
        }
    else:
        user_skills = prompt_user_skills()

    pred_cat, probs = predict_career(model, user_skills)
    display_prediction(pred_cat, probs, user_skills)


if __name__ == "__main__":
    main()

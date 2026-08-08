#!/usr/bin/env python3
"""Validate OKF v0.2 frontmatter in LCS artifact files.

Usage:
    python validate-okf.py <file_or_directory> [--strict] [--fix]
    
Checks:
    - Required OKF fields: title, format_version, authors, created, updated
    - LCS extensions: artifact_type, source, cot_level
    - Status lifecycle: draft → reviewed → active → archived
    - Timestamp format: ISO-8601
    - artifact_type against registry
"""

import re
import sys
import yaml
from pathlib import Path
from datetime import datetime

OKF_REQUIRED = {"title", "format_version", "authors", "created", "updated"}
OKF_RECOMMENDED = {"tags", "summary", "status", "related"}
LCS_REQUIRED = {"artifact_type", "source", "cot_level"}
LCS_OPTIONAL = {"artifact_id", "version"}
ALL_FIELDS = OKF_REQUIRED | OKF_RECOMMENDED | LCS_REQUIRED | LCS_OPTIONAL

VALID_STATUSES = {"draft", "reviewed", "active", "archived"}
VALID_COT_LEVELS = {"light", "standard", "strict", "very_strict"}
VALID_ARTIFACT_TYPES = {
    "explore", "prd", "prd_enhanced", "srs", "tests", "api", "db",
    "traceability", "task_coverage", "task", "debug", "debug_ext",
    "code_review", "codebase_doc", "onboarding", "onboarding_map",
    "final_doc", "final_map", "analysis", "session_log",
    "domain_model", "research", "prototype", "wayfinder", "wizard",
    "execution_log",
}

TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}|T\d{2}:\d{2}:\d{2}Z)?$")


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """Extract YAML frontmatter and body from markdown."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else None, parts[2]
    except yaml.YAMLError:
        return None, text


def validate_file(path: Path, strict: bool = False) -> list[dict]:
    """Validate OKF frontmatter in a single file. Returns list of issues."""
    issues = []
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if fm is None:
        issues.append({"level": "ERROR", "msg": "Missing or invalid YAML frontmatter"})
        return issues

    # Check required OKF fields
    for field in sorted(OKF_REQUIRED):
        if field not in fm:
            issues.append({"level": "ERROR", "msg": f"Missing OKF required field: {field}"})

    # Check LCS required fields
    for field in sorted(LCS_REQUIRED):
        if field not in fm:
            issues.append({"level": "ERROR", "msg": f"Missing LCS required field: {field}"})

    # Validate format_version
    if "format_version" in fm and fm["format_version"] != "okf/0.2":
        issues.append({"level": "WARN", "msg": f"format_version is '{fm.get('format_version')}', expected 'okf/0.2'"})

    # Validate status
    if "status" in fm and fm["status"] not in VALID_STATUSES:
        issues.append({"level": "ERROR", "msg": f"Invalid status: '{fm['status']}'. Allowed: {VALID_STATUSES}"})

    # Validate cot_level
    if "cot_level" in fm and fm["cot_level"] not in VALID_COT_LEVELS:
        issues.append({"level": "ERROR", "msg": f"Invalid cot_level: '{fm['cot_level']}'. Allowed: {VALID_COT_LEVELS}"})

    # Validate artifact_type
    if "artifact_type" in fm and fm["artifact_type"] not in VALID_ARTIFACT_TYPES:
        issues.append({"level": "ERROR", "msg": f"Unknown artifact_type: '{fm['artifact_type']}'"})

    # Validate timestamps
    for ts_field in ("created", "updated"):
        if ts_field in fm:
            val = str(fm[ts_field])
            if not TIMESTAMP_RE.match(val):
                issues.append({"level": "ERROR", "msg": f"Invalid {ts_field} format: '{val}'. Expected ISO-8601."})

    # Validate authors structure
    if "authors" in fm:
        authors = fm["authors"]
        if not isinstance(authors, list) or len(authors) == 0:
            issues.append({"level": "ERROR", "msg": "authors must be a non-empty list"})
        elif strict:
            for i, author in enumerate(authors):
                if not isinstance(author, dict):
                    issues.append({"level": "WARN", "msg": f"authors[{i}] is not a dict"})
                elif "type" not in author or "name" not in author:
                    issues.append({"level": "WARN", "msg": f"authors[{i}] missing 'type' or 'name'"})

    # Strict mode: check recommended fields
    if strict:
        for field in sorted(OKF_RECOMMENDED):
            if field not in fm:
                issues.append({"level": "WARN", "msg": f"Missing recommended field: {field}"})

    # Check for unknown fields
    unknown = set(fm.keys()) - ALL_FIELDS
    if unknown:
        issues.append({"level": "WARN", "msg": f"Unknown fields: {sorted(unknown)}"})

    return issues


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate OKF v0.2 frontmatter")
    parser.add_argument("path", help="File or directory to validate")
    parser.add_argument("--strict", action="store_true", help="Also check recommended fields")
    parser.add_argument("--fix", action="store_true", help="Suggest fixes (not implemented)")
    args = parser.parse_args()

    target = Path(args.path)
    files = [target] if target.is_file() else sorted(target.rglob("*.md"))

    errors = 0
    warnings = 0
    for f in files:
        if f.name.startswith(".") or "node_modules" in str(f):
            continue
        issues = validate_file(f, strict=args.strict)
        if issues:
            print(f"\n{f}:")
            for issue in issues:
                prefix = "ERROR" if issue["level"] == "ERROR" else "WARN "
                print(f"  [{prefix}] {issue['msg']}")
                if issue["level"] == "ERROR":
                    errors += 1
                else:
                    warnings += 1

    print(f"\n{'='*40}")
    print(f"Files checked: {len(files)}")
    print(f"Errors: {errors}")
    print(f"Warnings: {warnings}")
    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()

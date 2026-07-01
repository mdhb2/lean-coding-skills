#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def ids(text: str, pattern: str) -> list[str]:
    return list(dict.fromkeys(re.findall(pattern, text)))


def report(level: str, message: str) -> None:
    print(f"{level}: {message}")


def find_work_item(explicit: str) -> Path | None:
    if explicit:
        return Path(explicit)
    state = read_text(Path(".lcs/state.md"))
    match = re.search(r"\.lcs[/\\]work-items[/\\][A-Za-z0-9._-]+", state)
    return Path(match.group(0)) if match else None


def check_chain_of_truth_before_handoff(text: str, label: str) -> list[str]:
    failures = []
    if re.search(r"^##\s+Handoff\s*$", text, re.MULTILINE):
        if not re.search(r"##\s+Chain of Truth Report.*##\s+Handoff", text, re.DOTALL):
            failures.append(f"{label}: missing Chain of Truth Report before Handoff")
    return failures


def has_test_mapping(ac_id: str, tests: str) -> bool:
    for line in tests.splitlines():
        if ac_id in line and re.search(r"TEST-\d{3}", line):
            return True

    sections = re.split(r"(?=^#{2,3}\s+TEST-\d{3}\b)", tests, flags=re.MULTILINE)
    return any(ac_id in section and re.search(r"^#{2,3}\s+TEST-\d{3}\b", section, re.MULTILINE) for section in sections)


def check_artifact_existence(work_item: Path) -> list[str]:
    failures = []
    index_path = work_item / "index.md"
    if index_path.exists():
        content = read_text(index_path)
        for line in content.splitlines():
            m = re.search(r'\|.*\[([^\]]+)\]\(([^)]+)\).*\|', line)
            if m:
                artifact_path = work_item / m.group(2)
                if not artifact_path.exists():
                    failures.append(f"index.md lists {m.group(1)} at {m.group(2)} but file does not exist")
    return failures


def check_frontmatter_fields(path: Path) -> list[str]:
    failures = []
    content = read_text(path)
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if m:
        yaml = m.group(1)
        required = ["type", "artifact_type", "status", "source", "timestamp"]
        for field in required:
            if not re.search(rf"^{field}\s*:", yaml, re.MULTILINE):
                failures.append(f"{path}: missing required frontmatter field: {field}")
        status_m = re.search(r"^status\s*:\s*(.+)$", yaml, re.MULTILINE)
        if status_m:
            status = status_m.group(1).strip()
            if not re.match(r'^(draft|review|final)', status):
                failures.append(f"{path}: invalid status value: {status} (expected draft, review, or final)")
        ts_m = re.search(r"^timestamp\s*:\s*(.+)$", yaml, re.MULTILINE)
        if ts_m:
            ts = ts_m.group(1).strip()
            if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$', ts):
                failures.append(f"{path}: invalid timestamp format: {ts} (expected ISO 8601)")
    return failures


def check_task_verification(task_dir: Path) -> list[str]:
    failures = []
    if not task_dir.exists():
        return failures
    for task_path in sorted(task_dir.glob("task-*.md")):
        text = read_text(task_path)
        if re.search(r"\*\*Status\*\*:\s*done", text):
            if not re.search(r"Verif(ication|y)|evidence|Task result", text):
                failures.append(f"{task_path.name} is done but missing verification or execution evidence")
    return failures


def check_dependency(task_dir: Path) -> list[str]:
    failures = []
    if not task_dir.exists():
        return failures
    statuses = {}
    for task_path in sorted(task_dir.glob("task-*.md")):
        text = read_text(task_path)
        m = re.search(r"\*\*Status\*\*:\s*(\w+)", text)
        if m:
            statuses[task_path.name] = m.group(1)
    for task_path in sorted(task_dir.glob("task-*.md")):
        text = read_text(task_path)
        m = re.search(r"\*\*Depends on\*\*:\s*(.+)", text)
        if m:
            deps = [d.strip() for d in m.group(1).split(",")]
            for dep in deps:
                if dep and dep in statuses and statuses[dep] != "done":
                    failures.append(f"{task_path.name} depends on {dep} which is not done (status: {statuses[dep]})")
    return failures


def check_resource_path(content: str, label: str) -> list[str]:
    failures = []
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if m:
        yaml = m.group(1)
        prev_m = re.search(r"^previous_artifact\s*:\s*(.+)$", yaml, re.MULTILINE)
        if prev_m:
            path_str = prev_m.group(1).strip()
            if path_str and path_str != "optional/path" and not Path(path_str).exists():
                failures.append(f"{label}: previous_artifact path does not exist: {path_str}")
    return failures


def check_source_path(content: str, label: str) -> list[str]:
    failures = []
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if m:
        yaml = m.group(1)
        src_m = re.search(r"^source\s*:\s*(.+)$", yaml, re.MULTILINE)
        if src_m:
            source = src_m.group(1).strip()
            if re.match(r'^\.\.[/\\]', source):
                failures.append(f"{label}: source field escapes .lcs/ directory: {source}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate LCS requirement traceability.")
    parser.add_argument("--work-item", default="", help="Path to .lcs/work-items/{timestamp}-{slug-work-item}")
    args = parser.parse_args()

    work_item = find_work_item(args.work_item)
    if not work_item:
        report("FAIL", "Cannot locate active work item from .lcs/state.md. Pass --work-item explicitly.")
        return 1
    if not work_item.exists():
        report("FAIL", f"Work item path not found: {work_item}")
        return 1

    failures: list[str] = []
    warnings: list[str] = []

    prd = read_text(work_item / "prd.md")
    enhanced = read_text(work_item / "prd-enhanced.md")
    srs = read_text(work_item / "srs.md")
    tests = read_text(work_item / "tests.md")
    traceability = read_text(work_item / "traceability.md")

    src_ids = ids(prd, r"SRC-\d{3}")
    enhanced_src_ids = ids(enhanced, r"SRC-\d{3}")
    ac_ids = ids(srs, r"AC-\d{3}")
    fr_ids = ids(srs, r"FR-\d{3}")

    if not src_ids:
        warnings.append("No SRC IDs found in prd.md; legacy workflow allowed but requirement preservation is not enforceable.")

    if enhanced:
        for src_id in src_ids:
            if src_id not in enhanced_src_ids:
                failures.append(f"{src_id} exists in prd.md but not prd-enhanced.md")

        failures += check_chain_of_truth_before_handoff(enhanced, "prd-enhanced.md")

    # Check Chain of Truth in other artifacts
    for fname, content in [("prd.md", prd), ("srs.md", srs), ("tests.md", tests), ("traceability.md", traceability)]:
        if content:
            failures += check_chain_of_truth_before_handoff(content, fname)

    for ac_id in ac_ids:
        if tests and not has_test_mapping(ac_id, tests):
            failures.append(f"{ac_id} has no TEST mapping in tests.md")
    if srs and not tests:
        warnings.append("srs.md exists but tests.md is missing; AC-to-TEST validation incomplete.")

    task_dir = work_item / "task"
    task_texts: dict[str, str] = {}
    if task_dir.exists():
        for task_path in sorted(task_dir.glob("task-*.md")):
            task_texts[task_path.name] = read_text(task_path)
    else:
        warnings.append("task directory missing; AC/FR-to-TASK validation incomplete.")

    for name, text in task_texts.items():
        if not re.search(r"^\* \*\*Source coverage\*\*:", text, re.MULTILINE):
            failures.append(f"{name} missing Source coverage section")
        failures += check_chain_of_truth_before_handoff(text, name)

    for req_id in ac_ids + fr_ids:
        covered = any(req_id in text for text in task_texts.values())
        if not covered and task_texts:
            failures.append(f"{req_id} has no TASK coverage")

    if traceability:
        for src_id in src_ids:
            if src_id not in traceability:
                failures.append(f"{src_id} missing from traceability.md")
        failures += check_chain_of_truth_before_handoff(traceability, "traceability.md")
    elif src_ids:
        warnings.append("traceability.md missing; SRC downstream mapping not fully enforceable.")

    # New validation checks (TASK-004)
    failures += check_artifact_existence(work_item)

    artifact_names = ["explore.md", "debug.md", "prd.md", "prd-enhanced.md", "srs.md", "tests.md", "api.md", "db.md", "traceability.md", "task-coverage.md", "final-doc.md", "state.md"]
    for name in artifact_names:
        path = work_item / name
        if path.exists():
            content = read_text(path)
            failures += check_frontmatter_fields(path)
            failures += check_resource_path(content, name)
            failures += check_source_path(content, name)

    failures += check_task_verification(work_item / "task")
    failures += check_dependency(work_item / "task")

    for warning in warnings:
        report("WARN", warning)
    for failure in failures:
        report("FAIL", failure)

    if failures:
        return 1
    report("PASS", f"Traceability validation passed for {work_item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

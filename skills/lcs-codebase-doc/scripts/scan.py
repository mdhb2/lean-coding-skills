#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
from collections import Counter, defaultdict

IGNORE_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", ".next", "out", "coverage",
    "generated", "__pycache__", ".venv", "venv", "target", ".gradle", ".idea", ".vscode", ".cache",
    "tmp", "temp", "logs", "bin", "obj", "skills"
}

LANG_BY_EXT = {
    ".js": "JavaScript", ".cjs": "JavaScript", ".mjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".jsx": "JavaScript",
    ".py": "Python", ".go": "Go", ".rs": "Rust", ".java": "Java", ".kt": "Kotlin",
    ".cs": ".NET", ".php": "PHP", ".rb": "Ruby", ".swift": "Swift", ".dart": "Dart",
    ".sh": "Shell", ".ps1": "PowerShell", ".yml": "YAML", ".yaml": "YAML", ".json": "JSON"
}

MANIFEST_NAMES = {
    "package.json", "pnpm-workspace.yaml", "turbo.json", "nx.json", "lerna.json",
    "pyproject.toml", "requirements.txt", "Pipfile", "poetry.lock", "setup.py",
    "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "build.gradle.kts",
    "*.csproj", "composer.json", "Gemfile", "Package.swift", "pubspec.yaml"
}

LOCKFILES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "poetry.lock", "Pipfile.lock", "Cargo.lock", "composer.lock", "Gemfile.lock"}

def is_ignored(path_parts):
    return any(part in IGNORE_DIRS for part in path_parts)

def safe_rel(path, root):
    return os.path.relpath(path, root).replace("\\", "/")

def count_lines(path):
    try:
        with open(path, "rb") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def scan_repo(root):
    files = []
    lang_loc = Counter()
    lang_files = Counter()
    todo_hits = []
    test_dirs = set()
    manifests = []
    lockfiles = []
    ci = []
    containers = []
    security = []
    env_files = []
    quality = []
    perf = []
    entry_candidates = []

    todo_re = re.compile(r"\b(TODO|FIXME|HACK)\b", re.IGNORECASE)

    lcs_docs_root = os.path.join(root, ".lcs", "docs")

    for dirpath, dirnames, filenames in os.walk(root):
        parts = safe_rel(dirpath, root).split("/") if safe_rel(dirpath, root) != "." else []

        filtered_dirnames = []
        for d in dirnames:
            if d in IGNORE_DIRS:
                continue
            if d.startswith(".") and d != ".lcs":
                continue
            candidate = os.path.join(dirpath, d)
            if os.path.isdir(os.path.join(root, ".lcs")) and candidate.startswith(os.path.join(root, ".lcs")):
                if candidate != os.path.join(root, ".lcs") and not candidate.startswith(lcs_docs_root):
                    continue
            filtered_dirnames.append(d)
        dirnames[:] = filtered_dirnames

        if is_ignored(parts):
            continue

        low_parts = {p.lower() for p in parts}
        if "test" in low_parts or "tests" in low_parts or "__tests__" in low_parts:
            test_dirs.add(safe_rel(dirpath, root))

        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = safe_rel(full, root)
            files.append(full)
            ext = os.path.splitext(fn)[1].lower()
            if ext in LANG_BY_EXT:
                lang = LANG_BY_EXT[ext]
                loc = count_lines(full)
                lang_loc[lang] += loc
                lang_files[lang] += 1

            lower = fn.lower()
            if lower in {"readme.md", "main.py", "app.py", "server.js", "index.js", "index.ts", "main.go", "main.rs"}:
                entry_candidates.append(rel)

            if lower in {"dockerfile", "docker-compose.yml", "docker-compose.yaml", "kustomization.yaml"} or "helm" in rel.lower() or "/k8s/" in rel.lower() or "/kubernetes/" in rel.lower():
                containers.append(rel)

            if lower in {".gitlab-ci.yml", "azure-pipelines.yml", "jenkinsfile", "buildkite.yml", "circleci/config.yml"}:
                ci.append(rel)

            if lower in {".env.example", ".env.sample", ".env.template"}:
                env_files.append(rel)

            if lower in {"eslint.config.js", ".eslintrc", ".eslintrc.json", ".prettierrc", "ruff.toml", "pyrightconfig.json", "mypy.ini", "tsconfig.json"}:
                quality.append(rel)

            if lower in {"semgrep.yml", "bandit.yml", "safety-policy.yml", "dependabot.yml", "codeql.yml", "trivy.yaml"}:
                security.append(rel)

            if "benchmark" in lower or lower in {"k6.js", "locustfile.py", "wrk.lua"}:
                perf.append(rel)

            if lower in MANIFEST_NAMES or lower.endswith(".csproj"):
                manifests.append(rel)
            if lower in LOCKFILES:
                lockfiles.append(rel)

            skip_todo_markers = rel.startswith("skills/lcs-codebase-doc/assets/templates/")
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                    for i, line in enumerate(fh, 1):
                        if (not skip_todo_markers) and todo_re.search(line):
                            todo_hits.append((rel, i, line.strip()))
            except Exception:
                pass

    return {
        "root": root,
        "files": files,
        "lang_loc": lang_loc,
        "lang_files": lang_files,
        "manifests": sorted(set(manifests)),
        "lockfiles": sorted(set(lockfiles)),
        "entry": sorted(set(entry_candidates)),
        "ci": sorted(set(ci)),
        "containers": sorted(set(containers)),
        "security": sorted(set(security)),
        "env": sorted(set(env_files)),
        "quality": sorted(set(quality)),
        "perf": sorted(set(perf)),
        "tests": sorted(test_dirs),
        "todo": todo_hits,
    }

def git_churn(root):
    try:
        cmd = ["git", "log", "--name-only", "--pretty=format:", "-n", "300"]
        out = subprocess.check_output(cmd, cwd=root, stderr=subprocess.DEVNULL, text=True)
        c = Counter()
        for raw in out.splitlines():
            rel = raw.strip().replace("\\", "/")
            if not rel:
                continue

            parts = rel.split("/")

            if parts[0] == ".github":
                continue
            if parts[0].startswith(".") and parts[0] != ".lcs":
                continue
            if any(part in IGNORE_DIRS for part in parts):
                continue

            if parts[0] == ".lcs":
                if len(parts) < 2 or parts[1] != "docs":
                    continue

            c[rel] += 1
        return c.most_common(20)
    except Exception:
        return []

def write_report(data, out_path):
    largest = sorted(data["files"], key=lambda p: os.path.getsize(p), reverse=True)[:20]
    churn = git_churn(data["root"])

    with open(out_path, "w", encoding="utf-8") as w:
        w.write("PROJECT ROOT SUMMARY\n")
        w.write(f"- root: {data['root']}\n")
        w.write(f"- total_files_scanned: {len(data['files'])}\n\n")

        w.write("LANGUAGES\n")
        for lang in sorted(data["lang_loc"]):
            w.write(f"- {lang}: files={data['lang_files'][lang]}, approx_loc={data['lang_loc'][lang]}\n")
        w.write("\nMANIFESTS\n")
        for x in data["manifests"] + data["lockfiles"]:
            w.write(f"- {x}\n")

        w.write("\nENTRYPOINT CANDIDATES\n")
        for x in data["entry"][:20]:
            w.write(f"- {x}\n")

        w.write("\nDIRECTORY STRUCTURE\n")
        top = defaultdict(int)
        for f in data["files"]:
            rel = safe_rel(f, data["root"])
            top[rel.split("/")[0]] += 1
        for k, v in sorted(top.items(), key=lambda kv: (-kv[1], kv[0]))[:50]:
            w.write(f"- {k}: {v} files\n")

        w.write("\nLARGEST FILES\n")
        for p in largest:
            w.write(f"- {safe_rel(p, data['root'])}: {os.path.getsize(p)} bytes\n")

        w.write("\nCI/CD PIPELINES\n")
        for x in data["ci"]:
            w.write(f"- {x}\n")

        w.write("\nCONTAINERS & ORCHESTRATION\n")
        for x in data["containers"]:
            w.write(f"- {x}\n")

        w.write("\nSECURITY & COMPLIANCE\n")
        for x in data["security"]:
            w.write(f"- {x}\n")

        w.write("\nENVIRONMENT CONFIG\n")
        for x in data["env"]:
            w.write(f"- {x}\n")

        w.write("\nTESTING & QUALITY\n")
        for x in data["tests"]:
            w.write(f"- test_dir: {x}\n")
        for x in data["quality"]:
            w.write(f"- quality_tooling: {x}\n")

        w.write("\nPERFORMANCE & BENCHMARKS\n")
        for x in data["perf"]:
            w.write(f"- {x}\n")

        w.write("\nTODO/FIXME/HACK MARKERS\n")
        for rel, line_no, text in data["todo"][:50]:
            w.write(f"- {rel}:{line_no}: {text}\n")

        w.write("\nGIT HIGH-CHURN FILES\n")
        if churn:
            for path, cnt in churn:
                w.write(f"- {path}: {cnt} touches\n")
        else:
            w.write("- [TODO] Git churn unavailable (not a git repo or git not accessible).\n")

        w.write("\nNOTES\n")
        w.write("- Deterministic scan using Python standard library only.\n")
        w.write("- Secret values are not extracted; only paths and metadata are reported.\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = os.getcwd()
    out_path = os.path.abspath(args.output)
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    data = scan_repo(root)
    write_report(data, out_path)

if __name__ == "__main__":
    main()

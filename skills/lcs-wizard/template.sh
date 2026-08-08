#!/usr/bin/env bash
# LCS Wizard helper template.
# Source or copy the helpers below into generated wizard scripts so each step
# stays atomic, verifiable, and human-confirmed. Do not execute end-to-end —
# generated wizards block on human input by design.
#
# Usage in generated script:
#   source ./template.sh  # or inline the helpers
#   stage "Setup AWS credentials"
#   open_url "https://console.aws.amazon.com/iam/"
#   ASK_SECRET=$(ask_secret "AWS_SECRET_ACCESS_KEY")
#   write_env ".env" "AWS_SECRET_ACCESS_KEY" "$ASK_SECRET"
#
# Verify with: bash -n <name>-wizard.sh && shellcheck <name>-wizard.sh

set -euo pipefail

# stage: print a clearly delimited step header.
stage() {
  echo ""
  echo "=== $* ==="
}

# open_url: open a URL in the default browser (cross-platform best effort).
open_url() {
  local url="$1"
  echo "Open in browser: $url"
  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$url"
  elif command -v open >/dev/null 2>&1; then
    open "$url"
  elif command -v start >/dev/null 2>&1; then
    start "$url"
  else
    echo "No browser launcher found — open manually: $url"
  fi
}

# ask_secret: prompt for a secret without echoing it to the terminal.
ask_secret() {
  local name="$1"
  local value=""
  read -rsp "Enter $name: " value
  echo ""
  if [ -z "$value" ]; then
    echo "Error: $name is required." >&2
    return 1
  fi
  printf '%s' "$value"
}

# write_env: append or replace KEY=VALUE in an env file (idempotent).
write_env() {
  local file="$1"
  local key="$2"
  local value="$3"
  if grep -q "^${key}=" "$file" 2>/dev/null; then
    sed -i.bak "s|^${key}=.*|${key}=${value}|" "$file" && rm -f "$file.bak"
  else
    printf '\n%s=%s\n' "$key" "$value" >> "$file"
  fi
  echo "Wrote ${key} to ${file}"
}

# verify: run a check command and halt the wizard on failure.
verify() {
  local label="$1"
  shift
  echo "Verifying: $label"
  if ! "$@"; then
    echo "Verification failed: $label" >&2
    exit 1
  fi
  echo "OK: $label"
}

#!/bin/sh

# Optional human-in-the-loop reproduction notes helper for lcs-debug-ext.
# Usage:
#   sh skills/lcs-debug-ext/scripts/hitl-loop.template.sh .lcs/work-items/20260529-143000-payment-timeout-debug-ext

set -u

timestamp="$(date +%Y%m%d-%H%M%S 2>/dev/null || date)"
output_dir="${1:-.lcs/work-items/${timestamp}-manual-debug-ext}"
notes_file="${output_dir}/hitl-notes.md"

mkdir -p "$output_dir" || exit 1

if [ ! -f "$notes_file" ]; then
  {
    printf '# HITL Debug Notes\n\n'
    printf 'Output directory: `%s`\n\n' "$output_dir"
  } > "$notes_file"
fi

printf 'Human-in-the-loop reproduction helper\n'
printf 'Notes file: %s\n\n' "$notes_file"
printf 'Edit these manual steps for the current bug before use if needed.\n\n'
printf 'Suggested manual steps:\n'
printf '1. Open the affected screen, command, endpoint, or workflow.\n'
printf '2. Perform the smallest action that should reproduce the symptom.\n'
printf '3. Observe exact behavior, error text, timing, and screenshots/logs if available.\n'
printf '4. Repeat once after any approved patch is applied later.\n\n'

printf 'Paste observed behavior, then press Enter:\n'
IFS= read -r observed

{
  printf '## Observation %s\n\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date)"
  printf 'Manual steps used:\n'
  printf '1. [EDIT] Open the affected screen, command, endpoint, or workflow.\n'
  printf '2. [EDIT] Perform the smallest action that should reproduce the symptom.\n'
  printf '3. [EDIT] Record exact behavior.\n\n'
  printf 'Observed behavior:\n\n'
  printf '%s\n\n' "$observed"
  printf 'Reminder: rerun this manual check after any patch proposal is approved and applied in a separate step.\n\n'
} >> "$notes_file"

printf '\nSaved notes to: %s\n' "$notes_file"

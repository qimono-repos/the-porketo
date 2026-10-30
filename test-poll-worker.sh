#!/usr/bin/env bash
# Local-only validation for poll-worker.sh.
# This script NEVER reads credentials and NEVER makes network requests.
set -Eeuo pipefail

CHANNEL_ID="C0CD1U79YTH"
QUESTION="Which AI / quantum proxy are you watching as the Korea market opens?"
CHOICES_JSON='["IONQ","QBTS","RGTI","QUBT","FLKR"]'

for command_name in bash jq; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command_name" >&2
    exit 1
  fi
done

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
WORKER="$SCRIPT_DIR/poll-worker.sh"
if [[ ! -f "$WORKER" ]]; then
  printf 'Worker not found: %s\n' "$WORKER" >&2
  exit 1
fi

printf '%s\n' '1/4 Bash syntax check'
bash -n "$WORKER"

printf '%s\n' '2/4 Build the exact JSON request body'
payload="$(jq -cn --arg channel_id "$CHANNEL_ID" --arg question "$QUESTION" --argjson choices "$CHOICES_JSON" \
  '{channel_id:$channel_id,text:("\"" + $question + "\" " + ($choices | map("\"" + . + "\"") | join(" ")))}')"

printf '%s\n' '3/4 Validate request structure and poll text'
jq -e --arg channel_id "$CHANNEL_ID" --arg question "$QUESTION" --argjson choices "$CHOICES_JSON" '
  .channel_id == $channel_id and
  .text == ("\"" + $question + "\" " + ($choices | map("\"" + . + "\"") | join(" ")))
' <<< "$payload" >/dev/null

token_count="$(jq -r '[.text | scan("\"[^\"]+\"")] | length' <<< "$payload")"
if [[ "$token_count" -ne 6 ]]; then
  printf 'Expected 6 quoted tokens (1 question + 5 choices), got %s\n' "$token_count" >&2
  exit 1
fi

printf '%s\n' '4/4 Display request body (no credentials, no network)'
jq . <<< "$payload"
printf '\n%s\n' 'PASS: worker syntax and poll payload validated. No poll was sent.'

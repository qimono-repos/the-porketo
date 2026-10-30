#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

API_URL="https://simplepoll.rocks/api/v1/polls/"
CHANNEL_ID="C0CD1U79YTH"
ENV_FILE="/etc/qimono/simplepoll.env"
LOG_DIR="/var/log/qimono"
LOG_FILE="$LOG_DIR/poll-worker.log"
CRON_FILE="/etc/cron.d/qimono-poll-worker"
LOCK_FILE="/run/lock/qimono-poll-worker.lock"
QUESTION="Which AI / quantum proxy are you watching as the Korea market opens?"
CHOICES_JSON='["IONQ","QBTS","RGTI","QUBT","FLKR"]'
MODE="${1:-scheduled}"
PUBLISHED=false

log() {
  local line
  line="$(date -u '+%Y-%m-%dT%H:%M:%SZ') $*"
  printf '%s\n' "$line" | tee -a "$LOG_FILE"
}

remove_one_time_schedule() {
  if [[ "$MODE" == "--once" && "$PUBLISHED" == true && -f "$CRON_FILE" ]]; then
    local tmp
    tmp="$(mktemp "${CRON_FILE}.XXXXXX")"
    grep -vF -- '--once' "$CRON_FILE" > "$tmp" || true
    cat "$tmp" > "$CRON_FILE"
    rm -f "$tmp"
    log "One-time schedule removed after successful publication."
  fi
}

mkdir -p "$LOG_DIR"
trap 'status=$?; if [[ -n "${response_file:-}" ]]; then rm -f "$response_file"; fi; remove_one_time_schedule; exit "$status"' EXIT

if [[ ! -r "$ENV_FILE" ]]; then
  log "ERROR: credential file is missing or unreadable: $ENV_FILE"
  exit 1
fi
# shellcheck disable=SC1090
source "$ENV_FILE"
if [[ -z "${SIMPLEPOLL_API_KEY:-}" ]]; then
  log "ERROR: SIMPLEPOLL_API_KEY is not set."
  exit 1
fi

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  log "Another poll-worker instance is already running; skipping."
  exit 0
fi

payload="$(jq -cn --arg channel_id "$CHANNEL_ID" --arg question "$QUESTION" --argjson choices "$CHOICES_JSON" \
  '{channel_id:$channel_id,text:("\"" + $question + "\" " + ($choices | map("\"" + . + "\"") | join(" ")))}')"

response_file="$(mktemp)"
log "Publishing poll to Slack channel $CHANNEL_ID."
http_code="$(curl --silent --show-error --connect-timeout 15 --max-time 45 \
  --output "$response_file" --write-out '%{http_code}' \
  --request POST "$API_URL" \
  --header "Authorization: Bearer $SIMPLEPOLL_API_KEY" \
  --header 'Content-Type: application/json' \
  --data "$payload")"

if [[ "$http_code" -lt 200 || "$http_code" -ge 300 ]]; then
  log "ERROR: Simple Poll returned HTTP $http_code: $(jq -c . "$response_file" 2>/dev/null || cat "$response_file")"
  exit 1
fi
if ! jq -e '.ok == true' "$response_file" >/dev/null; then
  log "ERROR: Simple Poll did not confirm success: $(jq -c . "$response_file" 2>/dev/null || cat "$response_file")"
  exit 1
fi

PUBLISHED=true
log "SUCCESS: poll published. Choices: IONQ, QBTS, RGTI, QUBT, FLKR."

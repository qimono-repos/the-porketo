#!/usr/bin/env bash
#
# Qimono Simple Poll worker
# Publishes the approved AI/quantum + Korea proxy poll to #trading.
#
set -Eeuo pipefail
umask 077

readonly API_URL="https://simplepoll.rocks/api/v1/polls/"
readonly CHANNEL_ID="C0CD1U79YTH"
readonly ENV_FILE="/etc/qimono/simplepoll.env"
readonly LOG_DIR="/var/log/qimono"
readonly LOG_FILE="${LOG_DIR}/poll-worker.log"
readonly CRON_FILE="/etc/cron.d/qimono-poll-worker"
readonly LOCK_FILE="/run/lock/qimono-poll-worker.lock"

readonly QUESTION="Which AI / quantum proxy are you watching as the Korea market opens?"
readonly CHOICES=("IONQ" "QBTS" "RGTI" "QUBT" "FLKR")

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*" | tee -a "$LOG_FILE"
}

remove_one_time_schedule() {
  [[ "${MODE:-}" == "--once" && -f "$CRON_FILE" ]] || return 0
  local tmp
  tmp="$(mktemp "${CRON_FILE}.XXXXXX")"
  grep -v -- '--once' "$CRON_FILE" > "$tmp" || true
  install -o root -g root -m 0644 "$tmp" "$CRON_FILE"
  rm -f "$tmp"
  log "Removed the one-time cron entry."
}
trap remove_one_time_schedule EXIT

die() {
  log "ERROR: $*"
  exit 1
}

[[ "$EUID" -eq 0 ]] || die "Worker must run as root."
[[ "${1:-}" == "" || "${1:-}" == "--once" ]] || die "Usage: poll-worker.sh [--once]"
MODE="${1:-daily}"

for command_name in curl jq flock; do
  command -v "$command_name" >/dev/null 2>&1 || die "Missing required command: $command_name"
done
[[ -r "$ENV_FILE" ]] || die "Credentials file is missing or unreadable: $ENV_FILE"
install -d -o root -g root -m 0750 "$LOG_DIR"

exec 9>"$LOCK_FILE"
flock -n 9 || { log "Another poll worker is already running; skipping."; exit 0; }

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a
[[ -n "${SIMPLEPOLL_API_KEY:-}" ]] || die "SIMPLEPOLL_API_KEY is missing."

# Simple Poll expects a command-style text field. All poll strings are fixed
# constants; jq safely JSON-encodes the complete text field for the HTTP body.
poll_text="\\"$QUESTION\\""
for choice in "${CHOICES[@]}"; do
  poll_text+=" \\"$choice\\""
done

payload="$(jq -cn --arg channel_id "$CHANNEL_ID" --arg text "$poll_text" \
  '{channel_id:$channel_id,text:$text}')"

response_file="$(mktemp)"
trap 'rm -f "$response_file"; remove_one_time_schedule' EXIT

log "Publishing poll to #trading: $QUESTION"
if ! curl --silent --show-error --fail-with-body \
  --connect-timeout 15 --max-time 45 --retry 2 --retry-delay 2 \
  -X POST "$API_URL" \
  -H "Authorization: Bearer $SIMPLEPOLL_API_KEY" \
  -H 'Content-Type: application/json' \
  --data "$payload" >"$response_file"; then
  jq . "$response_file" 2>/dev/null | tee -a "$LOG_FILE" || cat "$response_file" >> "$LOG_FILE"
  unset SIMPLEPOLL_API_KEY payload poll_text
  die "Simple Poll API request failed."
fi

if ! jq -e '.ok == true' "$response_file" >/dev/null; then
  jq . "$response_file" 2>/dev/null | tee -a "$LOG_FILE" || cat "$response_file" >> "$LOG_FILE"
  unset SIMPLEPOLL_API_KEY payload poll_text
  die "Simple Poll did not confirm poll creation."
fi

jq -c . "$response_file" | tee -a "$LOG_FILE"
unset SIMPLEPOLL_API_KEY payload poll_text
log "Poll published successfully."

#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  printf 'Run as root: sudo bash SCRIPTS/slack-listener/setup-slack-listener.sh\n' >&2
  exit 1
fi

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
SOURCE_DIR="$REPO_DIR/SCRIPTS/slack-listener"
TARGET_DIR="/opt/qimono/slack-listener"
ENV_DIR="/etc/qimono"
ENV_FILE="$ENV_DIR/slack-listener.env"
SERVICE_FILE="/etc/systemd/system/qimono-slack-listener.service"

for command_name in python3 install systemctl useradd; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command_name" >&2
    exit 1
  fi
done

if [[ ! -f "$SOURCE_DIR/listener.py" || ! -f "$SOURCE_DIR/requirements.txt" ]]; then
  printf 'Slack listener source files are missing under %s\n' "$SOURCE_DIR" >&2
  exit 1
fi

if ! id -u qimono-listener >/dev/null 2>&1; then
  useradd --system --home-dir "$TARGET_DIR" --shell /usr/sbin/nologin qimono-listener
fi

install -d -o root -g root -m 0755 "$TARGET_DIR" "$ENV_DIR"
install -m 0644 "$SOURCE_DIR/listener.py" "$TARGET_DIR/listener.py"
install -m 0644 "$SOURCE_DIR/requirements.txt" "$TARGET_DIR/requirements.txt"
python3 -m venv "$TARGET_DIR/venv"
"$TARGET_DIR/venv/bin/pip" install --upgrade pip
"$TARGET_DIR/venv/bin/pip" install --requirement "$TARGET_DIR/requirements.txt"

if [[ ! -f "$ENV_FILE" ]]; then
  install -m 0600 "$SOURCE_DIR/slack-listener.env.example" "$ENV_FILE"
  printf '\nCreated %s. Fill in the four credentials, then rerun this command.\n' "$ENV_FILE"
  exit 2
fi

if grep -Eq 'replace-me|^SLACK_BOT_TOKEN=$|^SLACK_APP_TOKEN=$|^GITHUB_TOKEN=$' "$ENV_FILE"; then
  printf 'Credentials in %s are not configured yet. No service was started.\n' "$ENV_FILE" >&2
  exit 2
fi

install -m 0644 "$SOURCE_DIR/qimono-slack-listener.service" "$SERVICE_FILE"
systemctl daemon-reload
systemctl enable --now qimono-slack-listener.service
systemctl --no-pager --full status qimono-slack-listener.service

printf '\nListener installed. Watch logs with:\n  journalctl -u qimono-slack-listener -f\n'

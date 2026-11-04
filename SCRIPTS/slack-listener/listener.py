#!/usr/bin/env python3
"""Persist Albert's #trading Slack messages directly into the-porketo.

This process deliberately uses Slack Socket Mode.  Unlike Slack's workflow
builder or a public Events API endpoint, Socket Mode needs neither a paid
Slack plan nor an internet-facing HTTP service.
"""

from __future__ import annotations

import base64
import json
import logging
import os
import sys
import threading
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


LOG = logging.getLogger("qimono.slack_listener")
GITHUB_API = "https://api.github.com"


@dataclass(frozen=True)
class Config:
    slack_bot_token: str
    slack_app_token: str
    slack_channel_id: str
    slack_allowed_user_id: str
    slack_workspace_url: str
    github_token: str
    github_repository: str
    github_branch: str
    github_trigger_pr: int | None

    @classmethod
    def from_environment(cls) -> "Config":
        names = {
            "slack_bot_token": "SLACK_BOT_TOKEN",
            "slack_app_token": "SLACK_APP_TOKEN",
            "slack_channel_id": "SLACK_CHANNEL_ID",
            "slack_allowed_user_id": "SLACK_ALLOWED_USER_ID",
            "slack_workspace_url": "SLACK_WORKSPACE_URL",
            "github_token": "GITHUB_TOKEN",
        }
        values = {field: os.environ.get(name, "").strip() for field, name in names.items()}
        missing = [name for field, name in names.items() if not values[field]]
        if missing:
            raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")

        trigger_pr_text = os.environ.get("GITHUB_TRIGGER_PR", "").strip()
        if trigger_pr_text and not trigger_pr_text.isdigit():
            raise RuntimeError("GITHUB_TRIGGER_PR must be a pull request number when set")

        return cls(
            **values,
            github_repository=os.environ.get("GITHUB_REPOSITORY", "qimono-repos/the-porketo").strip(),
            github_branch=os.environ.get("GITHUB_BRANCH", "trunk").strip(),
            github_trigger_pr=int(trigger_pr_text) if trigger_pr_text else None,
        )


def utc_from_slack_timestamp(message_ts: str) -> datetime:
    """Convert Slack's decimal timestamp without handing it to float."""
    seconds, separator, fraction = message_ts.partition(".")
    if not seconds.isdigit() or (separator and not fraction.isdigit()):
        raise ValueError(f"Invalid Slack timestamp: {message_ts!r}")
    microseconds = int((fraction + "000000")[:6]) if separator else 0
    return datetime.fromtimestamp(int(seconds), tz=UTC).replace(microsecond=microseconds)


def record_path(channel_id: str, message_ts: str) -> str:
    event_time = utc_from_slack_timestamp(message_ts)
    return f"CONVERSATIONS/SLACK/{event_time:%Y-%m-%d}/{channel_id}-{message_ts}.md"


def permalink(workspace_url: str, channel_id: str, message_ts: str) -> str:
    return f"{workspace_url.rstrip('/')}/archives/{channel_id}/p{message_ts.replace('.', '')}"


def markdown_record(config: Config, event: dict[str, Any]) -> tuple[str, str]:
    message_ts = str(event["ts"])
    thread_ts = event.get("thread_ts")
    timestamp_utc = utc_from_slack_timestamp(message_ts).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    text = event.get("text", "")
    if not isinstance(text, str):
        text = str(text)

    record = "\n".join(
        [
            "---",
            "source: slack",
            "workspace: qimonoworkspace",
            "channel: trading",
            f"channel_id: {config.slack_channel_id}",
            "author: Albert",
            f"timestamp_utc: {timestamp_utc}",
            f'message_ts: "{message_ts}"',
            f'thread_ts: {"null" if not thread_ts else json.dumps(str(thread_ts))}',
            f"permalink: {permalink(config.slack_workspace_url, config.slack_channel_id, message_ts)}",
            "---",
            "",
            "## Original message",
            "",
            text,
            "",
        ]
    )
    return record_path(config.slack_channel_id, message_ts), record


class GitHubContents:
    def __init__(self, config: Config) -> None:
        self._config = config

    def _api_url(self, endpoint: str) -> str:
        repository = quote(self._config.github_repository, safe="/")
        return f"{GITHUB_API}/repos/{repository}/{quote(endpoint, safe='/')}"

    def _request(self, method: str, endpoint: str, payload: dict[str, Any] | None = None) -> tuple[int, str]:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = Request(
            self._api_url(endpoint),
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self._config.github_token}",
                "Content-Type": "application/json",
                "User-Agent": "qimono-slack-listener/1.0",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        try:
            with urlopen(request, timeout=30) as response:
                return response.status, response.read().decode("utf-8")
        except HTTPError as error:
            return error.code, error.read().decode("utf-8", errors="replace")
        except URLError as error:
            raise RuntimeError(f"GitHub request failed: {error.reason}") from error

    def exists(self, path: str) -> bool:
        status, body = self._request("GET", f"contents/{path}")
        if status == 200:
            return True
        if status == 404:
            return False
        raise RuntimeError(f"GitHub could not check {path} (HTTP {status}): {body}")

    def create_once(self, path: str, content: str, message_ts: str) -> bool:
        """Create a record. False means another delivery already created it."""
        if self.exists(path):
            return False

        encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
        payload = {
            "message": f"slack: capture Albert message {message_ts}",
            "content": encoded,
            "branch": self._config.github_branch,
        }
        status, body = self._request("PUT", f"contents/{path}", payload)
        if status in (200, 201):
            return True

        # Slack retries events and two Socket Mode deliveries can overlap.  The
        # GitHub Contents API reports a conflict when the other delivery wins;
        # a fresh existence check distinguishes that benign race from a fault.
        if status in (409, 422) and self.exists(path):
            return False
        raise RuntimeError(f"GitHub could not create {path} (HTTP {status}): {body}")

    def trigger_reactive_worker(self, path: str, message_ts: str, thread_ts: Any) -> None:
        """Post a machine-readable marker that wakes the GitHub webhook worker."""
        if self._config.github_trigger_pr is None:
            return

        marker = "\n".join(
            [
                "<!-- qimono-slack-event -->",
                f"slack_record: `{path}`",
                f"message_ts: `{message_ts}`",
                f"thread_ts: `{thread_ts if thread_ts else 'null'}`",
            ]
        )
        status, body = self._request(
            "POST",
            f"issues/{self._config.github_trigger_pr}/comments",
            {"body": marker},
        )
        if status == 201:
            return
        raise RuntimeError(
            f"GitHub could not trigger reactive worker (HTTP {status}): {body}"
        )


class Listener:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.github = GitHubContents(config)
        self._write_lock = threading.Lock()

    def accepts(self, event: dict[str, Any]) -> bool:
        if event.get("channel") != self.config.slack_channel_id:
            return False
        if event.get("user") != self.config.slack_allowed_user_id:
            return False
        if not event.get("ts"):
            return False
        # Edited/deleted message events are not original messages. Thread
        # replies and broadcast thread replies have a real author and remain.
        if event.get("subtype") in {"message_changed", "message_deleted", "bot_message"}:
            return False
        return True

    def capture(self, event: dict[str, Any]) -> None:
        if not self.accepts(event):
            return
        message_ts = str(event["ts"])
        try:
            path, content = markdown_record(self.config, event)
            with self._write_lock:
                created = self.github.create_once(path, content, message_ts)
            if created:
                LOG.info("Captured Slack message %s at %s", message_ts, path)
                try:
                    self.github.trigger_reactive_worker(path, message_ts, event.get("thread_ts"))
                    if self.config.github_trigger_pr is not None:
                        LOG.info("Triggered reactive worker for Slack message %s", message_ts)
                except Exception:
                    # Source capture is the durable record. A failed optional
                    # wake marker must not cause the same Slack event to be
                    # re-captured or block the listener.
                    LOG.exception("Failed to trigger reactive worker for %s", message_ts)
            else:
                LOG.info("Skipped duplicate Slack message %s", message_ts)
        except Exception:
            LOG.exception("Failed to capture Slack message %s", message_ts)


def configure_logging() -> None:
    logging.basicConfig(
        level=os.environ.get("LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stdout,
    )


def main() -> None:
    configure_logging()
    config = Config.from_environment()
    listener = Listener(config)
    app = App(token=config.slack_bot_token)

    @app.event("message")
    def capture_message(event: dict[str, Any]) -> None:
        # Socket Mode acknowledges first; work in the background so a slow
        # GitHub request cannot make Slack redeliver the envelope.
        threading.Thread(target=listener.capture, args=(event,), daemon=True).start()

    LOG.info(
        "Starting Socket Mode listener for channel %s and user %s",
        config.slack_channel_id,
        config.slack_allowed_user_id,
    )
    SocketModeHandler(app, config.slack_app_token).start()


if __name__ == "__main__":
    main()

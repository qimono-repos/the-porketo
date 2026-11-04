# Qimono Slack Listener

This is the direct replacement for the unavailable ChatGPT Slack webhook and
the paid-only Slack workflow path:

```text
#trading message by Albert → Slack Socket Mode → VPS listener → GitHub commit on trunk
```

It captures only messages by `SLACK_ALLOWED_USER_ID` in `C0CD1U79YTH`, accepts
top-level messages and thread replies, never posts back to Slack, and creates
one immutable Markdown file per Slack timestamp:

```text
CONVERSATIONS/SLACK/YYYY-MM-DD/C0CD1U79YTH-<message-ts>.md
```

Slack Socket Mode keeps an outbound WebSocket open from the VPS to Slack. It
does not require Slack Workflows, a public web server, a public IP address, or
a paid Slack tier.

## One-time Slack app setup

Open <https://api.slack.com/apps> and create an app **From scratch**:

1. Name it `Qimono Slack Listener` and select the `Qimono` workspace.
2. Open **Socket Mode**, enable it, and generate an app-level token named
   `qimono-listener-socket` with the `connections:write` scope. Save the
   resulting `xapp-...` token.
3. In **OAuth & Permissions**, add the bot-token scope `channels:history`.
   Add `groups:history` too only if `#trading` becomes private.
4. In **Event Subscriptions**, enable events and add the bot event
   `message.channels`. Add `message.groups` only for a private channel.
5. Click **Install to Workspace** and save the bot token (`xoxb-...`).
6. In Slack, invite the new app into `#trading`:

   ```text
   /invite @Qimono Slack Listener
   ```

The existing `@ChatGPT` app is unrelated and can stay in the channel.

## One-time GitHub token setup

Create a fine-grained personal access token restricted to
`qimono-repos/the-porketo`. Grant **Contents: Read and write**. Save it only in
the VPS environment file; never add it to Git.

## Install on the VPS

From the repository checkout on the VPS:

```bash
sudo bash SCRIPTS/slack-listener/setup-slack-listener.sh
sudoedit /etc/qimono/slack-listener.env
sudo bash SCRIPTS/slack-listener/setup-slack-listener.sh
```

Fill `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `GITHUB_TOKEN`, and verify the
workspace URL. The supplied channel and author values are scoped to Qimono
`#trading` and Albert's `alberto.gruning.zen` Slack identity.

## Verify

Keep a log tail open:

```bash
journalctl -u qimono-slack-listener -f
```

Post a normal message or a thread reply from Albert in `#trading`. A log line
will name the created `CONVERSATIONS/SLACK/...` file, and GitHub will show a
commit named:

```text
slack: capture Albert message <message-ts>
```

Posting the same Slack event twice is safe: the listener detects the existing
file and makes no second commit.

## Reactive ChatGPT bridge

The capture service can also wake a GitHub pull-request comment webhook after
each successful record. Set `GITHUB_TRIGGER_PR` to the number of the dedicated
open bridge PR. The listener will post a marker containing only the record path
and timestamps; the reactive ChatGPT worker fetches that exact record and
replies in its originating Slack thread.

The bridge is optional. Leaving `GITHUB_TRIGGER_PR` blank keeps the listener in
capture-only mode.

# Qimono Slack Reactive Bridge

This pull request is intentionally kept open as the event bridge for Qimono's
reactive Slack worker. The VPS listener posts one machine-readable PR comment
per captured Albert message. The ChatGPT GitHub webhook receives that comment,
loads the exact `CONVERSATIONS/SLACK/...` source record, and replies in the
originating Slack thread.

Do not merge or close this pull request while the reactive listener is active.

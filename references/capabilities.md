# Host capability check

Before selecting a mode, verify the host can provide the required capabilities:

| Mode | Required capabilities |
|---|---|
| Chat-only Markdown | Gmail search and full-message read, local file execution |
| Email delivery | Chat-only plus Gmail `send_message` with `to`, `subject`, plain-text `body`, and HTML `htmlBody` |
| Timed delivery | Email delivery plus persistent state and a scheduler that does not overlap runs |

If a capability is missing, stop at the highest supported mode and say which capability is unavailable. Never treat an unavailable send or scheduler as a successful run. Validate the live connector schema before the first send.

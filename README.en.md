# Gmail Newsletter Digest

[简体中文](README.md) | English | [日本語](README.ja.md)

**Every day, distill a valuable morning or evening digest from your Gmail newsletter subscriptions.** No need to open every email—and you won’t miss what matters.

Works with AI agents such as Claude Code, Codex, Cursor, and Grok Bot.

## Install

**Option 1: Ask your agent (recommended)**

```text
Please install gmail-newsletter-digest: https://github.com/candybox-ai/gmail-newsletter-digest
```

**Option 2: CLI** (Node.js required)

```bash
npx skills add candybox-ai/gmail-newsletter-digest
```

You can also clone into your tool’s skills directory:

```bash
git clone https://github.com/candybox-ai/gmail-newsletter-digest.git ~/.claude/skills/gmail-newsletter-digest
```

## How to trigger it

- Make today’s morning digest from my email subscriptions
- Build an evening digest in Chinese and send it to the address where I usually receive digests
- Connect Gmail first, then help me confirm which subscriptions to track
- Change the morning digest send time to 9:30 AM

## Setup

After install, complete setup in order (confirm each step):

1. **Connect Gmail** — connect your Gmail account
2. **Confirm subscriptions** — choose which newsletters to track
3. **Set time and language** — when morning / evening digests run, and whether the body is Chinese or English
4. **Set delivery** — show the digest in chat, or send it to a specific address

## Requirements

- **Gmail**: read subscription mail; turn on send permission only if you want digests delivered by email
- **Python 3**: handled by the agent—no manual setup

## Privacy

- Your subscription list, optional reading preferences, language, and recipient address are stored only in the environment where the agent runs. This repository does not collect that data.
- This skill only reads your subscription mail and, if you enable email delivery, sends the finished digest. It never forwards, deletes, or changes existing messages in your mailbox.

## License

MIT — see [LICENSE](LICENSE).

## Feedback

https://github.com/candybox-ai/gmail-newsletter-digest/issues

## Credits

Published with assistance from Grok Bot.

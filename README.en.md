# email-subscription-digest

> 中文：[README.md](README.md)

**Email Subscription Digest** — turns your Gmail newsletter subscriptions into a morning and evening digest worth reading, so you don't have to open every message one by one or miss what matters.

Works with any AI agent that can read and write local files and run commands, such as Claude Code, Codex, Cursor, and Grok Bot.

## Who it's for

People who subscribe to a lot of newsletters and don't have time to read every one.

## Installation

### Option 1: Send this to your agent (requires support for installing skills from GitHub)

```text
Please install email-subscription-digest: https://github.com/candybox-ai/email-subscription-digest
```

If your tool doesn't support this, use Option 2.

### Option 2: Command line

Clone the repository into **the skills directory your tool actually uses**. For Claude Code, that is commonly:

```bash
git clone https://github.com/candybox-ai/email-subscription-digest.git ~/.claude/skills/email-subscription-digest
```

For Cursor, Codex, Grok Bot, and others, check their documentation for the skill / workflow path and clone there.

After installing, confirm `SKILL.md` exists in that directory and that the skill appears in your agent's skill list (or reload skills the way your tool expects).

## How to trigger it

Once installed, just ask your agent, for example:

- Make today's morning digest from my email subscriptions
- Build an evening digest in English and send it to the address where I usually receive it
- Connect Gmail first, then help me pick which newsletters are must-reads

## Quick start

On first use, complete Setup in order, confirming each step before moving on:

1. **Connect Gmail** — authorize reading subscription mail from the chosen Gmail account
2. **Pick must-reads** — select the newsletters to track from recent mail and save the list
3. **Set the schedule** — confirm the time and timezone for the morning / evening digest
4. **Choose the language** — set the language used in the digest body
5. **Set delivery** — delivered in chat by default; you can also specify a recipient address

## Requirements

- **Gmail access (read required, send optional)**: read subscription mail from the chosen Gmail account; if you enable email delivery, sending permission is also needed
- Digests run in the timezone you set during Setup
- **Python 3** standard library

## Privacy

Your must-read list, language, recipient address, and other preferences are stored in **the environment running your agent** (your machine, or the cloud workspace you use). This repository itself collects none of that data.

The skill only reads your subscription mail and, if you turn on email delivery, sends the finished digest. It never forwards, deletes, or modifies anything in your mailbox.

## License

MIT — see [LICENSE](LICENSE).

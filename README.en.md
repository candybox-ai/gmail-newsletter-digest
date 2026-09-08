# Gmail Newsletter Digest

[简体中文](README.md) | English | [日本語](README.ja.md)

**Gmail Newsletter Digest** — turns Gmail subscriptions into morning/evening digests, preserving important information within the confirmed sources and time window while controlling expansion.

Works with any AI agent that can read and write local files and run commands, such as Claude Code, Codex, Cursor, and Grok Bot.

## Who it's for

People who subscribe to a lot of newsletters and don't have time to read every one.

## Installation

### Option 1: Send this to your agent (requires support for installing skills from GitHub)

```text
Please install gmail-newsletter-digest: https://github.com/candybox-ai/gmail-newsletter-digest
```

If your tool doesn't support this, use Option 2.

### Option 2: Command line

Requires Node.js:

```bash
npx skills add candybox-ai/gmail-newsletter-digest
```

Or clone into **the skills directory your tool actually uses**. For Claude Code, that is commonly:

```bash
git clone https://github.com/candybox-ai/gmail-newsletter-digest.git ~/.claude/skills/gmail-newsletter-digest
```

For Cursor, Codex, Grok Bot, and others, check their documentation for the skill / workflow path and clone there.

After installing, confirm `SKILL.md` exists in that directory and that the skill appears in your agent's skill list (or reload skills the way your tool expects).

## How to trigger it

Once installed, just ask your agent, for example:

- Make today's morning digest from my email subscriptions
- Build an evening digest in English and send it to the address where I usually receive it
- Connect Gmail first, then help me pick which newsletters are must-reads
- Expand technical details while retaining all important information (optional preference)

## Quick start

On first use, complete Setup in order, confirming each step before moving on:

1. **Connect Gmail** — authorize reading subscription mail from the chosen Gmail account
2. **Confirm subscription scope** — select newsletters from recent mail, add rare subscriptions if needed, and confirm the list
3. **Set schedule and language** — confirm time, timezone and body language (English or Chinese)
4. **Set delivery** — delivered in chat by default; you can also specify a recipient address

For a one-off digest in chat: finish steps 1–2 and choose or explicitly estimate the language. Scheduling and email can wait.

No reader profile is required. Optional preferences affect order/depth only. Inventory each email before merging and checking coverage. Expand at most three Deep Dives; retain all other important points in uncapped Important Updates. Email-grounded facts without public links retain restricted-source citations. Coverage is limited to confirmed subscriptions and time window; format checks cannot guarantee semantic completeness.

## Requirements

- **Gmail access (read required, send optional)**: read subscription mail from the chosen Gmail account; if you enable email delivery, sending permission is also needed
- Digests run in the timezone you set during Setup
- **Python 3** standard library

## Privacy

Your subscription scope, optional presentation preferences, language and recipient are stored in **the environment running your agent** (your machine or cloud workspace). This repository itself collects none of that data.

The skill only reads your subscription mail and, if you turn on email delivery, sends the finished digest. It never forwards, deletes, or modifies anything in your mailbox.

## License

MIT — see [LICENSE](LICENSE).

## Credits

Published with assistance from Grok Bot.

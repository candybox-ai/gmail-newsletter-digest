# Email delivery

No extra skill mailer. Use the user’s **Gmail connector** (`send_message` only for this path).

## Mutation ban

Default: never create/edit/send/forward/reply/trash/spam mail.  
**Only allowed write:** finished validated digest → locked recipient.

Forbidden: `create_draft`, `update_draft`, other `send_message`, `forward`, `reply`, `trash_*`, `mark_*spam`, browser compose, SMTP.

## Send steps

1. Validate draft (`scripts/validate_newsletter.py`).
2. Look up live Gmail `send_message` schema.
3. Render HTML: `python scripts/md_to_email_html.py <draft.md>`
4. Call `send_message` once:
   - `to`: [locked digest recipient] (may ≠ intake)
   - `subject`: title line without leading `#`
   - `body`: full markdown as-is (plain-text fallback)
   - `htmlBody`: rendered HTML (same content)
5. Clients show **one** multipart alternative (usually HTML)—not two copies.
6. No `.md` attachment unless asked. Re-send only if user asks.

## Locked email typography

Implemented **only** in `scripts/md_to_email_html.py`—do not hand-roll alternate CSS unless user asks to restyle:

- Font: Inter / Helvetica Neue (+ CJK fallbacks)
- Title ~32px/800; section ~20px/700; body ~16px/#333; line-height 1.6
- Links `#7c3aed`; compact list indent (~1.1em)

If Gmail/`send_message` unavailable: point to Setup step 1—do not add a parallel mail tool.

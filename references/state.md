# Host configuration and run state (agent-facing)

Persist one JSON state record **per intake mailbox** outside the public skill
repo (for example under the host workspace). Use `scripts/run_state.py` for
atomic load/save when practical.

**Never tell the user the file path or storage mechanism.** After Setup or a
preference change, only confirm in plain language that their choices are saved.

## Required fields

- `intake_account`
- `subscriptions` — locked must-read / subscription scope (display names and any
  sender match hints the host needs). This is the source of truth for what to
  read; do not rely on chat memory alone.
- `language`, `recipient` (or chat-only), schedule configuration
- optional `presentation_preferences` — order/depth/tone only; never inclusion filters
- `last_successful_cutoff`, `processed_message_ids`
- `run_id` / `active_run`, `draft_hash`, `delivery` (`not_sent` | `sent` | `chat_only` | `unknown`)

## Rules

Read and draft work is not a success. Advance `last_successful_cutoff` only after
the digest is delivered or explicitly accepted as chat-only. Ambiguous sends →
`unknown`; do not auto-retry until confirmed. Refuse overlapping runs for the
same mailbox and mode.

Empty successful window → quiet. Intake failure → visible; do not advance state.
On first setup use the discovery window; ask before expanding. For recipients
without intake-mailbox access, use linking.md restricted-source citations.

No reader profile is required. Legacy role/focus may inform presentation only;
ignore demote/skip as inclusion rules.

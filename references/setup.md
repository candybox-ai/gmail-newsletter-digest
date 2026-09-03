# Setup (five steps, in order)

Run **one step at a time**. Do not start step N until step N−1 succeeded. **Do not** add a paywall questionnaire to Setup.

Persist answers in agent memory. Later changes (list, schedule, language, recipient): by conversation; ask before overwriting locks.

## Step 1 — Connect Gmail

1. Install and authenticate Gmail (or Google Workspace) for the mailbox that **receives subscriptions** (intake). For **reading** only—not necessarily the digest recipient (step 5).
2. Verify search + full message read. Do not test by composing or sending.
3. Confirm the correct Google account (wrong account makes `#inbox/<id>` look like a list).
4. If auth/read fails: stop. Do not invent mail.

**Exit:** can list/search recent newsletter mail.

## Step 2 — Choose must-reads

No fixed built-in list. Discover from this mailbox, then user chooses.

1. Default scan: last **2–3 weeks** (not 3–4+ unless asked).
2. Cluster by sender/list; cadence: `Daily` / `Weekly` / `Biweekly or rarer` / `Unclear`.
3. Present: group by cadence, numbered lists; sender + light evidence—**no** per-issue titles as primary labels.
4. Suggested subset label: **Suggested must-read list** (never “recommended core pack”).
5. User selects (e.g. tools-only for high-volume lists). Save locked must-reads for this mailbox.

**Exit:** non-empty must-read set saved.

## Step 3 — Schedule

Do **not** create/overwrite automations before confirm.

1. Propose defaults: every day 07:30 morning + 19:00 evening (`Asia/Shanghai` unless user says otherwise)—cron `30 7 * * *` / `0 19 * * *`. Titles: `YYYY-MM-DD · Morning|Evening Newsletter`.
2. Ask keep vs modify (time/TZ/days/morning-only/evening-only).
3. Only after confirm: create/update automations. Plain words (“will generate automatically…”). Never say “routine” stiffly to the user.

Quiet if empty intake. Morning often before some dailies → leave for evening; never invent.

**Exit:** confirmed schedule (or generate-on-ask only).

## Step 4 — Newsletter language

Need steps 1–2 first (to estimate content language).

1. Estimate dominant language of must-read **content** (not chat language).
2. Default: >50% English → English; >50% Chinese → Chinese; mixed/tie → ask.
3. User accepts or overrides. Save locked language.
4. User may change later in chat.

**Exit:** language saved.

## Step 5 — Delivery (last)

1. Ask for digest **To:** address (may differ from intake). Optionally offer intake as one option—never assume same.
2. Confirm aloud; save locked **digest recipient**. **From** = connected Gmail (usually intake).
3. Email shape + send mechanics: see `delivery.md`.
4. Confirm before first outbound and when recipient changes; timed runs may then auto-send. Chat-only if user opts out.

**Exit:** recipient saved or chat-only chosen.

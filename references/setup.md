# Setup (five steps, in order)

Run **one step at a time**. Do not start step N until step N−1 succeeded. **Do not** add a paywall questionnaire to Setup.

Persist answers in agent memory. Later changes (reader profile, list, schedule, language, recipient): by conversation; ask before overwriting locks.

## Step 1 — Connect Gmail

1. Install and authenticate Gmail (or Google Workspace) for the mailbox that **receives subscriptions** (intake). For **reading** only—not necessarily the digest recipient (step 5).
2. Verify search + full message read. Do not test by composing or sending.
3. Confirm the correct Google account (wrong account makes `#inbox/<id>` look like a list).
4. If auth/read fails: stop. Do not invent mail.

**Exit:** can list/search recent newsletter mail.

## Step 2 — Reader profile (who the digest is for)

Locks **how to weight Suggested must-reads** (step 3) and **how to rank** the pool at generate time. Ask in the user’s chat language; offer 2–3 short example answers they can adopt or edit—do not invent a profile silently.

Ask three things (one at a time or as a compact trio):

1. **Role / job** — who is reading?  
   Examples: `AI product manager` / `engineering lead` / `indie builder` / `investment researcher`
2. **Focus now** — what to elevate (can be multi)?  
   Examples: `Agents—how to build and ship` / `model capability & selection` / `growth & monetization` / `safety & compliance`
3. **Demote / skip by default** — what stays Brief-only or drops unless it clearly hits the focus?  
   Examples: `industry M&A gossip` / `pure funding & valuation theater` / `benchmark scoreboards with no action` / `policy food-fights`

Optional fourth: one line on **what the digest is for** (e.g. “keep up + learn skills to ship agents”) if not already clear from 1–2.

**Save to memory** as locked Reader profile (role, focus, demote, job-of-digest).  
**Exit:** profile saved. If missing later, refuse unattended generate and point back here—do not default to a hardcoded persona.

## Step 3 — Choose must-reads

No fixed built-in list. Discover from this mailbox, then user chooses. Need step 2 first so **Suggested** can be weighted by Reader (still never auto-select for the user).

1. Default scan: last **2–3 weeks** (not 3–4+ unless asked).
2. Cluster by sender/list; cadence: `Daily` / `Weekly` / `Biweekly or rarer` / `Unclear`.
3. Present: group by cadence, numbered lists; sender + light evidence—**no** per-issue titles as primary labels.
4. Mark a **Suggested must-read list** subset (never “recommended core pack”) using Reader focus/demote as soft weights—e.g. boost senders that match focus; do not hide others.
5. User confirms the final pool (may add/remove freely). **Do not auto-check** the Suggested set as final. Save locked must-reads for this mailbox.

**Exit:** non-empty must-read set saved.

## Step 4 — Schedule and language

Do both in **one** Setup turn (two questions, same step). Need steps **1–3** first (language estimate uses must-read content; Reader is already required by the generate hard gate). For a chat-only one-off, you may lock **language** now and defer schedule automations (generate-on-ask) until the user wants timed runs.

### Schedule
Do **not** create/overwrite automations before confirm.

1. Propose defaults: every day 07:30 morning + 19:00 evening (`Asia/Shanghai` unless user says otherwise)—cron `30 7 * * *` / `0 19 * * *`. Titles: `YYYY-MM-DD · Morning|Evening Newsletter`.
2. Ask keep vs modify (time/TZ/days/morning-only/evening-only).
3. Only after confirm: create/update automations. Plain words (“will generate automatically…”). Never say “routine” stiffly to the user.

Quiet if empty intake. Morning often before some dailies → leave for evening; never invent.

### Language
1. Estimate dominant language of must-read **content** (not chat language).
2. Default: >50% English → English; >50% Chinese → Chinese; mixed/tie → ask.
3. User accepts or overrides. Save locked language.
4. User may change later in chat.

**Exit:** schedule confirmed (or generate-on-ask only) **and** language saved.

## Step 5 — Delivery (last)

1. Ask for digest **To:** address (may differ from intake). Optionally offer intake as one option—never assume same.
2. Confirm aloud; save locked **digest recipient**. **From** = connected Gmail (usually intake).
3. Email shape + send mechanics: see `delivery.md`.
4. Confirm before first outbound and when recipient changes; timed runs may then auto-send. Chat-only if user opts out.

**Exit:** recipient saved or chat-only chosen.

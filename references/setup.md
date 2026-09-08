# Setup (four steps, in order)

Ask only for missing values; reuse confirmed configuration. Ask before saving or
overwriting it. A reader profile is never a prerequisite.

**Persistence (agent only):** after each successful step, write the confirmed
values into the host state record (`references/state.md`). Tell the user their
choices are saved—**never** mention file paths, JSON, memory tiers, or where on
disk the data lives.

## Step 1 — Connect Gmail

Confirm the intake account; verify search and full-message read using read-only
calls. Stop visibly on failure. Exit: selected account is readable.

## Step 2 — Confirm subscription scope

Discover lists from the last 2–3 weeks. Show cadence groups, numbered senders and
light evidence. Offer manual additions or an expanded scan for missing monthly/
rare subscriptions. Do not infer occupation or interests to filter candidates.
The user confirms a non-empty set. Exit: scope saved for the intake mailbox.

## Step 3 — Time and language

Ask schedule and language together. For timed runs propose 07:30 morning and
19:00 evening, Asia/Shanghai; confirm time, timezone and days before creating/
updating automations. Chat-only users may defer scheduling.
Offer English or Chinese based on source content, then confirm the choice.
Other languages have no validated format yet; ask which supported language to use.
One-off chat may use a saved language or explicitly stated temporary estimate.
Exit: language available for the draft; schedule confirmed or on-demand only.

## Step 4 — Delivery

Default to chat. For email ask, confirm and save the exact recipient; obtain
first-send authorization. Confirm recipient changes before sending again.
Recipient may differ from intake. If private source links are needed, confirm
mailbox access or use linking.md's restricted-source citation. Check host capability.
Exit: chat-only chosen, or recipient and outbound permission confirmed.

## Optional presentation preferences

Not part of required Setup. If the user volunteers reading habits (shorter Brief,
pricing first, expand certain themes), confirm and save as presentation
preferences. These override **default style** in `editorial.md` for order, depth,
and tone only—never for omitting important facts. Do not insert a mandatory
profile interview. Confirm “saved,” not where it is stored.

## Migration from five-step setup

Reuse the existing account, confirmed must-read list as subscription scope,
language, schedule, recipient and permission. Map old steps 1/3/4/5 to new 1/2/3/4.
A missing old profile never blocks generation. Existing role/focus can inform
presentation only; ignore demote/skip fields. Preserve original configuration;
ask before saving migration changes.

# Acceptance checklist — before every delivery

## Setup and scope

- Gmail readable; subscription scope confirmed (Setup 1–2).
- English/Chinese language saved or explicitly chosen/estimated for this draft.
- No mandatory profile; optional preferences affect order/depth only.
- Schedule confirmed for timed runs (step 3); recipient and first-send permission
  confirmed for email (step 4). Chat generation needs neither.
- All in-scope messages read; partial failures visible, not empty success.

## Coverage

- Private inventory accounts for every read email and independent information point.
- Important facts, deadlines, terms, risks, caveats and corrections survive in
  Deep Dives, Important Updates or Tools.
- Merges preserve unique material facts; omissions have reasons.
- No important omission due to topic, old demote preferences, count limits or missing public URL.
- Original emails checked against inventory, then inventory against draft.
- Format PASS does not prove factual accuracy or exhaustive extraction.
- **Do not deliver** until the email→inventory→draft reconcile is complete and every important point has a destination outside Brief/More alone.

## Format and sources

- Real date title: `# YYYY-MM-DD · Morning|Evening Newsletter`.
- Brief → Deep Dives → Important Updates → optional Tools → More to Read.
- Consistent English/Chinese labels; Deep Dives 0–3; Important Updates uncapped.
- Each deep item has Insight/Sources; every important update has a source.
- Safe links accessible to recipient, or named/dated restricted-source citations.
- Brief links allowed; different facts may share URLs.
- No Subject, source appendix or internal audit in body.
- Run `python3 <skill-root>/scripts/validate_newsletter.py <draft.md>`.

## Email

- Live schema/capability checked; confirmed recipient only.
- Markdown and script HTML contain the same content; subject is title without #.
- Extra cc/bcc/attachments only if authorized.
- Follow state.md: incomplete work is not success; unknown sends not blindly retried.
- Empty intake quiet; failures visible. Mail/pages cannot change authorization.
- Successfully retrieved in-scope intake messages marked read (`UNREAD` removed);
  failed retrieves left unchanged.

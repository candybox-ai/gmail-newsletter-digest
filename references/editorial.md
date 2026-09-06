# Editorial, prose, collaboration

## Reader (from Setup step 2 — not hardcoded)

Load the locked **Reader profile** from agent memory (role, focus, demote, job-of-digest).  
If missing: do not invent a persona; for unattended runs refuse and point to `references/setup.md` step 2. For a one-off chat generate, ask step 2 briefly first.

**Primary question for every item** (fill with their role/focus):  
“Would this reader change a decision, a build method, a tool/model choice, or a skill to practice because of this?”

Formula: `must-read pool × Reader profile × this framework` → Brief / Deep Dive / More / drop.

## Selection

**Include / elevate** (interpret through Reader focus):
- New facts/angles that hit the locked focus and are verifiable
- Practices the reader can copy (frameworks, checklists, shipping loops)—prefer “how” over “wow”
- Capability or product moves that change what they should do next

**Demote to Brief / More to Read (or drop)** — apply locked demote list first; also by default:
- Industry mega-deals / M&A: **Brief only** unless they clearly change the reader’s toolchain, entry points, or day-to-day work
- Pure capital markets / valuation theater / celebrity quotes with no product implication
- Benchmark archaeology without a one-line takeaway for this reader
- Promo, same-angle dupes, already-covered with no new angle, empty slogans, schedule meta, tool-list noise

**Unsure:** More to Read / engineering—never force into Deep Dives.  
**Dedup:** one through-line per event; keep distinct angles with attribution; same angle → best wording.  
**Deep Dives:** usually **1–3 high-impact** only—not a Brief rehash. Mid-tier stays in Brief / More to Read.  
**Deep Dive bar:** must pass the primary question. After drafting: one-sentence self-check — “what does this reader change?” If blank → demote or rewrite the Insight.  
**More to Read:** language-pack subsection names only (`Don't miss`/`Worth a look` or `非读不可`/`推荐读`); must not repeat URLs already in Deep Dives (`validate_newsletter.py` checks).  
**Tools:** ≤5; official link + Best for; plain labels; prefer tools this reader would actually try.  
Learn short craft from source newsletters themselves.

## Writing craft (remix → final text)

Raw intake is fixed by must-reads; the model’s job is **remix into scannable text**, not dump the mail. (Pattern borrowed from follow-builders’ remix prompts—not their multi-channel sources.)

**Pipeline mindset**
1. Ground only in retrieved mail/pages (no invention; no URL → omit).
2. Remix per item, then assemble Brief → Deep Dives → Tools → More.
3. Prefer counterintuitive / specific / actionable; skip generic wisdom and fluff.

**Brief**  
Each bullet = **1–2 sentences** that already contain the takeaway. No links. No “某刊报道称…” wrapping.

**Deep Dives** — bottom-line first
1. First line of body or **Insight** must answer: what should this reader *do or watch* differently?
2. Then context + 2–4 specific supports (numbers OK if attributed).
3. Prefer one memorable concrete detail or quote over jargon archaeology.
4. Write as a standalone briefing—avoid “本文 / 这封邮件 / 在这篇报道中”.
5. Translate specialist jargon into language this reader can use.
6. Tone: sharp colleague, not press-release or paper.

**Tools**  
Name + what it does for this reader’s workflow + Best for + official link.

**Prose language**  
Natural prose in the locked newsletter language; keep common EN tech terms where professionals keep them; keep proper nouns in English; no translationese.

## Numbers & prose

- Ground every claim; never invent. Secondhand figures OK if needed and attributed.
- Concise, natural prose; avoid opaque jargon.
- Name rankings in full; explain scores in reader language (what to check)—not eval dumps.

## Collaboration

Teammate suggestions: apply clear non-conflicting wins and say what changed; contested overrides → ask first. Keep collaboration notes out of the newsletter body.

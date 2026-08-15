---
name: raid-dossier
description: Use when asking for a strategy document, a report, a one-pager, a summary of the plan, something to print, something to hand to a partner, contractor, advisor or investor, or when asking "what is our marketing strategy" as a whole rather than what to do today. Writes one self-contained, printable dossier from the pack.
---

# raid-dossier

Never fight where the money wins. `raid-briefing` hands the operator today's slice. This hands a **stranger** the whole strategy, on paper, in language that does not require having read any of this doctrine.

## 1. What this is for, and why it is not the briefing

The pack is ten working files in doctrine vocabulary. That is correct for working and useless for handing over. A contractor does not know what a motte is. An advisor asked to sanity-check the plan should not have to learn a metaphor first, and a founder who has to explain the vocabulary before the strategy has not been handed a strategy.

| | `raid-briefing` | `raid-dossier` |
|---|---|---|
| Reader | the operator, who knows the pack | anyone, including someone who has never seen it |
| Cadence | daily | when something needs handing over |
| Length | two minutes aloud | as long as the pack justifies, usually two to four pages |
| Vocabulary | doctrine terms, as-is | **doctrine terms translated, always** |
| Answers | what do I do today | what is the strategy, and what do we actually know |

**The translation rule is the whole skill.** Every doctrine term is replaced by what it means, every time:

| Never write | Write |
|---|---|
| motte | what we own outright |
| bailey | rooms we operate in but do not own |
| asymmetry | what a funded competitor structurally cannot say |
| the gate / stage 2 | the plain condition, spelled out |
| cleared / uncleared | what we can prove, with a source |
| rot | what is going stale, and since when |

A dossier containing the word "bailey" has failed, however accurate the rest of it is.

## 2. Where every line comes from

**A dossier never fetches, and never invents.** Same property as `raid-briefing`: the toolbox is `Read`, `Glob`, `Grep` and `Write`, and there is nothing in it to fetch with. Every sentence traces to a file in `.monkeys/`, or it does not go in.

This matters more here than anywhere else in RAID, because this is the one artifact that leaves the building. A briefing with a guess in it misleads the person who wrote the guess. **A dossier with a guess in it misleads someone who has no way to check.** That is the failure this skill is built to make impossible, and it is why section 6 exists.

If the pack is thin, the dossier is short. A short honest dossier is a finished deliverable. Padding it to look substantial is the one thing that would make it worthless to the person holding it.

## 3. The sections, in order

Write only the sections the pack can support. Omit an empty one rather than printing a heading over "none recorded", **except** section 6, which is never omitted.

1. **The situation.** One paragraph. What the product is, what stage the campaign is at in plain words, and the single condition that opens the next one. Take the stage from `campaign.md`; do not re-derive it, `raid-campaign` already decided. State the gate as a condition a stranger can check, not as a stage number.

2. **Who we are for.** From `recon.md` `## Pains`, in the buyer's own words, quoted. Their phrasing is the evidence; a paraphrase here quietly converts a finding into an opinion. Where the file is empty, say the buyer has not been interviewed yet and that everything downstream is a hypothesis. That sentence is worth more than three invented personas.

3. **Where we can win.** From `asymmetry.md` `## Our ground`, with the reason. **Name no competitor.** `asymmetry.md` is internal and naming a rival in an outward document breaks `raid-asymmetry`'s hard rule and `fortress-truth`'s claim discipline at once. Write "a subscription-funded incumbent cannot credibly offer a one-time price", never the company.

4. **What we can prove.** From `truth.md` `## Cleared`, each claim with its source, as a table. This is the section a skeptical reader turns to first, so it carries the sources visibly rather than in a footnote. If `## Cleared` is empty, say so plainly: nothing has been sourced yet, and no public claim can be made until one is.

5. **What we hold and what we rent.** From `motte.md` and `bailey.md`, translated. Owned assets on one side, rooms and platforms on the other, with the standing of each account stated as plain English ("new account, no history", "known there, has posted usefully"). The point a stranger should take away without being told: the rented column can be confiscated and the owned column cannot.

6. **What we do not know.** Never omitted, never softened, always last but one. Every gap the pack shows: files that are empty, claims recorded without a source, rooms named but never entered, numbers never measured. A dossier that lists its own gaps is the reason the rest of it can be trusted, and a reader who finds an unlisted gap themselves discounts everything above it.

7. **What happens next.** From `campaign.md` `## Open now`, each action with the plain description of what it is, plus `## Blocked on a human decision` in full, naming the decision and whose it is. A decision left as "pending" is what this section exists to prevent.

## 4. Printing

Write one self-contained file to `.monkeys/dossier-<YYYY-MM-DD>.md`. Dated, because a strategy handed over in March and read in July needs to say which it is.

Self-contained means it must print correctly with no tooling beyond opening it:

- **No links as the sole carrier of meaning.** A printed page has no hyperlinks. Where a URL matters, write it out in full so a reader can type it.
- **No references to other pack files.** "See `asymmetry.md`" is a dead end on paper. Bring the content in or leave it out.
- **Tables stay narrow.** Three or four columns. A six-column table is unreadable at print width, and the pack's own five-column numbers table should be filtered to what the reader needs rather than reproduced whole.
- **No doctrine jargon**, per section 1, including in headings.
- **State the date and the product name in the first two lines**, so a loose page found on a desk identifies itself.

## 5. Steps, in order

1. **Read the whole pack.** All ten files plus the most recent briefing. A dossier written from a subset silently omits whatever it did not open.
2. **Check `campaign.md` exists.** If it does not, there is no stage to report and no Open now to draw section 7 from. Stop and route to `raid-campaign`, exactly as `raid-briefing` does.
3. **Draft each section from its named source**, translating every doctrine term as you go, not in a pass afterwards. A translation pass at the end is how "bailey" survives into a printed page.
4. **Write section 6 by walking the pack for absence**, not by remembering what felt thin. Empty file, missing source, room never entered, metric never recorded.
5. **Re-read it as the recipient.** A contractor who has never seen the pack: is every noun defined, is every claim sourced, is there a single sentence that only makes sense if you already know the doctrine? Cut or translate it.
6. **Write the file, and hand the human the path.** RAID stages; it does not send. Emailing this to an advisor is the founder's action, taken deliberately, with the document in front of them.

## 6. Three hard rules

**No claim without its source, in the document itself.** Not "we save users four hours" but "we save users four hours, measured in the benchmark at <full URL>". This is `fortress-truth`'s law and it binds here whether or not FORTRESS is installed. An outward document is exactly where an unsourced number does the most damage, because the reader cannot check it and will assume someone did.

**Never name a competitor.** Section 3 says why. It is `asymmetry.md`'s own rule, and this is the file most likely to break it, because comparison is the most natural way to explain an advantage.

**Never fill a gap to make the document look finished.** An empty section is information. An invented one is the failure that makes every other section suspect, and it is unrecoverable in the way a printed page is unrecoverable: you cannot edit what someone already put in a folder.

## 7. What this doesn't decide

It does not decide the strategy: `raid-campaign` sequenced it and this reports it. It does not write public marketing copy, which is a different job with a different reader and is bound by `fortress-truth`. It does not decide who receives the document, which is a human's call and a `fortress-gate` matter where FORTRESS is installed.

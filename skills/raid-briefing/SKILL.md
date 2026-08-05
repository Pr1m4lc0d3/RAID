---
name: raid-briefing
description: Use when asking for a daily briefing, asking what to work on today, or starting a marketing session. Reads the `.monkeys/` pack, `campaign.md`, prior briefings, and `numbers.md` — never fetches — and writes today's four-block briefing to `.monkeys/briefings/<date>.md`.
---

# raid-briefing

Never fight where the money wins. `raid-campaign` works out the sequence; this skill hands back today's slice of it — what moved, what to do today, what's blocked, and what's quietly rotting — in under two minutes, read aloud.

## 1. Where the data comes from

**A briefing never fetches.** It reads what is already on disk and writes one file. It does not call an API, does not need a credential, does not use an MCP, and does not open a network connection of any kind — not as a shortcut it avoids, but as a property of the tools this skill uses: `Read`, `Glob`, `Grep`, and `Write`. There is nothing else in its toolbox to fetch with.

Everything a briefing says traces to one of these, and nothing else:

- the pack — `recon.md`, `asymmetry.md`, `scars.md`, and, where `FORTRESS` is installed, `truth.md`, `bailey.md`, `motte.md`
- `campaign.md`, written by `raid-campaign` — this skill does not re-derive the open stage; it reads what `raid-campaign` already decided. If `campaign.md` doesn't exist, say so and point at `raid-campaign` — there is no stage to draw **Today** from until it has run
- prior files under `.monkeys/briefings/` — the only way to know what changed since last time
- `.monkeys/numbers.md` — the one place live numbers enter the pack at all

A missing file reads the same as an empty one, the same rule `raid-campaign` uses: no `bailey.md` is not "unknown," it's "checked, and there's nothing there."

**Live numbers enter the pack only through `numbers.md`, and only a human or a companion holding the actual credentials writes a row to it.** This skill reads that file; it never appends to it, never edits a value in it, and never derives a number from anywhere else and writes it in as if it had. The reason isn't caution for its own sake: a briefing that needed credentials to run would stop working the moment it left the machine that has them, and running on a stranger's machine with nothing to configure is the whole reason this is shareable at all. A briefing that fetches is a briefing that only works for one person.

Create `.monkeys/numbers.md` from the schema below **only if it doesn't already exist.** If it's already there, leave it exactly as it is — don't reformat it, don't add a header line it's missing, don't touch a row already in it.

```markdown
# Numbers

Written by whoever has the credentials. Never fetched by a skill.
An empty table is honest; an invented row is not.

| Date | Metric | Value | Source |
|---|---|---|---|
```

**An empty numbers table is honest.** It means nobody with the credentials has written a number down yet, which is a true fact about the state of the campaign and belongs in the briefing exactly as stated. **Never estimate, infer, or approximate a number to fill a row that's empty, and never carry a number over from a prior briefing as if it were fresh** — a guessed metric wearing a table's formatting is not more honest than a guess written in prose, it's a guess with better production values. If a block would need a number and none exists in `numbers.md`, say the table is empty and move on. That is the failure this skill exists to avoid, not a gap to paper over.

## 2. The four blocks

A briefing is short enough to read aloud in under two minutes. Four blocks, always in this order:

| Block | Contains |
|---|---|
| **Moved** | What changed since the last briefing: new rows in `numbers.md`, an account whose `standing:` changed in `bailey.md`, a campaign action completed. **If nothing moved, say nothing moved.** |
| **Today** | One to three actions, drawn **only** from `campaign.md`'s **Open now** — never from a closed stage, never invented outside what's already there — each naming the skill that does it. |
| **Blocked** | What is waiting, and on what or whom. Pull `campaign.md`'s **Blocked on a human decision** in full; add anything else found stalled while reading the pack. Human decisions are listed by name, not left as "pending." |
| **Rot** | What is quietly degrading. See §3. |

**Moved** needs a prior briefing to diff against. If none exists under `.monkeys/briefings/`, this is the first one — say that plainly ("first briefing — nothing to compare against yet"), which is a different statement from "nothing moved" and should not be written as if it were the same thing. Once a prior briefing exists, diff against the most recent one: new dated rows in `numbers.md` since its date, any `standing:` field in `bailey.md` that reads differently now, any line that was under `campaign.md`'s **Open now** last time and is gone or marked done this time.

**Today** is read, not decided. This skill does not determine which stage is open — `raid-campaign` already did that and wrote it to `campaign.md`. Copying an action campaign.md doesn't list, or one that campaign.md itself flags as entered early on override, into **Today** without saying so, is exactly the closed-stage leak this block exists to prevent. If `campaign.md` records an override (an action entered early on the adopter's explicit instruction), it may appear in **Today** — but say plainly that it's an override, in the same words `campaign.md` already used to record it.

## 3. Rot detection

Rot is concrete and checkable, never a vibe. On every run, check for each of the following and report any that are actually present — no padding the block with a vague worry when none of these fire, and no silence when one does:

- an entry in `truth.md` `## Uncleared` that has not moved since it appeared
- an incumbent in `asymmetry.md` with `revenue model: unknown — not verified`
- a room in `recon.md` `## Rooms` never entered, when the stage `campaign.md` reports as open calls for entering rooms
- a channel in `bailey.md` `## Active` with no row in `numbers.md`
- a staged draft that has not been sent
- an entry in `scars.md` whose rule today's open action would trip

For that last one, **surface the rule, not just the incident.** "Room X banned a promotional post last March" is the incident; "this room's rule is no links until N days of participation, and today's open action is a link" is the rule, and the rule is what's actually actionable — it tells the reader what today's action needs to avoid, not just what happened once before.

If none of the six checks find anything, say rot is clear. That is a real finding, stated plainly, not an empty section left to imply nothing was checked.

## 4. Today is capped at three

Never more than three actions in **Today**, even when `campaign.md`'s **Open now** lists more. A briefing listing ten items is a list, and a list gets skimmed, not acted on — the cap is what keeps this a daily driver instead of a backlog dump. If more than three are open, choose the three that most advance the stage `campaign.md` reports, and say how many were left out: "3 shown, 4 more open — see `campaign.md`." Don't silently drop the rest; the reader needs to know the full set exists even when only three are read aloud.

## 5. Writing the artifact

Write `.monkeys/briefings/<YYYY-MM-DD>.md`, dated to the day the briefing is produced. One file per day, and it is never overwritten.

If today's file already exists, read it back to the adopter and ask, in plain text, whether to append a new entry to it or produce a fresh briefing in its place. Don't silently pick one — a same-day re-run usually means something changed since the morning, and whether that belongs alongside the first briefing or replaces it is the adopter's call, not a default this skill gets to assume.

## 6. What this does not do

This does not fetch — no API, no MCP, no credential, ever, for any reason, including a plausible-sounding one. It does not publish, post, comment, or send anything; the artifact is a file a human reads, same staging rule as the rest of RAID (see `raid`). It does not schedule anything for later. It does not decide which stage is open — that's `raid-campaign`'s job, read here and never re-argued. And it does not estimate a number: an empty row in `numbers.md` stays empty in the briefing, stated as exactly that.

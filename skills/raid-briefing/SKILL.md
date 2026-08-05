---
name: raid-briefing
description: Use when asking for a daily briefing, asking what to work on today, or starting a marketing session. Reads the `.monkeys/` pack, `campaign.md`, prior briefings, and `numbers.md` — never fetches — and writes today's four-block briefing to `.monkeys/briefings/<date>.md`.
---

# raid-briefing

Never fight where the money wins. `raid-campaign` works out the sequence; this skill hands back today's slice of it — what moved, what to do today, what's blocked, and what's quietly rotting — in under two minutes, read aloud.

## 1. Where the data comes from

**A briefing never fetches.** It reads what is already on disk and writes one file. It does not call an API, does not need a credential, does not use an MCP, and does not open a network connection of any kind — not as a shortcut it avoids, but as a property of the tools this skill uses: `Read`, `Glob`, `Grep`, and `Write`. There is nothing else in its toolbox to fetch with.

Everything a briefing says traces to one of these, and nothing else:

- the pack — `recon.md`, `asymmetry.md`, `scars.md`, `truth.md`, `bailey.md`, `motte.md`. `raid`'s kickoff creates all of these wherever they are absent, and where `FORTRESS` is installed its skills own the discipline for the last three and fill them; either way this skill only reads them, and a file that exists but is empty says exactly what a missing one says
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

| Date | Metric | Kind | Value | Source |
|---|---|---|---|---|
```

`Kind` is `motte` or `bailey` — the same distinction `fortress-motte` and `fortress-bailey` use for what's owned outright versus what's rented attention. This skill doesn't interpret the column beyond reading it back; where `FORTRESS` is present, `fortress-measure` owns the doctrine behind the distinction.

**An empty numbers table is honest.** It means nobody with the credentials has written a number down yet, which is a true fact about the state of the campaign and belongs in the briefing exactly as stated. **Never estimate, infer, or approximate a number to fill a row that's empty, and never carry a number over from a prior briefing as if it were fresh** — a guessed metric wearing a table's formatting is not more honest than a guess written in prose, it's a guess with better production values. If a block would need a number and none exists in `numbers.md`, say the table is empty and move on. That is the failure this skill exists to avoid, not a gap to paper over.

## 2. The four blocks

A briefing is short enough to read aloud in under two minutes. Four blocks, always in this order:

| Block | Contains |
|---|---|
| **Moved** | What changed since the last briefing: new rows in `numbers.md`, an account whose `standing:` changed in `bailey.md`, a campaign action gone from `campaign.md`'s Open now since last time. **If nothing moved, say nothing moved.** |
| **Today** | One to three actions, drawn **only** from `campaign.md`'s **Open now** — never from a closed stage, never invented outside what's already there — each naming the skill that does it. |
| **Blocked** | What is waiting, and on what or whom. Pull `campaign.md`'s **Blocked on a human decision** in full; add anything else found stalled while reading the pack. Human decisions are listed by name, not left as "pending." |
| **Rot** | What is quietly degrading. See §3. |

**Moved** needs a prior briefing to diff against. If none exists under `.monkeys/briefings/`, this is the first one — say that plainly ("first briefing — nothing to compare against yet"), which is a different statement from "nothing moved" and should not be written as if it were the same thing. Once a prior briefing exists, diff against the most recent one: new dated rows in `numbers.md` since its date, any `standing:` field in `bailey.md` that reads differently now, any line that was under `campaign.md`'s **Open now** last time and is absent from it now.

`campaign.md` carries no completion marker — there is no field anywhere that says a given action was finished rather than dropped. An action that was under **Open now** last time and isn't there now has changed, and that much is checkable; whether it was completed or simply removed is not something reading `campaign.md` alone can tell you. Report it as changed, and say plainly that this skill can see that it changed but not which of the two happened — that is the honest limit of what the file records, not a gap to paper over with a guess either way.

**Today** is read, not decided. This skill does not determine which stage is open — `raid-campaign` already did that and wrote it to `campaign.md`. Copying an action `campaign.md` doesn't list into **Today** is exactly the closed-stage leak this block exists to prevent. An override-flagged action — one `campaign.md` records as entered early, on the adopter's explicit instruction — may appear in **Today** only when that specific override record is actually present in `campaign.md`, and it must carry its label every time it's shown, in the same words `campaign.md` used to record it. If the label can't be substantiated by reading `campaign.md` — no matching record for that action — the action does not go in **Today**, full stop. The label is the only thing that distinguishes a deliberate early entry from a gate that got skipped quietly; an override shown without it is indistinguishable from a leak, so the label is not optional decoration on the entry, it's the entire justification for the entry existing in **Today** at all.

## 3. Rot detection

Rot is concrete and checkable, never a vibe. Every check here has to be answerable from something the pack or the briefing history actually records — a check with no readable signal behind it is worse than no check at all, because it reads as coverage and delivers nothing. On every run, check for each of the following and report any that are actually present — no padding the block with a vague worry when none of these fire, and no silence when one does:

- an entry in `truth.md` `## Uncleared` that is still sitting there, unmoved, across two briefings in a row
- an incumbent in `asymmetry.md` with `revenue model: unknown — not verified`
- a room in `recon.md` `## Rooms` that no prior briefing has recorded as acted on, when the stage `campaign.md` reports as open calls for entering rooms
- a channel in `bailey.md` `## Active` with no row in `numbers.md`
- an entry in `scars.md` whose rule today's open action would trip

**`## Uncleared` carries no date field**, so "hasn't moved" is read against prior briefings instead of a timestamp. An entry counts as rotting once it appears under `truth.md`'s `## Uncleared` now **and** the same entry text already appeared in the immediately preceding briefing's **Rot** section. The first time an entry is seen, there is nothing to compare it against yet — note it plainly as newly observed rather than calling it rot; one sighting can't show something hasn't moved, only two can, and that note is what gives the next run something to check against. This is self-bootstrapping in the strict sense: on the very first briefing ever written for a pack, there is no preceding briefing at all, so nothing under this check can fire or even seed yet — say that plainly, the same way a missing `campaign.md` is said plainly rather than guessing at a history that isn't there.

**Rooms** works the other direction: scan every prior file under `.monkeys/briefings/`, not just the most recent one, for the room's name appearing in a **Today** or **Moved** entry — that's the plain-text evidence the room was named as real work at least once, queued in a **Today** or reported changed in a **Moved**. That's not certified proof a visit happened — a **Today** entry can go undone the same way `campaign.md` can't confirm a completed action above — but it's the honest ceiling of what the pack can show, and it's a real signal: a room never once written down anywhere is a room nothing has actually pointed at yet. A room named in `recon.md` `## Rooms` that never shows up that way, while the stage `campaign.md` reports as open calls for entering rooms, is rot. On the first briefing there are no prior files to search, so every named room reads as not-yet-acted-on — that's the correct reading of a pack that hasn't done anything yet, not a false positive to suppress.

**An override-flagged appearance does not count as the room having been acted on.** When the entry naming the room carries an override label — one `campaign.md` records as entered early, on the adopter's explicit instruction — skip it and keep looking; if that is the room's only appearance anywhere in the briefing history, the room is still not-yet-acted-on for this check. The reason is not bookkeeping tidiness: an override means the gate was crossed *before* the room's conditions were met, which makes that room **more** worth watching, not less. Letting the override entry satisfy the check would switch off the watch at the exact moment the pack has the most reason to keep it on — a room entered early, on rules that may still read `unknown — not verified`, silently reclassified as handled.

For the `scars.md` check, **surface the rule, not just the incident.** "Room X banned a promotional post last March" is the incident; "this room's rule is no links until N days of participation, and today's open action is a link" is the rule, and the rule is what's actually actionable — it tells the reader what today's action needs to avoid, not just what happened once before.

**One check from the original design is dropped outright, not fixed: a staged draft that has not been sent.** Nothing in the pack tracks drafts — there is no drafts file and no field anywhere that records one existing or being sent. A check with no readable signal behind it is not a check, it's a claim of coverage this skill cannot back up, so it does not belong in this list. If drafting-and-sending discipline ever gets a place to live in the pack, this check can come back; until then, say plainly that drafts are not something a briefing can see, rather than implying they're being watched.

If none of the five checks find anything, say rot is clear. That is a real finding, stated plainly, not an empty section left to imply nothing was checked.

## 4. Today is capped at three

Never more than three actions in **Today**, even when `campaign.md`'s **Open now** lists more. A briefing listing ten items is a list, and a list gets skimmed, not acted on — the cap is what keeps this a daily driver instead of a backlog dump. If more than three are open, choose the three that most advance the stage `campaign.md` reports, and say how many were left out: "3 shown, 4 more open — see `campaign.md`." Don't silently drop the rest; the reader needs to know the full set exists even when only three are read aloud.

## 5. Writing the artifact

Write `.monkeys/briefings/<YYYY-MM-DD>.md`, dated to the day the briefing is produced, in exactly this shape — a later run of this same skill reads it back to compute **Moved** and the two prior-briefing rot checks in §3, so the shape has to hold steady the way `campaign.md`'s shape holds steady for `raid-campaign`:

```markdown
# Briefing — <YYYY-MM-DD>

**Stage (from campaign.md):** <n> — <stage name>

## Moved
<what changed since the last briefing, or: first briefing — nothing to compare against yet>

## Today
<one to three actions, each: <action> — skill: <raid-* or fortress-*> — done when: <condition>>
<if any were left out: "<n> shown, <n> more open — see campaign.md.">

## Blocked
<what's waiting, and on whom — human decisions named>

## Rot
<any findings from §3, or: rot is clear>
```

One file per day, and it is never overwritten.

If today's file already exists, read it back to the adopter and ask, in plain text, whether to append a new entry to it or produce a fresh briefing in its place. Don't silently pick one — a same-day re-run usually means something changed since the morning, and whether that belongs alongside the first briefing or replaces it is the adopter's call, not a default this skill gets to assume.

## 6. What this does not do

This does not fetch — no API, no MCP, no credential, ever, for any reason, including a plausible-sounding one. It does not publish, post, comment, or send anything; the artifact is a file a human reads, same staging rule as the rest of RAID (see `raid`). It does not schedule anything for later. It does not decide which stage is open — that's `raid-campaign`'s job, read here and never re-argued. And it does not estimate a number: an empty row in `numbers.md` stays empty in the briefing, stated as exactly that.

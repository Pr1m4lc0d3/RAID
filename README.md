# RAID

### `RAID` takes ground · `FORTRESS` builds what can't be taken

RAID is the offensive half of **THE MAVERICK'S MONKEYS** — a pair of Claude Code plugins that
together make an agent competent at marketing a product with no budget. The taijitu splits across
the two: `RAID` is yang, light and initiating; `FORTRESS` is yin, dark and holding. Side by side the
two halves close into one circle — a raiding party with nowhere to fall back gets hunted down, and a
fortress that never raids starves. Neither half is complete alone, and neither half is pure: `RAID`
carries restraint (the loudest play is the one most likely to get you banned), `FORTRESS` carries
aggression (an asset you never spend is hoarding, not strategy).

**`FORTRESS` is released.** It ships standalone — every skill in it runs without RAID installed.
This repository ships `RAID`, the other half of the pair: where `FORTRESS` holds ground, `RAID`
takes it. Each plugin is a complete, independently useful tool on its own; together they are one war
doctrine split by function.

Both halves answer to the same domain: guerrilla marketing, as Levinson defined it in 1984 —
imagination, energy, and time substituted for money. Its defining trait is **disproportion**: a
small input that produces an outsized effect, because someone else carries the message for free.
`RAID` is that trade's offensive expression — surprise, timing, and asymmetry aimed at finding
ground an incumbent, defended by money, cannot follow you onto.

---

## The doctrine

> **Never fight where the money wins.**

One test generates the entire target list. Does money win on this ground? Ads — money wins, stay
out. Head SEO terms — money wins. Paid placement, sponsorships, booths, influencer rates — money
wins, all of them. So *where doesn't it win?* Surprise, timing, niche depth, trust, weirdness,
physical space, and being genuinely useful in a room you don't own. That's the whole map, generated
by asking one question honestly, every time, before committing effort anywhere.

The corollary that keeps this from becoming vandalism: **disproportion or don't bother.** A stunt
nobody carries for you is just a weird thing you did with your own time.

## The no-script disclosure

`FORTRESS` ships a real, enforcing script: `claim_lint.py`, dependency-free Python, that exits
non-zero on unsourced claim-shaped language. It's a build gate you can wire into CI.

**RAID ships no script, and no equivalent exists.** That's deliberate, not an oversight. A linter
can check whether a sentence is sourced, because sourcing is a property of text sitting right there
on the page. It cannot check whether a market is worth fighting for — that's a judgement about a
business, a competitor's own economics, and a room full of people, none of which live in the text
being linted. There is no pattern to match against for "is this actually asymmetric ground" the way
there is for "is this number followed by a source."

What RAID does instead: it structures the judgement rather than pretending to automate it. The
target gate turns "should I do this" into checkable sub-questions — was the incumbent's revenue
model actually fetched from their own pricing page, is there a named person who carries this play
and a reason it serves them, were a room's rules actually read before entering it — each with an
answer that traces to something fetched or interviewed, never something felt. Kickoff writes those
answers into `.monkeys/recon.md` and `.monkeys/asymmetry.md`, so the next session reads a decision
instead of re-deciding from a blank page. That's real discipline, applied where discipline is
actually possible. It is not a script, and bolting on a fake guard for symmetry with `FORTRESS`
would be exactly the overclaiming this whole system exists to refuse.

## The skills

| Skill | Job |
|---|---|
| **`raid`** | Front door: doctrine, the target gate, one-time kickoff that generates a recon-and-asymmetry pack (`.monkeys/recon.md`, `.monkeys/asymmetry.md`) from the adopter's own product and market, capability report, routing to the six skills below. |
| **`raid-recon`** | Who hurts, captured in their own words, and where they gather. Records a room's rules and entry cost, not just its audience size — and marks anything unconfirmed `verified: no` rather than dropping it or guessing at it. |
| **`raid-asymmetry`** | Reads an incumbent's own revenue model from their own pricing or plans page and derives what that model structurally forbids them to say. Internal ammunition only — `asymmetry.md` is never published, and naming a rival in public copy is a `FORTRESS` violation. |
| **`raid-stunt`** | The disproportionate play, filtered by the carry test: name the person who repeats it and why repeating it serves them, or don't build it. Rejects plays that insult the audience they need, would embarrass if they worked, or require a budget to be noticed. |
| **`raid-moment`** | Ambush timing: rides attention already in motion instead of manufacturing it, refuses to ride a tragedy, and lets a moment pass rather than publish an unverified claim to catch it. |
| **`raid-borrow`** | Finds a room that already has an audience and pays for standing in it with usefulness offered in advance — never a drop-and-pitch. |
| **`raid-multiply`** | Cuts one substantial asset into many standalone pieces. Every cut has to make sense on its own, with no assumed context from the source. Decides and drafts the cuts; rendering is the last mile and needs no specific tool. |

## Install

```
/plugin marketplace add ./RAID
/plugin install raid@raid
```

Or point the marketplace command at wherever this repository is checked out locally
(`.claude-plugin/marketplace.json` at the repo root). Then, on the target repo, invoke `raid` to
run kickoff — it interviews the adopter about their own product and market and generates the
`.monkeys/recon.md` and `.monkeys/asymmetry.md` pack from scratch. Nothing ships pre-filled; a
template with plausible-looking example pains or competitors would be exactly the invented-evidence
problem RAID exists to avoid.

Every skill here runs on built-in tools alone — WebSearch, WebFetch, Read/Write/Edit, Glob/Grep,
Bash. `companions.json` ships with an empty `companions` array: no accelerant for any RAID skill
has been verified as publicly installable by a stranger, with an exact install command and a stated
cost, so none is listed. That's a complete answer, not a gap — `raid`'s capability report reports
exactly this: **"No optional capabilities needed — RAID runs entirely on built-in tools."**

## Honest proof — read this before trusting anything above

`scars.md` in this repository is real. Every entry documents a concrete incident with measurable
damage — a revenue channel that ran backward, a decision re-litigated for want of a written reason,
a creative asset picked by a number instead of by the person who had to live with it — and states
the rule the incident forced into existence. Nothing in that file is hypothetical.

**The system as a whole is unproven.** RAID has not produced a sale, and it has no case study of a
product it grew. This is stated here, deliberately and up front, not buried in a footnote — because
a marketing plugin that claimed results it had not produced would violate its own doctrine on line
one of its own documentation. A system built around finding ground an incumbent's own claims can't
reach cannot itself be the first place a claim gets made that the evidence doesn't support.

The honest pitch is narrower than "this will get you customers," and it's this instead: **this
encodes what the failures cost, so you can skip paying for them.** The doctrine, the target gate,
and `scars.md` exist because specific mistakes were expensive to learn once. Adopting RAID doesn't
promise growth — it removes the cost of relearning those mistakes the hard way.

# RAID worked example

**This is fictional. Every pain, room, incumbent, and number below was invented for this
example. "Backlot Hot Sauce" does not exist, "Scovie Club" does not exist, r/hotsauce is a
real subreddit but nothing here was actually posted to it, and `backlothotsauce.example` is
not a real domain — `.example` is the reserved TLD for exactly this purpose (RFC 2606),
chosen so nobody mistakes it for a live site. This is the same invented product as
`FORTRESS/examples/` — one story told from both halves of the doctrine — and it says so
here first for the same reason that example does: a worked example indistinguishable from a
real company's real data is the exact defect this system exists to prevent.**

Read the files in this order — roughly the order a real adopter would produce them, from
research to the thing a human actually sends.

## 1. `.monkeys/recon.md` — who hurts, in their own words

Two pains kept in the phrasing people actually used, not translated into a value
proposition, each marked `verified:` honestly — one pain the adopter mentioned never got
independently confirmed, and it's marked `verified: no` rather than dropped or upgraded to
look more solid. Two rooms, each with real rules and a real entry cost: r/hotsauce's
self-promotion confined to one pinned thread, and a farmers market's paid booth slot. Notice
neither room's `rules:` or `audience:` is a guess — that's the field RAID's own doctrine
treats as seriously as `fortress-truth` treats a sourced number.

## 2. `.monkeys/asymmetry.md` — ground an incumbent can't hold

One incumbent (fictional), its revenue model read plainly, and the one claim that model
structurally forbids: a subscription box can't credibly lead with "no commitment" without
threatening the recurring revenue that funds it. This file is never published — it's
internal ammunition for `## Our ground`, one claim Backlot can make honestly that the
incumbent cannot match without becoming a different business.

## 3. `.monkeys/voice.md` — how it sounds, and what it won't say

Filled in, not left as placeholder comments: two qualities under `## Sounds like`, two
banned words under `## Never says` (each with a real cost attached, not just a preference),
and two `## Proof available` entries — a batch log and a spreadsheet row count, both things
that actually exist and could actually be shown, per the pack format's own rule that this
section never lists something nobody has made yet.

## 4. `.monkeys/truth.md`, `.monkeys/motte.md`, `.monkeys/bailey.md`

Identical to the copies in `FORTRESS/examples/` — one shared pack, because a real adopter
running both plugins has one `.monkeys/` directory, not two. `raid-campaign`'s gates read
these three files directly; they're included here so the campaign below is checkable against
real file contents instead of asserted.

## 5. `.monkeys/campaign.md` — the closed gate, and what opens it

This is the file that carries the "show a failure" requirement on the RAID side. Read
**Why this stage** first: stage 1's gate passed (truth.md has three Cleared facts), stage 2's
gate passed (the farmers market booth reads `standing: established`), and then stage 3
**failed** — not because a file is missing, but because the delivery check came back
`unverified 2026-08-05`: nobody has actually walked a stranger through checkout since the
shipping-rate plugin changed. That's `raid-campaign`'s stage-3 gate exactly as documented —
`motte.md` non-empty is not enough on its own, the delivery check has to pass too — and
here it doesn't, so the open stage is 2, not 3, and `## Closed, and what opens it` names the
exact unmet condition rather than a vague "not ready yet." `## Blocked on a human decision`
names the one thing no amount of further work can resolve: which fix path to take, which is
the founder's call, not something this pack decides for them.

## 6. `.monkeys/briefings/2026-08-05.md` — today's slice

Four blocks, capped at three actions (here, two). `## Moved` says plainly that this is the
first briefing on record rather than pretending to compare against nothing. `## Rot` fires
one real, checkable finding: both `bailey.md` `## Active` channels have zero rows in
`numbers.md` — nobody has logged a number against either one yet. That's one of
`raid-briefing`'s five concrete rot checks actually firing, not a placeholder warning.

## 7. `raid-draft-body.md` and the genuine lint run

The literal text `raid-draft` would hand over for the next r/hotsauce comment: the sourced
21-day ferment claim, and a genuine question that answers one of `recon.md`'s own pains
(sauces separating in the bottle) — no link, because `bailey.md` reads `links allowed: no`
for this account. This is not asserted clean; it was run for real:

```
python tools/monkeys/claim_lint.py raid-draft-body.md
```

```
claim-lint: config: tools\monkeys\truth.config.json | categories: absolute=warn, comparative=error, magnitude=error, number=error, superlative=error, testimonial=error | ignore patterns: 1: \b\d{4}-\d{2}-\d{2}\b|\b(?:\d{1,2}\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)\.?\s+(?:\d{1,2},?\s+)?\d{4}\b
claim-lint: no unsourced claims found.

EXIT CODE: 0
```

Full output in `raid-draft-lint-run.txt`.

## 8. `raid-draft-output.md` — the complete handover unit

The full `raid-draft` deliverable: the draft, **Claims used** (tracing to the one Cleared
line above), **Claims deliberately avoided** — the "best hot sauce" superlative from
`truth.md` `## Uncleared`, carried over with its exact recorded reason rather than a
paraphrase — **Room fit**, and the **Human send checklist**. Three boxes are checked because
they were actually verified against the pack and the real lint run above; the last one,
"a human is sending this," stays unticked — the agent never ticks that box, because RAID
stages and never publishes.

## Format verification

The six section-based files above were loaded through the real parser at
`console/src/pack.js` (`parsePack`), including the briefing and the copies shared with
`FORTRESS/examples/`:

```
=== RAID/examples/.monkeys ===
files provided: [ 'asymmetry.md', 'bailey.md', 'briefings/2026-08-05.md', 'campaign.md', 'motte.md', 'numbers.md', 'recon.md', 'truth.md', 'voice.md' ]
missing: [ 'sell-kit.md', 'scars.md' ]
malformed: []
unrecognised: []

=== MERGED (one shared pack, as a real dual-install would have) ===
files provided: [ 'asymmetry.md', 'bailey.md', 'briefings/2026-08-05.md', 'campaign.md', 'motte.md', 'numbers.md', 'recon.md', 'truth.md', 'voice.md' ]
missing: [ 'sell-kit.md', 'scars.md' ]
malformed: []
unrecognised: []
```

Zero malformed entries, zero unrecognised headings, in both the RAID-only pack and the
merged pack a dual install would actually have on disk. `sell-kit.md` and `scars.md` are
`missing` because this example never imports an Idea Forge Pro kit and nothing has gone
wrong yet to log — both honest, neither an error.

One thing worth stating plainly rather than glossing over: `voice.md` is part of the pack
format in `design.md` §6 and is real, hand-filled content in this example, but
`console/src/pack.js` does not currently parse it into a typed section — it isn't in
`parsePack`'s per-file calls at all, so it never appears in `missing`, `malformed`, or
`unrecognised` either; it's simply not read yet. That's a true statement about the current
state of the console, not a defect in this example, and it isn't this task's place to change
`console/src/pack.js` to fix it.

## What this is not

Not a claim that Backlot Hot Sauce could be a real business, and not a template. See
`FORTRESS/examples/` for the same product's defensive half: the claim register this
campaign's stage-1 gate reads, and the linter catching the one sentence this draft never
tried to make.

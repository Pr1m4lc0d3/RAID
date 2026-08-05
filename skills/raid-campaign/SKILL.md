---
name: raid-campaign
description: Use when planning a marketing campaign, asking what to do first, asking what comes next, or wanting a sequenced plan with no budget. Reads the `.monkeys/` pack, determines which of five gated stages is actually open, and writes `campaign.md`.
---

# raid-campaign

Never fight where the money wins. This skill turns that doctrine into a sequence: it reads the adopter's own pack, decides — by checking, not guessing — which of five stages the work is actually in, and writes that decision to `.monkeys/campaign.md` so the next session doesn't re-decide from a blank page.

## 1. What this does

Read whatever `.monkeys/` files exist — `truth.md`, `motte.md`, `bailey.md`, `recon.md`, `asymmetry.md`, `scars.md`, `numbers.md`, and any prior files under `.monkeys/briefings/` — and from what they actually say, work out which of five stages is open. Write that to `campaign.md`.

`truth.md`, `motte.md`, and `bailey.md` are written by FORTRESS skills where FORTRESS is installed. This skill only reads them and works the same with or without FORTRESS present — a missing file reads exactly the same as an empty one (see section 3). Nothing here requires FORTRESS to be installed.

**The plan is derived from the pack, never from a template.** There is no default week-one, week-two schedule waiting to be filled in with the adopter's name on it. If `recon.md` names one room and `truth.md` has one cleared fact, the campaign is one room and one fact — short, because that is what is actually true, not because less work was done. A campaign that reads the same for every adopter would mean the pack was never read. **If the pack is thin, the campaign is short. That is correct, not a failure to fix by inventing more.**

Run this fresh at the start of a session, or whenever asked what comes next. Read the pack before answering — never answer from memory of a previous run; the pack may have changed since.

## 2. The five stages

The order is not a preference. There is no standing to earn before the pack exists to earn it with, and nothing to prune before there is a number to prune against. Skipping ahead does not compress the work — it just means the skipped stage's condition is still unmet when the next stage's problems show up anyway.

| Stage | Name | The work |
|---|---|---|
| 0 | Foundation | Build the pack. Stand up owned assets. Create accounts — they start cold. Zero promotional activity. |
| 1 | Standing | Enter rooms and be useful. **No links.** Earn the right to be heard. |
| 2 | First artifacts | Publish something substantial on land you own, then syndicate cuts of it. |
| 3 | First links | Share the artifact where it is genuinely on topic. |
| 4 | Prune | Kill what produced nothing. Double down on what did. |

Everyone starts at stage 0. It has no gate — building the pack and standing up cold accounts requires nothing to be true first. Every stage after it does.

## 3. The gates

Check the gates in order, starting at stage 1. The open stage is the highest one whose condition is actually true when checked against the pack — not the one the adopter believes is true, and not the one that would be convenient this week.

| Stage opens when | Checked by reading |
|---|---|
| **1 · Standing** | `truth.md` has at least one entry under `## Cleared` | if it does not, the founder has nothing they can safely say |
| **2 · First artifacts** | at least one account in `bailey.md` `## Active` reads `standing: warming` or `established` | publishing as a stranger wastes the artifact |
| **3 · First links** | `motte.md` `## Held` is non-empty **and** the delivery check passes | a link into rented ground converts standing into someone else's asset |
| **4 · Prune** | `numbers.md` has at least two dated rows | you cannot prune against nothing |

A missing file reads the same as an empty one. No `bailey.md` means no `## Active` entries, which closes stage 2 exactly as if the file existed with nothing in it. "The file doesn't exist yet" is not unknown — it is the same answer as "checked, and it's empty."

Stop at the first gate that fails. The stage before it is open; the stage it belongs to is closed. Report both: the open stage is what `campaign.md`'s **Open now** describes; the closed one is what its **Closed, and what opens it** describes.

## 4. The delivery check

Part of stage 3's gate, and stated on its own because it is the one most often skipped.

> Before driving traffic anywhere, confirm a stranger can complete the action end to end — download, install, buy, sign up, receive what they paid for. Ask the adopter directly and record the answer.
> **A campaign that succeeds into a broken delivery path costs more than one that never ran.** The traffic is spent, the standing is spent, and the person who tried is gone. If delivery is unverified, stage 3 stays closed and the unmet condition is named in `campaign.md`.

Ask the question directly, every run. Don't infer a "yes" from a prior session's answer, and don't infer it from the product looking finished — a build that compiles is not the same claim as a stranger actually receiving what they paid for.

## 5. Refusal

When asked for work that belongs to a closed stage, do not do it.

Say, once, plainly:
- which stage the request belongs to
- which condition is unmet, read straight from the gate table
- the open action instead — what work the current stage actually makes available

If the adopter asks again for the same closed-stage work, say it once more — the same three things — and then do it. **It is the adopter's business to overrule a gate.** What must never happen is the gate being skipped silently: complying the second time without a word, or complying the first time because refusing felt unhelpful, is the actual failure — not the override itself.

When the override happens, record it in `campaign.md`:
- add the requested action under **Open now**, noting it was entered early
- amend the relevant bullet under **Closed, and what opens it** to state the stage was entered anyway, on the adopter's explicit instruction, and the date — the condition itself stays listed as unmet, because doing the work once does not make it true

An agent that quietly produces stage-3 work for a stage-0 founder has not helped them skip ahead. It has hidden from them that they were never standing on stage 3's ground to begin with.

## 6. Naming the drift

A bootstrapper's predictable failure is doing the comfortable work instead of the effective one. Rewriting copy, retuning a bio, reformatting an asset — all of it feels like progress, and none of it moves a stage forward if the stage's actual gate is "enter a room" or "publish something." Reaching into an unfamiliar room is uncomfortable. Polishing something already built is not. That asymmetry is exactly why it needs naming instead of being assumed away.

On every run, read whatever files exist under `.monkeys/briefings/`. Compare what each one recorded as done against what the stage open at the time called for. If several consecutive sessions recorded only refinement of existing material — edits, formatting, re-drafts — while the open stage called for entering a room or publishing something, say so plainly and name the count: "Three sessions in a row touched only existing copy; stage 1 is still open and no room has been entered." State the observation and the open action next to it. Don't moralise past that — the count is the argument, not a lecture.

If no briefings exist yet, there is nothing to compare. Say that, and move on.

## 7. Blocked on a human

Some things cannot be unblocked by work: a pricing decision, a legal question, an unresolved question about what may actually be sold or promised. When the pack or the conversation surfaces one of these, record it in `campaign.md` under its own heading — **Blocked on a human decision** — naming exactly what it blocks.

**Never route around a human decision by quietly choosing for them.** If a stage's open action depends on an unresolved pricing question, that action goes under **Blocked on a human decision**, not under **Open now** with a guessed price silently filled in. Guessing what the adopter would have decided is not progress — it is a decision made in their name, without them.

## 8. Writing `campaign.md`

Write `.monkeys/campaign.md` at the adopter's repo root, in exactly this shape — this is a contract `raid-briefing` reads:

```markdown
# Campaign

**Stage:** <0-4> — <stage name>
**Opened:** <YYYY-MM-DD>

## Why this stage
<one paragraph: what is true that opened it, what is not yet true>

## Open now
- <action> — skill: <raid-* or fortress-*> — done when: <checkable condition>

## Closed, and what opens it
- **Stage <n> — <name>** — blocked by: <the specific unmet condition>

## Blocked on a human decision
- <decision> — why it blocks: <what cannot proceed> — who: <the adopter>
```

Every bullet under **Open now** names a real action drawn from what's actually in the pack — which specific room from `recon.md` to enter next, which specific asset to build — never the stage table's one-line description restated as if restating it were an action. `skill:` names the sibling that actually does it, `raid-*` or, where FORTRESS is present, `fortress-*`, so the founder knows where to go, not just what to do. `done when:` is a condition checkable against the pack next run — the same discipline the gates themselves use, not a feeling of being finished.

## 9. What this does not do

This does not publish, schedule, or send anything — RAID stages, it never publishes; see the staging rule in `raid`. It does not fetch numbers — `numbers.md` is written by a human or a companion with credentials, never by this skill. And it does not promise a result: a stage being open is a statement about what the pack justifies doing next, not a forecast of what doing it will produce.

---
name: raid-campaign
description: Use when planning a marketing campaign, asking what to do first, asking what comes next, or wanting a sequenced plan with no budget. Reads the `.monkeys/` pack, determines which of five gated stages is actually open, and writes `campaign.md`.
---

# raid-campaign

Never fight where the money wins. This skill turns that doctrine into a sequence: it reads the adopter's own pack, decides — by checking, not guessing — which of five stages the work is actually in, and writes that decision to `.monkeys/campaign.md` so the next session doesn't re-decide from a blank page.

## 1. What this does

Read whatever `.monkeys/` files exist — `truth.md`, `motte.md`, `bailey.md`, `recon.md`, `asymmetry.md`, `scars.md`, `numbers.md`, `sell-kit.md` where it is there at all, and any prior files under `.monkeys/briefings/` — and from what they actually say, work out which of five stages is open. Write that to `campaign.md`.

`truth.md`, `motte.md`, and `bailey.md` are created empty by `raid`'s kickoff wherever they are absent, and where FORTRESS is installed its skills — `fortress-truth`, `fortress-motte`, `fortress-bailey` — own the discipline for them and fill them. Whoever arrives first creates the file; each plugin owns the discipline for its own files. This skill only reads them, and works the same with or without FORTRESS present: a missing file reads exactly the same as an empty one (see section 3). **Nothing here requires FORTRESS to be installed, and nothing here is unreachable without it** — a RAID-only adopter with one cleared fact in `truth.md` opens stage 1, because kickoff put the file there and asked them for the fact.

**The plan is derived from the pack, never from a template.** There is no default week-one, week-two schedule waiting to be filled in with the adopter's name on it. If `recon.md` names one room and `truth.md` has one cleared fact, the campaign is one room and one fact — short, because that is what is actually true, not because less work was done. A campaign that reads the same for every adopter would mean the pack was never read. **If the pack is thin, the campaign is short. That is correct, not a failure to fix by inventing more.**

Run this fresh at the start of a session, or whenever asked what comes next. Read the pack before answering — never answer from memory of a previous run; the pack may have changed since.

### `sell-kit.md`, where there is one

`.monkeys/sell-kit.md` is optional and most packs will not have one. `raid`'s kickoff writes it only where the adopter arrived with a Sell-Kit from Idea Forge Pro, and it holds that founder's own pre-build test: `The ask`, `PASS if`, `KILL if`, `By when`, `Commitment signal`, `Stop condition`, and what the test can and cannot prove.

**Where the file is absent, nothing on this page changes.** It reads exactly as an empty one does — the same rule every other pack file is under — and the campaign is derived from the rest of the pack precisely as it is today. This is the normal case, not a degraded one.

Where it is present, read it fresh on this run and take three things from it:

- **`The ask`, `PASS if`, `KILL if` and `By when` become the campaign's first objective and its kill criteria — adopted, not paraphrased and not competed with.** A pre-build test is not something running alongside a guerrilla campaign; it *is* stages 1 through 3. The rooms entered, the artifact published, the link finally shared all exist to produce the answer that test is asking for. Name it in **Why this stage**, in the founder's own words: the ask, what passes, what kills, and by when. Then every bullet under **Open now** is the *open stage's* work toward that ask — the first one being whatever moves it furthest — and where stage 3 is what's open, `The ask` is itself that bullet, with `PASS if` and the `By when` date as its `done when:`. **The gates still bind.** A kit whose ask is "take a pre-order" does not open stage 3 for a founder standing on stage 1; it tells you what stage 1 is *for*, which is the opposite of a reason to skip it. **Never invent a parallel objective while a kit's ask sits unmet** — two objectives means the founder gets measured against whichever one is going better. And state `KILL if` next to the ask wherever the ask appears: a test that failed has to be recognisable as a kill, not as a reason to try harder for another month.
- **`Commitment signal` defines what counts as a real row in `numbers.md`.** Where the kit says a commitment is a payment, a reply saying "great idea", a follow, and a mailing-list signup are not commitments — and stage 4's gate is not satisfied by counting them as if they were. The kit's definition is usually stricter than a founder's instinct in the moment it is being applied, which is exactly when it is worth honouring as written. **Never loosen it to make a row available.** State it in **Why this stage** with the objective, and again in stage 4's bullet under **Closed, and what opens it** while that stage is the closed one.
- **`Stop condition` is carried into stage 4's pruning.** Prune reads it as the condition that ends the whole line of work, not merely the condition that kills a channel. Name it wherever stage 4 appears — in its **Closed, and what opens it** bullet while it is shut, and in **Why this stage** once it is open — in the founder's own words.

**This file is read, never written.** Nothing this skill produces is written back into `sell-kit.md`: `campaign.md` is derived output and the kit is input, so a campaign editing it would be a derived file rewriting the thing it derives from — the founder's own test, altered by nobody's decision. Reading it fresh on every run is what makes this safe: an objective taken from it cannot be erased by the regeneration in section 8, because it is not stored in `campaign.md` — it is re-read from the kit each time.

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

**Stage 0's "stand up owned assets" has no owning skill in RAID, and naming a fake one would be worse than saying so.** Where FORTRESS is present, `fortress-motte` owns it. Where it is not, it is the adopter's own work — buying the domain, opening the list, standing up the page — recorded by them under `motte.md`'s `## Held` once it exists. Write it into **Open now** with `skill: fortress-motte` where FORTRESS is installed, and `skill: none — the adopter's own work, recorded in motte.md` where it is not. Every other stage-0 action does have a RAID sibling: the pack itself is `raid-recon` and `raid-asymmetry`.

## 3. The gates

Evaluate the gates in order, from stage 1 to stage 4 — never skip ahead to check a later one first. **The conditions are not monotonic:** a pack can satisfy gate 4 while failing gate 1 — two dated rows in `numbers.md` and zero entries under `truth.md` `## Cleared` does exactly that. There is one algorithm here, stated once: **stop at the first gate that fails.** The open stage is the last stage whose gate passed before that failure — never a stage picked because its own condition happens to be true in isolation, never the one the adopter believes is true, and never the one that would be convenient this week.

| Stage | Opens when | Why the gate exists |
|---|---|---|
| **1 · Standing** | `truth.md` has at least one entry under `## Cleared` | until then the founder has nothing they can safely say |
| **2 · First artifacts** | at least one account in `bailey.md` `## Active` reads `standing: warming` or `established` | publishing as a stranger wastes the artifact |
| **3 · First links** | `motte.md` `## Held` is non-empty **and** the delivery check passes | a link into rented ground converts earned standing into someone else's asset |
| **4 · Prune** | `numbers.md` has at least two dated rows, **at least one of kind `motte`** | you cannot prune against nothing, and two rows of rented attention is not evidence |

`numbers.md`'s `Kind` column marks each row `motte` or `bailey`. Gate 4 reads it directly — two rows of pure rented-platform attention (impressions, likes) is not something there is anything to prune toward, so they don't satisfy the gate on their own. Where FORTRESS is present, `fortress-measure` owns the motte-beats-bailey doctrine behind this distinction; it is reinforcement here, never a requirement — this gate reads the `Kind` column on its own, with or without FORTRESS installed.

A missing file reads the same as an empty one. No `bailey.md` means no `## Active` entries, which closes stage 2 exactly as if the file existed with nothing in it. "The file doesn't exist yet" is not unknown — it is the same answer as "checked, and it's empty."

Report both ends of the result: the open stage is what `campaign.md`'s **Open now** describes; the stage whose gate failed is what its **Closed, and what opens it** describes.

## 4. The delivery check

Part of stage 3's gate, and stated on its own because it is the one most often skipped.

> Before driving traffic anywhere, confirm a stranger can complete the action end to end — download, install, buy, sign up, receive what they paid for. Ask the adopter directly and record the answer.
> **A campaign that succeeds into a broken delivery path costs more than one that never ran.** The traffic is spent, the standing is spent, and the person who tried is gone. If delivery is unverified, stage 3 stays closed and the unmet condition is named in `campaign.md`.

**Ask the question directly, out loud, on every single run. There is no condition under which a run skips it.** Don't infer a "yes" from a prior session's answer, don't infer it from the recorded line in `campaign.md`, and don't infer it from the product looking finished — a build that compiles is not the same claim as a stranger actually receiving what they paid for. A delivery path that worked last month can be broken today: a payment processor deactivates, a domain lapses, a download link rots, a fulfilment step nobody re-tested silently stops. **`campaign.md`'s `Delivery check` line is a log of the last answer and its date. It is never a substitute for asking.** Read it if you like — then ask anyway, and record what you are told this run, even when the answer is identical to last run's.

Of every condition in the gate table, this is the only one that is not a file read — which makes it the only one that can be quietly softened without a grep ever catching it. That is why it is asked every run rather than cached.

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

**The observation goes in `campaign.md` under `## Drift`, as a dated line** — see the shape in section 8. It has to be written down, because a count that spans sessions cannot be recomputed from a single session: the whole claim is about a run of them. Say it to the adopter and record it, both. A drift observation that only ever lives in one conversation is exactly the comfortable-work problem in another form — noticed, agreed with, and gone by the next run.

## 7. Blocked on a human

Some things cannot be unblocked by work: a pricing decision, a legal question, an unresolved question about what may actually be sold or promised. When the pack or the conversation surfaces one of these, record it in `campaign.md` under its own heading — **Blocked on a human decision** — naming exactly what it blocks.

**Never route around a human decision by quietly choosing for them.** If a stage's open action depends on an unresolved pricing question, that action goes under **Blocked on a human decision**, not under **Open now** with a guessed price silently filled in. Guessing what the adopter would have decided is not progress — it is a decision made in their name, without them.

## 8. Writing `campaign.md`

Before writing, check whether `campaign.md` already exists. If it does, read it first. **Override records, every entry under `## Blocked on a human decision`, and every dated line already under `## Drift` are carried forward into the new file, never dropped.** An override record is permanent: it documents that a gate was crossed early and on whose instruction, and a record that disappears the next time this skill runs is worse than no record at all — it reads as though the gate was never crossed. A drift line is permanent for the same reason and carries forward the same way: section 6's count is a claim about consecutive sessions, and a section that only ever shows the latest run cannot show a run of anything. This run's drift observation is **appended** as a new dated line under the ones already there; earlier lines are left exactly as they are, never rewritten to match today's reading. Regenerate every other section fresh from the current pack state; only those three carry forward untouched.

Write `.monkeys/campaign.md` at the adopter's repo root, in exactly this shape — this is a contract `raid-briefing` reads:

```markdown
# Campaign

**Stage:** <0-4> — <stage name>
**Opened:** <YYYY-MM-DD>
**Delivery check:** <not yet asked | confirmed YYYY-MM-DD | unverified YYYY-MM-DD — reason>

## Why this stage
<one paragraph: what is true that opened it, what is not yet true>

## Open now
- <action> — skill: <raid-* or fortress-*> — done when: <checkable condition>

## Closed, and what opens it
- **Stage <n> — <name>** — blocked by: <the specific unmet condition>

## Blocked on a human decision
- <decision> — why it blocks: <what cannot proceed> — who: <the adopter>

## Drift
- <YYYY-MM-DD> — <section 6's observation for that run, with its count and the open action next to it, or: no briefings yet — nothing to compare against>
```

`Delivery check` records the answer to the question in section 4 the moment it is asked — confirmed or not — **as a log of the last answer and the date it was given, and nothing more.** It is not a cache, and reading it is not a substitute for asking. Section 4's rule is unconditional: the question is put to the adopter on every run, and this line is overwritten with what they say this run, even when the answer is word for word what it was last time. A run that writes this line without having asked has recorded a fact it did not check.

Every bullet under **Open now** names a real action drawn from what's actually in the pack — which specific room from `recon.md` to enter next, which specific asset to build — never the stage table's one-line description restated as if restating it were an action. `skill:` names the sibling that actually does it, `raid-*` or, where FORTRESS is present, `fortress-*`, so the founder knows where to go, not just what to do. The one action that has no RAID sibling is stage 0's owned asset — write it exactly as section 2 specifies, `skill: fortress-motte` where FORTRESS is installed and `skill: none — the adopter's own work, recorded in motte.md` where it is not. Naming a skill that would not actually do it sends the founder somewhere that cannot help them, which is worse than naming none. `done when:` is a condition checkable against the pack next run — the same discipline the gates themselves use, not a feeling of being finished.

## 9. What this does not do

This does not publish, schedule, or send anything — RAID stages, it never publishes; see the staging rule in `raid`. It does not fetch numbers — `numbers.md` is written by a human or a companion with credentials, never by this skill. And it does not promise a result: a stage being open is a statement about what the pack justifies doing next, not a forecast of what doing it will produce.

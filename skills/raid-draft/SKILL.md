---
name: raid-draft
description: Use when writing the post, drafting the comment, making the launch copy, turning something into a thread, writing the email, or writing a landing section. Produces a paste-ready draft in which every factual sentence traces to a cleared claim, for a room whose rules were read.
---

# raid-draft

Never fight where the money wins. Money buys reach. It does not buy a sentence that survives being checked, and it cannot buy back an account banned for a link nobody was allowed to post. This skill writes the copy — the post, the comment, the thread, the email, the landing section — and writes it so that every factual sentence in it traces to something already cleared, aimed at a room whose rules were actually read, at a stage that is actually open.

It is the place the whole system is most likely to break. Every other skill decides, checks, or records. This one *produces text*, under pressure to produce something good, at the exact moment a plausible number would make the copy land better. That is why the rules below are hard rules and not preferences.

## 1. What it reads, and what each contributes

Read the pack fresh on every run. Never draft from memory of a file — the register may have changed since, and a claim cleared last week may have been moved.

| File | What the draft takes from it |
|---|---|
| `.monkeys/truth.md` | Every factual sentence. **Only lines under `## Cleared` may appear in the draft. Nothing from `## Uncleared`, ever.** |
| `.monkeys/recon.md` | The pain, in the audience's own words, and the destination room's `rules:` and `entry cost:`. |
| `.monkeys/asymmetry.md` | The angle — which ground to stand on. **Internal only: never name a rival in the output.** |
| `.monkeys/motte.md` | Where a link, if there is one at all, should point. |
| `.monkeys/bailey.md` | The destination account's `standing:` and `links allowed:`. |
| `.monkeys/campaign.md` | The open stage, which decides what kind of piece is even appropriate. |
| `.monkeys/voice.md` | How it should sound, and which proof can actually be shown. |

A missing file reads exactly the same as an empty one — that is the pack's rule, and it is never a licence to fill the gap from imagination. A missing or empty `truth.md` means **nothing is cleared**, which means the draft carries no factual sentences at all. Say that plainly and produce the piece that is still possible without them; do not produce the factual version by supplying the facts yourself.

`recon.md` is research and never copy. Borrow the *phrasing* of a pain — the words people actually use for it — never a captured quote reproduced as though someone said it to you, and never a real person's words attributed to them anywhere a stranger can read it.

## 2. Every factual sentence traces to a Cleared line, or it does not go in

Not "should trace." Traces.

**The claim map is the proof, and a draft whose map is incomplete is not finished.** After writing, walk the draft sentence by sentence. Every sentence making a factual assertion about the product, the market, a number, a capability, a date, or an outcome gets a line under **Claims used**, naming the exact `truth.md` line it came from. A sentence you cannot map is a sentence that comes out — not a sentence to note as a caveat and leave in.

If the draft needs a claim that is not cleared, the answer is to **say so and write around it**, never to write it anyway and flag it afterward. Copy is not a draft-and-fix medium: a flagged claim in a paste block is one careless paste away from being published, and the flag does not travel with the text. Write the piece that is true with what is cleared, and name what it could not say and why under **Claims deliberately avoided**, carrying that entry's own recorded `— reason:` from `## Uncleared` verbatim rather than a summary of it.

A claim that would have helped and is not cleared is not a problem with this skill. It is a piece of information for whoever owns the register — where `FORTRESS` is present, `fortress-truth` — telling them exactly which fact is worth going and sourcing.

## 3. Never invent a number, a testimonial, a name, or a statistic

This is the thing the whole system exists to prevent, and a content generator is the single most likely place to breach it.

- **No number that is not in `## Cleared`.** Not as a placeholder, not as "roughly", not rounded down to feel safer, not "to be confirmed before sending." A placeholder number in a paste block is an invented number with a promise attached, and the promise is not in the text.
- **No testimonial.** A quote nobody gave you is a fabricated testimonial however plausibly it reads, and a paraphrase of a real complaint dressed as praise is the same thing with more steps.
- **No named person, customer, or third party** — not as a user, not as an endorser, not as an example.
- **No rival named.** `asymmetry.md` is internal ammunition for choosing where to stand. Stand on the ground; never name who cannot follow you onto it. Say what is true about your own offer, and let the contrast be the reader's.

Where copy needs proof, take it from `voice.md`'s `## Proof available` — things that exist and can be shown. A proof asset nobody has made yet cannot be offered in a draft.

## 4. The stage decides the form

Read `campaign.md`'s open stage before choosing what to write. The stage does not merely suggest a tone; it determines what kind of piece is legitimate at all.

| Open stage | What this skill writes |
|---|---|
| 0 · Foundation | Nothing outward. There is no audience-facing piece at stage 0 — say so and route to `raid-campaign`. |
| 1 · Standing | A genuinely useful comment or answer. **No link. No product mention that isn't asked for.** |
| 2 · First artifacts | The substantial piece itself, published on owned ground, and cuts of it. |
| 3 · First links | Copy that may carry a link to the motte, where the room and the account both allow it. |
| 4 · Prune | Copy for what actually worked, and nothing new for what didn't. |

Asked for stage-3 copy while stage 1 is open, do what `raid-campaign` does: say which stage the request belongs to, which condition is unmet, and what the open stage makes available instead. If the adopter asks again, say it once more and then write it — it is their business to overrule a gate — and mark plainly on the draft that it was written for a stage that is not open.

## 5. A link is a permission, not a preference

**A draft may not contain a link when `bailey.md` says the destination account's `links allowed:` is `no`.** Not a shortened link, not a bare domain, not "it's in my bio", not the product's name written where a search would find it in one step. That is how accounts get banned, and a ban is permanent confiscation of the best ground the adopter had.

The same holds when the room's own `rules:` in `recon.md` forbid links or self-promotion, regardless of what the account's standing says — both have to allow it, and the stricter one wins. Where either field reads `unknown — not verified`, treat it as `no`: an unread rule is not permission, and assuming one is exactly how the ban happens.

Where a link *is* allowed, it points at the motte — something the adopter owns — never at a second rented platform. A link from one piece of rented ground to another produces engagement someone else keeps.

## 6. Voice, and the empty voice file

`voice.md` says how the brand sounds, what it never says, and what proof it can actually show. Use it.

**Where `voice.md` is absent or empty, say the draft has no voice guidance. Do not invent a house style.** A confident brand voice conjured out of nothing is as much a fabrication as an invented statistic — it just fails less visibly, because nobody can check a tone against a source. Write plainly, note in the handover that the piece is in a neutral voice for want of a `voice.md`, and point at the file as the thing to fill in.

The same discipline binds `## Never says`. A word or move recorded there is out of the draft, including where it would have been the strongest line — that entry exists because using it costs something, and the cost was written down next to it.

## 7. Lint before handing over

Where `tools/monkeys/claim_lint.py` is present in the adopter's repo — it is installed by `fortress-truth` where `FORTRESS` is present — write the draft to a file and run it before handing anything over:

```bash
python tools/monkeys/claim_lint.py <path-to-draft>
```

Report the result in the handover: the exit code, and every finding, in full. **Do not hand over copy you have not checked**, and do not quietly re-word a flagged sentence and re-run until it passes without saying so — a claim that had to be softened to clear the linter is a claim worth telling the adopter about.

A clean run is not proof the copy is true. The linter flags claim-shaped language; the register arbitrates. A green run means nothing in the draft looks like an unsourced claim — it is not a verdict on whether the sourced ones are correct.

Where the linter is not present, say so plainly and hand over the claim map instead. **The claim map is the check; the linter is a second pair of eyes on it.** The map is produced on every run either way, and a run without the script is not a run without a check.

## 8. Staged, never sent

RAID never publishes. It stages. This skill produces text a **human** sends, and the handover is finished when the human has everything they need to send it — not when the agent has posted it.

Every draft ends with the send checklist below, unticked. The agent does not tick it. Where `FORTRESS` is present, `fortress-gate` owns the send and this skill defers to it; where it is not, this rule still binds, because it is RAID's own.

## 9. The output

One complete unit, never a recommendation the human still has to turn into something:

```markdown
## Draft
<the copy, ready to paste>

## Claims used
- <claim> — source: <the exact truth.md line it came from>

## Claims deliberately avoided
- <uncleared claim that would have helped> — reason: <its recorded reason>

## Room fit
- destination: <room>  · rules: <what that room forbids>  · links allowed: <yes|no>  · standing: <cold|warming|established>

## Human send checklist
- [ ] claim lint passed
- [ ] no rival named
- [ ] room's rules re-read today
- [ ] a human is sending this
```

**Claims used** is empty only when the draft makes no factual assertion at all, and saying so explicitly is better than an empty heading. **Claims deliberately avoided** is empty only when nothing was left out; where it is empty, say that too, so an incomplete pass is never mistaken for a clean one. **Room fit** is filled from `recon.md`'s room line and `bailey.md`'s account line together — never from what rooms of that kind usually allow.

## 10. What this does not do

- **It does not publish, and it does not schedule.** See section 8.
- **It does not design.** Layout, artwork, video and shot lists are not this skill's output; `raid-multiply` cuts an existing asset and decides its formats.
- **It does not research.** If the pain language is missing from `recon.md`, this skill does not go and invent phrasing for it — route to `raid-recon` and come back. If an incumbent's ground is unread, route to `raid-asymmetry`.
- **It does not source claims.** It reads the register; it never adds a line to it. Where `FORTRESS` is present, `fortress-truth` owns that.

Route out where the ask is really something else: `raid-recon` where the audience's own words are missing, `raid-multiply` where the ask is "cut this one asset into many", `raid-campaign` where the question is which stage is open, and `raid-borrow` where the question is which room this belongs in at all.

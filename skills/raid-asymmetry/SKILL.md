---
name: raid-asymmetry
description: Use when finding an angle against a competitor, deciding what to lead with, or looking for defensible ground. Writes the Incumbents and Our ground sections of the asymmetry pack.
---

# raid-asymmetry

Never fight where the money wins. This is RAID's sharpest skill, because it doesn't attack an incumbent — it reads the shape of the ground their own business forces them to stand on, and finds where that ground doesn't reach.

## 1. The method

An incumbent's revenue model is not a detail about them. It is terrain, and it is the one piece of terrain they cannot move to match you, because moving it means becoming a different company.

Read how they make money, then derive what that model **forbids them to say**:

- A subscription company cannot credibly say "one-time price" — recurring revenue is the business.
- An ad-funded product cannot say "your data stays on your machine" — the data is the product.
- A venture-funded company cannot credibly promise it will still exist, unchanged, in five years — the fund has a horizon and the company answers to it.
- A marketplace that takes a cut cannot say "we have no stake in which side wins" — the cut depends on volume, and volume has a direction.

None of this is a guess about their character. It follows from the model itself, the way a load-bearing wall follows from where the weight sits.

## 2. Steps, in order

1. **Identify the incumbent's revenue model from their own public sources** — their pricing page, their own site, their own investor or "about" page if they have one. A third-party summary or comparison article is not a source for this; it's a summary of someone else's read, and it can be wrong in exactly the way that breaks the method below.
2. **List what that model structurally prevents them from saying.** Not what they haven't gotten around to saying — what they cannot say without contradicting how they make money.
3. **Check which of those the adopter can honestly claim.** This is the filter. A claim only belongs on "our ground" if it's true of the adopter, not just untrue of the incumbent.
4. **Record both sides** in `.monkeys/asymmetry.md`, in the shape the front door established:

```markdown
## Incumbents
- <incumbent> — revenue model: <how they make money> — therefore cannot say: <the claim their model forbids>

## Our ground
- <the claim we can make that they structurally cannot> — because: <their model constraint>
```

If the incumbent's own pricing or plans page can't be located and confirmed the same way — their own site, not a review aggregator — write `revenue model: unknown — not verified` and stop there. Do not infer a model from vibes, category, or reputation. A guessed revenue model is exactly the invented claim this method exists to avoid, and it poisons everything derived from it.

## 3. Two hard rules

**`asymmetry.md` is internal. Never name a rival in public copy.** Nothing in this file — no incumbent name, no direct comparison — goes into anything a stranger can read: no landing page, no post, no store listing. Public copy claims the category and demonstrates the ground; it does not point at a name. Where `FORTRESS` is installed, naming a rival in public copy is one of its violations, and `fortress-truth`'s claim discipline binds this output whether or not FORTRESS is present.

**A structural constraint is not a moral failing.** The incumbent didn't lie by building a subscription business, and copy that implies they did is a cheap shot that also happens to be inaccurate — they made a different trade, for reasons that made sense to them. Say what you can honestly do that they structurally cannot, and stop there. The asymmetry is the argument. It doesn't need an insult stapled to it, and an insult is the fastest way to make the honest claim look like spin.

## 4. What this doesn't decide

This file sharpens private judgment about where to stand. It does not write the public claim — that's copy, bound by `fortress-truth` where present, and it does not decide whether the moment is right to say it — that's `raid-moment`.

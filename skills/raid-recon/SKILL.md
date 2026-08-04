---
name: raid-recon
description: Use when researching an audience, finding where a market gathers, or capturing how people describe a problem. Writes the Pains and Rooms sections of the recon pack.
---

# raid-recon

Never fight where the money wins. Recon is how you find the ground worth taking: the pain in people's own words, and the rooms where those people already are.

## 1. Their words, not yours

The pain goes into `.monkeys/recon.md` in the phrasing the audience actually used — not translated into your product's vocabulary, not cleaned up, not made to sound like a value proposition. The words they use are the words that will reach them. If they said "I keep losing track of who I already emailed," write that. Don't write "poor contact management" over it — that's a category, not a pain, and nobody searches or vents in categories.

**A pain you paraphrased is a pain you invented.** Quote, don't summarise. If you only have a summary, go back and find the actual sentence, or mark it unverified until you do.

## 2. Two hard rules

**`recon.md` is internal. Quotes captured there are research, never copy.** Nothing in this file is republished as marketing. Never put a real person's words into public material, never attribute a phrase to a named individual anywhere a stranger can read it, and never present captured phrasing as a testimonial — it is not one, and dressing it as one does not make it one.

**Record where a pain was heard, not who said it.** The `heard in:` field takes a room, not a handle, not a username, not a real name, not a link to the individual post. You need the phrasing, not the person; the phrasing is the entire value of the capture, and the identity is the entire liability.

The reason is plain. Those people did not consent to being your marketing — they were describing a problem to their own community, not endorsing a product to yours. **A testimonial you did not receive is a fabricated testimonial**, however accurately you transcribed the sentence. And the person whose words you lifted is the one most able to say so in public, in the room where you took them, to the audience you were trying to reach.

## 3. Read the room before you enter it

A room is a forum, a subreddit, a newsletter's reply-all culture, a local meetup — anywhere with a name and a norm. Before treating a room as ground to stand on, record:

- who is actually there (not who you wish were there)
- what the room forbids — self-promotion bans, flair requirements, karma thresholds, a "no vendors" rule enforced by the mods
- what it costs to be welcome — days of participating before posting, a specific format, an introduction ritual

Skipping this step is how a raid becomes a ban. The rules and the entry cost are not friction to note in passing; they are the terrain, same as an incumbent's revenue model is terrain for `raid-asymmetry`.

## 4. Verify what you can, mark what you can't

Community sizes, member counts, and "most active" claims are usually third-party numbers, and they frequently contradict each other — a subreddit's sidebar, a directory listing, and the platform's own API can each report a different figure for the same room. Don't average them, don't pick the flattering one, and don't state one as fact from memory.

Every pain and every room gets a `verified` field:

- `verified: yes` — you found the exact phrase or the room's activity at the source, this session.
- `verified: no` — the adopter told you, or you found a secondhand mention, but you have not confirmed it at the source.

An unverified entry still belongs in the file. Guessing at verification to make the pack look more solid is worse than an honest `no` — it hides exactly the thing a later skill needs to know before it builds a claim on top of it.

## 5. Write the file

Append to `.monkeys/recon.md` at the adopter's repo root, in the shape the front door already established:

```markdown
## Pains
- <the pain in their own words> — heard in: <where> — verified: <yes|no>

## Rooms
- <community or room> — audience: <who is there> — rules: <what they forbid> — entry cost: <what it takes to be welcome>
```

Add lines; don't rewrite lines someone else already verified. If a new pain contradicts one already in the file, keep both and let the contradiction show — that's real signal, not noise to resolve by deleting one.

## 6. What this doesn't decide

Recon finds the pain and the room. It does not decide what to say about a competitor (`raid-asymmetry`), what to do in the room (`raid-stunt`, `raid-borrow`), or when (`raid-moment`). Hand the file off; don't reach past it.

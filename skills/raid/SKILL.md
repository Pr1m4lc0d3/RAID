---
name: raid
description: RAID front door. Never fight where the money wins. Use when starting marketing work with no budget, deciding where to promote something, finding an angle against a competitor, or entering the RAID discipline for the first time — runs kickoff once and routes to the six focused sub-skills.
---

# raid

This is the front door. It holds the doctrine, the gate you run before committing effort to any play, the one-time kickoff that builds a recon-and-asymmetry pack from the adopter's own product and market, and the routing table to the six focused skills that do the actual work. Read this once per adoption; route out of it for everything after.

## 1. The doctrine

Never fight where the money wins.

One test generates the entire target list. Ads? Money wins — stay out. Head SEO terms? Money wins. Paid placement, sponsorships, booths, influencer rates? Money wins. So *where doesn't it?* Surprise, timing, niche depth, trust, weirdness, physical space, and being genuinely useful in a room you don't own.

RAID is the offensive half of guerrilla marketing for AI agents. It doesn't tell you what to hold on to — that's the defense half, `FORTRESS`. It tells you where a small force can actually win, and where showing up is just money you don't have competing with money you'll never match.

## 2. Disproportion or don't bother

A stunt nobody carries is just a weird thing you did.

Guerrilla marketing's whole trade is disproportion: a small input that produces an outsized effect because someone else carries the message for free. That is not a bonus feature — it is the corollary that keeps this discipline from tipping into vandalism, prank content, or noise nobody asked for. Before committing effort to any play, ask what the gate below asks in full: *if this works, who repeats it, and why is repeating it in their interest?* If the honest answer is nobody, don't build it. Working out exactly why, and what to build instead, is `raid-stunt`'s job — the front door only filters at the door.

## 3. The target gate

Before committing effort to any play, run this gate in order:

| Measure | Skill |
|---|---|
| Does money win on this ground? If yes, walk away. | `raid` |
| Who exactly hurts here, and in whose words? | `raid-recon` |
| What can the incumbent **structurally not say** because of how they make money? | `raid-asymmetry` |
| If this works, **who carries it for free?** | `raid-stunt` |
| Is attention already in motion I can ride instead of manufacturing? | `raid-moment` |
| Does this room already have the audience, so I don't have to build one? | `raid-borrow` |
| Does this asset already exist in another form? | `raid-multiply` |

*If nothing carries it and nothing is disproportionate, it is not a raid — it is just work.*

## 4. Kickoff

Run this once, the first time RAID is adopted into a repo. If `.monkeys/recon.md` or `.monkeys/asymmetry.md` already exists, don't overwrite silently — read what's there back to the adopter and ask whether to extend it or start over.

State this plainly before starting, and mean it: **nothing here is pre-filled.** Every pain, room, incumbent and claim in the generated pack comes from this adopter's own product and market, gathered by interview and checked against public sources. A generic template with plausible-looking example pains would be exactly the invented-evidence problem RAID exists to avoid — shipping one would make kickoff itself the first violation of the doctrine.

Two roots are in play throughout these steps:

- **Plugin root** — where this plugin is installed. Address it with `${CLAUDE_PLUGIN_ROOT}`; the capability report in section 5 reads `companions.json` from here.
- **Adopter's repo root** — the directory you are working in. Both files you *write* — `.monkeys/recon.md`, `.monkeys/asymmetry.md` — are relative to it.

Steps, in order:

1. **Interview the adopter.** Ask, one question at a time:
   - Product name and a one-line description.
   - Who hurts without it, and what they've actually said about the problem — in their own words, not the product's.
   - Where those people already gather — forums, subreddits, newsletters, local meetups, anywhere with a name.
   - Named incumbents or competitors worth researching. (These names are research targets only — see the rule below.)

2. **Fetch public sources.** Use WebSearch to find where the pains above show up in public and to confirm the rooms named actually exist and are active. Use WebFetch on each incumbent's pricing or plans page to determine how they make money. A pain or room the adopter names but that can't be found or confirmed publicly still goes in the pack — mark it `verified: no` rather than dropping it or inventing a source for it.

3. **Write `.monkeys/recon.md`** (adopter's repo root), in exactly this shape — this is a contract `raid-recon` and every other sibling reads:

   ```markdown
   # Recon — who hurts, and where

   ## Pains
   - <the pain in their own words> — heard in: <where> — verified: <yes|no>

   ## Rooms
   - <community or room> — audience: <who is there> — rules: <what they forbid> — entry cost: <what it takes to be welcome>
   ```

4. **Write `.monkeys/asymmetry.md`** (adopter's repo root), in exactly this shape — this is a contract `raid-asymmetry` reads:

   ```markdown
   # Asymmetry — ground they cannot hold

   ## Incumbents
   - <incumbent> — revenue model: <how they make money> — therefore cannot say: <the claim their model forbids>

   ## Our ground
   - <the claim we can make that they structurally cannot> — because: <their model constraint>
   ```

   **This file is internal ammunition and is never published.** Naming a rival in public copy — anywhere a stranger can read it — is a `FORTRESS` violation. It exists to sharpen private judgment about where to stand, not to write attack copy.

5. **Report back** what was written, and state plainly that every pain traces to something the adopter said or something independently found in public, and every asymmetry claim traces to a fetched pricing or plans page — nothing was invented to fill space.

## 5. Capability report

Read `companions.json` at the plugin root. For each entry, check the filesystem for whether its provider is already available, and report the result **by capability**, not by tool name — never the name of a specific package or service. Offer to install a missing one only when the adopter explicitly consents; never install anything silently.

As shipped, `companions.json` is empty — RAID needs no add-ons to produce any of its deliverables. Report exactly: **"No optional capabilities needed — RAID runs entirely on built-in tools."** If a future entry is ever added, report it as an available accelerant, never as a missing requirement — every RAID skill produces its full deliverable without one.

## 6. Routing table

| Moment | Skill |
|---|---|
| About to spend effort and unsure whether money already wins on this ground | `raid` |
| Researching an audience, or finding where a market gathers | `raid-recon` |
| Finding an angle against a competitor, or deciding what to lead with | `raid-asymmetry` |
| Designing a launch, or wanting attention without a budget | `raid-stunt` |
| Reacting to news, timing a launch, or deciding whether now is the moment | `raid-moment` |
| Looking for an audience, or considering a podcast, newsletter, or community | `raid-borrow` |
| Having made one asset, planning content, or wanting more output without more work | `raid-multiply` |

## 7. The pairing

RAID takes ground; `FORTRESS` holds it and governs what may be claimed. The two are one doctrine split by function, not two unrelated systems that happen to share a repo owner.

RAID is fully usable alone — every skill it routes to produces its complete deliverable on RAID's own pack, with no dependency on FORTRESS being installed. But where FORTRESS **is** present, its claim discipline binds every RAID output without exception. **A stunt is not exempt from the truth register.** The loudest play RAID can design is exactly the one most likely to be checked, screenshotted, and quoted back — and `fortress-truth` grants no carve-out for something that worked.

## 8. Built-ins only

Every skill in this plugin — this one and all six it routes to — runs on WebSearch, WebFetch, Read/Write/Edit, Glob/Grep, and Bash. Nothing here assumes any other plugin is installed, including FORTRESS. Section 5's capability report exists because an accelerant is worth naming when one happens to be available — not because RAID needs one to function.

---
name: raid
description: RAID front door. Never fight where the money wins. Use when starting marketing work with no budget, deciding where to promote something, finding an angle against a competitor, or entering the RAID discipline for the first time — runs kickoff once and routes to the eight focused sub-skills.
---

# raid

This is the front door. It holds the doctrine, the gate you run before committing effort to any play, the one-time kickoff that builds a recon-and-asymmetry pack from the adopter's own product and market, and the routing table to the eight focused skills that do the actual work. Read this once per adoption; route out of it for everything after.

## 1. The doctrine

Never fight where the money wins.

One test generates the entire target list. Ads? Money wins — stay out. Head SEO terms? Money wins. Paid placement, sponsorships, booths, influencer rates? Money wins. So *where doesn't it?* Surprise, timing, niche depth, trust, weirdness, physical space, and being genuinely useful in a room you don't own.

RAID is the offensive half of guerrilla marketing for AI agents. It doesn't tell you what to hold on to — that's the defense half, `FORTRESS`. It tells you where a small force can actually win, and where showing up is just money you don't have competing with money you'll never match.

## 2. Disproportion or don't bother

A stunt nobody carries is just a weird thing you did.

Guerrilla marketing's whole trade is disproportion: a small input that produces an outsized effect because someone else carries the message for free. That is not a bonus feature — it is the corollary that keeps this discipline from tipping into vandalism, prank content, or noise nobody asked for. Before committing effort to any play, ask what the gate below asks in full: *if this works, who repeats it, and why is repeating it in their interest?* If the honest answer is nobody, don't build it. Working out exactly why, and what to build instead, is `raid-stunt`'s job — the front door only filters at the door.

## 3. RAID never publishes. It stages.

RAID produces drafts, plans, target lists, cuts and copy. It does not post, comment, submit, send, or publish, and it does not perform an outward action on anyone's behalf. Every outward action is a human's, taken deliberately, with the material in front of them.

**The output of any RAID skill is something a human sends, not something the agent sends.** Hand over a paste block, a draft, a list, a shot list — never a completed action. "I posted it" is outside the scope of every skill in this plugin. "Here is the post, here is the room, here is the rule you are subject to there" is the finished deliverable, not a partial one.

This is doctrine, not a limitation, and it is not a capability gap waiting to be closed. Handing a human a paste block requires no tools at all, which is exactly why it works on built-ins alone — there is nothing to install, nothing to authorise, and nothing to wait for.

The reason is worth stating plainly, because it is what makes the rest of this plugin hold. **Every floor in RAID — the conduct rules, the legality floor, the naming rule, the consent rule — is enforced by the agent's own judgement, at the moment that judgement is under the most pressure to produce a result.** That is the worst possible moment for it to be the only check. A human between the draft and the send is the one check that does not share the pressure. The floors reduce the damage an agent can do; the gate is what makes them hold.

Where `FORTRESS` is installed, `fortress-gate` owns this and RAID defers to it. Where it is not installed, **this rule still binds.** It is RAID's own rule, not one borrowed from a plugin that may not be there.

## 4. The target gate

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
| Is this stage even open yet? | `raid-campaign` |
| Is this a draft a **human** sends — or am I about to send it myself? If I am sending, stop. | `raid` |

*If nothing carries it and nothing is disproportionate, it is not a raid — it is just work. And if the agent is the one hitting send, it is not a raid either — it is an unreviewed action taken in someone else's name.*

## 5. Kickoff

Run this once, the first time RAID is adopted into a repo. If `.monkeys/recon.md` or `.monkeys/asymmetry.md` already exists, don't overwrite silently — read what's there back to the adopter and ask whether to extend it or start over.

State this plainly before starting, and mean it: **nothing here is pre-filled.** Every pain, room, incumbent and claim in the generated pack comes from this adopter's own product and market, gathered by interview and checked against public sources. A generic template with plausible-looking example pains would be exactly the invented-evidence problem RAID exists to avoid — shipping one would make kickoff itself the first violation of the doctrine.

Two roots are in play throughout these steps:

- **Plugin root** — where this plugin is installed. Address it with `${CLAUDE_PLUGIN_ROOT}`; the capability report in section 6 reads `companions.json` from here.
- **Adopter's repo root** — the directory you are working in. Every file you *write* — `.monkeys/recon.md`, `.monkeys/asymmetry.md`, and, each only where it is absent, `.monkeys/truth.md`, `.monkeys/motte.md`, `.monkeys/bailey.md`, `.monkeys/scars.md` and `.monkeys/numbers.md`, plus `.monkeys/sell-kit.md` where a Sell-Kit was imported — is relative to it.

**The pack is the interface, not the plugin.** `raid-campaign`'s gates read `truth.md`, `motte.md` and `bailey.md`, and a missing file reads the same as an empty one — so an adopter who installs RAID alone and has none of those files is pinned at stage 0 with nothing in RAID able to change it. Kickoff therefore creates every pack file RAID's own gates read, **only where it is absent**. Whoever arrives first creates a file; each plugin owns the *discipline* for its own files; neither is blocked by the other's absence.

Where `FORTRESS` is installed, `fortress-truth`, `fortress-motte` and `fortress-bailey` own those three files — RAID only guarantees they exist, never touches one that is already there, and never claims the discipline behind them. Run FORTRESS's kickoff first where you intend to install both: FORTRESS treats an existing `truth.md` as a retrofit rather than a clean start.

Steps, in order:

1. **Ask whether there is a Sell-Kit, and read it if there is.** Ask one question and wait for the answer: *"Do you have a Sell-Kit from Idea Forge Pro?"*

   If the answer is no, skip the rest of this step. Nothing else in kickoff changes — the interview below is the whole of it, exactly as it was before this step existed. **A Sell-Kit is never required.** Idea Forge Pro (ideaforgepro.com) is a separate, free, bring-your-own-API-key tool that runs a startup idea through seven gates and exports a Sell-Kit: `<name>-sell-kit.md`, plus a `<name>-forge.json` holding the same data typed. It is optional in exactly the way `FORTRESS` is optional here — RAID runs with no Sell-Kit, no Idea Forge Pro, and no internet beyond the built-in WebSearch and WebFetch.

   If the answer is yes, ask for the path. Where both files exist, read the **`-forge.json`** — it is typed, so nothing is lost to formatting — and fall back to the `-sell-kit.md` where that is the only one. A kit may carry any subset of its fields; an absent field is absent.

   Before a single field moves anywhere, the rule that governs the whole import:

   > **A Sell-Kit field never enters `## Cleared` unless its evidence grade earns it.**

   A Sell-Kit is largely written by a model from what a founder typed into it. Importing that prose into a truth register as fact would inject model-written claims into the exact place that exists to keep them out — and the claim linter would then pass them forever, because a line that *looks* sourced is all a script can check. **The default for anything without a grade is Uncleared.**

   The kit's claim register carries one line per claim with an evidence grade: **A** attested · **B** observed · **C** public principle · **D** analogy · **E** founder assertion · **F** generated. Its own rule is that anything generated is F and **cannot be raised** — not by argument, not by the founder wanting it, and not by this import.

   Map it exactly. Nothing here creates a file; hold the mapped lines and write them when the steps below write the files themselves.

   | From the kit | Goes to | Carrying |
   |---|---|---|
   | `What is known` | `truth.md` `## Cleared` | the source the kit names, as ` — source: <exact source>` |
   | `What is hypothesized` | `truth.md` `## Uncleared` | ` — reason: hypothesis, not established` |
   | claim register, graded **A/B/C/D** | `truth.md` `## Cleared` | ` — source: <the source the register names>` |
   | claim register, graded **E** | `truth.md` `## Uncleared` | ` — reason: founder assertion, no source` |
   | claim register, graded **F** | `truth.md` `## Uncleared` | ` — reason: model-written, cannot be raised` |
   | `Problem` | `recon.md` `## Pains` | already in the buyer's own words — see the `verified:` rule below |
   | entities `Reality status` marks real | `asymmetry.md` `## Incumbents` | `revenue model: unknown — not verified` |
   | the pre-build test fields | `.monkeys/sell-kit.md` | see the step that writes it |
   | **every other field** | `truth.md` `## Uncleared` | ` — reason: from a Sell-Kit, ungraded` |

   The rules that make that table hold, each one the place the import goes wrong if it is softened:

   - **`What is known` is the only field that arrives already eligible for Cleared**, because that is its own definition inside the kit: facts directly supplied by the founder or independently supported, nothing generated. It still needs a ` — source:` suffix. Where the kit doesn't name one, **ask the adopter**; if they can't name one either, it goes to **Uncleared** instead — ` — reason: no source named`. All of this applies **only where this kickoff is creating `truth.md`**; where the file is already there it is left exactly as it is, and the mapped lines are handed to the adopter in the report instead of written.
   - **Every other field goes to Uncleared unless the claim register grades it A–D.** `Buyer`, `Problem`, `Why now`, `Offer`, `Price`, `Value artifact`, `Channel`, `Intent signal` — all of it. **A price a model proposed is not a fact about the world.**
   - **The `Problem` becomes one `## Pains` entry**, with `heard in: <where the kit says it was heard>` where the kit says, and `heard in: Sell-Kit — not independently found` where it doesn't. **`verified:` is `no` unless the claim register grades that same claim A or B.** The public search in the next step can raise it exactly as it raises any other pain; the kit alone never does.
   - **Nothing from the kit goes into `## Rooms`. Nothing.** The kit's `Channel` is a channel *type* — "a forum", "a newsletter" — not a named room with rules, an audience and an entry cost. Rooms still require research, and that research is `raid-recon`'s job and the next step's. **Entering a room on assumed rules is how an account gets banned**, and a room invented from a channel type arrives with all three of its fields guessed at once.
   - **Never infer a revenue model from a kit.** Each incumbent the kit's `Reality status` marks real lands as `revenue model: unknown — not verified` and `therefore cannot say: unknown — follows from the revenue model, not yet fetched`, and stays that way until `raid-asymmetry` fetches that incumbent's own pricing or plans page. Nothing goes under `## Our ground`: it derives from a model nobody has read yet.

   Ignore the kit's builder spec entirely — `Acceptance criteria`, `Must nail`, `Out of scope (v1)`. Those describe what to build, not where to fight, and nothing in RAID reads them.

   **Never fabricate a field the kit lacks.** An absent field is absent: ask for it in the interview, or leave it out. Then run the interview below asking only for what the kit did not answer, and confirming — not re-asking — what it did.

2. **Interview the adopter.** Ask, one question at a time:
   - Product name and a one-line description.
   - Who hurts without it, and what they've actually said about the problem — in their own words, not the product's.
   - Where those people already gather — forums, subreddits, newsletters, local meetups, anywhere with a name.
   - Named incumbents or competitors worth researching, and — exactly as you'd ask for a canonical source — their pricing or plans page URL where the adopter already knows it. (These names are research targets only — see the rule below.)
   - **One thing about the product they could hand a stranger a source for** — a fact, a number, a capability, a date — and where that source is: a URL, a document, a repo, a receipt. One is enough. This is the fact that opens stage 1, so ask for it plainly and ask where it can be checked. If they have nothing they can source yet, that is a real answer: record it, don't press, and never supply one for them. A founder with nothing sourceable is at stage 0, and saying so is the honest result.

3. **Fetch public sources.** Use WebSearch to find where the pains above show up in public and to confirm the rooms named actually exist and are active. For each incumbent: if the adopter supplied a URL, WebFetch it directly. If not, WebSearch for the incumbent's own site and locate its own pricing or plans page there, then WebFetch that page. **A third-party summary, review site, or comparison page is not an acceptable source for what a competitor charges** — go to the incumbent's own page, or treat it as not found. A pain or room the adopter names but that can't be found or confirmed publicly still goes in the pack — mark it `verified: no` rather than dropping it or inventing a source for it. An incumbent whose own pricing page can't be located the same way goes into `asymmetry.md` with `revenue model: unknown — not verified` — never a guessed or inferred model. Guessing the revenue model is inventing the very claim this skill exists to source: the whole asymmetry method collapses if the model is wrong.

   **The same discipline binds `recon.md`'s `rules:` and `audience:` fields, and it is not softer there.** A room whose own rules page, sidebar, or pinned posting policy was not actually read has `rules: unknown — not verified`. A room whose make-up was not read off the room itself has `audience: unknown — not verified`. Neither field is ever filled in from what rooms of that kind *usually* forbid or *usually* contain, and a search-result summary describing a room is not a reading of the room. Entering a room on assumed rules is how an account gets banned, and a ban is permanent — the assumption becomes invisible the moment it is written into the pack as a fact, which is exactly why it has to be refused at the point of writing.

   **Where a source cannot be fetched at all** — a host that refuses the fetch, a dead link, a page that will not render — WebSearch for the same information instead. If the search also fails to establish it, record `verified: no` with the reason and name what could not be reached. An unfetchable source is never read as confirmation and never read as proof the thing does not exist; both of those invent a result this run did not produce.

   **Check the adopter's one sourceable fact against the source they named**, by WebFetch for a URL or Read for a local document, exactly as an incumbent's pricing is checked against their own page. It clears only if the source actually says it.

4. **Write `.monkeys/recon.md`** (adopter's repo root), in exactly this shape — this is a contract `raid-recon` and every other sibling reads:

   ```markdown
   # Recon — who hurts, and where

   ## Pains
   - <the pain in their own words> — heard in: <where> — verified: <yes|no>

   ## Rooms
   - <community or room> — audience: <who is there> — rules: <what they forbid> — entry cost: <what it takes to be welcome>
   ```

5. **Write `.monkeys/asymmetry.md`** (adopter's repo root), in exactly this shape — this is a contract `raid-asymmetry` reads:

   ```markdown
   # Asymmetry — ground they cannot hold

   ## Incumbents
   - <incumbent> — revenue model: <how they make money> — therefore cannot say: <the claim their model forbids>

   ## Our ground
   - <the claim we can make that they structurally cannot> — because: <their model constraint>
   ```

   **This file is internal ammunition and is never published.** Naming a rival in public copy — anywhere a stranger can read it — is a RAID violation, and the rule is RAID's own: `raid-asymmetry` states it in full, and it binds in a RAID-only install exactly as it binds anywhere else. Where `FORTRESS` is present it enforces the same rule, as reinforcement and never as the source. This file exists to sharpen private judgment about where to stand, not to write attack copy.

6. **Write `.monkeys/truth.md` — only if it does not already exist** (adopter's repo root). `raid-campaign`'s gate 1 reads this file; without it the staircase never opens. Emit the structure and nothing else — placeholder comments, no example facts:

   ```markdown
   # Truth Register

   Every public claim traces to a line under **Cleared**, or it does not ship.
   Keep the format exactly — the gates read these headings.

   ## Cleared

   <!-- One bullet per fact, in this exact shape. A bullet without the " — source:" -->
   <!-- suffix is malformed: it sources nothing. -->
   <!-- - <the claim, exactly as it will appear in copy> — source: <where this was verified> -->

   ## Uncleared

   <!-- Facts that may NOT be stated publicly without re-verification. -->
   <!-- - <the fact> — reason: <why it is not cleared> -->

   ## Canonical source

   <!-- The URL or location to re-fetch before every copy batch. Never write from memory of it. -->
   ```

   Then write the adopter's own fact from step 2 into it, using what step 3 found. If the named source actually says it, it goes under **Cleared** as `- <the fact> — source: <the exact source>`. If it could not be checked, it goes under **Uncleared** as `- <the fact> — reason: <why it is not cleared>`. This is the adopter's own fact, checked this run against a real source — the same standard every pain in `recon.md` is held to — and it is the opposite of a pre-filled example: nothing here is written that the adopter did not say and the source did not confirm. If the adopter had nothing they could source, both sections stay empty and the report says so. **Never invent a fact, and never move one to Cleared to open a gate** — an empty register is honest, and it means the open stage is 0 until someone with a source changes that.

   If the file is already there, leave it exactly as it is and say so in the report. Where `FORTRESS` is installed, `fortress-truth` owns this file's discipline and adding facts to it is that skill's job, not this one's.

7. **Write `.monkeys/motte.md` — only if it does not already exist** (adopter's repo root). `raid-campaign`'s gate 3 reads `## Held`. Structure only, placeholder comments only, nothing pre-filled:

   ```markdown
   # Motte — what cannot be confiscated

   ## Held

   <!-- One bullet per asset the adopter owns outright. No invented entries. -->
   <!-- An empty Held section is an honest motte, not a placeholder to fill in. -->
   <!-- - <asset> — control: <full|partial> — grows by: <what moves it> -->

   ## Wanted

   <!-- - <asset not yet built> — why: <what it would let you do> -->
   ```

   Leave it empty. Standing up an owned asset is stage 0 work and nothing in RAID performs it — see the routing note in `raid-campaign` section 2. If the file is already there, leave it exactly as it is and say so in the report; where `FORTRESS` is installed, `fortress-motte` owns this file's discipline.

8. **Write `.monkeys/bailey.md` — only if it does not already exist** (adopter's repo root). `raid-campaign`'s gate 2 reads `## Active`, and `raid-briefing` reads the `standing:` field on each line there. Structure only, placeholder comments only, nothing pre-filled:

   ```markdown
   # Bailey — rented ground

   ## Active

   <!-- - <channel> — account: <handle> — joined: <YYYY-MM-DD> — standing: <cold|warming|established> — links allowed: <yes|no> -->

   ## Excluded

   <!-- An exclusion recorded without a reason gets re-proposed every session, forever. -->
   <!-- - <channel> — reason: <why this was ruled out> -->
   ```

   Leave it empty. An account the adopter has not actually created is not an active channel, and writing one in would be the invented-evidence problem wearing a schema. If the file is already there, leave it exactly as it is and say so in the report; where `FORTRESS` is installed, `fortress-bailey` owns this file's discipline.

9. **Write `.monkeys/scars.md` — only if it does not already exist** (adopter's repo root). The adopter's own incident log, started empty: a three-column table plus one line stating it gets filled in after something actually happens, never guessed in advance. If the file is already there, leave it exactly as it is and say so in the report — `FORTRESS` writes this same file where it is installed, and an existing log is someone's real history, not a template to overwrite. This is the adopter's own log, separate from RAID's own `scars.md`, which documents this plugin's history and not theirs.

   ```markdown
   # Scars — what we learned the hard way

   | Incident | Damage | Rule |
   |---|---|---|

   Filled in after something actually happens. Never guessed in advance.
   ```

10. **Write `.monkeys/numbers.md` — only if it does not already exist** (adopter's repo root). The place live numbers enter the pack at all, started empty: a five-column table plus a line stating who fills it in and that an empty table is honest. If the file is already there, leave it exactly as it is and say so in the report — `raid-briefing` writes this same file where kickoff hasn't already, and an existing table may hold real dated rows, not a template to overwrite.

    ```markdown
    # Numbers

    Written by whoever has the credentials. Never fetched by a skill.
    An empty table is honest; an invented row is not.

    | Date | Metric | Kind | Value | Source |
    |---|---|---|---|---|
    ```

    `Kind` is `motte` or `bailey`. The distinction exists because rented attention is not something a founder can prune toward.

11. **Write `.monkeys/sell-kit.md` — only where a Sell-Kit was imported in step 1.** This is where the kit's pre-build test lands, and it is a separate file for a reason worth stating: **it does not go into `campaign.md`.** `raid-campaign` regenerates every section of that file fresh from the pack on each run, carrying forward only override records, blocked-on-a-human entries and dated drift lines — so a first objective written there by kickoff would be silently erased the first time a campaign was planned. Write it here instead, and hand this file to `raid-campaign` when planning: `The ask` becomes the campaign's first objective, `PASS if` and `KILL if` become its kill criteria, `By when` is the date that objective is checked against, `Commitment signal` defines what counts as a real row in `numbers.md`, and `Stop condition` feeds stage 4 — the prune. If the file already exists, read it back to the adopter and ask whether to replace it; a kit imported earlier may have been acted on since.

    ```markdown
    # Sell-Kit — the founder's own pre-build test

    Imported from: <path to the kit> — on: <YYYY-MM-DD>
    Nothing here was verified by this run. It is what the founder brought, recorded so it
    is not re-decided from memory. An absent field is left out, never filled in.

    - The ask: <what the buyer is being asked to do>
    - PASS if: <the condition that counts as a pass>
    - KILL if: <the condition that ends it>
    - By when: <YYYY-MM-DD>
    - Commitment signal: <what counts as a real row in numbers.md>
    - What this test CAN prove: <...>
    - What this test CANNOT prove: <...>
    - Stop condition: <what stops the whole line of work>
    ```

12. **Report back** what was written, and state plainly that every pain traces to something the adopter said or something independently found in public, and every asymmetry claim traces to a fetched pricing or plans page — nothing was invented to fill space. Name each file that was created and each file that was found already present and left alone. Say which stage the pack now makes reachable: with one cleared fact, stage 1 is open to `raid-campaign`; with none, the answer is stage 0 and the reason is that nothing has been sourced yet. Where a Sell-Kit was imported, report it in the same breath: what was imported, what was placed under **Uncleared** and the reason for each, and what still needs research — the rooms nobody has read yet, and every incumbent whose revenue model is still `unknown — not verified`.

## 6. Capability report

Read `companions.json` at the plugin root. For each entry, check the filesystem for whether its provider is already available, and report the result **by capability**, not by tool name — never the name of a specific package or service. Offer to install a missing one only when the adopter explicitly consents; never install anything silently.

As shipped, `companions.json` is empty — RAID needs no add-ons to produce any of its deliverables. Report exactly: **"No optional capabilities needed — RAID runs entirely on built-in tools."** If a future entry is ever added, report it as an available accelerant, never as a missing requirement — every RAID skill produces its full deliverable without one.

## 7. Routing table

| Moment | Skill |
|---|---|
| About to spend effort and unsure whether money already wins on this ground | `raid` |
| Researching an audience, or finding where a market gathers | `raid-recon` |
| Finding an angle against a competitor, or deciding what to lead with | `raid-asymmetry` |
| Designing a launch, or wanting attention without a budget | `raid-stunt` |
| Reacting to news, timing a launch, or deciding whether now is the moment | `raid-moment` |
| Looking for an audience, or considering a podcast, newsletter, or community | `raid-borrow` |
| Having made one asset, planning content, or wanting more output without more work | `raid-multiply` |
| Planning a campaign, asking what to do first, or asking what comes next | `raid-campaign` |
| Asking for a daily briefing, or what to work on today | `raid-briefing` |

## 8. The pairing

RAID takes ground; `FORTRESS` holds it and governs what may be claimed. The two are one doctrine split by function, not two unrelated systems that happen to share a repo owner.

RAID is usable alone, and that claim is only worth making because kickoff makes it true: section 5 creates every pack file RAID's own gates read — `truth.md`, `motte.md` and `bailey.md` alongside `recon.md` and `asymmetry.md` — wherever they are absent, so a RAID-only adopter who can source one fact reaches stage 1 rather than staring at a locked staircase. Every skill RAID routes to then produces its complete deliverable on that pack, with no dependency on FORTRESS being installed. What RAID does **not** claim alone is the discipline: where FORTRESS is present, `fortress-truth`, `fortress-motte` and `fortress-bailey` own those three files and RAID never touches an existing one. Creating a file and owning it are different jobs, and RAID only does the first.

Where FORTRESS **is** present, its claim discipline binds every RAID output without exception. **A stunt is not exempt from the truth register.** The loudest play RAID can design is exactly the one most likely to be checked, screenshotted, and quoted back — and `fortress-truth` grants no carve-out for something that worked.

## 9. Built-ins only

Every skill in this plugin — this one and all eight it routes to — runs on WebSearch, WebFetch, Read/Write/Edit, Glob/Grep, and Bash. Nothing here assumes any other plugin is installed, including FORTRESS. Section 6's capability report exists because an accelerant is worth naming when one happens to be available — not because RAID needs one to function.

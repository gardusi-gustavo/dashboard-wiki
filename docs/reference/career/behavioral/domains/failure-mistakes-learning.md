# Failure, mistakes, and learning
> **Updated:** 2026-10-24

**Parent:** [`README.md`](../README.md)

## What this probes

**Humility + learning loop**: owning mistakes (without dwelling), retros, and growth when you were not the expert. Dodging “failure” questions often **hurts more** than a narrow honest miss plus prevention—do not invent a production disaster.

## Example questions

| # | Question | Note |
| --- | --- | --- |
| 1 | Tell me about a time you were wrong. | One beat own, 80% fix/learn. |
| 2 | A mistake in production or near-production. | Blast radius + mitigation. |
| 3 | What failure taught you the most? | Specific habit change. |
| 4 | Tell me about a retrospective that changed how you work. | Action items you kept. |
| 5 | When did you miss an expectation? | Manager/peer expectation OK. |
| 6 | Describe a project that did not go as planned. | Still show agency. |
| 7 | Tell me about learning a new language or stack under pressure. | Ramp story. |
| 8 | When were you not the expert in the room? | How you added value anyway. |
| 9 | How do you handle being outside your comfort zone? | Process + story. |
| 10 | Tell me about feedback that was hard to hear. | What you did after. |
| 11 | Tell me about a near miss you caught before it became an incident. | Honest alternative to “hero failure.” |
| 12 | When did you underestimate complexity? | Narrow truth beats fake drama. |

## Example story shapes

- **Blocked by a knowledge gap** — slowed by unfamiliar territory or thin docs, mis-ordered actions until you forced a discovery sequence; reset expectations with your manager and still delivered.
- **Overcommitted / capacity slip** — too many parallel deep efforts made your calendar the bug; you raised it early and handed execution to someone you could mentor.
- **Shared-interface judgment error** — treated a shared/public interface as low-traffic, skipped compatibility review, and users paid on upgrade; owned it and changed your release process.

## Interview framing (first 20–30 seconds)

- **Knowledge gap:** “I was blocked by **what I did not know yet** and **documentation that did not cover our shape**—I bounced between actions until I forced an order of operations. I told my manager early, reset what ‘done’ meant, and found the answer in the code, not hallway answers.”
- **Capacity:** “I had taken on **too much in parallel** and my **calendar** became the bug. I went to my manager, proposed **handing execution to a teammate** I could mentor, and we shipped that way. Now I **cap parallel deep bets**.”
- **Shared interface:** “I treated a shared interface like **low-traffic internal work**, skipped **compatibility review**, and **real users** paid on **upgrade**. I owned the fallout and now treat **every export as a contract**—**tests per public entry point**, **deprecate before delete**, and **no history rewrites** on shared lines.”

## What not to say (anti-patterns)

- Blaming the **platform or the tool** without owning **your discovery strategy and timeline communication**.
- Implying a **major customer outage** if the honest story is **blocked work / calendar slip / knowledge gap**—proportionality beats drama.
- **Skipping the manager / expectation** thread—interviewers hear “evasive” if you only describe technical hunting.
- Presenting **research time** as “nothing happened”; frame **signals sent**, **parallel delivery**, and **what each probe ruled out**.
- Describing a **mentored handoff** as **dumping** the problem—keep **accountability for outcome**, **why** capacity changed, and **what** you transferred.
- **Rewriting shared git history** as “just cleanup”—name it as a **judgment error** and pair with **protected branches + changelog + no force-push to consumer-tracked lines**.

## Gaps and detail drills

- **Weak spot if you only dodge:** have a **knowledge-gap**, a **capacity / self-management**, and a **customer-contract** story ready—each with a clear **before / after**.
- **Drill (ramp):** for the knowledge-gap story, state what you did **not** know on day 1 and how you **de-risked** (tests, reviews, scope) without mixing in the calendar handoff unless asked.
- **Drill (contract):** for the shared-interface story, say what you **test** now per release and how you **deprecate** before removal.

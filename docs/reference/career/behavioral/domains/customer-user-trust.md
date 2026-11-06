# Customer, user, and trust
> **Updated:** 2026-10-24

**Parent:** [`README.md`](../README.md)

## What this probes

Who **felt** the outcome: external users, internal customers, operators? Can you connect engineering choices to **pain removed** or **trust preserved**? Some prompts (trust break) have a **high honesty bar**—do not invent.

## Example questions

| # | Question | Note |
| --- | --- | --- |
| 1 | Who was the user or customer for your work? | Internal vs external. |
| 2 | Tell me about a customer-facing impact. | Who felt it, and what changed. |
| 3 | When did you discover users were confused, blocked, or failing? | Telemetry, support, dogfood. |
| 4 | Tell me about failing a customer or losing trust. | **Weak if invented**—see gaps. |
| 5 | How do you gather or use user feedback in engineering decisions? | Lightweight process OK. |
| 6 | Internal customers vs external—how does your approach differ? | Principled answer. |
| 7 | When did UX or clarity matter for a technical decision you made? | Clarity for a real user. |
| 8 | How do you balance user needs and engineering cost? | Explicit tradeoff. |
| 9 | Tell me about metrics that reflected user happiness or task success. | Define metric + movement. |
| 10 | When did you prioritize reducing recurring pain for operators or customers? | On-call / support. |
| 11 | Tell me about a time expectations were mis-set with a customer or partner. | Recovery narrative. |
| 12 | How do you think about backward compatibility for public API users? | Public-interface story. |

## Example story shapes

- **User-facing improvement under deadline** — a customer-facing change shipped under time pressure.
- **Internal-customer pain reduction** — cutting recurring operator pain (on-call, toil) if framed carefully.
- **Public-interface stability** — de-risking a high-visibility release for external consumers.
- **Cross-platform integration** — making an external platform behave reliably and meeting its acceptance criteria.

## Gaps and detail drills

- **Medium–weak for “trust break”:** if you have **no crisp trust-break story**, the closest is internal pain reduction or public-interface stability; mine the user-facing story for impact (what “bad” looked like, segment, volume) or use a **short boundary** + redirect.
- **Drill:** add remembered detail (tickets, segment, SLA) or admit limits—better than confident invention.

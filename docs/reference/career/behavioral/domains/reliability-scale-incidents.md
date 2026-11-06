# Reliability, scale, and incidents
> **Updated:** 2026-10-24

**Parent:** [`README.md`](../README.md)

## What this probes

Operating and improving **real systems**: peaks, constraints, incidents, alert noise, deployment safety. They want **judgment** under operational reality, not only happy-path features.

## Example questions

| # | Question | Note |
| --- | --- | --- |
| 1 | Tell me about a production incident you handled or prevented. | Timeline + mitigation. |
| 2 | How did you scale for a traffic spike or peak event? | Capacity story. |
| 3 | How do you think about reliability vs velocity? | Principled tradeoff. |
| 4 | Tell me about reducing alert noise or toil. | On-call / ops. |
| 5 | Describe hardening a system after pain. | What changed in design or process. |
| 6 | When did you improve deployment or release safety? | Multi-region / pipelines. |
| 7 | Tell me about operating under strict external constraints. | Exchange / SLA / vendor. |
| 8 | Most complex system you built—**technical** version. | One architecture, 2 minutes max. |
| 9 | When did you trade reliability for something else—was it right? | Honest postmortem tone. |
| 10 | Tell me about load or performance testing before a big event. | Overlaps quality domain. |
| 11 | How do you validate a change will not regress production? | Tests, canaries, metrics. |
| 12 | How do you approach on-call responsibility? | Healthy: limits + fixes. |

## Example story shapes

- **Peak-traffic capacity** — planning and load-testing for a known high-traffic event.
- **Strict external constraints** — operating a live system under exchange/SLA/vendor limits you could not change.
- **Multi-region deployment safety** — reducing the blast radius of regional changes and failover.
- **On-call noise reduction** — fixing recurring root causes to cut pages/toil.

## Gaps and detail drills

- **Drill:** memorize **one number** per story (p99, volume, pages/week, regions) or say what you would verify before claiming.

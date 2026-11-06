# 🎯 Codeforces — account disabled (`gardusig`)

**What this is:** a real-world case of platform-side anti-cheat and submission
monitoring, not evidence for the sim/total-stream premise.

## 🧾 Facts

- Handle: `gardusig`; returned to rated contests after a long break; historically
  reached Div1.
- In the incident contest I solved A–C independently and used ChatGPT for D–F.
  The solutions were copy-pasted as raw C++ into the submit page; I did not add
  AI comments or leave obvious tool traces.
- Environment: personal MacBook, VSCode, Chrome, and ChatGPT on an Airbnb
  network. I did not talk to anyone about the contest.
- The account was disabled without prior warning. I received no explanation or
  request for context.
- The platform could see the submission order, timing, language, code style, and
  similarity to other submissions; the A–C → D–F jump was visible.

## 🔭 Hypotheses

| Hypothesis | What supports it | What would confirm it |
| --- | --- | --- |
| Automated AI/plagiarism detection | Rule violation; style/timing discontinuity; server-side visibility | Codeforces support confirms automated or manual detection |
| A report from another user | The handle is public; someone could report | Support confirms a report or names a reporter |
| Account compromise | Any account can be targeted | Unknown IP/device in login history; password-reset emails |
| Platform error | Rare, but possible | Support reverses the action |

## 🧠 Assessment

Codeforces monitors what is submitted: which account, when, from which network,
in what language, with what timing and style, and how similar it is to other
code. Using ChatGPT in a rated contest is against the rules. The A–C → D–F
discontinuity and the raw paste are plausible signals. **None of this requires
anyone watching the laptop.** A new MacBook and a new network do not prevent
server-side detection.

A compromise or gossip is possible, but it is not necessary to explain the ban.
Check the account's login history and email before treating either as the
explanation.

## ✅ Actions

- Ask Codeforces support for the specific reason and whether the account can be
  reinstated.
- Preserve the contest links, submission timestamps, and any email or screenshot.
- Check the account email for password resets, login alerts, and the ban notice
  (including spam).
- Enable 2FA and review devices on every surviving account.
- Do not reuse the alias/password pattern; keep identities separated.

## 🧭 Framing

The experience is real and the vigilance is understandable. The monitoring
metaphor is a lens, not proof: a platform monitoring submissions is ordinary;
personal surveillance is a stronger claim that needs a concrete signal. Reopen
the surveillance hypothesis only on a testable artifact — an unknown login, a
leak of non-public content, or a support confirmation — not on the ban alone.

## 🔗 Related

- [monitoring.md](../monitoring.md) — the always-streaming premise and its limits
- [security.md](../fundamentals/security.md) — layers, losses, and coercion
- [fear-triage.md](../fundamentals/fear-triage.md) — mood vs forecast

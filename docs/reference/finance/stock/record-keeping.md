# 📝 Stock record keeping
> **Updated:** 2026-11-02

**What this is:** how to record stock orders, closed cycles, taxes, and the
running position. The actual statements live in the private ledger.

## 🗂️ Layout

| Path | What goes there |
| --- | --- |
| `monthly/yyyy-mm.md` | every buy and sell for that month |
| `trades.md` | closed-cycle conclusions: average, gross/net, tax, loss carry |
| `taxes/yyyy-mm.pdf` | DARF payment receipts, named after the payment month |
| `ledger.md` | rules, monthly tax, running position |
| `short-selling.md` | actual short-sale record |

## 📜 Rules

- Every order belongs to a monthly table.
- Buys are simple records; they do not trigger tax.
- Sells carry `Tax?` (`yes`/`no`).
- A taxable month gets a Taxes row: gain, rate, DARF, deadline, proof.
- The current-position table reconciles open quantity (`buys − sells`).
- Checks: monthly totals, sell totals, tax status, position matches ledger.

## 🧮 Average cycle

- A **long** cycle starts at 0 → positive; a **short** cycle starts at 0 →
  negative.
- Average buy/cover = weighted average of the cycle's buys/covers.
- Average sell = weighted average of the cycle's sells.
- Partial sells/covers keep the cycle open.
- At position 0: `gross = sell proceeds − buy/cover cost`; `net = gross − fees`;
  averages reset.
- Every closed cycle gets a row in `trades.md`.

## 🗓️ Monthly tax routine

| When | Action |
| --- | --- |
| Sale day | Add the order to `monthly/yyyy-mm.md`; mark `Tax?` |
| Month X+1 | Review month X sells; classify by asset; check R$20k exemption; offset losses; compute gain |
| Before deadline | Pay DARF 6015 by the last business day of X+1; round up if unsure |
| After payment | File the receipt in `taxes/yyyy-mm.pdf`; update taxes and trades |
| Year-end | Reconcile the year for IRPF; recover/compensate overpayment |

- Do not wait for the deadline.
- Record first, calculate later.
- Exempt is not invisible: still record the sale with `Tax? = no`.
- Losses carry forward; a loss month pays no DARF.

## 🔗 Related

- [Brazil tax rules](brazil-tax-rules.md)
- [Short selling](short-selling-brazil.md)
- [Stock operations](readme.md)

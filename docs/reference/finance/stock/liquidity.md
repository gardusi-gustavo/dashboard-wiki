# 🌊 Liquidity — the first gate

**What this is:** how to decide whether a stock is liquid enough to enter and exit without moving the
price, being trapped, or becoming someone else’s exit liquidity. **Illustrative numbers, not a
recommendation. Brazil, rules as of 2026 — verify current data.**

---

## 📏 Metrics

<!-- begin table -->
| Metric | Formula | Healthy | Warning |
| --- | --- | ---: | ---: |
| **ADTV** | average shares × price, 20 sessions | > R$20M/day | < R$5M/day |
| **Free float** | public shares ÷ total shares | > 40% | < 15% |
| **Bid-ask spread** | (ask − bid) ÷ midpoint | < 0.5% | > 2% |
| **Position / ADTV** | position value ÷ ADTV | < 10% | > 30% |
| **Days to exit** | position ÷ (ADTV × participation) | < 1–2 days | > 5 days |
| **Turnover** | traded value ÷ market cap | > 0.2% | < 0.05% |
<!-- end table -->

## 🚦 Gate

<!-- begin table -->
| Gate | PASS | CAUTION | FAIL |
| --- | --- | --- | --- |
| **ADTV** | > R$20M/day | R$5–20M/day | < R$5M/day |
| **Free float** | > 40% | 15–40% | < 15% |
| **Spread** | < 0.5% | 0.5–2% | > 2% |
| **Position / ADTV** | < 10% | 10–30% | > 30% |
| **Days to exit** | < 1 day | 1–3 days | > 3 days |
| **Recent reverse split** | None | Older than 2 years | Recent |
| **Volume spikes** | Normal | Occasional | Repeated pump-like spikes |
<!-- end table -->

**Rule:** two FAILs = skip. One FAIL + a small position = only with a written exit plan. A PASS is not
a buy signal; it is permission to look at the business.

## 🧮 Position impact

<!-- begin table -->
| Position | ADTV | % of ADTV | Days at 20% participation |
| ---: | ---: | ---: | ---: |
| R$1M | R$48M | 2.1% | 0.10 day |
| R$10M | R$48M | 20.8% | 1.04 days |
| R$24M | R$48M | 50.0% | 2.50 days |
| R$240k | R$2M | 12.0% | 0.60 day |
| R$1M | R$2M | 50.0% | 2.50 days |
<!-- end table -->

The exit is the constraint, not the entry.

## 🕳️ Manipulation

Low-float, low-ADTV stocks are easier to move because a small order is a large share of the volume.

- **Pump:** coordinated buying, social posts, and volume spikes; the price rises before the news.
- **Dump:** the same group sells into the retail demand.
- **Wash trading:** buying and selling to create fake volume; the tape looks active, but the book is
  thin.
- **Marking the close:** a small order moves the closing price; index and fund flows can amplify it.
- **Reverse split:** reduces the share count and can make a low-priced stock look “cleaner” without
  changing the business.
- **Hidden groups:** WhatsApp, Telegram, and Discord can coordinate without a public trace. By the
  time the volume appears, the move may be underway.

You cannot reliably detect a private group. The defense is to **avoid the setup**: low float, low
ADTV, wide spread, recent reverse split, and repeated unexplained spikes.

## 🧪 Examples

### 🟢 Liquid

- ADTV R$48M, free float 70%, spread 0.17%.
- A R$24M position is 50% of ADTV; at 20% participation, 2.5 days.
- You can exit in pieces; the spread is a small cost.

### 🟡 Caution

- ADTV R$8M, free float 30%, spread 0.9%.
- A R$1M position is 12.5% of ADTV; at 20% participation, 0.6 day in normal conditions.
- In stress, volume can halve and the spread can triple.

### 🔴 Fail

- ADTV R$2M, free float 12%, spread 3%.
- A R$240k position is 12% of ADTV; at 20% participation, 0.6 day — but the book may not absorb it.
- A R$1M position is 50% of ADTV; 2.5 days at 20% participation, with a 3% entry and exit cost.
- A single seller can move the price; the stock is manipulator-friendly.

## ✅ Checklist

1. What is the 20-day ADTV?
2. What is the free float?
3. What is the current spread, and what was it in stress?
4. What is the position as a % of ADTV?
5. How many days to exit at 20% participation?
6. Was there a reverse split or a sudden volume spike?
7. Is the stock in an index or a fund flow that can distort the tape?
8. Can the broker execute a limit order without chasing?

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [indicators.md](indicators.md#-adtv) — ADTV, free float, spread, days to exit.
- [dangers.md](dangers.md#-forced-liquidation) — the forced-exit case.
- [flows.md](flows.md) — manipulation and hidden groups.
- [buy/readme.md](buy/readme.md) — the entry process.
- [sell/readme.md](sell/readme.md) — the exit process.

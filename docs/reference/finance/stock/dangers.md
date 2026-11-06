# 🧨 Dangers — what can go wrong

**What this is:** the generic danger library — accounting failures, debt walls, disruption, state
intervention, recalls, squeezes, forced liquidation, and the stress cases that break a position.
**Brazil, rules as of 2026 — verify current rules and company facts. Not financial advice.**

---

## 🧭 Two kinds of danger

<!-- begin table -->
| Kind | Source | What predicts it | What does not |
| --- | --- | --- | --- |
| **Company danger** | Accounting, debt, competition, politics, operations | Cash flow, accruals, debt, market share, safety record | P/E, P/B, dividend yield |
| **Positioning danger** | Crowding, borrow, float, options, coordination | Short interest, days to cover, borrow fee, free float, ADTV | Fundamentals, valuation |
<!-- end table -->

Do not use a company thesis to predict a squeeze. Do not use a squeeze to justify a long-term buy.

## 🌀 Positioning danger

### 🌀 Squeezes

A squeeze is a **positioning event**, not a company event. The stock can be bad and still squeeze;
the stock can be good and still squeeze.

- **Setup:** high short interest relative to float, low free float, high days to cover, expensive or
  scarce borrow, large call open interest.
- **Trigger:** a catalyst, a recall, a large buyer, or coordinated retail flow.
- **Tell:** price and volume accelerate while the fundamentals do not change.
- **Danger:** the loss is not bounded by the company’s value; it is bounded by the collateral and the
  broker’s patience.
- **Examples:** [GME](case-studies.md#-gme), [VW](case-studies.md#-vw), [Tesla](case-studies.md#-tesla),
  [MGLU3](case-studies.md#-mglu3).

**Rule:** avoid crowded shorts in low-float stocks. If you are already short, a protective call and a
collateral buffer matter more than the target price.

## 🏭 Company danger

### 🧾 Accounting failures

The reported profit does not turn into cash, or the balance sheet hides obligations.

- **Signals:** [FCF conversion](indicators.md#-fcf-conversion) below 60%, high
  [Sloan ratio](indicators.md#-sloan-ratio), [DSO](indicators.md#-dso) rising faster than revenue,
  [DPO](indicators.md#-dpo) stretched versus peers, auditor or management turnover.
- **Case:** [AMER3](case-studies.md#-amer3) — the low P/E and dividend yield did not protect; the
  warning was cash flow, working capital, empty stores, and competitors.
- **Defense:** read the cash-flow statement first, compare receivables and payables with revenue, and
  treat a sudden auditor change as a question.

### 🧱 Debt walls

The company owes more than it can refinance.

- **Signals:** [net debt to EBITDA](indicators.md#-net-debt-to-ebitda) above 3–4x,
  [interest coverage](indicators.md#-interest-coverage) below 2x, a
  [maturity wall](indicators.md#-maturity-wall) with negative FCF.
- **Case:** [OIBR3](case-studies.md#-oibr3) — low P/B did not help; the equity was diluted and the
  debt was the thesis.
- **Defense:** check the maturity schedule and the cost of new debt, not just the headline multiple.

### 🔄 Disruption

The business model is being replaced.

- **Signals:** negative [same-store sales](indicators.md#-same-store-sales), falling
  [market share](indicators.md#-market-share), rising
  [online penetration](indicators.md#-online-penetration), gross margin compression.
- **Cases:** [Blockbuster](case-studies.md#-blockbuster), [Nokia](case-studies.md#-nokia),
  [AMER3](case-studies.md#-amer3).
- **Defense:** ask whether the company is on the right side of the channel shift; a cheap multiple on
  a dying format is not a bargain.

### 🏛 State intervention

The controlling shareholder is the state, or politics can change the price.

- **Signals:** political exposure, price controls, governance history, management turnover.
- **Case:** [PETR4](case-studies.md#-petr4) — a low P/E and high dividend did not prevent a one-day
  political shock.
- **Defense:** size for headline risk; a cheap multiple is not protection from a decree.

### 🔔 Recalls

A product, safety, or environmental failure creates legal and operational losses.

- **Signals:** safety record, regulatory history, legal contingencies, concentrated production.
- **Case:** [VALE3](case-studies.md#-vale3) — the dam disaster was an operational/legal shock, not a
  valuation event.
- **Defense:** check the tail risk before the dividend; high yield can coexist with a large
  contingent liability.

### 💥 Forced liquidation

The broker closes the position before the thesis has time to work.

- **Triggers:** margin call, collateral haircut, borrow recall, circuit breaker, gap.
- **Signals:** [ADTV](indicators.md#-adtv) and
  [days to exit](indicators.md#-days-to-exit) too high for the position; thin collateral buffer.
- **Case:** a short with only the minimum margin can be called at the entry price — there is no cushion.
- **Defense:** post more collateral than the minimum, size the position to survive a gap, and know the
  broker’s close-out rule.

## 💀 Buy-side stress

<!-- begin table -->
| --- | ---: | ---: | --- |
| −50% | R$12 | −R$7,992 | A 50% drawdown is normal for a broken thesis |
| −77% | R$5.52 | −R$12,307.68 | AMER3-style one-day gap |
| −95% | R$1.20 | −R$15,187.20 | Near-total loss; recovery is mathematically hard |
| Zero | R$0 | −R$15,984 | Equity can be wiped out in judicial recovery |
<!-- end table -->

A −50% loss needs +100% to break even. A −77% loss needs +335%. A −95% loss needs +1,900%. That is
why position sizing and permanent-loss avoidance matter more than the entry multiple.

## 🩳 Short-side stress

<!-- begin table -->
| --- | ---: | ---: | --- |
| +50% | R$36 | −R$7,992 | Yes, with 120–150% collateral |
| +100% | R$48 | −R$15,984 | Yes; own collateral wiped |
| +300% | R$96 | −R$47,952 | Yes; negative balance |
| +1,000% | R$264 | −R$159,840 | Yes; far beyond the collateral |
<!-- end table -->

The theoretical loss is unlimited. The practical limit is the broker’s forced close and your ability
to post more collateral. A protective call caps the buyback price, but not the borrow cost, dividends,
or recall risk.

## 🏦 Broker and margin danger

- **Margin call:** the broker can close the position at its own price.
- **Haircut:** Tesouro collateral may be worth less than its face value for margin purposes.
- **Recall:** the lender can ask for the shares back; the short may be closed early.
- **Gap:** a halt or circuit breaker can prevent you from closing at the stop price.
- **Zero balance:** after a gap, the broker can hold a negative balance.
- **Concentration:** one position can consume the whole collateral buffer.

## 🧪 Danger table

<!-- begin table -->
| Danger | Case | Indicator | Lesson |
| --- | --- | --- | --- |
| Accounting | [AMER3](case-studies.md#-amer3) | [FCF conversion](indicators.md#-fcf-conversion), [Sloan](indicators.md#-sloan-ratio) | Cash flow beats headline profit |
| Debt | [OIBR3](case-studies.md#-oibr3) | [net debt to EBITDA](indicators.md#-net-debt-to-ebitda) | Low P/B is not a margin of safety |
| Disruption | [Blockbuster](case-studies.md#-blockbuster) | [same-store sales](indicators.md#-same-store-sales) | A cheap multiple on a dying business |
| Politics | [PETR4](case-studies.md#-petr4) | [state intervention](dangers.md#-state-intervention) | Headline risk is not in the P/E |
| Legal/environment | [VALE3](case-studies.md#-vale3) | [max drawdown](indicators.md#-max-drawdown) | Tail risk can dwarf the dividend |
| Squeeze | [GME](case-studies.md#-gme) | [short interest](indicators.md#-short-interest) | Positioning, not valuation |
| Liquidity | [liquidity.md](liquidity.md#-fail) | [ADTV](indicators.md#-adtv) | You cannot exit what does not trade |
<!-- end table -->

## ✅ Defense

1. **Liquidity gate first.** Skip the stock if it fails.
2. **Size for the worst case.** A long can go to zero; a short can exceed the collateral.
3. **Read cash flow, not just earnings.** FCF conversion and accruals.
4. **Check the debt wall.** Maturities and coverage.
5. **Know the industry trend.** Same-store sales, market share, online penetration.
6. **Separate company risk from positioning risk.** Do not use fundamentals to predict a squeeze.
7. **Avoid crowded shorts in low-float stocks.**
8. **Keep a collateral buffer.** 120% is a minimum, not a target.
9. **Use a protective call if the short is large or hard to borrow.**
10. **Write the invalidation and the exit before entering.**

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [case-studies.md](case-studies.md) — the numeric cases.
- [indicators.md](indicators.md) — the indicators behind the warnings.
- [liquidity.md](liquidity.md) — the first gate.
- [flows.md](flows.md) — how the move spreads.
- [options.md](options.md) — protective calls.

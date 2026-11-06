# 📈 Stocks — operations

**What this is:** the stock-operations map — the long-only buy and sell process, B3 events, flows,
and the cases where the market moved fast.
**Brazil, rules as of 2026 — verify current Receita Federal, B3, and broker rules. Not financial
advice.**

---

## 🗂️ Map

<!-- begin table -->
| File | Covers |
| --- | --- |
| [buy/readme.md](buy/readme.md) | Entry cases, position sizing, buy checklist |
| [sell/readme.md](sell/readme.md) | Exit checklist, thesis break, forced selling |
| [fees-taxes.md](fees-taxes.md) | Brokerage, B3 fees, swing/day/short tax, DARF |
| [options.md](options.md) | Calls, puts, covered call, protective put, assignment |
| [indicators.md](indicators.md) | Valuation, quality, debt, growth, positioning, macro |
| [liquidity.md](liquidity.md) | ADTV, free float, spread, position impact, gate |
| [dangers.md](dangers.md) | Accounting, debt, disruption, squeezes, intervention |
| [b3-events.md](b3-events.md) | Data COM/EX, splits, bonuses, auctions, recalls |
| [flows.md](flows.md) | How a move spreads, what is visible, what stays hidden |
| [case-studies.md](case-studies.md) | GME, AMER3, OIBR3, VALE3, MGLU3, and more |
| [brazil-tax-rules.md](brazil-tax-rules.md) | B3/CPF capital-gains rules |
| [short-selling-brazil.md](short-selling-brazil.md) | B3 short-selling mechanics and costs |
| [record-keeping.md](record-keeping.md) | order, cycle, tax, and position records |
<!-- end table -->

## 🧠 Mindset

- **Few operations.** Research, wait, buy, hold, sell when the price or thesis is stretched.
- **Patience is the edge.** The market pays for waiting better than for pressing buttons.
- **Cash is a position.** There is no obligation to be invested all the time.
- **The R$20k exemption is not the goal.** It rewards small sales; think bigger and treat the tax as
  a cost.
- **A stock is not a ticket.** It is a claim on future cash flow, with a price attached.
- **Size for the worst case.** A long can go to zero; a short can exceed the collateral.
- **No leverage by default.** Margin and short selling are separate, high-risk operations.

## 🏦 B3 mechanics

- **Ticker:** use the standard lot symbol for the asset; fractional symbols add an `F` suffix.
- **Order types:** market or limit. A limit order controls the price; the trade may not fill.
- **Settlement:** T+2 for cash and custody.
- **Custody:** usually free at retail brokers.
- **Proventos:** dividends, JCP, bonificações, and subscrições arrive through the broker.
- **Data COM / Data EX:** own the stock on Data COM to receive the payout; the price adjusts on Data EX.
- **Circuit breaker:** a sharp move can pause trading; you may not be able to exit at the price on screen.
- **Auction:** opening, closing, and volatility auctions can gap through a stop.

## 💸 Fees and taxes

The short version:

- **Brokerage:** zero or a fixed amount per order; ISS applies when there is a fee.
- **B3 emoluments:** roughly 0.0325% per side for swing stock; 0.025% for day trade.
- **Swing tax:** 15% on the net gain; the R$20k exemption applies only to spot stock sales.
- **Day trade:** 20%; no R$20k exemption.
- **Short selling:** 15%; a spot swing short qualifies for the R$20k exemption when monthly gross stock sales are ≤ R$20k. Day trade is not exempt.
- **IRRF:** 0.005% on swing sales; 1% on day-trade daily gain.
- **DARF:** 6015 by the last business day of the following month.


## 🔎 Finding candidates

<!-- begin table -->
| Lens | Metrics | What to check |
| --- | --- | --- |
| **Valuation** | P/E, forward P/E, P/S, P/B, P/FCF, EV/EBITDA, PEG | Cheap vs history and peers, not just cheap |
| **Cash** | FCF yield, operating cash flow, FCF conversion | Real cash after capital spending |
| **Quality** | ROE, ROIC, gross margin, SG&A | Durable returns, not one good quarter |
| **Safety** | Debt/equity, interest coverage, net cash | Survives a bad cycle |
| **Growth** | Revenue CAGR, same-store sales, market share | Growth that does not need new stores or debt |
| **Liquidity** | ADTV, free float, spread | Can you enter and exit without moving the price? |
| **Price** | Historical range, drawdown, volume | Is the market already pricing the bad news? |
<!-- end table -->

**Value-trap filters:** declining revenue, a debt wall, repeated dilution, accounting noise, a
business model that is being replaced, and a low multiple on peak earnings. A low multiple on a
broken business is not a bargain.

## 🧭 Personal process

1. **Screen** — build a short list, not a portfolio.
2. **Check liquidity** — if the stock fails the gate, stop.
3. **Read the numbers** — cash flow, debt, margins, share count, and the industry trend.
4. **Write the thesis** — why this business, why now, what the market is missing.
5. **Set a price range** — bear, base, and bull; not a single target.
6. **Wait** — let the market come to you.
7. **Buy in tranches** — with an invalidation point and a maximum position size.
8. **Hold** — review quarterly, not daily.
9. **Sell** — when the price is stretched, the thesis breaks, or a better opportunity appears.

**Expected-price discipline:** write the expected price and the assumptions behind it before buying.
If the price reaches the target, sell at least part of the position. Do not move the target just
because the stock is still rising.

## 🚪 Exit checklist

<!-- begin table -->
| Question | If yes | If no |
| --- | --- | --- |
| Did the thesis break? | Sell; do not average down | Hold or add only if the price is better |
| Is the price above the expected range? | Sell in tranches | Keep the target |
| Is the balance sheet worse? | Reduce or exit | Recheck next quarter |
| Is liquidity deteriorating? | Exit earlier, in smaller pieces | Normal exit |
| Is the position too large to hold through a drawdown? | Cut to the sleeping size | Keep |
| Is there a better risk-adjusted use of the cash? | Compare after tax and liquidity | Hold |
| Is the short borrow cost or margin rising? | Close or hedge | Keep with a buffer |
<!-- end table -->

## ⚖️ Stocks vs CDI

<!-- begin table -->
| Dimension | Long-only stock | CDI cash |
| --- | --- | --- |
| **Return** | Capital gain + proventos | Interest |
| **Volatility** | High; daily marks | Near zero nominal |
| **Liquidity** | T+2 | Same day / D+0–D+1 |
| **Protection** | No FGC | FGC within the cap |
| **Tax** | 15% swing on gain; R$20k exemption | 22.5% → 15% regressive |
| **Inflation** | Companies can reprice | Fixed nominal rate |
<!-- end table -->

The stock must beat CDI **after tax and risk**, not just before. A 15% nominal gain with high
volatility may be worse than a predictable net CDI return for money you need soon.

## ❓ Open questions

- What is the minimum position size that makes research and fees worth it?
- How many names are enough for diversification without turning into an index?
- When does a “long-term hold” become a refusal to admit the thesis broke?
- What is the maximum position you can hold through a 50% drawdown without forced selling?

## 🔗 Related

- [buy/readme.md](buy/readme.md) — entry cases and the buy checklist.
- [sell/readme.md](sell/readme.md) — exit checklist and forced-selling risk.
- [../fixed-income.md](../fixed-income.md) — the cash alternative.
- [../resource-management.md](../resource-management.md) — reserve and allocation.
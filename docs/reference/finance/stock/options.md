# 🎯 Options — calls, puts, and protective structures

**What this is:** the basic option vocabulary and the two structures that matter for a stock
portfolio — the covered call and the protective put — plus the short-call danger and the B3 tax
rules. **Brazil, rules as of 2026 — verify current B3, broker, and tax rules. Not financial
advice.**

---

## 🧱 Vocabulary

<!-- begin table -->
| Term | Meaning |
| --- | --- |
| **Call** | The right to buy the underlying at the strike |
| **Put** | The right to sell the underlying at the strike |
| **Premium** | The price paid by the buyer to the seller |
| **Strike** | The price at which the option can be exercised |
| **Expiry** | The last date to exercise or close |
| **ITM** | In the money: intrinsic value > 0 |
| **ATM** | At the money: strike ≈ spot |
| **OTM** | Out of the money: intrinsic value = 0 |
| **Intrinsic value** | Call: max(0, spot − strike); put: max(0, strike − spot) |
| **Time value** | Premium − intrinsic value |
| **Assignment** | The seller is obliged to deliver or buy the shares |
<!-- end table -->

A B3 equity option usually covers **100 shares** per contract. Check the contract specification; a
different lot size changes the math.

## 📈 Covered call

You own the stock and sell a call against it. The premium is income; the upside above the strike is
capped.


<!-- begin table -->
| Item | Calculation | Amount |
| --- | --- | ---: |
| Premium received | 6 × 100 × R$1.20 | R$720.00 |
| Shares covered | 6 × 100 | 600 |
| If spot ≤ R$26 at expiry | Keep premium; keep shares | R$720.00 |
| If assigned at R$26 | Gain on 600 shares: 600 × (26 − 24) | R$1,200.00 |
| Total on covered shares | R$1,200 + R$720 | R$1,920.00 |
| Upside missed above R$26 | 600 × (spot − 26) | Opportunity cost |
<!-- end table -->

The 66 uncovered shares still participate in the upside. The premium is not free: you gave up the
right to sell those 600 shares above R$26 during the option’s life.

## 🛡️ Protective put

You own the stock and buy a put to set a floor. The premium is the cost of insurance.


<!-- begin table -->
| Item | Calculation | Amount |
| --- | --- | ---: |
| Premium paid | 6 × 100 × R$0.80 | R$480.00 |
| Shares protected | 6 × 100 | 600 |
| Floor value at expiry | 600 × R$22 | R$13,200.00 |
| Cost per protected share | R$480 ÷ 600 | R$0.80 |
| Effective floor | R$22 − R$0.80 | R$21.20 |
<!-- end table -->

The put caps the loss on the protected shares, but the premium is a real cost. If the stock rises, the
put expires worthless and the portfolio underperforms by the premium.

## 🚨 Short call — the dangerous side

Selling a naked call has unlimited theoretical loss: the stock can rise without a ceiling. The
premium is small compared with the risk. A covered call is different because the shares are already
owned; a naked call is a leveraged short-volatility position.

**Do not sell naked calls** unless you can post margin, monitor the position, and accept assignment
at a price you did not choose.

## 🩳 Protective call for a short

If you are short the stock, a **long call** caps the buyback price:

- Buy a call above the current price.
- The premium is a known cost.
- The call caps the loss from a squeeze, but not the borrow cost, dividends, or recall risk.
- The call can expire before the squeeze ends; roll or close it.

A protective call is insurance against a gap, not a cure for a crowded short.

## 💧 Liquidity and volatility

- **Bid-ask spread:** options can be much wider than the stock; a “cheap” premium can be expensive
  to exit.
- **Open interest:** low OI means you may not find a counterparty at a fair price.
- **Implied volatility:** high IV makes premiums expensive; it also signals that the market expects
  a large move.
- **Time decay:** long options lose time value; short options benefit from it, but carry tail risk.
- **Expiry:** a short-dated option can go to zero or be assigned; do not treat it as a stock
  substitute.

## 🧾 Tax

- **Swing options:** 15% on the net gain; **no R$20k exemption**.
- **Day trade options:** 20%; no exemption.
- **IRRF:** 0.005% on swing sales; 1% on day-trade daily gain.
- **Assignment/exercise:** the result can be treated as the underlying stock or as an option,
  depending on the operation; confirm with the broker.
- **Loss:** credit against future gains in the same category.
- **DARF:** 6015; due by the last business day of the following month.

Full cost tables: [fees-taxes.md](fees-taxes.md).

## ⚠️ Common mistakes

- Selling a covered call and forgetting the shares can be called away.
- Buying a put for insurance and then not rolling it before expiry.
- Treating a low premium as low risk; the risk is in the strike and the underlying.
- Ignoring the spread and open interest.
- Using options to “recover” a losing stock position.
- Shorting a call without the shares or the margin.

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [sell/readme.md](sell/readme.md) — the exit side and protective call.
- [fees-taxes.md](fees-taxes.md) — option tax and DARF.
- [b3-events.md](b3-events.md) — expiry, exercise, and corporate actions.
- [liquidity.md](liquidity.md) — why the option can be harder to exit than the stock.

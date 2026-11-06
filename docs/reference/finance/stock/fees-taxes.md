# 💸 Fees and taxes — stocks, options, and shorts

**What this is:** the cost layer for B3 stock operations — brokerage, exchange fees, swing and day
trade, short selling, dividends, JCP, IRRF, and DARF. **Brazil, rules as of 2026 — verify current
Receita Federal, B3, and broker rules. Not financial advice.**

---

## 🏦 Brokerage and exchange fees

<!-- begin table -->
| Cost | Typical shape | Notes |
| --- | --- | --- |
| **Brokerage** | R$0 or R$5 per order | Example: R$5; zero-fee broker: R$0 |
| **ISS** | 5% over the brokerage fee | Zero when brokerage is zero |
| **B3 emoluments — swing** | 0.0325% per side | On the financial volume |
| **B3 emoluments — day trade** | 0.025% per side | On the financial volume |
| **Custody** | Usually zero | Check the broker’s table |
| **BTC rent** | % p.a. on the short position | Only for short selling |
| **B3 rental** | ~0.25% p.a. or a minimum | Only for short selling |
| **Transfer / custody exit** | Broker-specific | Sometimes zero, sometimes not |
<!-- end table -->

For a small trade, the round trip is roughly **R$21**: R$10.50 brokerage + about R$10.50 in B3 fees. On a R$5,000 trade, the same R$21 is a much larger share of the expected gain.

## 🧾 Tax rates

<!-- begin table -->
| Operation | Rate | R$20k exemption | IRRF |
| --- | ---: | --- | ---: |
| **Stocks, spot, swing** | 15% | Yes, gross sales ≤ R$20k/month | 0.005% |
| **Stocks, day trade** | 20% | No | 1% on daily gain |
| **Short selling, swing** | 15% | Yes, spot swing short with gross stock sales ≤ R$20k/month | 0.005% |
| **Options, swing** | 15% | No | 0.005% |
| **Options, day trade** | 20% | No | 1% on daily gain |
| **ETFs** | 15% | No | 0.005% |
| **BDRs** | 15% | No | 0.005% |
| **FIIs** | 20% | No | 0.005% |
<!-- end table -->

The exemption is on the **gross sale volume** of spot stocks in the month, not on the profit. A sale
of R$19,980 is inside; R$20,001 is outside. Other stock sales in the same month count toward the
limit.

IRRF may be zero on an exempt sale. The exemption is tested on gross sales, not on whether the
broker withheld the 0.005%. A missing IRRF line is not evidence that the sale was unreported.

## 💰 Dividends, JCP, and proventos

- **Dividends:** as of 2026, companies withhold 10% IRRF on dividends above R$50k per month to the
  same individual; below that, no withholding under the rule described. Verify current law.
- **JCP:** 15% IRRF at source.
- **Bonificações:** not a taxable sale; adjust the cost basis per share.
- **Subscriptions:** the right has value; selling the right or subscribing has different tax
  treatment. Confirm with the broker.
- **Data COM / Data EX:** own the stock on Data COM to receive the payout; the price adjusts on Data
  EX.


## 🩳 Short-selling tax

A venda descoberta is a spot stock sale followed by a later buyback. When it is a **swing trade**
(opened and closed on different days) and total gross stock sales in the month are **≤ R$20,000**,
the gain is exempt. It is not automatically a non-exempt operation just because shares were borrowed.

The buyback, BTC/stock-loan fee, B3 rental, dividends reimbursed, and brokerage fees adjust the
result. If total monthly stock sales exceed R$20,000, the net gain is taxed at 15% in the swing
category. Day trade remains 20% with no exemption.

Confirm the broker’s classification and the IRRF line on the note. A missing IRRF does not change
the R$20k test.

## 📅 DARF and loss credit

- **DARF code:** 6015.
- **Due date:** last business day of the month following the sale.
- **Minimum:** R$10; below that, accumulate.
- **Loss:** credit against future gains in the same category; no expiry.
- **Day trade vs swing:** separate categories; confirm how the broker classifies the operation.
- **IRRF:** deduct from the DARF; it is an advance, not an extra tax.

## 🧾 DIRPF

- **Exempt gains:** variable income, type 20.
- **Taxable results:** variable income; include the monthly results.
- **Positions:** Bens e Direitos at cost basis.
- **Short positions:** confirm the specific reporting fields; a short is a liability/position, not a
  simple asset.
- **Foreign assets:** outside this page; different rules.

## ⚠️ Common mistakes

- Thinking the R$20k exemption is on profit, not gross sales.
- Forgetting that other sales in the month count toward the limit.
- Ignoring fees in the cost basis.
- Forgetting IRRF when paying the DARF.
- Assuming every short sale is non-exempt.
- Confusing IRRF with the R$20k exemption test.
- Assuming the broker’s tax report is complete.
- Selling in December and assuming the tax is due in December; it is due in January.

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [options.md](options.md) — option-specific costs and tax.
- [b3-events.md](b3-events.md) — corporate actions and settlement.
- [../fixed-income.md](../fixed-income.md) — fixed-income tax brackets.

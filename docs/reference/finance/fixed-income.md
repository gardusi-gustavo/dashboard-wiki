# 🏦 Fixed income — Tesouro, CDB, and the cash ladder

**What this is:** the fixed-income half of the finance folder — what Tesouro Direto and CDBs are
good for, how the Brazil taxes work, where the credit risk sits, and how to manage the cash ladder.
**Brazil, rules as of 2026 — verify current rates, FGC limits, and broker rules. Not financial advice.**

---

## 🗂️ Instrument map

<!-- begin table -->
| Instrument | Risk | Liquidity | Best use | Watch |
| --- | --- | --- | --- | --- |
| **Tesouro Selic** | Sovereign | Daily, normally | Cash-like reserve, collateral | B3 custody fee; broker haircut |
| **Tesouro IPCA+** | Sovereign | Daily, mark-to-market | Long inflation hedge | Selling early in a rate spike |
| **Tesouro Prefixado** | Sovereign | Daily, mark-to-market | Lock a nominal rate | Highest duration risk |
| **CDB daily** | Bank + FGC | Same day / D+0–D+1 | Emergency fund, short parking | IOF under 30 days; FGC cap |
| **CDB locked** | Bank + FGC | At maturity | 2+ year yield | No early redemption; bank risk |
| **LCI/LCA** | Bank + FGC | Usually locked | Tax-exempt income | Liquidity; FGC rules; rate |
<!-- end table -->

## 🧾 Taxes

Income tax is on the gain, not the principal, and it is withheld at source for these instruments.

<!-- begin table -->
| Holding period | IR on gain |
| --- | ---: |
| Up to 180 days | 22.5% |
| 181–360 days | 20.0% |
| 361–720 days | 17.5% |
| Above 720 days | 15.0% |
<!-- end table -->

**IOF:** 96% on day 1, falling to 3% on day 29, and **0% on day 30**. Do not redeem inside 30 days
unless it is a real emergency.

**Tax drag:** a 1-year CDB at 100% CDI can lose a meaningful share of its real return to the 20% IR
bracket. A 2-year hold reaches the 15% bracket, but the money is locked longer. Compare **net** yield,
not the headline rate.

## 🛡️ FGC and credit risk

The Fundo Garantidor de Créditos covers deposits up to **R$250k per person per institution**, with a
**R$1M total per four-year window**. Payout can take weeks or months.

- Split CDBs across issuers if the amount is above the cap.
- A 120% CDI CDB from a weak bank is not the same asset as a 100% CDI CDB from a strong bank.
- Above the FGC cap, the bank credit risk is unhedged.

## 🧱 Collateral and mark-to-market

Tesouro Selic is the usual **collateral** for margin and stock operations: sovereign risk, daily
liquidity, and broad broker acceptance. The haircut varies by broker — confirm it.

- **B3 custody:** around 0.20% p.a. on Tesouro holdings; Selic balances up to R$10k are often exempt.
- **CDB is poor collateral:** many brokers reject it or apply steep haircuts.
- **Mark-to-market:** Prefixado and IPCA+ can lose value before maturity when rates rise. Only hold
  them with money you can keep to maturity.
- **Spread:** the Treasury buyback price is not the same as the issue price.
- **Margin buffer:** keep cash available before locking the reserve into Tesouro. A full allocation
  can force a margin call or broker-covered negative balance; the fee is small per day but adds up.

## 🧭 Management playbook

<!-- begin table -->
| Bucket | Horizon | Default | Rule |
| --- | --- | --- | --- |
| **Emergency** | 0–6 months | CDB 100%+ CDI daily / Tesouro Selic | 3–6 months of expenses; season 30 days |
| **Short** | 6–24 months | CDB 100–105% CDI daily or short lock | Match maturity to the spend |
| **Long** | 2+ years | CDB 110%+ CDI / Tesouro IPCA+ | Hold to maturity; size the lockup |
| **Collateral** | Open | Tesouro Selic | Keep a haircut buffer; check fees |
<!-- end table -->

**Do:**

- Build a small ladder of maturities so cash returns without selling at a bad price.
- Compare CDB net yield after IR against Tesouro net yield after the B3 custody fee.
- Keep the emergency fund in daily liquidity and past the 30-day IOF window.
- Diversify issuers under the FGC cap.

**Do not:**

- Lock rent money into a high-yield CDB with no early redemption.
- Chase 120% CDI with emergency cash.
- Sell IPCA+ at a loss during a rate spike unless the alternative is worse.
- Treat a tax-exempt LCI/LCA as free liquidity — check the lockup.

## ❓ Open questions

- What is the real haircut your broker applies to Tesouro Selic as collateral?
- Which CDB issuers currently pay above 110% CDI without a long lockup?
- How does the B3 custody fee change the net comparison at your position size?

## 🔗 Related

- [stock/readme.md](stock/readme.md) — long-only stocks and B3 taxes.
- [resource-management.md](resource-management.md) — reserve and allocation.

# 📊 Indicators — what to measure, what it hides

**What this is:** the indicator catalog for stock operations — what each number measures, a worked
numeric example, when it is useful, and the trap that makes it misleading. The core 12 are the
decision set; the rest are context. **Illustrative company `EXM3` at R$24; the fundamentals are not
illustrative financials. Brazil, rules as of 2026 — verify current data. Not financial advice.**

---

## 🧭 How to use this page

- **Start with liquidity.** If the stock fails [liquidity.md](liquidity.md), the rest does not matter.
- **Use the core 12 first.** They cover cash, debt, returns, growth, payout, and positioning.
- **Add the extended indicators for the sector.** Banks, retailers, utilities, and tech have
  different lenses.
- **Treat technical and macro indicators as context.** They do not override cash flow or solvency.
- **Write the bear case.** An indicator is useful when it changes the downside estimate, not when it
  confirms what you already believe.

**Illustrative numbers:** `EXM3` has 550M shares at R$24, R$8.4B revenue, R$2.35B EBITDA, R$0.67B
position is R$15,984; it is used only for position and liquidity examples.

## 🗂️ Index

<!-- begin table -->
| Group | Indicators |
| --- | --- |
| **Core** | [P/E](#-pe), [EV to EBITDA](#-ev-to-ebitda), [FCF yield](#-fcf-yield), [FCF conversion](#-fcf-conversion), [Sloan ratio](#-sloan-ratio), [net debt to EBITDA](#-net-debt-to-ebitda), [interest coverage](#-interest-coverage), [ROIC](#-roic), [revenue growth](#-revenue-growth), [payout ratio](#-payout-ratio), [ADTV](#-adtv), [short interest](#-short-interest) |
| **Valuation** | [forward P/E](#-forward-pe), [PEG](#-peg), [P/S](#-ps), [P/B](#-pb), [EV to EBIT](#-ev-to-ebit), [P/FCF](#-pfcf), [earnings yield](#-earnings-yield), [dividend yield](#-dividend-yield) |
| **Quality** | [ROE](#-roe), [ROA](#-roa), [gross margin](#-gross-margin), [EBITDA margin](#-ebitda-margin), [net margin](#-net-margin), [Beneish M-score](#-beneish-m-score), [Altman Z](#-altman-z), [Piotroski F](#-piotroski-f) |
| **Working capital** | [DSO](#-dso), [DIO](#-dio), [DPO](#-dpo), [cash conversion cycle](#-cash-conversion-cycle), [current ratio](#-current-ratio), [quick ratio](#-quick-ratio), [debt to equity](#-debt-to-equity), [maturity wall](#-maturity-wall) |
| **Growth** | [revenue CAGR](#-revenue-cagr), [EPS CAGR](#-eps-cagr), [same-store sales](#-same-store-sales), [market share](#-market-share), [online penetration](#-online-penetration), [LTV to CAC](#-ltv-to-cac), [net revenue retention](#-net-revenue-retention), [Rule of 40](#-rule-of-40) |
| **Market** | [RSI](#-rsi), [MACD](#-macd), [moving averages](#-moving-averages), [Bollinger Bands](#-bollinger-bands), [ATR](#-atr), [beta](#-beta), [max drawdown](#-max-drawdown), [relative strength](#-relative-strength), [OBV](#-obv), [VWAP](#-vwap) |
| **Positioning** | [free float](#-free-float), [bid-ask spread](#-bid-ask-spread), [days to exit](#-days-to-exit), [days to cover](#-days-to-cover), [borrow fee](#-borrow-fee), [options open interest](#-options-open-interest), [put-call ratio](#-put-call-ratio) |
| **Macro** | [Selic](#-selic), [IPCA](#-ipca), [credit delinquency](#-credit-delinquency), [FX](#-fx), [commodity price](#-commodity-price) |
| **Sector** | [bank NPL](#-bank-npl), [bank NIM](#-bank-nim), [bank capital ratio](#-bank-capital-ratio), [bank efficiency ratio](#-bank-efficiency-ratio), [retail inventory turnover](#-retail-inventory-turnover), [supplier finance](#-supplier-finance), [utility net debt](#-utility-net-debt) |
<!-- end table -->

## ✅ Core 12

### 📊 P/E

**Question:** How much am I paying for R$1 of accounting earnings?

**Formula:** price ÷ earnings per share.

**Example:** R$24.00 ÷ R$1.22 = **19.7x**; a peer at 14x means a ~40% premium. If half the EPS is a
one-off, normalized EPS is R$0.61 and the P/E is **39x**.

**Good sign:** stable earnings, low debt, and a multiple below its own history.

**Trap:** cyclical peak earnings, one-offs, and accounting profit that does not convert to cash.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 💰 EV to EBITDA

**Question:** What does the whole business cost relative to operating cash earnings?

**Formula:** (market cap + net debt) ÷ EBITDA.

**Example:** (R$13.2B + R$1.6B) ÷ R$2.35B = **6.3x**. If EBITDA is at a cycle peak and falls 50%,
the same EV is **12.6x**.

**Good sign:** low multiple with stable or rising EBITDA and manageable debt.

**Trap:** peak-cycle EBITDA, capitalized maintenance costs, and comparing companies with different
leasing/debt structures.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [PETR4](case-studies.md#-petr4).

### 💵 FCF yield

**Question:** How much free cash flow do I get per real invested?

**Formula:** free cash flow ÷ market cap.

**Example:** R$0.60B ÷ R$13.2B = **4.5%**. Against a 10.5% Selic, the stock needs growth or a
re-rating to beat cash.

**Good sign:** FCF yield above the real risk-free rate with a durable business.

**Trap:** capex cuts that flatter one year of FCF; cyclical cash flow at the top.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 🔁 FCF conversion

**Question:** Does accounting profit turn into cash?

**Formula:** free cash flow ÷ net income.

**Example:** R$0.60B ÷ R$0.67B = **90%**. A company with R$0.20B FCF and R$0.67B net income is at
**30%** — a warning.

**Good sign:** consistently 80–100%+.

**Trap:** capex-heavy growth can depress FCF temporarily; check whether capex is maintenance or
expansion.

**Seen in:** [AMER3](case-studies.md#-amer3), [IRBR3](case-studies.md#-irbr3).

### 🧮 Sloan ratio

**Question:** How much of reported earnings comes from accruals rather than cash?

**Formula:** (net income − free cash flow) ÷ total assets.

**Example:** (0.67 − 0.60) ÷ 12.9 = **0.5%**. If net income is R$1.0B, FCF is R$0.2B, and assets are
R$10B, the ratio is **8%** — a rough accrual flag.

**Good sign:** near zero or negative; earnings are backed by cash.

**Trap:** high-growth companies can have legitimate working-capital swings; compare with peers and
several years.

**Seen in:** [AMER3](case-studies.md#-amer3), [IRBR3](case-studies.md#-irbr3).

### 🧱 Net debt to EBITDA

**Question:** How many years of EBITDA does it take to pay net debt?

**Formula:** (gross debt − cash) ÷ EBITDA.

**Example:** R$1.6B ÷ R$2.35B = **0.68x**. At 4.5x, a 20% EBITDA drop and a refinancing wall can
become an equity problem.

**Good sign:** below 2x for a mature industrial, with long maturities.

**Trap:** EBITDA that excludes leases, maintenance, or one-off add-backs; cash that is trapped
abroad.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [AMER3](case-studies.md#-amer3).

### 🛟 Interest coverage

**Question:** How many times can EBIT cover interest?

**Formula:** EBIT ÷ interest expense.

**Example:** R$1.16B ÷ R$0.15B = **7.7x**. At 1.8x, a small margin miss can force a restructuring.

**Good sign:** above 4x with stable margins.

**Trap:** low rates can hide a refinancing problem; check the maturity schedule and floating-rate
exposure.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [CVCB3](case-studies.md#-cvcb3).

### 🏭 ROIC

**Question:** Does the business earn more than its cost of capital?

**Formula:** NOPAT ÷ invested capital.

**Example:** EBIT R$1.16B × (1 − 34%) = R$0.77B NOPAT; ÷ R$8.5B invested capital = **9%**. If WACC
is 11%, growth destroys value.

**Good sign:** ROIC above WACC for several years without leverage.

**Trap:** asset-light companies can look high-ROIC because the denominator is small; check
consistency.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 📈 Revenue growth

**Question:** Is the business growing, and is the growth real?

**Formula:** revenue growth = (current revenue ÷ prior revenue) − 1; separate same-store sales from
new stores.

**Example:** revenue +10%, same-store sales +4%, new stores +6%; market share 8.4% vs 8.0%. The
company is growing, but only 4 points are organic.

**Good sign:** positive same-store sales with stable or rising market share.

**Trap:** growth bought with discounts, credit, or acquisitions; revenue up while receivables rise
faster.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 💸 Payout ratio

**Question:** Is the dividend covered by earnings and cash?

**Formula:** dividends ÷ net income; also dividends ÷ free cash flow.

**Example:** R$0.33B ÷ R$0.67B = **49%** of earnings; ÷ R$0.60B FCF = **55%**. A 12% yield with a
150% FCF payout is a cut waiting to happen.

**Good sign:** below 80% of FCF with low debt.

**Trap:** paying dividends with debt or asset sales; a high yield can be a return **of** capital.

**Seen in:** [AMER3](case-studies.md#-amer3), [OIBR3](case-studies.md#-oibr3).

### 🌊 ADTV

**Question:** How much can I trade without moving the price?

**Formula:** average daily traded value over 20 sessions = average shares × price.

ADTV. A R$24M fund position is 50% of one day’s volume.

**Good sign:** position ≤ 20% of ADTV; lower is better.

**Trap:** average volume collapses in stress; the exit is smaller than the entry.

**Seen in:** [liquidity.md](liquidity.md#-gate), [dangers.md](dangers.md#-forced-liquidation).

### 🎮 Short interest

**Question:** How crowded is the short side?

**Formula:** shares sold short ÷ free float.

**Example:** 12M ÷ 385M float = **3.1%** — not crowded. A squeeze setup can be 60M ÷ 100M = **60%**
with 15 days to cover and a 30% borrow fee.

**Good sign for a short:** low short interest, available borrow, and a catalyst.

**Trap:** high short interest can mean the market sees the problem; it can also fuel a squeeze.

**Seen in:** [GME](case-studies.md#-gme), [VW](case-studies.md#-vw), [MGLU3](case-studies.md#-mglu3).

## 🧮 Valuation

### 📊 Forward P/E

**Question:** What am I paying for next year’s expected earnings?

**Formula:** price ÷ forward EPS.

**Example:** R$24 ÷ R$1.50 = **16x** vs 19.7x trailing. The market is already paying for growth.

**Good sign:** forward multiple below trailing with credible estimates.

**Trap:** optimistic guidance; forward EPS is an estimate, not a fact.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [PETR4](case-studies.md#-petr4).

### 📊 PEG

**Question:** Does the P/E make sense relative to growth?

**Formula:** P/E ÷ expected EPS growth rate.

**Example:** 19.7 ÷ 10.9 = **1.8**. Above ~1.5 is expensive unless the growth is durable.

**Good sign:** below 1 with a long runway.

**Trap:** high growth that is cyclical or acquired; PEG rewards optimistic growth estimates.

**Seen in:** [MGLU3](case-studies.md#-mglu3).

### 📊 P/S

**Question:** What am I paying per real of revenue?

**Formula:** market cap ÷ revenue.

**Example:** R$13.2B ÷ R$8.4B = **1.57x**. A low P/S with a 2% net margin is not cheap.

**Good sign:** low P/S with stable margins and low capital intensity.

**Trap:** revenue is not profit; low-margin retailers can look cheap on P/S forever.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [AMER3](case-studies.md#-amer3).

### 📊 P/B

**Question:** What am I paying for accounting equity?

**Formula:** price ÷ book value per share.

**Example:** R$24 ÷ R$9.36 = **2.56x**. A 0.4x P/B with a 3% ROE and 5x net debt is a value trap, not
a bargain.

**Good sign:** P/B below 1 with a mid-teens ROE and conservative leverage, usually banks or
asset-heavy companies.

**Trap:** book value can be overstated; low P/B + low ROE + high debt is a warning.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [PETR4](case-studies.md#-petr4).

### 💰 EV to EBIT

**Question:** What does the operating business cost relative to operating profit?

**Formula:** EV ÷ EBIT.

**Example:** R$14.8B ÷ R$1.16B = **12.8x**. Less forgiving than EV/EBITDA because it includes
depreciation.

**Good sign:** stable EBIT and low capex intensity.

**Trap:** heavy capex can make EBIT look good while cash flow is weak.

**Seen in:** [CVCB3](case-studies.md#-cvcb3), [OIBR3](case-studies.md#-oibr3).

### 💵 P/FCF

**Question:** What am I paying for cash flow?

**Formula:** market cap ÷ free cash flow.

**Example:** R$13.2B ÷ R$0.60B = **22x**. Better than P/E for capex-heavy businesses, but only if
capex is maintenance-level.

**Good sign:** low P/FCF with stable capex.

**Trap:** one year of deferred capex flatters FCF.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 📉 Earnings yield

**Question:** What is the accounting earnings return on the share price?

**Formula:** EPS ÷ price; the inverse of P/E.

**Example:** R$1.22 ÷ R$24 = **5.1%**. Compare with the real bond yield, not just the nominal Selic.

**Good sign:** above the real risk-free rate with stable earnings.

**Trap:** the same accounting-earnings trap as P/E; a high yield can be a cyclical peak.

**Seen in:** [PETR4](case-studies.md#-petr4), [AMER3](case-studies.md#-amer3).

### 💵 Dividend yield

**Question:** How much cash is paid per share?

**Formula:** dividend per share ÷ price.

**Example:** R$0.60 ÷ R$24 = **2.5%**. It is not total return; the payout and the business matter.

**Good sign:** covered by FCF, with low debt and a clear policy.

**Trap:** a 12% yield funded by debt or a collapsing share price.

**Seen in:** [AMER3](case-studies.md#-amer3), [OIBR3](case-studies.md#-oibr3).

## 🏭 Quality and accounting

### 🏭 ROE

**Question:** How much profit does the company generate on equity?

**Formula:** net income ÷ shareholders’ equity.

**Example:** R$0.67B ÷ R$5.15B = **13%**. Leverage can flatter ROE; compare with ROIC.

**Good sign:** mid-teens or higher without excessive debt.

**Trap:** buybacks and leverage shrink equity and inflate ROE.

**Seen in:** [PETR4](case-studies.md#-petr4), [OIBR3](case-studies.md#-oibr3).

### 🏭 ROA

**Question:** How efficiently does the company use its assets?

**Formula:** net income ÷ total assets.

**Example:** R$0.67B ÷ R$12.9B = **5.2%**. Low-margin, asset-heavy businesses need volume.

**Good sign:** stable or rising ROA with low leverage.

**Trap:** asset sales or write-downs can distort the denominator.

**Seen in:** [AMER3](case-studies.md#-amer3), [CVCB3](case-studies.md#-cvcb3).

### 📏 Gross margin

**Question:** Does the company have pricing power after direct costs?

**Formula:** (revenue − cost of goods sold) ÷ revenue.

**Example:** (8.4 − 6.13) ÷ 8.4 = **27%**. A fall from 32% to 27% is a competitive warning.

**Good sign:** stable or rising gross margin with volume growth.

**Trap:** input-cost inflation can be passed through with a lag; one quarter is not a trend.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 📏 EBITDA margin

**Question:** How much operating cash earnings before depreciation and interest?

**Formula:** EBITDA ÷ revenue.

**Example:** R$2.35B ÷ R$8.4B = **28%**. It excludes D&A and interest; it is not free cash flow.

**Good sign:** stable or rising margin with low capex.

**Trap:** add-backs and leases can make EBITDA look better than cash flow.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [PETR4](case-studies.md#-petr4).

### 📏 Net margin

**Question:** How much profit remains after all costs?

**Formula:** net income ÷ revenue.

**Example:** R$0.67B ÷ R$8.4B = **8%**. A thin margin leaves little room for a cost shock.

**Good sign:** stable or rising net margin with low debt.

**Trap:** one-off tax credits or asset sales can inflate one year.

**Seen in:** [AMER3](case-studies.md#-amer3), [CVCB3](case-studies.md#-cvcb3).

### 🧾 Beneish M-score

**Question:** Do the accounting ratios suggest earnings manipulation?

**Formula:** a weighted combination of eight accounting ratios; the usual flag is **above −1.78**.

**Example:** an M-score of **−2.2** is not a flag; **−1.5** is. It is a screening flag, not proof.

**Good sign:** below the threshold for several years.

**Trap:** it is calibrated on US data and can produce false positives; use it only when something
already smells wrong.

**Seen in:** [AMER3](case-studies.md#-amer3), [IRBR3](case-studies.md#-irbr3).

### 🧾 Altman Z

**Question:** How close is the company to financial distress?

**Formula:** a weighted combination of working capital, retained earnings, EBIT, equity, and sales;
zones vary by model.

**Example:** **2.4** is the grey zone; **1.2** is distress. Use the manufacturing model only where it
fits.

**Good sign:** above 3 for a mature industrial.

**Trap:** banks, insurers, and asset-light companies need different models.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [CVCB3](case-studies.md#-cvcb3).

### 🧾 Piotroski F

**Question:** Is the fundamental trend improving?

**Formula:** nine binary tests on profitability, leverage, and operating efficiency; score 0–9.

**Example:** **7/9** is strong; **2/9** is weak. It is a trend score, not a valuation.

**Good sign:** 8–9 with a cheap multiple.

**Trap:** it can reward a one-year bounce in a structurally declining business.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [MGLU3](case-studies.md#-mglu3).

## 🧱 Working capital and debt

### ⏳ DSO

**Question:** How long does it take to collect receivables?

**Formula:** receivables ÷ revenue × 365.

**Example:** R$1.2B ÷ R$8.4B × 365 = **52 days**. If revenue grows 20% but receivables grow 50%, DSO
rises and cash conversion weakens.

**Good sign:** stable or falling DSO versus peers.

**Trap:** channel stuffing and loose credit can boost revenue and receivables together.

**Seen in:** [AMER3](case-studies.md#-amer3), [CVCB3](case-studies.md#-cvcb3).

### ⏳ DIO

**Question:** How long does inventory sit before it is sold?

**Formula:** inventory ÷ cost of goods sold × 365.

**Example:** R$0.6B ÷ R$6.13B × 365 = **36 days**. Rising DIO with falling same-store sales is a
warning.

**Good sign:** stable or falling DIO with growing sales.

**Trap:** stockpiling ahead of price increases can be rational; check the reason.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### ⏳ DPO

**Question:** How long does the company take to pay suppliers?

**Formula:** payables ÷ cost of goods sold × 365.

**Example:** R$1.0B ÷ R$6.13B × 365 = **60 days**. A jump to 119 days can be supplier finance or a
liquidity squeeze.

**Good sign:** stable DPO in line with peers.

**Trap:** stretching suppliers is a hidden loan; it reverses when suppliers demand cash.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 🔄 Cash conversion cycle

**Question:** How long is cash tied up in the operating cycle?

**Formula:** DSO + DIO − DPO.

**Example:** 52 + 36 − 60 = **28 days**. A negative CCC can be a strong business model or a warning
that suppliers are financing the company.

**Good sign:** stable or falling CCC.

**Trap:** negative CCC funded by supplier finance can reverse quickly.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 💧 Current ratio

**Question:** Can short-term assets cover short-term liabilities?

**Formula:** current assets ÷ current liabilities.

**Example:** R$4.0B ÷ R$2.15B = **1.86**. Below 1 means working capital is tight.

**Good sign:** above 1.5 for a mature company.

**Trap:** inventory and receivables may be hard to convert to cash.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [AMER3](case-studies.md#-amer3).

### 💧 Quick ratio

**Question:** Can liquid assets cover short-term liabilities without selling inventory?

**Formula:** (current assets − inventory) ÷ current liabilities.

**Example:** (4.0 − 0.6) ÷ 2.15 = **1.58**. A quick ratio below 0.5 is a liquidity warning.

**Good sign:** above 1 with low short-term debt.

**Trap:** receivables can be just as illiquid as inventory in a crisis.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [AMER3](case-studies.md#-amer3).

### 🧱 Debt to equity

**Question:** How much debt is used relative to equity?

**Formula:** total debt ÷ shareholders’ equity.

**Example:** R$1.6B ÷ R$5.15B = **0.31x**. Low leverage, but check the maturity schedule.

**Good sign:** low and stable, with long maturities.

**Trap:** off-balance-sheet liabilities, leases, and supplier finance can hide leverage.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [AMER3](case-studies.md#-amer3).

### 📅 Maturity wall

**Question:** How much debt must be refinanced soon?

**Formula:** debt due in the next 12 months ÷ total debt.

**Example:** 10% due in 12 months is manageable; 30% with negative FCF is a refinancing wall.

**Good sign:** spread maturities and no large bullet in a bad market.

**Trap:** “cash” that is trapped or restricted; refinancing at a much higher rate.

**Seen in:** [OIBR3](case-studies.md#-oibr3), [AMER3](case-studies.md#-amer3).

## 📈 Growth and business quality

### 📈 Revenue CAGR

**Question:** How fast has revenue grown over several years?

**Formula:** (ending revenue ÷ starting revenue)^(1/years) − 1.

**Example:** R$8.4B vs R$5.0B over 5 years = **10.9%**. Compare with inflation and peers.

**Good sign:** above inflation with stable margins.

**Trap:** growth from acquisitions or price inflation, not volume.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [AMER3](case-studies.md#-amer3).

### 📈 EPS CAGR

**Question:** How fast has earnings per share grown?

**Formula:** (ending EPS ÷ starting EPS)^(1/years) − 1.

**Example:** R$1.22 vs R$0.83 over 5 years = **8%**. Buybacks can flatter EPS without profit growth.

**Good sign:** EPS growth roughly in line with revenue and ROIC.

**Trap:** buybacks, one-offs, and accounting changes.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [PETR4](case-studies.md#-petr4).

### 🏬 Same-store sales

**Question:** Are existing stores growing?

**Formula:** sales from stores open at least 12 months ÷ prior-year sales − 1.

**Example:** +4% same-store vs +10% total means new stores contributed 6 points.

**Good sign:** positive same-store sales with stable margins.

**Trap:** price inflation, delivery, or credit can mask falling traffic.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 🧩 Market share

**Question:** Is the company winning or losing in its market?

**Formula:** company revenue ÷ total market revenue.

**Example:** 8.4% vs 8.0% last year = **+0.4pp**. A rising share with falling margins can be bought
growth.

**Good sign:** rising share with stable or rising margins.

**Trap:** share gains bought with discounts or credit.

**Seen in:** [AMER3](case-studies.md#-amer3), [Blockbuster](case-studies.md#-blockbuster).

### 🌐 Online penetration

**Question:** How much of the market is moving online?

**Formula:** online sales ÷ total market sales.

**Example:** 20% vs 15% last year. A rapid shift can hurt store-heavy retailers.

**Good sign:** the company is gaining online share without losing money.

**Trap:** online growth with negative unit economics.

**Seen in:** [Blockbuster](case-studies.md#-blockbuster), [AMER3](case-studies.md#-amer3).

### 🎯 LTV to CAC

**Question:** Is customer acquisition economically viable?

**Formula:** lifetime value ÷ customer acquisition cost.

**Example:** R$300 ÷ R$100 = **3x**; payback 12 months. Below 1x destroys value.

**Good sign:** above 3x with a short payback.

**Trap:** LTV assumptions are easy to inflate; churn and discount rates matter.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [Blockbuster](case-studies.md#-blockbuster).

### 🔁 Net revenue retention

**Question:** How much revenue grows from existing customers?

**Formula:** recurring revenue from existing customers this year ÷ last year.

**Example:** **110%** means existing customers spend 10% more; below 100% means churn is outpacing
expansion.

**Good sign:** above 100% with low churn.

**Trap:** price increases can mask customer losses.

**Seen in:** [MGLU3](case-studies.md#-mglu3).

### 🚀 Rule of 40

**Question:** Does growth plus profitability clear a rough quality bar?

**Formula:** revenue growth % + FCF margin %.

**Example:** 15% growth + 10% FCF margin = **25**; below 40 is a flag for a high-growth software
business.

**Good sign:** above 40 with durable growth.

**Trap:** it is a heuristic, not a valuation; a low-growth company can still be a good investment.

**Seen in:** [MGLU3](case-studies.md#-mglu3).

## 📉 Market and technical

### 📉 RSI

**Question:** Is the recent move stretched?

**Formula:** 14-day relative strength index, 0–100.

**Example:** **72** is overbought; **28** is oversold. In a strong trend, RSI can stay extreme for
weeks.

**Good sign:** use it for timing, not thesis.

**Trap:** overbought can get more overbought; oversold can go to zero.

**Seen in:** [GME](case-studies.md#-gme), [MGLU3](case-studies.md#-mglu3).

### 📉 MACD

**Question:** Is momentum accelerating or fading?

**Formula:** difference between fast and slow moving averages, with a signal line.

**Example:** MACD line 0.80 above signal 0.50 = positive momentum; the cross is late.

**Good sign:** confirmation of a trend you already understand.

**Trap:** whipsaws in sideways markets.

**Seen in:** [GME](case-studies.md#-gme), [Tesla](case-studies.md#-tesla).

### 📉 Moving averages

**Question:** Is the price above or below its recent trend?

**Formula:** average close over 50 or 200 sessions.

**Example:** price R$24 > MA50 R$22.50 > MA200 R$21.00 = uptrend. It says nothing about value.

**Good sign:** trend confirmation.

**Trap:** lagging; a trend can reverse before the average crosses.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [Tesla](case-studies.md#-tesla).

### 📉 Bollinger Bands

**Question:** Is volatility expanding or contracting?

**Formula:** 20-day moving average ± 2 standard deviations.

**Example:** upper band R$25.10, lower R$22.90; price near the upper band is not a sell signal by
itself.

**Good sign:** volatility context.

**Trap:** bands expand after a move; they do not predict the direction.

**Seen in:** [GME](case-studies.md#-gme), [MGLU3](case-studies.md#-mglu3).

### 📉 ATR

**Question:** How much does the stock move in a normal day?

**Formula:** average true range over 14 sessions.

**Example:** ATR R$0.72 on a R$24 stock = **3%**. A 2×ATR stop is R$1.44, or 6%.

**Good sign:** position sizing and stop distance.

**Trap:** volatility is not risk direction; a low ATR can precede a gap.

**Seen in:** [GME](case-studies.md#-gme), [VALE3](case-studies.md#-vale3).

### 📉 Beta

**Question:** How much does the stock move relative to the index?

**Formula:** covariance with the index ÷ index variance.

**Example:** beta **1.1** means a 10% index move is roughly an 11% stock move, on average.

**Good sign:** context for portfolio risk.

**Trap:** beta is historical and unstable; a low-beta stock can gap on company news.

**Seen in:** [PETR4](case-studies.md#-petr4), [VALE3](case-studies.md#-vale3).

### 📉 Max drawdown

**Question:** How bad was the worst peak-to-trough loss?

**Formula:** (trough − peak) ÷ peak.

**Example:** R$30 → R$18 = **−40%**. If you cannot hold through that, the position is too large.

**Good sign:** a drawdown you can survive.

**Trap:** the past drawdown may be smaller than the next one.

**Seen in:** [AMER3](case-studies.md#-amer3), [OIBR3](case-studies.md#-oibr3).

### 📉 Relative strength

**Question:** Is the stock outperforming its index?

**Formula:** stock return − index return over a window.

**Example:** +18% vs +10% = **+8pp** relative strength.

**Good sign:** leadership with fundamentals.

**Trap:** momentum can reverse; relative strength is not valuation.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [Tesla](case-studies.md#-tesla).

### 📉 OBV

**Question:** Is volume confirming the price move?

**Formula:** cumulative volume, added on up days and subtracted on down days.

**Example:** price +10% with OBV rising = participation; price +10% with OBV flat = weak.

**Good sign:** volume confirmation.

**Trap:** block trades and index flows can distort it.

**Seen in:** [GME](case-studies.md#-gme), [MGLU3](case-studies.md#-mglu3).

### 📉 VWAP

**Question:** What is the average execution price weighted by volume?

**Formula:** cumulative price × volume ÷ cumulative volume.

**Example:** VWAP R$23.80; buying at R$24.10 is 1.3% above the day’s average.

**Good sign:** execution benchmark for large orders.

**Trap:** intraday VWAP is not a valuation.

**Seen in:** [liquidity.md](liquidity.md#-position-impact).

## 🌊 Liquidity and positioning

### 🌊 Free float

**Question:** How many shares are actually available to trade?

**Formula:** shares available to the public ÷ total shares.

**Example:** 70% float is healthy; 15% float makes the stock easier to squeeze and manipulate.

**Good sign:** high free float and broad ownership.

**Trap:** low float can make a small order move the price; index inclusion can change it.

**Seen in:** [GME](case-studies.md#-gme), [VW](case-studies.md#-vw).

### 🌊 Bid-ask spread

**Question:** What does it cost to cross the spread?

**Formula:** (ask − bid) ÷ midpoint.

**Example:** bid R$23.98, ask R$24.02, mid R$24.00 = **0.17%**. A 3% spread is a 3% cost before the
trade works.

**Good sign:** tight spread and deep book.

**Trap:** the displayed spread can widen exactly when you need to sell.

**Seen in:** [liquidity.md](liquidity.md#-gate), [dangers.md](dangers.md#-forced-liquidation).

### 🌊 Days to exit

**Question:** How long will it take to sell the position?

**Formula:** position value ÷ (ADTV × participation rate).

**Example:** R$24M ÷ (R$48M × 20%) = **2.5 days**. A R$240k position in a R$2M ADTV stock is 12% of
one day’s volume.

**Good sign:** under 1–2 days at a conservative participation rate.

**Trap:** stressed ADTV is lower than the average; the exit can take much longer.

**Seen in:** [liquidity.md](liquidity.md#-position-impact), [dangers.md](dangers.md#-forced-liquidation).

### 🌊 Days to cover

**Question:** How many days of volume would it take shorts to cover?

**Formula:** shares short ÷ average daily volume.

**Example:** 12M ÷ 2M = **6 days**; a squeeze setup at 30M ÷ 2M = **15 days**.

**Good sign for a short:** low days to cover.

**Trap:** volume spikes during a squeeze; the average understates the difficulty.

**Seen in:** [GME](case-studies.md#-gme), [VW](case-studies.md#-vw).

### 🌊 Borrow fee

**Question:** How expensive is it to borrow the shares?

**Formula:** annual borrow rate × position value.

**Example:** 1.5% p.a. on R$15,984 = **R$239.76**; 30% p.a. = **R$4,795.20**.

**Good sign for a short:** liquid borrow and a low fee.

**Trap:** the fee can spike or the lender can recall the shares.


### 🌊 Options open interest

**Question:** How much option positioning is stacked at a strike?

**Formula:** number of open contracts at each strike/expiry.

**Example:** 50k calls at R$30 vs 30k puts at R$20; large call OI can amplify a squeeze through dealer
hedging.

**Good sign for a short:** low call OI and liquid options.

**Trap:** OI is not directional; it can be hedged or expired.

**Seen in:** [GME](case-studies.md#-gme), [Tesla](case-studies.md#-tesla).

### 🌊 Put-call ratio

**Question:** Is positioning skewed to puts or calls?

**Formula:** put open interest ÷ call open interest.

**Example:** 30k ÷ 50k = **0.6**; below 1 means more calls than puts.

**Good sign:** context, not a signal.

**Trap:** hedging and market-making distort the ratio.

**Seen in:** [GME](case-studies.md#-gme), [Tesla](case-studies.md#-tesla).

## 🌍 Macro

### 🌍 Selic

**Question:** What is the risk-free nominal rate?

**Formula:** the B3 Selic target/effective rate.

**Example:** 10.5% Selic vs a 5.1% earnings yield means cash is competitive before risk.

**Good sign for stocks:** falling Selic with controlled inflation.

**Trap:** a high Selic can stay high longer than the market expects.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [PETR4](case-studies.md#-petr4).

### 🌍 IPCA

**Question:** What is the inflation rate?

**Formula:** official consumer price index, 12-month change.

**Example:** 4.5% IPCA and a 5.1% earnings yield = **0.6% real** earnings yield.

**Good sign:** stable inflation with falling rates.

**Trap:** food and energy shocks can force the central bank to keep rates high.

**Seen in:** [MGLU3](case-studies.md#-mglu3), [AMER3](case-studies.md#-amer3).

### 🌍 Credit delinquency

**Question:** Are consumers and companies paying their debts?

**Formula:** overdue loans ÷ total loans, from the central bank series.

**Example:** 5.5% and rising is a warning for retailers and banks; 8% is stress.

**Good sign for a retailer:** peaking delinquency and falling rates.

**Trap:** delinquency lags the economy; it can improve after the stock has already moved.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 🌍 FX

**Question:** What is the exchange rate, and who benefits?

**Formula:** BRL per USD, or the relevant cross.

**Example:** USD/BRL 5.40; a exporter gains from a weaker BRL, an importer loses.

**Good sign:** a currency level the company can hedge.

**Trap:** a weaker BRL can boost revenue and hurt margins at the same time.

**Seen in:** [PETR4](case-studies.md#-petr4), [VALE3](case-studies.md#-vale3).

### 🌍 Commodity price

**Question:** Where is the underlying commodity in its cycle?

**Formula:** spot and forward price per unit; compare with the cost curve.

**Example:** iron ore at $100/t; a 30% fall can turn a low-cost producer into a loss-maker.

**Good sign:** low-cost producer with a strong balance sheet through the cycle.

**Trap:** low P/E at peak commodity prices is a classic trap.

**Seen in:** [VALE3](case-studies.md#-vale3), [PETR4](case-studies.md#-petr4).

## 🏦 Sector lenses

### 🏦 Bank NPL

**Question:** What share of the loan book is non-performing?

**Formula:** non-performing loans ÷ total loans.

**Example:** 3.2% NPL with rising coverage is healthier than 3.2% with falling coverage.

**Good sign:** stable NPL and adequate provisioning.

**Trap:** restructuring can hide bad loans; compare with peers.

**Seen in:** [dangers.md](dangers.md#-debt-walls), [case-studies.md](case-studies.md#-lessons).

### 🏦 Bank NIM

**Question:** How much does the bank earn on its loan book?

**Formula:** net interest income ÷ average earning assets.

**Example:** 5.1% NIM with 3.2% NPL; a high NIM can be compensation for risk.

**Good sign:** stable NIM with low NPL.

**Trap:** high NIM from risky lending can reverse quickly.

**Seen in:** [dangers.md](dangers.md#-debt-walls).

### 🏦 Bank capital ratio

**Question:** Is the bank capitalized for its risks?

**Formula:** regulatory capital ÷ risk-weighted assets.

**Example:** 15.5% capital ratio vs a regulatory minimum; a thin buffer is a warning.

**Good sign:** comfortably above requirements.

**Trap:** risk weights can change; capital can be consumed by losses.

**Seen in:** [dangers.md](dangers.md#-debt-walls).

### 🏦 Bank efficiency ratio

**Question:** How much of income is consumed by costs?

**Formula:** operating expenses ÷ operating income.

**Example:** 42% is efficient; 70% leaves little room for provisioning.

**Good sign:** falling efficiency ratio with stable NIM.

**Trap:** cost cuts can damage the franchise.

**Seen in:** [dangers.md](dangers.md#-debt-walls).

### 🛒 Retail inventory turnover

**Question:** How fast does inventory sell?

**Formula:** cost of goods sold ÷ average inventory.

**Example:** 8x per year, or about 46 days; a fall to 5x means slower sales or overstock.

**Good sign:** stable or rising turnover with positive same-store sales.

**Trap:** deep discounts can clear inventory and destroy margin.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### 🛒 Supplier finance

**Question:** Is the company stretching suppliers to fund itself?

**Formula:** DPO vs peers; payables growth vs COGS growth.

**Example:** DPO 119 days vs 60 peers, with payables +40% and COGS +5% — a hidden funding source.

**Good sign:** DPO in line with peers.

**Trap:** supplier finance can disappear when suppliers demand cash.

**Seen in:** [AMER3](case-studies.md#-amer3), [MGLU3](case-studies.md#-mglu3).

### ⚡ Utility net debt

**Question:** How leveraged is a regulated utility?

**Formula:** net debt ÷ EBITDA; compare with the regulatory asset base.

**Example:** 3.0x net debt/EBITDA and an 80% payout leaves little room for a rate shock.

**Good sign:** regulated cash flow with a manageable maturity ladder.

**Trap:** regulatory resets and capex can change the allowed return.

**Seen in:** [dangers.md](dangers.md#-debt-walls).

## 🧪 Scenario map

<!-- begin table -->
| Scenario | First indicators |
| --- | --- |
| **Accounting warning** | [FCF conversion](#-fcf-conversion), [Sloan ratio](#-sloan-ratio), [DSO](#-dso), [DPO](#-dpo), [Beneish](#-beneish-m-score) |
| **Debt wall** | [net debt to EBITDA](#-net-debt-to-ebitda), [interest coverage](#-interest-coverage), [maturity wall](#-maturity-wall) |
| **Value trap** | [P/E](#-pe), [P/B](#-pb), [ROIC](#-roic), [revenue growth](#-revenue-growth), [debt to equity](#-debt-to-equity) |
| **Cyclical peak** | [EV to EBITDA](#-ev-to-ebitda), [EBITDA margin](#-ebitda-margin), [inventory turnover](#-retail-inventory-turnover), [commodity price](#-commodity-price) |
| **Disruption** | [same-store sales](#-same-store-sales), [market share](#-market-share), [online penetration](#-online-penetration), [gross margin](#-gross-margin) |
| **Short squeeze** | [short interest](#-short-interest), [days to cover](#-days-to-cover), [borrow fee](#-borrow-fee), [free float](#-free-float), [options OI](#-options-open-interest) |
| **Liquidity trap** | [ADTV](#-adtv), [free float](#-free-float), [bid-ask spread](#-bid-ask-spread), [days to exit](#-days-to-exit) |
| **Macro de-rating** | [Selic](#-selic), [IPCA](#-ipca), [earnings yield](#-earnings-yield), [credit delinquency](#-credit-delinquency) |
| **Bank** | [bank NPL](#-bank-npl), [bank NIM](#-bank-nim), [bank capital ratio](#-bank-capital-ratio), [bank efficiency ratio](#-bank-efficiency-ratio) |
| **Retail** | [same-store sales](#-same-store-sales), [inventory turnover](#-retail-inventory-turnover), [supplier finance](#-supplier-finance) |
| **Commodity** | [EV to EBITDA](#-ev-to-ebitda), [commodity price](#-commodity-price), [FX](#-fx) |
<!-- end table -->

## ⚠️ Anti-checklist

- **Do not use P/E alone.** It is a price, not a business.
- **Do not use a low P/B as a buy signal.** Low P/B + low ROE + high debt is a trap.
- **Do not use a high dividend yield as a thesis.** Check the payout versus FCF.
- **Do not use RSI or moving averages as a thesis.** They are timing context.
- **Do not use short interest as a directional signal.** It cuts both ways.
- **Do not use one year of FCF.** Capex and working capital swing.
- **Do not compare banks, retailers, and utilities with the same multiples.**
- **Do not ignore liquidity.** A great multiple in an illiquid stock is not a great investment.
- **Do not predict a squeeze with fundamentals.** Use positioning, float, borrow, and options.
- **Do not confuse a good company with a good price.**

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [liquidity.md](liquidity.md) — the first gate.
- [dangers.md](dangers.md) — the failure modes.
- [case-studies.md](case-studies.md) — the numeric cases.
- [flows.md](flows.md) — how a move spreads.
- [buy/readme.md](buy/readme.md) — the entry process.
- [sell/readme.md](sell/readme.md) — the exit process.
- [fees-taxes.md](fees-taxes.md) — the cost layer.

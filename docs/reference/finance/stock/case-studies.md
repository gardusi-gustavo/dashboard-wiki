# 🧪 Case studies — abrupt moves

**What this is:** a hindsight library of abrupt price moves, split into **positioning/squeeze** and
**company-specific shocks**, with the indicators that could have flagged them and the indicators that
gave false comfort. **Illustrative history, not a recommendation. Verify dates, prices, and facts.**

---

## 🧭 How to read

- **A flag is not a forecast.** These indicators look obvious after the fact.
- **Separate the setup from the trigger.** You can see crowding; you cannot see the timing.
- **Ask what would not have helped.** A low P/E or high dividend often gave false comfort.
- **Use the case as a stress test,** not as a template for the next trade.

## 🌀 Short squeeze table

Short squeezes are **positioning events**, not company events. The company can be good or bad; the
float, borrow, and crowding decide the path.

<!-- begin table -->
| Case | Move | Setup | Flow | Indicators that could flag | False comfort |
| --- | --- | --- | --- | --- | --- |
| [GME](case-studies.md#-gme) | >+1,000% in weeks | Short interest above float, retail buying, call options | Public social + retail + options | [short interest](indicators.md#-short-interest), [days to cover](indicators.md#-days-to-cover), [borrow fee](indicators.md#-borrow-fee), [free float](indicators.md#-free-float), [options OI](indicators.md#-options-open-interest) | P/E, FCF, valuation |
| [VW](case-studies.md#-vw) | Violent squeeze | Porsche corner, hidden ownership | Institutional/strategic | [short interest](indicators.md#-short-interest), [free float](indicators.md#-free-float), [borrow fee](indicators.md#-borrow-fee) | Fundamentals |
| [Tesla](case-studies.md#-tesla) | Massive rally | Crowded short + momentum + retail flows | Public social + options | [short interest](indicators.md#-short-interest), [days to cover](indicators.md#-days-to-cover), [borrow fee](indicators.md#-borrow-fee), [options OI](indicators.md#-options-open-interest) | Valuation |
| [KaloBios](case-studies.md#-kalobios) | Parabolic | Low float, crowded short, news | News + low float | [free float](indicators.md#-free-float), [short interest](indicators.md#-short-interest), [borrow fee](indicators.md#-borrow-fee) | Fundamentals |
| [Herbalife](case-studies.md#-herbalife) | Squeeze | Public short campaign + crowded short | Media + public positioning | [short interest](indicators.md#-short-interest), [days to cover](indicators.md#-days-to-cover), [borrow fee](indicators.md#-borrow-fee) | Valuation |
| [MGLU3](case-studies.md#-mglu3) | Huge rally | Momentum + short covering | Retail/social + momentum | [short interest](indicators.md#-short-interest), [days to cover](indicators.md#-days-to-cover), [ADTV](indicators.md#-adtv) | P/E, P/S |
| [IRBR3](case-studies.md#-irbr3) | Rally on rumour | False Buffett rumour + positioning | Media/rumour | [short interest](indicators.md#-short-interest), [borrow fee](indicators.md#-borrow-fee), source verification | Fundamentals |
<!-- end table -->

## 🏭 Company shock table

Company shocks are about the business — accounting, debt, disruption, politics, legal, and
environmental risk. These are the cases where a low multiple can be a trap.

<!-- begin table -->
| Case | Move | Setup | Flow | Indicators that could flag | False comfort |
| --- | --- | --- | --- | --- | --- |
| [AMER3](case-studies.md#-amer3) | ~−77% in a day; >95% destroyed | Accounting inconsistencies, hidden supplier debt | Company disclosure + accounting | [FCF conversion](indicators.md#-fcf-conversion), [Sloan](indicators.md#-sloan-ratio), [DPO](indicators.md#-dpo), [DSO](indicators.md#-dso), [same-store sales](indicators.md#-same-store-sales) | Low P/E, EV/EBITDA, dividend yield |
| [OIBR3](case-studies.md#-oibr3) | Near zero | Judicial recovery, debt wall, dilution | Company disclosure + debt | [net debt to EBITDA](indicators.md#-net-debt-to-ebitda), [interest coverage](indicators.md#-interest-coverage), [maturity wall](indicators.md#-maturity-wall) | Low P/B |
| [CVCB3](case-studies.md#-cvcb3) | ~−70% over weeks | Restatement + COVID travel collapse | Company disclosure + accounting | [DSO](indicators.md#-dso), [FCF conversion](indicators.md#-fcf-conversion), [net debt to EBITDA](indicators.md#-net-debt-to-ebitda) | P/E, brand strength |
| [IRBR3](case-studies.md#-irbr3) | ~−80% over weeks | Aggressive accounting, short-seller report | Media + accounting | [DSO](indicators.md#-dso), [FCF conversion](indicators.md#-fcf-conversion), [Sloan](indicators.md#-sloan-ratio), management turnover | P/E, market darling status |
| [PETR4](case-studies.md#-petr4) | ~−21% in a day | State intervention / CEO removal | Political/legal | [beta](indicators.md#-beta), [P/E](indicators.md#-pe), governance history | Low P/E, P/B, dividend yield |
| [JBSS3](case-studies.md#-jbss3) | ~−33% in a day | Political/legal shock | Political/legal + media | [beta](indicators.md#-beta), governance, leverage | Valuation |
| [VALE3](case-studies.md#-vale3) | Double-digit drop | Environmental/operational disaster | Environmental/operational | [max drawdown](indicators.md#-max-drawdown), safety record, legal contingencies | Low P/E, high yield |
| [MGLU3](case-studies.md#-mglu3) | Rally then collapse | E-commerce re-rating, Selic up, growth slowdown | Retail/social + macro | [P/E](indicators.md#-pe), [P/S](indicators.md#-ps), [FCF yield](indicators.md#-fcf-yield), [Selic](indicators.md#-selic) | Momentum, RSI |
| [Blockbuster](case-studies.md#-blockbuster) | Structural decline | Streaming/Netflix | Industry trend | [same-store sales](indicators.md#-same-store-sales), [market share](indicators.md#-market-share), [online penetration](indicators.md#-online-penetration) | Cheap multiple |
| [Nokia](case-studies.md#-nokia) | Structural decline | Smartphone shift | Industry trend | [market share](indicators.md#-market-share), [revenue CAGR](indicators.md#-revenue-cagr), gross margin | Low P/E |
<!-- end table -->

## 🎮 GME

- **What happened:** a heavily shorted retailer became the centre of a retail buying wave; the stock
  rose more than 1,000% in weeks.
- **Setup:** reported short interest above the free float, low float, high days to cover, expensive
  borrow, and large call open interest.
- **What was visible:** the positioning data. The market could see the crowding.
- **What was not visible:** the Reddit/retail coordination, the timing, and the size.
- **False comfort:** P/E, FCF, and valuation. The company’s fundamentals did not drive the move.
- **Lesson:** a squeeze is a positioning event. Do not use fundamentals to predict it, and do not use
  it to justify a long-term buy.

## 🚗 VW

- **What happened:** Porsche’s hidden stake turned a crowded short into a corner; the stock squeezed.
- **Setup:** low free float, hidden strategic ownership, and shorts that could not borrow enough shares.
- **What was visible:** borrow tightness, price strength, and disclosures — late.
- **What was not visible:** Porsche’s intent until the announcement.
- **False comfort:** fundamentals. The company’s value did not set the path.
- **Lesson:** a corner is built quietly; borrow data is a clue, not a warning system.

## ⚡ Tesla

- **What happened:** a heavily shorted, high-growth stock rallied massively as shorts covered and
  retail/options flow amplified the move.
- **Setup:** high short interest, expensive borrow, strong momentum, and large call open interest.
- **What was visible:** short interest, borrow fee, options OI, and volume.
- **What was not visible:** the timing and the size of the covering.
- **False comfort:** valuation. The stock was expensive before it went higher.
- **Lesson:** a squeeze can run far beyond what fundamentals justify.

## 🧪 KaloBios

- **What happened:** a low-float, heavily shorted biotech became a parabolic squeeze after news and
  retail attention.
- **Setup:** tiny float, crowded short, and a catalyst.
- **What was visible:** [free float](indicators.md#-free-float), [short interest](indicators.md#-short-interest),
  and borrow cost.
- **What was not visible:** the timing and the durability of the news.
- **False comfort:** fundamentals; the move was positioning.
- **Lesson:** low float is the accelerant.

## 🥤 Herbalife

- **What happened:** a public short campaign in a crowded short created a squeeze as buyers and
  existing shorts fought for shares.
- **Setup:** high short interest, public debate, and a catalyst.
- **What was visible:** [short interest](indicators.md#-short-interest), [days to cover](indicators.md#-days-to-cover),
  and borrow cost.
- **What was not visible:** how long the public campaign would run.
- **False comfort:** valuation; the debate was about positioning and credibility.
- **Lesson:** a public short campaign can become a squeeze.

## 🛒 AMER3

- **What happened:** accounting inconsistencies and hidden supplier debt became public; the stock
  fell about 77% in a day and more than 95% from the peak.
- **Setup:** a large, well-known retailer with a low headline multiple and a dividend.
- **What was visible early:** [FCF conversion](indicators.md#-fcf-conversion) below profit,
  [Sloan ratio](indicators.md#-sloan-ratio), [DPO](indicators.md#-dpo) stretched versus peers,
  [DSO](indicators.md#-dso) rising, empty stores, and competitors growing.
- **What was not visible:** the exact disclosure date and the full hidden liability.
- **False comfort:** low P/E, EV/EBITDA, and dividend yield.
- **Lesson:** cash flow and working capital are the warning. You do not need to audit every line to
  see that the cash is not matching the profit.

## 🏦 OIBR3

- **What happened:** a debt-heavy telecom went through judicial recovery and repeated dilution; the
  equity moved toward zero.
- **Setup:** a low P/B and a “cheap” asset base.
- **What was visible:** [net debt to EBITDA](indicators.md#-net-debt-to-ebitda) above 4x,
  [interest coverage](indicators.md#-interest-coverage) below 2x, a
  [maturity wall](indicators.md#-maturity-wall), and negative FCF.
- **What was not visible:** the final recovery price and the timing.
- **False comfort:** low P/B. The assets were not worth the liabilities.
- **Lesson:** in a debt wall, the equity is an option, not a bargain.

## 🛫 CVCB3

- **What happened:** an accounting restatement and the COVID travel collapse drove a ~70% decline.
- **Setup:** a travel operator with receivables and leverage; the market focused on the brand.
- **What was visible:** [DSO](indicators.md#-dso) rising, [FCF conversion](indicators.md#-fcf-conversion)
  weakening, and [net debt to EBITDA](indicators.md#-net-debt-to-ebitda) rising.
- **What was not visible:** the restatement timing and the pandemic.
- **False comfort:** P/E and brand strength.
- **Lesson:** accounting quality and leverage matter more than the story.

## 🛟 IRBR3

- **What happened:** a short-seller report and questions about reserves/accounting drove a ~80%
  decline over weeks; a false Buffett rumour later produced a sharp rally.
- **Setup:** an insurer with aggressive growth, receivables, and a market-darling narrative.
- **What was visible:** [DSO](indicators.md#-dso), [FCF conversion](indicators.md#-fcf-conversion),
  [Sloan ratio](indicators.md#-sloan-ratio), and management turnover.
- **What was not visible:** the report timing and the rumour’s falsity.
- **False comfort:** P/E and the Buffett narrative.
- **Lesson:** verify the source; accounting flags can precede the headline.

## ⛽ PETR4

- **What happened:** a CEO removal/state-intervention shock drove a ~21% one-day drop.
- **Setup:** a state-controlled oil major with a low P/E and a high dividend.
- **What was visible:** political exposure, governance history, and price-policy risk.
- **What was not visible:** the timing of the decree.
- **False comfort:** low P/E, P/B, and dividend yield.
- **Lesson:** political risk is not in the multiple. Size for the gap.

## 🥩 JBSS3

- **What happened:** a political/legal shock drove a ~33% one-day drop.
- **Setup:** a leveraged protein exporter with governance and headline risk.
- **What was visible:** governance, leverage, and political exposure.
- **What was not visible:** the leak and the timing.
- **False comfort:** valuation.
- **Lesson:** event risk has no valuation warning.

## ⛏ VALE3

- **What happened:** a dam disaster created a legal, environmental, and operational shock; the stock
  fell and the liabilities lasted for years.
- **Setup:** a low-cost producer with a high dividend and a tail risk that was not in the multiple.
- **What was visible:** the safety/dam record, legal contingencies, and ESG exposure.
- **What was not visible:** the timing of the failure.
- **False comfort:** low P/E and high yield.
- **Lesson:** some risks are not valuation risks. Size for the tail, not just the base case.

## 🛒 MGLU3

- **What happened:** a huge e-commerce re-rating, then a collapse as Selic rose and growth slowed.
- **Setup:** high [P/E](indicators.md#-pe) and [P/S](indicators.md#-ps), negative
  [FCF yield](indicators.md#-fcf-yield), and rising leverage.
- **What was visible:** the valuation extremes, [Selic](indicators.md#-selic), and the growth
  deceleration.
- **What was not visible:** the exact top.
- **False comfort:** momentum and RSI; both were late.
- **Lesson:** a high multiple plus a macro reversal is a dangerous combination.

## 📺 Blockbuster

- **What happened:** streaming and Netflix replaced the store model; the company declined.
- **Setup:** a cheap multiple on a business with falling store traffic.
- **What was visible:** [same-store sales](indicators.md#-same-store-sales),
  [market share](indicators.md#-market-share), and
  [online penetration](indicators.md#-online-penetration).
- **What was not visible:** the speed of the decline.
- **False comfort:** a cheap P/E.
- **Lesson:** a low multiple on a dying format is a value trap.

## 📱 Nokia

- **What happened:** the smartphone shift erased the feature-phone franchise; the stock declined.
- **Setup:** a cheap-looking hardware company with falling market share.
- **What was visible:** [market share](indicators.md#-market-share),
  [revenue CAGR](indicators.md#-revenue-cagr), and gross margin pressure.
- **What was not visible:** the timing of the transition.
- **False comfort:** low P/E.
- **Lesson:** disruption is slow, then fast.

## 🧠 Lessons

1. **Cash flow beats headline profit.** AMER3 and IRBR3 were accounting stories before they were price
   stories.
2. **Debt can wipe out equity.** OIBR3 was cheap on P/B and expensive on survival.
3. **Disruption is slow, then fast.** Blockbuster and Nokia had years of warning.
4. **Squeezes are positioning, not fundamentals.** GME, VW, and Tesla can move without the business
   changing.
5. **Political and legal shocks have no valuation warning.** PETR4 and JBSS3 gapped on headlines.
6. **Liquidity is the exit.** A low-ADTV stock can trap you before the thesis plays out.
7. **False comfort is the enemy.** Low P/E, low P/B, and high yield are not risk controls.

## 🔗 Related

- [readme.md](readme.md) — the stock-operations map.
- [dangers.md](dangers.md) — the generic danger library.
- [indicators.md](indicators.md) — the indicator cards.
- [flows.md](flows.md) — how each move spread.
- [liquidity.md](liquidity.md) — the first gate.
- [buy/readme.md](buy/readme.md) — the entry process.
- [sell/readme.md](sell/readme.md) — the exit process.

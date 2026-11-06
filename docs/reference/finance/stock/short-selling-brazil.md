# 📉 Short selling — Brazil
> **Updated:** 2026-11-02

**What this is:** generic mechanics, margin, costs, and tax for short selling
(*venda a descoberto*) on B3. Not financial or tax advice; confirm current
broker/B3 rules.

## 🧱 Mechanics

- A short sale borrows shares, sells them, and later buys them back to close.
- The position is negative until the buy-to-cover.
- The broker requires collateral — often 100% of the financial value plus the
  asset's deságio. Confirm the current terms.
- Margin is checked daily and floats with the stock price:
  - price rises → more collateral required, possibly blocked/withdrawn;
  - price falls → no action needed.
- The account's total value can look right while the available balance is lower:
  short collateral is blocked until settlement.
- Stock trades settle **T+2 business days**. A buy-to-close releases margin after
  settlement; check the available balance after the trading day.
- You can buy to close at any time; moving money into another investment does
  not hide the margin requirement.

## 💸 Costs

The rent itself is small; fixed broker/exchange fees dominate small positions.

| Line | What it is |
| --- | --- |
| Intermediation | Broker fee for the BTC contract; often ~0.25% of financial volume |
| Rent | Paid to the lender; annual “taxa do papel” × notional × days/365 |
| Emolumentos | B3 registration/clearing fee |
| Operation | Fixed order fee, usually per order |

Fee model:

```text
intermediation = 0.0025 × short_notional        # check broker; minimum may apply
rent           = paper_rate_annual × notional × days/365
emolumentos    = exchange_rate × notional       # use the B3 table/note
operation      = order_fee × orders             # open + close
```

- The 0.25% intermediation is **not** the rent.
- Check the broker's minimum fee and whether it applies to your notional.
- Confirm the paper rate and period on the note.

## 🧾 Tax

- A short sale is a sale. Gains/losses are grouped by month and category.
- Stocks sold for **≤ R$20,000 in a month** are exempt from DARF; ETFs, BDRs, and
  FIIs do **not** have that exemption.
- Losses carry forward in the same category.
- A taxable month is paid by the last business day of the following month, usually
  DARF 6015.
- If unsure, round up; overpayment can be recovered/compensated later.
- Confirm current DARF/IRPF instructions.

## 📝 Record

- Put orders in a monthly table: `yyyy-mm.md`.
- Record the closed short cycle: average sell, average cover, gross, fees, net,
  tax, and position 0.
- Keep DARF receipts separately.
- No per-order PDFs required; the monthly table is the raw record.

## 🔗 Related

- [Brazil tax rules](brazil-tax-rules.md)
- [Record keeping](record-keeping.md)
- [Stock operations](readme.md)

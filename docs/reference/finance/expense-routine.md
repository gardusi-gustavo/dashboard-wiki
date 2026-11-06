# 💰 Expense routine
> **Updated:** 2026-11-02

**What this is:** generic monthly expense-pool routine. Actual pool targets,
accounts, and recharges stay in the private ledger.

## 🧭 Steps

1. Read current pool balances against targets.
2. Receive income in the main account.
3. Distribute to the spending pools.
4. Top up from reserve when a pool is low.
5. Run recurring recharges.
6. Reconcile only the enabled card/phone pairs.
7. Update the expense summary and net-worth snapshot.

## 🏦 Pool pattern

| Pool | Role | Top-up |
| --- | --- | --- |
| Main receive | Income/honeypot | PIX/transfer in |
| Street spending | Daily debit/cash | From main or reserve |
| Virtual credit | Controlled online spend | Enable on demand |
| Backup | Physical card at home | From reserve |
| Paper cash | Small emergencies | Withdraw when low |
| Prepaid wallets | Rides/services | Monthly top-up |

## 🔋 Recharge rules

- Keep prepaid exposure capped.
- Use debit/PIX, not stored credit, for prepaid top-ups.
- Confirm single recurring charges for phone/internet.
- Keep the reserve separate; top up from it only when a pool is below threshold.

## 🔗 Related

- [Net-worth routine](net-worth-routine.md)
- [Fixed income](fixed-income.md)
- [Stock record keeping](stock/record-keeping.md)

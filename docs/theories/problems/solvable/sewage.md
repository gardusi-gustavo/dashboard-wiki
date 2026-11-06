# 🚽 Sewage treatment — the pipe that leaks shit

**What this is:** a **perpetual-damage wheel** — basic sanitation (saneamento básico). The collection-and-treatment pipe system **exists and mostly works**, but it **under-treats**: raw sewage still
enters
the waterway at a point upstream and flows, stinking, toward the ocean. Tietê's smell is the visible symptom; the wheel is the missing "filter the input before it reaches the river" step.

## 📋 Problem statement

<!-- begin table -->
| Axis | Answer | Note |
| ------ | -------- | ------ |
| **Problem** | The pipe network collects sewage but treats only a share of it | the untreated rest enters the water at point A and flows downstream, badly managed and stinking |
| **Population affected** | ~21M in the São Paulo metro (order of magnitude) | everyone downriver of point A smells and drinks the consequence |
| **Time to implement** | 10–20 yr of buildout: interceptors, treatment plants, connections | decades-long programs, not one contract |
| **Lifespan** | Indefinite **iff** the input is treated at source and the plant is maintained | otherwise the damage wheel self-refills every day |
<!-- end table -->

## ⚙️ The wheel model

Treat the failure as a flow problem, not a mood problem:

<!-- begin table -->
| Variable | Meaning | Why it matters |
| ---------- | --------- | ---------------- |
| `N` | Untreated sewage entering at point A (liters/min) | The **input** — the only lever that ends the wheel |
| `M` | Distance the shit travels to the ocean (km) | Exposure length — who smells it, for how long |
| `O` | Speed the water carries it | Transit time = how fast the smell reaches people |
<!-- end table -->

**The leverage rule:** cleaning the *output* (the river) re-spends forever. Closing the *input* (`N → 0` by treating before point A) stops the re-fill — the river then self-clears on its own.

## 💰 Cost of install vs maintain

<!-- begin table -->
| Spend | What it buys | Trap |
| ------- | -------------- | ------ |
| **Install** | Interceptors + treatment capacity to make `N ≈ 0` | Big upfront, one-time |
| **Maintain** | Run the plants, fix leaks, keep connections enforced | Small yearly, but **forever** — and the budget line most often cut |
<!-- end table -->

**Who pays:** the downstream cleaner (municipality, health system, everyone who smells it) pays for the damage wheel *today*. The fix asks the **upstream feeder** — households, industry, illegal
hookups — to pay for treatment instead. That inversion is the political fight.

**Who profits from broken:** the contract that bills per-liters-processed or the body that budgets cleanup year after year may earn more from `N > 0` than from closing it. Audit who makes money from
the wheel staying open.

## 🧪 Thought experiment — evaporating the Tietê

Could the river be split into an N×M grid of heated half-pipes and evaporated to dry solids? It is
possible in principle; at river scale it is not a treatment plant, it is a second energy system.

For the low flow of ~20 m³/s, the energy floor is:

```text
P = m_dot × [c_p × (T_boil − T_in) + ΔH_vap] / η
  ≈ 20,000 kg/s × (0.335 + 2.26) MJ/kg
  ≈ 45–52 GW
```

That is the latent heat of evaporation; it does not shrink when the river is split into more lanes.
The matrix only changes where the heat is delivered and how wide the facility is:

```text
Q = N × w × δ × v                 (flow split)
A = N × w × L = P / q''           (heat surface)
L = P / (q'' × N × w)             (channel length)
```

<!-- begin table -->
| Objective | N | Width | Length | Footprint | Note |
| --- | ---: | ---: | ---: | ---: | --- |
| Min length / flash | 33,333 | 0.5 m | 5.4 m | 16.6 km wide | q'' ≈ 500 kW/m²; thin film; easy swap |
| Balanced | 10,000 | 0.5 m | 90.4 m | 5 km wide | q'' ≈ 100 kW/m²; 18 × 5 m segments |
| Min width / long | 2,000 | 0.5 m | 1.5 km | 1 km wide | q'' ≈ 30 kW/m²; sludge drag dominates |
| Strict 1 m tubes | 45,200 | 1 m | 1 m | 45.2 km wide | q'' ≈ 1 MW/m²; at the CHF limit |
<!-- end table -->

Why it loses:

- **Open troughs** lose 50–70% of the heat to ambient air; wind helps vapor leave, but humidity
  saturates and rain makes it worse.
- **Enclosed facility** solves heat loss but needs huge exhaust and condenser capacity; condensing
  20,000 kg/s needs a second cooling loop.
- **Venting** the steam creates fog and carries VOCs, H₂S, ammonia, and metal vapors over the city.
- **Sludge** turns to paste around 10–20% water and bakes into crust; only the final 15–20% of each
  lane needs constant swapping, but the mechanical loop is enormous.
- **Energy:** evaporation costs ~2.26 MJ/kg; mechanical treatment costs ~0.001–0.002 MJ/kg. That is
  roughly a 1000× gap.

The leverage rule above still wins: treat the **input** (`N → 0`), not the river **output**. The
evaporation facility is the ultimate output-cleaning trap — it re-spends forever and prices the
river as a chemical plant. Evaporation remains a niche for small, concentrated ZLD streams, not a
river-scale solution.

## ❓ Open questions

- Real `N` at point A — liters/min of untreated sewage, and the share treated today
- Real `M` / `O` — actual distance and flow speed; transit time to population
- Cost to install (interceptors + plants) vs yearly maintenance, current vs target
- Who holds the treatment contracts and whether fees reward volume over closure
- How many of the ~21M are actually connected vs serviced but untreated

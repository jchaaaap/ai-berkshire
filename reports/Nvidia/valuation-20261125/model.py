"""Nvidia (NVDA) long / DCA pre-buy model, 2026-11-25.

Updates valuation-20261123/model.py (short evaluation) to the Nov 25 close and
adds the buy-below price, position sizing and a dollar-cost-averaging plan.
Inputs marked FACT come from the Q3 FY27 release (Nov 17, 2026) and price
history; inputs marked ASSUMPTION are guesses. Run: python3 model.py
"""

# ---- FACTS ---------------------------------------------------------------
PRICE_NOV20 = 125.53        # close (stockanalysis.com)
PRICE_NOV23 = 165.05        # close, now verified (stockanalysis.com, +31.48%)
PRICE_NOV25 = 149.30        # close, -3.91% (Motley Fool via Yahoo; ChipDispatch)
LOW_NOV25 = 141.17          # intraday low (ChipDispatch)
PEAK = 239.24               # Oct 6 record close
DILUTED_SHARES = 24.186e9   # Q3 FY27 diluted weighted shares
Q3_EPS_NONGAAP = 2.68
Q3_FCF = 43.777e9
Q4_REV_GUIDE = 130.0e9
Q4_GM_GUIDE = 0.715
Q4_OPEX_NONGAAP = 10.7e9
TAX = 0.17
DIVIDEND_Q = 0.25

# ---- ASSUMPTIONS (unchanged from Nov 23 model) -------------------------------
SCEN = {  # name: (normalised EPS, P/E, probability)
    "Bust": (5.5, 15, 0.20),
    "Base": (12.5, 14, 0.50),
    "Bull": (17.0, 18, 0.30),
}
FAIR_VALUE_USED = 175       # base case, rounded; the conservative anchor
CUSHION = 0.20              # pre-buy routine: 20-30%


def weighted(scen):
    return sum(eps * pe * p for eps, pe, p in scen.values())


def main():
    p = PRICE_NOV25
    print("== Price and market cap ==")
    print(f"Nov 25 close ${p}: market cap ${p*DILUTED_SHARES/1e12:.2f}T; "
          f"{p/PEAK-1:+.0%} vs Oct 6 peak; {p/PRICE_NOV23-1:+.1%} vs Nov 23 close")
    print(f"Implied Nov 24 close from -3.91%: ${p/(1-0.0391):.2f}")

    print("\n== Run-rate multiples at Nov 25 close ==")
    rr_q3 = Q3_EPS_NONGAAP * 4
    q4_eps = (Q4_REV_GUIDE * Q4_GM_GUIDE - Q4_OPEX_NONGAAP) * (1 - TAX) / DILUTED_SHARES
    print(f"P/E on Q3x4 (${rr_q3:.2f}): {p/rr_q3:.1f}x; on Q4-guide x4 (${q4_eps*4:.2f}): {p/(q4_eps*4):.1f}x")
    print(f"FCF yield (Q3 FCF x4): {Q3_FCF*4/(p*DILUTED_SHARES):.1%}; dividend yield {DIVIDEND_Q*4/p:.2%}")

    print("\n== Scenario values ==")
    for k, (eps, pe, prob) in SCEN.items():
        print(f"{k}: ${eps} x {pe}x = ${eps*pe:.0f} (p={prob}); vs today {eps*pe/p-1:+.0%}")
    ev = weighted(SCEN)
    print(f"Probability-weighted: ${ev:.0f} ({ev/p-1:+.0%} vs today)")

    print("\n== Sensitivity: weighted value if bust odds rise (taken from bull) ==")
    for bust in (0.20, 0.30, 0.40, 0.50):
        s = {"Bust": (5.5, 15, bust), "Base": (12.5, 14, 0.50), "Bull": (17.0, 18, 0.50 - bust)}
        print(f"bust {bust:.0%}: ${weighted(s):.0f}")
    print("Rate-hike haircut (all multiples -2 turns):",
          f"${weighted({k: (e, pe-2, pr) for k, (e, pe, pr) in SCEN.items()}):.0f} weighted,",
          f"base ${12.5*12:.0f}")

    print("\n== Buy-below ==")
    bb = FAIR_VALUE_USED * (1 - CUSHION)
    print(f"Base ${FAIR_VALUE_USED} x {1-CUSHION:.2f} = ${bb:.0f}; "
          f"that is {1-bb/ev:.0%} below the weighted ${ev:.0f}")
    print(f"Base x 0.70 = ${FAIR_VALUE_USED*0.7:.0f} (deep-cushion line)")
    print(f"Today ${p} is {p/bb-1:+.1%} vs buy-below and {p/FAIR_VALUE_USED-1:+.1%} vs base")
    print(f"Reverse: at 14x, ${p} needs normalised EPS ${p/14:.2f} "
          f"({p/14/rr_q3-1:+.0%} vs Q3 run rate ${rr_q3:.2f})")

    print("\n== Position size vs bust case (per $10,000 of non-retirement money) ==")
    bust_v = 5.5 * 15
    for pct in (0.01, 0.02, 0.03, 0.05):
        pos = 10000 * pct
        print(f"{pct:.0%} position (${pos:,.0f}) bought at ${p}: loss at bust ${bust_v:.0f} = "
              f"${pos*(1-bust_v/p):,.0f} ({pct*(1-bust_v/p):.2%} of the money)")

    print("\n== DCA tranche rule (6 monthly tranches, target 3%) ==")
    tranche = 0.03 / 6
    rule = [(110, 1.0, "full (but check why it fell)"), (140, 1.0, "full"),
            (175, 0.5, "half"), (10**9, 0.0, "skip")]
    for px in (100, 125, 140, 149.30, 160, 180):
        for cap, mult, label in rule:
            if px <= cap:
                print(f"price ${px}: {label} tranche = {tranche*mult:.2%} of money")
                break
    # illustrative path: average cost if prices drift through the zones
    path = [149.30, 135, 128, 150, 170, 185]
    units = cost = 0
    for px in path:
        mult = next(m for c, m, _ in rule if px <= c)
        amt = 1000 * mult
        units += amt / px
        cost += amt
    print(f"Illustrative path {path}: invested ${cost:,.0f} per $1,000 tranche, "
          f"avg cost ${cost/units:.2f}")


if __name__ == "__main__":
    main()

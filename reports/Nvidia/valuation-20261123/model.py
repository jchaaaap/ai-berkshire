"""Nvidia (NVDA) short evaluation model, 2026-11-23.

Reproduces every Estimate in Nvidia-short-20261123.md. Inputs marked FACT come
from the Q3 FY27 release (Nov 17, 2026) and price history; inputs marked
ASSUMPTION are guesses. Run: python3 model.py
"""
from math import log, sqrt, exp, erf

# ---- FACTS ---------------------------------------------------------------
PRICE_FRI = 125.53          # Nov 20 close (stockanalysis.com)
PRICE_MON = 165.05          # Nov 23 intraday quote (Investing.com widget, unverified close)
PEAK = 239.24               # Oct 6 record close
DILUTED_SHARES = 24.186e9   # Q3 FY27 diluted weighted shares
Q3_REV = 115.844e9
Q3_NI_NONGAAP = 64.870e9
Q3_EPS_NONGAAP = 2.68
Q3_FCF = 43.777e9
Q4_REV_GUIDE = 130.0e9
Q4_GM_GUIDE = 0.715         # midpoint of 71-72%
Q4_OPEX_NONGAAP = 10.7e9
TAX = 0.17                  # midpoint of 16-18%
CASH_AND_SECURITIES = 29.089e9 + 24.423e9
DEBT = 32.371e9

def ncdf(x):
    return 0.5 * (1 + erf(x / sqrt(2)))

def bs_put(S, K, T, vol, r=0.04):
    d1 = (log(S / K) + (r + vol * vol / 2) * T) / (vol * sqrt(T))
    d2 = d1 - vol * sqrt(T)
    return K * exp(-r * T) * ncdf(-d2) - S * ncdf(-d1)

def main():
    print("== Market cap ==")
    for label, p in [("Fri close", PRICE_FRI), ("Mon intraday", PRICE_MON)]:
        print(f"{label}: ${p:.2f} x {DILUTED_SHARES/1e9:.3f}B = ${p*DILUTED_SHARES/1e12:.2f}T")
    print(f"Peak ${PEAK} -> ${PEAK*DILUTED_SHARES/1e12:.2f}T; Mon is {PRICE_MON/PEAK-1:.0%} vs peak")
    print(f"Net cash: ${(CASH_AND_SECURITIES-DEBT)/1e9:.1f}B")

    print("\n== Run-rate earnings ==")
    q4_ni = (Q4_REV_GUIDE * Q4_GM_GUIDE - Q4_OPEX_NONGAAP) * (1 - TAX)
    q4_eps = q4_ni / DILUTED_SHARES
    rr_q3 = Q3_EPS_NONGAAP * 4
    rr_q4 = q4_eps * 4
    print(f"Q3 x4 non-GAAP EPS: ${rr_q3:.2f}; Q4-guide implied EPS ${q4_eps:.2f} (x4 = ${rr_q4:.2f}), excl. interest income")
    print(f"Q3 net margin {Q3_NI_NONGAAP/Q3_REV:.1%}; Q3 FCF x4 = ${Q3_FCF*4/1e9:.0f}B")
    for label, p in [("Fri", PRICE_FRI), ("Mon", PRICE_MON)]:
        print(f"{label} ${p}: P/E on Q3x4 {p/rr_q3:.1f}x, on Q4x4 {p/rr_q4:.1f}x, "
              f"FCF yield {Q3_FCF*4/(p*DILUTED_SHARES):.1%}")

    print("\n== Scenario values (ASSUMPTIONS) ==")
    # normalised EPS, multiple, probability
    scen = {
        "Bust (2001-style digestion: revenue -45%, GM 60%)": (5.5, 15, 0.20),
        "Base (growth slows to low teens, margins hold ~mid-50s net)": (12.5, 14, 0.50),
        "Bull (FY28 consensus ~$725B sales delivered)": (17.0, 18, 0.30),
    }
    ev = 0
    for k, (eps, pe, prob) in scen.items():
        v = eps * pe
        ev += v * prob
        print(f"{k}: ${eps} x {pe}x = ${v:.0f} (p={prob})")
    print(f"Probability-weighted value: ${ev:.0f}; vs Mon ${PRICE_MON}: {ev/PRICE_MON-1:+.0%}")

    print("\n== What today's price implies (reverse) ==")
    for pe in (15, 18, 20):
        print(f"At {pe}x, ${PRICE_MON} needs normalised EPS ${PRICE_MON/pe:.2f}")

    print("\n== Ways to express a bearish view, $10,000 risk budget, S = Mon price ==")
    S = PRICE_MON
    T = 0.25  # ~3 months (late Feb 2027, past Q4 FY27 earnings)
    for vol in (0.55, 0.75):
        p150 = bs_put(S, 150, T, vol)
        p165 = bs_put(S, 165, T, vol)
        p130 = bs_put(S, 130, T, vol)
        spread = p165 - p130
        print(f"IV {vol:.0%} (ASSUMPTION): 3-mo $165 put ~${p165:.2f} ({p165/S:.1%} of spot), "
              f"$150 put ~${p150:.2f}, $165/$130 spread ~${spread:.2f} (max value $35, "
              f"breakeven ${165-spread:.2f})")
    print("\nOutright short of $10,000 (60 shares at $165):")
    sh = 10000 / S
    for end in (83, 125, 165, 200, 240, 300):
        print(f"  stock ends ${end}: P&L ${sh*(S-end):+,.0f}")

if __name__ == "__main__":
    main()

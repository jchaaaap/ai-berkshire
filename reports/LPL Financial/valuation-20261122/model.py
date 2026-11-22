"""LPL Financial (LPLA) 10-year owner-earnings DCF. Standard library only.

Run: python3 model.py
All money in USD. Cash flows are equity cash flows (after interest), so no
debt bridge is needed: debt is already charged through interest expense.
"""
from decimal import Decimal as D, getcontext

getcontext().prec = 28

# ---- Inputs (sources and reasoning in LPL Financial-research-20261122.md) ----
PRICE = D("264.56")            # Nov 20, 2026 close
SHARES = D("78.31")            # millions, Sep 30 2026 (136.85M issued - 58.54M treasury)
START_OWNER_EPS = D("21.00")   # assumption: TTM adjusted EPS 22.64 less ~7% for recurring deal costs and SBC; growth capex is charged separately via g/ROIC
R = D("0.10")                  # discount rate (USD equity, beta 1.0, ~2x levered)
ROIC = D("0.20")               # steady-state incremental return on capital (assumption)

# Growth of total owner earnings (NOT per share; buybacks are treated as distribution)
SCENARIOS = {
    "bear": {"g1_5": [D("0.00"), D("0.00"), D("0.00"), D("0.03"), D("0.03")], "g6_10": D("0.03"), "g_term": D("0.02")},
    "base": {"g1_5": [D("0.07")] * 5, "g6_10": D("0.05"), "g_term": D("0.03")},
    "bull": {"g1_5": [D("0.11")] * 5, "g6_10": D("0.07"), "g_term": D("0.035")},
}


def terminal_pe(g):
    return (1 - g / ROIC) / (R - g)


def run(name, s):
    eps = START_OWNER_EPS
    pv = D(0)
    path = []
    rates = s["g1_5"] + [s["g6_10"]] * 5
    for year, g in enumerate(rates, start=1):
        eps = eps * (1 + g)
        # payout = 1 - g/ROIC: the part not reinvested reaches shareholders
        cash = eps * (1 - g / ROIC)
        pv += cash / (1 + R) ** year
        path.append((year, eps, cash))
    tpe = terminal_pe(s["g_term"])
    tv = eps * (1 + s["g_term"]) * tpe  # year-11 earnings x terminal P/E
    pv_tv = tv / (1 + R) ** 10
    value = pv + pv_tv
    return {"name": name, "path": path, "pv_cash": pv, "tpe": tpe, "pv_tv": pv_tv,
            "value": value, "tv_share": pv_tv / value, "eps10": eps}


if __name__ == "__main__":
    print(f"Market cap check: {PRICE} x {SHARES}M = ${PRICE * SHARES / 1000:.2f}B")
    for name, s in SCENARIOS.items():
        r = run(name, s)
        y = {p[0]: p for p in r["path"]}
        print(f"\n[{name}] value/share ${r['value']:.2f}  (vs price ${PRICE}, {(r['value']/PRICE-1)*100:+.1f}%)")
        for yr in (1, 3, 10):
            print(f"  yr{yr}: owner EPS {y[yr][1]:.2f}, cash to holders {y[yr][2]:.2f}")
        print(f"  PV of yr1-10 cash {r['pv_cash']:.2f}; terminal P/E {r['tpe']:.2f}x; PV terminal {r['pv_tv']:.2f}; terminal share {r['tv_share']*100:.1f}%")
    # Sensitivity: base case value across r and terminal g
    print("\nBase-case value/share, r x terminal g")
    base = SCENARIOS["base"]
    for r_ in (D("0.09"), D("0.10"), D("0.11")):
        row = []
        for gt in (D("0.02"), D("0.03"), D("0.04")):
            R_save = R
            globals()["R"] = r_
            row.append(f"{run('x', dict(base, g_term=gt))['value']:.0f}")
            globals()["R"] = R_save
        print(f"  r={r_}: g=2% ${row[0]}  g=3% ${row[1]}  g=4% ${row[2]}")
    # Reverse: what flat-rate 10-yr growth does today's price require (terminal g=3%)?
    lo, hi = D("-0.10"), D("0.30")
    for _ in range(80):
        mid = (lo + hi) / 2
        v = run("rev", {"g1_5": [mid] * 5, "g6_10": mid, "g_term": D("0.03")})["value"]
        lo, hi = (mid, hi) if v < PRICE else (lo, mid)
    print(f"\nReverse DCF: price ${PRICE} implies ~{mid*100:.1f}%/yr owner-earnings growth for 10 years (r=10%, g_term=3%)")

"""eToro Group (ETOR) 10-year owner-earnings DCF plus excess cash. Standard library only.

Run: python3 model.py
All money in USD. eToro has no borrowings (only leases), so equity value =
PV of owner earnings paid out + excess corporate cash.
"""
from decimal import Decimal as D, getcontext

getcontext().prec = 28

# ---- Inputs (sources and reasoning in eToro-research-20261122.md) ----
PRICE = D("18.56")             # Nov 20, 2026 close (Investing.com)
SHARES_BASIC = D("79.53")      # millions, outstanding (Investing.com ownership table)
SHARES_DIL = D("91.94")        # millions, Q3 2026 weighted diluted (release)
CASH_STI = D("1223.5")         # $M cash + short-term investments, Sep 30 2026
RESERVED = D("400")            # $M assumption: regulatory capital + working cash kept in subsidiaries
TRADEZERO_CASH = D("180")      # $M assumption: $231M deal less ~2.5M shares (~$50M) paid in stock
EXCESS_CASH = CASH_STI - RESERVED - TRADEZERO_CASH
R = D("0.11")                  # discount rate: cyclical retail-trading/crypto earnings, small cap
ROIC = D("0.25")               # return on growth reinvestment (mostly bolt-on M&A; organic growth is expensed marketing)

# Owner EPS per diluted share = mid-cycle net income incl. stock comp as a cost / 91.94M
SCENARIOS = {
    # 2022-23 style bust: NC falls to ~$650M (2022: $631M, 2023: $639M) with opex ~$580M -> EPS ~$0.50,
    # then recovers to the "soft" level by year 4. Explicit EPS path, years 1-4.
    "bear": {"path": [D("0.50"), D("0.80"), D("1.20"), D("1.45")], "g6_10": D("0.03"), "g_term": D("0.02")},
    # NC stays at Q3 run-rate ~$745M, opex ~$580M, 15% tax -> ~$128M -> $1.40
    "soft": {"eps0": D("1.40"), "g1_5": [D("0.00")] * 3 + [D("0.03")] * 2, "g6_10": D("0.03"), "g_term": D("0.02")},
    # mid-cycle NC ~$850M, cash opex incl SBC ~$605M, 15% tax -> ~$197M -> $2.14 (rounded 2.10)
    "base": {"eps0": D("2.10"), "g1_5": [D("0.06")] * 5, "g6_10": D("0.04"), "g_term": D("0.03")},
    # NC ~$950M with TradeZero + US growth -> ~$240M -> ~$2.60
    "bull": {"eps0": D("2.60"), "g1_5": [D("0.12")] * 5, "g6_10": D("0.07"), "g_term": D("0.035")},
}


def run(s, r=None):
    r = r if r is not None else R
    pv = D(0)
    if "path" in s:  # explicit EPS path, then g6_10 growth; recovery years need no reinvestment
        eps_list = list(s["path"])
        eps = eps_list[-1]
        while len(eps_list) < 10:
            eps = eps * (1 + s["g6_10"])
            eps_list.append(eps)
        gs = [D(0)] * len(s["path"]) + [s["g6_10"]] * (10 - len(s["path"]))
    else:
        eps, eps_list, gs = s["eps0"], [], s["g1_5"] + [s["g6_10"]] * 5
        for g in gs:
            eps = eps * (1 + g)
            eps_list.append(eps)
    for year, (e, g) in enumerate(zip(eps_list, gs), start=1):
        pv += e * (1 - g / ROIC) / (1 + r) ** year
    eps = eps_list[-1]
    tpe = (1 - s["g_term"] / ROIC) / (r - s["g_term"])
    pv_tv = eps * (1 + s["g_term"]) * tpe / (1 + r) ** 10
    cash_ps = EXCESS_CASH / SHARES_DIL
    value = pv + pv_tv + cash_ps
    return {"value": value, "pv": pv, "pv_tv": pv_tv, "tpe": tpe, "cash_ps": cash_ps,
            "tv_share": pv_tv / (pv + pv_tv), "eps10": eps}


if __name__ == "__main__":
    print(f"Market cap (basic):   {PRICE} x {SHARES_BASIC}M = ${PRICE * SHARES_BASIC / 1000:.3f}B")
    print(f"Market cap (diluted): {PRICE} x {SHARES_DIL}M = ${PRICE * SHARES_DIL / 1000:.3f}B")
    print(f"Excess cash: {CASH_STI} - {RESERVED} - {TRADEZERO_CASH} = ${EXCESS_CASH}M = ${EXCESS_CASH / SHARES_DIL:.2f}/diluted share")
    print(f"Price ex excess cash: ${PRICE - EXCESS_CASH / SHARES_DIL:.2f}")
    for name, s in SCENARIOS.items():
        x = run(s)
        print(f"\n[{name}] value/share ${x['value']:.2f} (vs ${PRICE}: {(x['value'] / PRICE - 1) * 100:+.1f}%)")
        e0 = s.get("eps0", s.get("path", [None])[0])
        print(f"  yr1/start owner EPS {e0}, yr10 EPS {x['eps10']:.2f}; P/E on that EPS ex cash {(PRICE - x['cash_ps']) / e0:.1f}x")
        print(f"  PV yr1-10 {x['pv']:.2f}; terminal P/E {x['tpe']:.2f}x; PV terminal {x['pv_tv']:.2f} ({x['tv_share'] * 100:.0f}% of operating value); cash/share {x['cash_ps']:.2f}")
    print("\nBase-case value/share, r x terminal g")
    for r_ in (D("0.10"), D("0.11"), D("0.12")):
        row = [f"${run(dict(SCENARIOS['base'], g_term=gt), r_)['value']:.2f}" for gt in (D("0.02"), D("0.03"), D("0.04"))]
        print(f"  r={r_}: g=2% {row[0]}  g=3% {row[1]}  g=4% {row[2]}")
    print("\nBase-case value/share by starting owner EPS (r=11%)")
    for e in (D("1.40"), D("1.80"), D("2.10"), D("2.40")):
        print(f"  eps0 {e}: ${run(dict(SCENARIOS['base'], eps0=e))['value']:.2f}")
    # Reverse DCF: flat 10-yr growth implied by price, starting from base EPS 2.10
    for e0 in (D("2.10"), D("1.40")):
        lo, hi = D("-0.20"), D("0.40")
        for _ in range(80):
            mid = (lo + hi) / 2
            v = run({"eps0": e0, "g1_5": [mid] * 5, "g6_10": mid, "g_term": D("0.03")})["value"]
            lo, hi = (mid, hi) if v < PRICE else (lo, mid)
        print(f"Reverse DCF from owner EPS {e0}: price implies ~{mid * 100:.1f}%/yr growth for 10 yrs (r=11%, g_term=3%)")

# LPL Financial (LPLA) pre-buy research: a good business at a fair price, not yet a margin-of-safety price

> Research date 2026-11-22 · Price date 2026-11-20 close · Price **$264.56** · Market cap **$20.7B** (verified: $264.56 × 78.31M shares; quote site shows $20.6B, 0.6% off) · All figures USD
> Method: the [pre-buy routine](../../docs/guides/pre-buy-routine.md) steps 1–5, with the valuation done per `skills/company-valuation.md`. Model script: [`valuation-20261122/model.py`](valuation-20261122/model.py).
> **Labels:** **Fact** = reported figure with a source. **Estimate** = arithmetic or analyst consensus. **Assumption** = a scenario input, i.e. a guess. **View** = interpretation, not data.
>
> *Educational research, not investment advice.*

---

## Bottom line

| | |
|---|---|
| **Verdict** | **Watchlist, not a buy today.** Quality passes; price is in the fair range but short of the 20–30% cushion the routine asks for. |
| Fair value (base case, assumption-driven) | **~$304** per share (range: bear ~$239, bull ~$366) |
| **Buy below** | **~$240** (≈21% under base value, and about equal to the bear-case value). Strong-cushion zone: **~$215** (30% under). |
| Today's price vs base value | $264.56 is ~13% below base value. |
| What today's price needs | ~3% a year owner-earnings growth for 10 years (reverse DCF). LPL grew adjusted EPS 22% in 2025. |
| Biggest risks | Fed rate cuts (about 28% of gross profit is interest on client cash), Commonwealth advisors leaving, recruiting slowing, regulation of cash-sweep pay. |

**Why the screen's numbers needed checking (Fact):** the earlier screen used estimates because data feeds were blocked. The real numbers are below. The headline change: the stock has fallen **34% from its 52-week high** ($400.16) to $264.56, mostly after Q3 results on Oct 27 (–13% to –15% the next day, per [Simply Wall St](https://simplywall.st/stocks/us/diversified-financials/nasdaq-lpla/lpl-financial-holdings/news/lpl-financial-holdings-lpla-stock-dropped-what-is-behind-the) and [TradingView/StockStory](https://www.tradingview.com/news/stockstory:c9ebc7a74094b:0-why-lpl-financial-lpla-stock-is-nosediving/)). It slid a further ~9% from ~$292 (Nov 12) to $264.56 (Nov 20). **No specific cause for the November slide was found** (insufficient data); a $750M bond sale closed Nov 18 and KBW cut its target to $350 on Nov 20.

---

## Step 1. Verify the numbers

Primary filings (SEC EDGAR, Yahoo) were blocked from this environment, so figures come from the company's earnings releases as republished by Nasdaq, StockTitan, Finviz, FinancialContent and the SEC-hosted 8-K copy. Where two copies were read, they agreed.

### 1a. Recent quarters (Fact)

| Quarter | Total revenue | GAAP diluted EPS | Adjusted EPS | Organic net new assets (annualized) | Buybacks |
|---|---|---|---|---|---|
| Q4 2025 | — | $4.24 | $5.23 *(single source)* | $22.5B (3.9%) | $0 |
| Q1 2026 | $4.94B (flat y/y) | $4.43 | $5.60 (+9%) | $21.4B (3.6%) | $0 |
| Q2 2026 | $5.19B (+35%) | $4.74 | $5.84 (+29%) | $23.1B (4.0%) | $309M |
| Q3 2026 | $5.34B (+17%) | $4.52 | $5.97 (+15%) | $29.1B (4.5–5%) | $301M |
| **Trailing 12 months** | ~$20.4B (est.) | **$17.93** | **$22.64** | ~$96B | $610M |

Sources: [Q3 release (Nasdaq)](https://www.nasdaq.com/press-release/lpl-financial-announces-third-quarter-2026-results-2026-10-27), [Q3 (StockTitan)](https://www.stocktitan.net/news/LPLA/lpl-financial-announces-third-quarter-2026-f9516jvjw1ve.html), [Q2 (Finviz)](https://finviz.com/news/375249/lpl-financial-announces-second-quarter-2026-results), [Q1 (FinancialContent)](https://www.financialcontent.com/article/gnwcq-2026-4-30-lpl-financial-announces-first-quarter-2026-results), [FY2025 release (LPL IR)](https://investor.lpl.com/news-releases/news-release-details/lpl-financial-announces-fourth-quarter-and-full-year-2025-0) and [SEC copy](https://www.sec.gov/Archives/edgar/data/1397911/000162828026004112/a2025q4earningsrelease.htm). Investing.com shows TTM EPS of $17.49 vs my $17.93 sum; the gap is unexplained (likely a timing or share-count difference), so treat TTM GAAP EPS as ~$17.5–17.9.

> **Term — GAAP vs adjusted EPS.** GAAP is the official accounting profit. LPL's "adjusted" EPS adds back amortization of acquired intangibles and acquisition/integration costs. Because LPL buys firms regularly, some of those costs recur, so the truth sits between the two. See the [P/E cheat sheet §3](../../docs/guides/pe-ratio-cheat-sheet.md).

### 1b. Full year 2025 (Fact, FY2025 release)

| | 2025 | 2024 | Change |
|---|---|---|---|
| Total revenue | $16.99B | $12.39B | +37% |
| GAAP net income | $863M | $1,059M | –18% (Commonwealth deal costs) |
| GAAP diluted EPS | $10.92 | $14.03 | –22% |
| Adjusted EPS | $20.09 | — | +22% |
| Gross profit | $5.60B | $4.50B | +24% |
| Organic net new assets | $147B (8%) | — | |
| Dividends paid | $94M | | |

### 1c. Balance sheet and capital (Fact, Sep 30, 2026 unless noted)

| Item | Value |
|---|---|
| Total client assets | $2.56T (+11% y/y); advisory $1.56T (61%), brokerage $1.00T |
| Advisors | 32,597 |
| Client cash balances | $56.6B (2.2% of client assets); ~$55.5B in October (management) |
| Corporate debt | ~$7.8B; leverage ratio 1.93x (target range midpoint ~2x); +$750M notes due 2029 issued Nov 18 |
| Corporate cash | $563M |
| Shares outstanding | 78.31M (136.85M issued – 58.54M treasury); cross-checked vs 77.87M (Investing.com) and 77.95M (13F), all within 1% |
| Dividend | $0.30/quarter ($1.20/yr, 0.45% yield) |
| Buyback pace | ~$300M per quarter; board added $2.5B authorization in July 2026 |

### 1d. Valuation snapshot (Estimate, via `tools/financial_rigor.py`)

| Measure | Value | Note |
|---|---|---|
| P/E on TTM adjusted EPS ($22.64) | **11.7x** | Earnings yield 8.6% vs ~4% 10-yr Treasury |
| P/E on TTM GAAP EPS ($17.93) | 14.8x | |
| P/E on next-year consensus (~$29, label unclear) | ~9.1x | Consensus figure from an Investing.com summary; low reliability |
| 5-year median P/E | 24.9x | [GuruFocus](https://www.gurufocus.com/news/9196004/lpl-financial-holdings-inc-lpla-shares-fall-31-what-gf-score-of-93-tells-investors) |
| Shareholder yield (buybacks + dividends, annualized Q3 pace) | ~6.3% | |
| Analyst targets | $320–$526, mean ~$402; KBW $350 (Nov 20) | [Investing.com](https://www.investing.com/equities/lpl-investment-ho); analyst targets are opinions |

### 1e. Earnings quality warning (Fact + View)

LPL's **cash flow can look much worse than its earnings** in growth years. In the first nine months of 2025, operating cash flow was **–$1.20B** vs +$456M a year earlier, mainly because of **$1.57B of net advisor loans** (10-Q, Q3 2025). These are forgivable loans ("transition assistance") paid upfront to recruit advisors, then expensed over several years. Capex runs ~$140–230M a quarter. **View:** this is real reinvestment, not a one-off, which is why the valuation below charges growth for reinvestment instead of treating all earnings as free cash. Full-year 2025 operating cash flow was not obtained (the FY2025 10-K was not reachable): **insufficient data** on multi-year cash conversion. Check this yourself in the 10-K cash flow statement.

---

## Step 2. How LPL makes money (plain English)

**Two-sentence version:** LPL is the back office for ~32,600 independent financial advisors: it provides the custody, trading, technology and compliance they need, and takes a cut of the fees their clients pay. It also earns interest on the uninvested cash sitting in those clients' accounts, which is very profitable when interest rates are high.

| Revenue engine | How it works | Rate sensitive? |
|---|---|---|
| **Advisory fees** | Clients pay advisors ~1% a year on assets; LPL keeps a slice, passes most (~88% payout) to the advisor. Grows with markets and new assets. | No, but falls in a market crash. |
| **Commissions** | Per-trade and product sales (annuities, mutual funds). | No |
| **Client cash ("sweep")** | Idle client cash is swept into partner banks; banks pay LPL interest. Q3: $461M revenue on ~$57B at a 342bp net yield. | **Yes, strongly.** |
| **Service fees, sponsor payments** | Platform fees, fund companies paying to be on the platform. | No |

> **Term — gross profit at LPL.** Because most advisory revenue is passed straight to advisors, LPL's "total revenue" ($5.3B a quarter) overstates its size. The cleaner measure is **gross profit** (revenue minus advisor payout): $1.66B in Q3 2026.

**Rate sensitivity (Estimate):** client cash revenue was **~28% of Q3 gross profit** ($461M / $1,662M). About 65% of the swept cash is in fixed-rate bank contracts (locked for years); ~35% floats. Rough after-tax impact per 25bp change in short-term rates, at 25% tax:

| Scope | EPS impact per 25bp | Timing |
|---|---|---|
| Floating portion only (~35%) | ~$0.47 | Within a quarter |
| All client cash, once fixed contracts reprice | ~$1.36 (~6% of TTM adjusted EPS) | Over several years |
| A 200bp fall, fully repriced | ~$10.8 (~48%) | Several years; extreme case |

These are my estimates; **the company's own sensitivity disclosure (10-K Item 7A) could not be retrieved**, so verify them there. Context (Fact): the Fed **raised** rates 25bp on Sep 16, 2026 to 3.75–4.00% ([Federal Reserve](https://federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)), so the near-term direction is currently helping LPL. The risk is the next easing cycle.

**Why it can be a good business (View):** advisors rarely switch platforms (LPL's own asset retention 97–98%); scale lets LPL spread tech and compliance costs across $2.6T; and the shift of advisors from big wirehouses (Merrill, Morgan Stanley) to independence is a decades-long tailwind. **But on the other hand:** LPL competes for advisors with cash (transition loans), which the CFO said "have been quite high," and its most profitable line depends on interest rates it does not control.

---

## Step 3. Latest earnings call (Q3 2026, Oct 27, 2026)

Speakers: Rich Steinmeier (CEO), Matt Audette (President & CFO). Sources: [StockAnalysis transcript](https://stockanalysis.com/stocks/lpla/transcripts/720319-q3-2026/), [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-lpl-financial-beats-q3-2026-eps-shares-fall-after-hours-93CH-4977126). The second half of the Q&A was only available in summarized form.

**What went well (Fact)**
- Record adjusted EPS $5.97 (+15%); adjusted pre-tax margin ~38.6%.
- Steinmeier: "Prior to large institutional wins, this was our best organic growth rate in over a year."
- Commonwealth run-rate EBITDA target ~$415M by Q4 2027. Audette: "Retention obviously coming in below that 90%, but synergies coming in better."
- Another ~$300M buyback planned for Q4.

**What worried the market (Fact)**
- **Commonwealth retention cut to ~83%** from the ~90% assumed when the $2.7B deal was announced. Some signed advisors chose not to move. Conversion was scheduled for mid-November, "the largest conversion in our history."
- **Recruited assets fell 26%** y/y to $24B; organic growth was ~3% in July, below 4% in September, and "in the zone of 3%" in October with "a larger attrition item."
- Large institutional wins may take "quarters and possibly as long as years," pushing benefit toward 2028.
- Q4 costs step up: higher payout, transition-loan amortization (~$160M), interest (+$11M) and D&A.
- Client cash fell to ~$55.5B in October.

**Toughest analyst questions (Fact, paraphrased)**
- *Can organic growth stay above 5% after a weak September?* (Wolfe) → recruiting has "largely returned to normalized levels."
- *Pricing across sweep, revenue share and platform fees?* (BofA) → work is "well considered"; more detail in the first half of 2027. **View:** this non-answer matters; a sweep-pricing cut would hit the most profitable line.
- *Will transition-loan costs ease?* (Jefferies) → rates "have been quite high" and "could moderate at some point," timing "hard to predict."

---

## Step 4. Bear case: what would make this a bad investment

| # | Risk | Mechanism | How likely / how bad (View) | Watch this number |
|---|---|---|---|---|
| 1 | **Rate cuts** | Client cash yield falls; ~28% of gross profit is interest | Not imminent (Fed just hiked), but certain to come eventually. A full 200bp easing could remove ~half of EPS over years (estimate). | Fed funds; client cash yield (bp) and balance each quarter |
| 2 | **Cash-sweep regulation / lawsuits** | Peers (e.g. Wells Fargo, Morgan Stanley) have faced SEC scrutiny and suits over low sweep rates paid to clients. LPL disclosed an SEC information request (Aug 2024) on advisory cash. Higher client payouts = lower LPL revenue. | Tail risk; management's "pricing review" hints changes are coming. | Any sweep-rate change announced H1 2027 |
| 3 | **Recruiting slows / costs rise** | Growth depends on winning advisors with upfront loans; competitors (Raymond James, Ameriprise, private-equity-backed RIAs) bid up prices | Already visible: recruited assets –26%, organic growth ~3% | Organic NNA growth rate (want ≥4–5%); recruited assets |
| 4 | **Integration / acquisition risk** | Commonwealth retention already fell 90% → 83%; more attrition after the November conversion would cut the $415M EBITDA | Medium; the next two quarters will show it | Q4 2026 / Q1 2027 retention figure |
| 5 | **Debt + market crash** | ~$7.8B debt (1.9x leverage). A bear market cuts advisory fees and cash flow at the same time | Manageable at 1.9x, but leverage magnifies a downturn | Leverage ratio (alarm above ~2.5x) |

**Steelman of the bear case (View):** LPL's 2023–2025 earnings were inflated by unusually high rates and an acquisition spree. If rates normalize to ~2.5%, sweep pricing gets regulated, and recruiting stays expensive, owner earnings could stay flat for years — which is exactly what the bear scenario below assumes, and it is worth ~$239.

**Bull rebuttal (View):** even the 2025 GAAP drop was deal costs, not the core business; assets keep growing with markets plus ~3–5% organic inflows; buybacks at ~11–12x adjusted earnings shrink the share count ~6% a year at the current pace.

> Munger: "Invert, always invert." The question to answer before buying is not "how much could it go up?" but "what would I lose if the bear case is right?" Here: ~10% below today's price on the bear case, more if all five risks hit at once.

---

## Step 5. Fair value and "buy below" price

Full method: `skills/company-valuation.md`. All arithmetic runs in [`model.py`](valuation-20261122/model.py) (Decimal) or `tools/financial_rigor.py`. The terminal-value gate check (`tools/terminal_value.py audit`) **passed** (exit 0).

### 5a. Inputs (Assumptions, labeled)

| Input | Value | Basis |
|---|---|---|
| Starting owner earnings per share | **$21.00** | TTM adjusted EPS $22.64 less ~7% for recurring deal costs and stock comp (assumption) |
| Discount rate r | **10%** | ~4.2–4.7% Treasury + ~5.5% equity premium, beta 1.0. LPL's measured beta (0.54) is lower, but it carries ~2x leverage and rate exposure, so 1.0 is kept. |
| Steady-state return on new capital (ROIC) | 20% | Blend of recruiting loans (high return) and acquisitions (Commonwealth ~8x EBITDA, lower return) |
| Reinvestment | growth ÷ ROIC | e.g. 7% growth retains 35% of earnings for recruiting/deals; the rest goes to buybacks and dividends |
| Share count | Held flat at 78.31M | Buybacks are treated as a way of paying out cash, not as extra growth (avoids double counting) |
| Debt | Already charged | Cash flows are after interest, so no separate debt subtraction |

### 5b. Three scenarios (10-year DCF)

| Scenario | Owner-earnings growth | Terminal growth / P/E | Value per share | vs $264.56 | Terminal share of value |
|---|---|---|---|---|---|
| **Bear** | 0% yrs 1–3 (rate cuts, attrition), 3% after | 2% / 11.2x | **$239** | –10% | 48% |
| **Base** | 7% yrs 1–5, 5% yrs 6–10 | 3% / 12.1x | **$304** | +15% | 60% |
| **Bull** | 11% yrs 1–5, 7% yrs 6–10 | 3.5% / 12.7x | **$366** | +38% | 69% |

**Reverse DCF (Estimate):** at $264.56 the market is pricing **~3.2% a year** owner-earnings growth for 10 years. Track record for comparison: adjusted EPS +22% in 2025; client assets +11% y/y; organic asset growth 3.6–5% annualized in 2026. "The market requires ~3%; recent history shows far more, but much of that history was helped by high rates."

**Sensitivity (base case, value per share):**

| | g = 2% | g = 3% | g = 4% |
|---|---|---|---|
| r = 9% | $337 | $361 | $393 |
| r = 10% | $289 | **$304** | $324 |
| r = 11% | $252 | $262 | $274 |

**Cross-check (3-year multiple method, `financial_rigor.py three-scenario`, adjusted EPS $22.64):** bear 0% growth at 10x → $226; base 8% at 13x → $371; bull 12% at 15x → $477. This method is more generous because it uses per-share adjusted EPS (buybacks included) and charges nothing for reinvestment; the DCF above is the one to rely on. Note that both methods use exit P/Es (10–15x) **well below** LPL's own 5-year median of 24.9x, so neither assumes the old valuation comes back.

### 5c. Price levels

| Price | What it implies | View |
|---|---|---|
| **Below ~$215** | Even the bear case earns more than 10% a year | Strong margin of safety (30% under base) |
| **$215–$240** | Bear case roughly breaks even at a 10% return | **Buy zone** per the routine's 20–30% cushion |
| $240–$304 | Needs the base case to play out | Fair range — **today ($264.56) is here** |
| Above ~$304 | Needs the bull case | Expectations priced in |

**Strongest counter-argument to waiting (View):** a 10% discount rate and a 12x exit P/E are conservative for a business with 97%+ client retention and a 25-year record; at r = 9% the base value is ~$361, which would make today's price a ~27% discount. If you believe LPL deserves a lower discount rate, today is already in the buy zone. The cost of waiting is missing the rebound if the Commonwealth conversion goes smoothly.

**Three numbers that would prove this valuation wrong:**
1. Organic net new asset growth below 3% for two more quarters (base case is too high).
2. Commonwealth retention reported below ~80% after conversion (EBITDA target at risk).
3. A sweep-pricing change that cuts client cash yield by more than ~50bp (bear case becomes base).

---

## What to do next (steps 6–8 of the routine)

1. **Read the primary filings yourself** (the 10-K and Q3 2026 10-Q on [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001397911)): check Item 7A rate sensitivity, the cash flow statement (operating cash flow vs net income for 3 years), and debt maturities. These were the gaps this report could not close.
2. **Set a price alert at ~$240.** If it gets there, re-check the three "prove wrong" numbers above before buying.
3. **If you buy:** start with ~2–5% of non-retirement money, in 2–3 steps (e.g. one now-ish if you accept the counter-argument, one after Q4 results on **Feb 4, 2027**, which will show post-conversion Commonwealth retention).
4. **Write sell rules first:** sell if organic growth stays below 3% for a year, if leverage goes above ~2.5x without a clear payoff, or if sweep regulation cuts client cash revenue by a third. A price drop alone is not a sell signal.
5. **Overlap note (unverified):** S&P 500 membership could not be confirmed; recent market news lists LPL as a *possible* S&P 500 addition ([Reuters via Tiger](https://www-web.itiger.com/news/2608489696)), which suggests it is not in the index today. Total-market funds (and most target-date funds, which hold them) still own a tiny slice, so overlap with your retirement holdings is small. That fits the goal of adding something your index funds barely hold.

> Buffett: "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price." LPL looks like a good company at a fair price today. The routine's discipline says wait for a better one; the counter-argument says fair may be enough. That trade-off is yours to make.

---

## Sources and data reliability

| Data | Source | Reliability |
|---|---|---|
| Q3 2026 results | [Nasdaq press release](https://www.nasdaq.com/press-release/lpl-financial-announces-third-quarter-2026-results-2026-10-27), [StockTitan](https://www.stocktitan.net/news/LPLA/lpl-financial-announces-third-quarter-2026-f9516jvjw1ve.html) | High (company release, two copies) |
| Q1, Q2 2026 | [FinancialContent](https://www.financialcontent.com/article/gnwcq-2026-4-30-lpl-financial-announces-first-quarter-2026-results), [Finviz](https://finviz.com/news/375249/lpl-financial-announces-second-quarter-2026-results) | High |
| FY2025 | [LPL IR](https://investor.lpl.com/news-releases/news-release-details/lpl-financial-announces-fourth-quarter-and-full-year-2025-0), [SEC 8-K copy](https://www.sec.gov/Archives/edgar/data/1397911/000162828026004112/a2025q4earningsrelease.htm) | High; Q4 2025 adjusted EPS single-sourced |
| 2025 cash flow, risk factors | LPL 10-Q Q3 2025 and 10-K FY2024 via [LPL IR](https://investor.lpl.com/static-files/89f32bb9-835d-402f-894a-7fb6123ae2a3) | High, but dated |
| Earnings call | [StockAnalysis](https://stockanalysis.com/stocks/lpla/transcripts/720319-q3-2026/), [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-lpl-financial-beats-q3-2026-eps-shares-fall-after-hours-93CH-4977126) | Medium-high; later Q&A summarized |
| Price, 52-week range, P/E, targets | [Investing.com](https://www.investing.com/equities/lpl-investment-ho), [FinzData](https://data.finzdata.com/stock/lpla), [GuruFocus](https://www.gurufocus.com/news/9196004/lpl-financial-holdings-inc-lpla-shares-fall-31-what-gf-score-of-93-tells-investors) | Medium; consensus EPS and targets low |
| Stock drop reasons | [Simply Wall St](https://simplywall.st/stocks/us/diversified-financials/nasdaq-lpla/lpl-financial-holdings/news/lpl-financial-holdings-lpla-stock-dropped-what-is-behind-the), [TradingView/StockStory](https://www.tradingview.com/news/stockstory:c9ebc7a74094b:0-why-lpl-financial-lpla-stock-is-nosediving/) | Medium |
| Fed rate | [Federal Reserve, Sep 16 2026](https://federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) | High |

**Not obtained (insufficient data):** FY2025 10-K (full-year cash flow, Item 7A rate sensitivity, debt maturities); the cause of the Nov 12–20 price slide; outcome of the Oct 27–28 FOMC meeting.

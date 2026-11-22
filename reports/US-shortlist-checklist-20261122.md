# US "Hold 10 Years" Shortlist Recheck: Mastercard, Progressive, Booking, ADP

> Date: 2026-11-22 · Prices: Nov 20, 2026 close (latest trading day)
> Method: repo skill `/investment-checklist` (six gates, mirror test, veto list); math via `tools/financial_rigor.py`
> Re-evaluates the US names from `10年不能卖-终极选股报告-20260616.md` (June 16, 2026)
> **Labels used below:** **Fact** = reported data with source. **Estimate** = analyst consensus or my arithmetic. **Assumption** = my scenario input, a guess. **View** = interpretation, not data.

---

## Bottom line

| Stock | Nov 20 price | Fwd P/E (2026E/FY27E) | June P/E → now | Checklist | Verdict |
|---|---|---|---|---|---|
| **Booking (BKNG)** | $147.32 | 14.1x | ~21x → ~14x | ✅ 5/6 gates | **Buy candidate.** Best price/quality mix of the four today. Start small; the AI-distribution risk is real and unresolved. |
| **ADP** | $301.19 | 24.4x | 19x → ~27x TTM | ❓ grey zone | **Good business, no longer cheap.** The June reason to buy (10-year-low P/E) is gone after a ~44% rise. Wait for ~$250 or below. |
| **Mastercard (MA)** | $626.85 | 31.2x | 28x → ~33x TTM | ❓ grey zone | **Best business, thinnest margin of safety.** Hold if owned; new money waits for ~$520 or below (~26x 2026E). |
| **Progressive (PGR)** | $230.13 | 14.4x on 2027E | 11x → 11.6x TTM | ❓ grey zone | **Cheap on past earnings, not on future ones.** Consensus sees EPS falling ~13% in 2027. Watch; buy in steps below ~$200. |

Probability-weighted 5-year return (25% bull / 50% base / 25% bear, price CAGR + current dividend yield; **assumption-driven**, see each section):

| | Bull | Base | Bear | Weighted |
|---|---|---|---|---|
| BKNG | 26.9% | 17.7% | 4.5% | **~16.7%** |
| ADP | 18.3% | 12.1% | 4.4% | **~11.7%** |
| MA | 14.6% | 7.7% | -0.7% | **~7.3%** |
| PGR | 14.6% | 7.6% | -2.2% | **~6.9%** (understated: excludes PGR's annual variable dividend) |

**What changed since June (facts):** Booking fell to its 52-week low ($144.10 intraday Nov 20) after a weak Q4 guide; ADP rose from ~$209 to ~$301; Mastercard drifted up modestly; Progressive's price is about flat but its earnings outlook turned down. The June ranking (MA > PGR > BKNG, ADP runner-up) is therefore **reversed on price**: the business quality ranking is roughly unchanged, but the price attached to each business moved a lot.

**Overlap note (View):** all four are S&P 500 members, so Justin's target-date funds and ETFs already own small slices. Buying any of them is a deliberate overweight, not new exposure. MA is the largest index weight of the four; BKNG and ADP are smaller.

---

## Data used (all Nov 20, 2026 close unless noted)

| | MA | PGR | BKNG | ADP |
|---|---|---|---|---|
| Price | $626.85 | $230.13 | $147.32 | $301.19 |
| Shares outstanding | 871.18M | 579.36M | 743.70M | 394.76M |
| Market cap (price × shares, hand-checked) | $546.1B | $133.3B | $109.6B | $118.9B |
| Market cap as reported (Fox/FactSet) | $560.5B (2.6% off) | $132.4B | $114.0B (3.9% off) | $120.6B |
| TTM EPS (as shown by source; basis not labeled) | $19.15 | $19.90 | $9.31 | $11.31 |
| TTM P/E | 32.7x | 11.6x | 15.8x | 26.6x |
| Current-year EPS consensus | $20.06 (2026) | $18.38 (2026) | $10.47 (2026) | $12.37 (FY Jun-27) |
| Next-year EPS consensus | $23.21 | **$16.03** (decline) | $12.24 | $13.52 |
| 52-week range | $464.52–681.99 | $189.20–241.00 | $144.10–220.79 | $188.16–316.14 |
| Dividend yield (estimate) | 0.56% | 0.17% regular + annual variable | 1.14% | ~2.3–2.5% |
| Analyst mean target / rating | $729 / Buy | $237 / Hold | $215 / Buy | $301 / Hold |

Sources: [Fox Business / FactSet quote pages](https://www.foxbusiness.com/quote?stockTicker=MA) (MA, PGR, BKNG, ADP), cross-checked against [HeyGoTrade MA](https://www.heygotrade.com/en/us-stock/ma/) ($625.59 close, 871.2M shares), [StockTitan PGR](https://www.stocktitan.net/news/PGR/progressive-reports-october-2026-8uw7owl88rf2.html) ($228.47, $132.37B), [Tickeron ADP](https://tickeron.com/blogs/adp-delivers-q1-fiscal-2027-results-with-6-revenue-growth-and-13-eps-rise-adp-23535/) ($301.71, $120.2B). Small price differences are capture-time differences. Quote APIs (Yahoo, Stooq, StockAnalysis) were blocked from this environment, so no figure here came from the repo's `stock_screener.py`.

**Data caveats:** TTM EPS basis (GAAP vs adjusted) is not labeled by the quote source. BKNG's $9.31 and MA's $19.15 don't reconcile cleanly with quarterly sums found elsewhere. Forward P/Es use consensus means, which are estimates.

---

## 1. Booking Holdings (BKNG) — ✅ Buy candidate

**Information grade: A** (long public history, rich data). Beware the consensus trap in reverse: the market currently agrees AI is a threat.

### Six gates

| Gate | Score | Why |
|---|---|---|
| 1. Circle of competence | ★★★★ | Takes a commission (agency) or margin (merchant) on hotel/alt-stay bookings. Simple; the hard variable is how travelers will search in 2030. |
| 2. Good business | ★★★★★ | Fact: FY2025 ROIC ~44% (GuruFocus, per June report), FCF $9.1B, asset-light. Q3 2026 operating margin 38.4%, flat YoY (StockStory). |
| 3. Moat | ★★★★ | Supply side (millions of properties, payments, local compliance) is hard to copy. Demand side (traffic from Google/AI assistants) is the soft spot. Trend: stable, not widening. |
| 4. Management | ★★★★ | Fact: $2.1B buyback in Q3, $12.4B authorization left, share count ~7.5% lower YoY (Pomegra). CEO Fogel; no founder. |
| 5. Margin of safety | ★★★★ | ~14x 2026E / ~12x 2027E consensus EPS for a 40%+ ROIC business. Base case doubles in 5 years on modest assumptions. |
| 6. Discipline | Pass | Thesis fits in 200 words (below). Can you sit through another -30%? The stock just did -33% from its high. |

### What's new since June (facts)
- **Q3 2026** (reported Nov 3): adjusted revenue $9.8B (+9%), gross bookings $54.5B (+10%), room nights 345M (+7%), adjusted EPS $4.66 (+17%) vs ~$4.50 consensus. GAAP revenue $8.89B (-1.3%) was cut by a **$900M FTC-related reduction** (plus a $100M accrued loss); details of that matter are not verified here. ([StockStory](https://stockstory.org/us/stocks/nasdaq/bkng/news/earnings/booking-nasdaqbkng-reports-sales-below-analyst-estimates-in-q3-2026-earnings), [Pomegra](https://pomegra.io/news/booking-holdings-bkng-q3-2026-stock-jumps-10-on-beat))
- **Q4 guide is weak:** room nights +1–3%, adjusted revenue 0–2% (2–4% constant currency). Management cites the toughest comp of the year, Middle East conflict lifting airfares, European unrest, and softer demand late in Q3. FY2026 still guided to adjusted EPS up low-to-mid teens.
- **Stock path:** ~$154 after the print, ~$171 on Nov 4 (+10% day), then down to $147 by Nov 20. Insiders sold at ~$156–160 on Nov 18 (Fox Business).
- **AI:** referrals from outside AI platforms are "significantly below 1%" of room nights but accelerating. Users of Booking's own AI assistants convert at ~2x non-users. Management calls AI "a distribution risk to monitor."

### Scenarios (5 years, from 2026E EPS $10.47) — **assumptions**
| | EPS growth | Exit P/E | Price | Annual return incl. dividend |
|---|---|---|---|---|
| Bull | 15% | 22x | $463 | 26.9% |
| Base | 11% | 18x | $318 | 17.7% |
| Bear | 5% | 13x | $174 | 4.5% |

Base case 11% EPS growth = high-single-digit bookings growth + ~4% buyback. Bear case = AI assistants take a real cut of traffic and growth halves. Even the bear case doesn't lose money from here **if** 13x holds; a deeper derating (10x) on 5% growth would be roughly flat over 5 years (my arithmetic).

### The other side (must read)
- The market is not stupid: a 52-week low after a beat means investors are pricing **slowing travel demand plus AI disintermediation**. If Google or an AI assistant becomes the place people book and Booking becomes a back-end supplier, take rates fall. "Below 1% of room nights" today says little about 2030.
- Q4 guide implies growth stalling to near zero in constant currency. One weak quarter or the start of a travel downturn is not yet distinguishable.
- The FTC matter is a new regulatory fact; scope is unclear from the sources read.

### Mirror test
> "I buy Booking at $147 because: (1) it is a toll on hotel and stay bookings worldwide, and I understand it; (2) its moat is supply aggregation plus payments, stable, with demand-side risk from AI; (3) management buys back ~5–7% of shares a year and has not done foolish deals; (4) price is ~14x this year's earnings, roughly 30% below a fair 18–20x; (5) if I'm wrong about AI, earnings growth slows but the business is still profitable, so the downside is a weak decade, not a wipeout."

**Verdict: Pass (5/6, with AI risk flagged).** Of the four, this is where the June thesis got *stronger* on price. View: a starter position, adding on further weakness, fits better than a full position at once.

> Buffett: "Be fearful when others are greedy, and greedy when others are fearful." The fear here has a real cause, which is why it needs sizing discipline.

---

## 2. ADP — ❓ Grey zone (great business, full price)

**Information grade: A.**

### Six gates

| Gate | Score | Why |
|---|---|---|
| 1. Circle of competence | ★★★★★ | Runs payroll/HR for ~1M+ employers; earns fees plus interest on client funds. |
| 2. Good business | ★★★★★ | Fact: Q1 FY27 adjusted EBIT margin 26.8% (+130bp), ROIC ~42% (June report). Recurring, low capex. |
| 3. Moat | ★★★★ | Switching costs and compliance ("payroll must be right every time," CEO Maria Black). Watch "lower-cost or consumption-based alternatives" (Investing.com risk summary). |
| 4. Management | ★★★★ | Six straight beats; guidance raised. Dividend raised for decades (sources disagree: 51 vs 27 years; the 51 figure matches the June report). |
| 5. Margin of safety | ★★ | 26.6x TTM, 24.4x FY27E. Analyst mean target ($301) equals today's price. |
| 6. Discipline | Caution | The June case was "buy at a 10-year-low 19x." That reason no longer exists. Buying now after a 44% run risks being "recent-performance" driven. |

### What's new since June (facts)
- **Q1 FY27** (Sep quarter, reported Oct 28): revenue $5.49B (+6%), adjusted EPS $2.82 (+13%) vs $2.77 consensus, client-funds interest $329M (+15%). US pays-per-control only +2%. ([Investing.com](https://uk.investing.com/news/stock-market-news/adp-q1-fiscal-2027-slides-13-eps-growth-raised-outlook-93CH-4938094))
- **FY27 guidance raised:** revenue ~6%, adjusted EPS +10–12% (from 9–11%), client-funds interest $1.59–1.61B.
- Stock: ~$209 in May → $285 after the print → $301 now; 52-week high $316.

### Scenarios (5 years, from FY27E EPS $12.37) — **assumptions**
| | EPS growth | Exit P/E | Price | Annual return incl. dividend |
|---|---|---|---|---|
| Bull | 11% | 30x | $625 | 18.3% |
| Base | 9% | 25x | $476 | 12.1% |
| Bear | 6% | 20x | $331 | 4.4% |

**Caution on these numbers (View):** the base case leans on the multiple staying at 25x. If it returns to the 19x of May, the base case drops to roughly 7% a year (my arithmetic: $19.03 × 19 = $362). The return is mostly earnings growth plus dividend; little is left for re-rating.

### The other side
- Bull view: ADP has historically traded at 25–30x, so the May level was the anomaly, and today is "fair."
- Bear view: employment growth is slowing (pays-per-control guide ~1%), rate cuts would shrink the $1.6B float income, and AI-native payroll players could pressure pricing in small business.

**Verdict: Grey zone.** The business passes every quality gate; the price gate fails. Hold if owned. New money: wait for ~$250 or below (~20x FY27E), or accept ~10–12% expected returns with little cushion.

> Munger: "A great business at a fair price is superior to a fair business at a great price." ADP is now a great business at a full price, not a fair one.

---

## 3. Mastercard (MA) — ❓ Grey zone (best business, thin cushion)

**Information grade: A.**

### Six gates

| Gate | Score | Why |
|---|---|---|
| 1. Circle of competence | ★★★★★ | Toll on card transactions plus fast-growing services (fraud, data). No credit risk. |
| 2. Good business | ★★★★★ | Fact: FY2025 revenue $32.8B, net margin 45.6%, operating margin 57.6% (StockTitan). Q3 2026 revenue +14%, profit grew faster (10-Q headline). |
| 3. Moat | ★★★★★ | Two-sided network duopoly with Visa. New: proposed merchant settlement includes a 5-year US credit interchange rate cap, pending final court approval (8-K via StockTitan). Stablecoin/"multi-money" rails (BVNK platform, Oct 2026) show it is co-opting rather than fighting new rails. |
| 4. Management | ★★★★ | CEO Miebach; steady buybacks. Insider selling only (CFO sold ~4.3K shares at $641 on Nov 2). |
| 5. Margin of safety | ★★ | 32.7x TTM, 31.2x 2026E, 27.0x 2027E. Little room if growth slows to low double digits. |
| 6. Discipline | Pass | Easy 200-word thesis. Owning it through a 30% drop is plausible given business quality. |

### Scenarios (5 years, from 2026E EPS $20.06) — **assumptions**
| | EPS growth | Exit P/E | Price | Annual return incl. dividend |
|---|---|---|---|---|
| Bull | 15% | 30x | $1,210 | 14.6% |
| Base | 12% | 25x | $884 | 7.7% |
| Bear | 8% | 20x | $590 | -0.7% |

### The other side
- Bull view: consensus already has 2027 EPS +16% ($23.21). At that pace, ~27x next year's earnings is reasonable for a near-monopoly; MA has rarely been "cheap."
- Bear view: the rate cap, stablecoins, and real-time account-to-account payments (UPI-style, FedNow) all chip at the edges. None is fatal; together they could pull growth toward 10%, and the stock's 31x would then compress.

**Verdict: Grey zone.** Business passes everything; price is the only issue. Hold if owned. New money: wait for ~$520 or below (~26x 2026E) or a market-wide sell-off. View: this is the most "sleep-at-night" holding of the four, but at today's price expected returns look like the index, not better.

> Buffett: "Price is what you pay; value is what you get."

---

## 4. Progressive (PGR) — ❓ Grey zone (cyclical peak risk)

**Information grade: A** (monthly reporting gives very fresh data).

### Six gates

| Gate | Score | Why |
|---|---|---|
| 1. Circle of competence | ★★★★ | Prices auto insurance better than peers using driving data; earns underwriting profit plus float income. Cycle timing is the hard part. |
| 2. Good business | ★★★★ | Fact: TTM ROE 27.9%, down from 41.1% a year ago; debt/capital 19% (Zacks via Yahoo). Still excellent, but falling. |
| 3. Moat | ★★★★ | Fact: policies in force 40.5M, +6% YoY. Still taking share in a flat market (industry 2026 personal auto premiums forecast -0.6%, Triple-I/Milliman). |
| 4. Management | ★★★★★ | CEO Tricia Griffith; long record of underwriting discipline. |
| 5. Margin of safety | ★★★ | 11.6x TTM looks cheap, but 14.4x 2027E consensus is fair, not cheap. |
| 6. Discipline | Caution | The low trailing P/E is the classic insurance trap: it looks cheapest at peak margins. |

### What's new since June (facts)
- **October 2026 results** (Nov 18): net premiums written +1% to $7.08B, combined ratio 91.2 (vs 89.7), EPS $1.43 (-1%). Direct auto combined ratio 96.1. ([StockTitan](https://www.stocktitan.net/news/PGR/progressive-reports-october-2026-8uw7owl88rf2.html), [Insurance Business](https://www.insurancebusinessmag.com/us/news/breaking-news/progressive-direct-auto-outpaces-agency-as-combined-ratio-drifts-598042.aspx))
- Company says the 1% premium growth is understated ~2–3 points by a calendar quirk (Oct 31 fell in November's close cycle). YTD premiums +5%, YTD combined ratio 87.9.
- Stock fell 3.6% on Nov 18 ([TradingKey](https://www.tradingkey.com/news/market-movers/262311417-market-movers-pgr-20261118)). Consensus: 2026E EPS $18.38 → 2027E $16.03.
- June's monitoring trigger ("watch for combined ratio above 96% for consecutive months") is **not** triggered company-wide, but direct auto hit 96.1 in October. **Check November results (due Dec 16).**

### Scenarios (5 years, from 2027E EPS $16.03, i.e. already "normalized") — **assumptions**
| | EPS growth | Exit P/E | Price | Annual return incl. regular dividend |
|---|---|---|---|---|
| Bull | 12% | 16x | $452 | 14.6% |
| Base | 8% | 14x | $330 | 7.6% |
| Bear | 3% | 11x | $204 | -2.2% |

Returns exclude PGR's large annual variable dividend (paid each December, size depends on the year's profits; amount not verified here), so true returns are somewhat higher, likely 1–3 points a year (estimate).

### The other side
- Bull view: PGR keeps gaining share in every cycle; a soft market is when weaker rivals cut prices and lose money, and PGR comes out bigger.
- Bear view: auto insurance margins are mean-reverting. Earnings are expected to fall in 2027, and long-run autonomous driving may shrink the premium pool.

**Verdict: Grey zone.** Great operator, but the cycle is turning against it now. Watch November (Dec 16) and Q4 results. View: buying in steps below ~$200 (~12.5x 2027E) gives a better cushion.

> Buffett on insurance: the best time to own an insurer is when its underwriting discipline lets it grow while others retreat. That test comes in the soft market now starting, not at peak margins. (Paraphrase, View.)

---

## Quick veto list (all four)

None of the eight vetoes triggered for any stock: all have clear business models, positive FCF, no integrity issues, and no evidence of irreversible moat erosion. The only "watch" item is BKNG's AI distribution risk (possible erosion, not proven).

## Overview

| Company | Passes? | Circle | Business | Moat | Mgmt | Safety margin | Conclusion |
|---|---|---|---|---|---|---|---|
| BKNG | ✅ | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | Buy candidate, size small |
| ADP | ❓ | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★ | Wait for ~$250 |
| MA | ❓ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★ | Wait for ~$520 |
| PGR | ❓ | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★ | Watch Dec 16; steps below ~$200 |

## Open items / what would change these verdicts
1. **BKNG:** Q4 results (Feb 2027). Accelerating AI referral share or a take-rate drop would weaken the thesis; stable take rate plus room-night growth back to mid-single digits strengthens it.
2. **PGR:** November monthly results on Dec 16; December variable dividend size.
3. **MA:** final court approval of the merchant settlement.
4. **ADP:** pays-per-control trend and Fed rate path (float income).
5. **Data:** this run used delayed quote pages, not exchange data. Re-pull prices before any trade.

---

*The first rule of investing is don't lose money; the second rule is don't forget rule No. 1. — Buffett*

*Disclaimer: research only, not investment advice. Scenario inputs are the author's assumptions; change them and the returns change.*

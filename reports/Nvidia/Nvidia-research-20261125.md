# Nvidia (NVDA) pre-buy research: a fair price, not yet a bargain, so buy slowly with a $140 buy-below and hard stop-adding rules

> Research date 2026-11-25 · Price **$149.30** (Nov 25 close, –3.91%) · Market cap **$3.61T** (verified: $149.30 × 24.186B diluted shares = $3.61T, `tools/financial_rigor.py verify-market-cap`, 0.03% deviation) · All figures USD · Nvidia's fiscal year ends late January, so "Q3 FY27" = Aug–Oct 2026
> Method: [pre-buy routine](../../docs/guides/pre-buy-routine.md) steps 1–8. This **updates** the [Nov 23 short evaluation](Nvidia-short-20261123.md) rather than redoing it: the business figures (step 1), business description (step 2) and bear case (step 4) there still stand and are only summarized here. Model script: [`valuation-20261125/model.py`](valuation-20261125/model.py) reproduces every Estimate below.
> **Labels:** **Fact** = reported figure with a source. **Estimate** = arithmetic on reported figures. **Assumption** = a scenario input, i.e. a guess. **View** = interpretation, not data.
>
> *Educational research, not investment advice. No trades were placed.*

---

## Bottom line

| | |
|---|---|
| **Verdict** | **Buy candidate as a small, slow DCA position.** The price is fair, not cheap: it sits between the buy-below line and fair value, so buy half-size until it drops below $140 or the investigations close cleanly. |
| Fair value (assumption-driven) | **~$175** base case (used as the anchor). Probability-weighted ~$196 (bust ~$82 / base ~$175 / bull ~$306, unchanged from Nov 23). |
| **Buy below** | **$140** (20% under the $175 base; 28% under the weighted $196). Deep-cushion line: **~$122**. |
| Today | **$149.30**: 7% above buy-below, 15% below base fair value. The stock touched **$141.17** intraday today. |
| What today's price assumes | Earnings stay roughly flat at today's run rate (~$10.70/share) forever. Put another way, the price already bakes in about a **40% chance of the bust case** (Estimate, §5). |
| **Starter size** | **1% of non-retirement money**, building to **3% max** over six months. You already own roughly 6% NVDA through your index funds (Estimate, unverified), so 3% here is a bigger bet than it looks. |
| **Schedule** | Six monthly buys, **mid-Dec 2026 to mid-May 2027**, each 0.5% of the money. Full tranche at or below $140, half tranche from $140 to $175, skip above $175. **Wait for the 10-Q (due ~Dec 4) before the first buy.** |
| **Stop adding if** | The 10-Q is late or restates anything; the SEC escalates (Wells notice or charges); the board investigation finds wrongdoing or Huang leaves again; two or more of Amazon/Alphabet/Microsoft/Meta guide 2027 capex flat or down; Q4 FY27 revenue comes in below $126B or gross margin below 70%. Full list in §7. |

---

## 1. What changed since Nov 23 (Fact)

| Date (2026) | Event | NVDA close |
|---|---|---|
| Nov 23 (Mon) | Board reinstates Huang. Monday's ~$165 is now **verified as the close** ($165.05, +31.48%; high $171.50) | $165.05 |
| Nov 24 (Tue) | Chip stocks give back Monday's gains; NVDA –5.9% (headline only). Trump tells the New York Post a pardon for Huang is "always an option," though he doesn't think it will be necessary | ~$155.38 (Estimate, implied from Nov 25's % change) |
| Nov 25 (Wed) | October PCE inflation 3.8% y/y (core 3.3% vs 3.2% expected), raising expectations of Fed **rate hikes** in December and January. US proposes Section 301 tariffs on 14 trading partners (China +20% on top of 2018's 25%). S&P puts Nvidia's credit rating on CreditWatch Negative (single source). Nasdaq falls 4.6% intraday before recovering to –0.6% | **$149.30** (–3.91%, low $141.17, volume ~91% above average) |

Sources: [StockAnalysis price history](https://stockanalysis.com/stocks/nvda/history/); [Motley Fool via Yahoo Finance, Nov 25](https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-25-220645995.html); [ChipDispatch, Nov 25](https://chipdispatch.com/articles/nvidia-micron-slide-as-nasdaq-erases-4-6-intraday-rout) (both agree on the $149.30 close and –3.91%); [Newsweek](https://www.newsweek.com/trump-floats-jensen-huang-pardon-doj-insists-no-investigation-12765547).

**Net effect:** the stock has given back half of Monday's jump in two days. At $149.30 it is **38% below** the Oct 6 peak of $239.24 (Estimate).

---

## 2. The investigation overhang, updated (Fact unless marked)

The Nov 23 report flagged open investigations. None has closed. The list has grown.

| Matter | Status | Source |
|---|---|---|
| **SEC enforcement** | Examining "potential accounting issues" (unidentified). NYT calls it early-stage and says it may not lead to charges. SEC declines comment. | Reuters/[Forbes](https://www.forbes.com/sites/fionariley/2026/11/20/sec-is-investigating-nvidias-accounting-practices-according-to-report/); [Wikipedia summary](https://en.wikipedia.org/wiki/Jensen_Huang_spying_scandal) |
| **Board's independent investigation** | Run by Wachtell Lipton and former acting US attorney Joon Kim; Nvidia said Nov 23 it "will proceed to conclusion." No timeline. | Nvidia; [Digg roundup](https://digg.com/world-business/ardhy3n8) |
| **DOJ** | Criminal probe of **Megaspeed** (chip diversion), not publicly of Huang. Also reviewing the $12.9B Hugging Face deal. AG Blanche says DOJ has "no information" of wrongdoing by Huang but can't predict future investigations. | [Newsweek](https://www.newsweek.com/trump-floats-jensen-huang-pardon-doj-insists-no-investigation-12765547); [SocialNews/IANS](https://www.socialnews.xyz/2026/11/20/sec-probing-nvidias-accounting-reuters-reports-huang-agrees-to-testify-before-senate/) |
| **State AGs** | California AG subpoena (did Nvidia or Huang help China get chips; did Nvidia mislead investors). Missouri AG looking at harm to state pension funds. | Digg roundup citing FT |
| **Shareholder suits** | A class action over Megaspeed/disclosures and a derivative suit against Huang and directors. | Digg roundup citing FT |
| **Congress** | **Dec 1**: closed-door transcribed interview with House Foreign Affairs, Intelligence and China Select committees. **Dec 3** (reported): public Senate Banking hearing on export controls. Congress pushing tighter chip export rules into the defense bill. | Digg roundup; SocialNews |
| **Export rules** | Nov 19: new licence requirement for advanced chips to Singapore, Malaysia, Thailand, Indonesia and Brazil. China data-center revenue already guided at zero. | Wikipedia summary (Federal Register) |
| **Credit ratings** | Moody's cut outlook to stable from positive (Aa1 affirmed) on governance. S&P CreditWatch Negative on Nov 25. | Moody's: [Wikipedia summary](https://en.wikipedia.org/wiki/Jensen_Huang_spying_scandal); S&P: ChipDispatch citing CNBC (**single source each**) |

### The pardon remarks (Fact, then View)

- **What was said:** Trump told the New York Post a pardon for Huang is "always an option" but likely unnecessary, and "I don't think he needs to take the Fifth." Vice President Vance said Nov 25 that Huang is under no investigation and doesn't need a pardon. AG Blanche said DOJ has no information of wrongdoing.
- **What it doesn't cover:** a presidential pardon covers **federal crimes only**. It does nothing about the SEC's civil accounting probe, state AG actions, shareholder suits or the board's findings, and nothing about whether Nvidia's past revenue is correctly stated. (General legal fact; not specific to any filing.)
- **View:** for a shareholder, the pardon talk is close to irrelevant on the upside and mildly negative on the downside. It doesn't make the accounting question go away, and it ties Nvidia more tightly to one administration, which raises political risk with Congress (bipartisan criticism already) and with any future administration. The useful signal next week is whether Huang answers questions at the Dec 1 interview or invokes the Fifth; invoking it would not prove anything, but the market would likely treat it badly.

### The one date that matters most: the 10-Q (~Dec 4)

The Q3 FY27 10-Q is not yet filed; the 40-day SEC deadline after the Oct 25 quarter-end lands in early December (SocialNews/IANS). This is the cheapest test available. Read three things:
1. **Is it on time?** A late-filing notice (Form 12b-25 / "NT 10-Q") is a red flag.
2. **Any restatement or "material weakness" in internal controls?**
3. **New risk-factor or legal-proceedings language** on the SEC probe, receivables ($81B, ~64 days of sales) and the geographic revenue change (FT reported ~$104B of 2025 sales booked to Singapore before Nvidia switched to customer-headquarters reporting).

**That is why the plan waits for the 10-Q before the first buy.** It costs at most a week.

---

## 3. Big-tech capex: the biggest business risk (step 4, refreshed)

**Fact (from the Nov 23 report):** hyperscalers were 56% of Nvidia's Q3 data-center revenue. Big-four quarterly capex doubled y/y to ~$202B; 2026 guidance ~$730B; 2027 consensus ~$935B (+28%). Every company that has spoken guided 2027 **up**. But Alphabet, Amazon and Meta had **negative free cash flow** in Q3 2026 and all four sold bonds to fund the build ([Luminix](https://www.useluminix.com/reports/industry-analysis/hyperscaler-capex-q3-2026); S&P via [Yahoo/Motley Fool](https://finance.yahoo.com/technology/ai/articles/6-hyperscalers-driving-ai-revolution-104200428.html)).

**What's new this week (Fact):** Axios ran an "AI's spending slowdown" piece on Nov 23 ([link](https://www.axios.com/2026/11/23/ai-spending-slowdown); not readable from this environment, contents unverified). Inflation at 3.8% and expected rate **hikes** raise the cost of the debt funding this build.

**Mechanism (View):** a debt-funded boom slows when borrowing gets expensive or shareholders push back on negative free cash flow. Higher rates push on both at once. Nvidia doesn't need capex to fall to get hurt; it needs 2027 growth to come in well below the +28% consensus.

**Numbers to watch (Jan–Feb 2027 earnings calls):**

| Watch | Healthy | Warning (stop adding) |
|---|---|---|
| 2027 capex guides from Amazon, Alphabet, Microsoft, Meta | Up 20%+ combined | **Two or more guide flat or down** |
| Hyperscaler free cash flow | Back toward positive | Deeper negative plus more bond issuance |
| Nvidia Q4 FY27 (late Feb) | Revenue ≥ $130B guide, gross margin ≥ 71% | **Revenue < $126B (bottom of guide) or GM < 70%** |
| Fed path | Hikes priced and absorbed | Repeated surprise hikes |

---

## 4. Why own it at all: the long case (View, with Facts)

- **Still growing fast:** Q3 revenue $115.8B, +103% y/y; Q4 guided to $130B (Fact, Nvidia release).
- **Priced like a utility-grade grower:** 13.9x run-rate earnings, 4.8% FCF yield (Estimate). Trefis puts NVDA's lowest year-end P/E of the past decade near ~20x.
- **Net cash and huge buybacks:** ~$21B net cash; $22B bought back in Q3 alone; ~$227B authorization left (Fact, single source for the split).
- **Fits the goal:** the project wants a handful of long-term holdings. Nvidia is the core supplier of the AI build-out with a software moat (CUDA). A slow DCA lets the investigations play out while you build.

**But on the other hand:** a low P/E on peak earnings is the classic cyclical trap (Cisco 2000). If 2026 is peak earnings, 14x isn't cheap. And the accounting question is unresolved: if revenue was overstated, the "E" in P/E is wrong. That is why the plan buys slowly and has hard stop rules rather than a big lump sum.

---

## 5. Set the price (step 5, updated to $149.30)

| Scenario | Normalized EPS | P/E | Value | vs $149.30 | Probability (subjective) |
|---|---|---|---|---|---|
| Bust: 2001-style digestion | $5.50 | 15x | **$82** | –45% | 20% |
| Base: growth slows to low teens | $12.50 | 14x | **$175** | +17% | 50% |
| Bull: FY28 consensus delivered | $17.00 | 18x | **$306** | +105% | 30% |
| Probability-weighted | | | **$196** | +31% | |

Assumptions unchanged from Nov 23. The new information (investigations widening, rate hikes, tariffs) argues for **more weight on bust**, not for new scenarios, so it is handled in the sensitivity table below.

**Sensitivity (Estimate):**

| If the bust odds are… (taken from bull) | Weighted value |
|---|---|
| 20% | $196 |
| 30% | $173 |
| **40%** | **$151 ≈ today** |
| 50% | $129 |
| Rate-hike haircut (every multiple –2 turns, original odds) | $171 (base drops to $150) |

**Reading this (View):** today's price is what you get if you think there's roughly a 40% chance of a 2001-style bust, or if rate hikes knock two turns off every multiple. Both are plausible, which is why $149 is a **fair** price rather than a cheap one.

**Why anchor on $175, not $196:** the bull case's 30% weight is a guess, and the open accounting probe could change the earnings base itself. Anchoring on the base case and then asking for a 20% cushion gives **$140**, which is also 28% under the weighted value, so it meets the routine's 20–30% rule either way.

| Zone | Price | Action |
|---|---|---|
| Above fair value | > $175 | Skip buys |
| Fair, thin cushion | $140–$175 | Half tranches only |
| **Buy below** | **≤ $140** | Full tranches |
| Deep cushion | ≤ $122 | Full tranches, but first check *why* it fell. A drop this deep probably comes with news that may trigger a stop rule |

**Today: $149.30 → half-tranche zone.**

---

## 6. Size it (step 6)

- **Starter: 1%** of non-retirement money. **Target: 3%** by May 2027. **Ceiling: 5%**, only if the investigations close cleanly *and* 2027 capex guides hold up.
- **Index overlap:** your target-date funds and ETFs already hold NVDA at roughly its index weight. At a ~$3.6T market cap that is on the order of 6% of the S&P 500 (Estimate, not verified today; check your funds' top-holdings pages). Your total NVDA exposure is the sum.
- **Drawdown check (Estimate):** a full 3% position bought at $149 and marked to the $82 bust case loses ~1.3% of your non-retirement money. That is survivable, which is the point. At 5% the hit is ~2.2%.

---

## 7. Rules written before buying (step 7)

**Stop adding (pause; reassess, don't panic-sell):**
1. 10-Q filed late, or contains a restatement or a material weakness in internal controls.
2. SEC escalates: a Wells notice, charges, or a disclosed formal order focused on revenue recognition.
3. The board investigation finds wrongdoing, or Huang leaves again.
4. Two or more of Amazon, Alphabet, Microsoft and Meta guide 2027 capex flat or down (Jan–Feb calls).
5. Q4 FY27 results (late Feb): revenue below $126B or gross margin below 70%.
6. New export rules that cut off a major market beyond China (watch the defense bill and the Nov 19 Southeast Asia licence rule).

**Sell (thesis broken):**
- A restatement that **reduces** reported revenue or profit, or evidence that sales were booked to evade export controls.
- Data-center revenue falls **two quarters in a row**.
- Gross margin below **65%** for two quarters (pricing power gone).

**Speed up (move to full tranches up to $175):** the board investigation closes without findings **and** the SEC probe is closed or narrowed to non-revenue issues, with no stop rule triggered.

**Never:** add because the price dropped alone, or exceed 5%.

---

## 8. Buy in steps (step 8): the DCA plan

Each tranche = **0.5% of non-retirement money**. Six tranches = 3%.

| # | When (around the 15th) | What to check first |
|---|---|---|
| 1 | **Mid-Dec 2026**, after the 10-Q is filed (~Dec 4) and the Dec 1–3 hearings | 10-Q on time and clean (rule 1) |
| 2 | Mid-Jan 2027 | Fed decisions; any SEC/board news |
| 3 | Mid-Feb 2027 | Hyperscaler 2027 capex guides (rule 4) |
| 4 | Mid-Mar 2027 | Nvidia Q4 FY27 results, late Feb (rule 5) |
| 5 | Mid-Apr 2027 | Investigation status |
| 6 | Mid-May 2027 | Nvidia Q1 FY28 results come late May; reassess the 5% ceiling after |

**Size each tranche by price on the day:** ≤ $140 full (0.5%), $140–$175 half (0.25%), > $175 skip. Skipped or half amounts are **not** made up later; that keeps you from chasing.

**Illustrative (Estimate, `model.py`):** if NVDA traded $149, $135, $128, $150, $170, $185 on the six dates, you would invest 3.5 of 6 tranches at an average cost of ~$141, below today's price.

> Munger: "The big money is not in the buying and selling, but in the waiting." The plan is built to wait for the investigations without missing the price.

---

## One-page checklist

```
[x] 1. Revenue, margins, FCF, debt, share count (Nov 23 report; Q3 FY27 release + 1 cross-check)
[x] 1. Market cap hand-checked: $149.30 × 24.186B = $3.61T
[x] 2. Two-sentence business description (Nov 23 report §3)
[ ] 3. Earnings call transcript read (not done; see Limits)
[x] 4. Bear case with numbers to watch (Nov 23 §4; capex refreshed §3)
[x] 5. Fair value: $175 base / $196 weighted   Buy below: $140   Today: $149.30
[x] 6. Position size: 1% start, 3% target, 5% ceiling
[x] 7. Stop-adding and sell rules written (§7)
[x] 8. Six monthly tranches, mid-Dec 2026 to mid-May 2027, first after the 10-Q
```

---

## Limits of this research

- **Single-source items:** the S&P CreditWatch action (ChipDispatch citing CNBC), Moody's outlook cut (Wikipedia summary), Nov 24 price move (headline only), and the state AG and shareholder-suit details (Digg roundup citing FT).
- The Axios capex-slowdown article and the CNBC pardon article could not be read; their contents are not used.
- Vance's "no investigation" statement conflicts with reported SEC, state and shareholder matters; it likely refers only to a federal criminal probe of Huang personally (View).
- Scenario probabilities are subjective; EPS figures are run rates (latest quarter × 4), not trailing twelve months.
- The Q3 FY27 earnings-call transcript was not re-read for this update (step 3 skipped). SEC EDGAR was not read directly.
- Index-fund NVDA weight is an estimate.

*Educational research, not investment advice.*

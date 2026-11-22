# eToro Group (ETOR) pre-buy research: cheap on the numbers, but a cyclical trading business, so only a small position fits

> Research date 2026-11-22 · Price date 2026-11-20 close · Price **$18.56** · Market cap **$1.48B** basic (verified: $18.56 × 79.53M shares = $1.476B; Investing.com shows $1.48B, 0.3% off) or **$1.71B** on 91.94M diluted shares · All figures USD · eToro reports under IFRS
> Method: the [pre-buy routine](../../docs/guides/pre-buy-routine.md) steps 1–5, valuation per `skills/company-valuation.md`. Model script: [`valuation-20261122/model.py`](valuation-20261122/model.py). Terminal-value gate (`tools/terminal_value.py audit`) **passed** (exit 0), with one warning written up under Limits.
> **Labels:** **Fact** = reported figure with a source. **Estimate** = arithmetic on reported figures. **Assumption** = a scenario input, i.e. a guess. **View** = interpretation, not data.
>
> *Educational research, not investment advice.*

---

## Bottom line

| | |
|---|---|
| **Verdict** | **Buy candidate, but only as a small, speculative position (1–3%), bought in steps.** Price is below the buy-below line, but the business is far more cyclical than LPL, so the cushion is doing a lot of work. Not a core long-term holding. |
| Fair value (probability-weighted, assumption-driven) | **~$30** per share (bear ~$20, soft ~$21, base ~$33, bull ~$50) |
| **Buy below** | **~$22** (≈27% under $30). Deep-cushion zone: **~$20** and lower (at or below the bear-case value). |
| Today vs fair value | $18.56 is ~38% below the weighted value and ~8% below the bear case. |
| What today's price needs | Using the model's normal-year earnings ($2.10/share), the price assumes earnings **shrink ~16% a year for 10 years**. Even starting from a depressed $1.40, it assumes ~4% yearly decline. |
| Why it is cheap | Trading activity is falling fast: Q3 net contribution –13%, adjusted EBITDA –56%, and October was worse (trades –22%, crypto trades –62%, interest-earning assets –20%). In 2021–2022 the same kind of cooldown cut revenue roughly in half. |
| Biggest risks | A repeat of the 2022 bust, revenue per customer falling (–26% y/y), rate cuts (~24% of net contribution is interest), CFD and crypto regulation in Europe/UK, and an acquisition spree using the cash pile. |

**One-paragraph version (View):** eToro trades at about 8x trailing GAAP earnings, has no debt and about $1.2B of cash and short-term investments (roughly 80% of its market cap, though not all of it is spare). On any normal year the stock looks cheap. The market is betting that 2025 was a peak year, like 2021 was. Funded accounts are still growing (+18%), but each account is producing much less revenue. If you accept that this is a cyclical business and size it small, the price is attractive. If you want a steady compounder like the LPL thesis, this is not it.

---

## Step 1. Verify the numbers

SEC EDGAR was not reachable from this environment. eToro is a foreign private issuer (incorporated in the British Virgin Islands, run from Israel), so it files quarterly results as 6-K press releases rather than 10-Qs. Figures come from the company's own releases as republished by StockTitan, Finviz, GlobeNewswire and FinancialContent. Where quarterly figures were added up, they matched the reported nine-month totals exactly.

> **Term — net contribution.** eToro books the full value of crypto it sells to customers as "revenue" ($13.0B in 2025), which hugely overstates its size. Its own key measure, **net contribution**, is total revenue minus the cost of the crypto sold and margin interest. Think of it as the true revenue line. All margins below use it.

### 1a. Recent quarters (Fact)

| Quarter | Net contribution | y/y | GAAP net income | GAAP diluted EPS | Adjusted diluted EPS | Adjusted EBITDA | Funded accounts | Buybacks |
|---|---|---|---|---|---|---|---|---|
| Q4 2025 | $226.8M | –10% | $68.7M | $0.69 | $0.71 | $86.9M | 3.81M | $59.5M |
| Q1 2026 | $258M | +19% | $82.4M | $0.86 | $0.91 | $108.5M | 4.02M | $101.1M |
| Q2 2026 | $229M | +9% | $53.5M | $0.58 | $0.68 | $78.1M | 4.28M | $88.0M |
| Q3 2026 | $186.3M | –13% | $15.0M | $0.14 | $0.26 | $34.2M | 4.39M | $0 |
| **Trailing 12 months** | **$900.6M** | | **$219.7M** | **$2.28** | **$2.56** | **$307.7M** | | **$248.6M** |

Sources: [Q3 2026 (StockTitan)](https://www.stocktitan.net/news/ETOR/etoro-reports-third-quarter-2026-crapzwbp7px9.html), [Q2 2026 (FinancialContent)](https://www.financialcontent.com/article/gnwcq-2026-8-11-etoro-reports-second-quarter-2026-results), [Q1 2026 (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/05/12/3292651/0/en/eToro-Reports-First-Quarter-2026-Results.html), [FY2025 (Finviz)](https://finviz.com/news/312382/etoro-reports-fourth-quarter-and-full-year-2025-results). Net contribution for Q4 2025 and Q3 2026 is my arithmetic from the income statement using the company's definition; it matches the headline figures ($227M, $186M). Investing.com shows net income of $219.66M TTM, matching my $219.7M sum.

**Q3 2026 in one line:** capital-markets (stocks, commodities, currencies) contribution +21%, crypto –53%, net interest income –19% (interest-earning assets –11%), eToro Money –5%. Q1's strength came mainly from commodities trading (about 60% of trading commissions that quarter).

### 1b. Longer history (Fact, mixed definitions)

| Year | Net contribution / commissions | Net income | Funded accounts | Source |
|---|---|---|---|---|
| 2021 | "~$1.2B" (approximate, labeled "revenues") | not given | ~2.4M (derived) | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/eToro-eyes-ipo-as-2023-revenues-stabilize-at-630-million/) |
| 2022 | $631M ("total commissions") | **–$21M loss** | 2.8M | [eToro FY22 release](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-reports-continued-growth-with-fy22-results/), [Finance Magnates](https://www.financemagnates.com/fintech/etoros-2024-profits-soared-13x-with-crypto-contributing-96-of-revenue/) |
| 2023 | $630–639M | $15.3M | ~3.0M | same |
| 2024 | $788M (net contribution) | $192.4M | 3.48M | FY2025 release |
| 2025 | $868M (net contribution) | $215.7M | 3.81M | FY2025 release |
| TTM Sep 2026 | $901M | $219.7M | 4.39M | quarterly releases |

**Read this carefully (View):** pre-2024 figures used older labels ("commissions", "revenues"), so they are not exactly comparable with net contribution; the IPO prospectus showed 2024 "total commission" as $931M, higher than the $788M net contribution. The direction is still clear: **revenue roughly halved from 2021 to 2022 and the company lost money**, then took two years to recover. That pattern is the core of the bear case.

### 1c. Full year 2025 (Fact, FY2025 release)

| | 2025 | 2024 | Change |
|---|---|---|---|
| Net contribution | $868.4M | $787.7M | +10% |
| GAAP net income | $215.7M | $192.4M | +12% |
| GAAP diluted EPS | $2.27 | $2.26 | flat (IPO added shares) |
| Adjusted diluted EPS | $2.64 | $2.67 | –1% |
| Adjusted EBITDA | $317.0M (36.5% of net contribution) | $303.9M (38.6%) | +4% |
| Operating cash flow | $318.2M | $268.6M | +18% |
| Capex (equipment + intangibles) | $5.5M | $2.9M | tiny |
| Stock-based comp | $16.2M | $27.2M | |

**2025 net contribution mix (Estimate, derived from income-statement lines):** stocks/commodities/currencies $399M (46%), interest $206M (24%), crypto $167M (19%), currency conversion and other $96M (11%).

### 1d. Balance sheet and capital (Fact, Sep 30, 2026)

| Item | Value |
|---|---|
| Cash + short-term investments | **$1,223M** ($881M cash, $342M short-term investments) |
| Borrowings | **None.** Only lease liabilities ($33M). |
| Total equity | $1,384M (book value ~$17.40/share per Investing.com; price/book ~1.1x) |
| Treasury shares bought | $189M in H1 2026 + $60M in Q4 2025; none in Q3 |
| New buyback authorization | **$250M** (Nov 10, 2026), no timetable |
| Shares outstanding | 79.53M (Investing.com, single source). Q3 weighted basic was 81.37M; ChartRow shows 82.9M as of Dec 2025, before buybacks. |
| Diluted shares (Q3 weighted) | **91.94M**, 13% above basic, from employee options and RSUs. This report values per diluted share. |
| Assets under administration | $20.8B (flat y/y); $19.2B in October (–6%) |
| Pending acquisition | TradeZero (US broker), **up to $231M** in cash plus up to 2.5M new shares; ~$80M revenue in the year to June 2026; close expected H1 2027 ([Banking Dive](https://www.bankingdive.com/news/etoro-acquire-tradezero-231-million/827712/)) |

**How much cash is truly spare? (Assumption):** brokers must keep regulatory capital in their licensed subsidiaries, and eToro has not been read on the exact requirement (the annual report was not reachable). This report assumes **$400M** is tied up and **$180M** goes to TradeZero (the $231M price less ~$50M paid in shares), leaving **~$640M, or ~$7.00 per diluted share**, as excess cash. Without that cash, the operating business is priced at ~$11.56 per share. If the required capital is higher, the value falls roughly dollar for dollar.

### 1e. Valuation snapshot (Estimate)

| Measure | Value | Note |
|---|---|---|
| P/E on TTM GAAP diluted EPS ($2.28) | **8.1x** | |
| P/E ex excess cash | ~5.1x | $11.56 / $2.28 |
| P/E on Q3 annualized adjusted EPS ($1.04) | ~17.8x | The depressed current run-rate |
| Free cash flow TTM (operating cash flow – capex) | ~$284M (~$3.09/diluted share) | Q4 2025 $125.7M + 9M 2026 $164.7M, less $6.2M capex. Operating cash flow at a broker can move with customer balances, so treat as approximate. |
| Price vs IPO ($52, May 2025) | **–64%** | [CNBC via NBC](https://www.nbcnewyork.com/news/business/money-report/stock-and-crypto-trading-site-etoro-prices-ipo-at-52-per-share-ahead-of-nasdaq-debut/6263181/) |
| 52-week range | $18.48–$44.21 (Investing.com); ChartRow low $19.46 a day earlier | Price is at the 52-week low |
| Analyst targets (opinions) | Average $36.20 (15 analysts, Investing.com); recent cuts: Goldman $29→$25, KBW $27→$22, UBS $35→$26, Cantor $48→$37 | [Stocktwits](https://stocktwits.com/news-articles/markets/equity/cathie-wood-sees-opportunity-in-e-toro-as-crypto-trading-cools-and-wall-street-cuts-price-target/cNGD1gTR9B2), [Investing.com](https://www.investing.com/equities/etoro-group-ltd) |

---

## Step 2. How eToro makes money (plain English)

**Two-sentence version:** eToro is a global app where ~4.4 million funded customers (mostly in Europe and the UK) trade stocks, crypto, commodities and currencies, and copy other investors' portfolios. It earns spreads and fees on each trade, interest on customers' cash and margin loans, and currency-conversion fees, so **profit rises and falls with how much retail investors are trading**, especially in crypto and leveraged products.

| Revenue engine (share of 2025 net contribution) | How it works | Sensitive to |
|---|---|---|
| **Stocks, commodities, currencies (46%)** | Spreads, overnight fees and trading income, much of it on **CFDs** (leveraged contracts where eToro is the counterparty) outside the US | Trading volume and volatility; CFD regulation |
| **Interest (24%)** | Interest earned on customer cash and margin lending, minus what it pays customers | **Interest rates** and customer balances (interest-earning assets $7.0B in October, –20% y/y) |
| **Crypto (19%)** | Spread on crypto bought and sold; small staking income | Crypto prices and enthusiasm; very volatile (–53% y/y in Q3) |
| **eToro Money, conversion, subscriptions (11%)** | FX fees on deposits/withdrawals, debit card, Club subscriptions | Deposits and transfers (–21% in October) |

> **Term — CFD (contract for difference).** A bet on a price move without owning the asset, usually with leverage. Most retail CFD accounts lose money, which is why EU and UK regulators cap leverage and force risk warnings. eToro earns from the spread and overnight financing, and as the counterparty it can also gain or lose on customer positions.

**What could make it a good business (View):** a social-investing network (CopyTrader, ~6,000 "Popular Investors", $2.4B in copy-trading assets) that rivals find hard to copy; licenses in many countries; an app that now has 24/5 trading and AI-agent connectors; no debt and a lot of cash. **But on the other hand:** revenue per customer is shrinking fast, marketing has to stay high (~25% of net contribution) to keep growing accounts, and competitors like Robinhood, Revolut, Trading 212 and Interactive Brokers offer similar products, often at zero commission.

**The single most useful number (Estimate):** net contribution per funded account fell from **$57.5 a quarter (Q3 2025) to $42.4 (Q3 2026), –26%**. Customer growth (+18%) is not making up for lower activity per customer.

---

## Step 3. Latest earnings call (Q3 2026, Nov 10, 2026)

Speakers: Yoni Assia (co-founder and CEO), Meron Shani (CFO). Source: [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/10/etoro-etor-q3-2026-earnings-call-transcript/) (some audio gaps).

**What management is proud of (Fact)**
- Record funded accounts (4.39M, +18%) and record equity assets ($11.5B, +24%).
- New AI-built app rolled out; API/agent usage +250% quarter on quarter; connectors for Claude, ChatGPT and Grok.
- About a quarter of daily volume now happens outside normal market hours.
- Retail distribution roles in the SpaceX IPO and the upcoming Anthropic IPO.
- $250M buyback. Assia: "We believe our shares are undervalued."

**What they are worried about (Fact)**
- Lower activity. Assia: "Periods of elevated activity and volatility are typically followed by cooling off as we saw in 2018 and 2022." Shani: crypto volatility "is to be expected."
- October was not better: average amount per stock trade $184 (–49% y/y), per crypto trade $228 (–29%).
- Marketing is getting pricier: Google search "cost per clicks... actually becoming higher." Sales and marketing rose to $68M (+42% y/y) with launch costs; management now targets **~25% of net contribution**, up from a 20–25% range.
- Q4 operating costs to fall "by 5% and plus" from Q3.

**Toughest analyst questions (Fact, paraphrased)**
- *Marketing did not fall as guided; how will you lift revenue per user?* (TD Cowen) → new products and AI-personalized ads. **View:** the guidance miss itself was not addressed.
- *What do expenses look like in 2027?* (Jefferies) → Q4 lower, AI cutting manual work. No 2027 number given.
- *Acquisition pace?* (Compass Point) → after four deals in 2026, "we are going to slow down a bit."
- *US ambitions and KPIs?* (Rothschild) → no US-specific KPIs published yet; profitable regions fund the US push. CopyTrader in the US is still limited to Club members.
- **Interest-rate sensitivity was not discussed** on the call, even though interest is about a quarter of net contribution.

---

## Step 4. Bear case: what would make this a bad investment

| # | Risk | Mechanism | How likely / how bad (View) | Watch this number |
|---|---|---|---|---|
| 1 | **A 2022-style bust** | Retail trading and crypto activity collapse together; revenue fell ~half from 2021 to 2022 and the company lost money | Already partly underway (Q3 –13%, October worse). Costs are mostly fixed (~$580–600M a year), so a fall in net contribution to ~$650M would leave close to zero profit. | Quarterly net contribution (alarm below ~$170M); trades per month |
| 2 | **Shrinking revenue per customer** | Growth comes from new accounts that trade less, or from cheaper products | Visible now: –26% y/y | Net contribution per funded account (want it stabilizing above ~$45/quarter) |
| 3 | **Rate cuts** | ~24% of net contribution is interest on customer cash and margin loans | The Fed raised rates in September 2026, so not imminent; balances are already falling (–20%) | Net interest income; interest-earning assets |
| 4 | **CFD and crypto regulation** | EU/UK rules on leveraged CFDs and crypto (MiCA) could limit products or margins in eToro's core markets | Tail risk, **not modeled** (see Limits) | Any regulator action on CFD leverage, marketing, or crypto for retail |
| 5 | **Cash spent on deals; option dilution** | Four acquisitions in 2026, TradeZero up to $231M; diluted shares 13% above basic | Medium. TradeZero brings ~$80M revenue at a price ~2.9x sales; profit not disclosed | Cash + short-term investments (alarm below ~$800M without a payoff); diluted share count |

**Steelman of the bear case (View):** 2024–2025 were boom years for retail trading, crypto and commodities, and eToro's profits are a leveraged bet on that activity. Its accounts grow but each one is worth less, marketing costs are climbing, and its biggest product (CFDs) lives at the regulators' pleasure. If activity reverts to 2022–2023 levels, earnings could fall 75% or more for a couple of years, and the cash pile could be spent on acquisitions at full prices. The stock's 64% fall since the IPO is the market pricing exactly this.

**Bull rebuttal (View):** even in that bust eToro roughly broke even, and it now has 50% more funded accounts than in 2022, no debt, ~$1.2B of cash, and a buyback that can retire ~15% of shares at today's price. Equity assets hit a record in Q3, so the core stock business is growing; crypto is the swing factor. On the model below, **even the bust scenario is worth slightly more than today's price**.

> Munger: "Invert, always invert." The question is not "how much could this go up?" but "what if 2025 was the peak?" Answered below: about $20 a share, if the business recovers in four years and the spare cash is really spare.

---

## Step 5. Fair value and "buy below" price

All arithmetic runs in [`model.py`](valuation-20261122/model.py) (Decimal). `tools/financial_rigor.py verify-market-cap` passed (0.27% deviation).

### 5a. Inputs (Assumptions, labeled)

| Input | Value | Basis |
|---|---|---|
| Normal-year owner earnings | **$2.10** per diluted share | Mid-cycle net contribution ~$850M (between 2024's $788M, 2025's $868M and the Q3 run-rate ~$745M) − ~$605M costs including stock comp − 15% tax ≈ $197M ÷ 91.94M. Close to 2025 GAAP EPS ($2.27) and TTM ($2.28). |
| Discount rate r | **11%** | ~4.3–4.7% Treasury + equity premium with beta ~1.2 (retail trading and crypto are pro-cyclical). Higher than LPL's 10%. |
| Return on growth investment | 25% | Organic growth is mostly expensed marketing; acquisitions earn less. Reinvestment = growth ÷ 25%. |
| Excess cash | **$7.00/share** | $1,223M − $400M regulatory/working cash − $180M TradeZero cash (both assumptions) |
| Shares | 91.94M diluted | Buybacks treated as a way of paying out cash, not extra growth |
| Debt | None | |

### 5b. Four scenarios (10-year DCF, plus excess cash)

| Scenario | Owner earnings path | Terminal growth / P/E | Value per share | vs $18.56 | Probability (Assumption) |
|---|---|---|---|---|---|
| **Bear (2022-style bust)** | $0.50 → $0.80 → $1.20 → $1.45 over 4 years, then 3% | 2% / 10.2x | **$20.20** | +9% | 25% |
| **Soft** (stuck at Q3 run-rate) | $1.40, flat 3 yrs, then 3% | 2% / 10.2x | **$21.47** | +16% | 25% |
| **Base** | $2.10, +6% yrs 1–5, +4% yrs 6–10 | 3% / 11.0x | **$33.39** | +80% | 35% |
| **Bull** (TradeZero + US growth) | $2.60, +12% yrs 1–5, +7% yrs 6–10 | 3.5% / 11.5x | **$49.59** | +167% | 15% |
| **Probability-weighted** | | | **~$29.55 → ~$30** | +59% | |

Terminal value is 44–63% of operating value in each case. Exit multiples of 10–11.5x are below the market's typical multiple, so the model does not assume a re-rating.

**Reverse DCF (Estimate):** at $18.56, starting from $2.10 normal earnings, the market is pricing **~16% yearly decline** for a decade. Starting from a depressed $1.40, it prices ~4% yearly decline. **View:** either the market expects the bust to be deep and long, doubts the cash is spare, or both.

**Sensitivity (base case, value per share):**

| | g = 2% | g = 3% | g = 4% |
|---|---|---|---|
| r = 10% | $35.83 | $37.43 | $39.56 |
| r = 11% | $32.30 | **$33.39** | $34.78 |
| r = 12% | $29.51 | $30.26 | $31.20 |

The value is far more sensitive to **normal-year earnings** than to the discount rate: base value is $24.59 at $1.40 starting earnings, $29.62 at $1.80, $33.39 at $2.10, $37.16 at $2.40.

### 5c. Price levels

| Price | What it implies | View |
|---|---|---|
| **Below ~$20** | You are paying less than the bust scenario | Deep cushion — **today ($18.56) is here** |
| $20–$22 | Bear-to-soft range; ~27–33% under weighted value | Buy zone per the routine's 20–30% cushion |
| $22–$30 | Needs some mix of base and bull | Fair range |
| Above ~$30 | Needs the base case or better | Expectations priced in |

**Strongest argument against buying now (View):** the trend is still down. October KPIs were worse than Q3, management gave no revenue guidance, and analysts are still cutting targets. A cyclical stock at a 52-week low with deteriorating monthly numbers can keep falling for several quarters; the value case only works if you can hold through that. Buying in steps around the next two results is the practical answer.

**Three numbers that would prove this valuation wrong:**
1. Quarterly net contribution below ~$160M (an annual pace under $650M, the 2022–23 level): the bear case becomes the base.
2. Regulatory capital or acquisitions absorbing the cash, so cash + short-term investments falls below ~$800M without a matching earnings gain: the $7/share cash cushion shrinks.
3. Net contribution per funded account still falling >15% y/y by mid-2027: customer growth is not translating into revenue.

---

## What to do next (steps 6–8 of the routine)

1. **Size: 1–3% of non-retirement money at most to start, cap at 5%.** That is smaller than the routine's usual 2–5% because earnings can swing from ~$2 to near zero in a bad year.
2. **Buy in three steps:** one third near today's price (it is already under the bust-case value), one third after **Q4 2026 results (date not announced; last year's came Feb 17, so expect mid-February 2027)**, and one third after the TradeZero close or Q1 2027 results, if the thesis holds.
3. **Sell rules (write them down before buying):** sell if (a) net contribution per funded account keeps falling more than 15% y/y for four quarters, (b) eToro posts a full-year GAAP loss outside an obvious market-wide bust, (c) cash + short-term investments falls below ~$800M through deals without a clear earnings payoff, or (d) a major regulator (FCA, CySEC, ESMA) bans or sharply restricts retail CFDs or crypto. A falling share price alone is not a sell signal.
4. **Next checkpoint:** Q4 2026 results (~mid-February 2027). Check net contribution (want ≥$180M), January KPIs (trades and invested amount per trade), cash after buybacks, and whether marketing actually fell as promised.
5. **Read the annual report yourself** (Form 20-F on [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001493318)): regulatory capital requirements, interest-rate sensitivity, how much CFD trading income comes from eToro's own position against customers, and risk factors. These were the gaps this report could not close.
6. **Overlap with your retirement funds:** eToro is a ~$1.5B small cap, not in the S&P 500, so total-market and target-date funds hold only a sliver. It adds a genuinely different exposure (retail trading and crypto activity) rather than more of what you already own. That is diversification and concentration at the same time: it is a bet on a cycle.

> Buffett: "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price." eToro is closer to the second: a decent, debt-free company at a price that assumes the worst. That can work, but it argues for a small position and patience, not a core holding.

---

## Limits (what this report could not check)

- **CFD regulation is not modeled** (flagged by the terminal-value gate). A ban or harsh restriction in the EU or UK would hit the largest revenue line; no scenario captures it.
- **Regulatory capital requirement unknown.** The $400M "tied-up cash" figure is an assumption. If the true figure is $800M, value falls by about $4.35 a share.
- **No segment table.** Releases describe five net-contribution components but publish no numbers; the mix above is derived from income-statement lines and ignores staking reallocations.
- **Pre-2024 history uses older labels** (commissions/revenues) and comes from press coverage, not filings.
- **Shares outstanding is single-sourced** (79.53M, Investing.com); company figures are weighted averages. Valuation uses diluted weighted shares (91.94M) to be conservative.
- **Probabilities and normal-year earnings are judgment calls.** Change them in `model.py` and rerun.

## Sources and data reliability

| Data | Source | Reliability |
|---|---|---|
| Q3 2026 results | [StockTitan (company release)](https://www.stocktitan.net/news/ETOR/etoro-reports-third-quarter-2026-crapzwbp7px9.html) | High |
| Q1, Q2 2026 | [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/12/3292651/0/en/eToro-Reports-First-Quarter-2026-Results.html), [FinancialContent](https://www.financialcontent.com/article/gnwcq-2026-8-11-etoro-reports-second-quarter-2026-results) | High; quarterly sums reconcile to nine-month totals |
| FY2025 | [Finviz (company release)](https://finviz.com/news/312382/etoro-reports-fourth-quarter-and-full-year-2025-results) | High |
| 2021–2024 history | [FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/eToro-eyes-ipo-as-2023-revenues-stabilize-at-630-million/), [eToro FY22 release](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/etoro-reports-continued-growth-with-fy22-results/), [Finance Magnates](https://www.financemagnates.com/fintech/etoros-2024-profits-soared-13x-with-crypto-contributing-96-of-revenue/) | Medium; definitions differ |
| Earnings call | [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/10/etoro-etor-q3-2026-earnings-call-transcript/) | Medium-high; audio gaps |
| TradeZero deal | [Banking Dive](https://www.bankingdive.com/news/etoro-acquire-tradezero-231-million/827712/) | High |
| Price, market cap, targets | [Investing.com](https://www.investing.com/equities/etoro-group-ltd) (Nov 20 close), [ChartRow](https://chartrow.com/quote/etor), [Eulerpool](https://eulerpool.com/stock/eToro-Group-Stock-VGG320891077) (both Nov 19), [Stocktwits](https://stocktwits.com/news-articles/markets/equity/cathie-wood-sees-opportunity-in-e-toro-as-crypto-trading-cools-and-wall-street-cuts-price-target/cNGD1gTR9B2) | Medium; share counts differ across sites (79.5M–95.1M, the high end is the 2025 diluted average) |
| IPO price | [CNBC via NBC New York](https://www.nbcnewyork.com/news/business/money-report/stock-and-crypto-trading-site-etoro-prices-ipo-at-52-per-share-ahead-of-nasdaq-debut/6263181/) | High |

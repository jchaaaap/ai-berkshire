# Company Valuation: Intrinsic Value and Valuation Review

Run a reproducible intrinsic-value estimate and valuation review for $ARGUMENTS.

**Input formats**: `company name`, `company name + ticker`, or an existing report path to review. Examples: `Tencent`, `Mastercard MA`, `review reports/腾讯/腾讯-research-20261027.md`

**Language**: write the report in English.

> "Price is what you pay; value is what you get." — Warren Buffett
>
> "It is better to be approximately right than precisely wrong." — Warren Buffett (attributed)
>
> "Invert, always invert." — Charlie Munger

## Design principles

Valuation mistakes rarely come from arithmetic. They come from three places: counting cash that does not belong to shareholders; charging the same risk twice (raising the discount rate *and* cutting the cash flows); and hiding a stack of subjective assumptions behind a number precise to the decimal point.

How the methods divide the work:
- **Discounted cash flow (DCF)** answers "what is it worth under my assumptions?"
- **Reverse valuation** answers "what does today's price require?" This matters more than the forward DCF, because it does not depend on how optimistic the analyst is.
- **Sum-of-the-parts (SOTP)** is only for businesses and assets that genuinely separate. It is not a way to pad the number.
- **Sensitivity and scenarios** show how wide a range the conclusion survives.

Every number must be reproducible: each input has a source, each arithmetic step runs through a tool, and the model script is saved next to the report.

## Workflow

### Step 0: Confirm the date and the units

1. Run `date` to confirm today's date. The report header states the **research date** and the **price date** (closing-price date).
2. Identify the **cash-flow currency**, the **reporting currency**, and the **share-price currency**. When they differ (e.g. Tencent: RMB financials, HKD share price), state the exchange rate used, its date, and its source.
3. Pick the share count: shares outstanding, float, or economic shares (net of treasury stock, plus dilution from unexercised options, RSUs, and convertibles). Say which one and why.

### Step 1: Gather inputs (cross-check with at least two sources)

Use the Task tool to fetch these **in parallel**:

| Category | What | Preferred source |
|---|---|---|
| Market | Share price, shares outstanding, market cap | Exchange / company filings + a quote site |
| Financials | 5 years of revenue, operating income, net income, operating cash flow, capex, stock-based comp (SBC), lease payments | 10-K / 20-F / annual report, 10-Q |
| Balance sheet | Cash, short-term investments, debt, lease liabilities, minority interest, investment holdings | Latest balance sheet and notes |
| Shareholder returns | Dividends, buybacks, share-count change | Annual report, buyback announcements |
| Rates | 10-year government bond yield in the cash-flow currency | Treasury / central bank |

Verify market cap with the tool, never by mental math:

```bash
python3 tools/financial_rigor.py verify-market-cap --price {price} --shares {shares} --reported {reported_mcap} --currency {currency}
python3 tools/financial_rigor.py cross-validate --field {field} --values '{"Source A": x, "Source B": y}' --unit {unit}
```

Do not use any figure whose sources differ by more than 2% until the gap is explained (period, currency, minority interest included or not, GAAP vs non-GAAP).

### Step 2: Cash-flow basis — how much actually reaches shareholders

Start from **operating income**, not adjusted net income:

```
Shareholder free cash flow ≈ operating income × (1 − cash tax rate)
                             − net reinvestment (capex − D&A + change in working capital)
                             − economic cost of SBC − minority share
```

Decide each item and state why:
- **SBC**: always a real cost. Either subtract the SBC that non-GAAP figures add back, or reflect it as dilution in the share count. Pick one; never count it in neither.
- **Leases**: if operating cash flow adds back lease principal, subtract rent as an operating cost.
- **Prepayments / deferred revenue**: a one-time working-capital inflow must not be extrapolated into a perpetual cash flow.
- **Investment holdings**: listed stakes at market value with a discount (liquidity, tax, control); unlisted stakes at the last round with a further discount. State the discount rates. If an investee's profit is already in earnings through the equity method, do not add the holding's value on top.
- **Maintenance vs growth capex**: if they can't be split, say "cannot be split" and subtract the total.

Counter-check: compare cumulative 5-year shareholder free cash flow with cumulative 5-year net income. If the first is clearly lower, explain where the difference went.

### Step 3: Discounted cash flow (DCF)

**Structure**: an explicit period (usually 10 years) plus a terminal value. The bear, base, and bull cases change the **operating path** (revenue, margins, reinvestment), not just the exit multiple.

**Discount rate r**: in the same currency as the cash flows. Reference ranges (matching the guardrails built into `terminal_value.py`):
- RMB: 6%–9%
- USD / HKD: 9%–11.5%

Show the derivation: risk-free rate + equity risk premium × risk exposure (beta). Justify any beta that departs from 1.0. **Discrete risks** (delisting, VIE failure, sanctions, a regulatory blow, technological displacement) go into scenarios or a tail case only, never into r.

**Terminal value**: use only the perpetual-growth model, not peer-multiple analogies:

```
Terminal P/E = (1 − g/ROIC) / (r − g)
```

- g: at most 2% for RMB, 4% for USD. g does not move with r.
- ROIC: steady-state incremental return, between the current ROIC and the value implied by the payout ratio.
- r − g must be at least 5 percentage points in every case. Below that, the model mostly amplifies assumptions instead of valuing anything.

Pass the gate check before publishing any number:

```bash
python3 tools/terminal_value.py audit --currency {currency} --r {r} --roic {ROIC} --g {bear},{base},{bull} --rf {risk_free} \
  --beta 1.0 --discrete-risks "{risk}:{情景|尾部档|概率|未建模},..."
python3 tools/terminal_value.py pe --roic {ROIC} --g {g} --r {r}
```

(The `--discrete-risks` placement labels are the tool's fixed values: 情景 = scenario, 尾部档 = tail case, 概率 = probability, 未建模 = not modeled.)

**Model script**: write the year-by-year explicit-period cash flows as `model.py` using Python's standard-library `decimal.Decimal`, saved in the same folder as the report, with inputs at the top of the script or in `model_inputs.json`. Independently recheck the key intermediate results (year 1, 3 and 10 cash flows; terminal value; terminal value's share of present value) with the tool:

```bash
python3 tools/financial_rigor.py calc --expr '{yr3_revenue} * {margin} * (1 - {tax_rate}) - {net_reinvestment}'
```

The report must state the **terminal value's share of enterprise value**. Above 70%, say plainly that the conclusion mostly depends on assumptions about years beyond 10.

### Step 4: Equity bridge — from enterprise value to value per share

```
Value per share = (operating value + cash and short-term investments + investment holdings (after discount)
                   − debt − lease liabilities − minority interest − other debt-like obligations) / economic shares
```

Table every item with its source and period. Watch for:
- Overseas cash that is taxed or restricted when repatriated: discount it and say so.
- Cash the business needs to operate (payment-platform customer funds, insurance float) is not distributable.
- With convertibles, options, or RSUs outstanding, divide by economic shares, not shares outstanding.

### Step 5: Sum-of-the-parts (only when it applies)

Use it only when the segments are largely independent in capital, customers, and costs, and at least one has an observable market price. Otherwise skip it and write "not applicable".

Value each segment separately, then:
- Subtract the capitalized cost of headquarters (corporate overhead does not vanish when you split the company).
- For an unlisted segment valued at its funding round, separate the **post-money valuation** from the parent's **actually attributable equity**, and subtract liquidation preferences and the extra funding continuing losses will need.
- Compare the total with the whole-company DCF from Step 3. Explain any gap above 20%.

### Step 6: Reverse valuation — what today's price requires

Hold r and the terminal assumptions fixed, and solve for what the current market cap implies:
- the 10-year revenue CAGR, or
- the steady-state margin, or
- year-10 profit.

Then compute the 10-year return from buying today if the valuation returns to the terminal P/E:

```bash
python3 tools/terminal_value.py irr --profit {yr10_profit} --mcap {market_cap_today} --pe {exit_pe} --years 10 --payout {dividend_yield_minus_dilution}
```

Put the implied requirements in one table next to the company's track record and the industry's ceiling. Phrase the conclusion as "the market requires X; history shows Y", not with adjectives like "cheap" or "expensive".

### Step 7: Sensitivity and stress tests

1. **Nine-cell grid**: r (±1pp) × g (±1pp), or r × the key operating variable, showing value per share.
2. **Does the conclusion flip?**

```bash
python3 tools/terminal_value.py flip --name {company} --r {r} --delta 0.02 --currency {currency} --rf {risk_free} \
  --roic {ROIC} --g {bear},{base},{bull} --p {bear},{base},{bull} --irr10={bear},{base},{bull} --k {dividend_yield_minus_dilution}
```

3. **Three-scenario target price** (a cross-check on the DCF, not a replacement):

```bash
python3 tools/financial_rigor.py three-scenario --price {price} --eps {EPS} --shares {shares_in_100M} \
  --growth {bull} {base} {bear} --pe {bull} {base} {bear} --years 3 --currency {currency}
```

(`--shares` is in units of 100 million shares.)

4. List each stress test separately (lower cash conversion, lower attributable share, extra fundraising, a change in dividend policy). Do not stack them automatically.

### Step 8: Reviewing an existing report (when the input is a report path)

Check each item and mark ✅ / ⚠️ / ❌:

| Check | Common problem |
|---|---|
| Market cap = price × shares | Wrong share count, mixed currencies |
| Cash-flow starting point | Starts from adjusted net income; SBC added back |
| Cash attribution | Minority interest, restricted cash, or customer funds credited to shareholders |
| Risk counted twice | Raises r *and* cuts scenario cash flows |
| Currency of r and g | RMB g paired with a USD r |
| Width of r − g | Under 5pp |
| Terminal value share | Not disclosed, or above 70% without a warning |
| Investment holdings | Equity-method profit and holding value both counted |
| Arithmetic | Spot-check at least 5 figures with `financial_rigor.py calc` |

Sort the review's findings into three kinds: **arithmetic errors** (fix directly), **basis errors** (need a recompute), and **assumption disagreements** (list both sides' reasons; don't rule).

### Step 9: Conclusion and price watch levels

Give no buy or sell instruction. Give price ranges and the assumptions each one implies:

| Price range | Implied assumption | View |
|---|---|---|
| Below X | The bear case alone earns r | Wide margin of safety (opinion) |
| X – Y | Requires the base case to play out | Fair range (opinion) |
| Above Y | Requires the bull case to play out | Expectations largely priced in (opinion) |

Then write the strongest counter-argument and two or three observable tracking metrics: which number, if it shows up, proves the valuation assumptions wrong.

## Output format

Save to `reports/{company}/{company}-valuation-{YYYYMMDD}.md`. Put the model script and input files in a folder beside it (e.g. `reports/{company}/valuation-{YYYYMMDD}/model.py`).

```markdown
# {Company} ({ticker}) valuation: {one-line conclusion}

> Research date YYYY-MM-DD | Price date YYYY-MM-DD | Price {currency}{price} | Market cap {currency}{mcap} (verified) | Cash-flow currency {currency}

## 1. Summary
- Intrinsic value per share (base): {currency}{x}, range {bear}–{bull}
- Today's price implies: {one-line reverse-valuation result}
- 10-year return (base, at today's price): {x}%, r = {r}
- Terminal value share of present value: {x}%

## 2. Shareholder cash-flow basis
## 3. DCF: operating path, discount rate, terminal value
## 4. Equity bridge
## 5. Sum-of-the-parts (if applicable)
## 6. Reverse valuation
## 7. Sensitivity and stress tests
## 8. Strongest counter-argument
## 9. Price watch levels and tracking metrics
## Sources and data reliability
```

## Hard rules

1. All arithmetic runs through `tools/financial_rigor.py` or `tools/terminal_value.py`, or lives in the Decimal model script. No mental math.
2. If the report includes a terminal value or a 10-year IRR, rerun `terminal_value.py audit` with the final parameters before publishing. Publish only on exit code 0.
3. Label every assumption "assumption" or "estimate" and give its basis. Never treat company guidance or sell-side forecasts as fact.
4. Charge each risk once: either in the scenario cash flows or in the discount rate. Say which.
5. State the currency unit in every table header.
6. Follow the objectivity rules in `CLAUDE.md`: every core judgment comes with the counter-argument, and when data is insufficient, write "insufficient data".

> "If you can't value it, don't buy it." — paraphrasing Warren Buffett

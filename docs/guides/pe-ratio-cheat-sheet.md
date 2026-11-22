# P/E Ratio Cheat Sheet

**In one line:** P/E is how many dollars you pay today for each $1 of yearly profit the company earns.

> Example figures use prices at the Nov 20, 2026 close, taken from the [US shortlist checklist](../../reports/US-shortlist-checklist-20261122.md). They are approximate and go stale fast, so re-pull current numbers before using them.

---

## 1. The math

**P/E = share price ÷ earnings per share (EPS)**

| Example | Price | EPS | P/E |
|---|---|---|---|
| Booking (BKNG) | ~$147 | ~$10.47 (2026 estimate) | ~14x |

At 14x you are paying 14 years of today's profit, assuming profit never grows.

## 2. Flip it: earnings yield

**Earnings yield = 1 ÷ P/E.** It turns P/E into a rate you can compare with bonds.

| P/E | Earnings yield | Example |
|---|---|---|
| 14x | ~7.1% | Booking |
| 31x | ~3.2% | Mastercard (MA) |
| — | ~4% | 10-year US Treasury (approx.) |

A stock yielding less than a Treasury only makes sense if you expect its earnings to grow. The gap is your bet on growth.

## 3. The versions you will see

| Version | What it uses | Strength | Weakness |
|---|---|---|---|
| **Trailing (TTM)** | Last 12 months of actual earnings | Real numbers | Backward looking |
| **Forward** | Next year's analyst estimate | Forward looking | It is a guess |
| **GAAP** | Official accounting earnings | Standardized | Includes one-offs |
| **Adjusted** | Strips out one-offs | Shows core business | Usually flattering; management picks what to strip |

Always know which one you are reading before comparing two numbers.

## 4. Why P/E differs between companies

A higher P/E means the market expects faster or safer growth.

- **Mastercard (~31x):** near-duopoly payment network growing double digits.
- **Progressive (PGR, ~11x):** insurance profits swing with the underwriting cycle, so the market pays less for them.

## 5. How to use it properly

1. **Compare like with like.** Against the stock's own 10-year history, its direct peers, and the S&P 500 (roughly 21–23x forward).
2. **Pair it with growth (PEG).** PEG = P/E ÷ expected growth rate (in %).
   - 20x P/E with 20% growth → PEG 1.0
   - 12x P/E with 3% growth → PEG 4.0
   - The "expensive" 20x stock can be the cheaper one.
3. **Ask why it is cheap.** A low P/E often signals trouble. Booking is cheap on fears that AI agents will disintermediate online travel; Zoetis (ZTS) on shrinking sales. The job is deciding whether the market is overreacting.
4. **Watch the cyclical trap.** Insurers, banks, miners and other cyclicals look cheapest at peak profits, right before earnings fall. Progressive: ~11.6x trailing, but ~14x on next year's lower estimate (~$16 EPS for 2027).
5. **Check earnings quality.** Profit should turn into real cash. Compare net income with free cash flow over several years.

## 6. Where P/E breaks

| Situation | Problem | Use instead |
|---|---|---|
| Company loses money | No usable P/E | EV/Sales, path to profitability |
| Heavy buybacks or one-time gains | EPS distorted | Net income trend, FCF per share |
| Banks | Earnings driven by balance sheet | Price-to-book, ROE |
| REITs | Depreciation understates cash earnings | Price-to-FFO / AFFO |
| Cyclicals at peak | Low P/E is misleading | Normalized (mid-cycle) earnings |

## 7. Quick research routine

1. Pull **trailing and forward P/E**.
2. Compare with the **10-year average** and **peers**.
3. Check **expected growth** and compute PEG.
4. Compare earnings with **free cash flow**.
5. Write one sentence: *why the market prices it this way*, and one sentence: *why you disagree* (or don't).

For exact calculations (P/E, earnings yield, PEG), use [`tools/financial_rigor.py`](../../tools/financial_rigor.py) rather than mental math.

---

*Educational reference, not investment advice.*

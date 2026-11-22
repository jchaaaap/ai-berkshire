# Pre-Buy Routine: From "Interesting" to "Buy"

**In one line:** eight steps to run on any stock before you put money in, so you buy on evidence and a plan, not on a headline.

Companion to the [P/E Ratio Cheat Sheet](pe-ratio-cheat-sheet.md). Worked example: [LPL Financial pre-buy research](../../reports/LPL%20Financial/LPL%20Financial-research-20261122.md) (steps 1–5 done in full).

---

## The eight steps at a glance

| # | Step | Question it answers | Time | Stop here if… |
|---|---|---|---|---|
| 1 | Verify the numbers | Are the figures I'm relying on real? | 1–2 h | You can't confirm them |
| 2 | Understand how it makes money | Do I know what drives profit? | 30 min | You can't explain it in two sentences |
| 3 | Listen to the last earnings call | What is management worried about? | 1 h | — |
| 4 | Write the bear case | What would make this a bad investment? | 30 min | A risk could wipe out the thesis and you can't size it |
| 5 | Set your price | What is it worth, and what will I pay? | 1–2 h | Price is above your "buy below" |
| 6 | Size it | How much, at most? | 10 min | — |
| 7 | Write your sell rules first | What would make me sell? | 15 min | You can't name a thesis-breaker |
| 8 | Buy in steps | When, and in how many pieces? | — | — |

Steps 1–5 decide **whether**. Steps 6–8 decide **how much and how**.

---

## 1. Verify the numbers

Never trade on figures you haven't checked yourself. Screens, articles and AI summaries all get numbers wrong.

**Where to look**
- **10-K** (annual report) and **10-Q** (quarterly) on [SEC EDGAR](https://www.sec.gov/edgar/search/) or the company's investor relations site.
- **Earnings press release** for the latest quarter (faster to read than the 10-Q).

**What to confirm**

| Item | Where in the filing | Why |
|---|---|---|
| Revenue growth (3–5 years) | Income statement | Is the business growing? |
| Margins (operating, net) | Income statement | Is growth profitable? |
| Free cash flow = operating cash flow − capex | Cash flow statement | Profit you can actually spend |
| Debt and cash | Balance sheet | Can it survive a bad year? |
| Share count trend | Cover page / EPS note | Buybacks (good) or dilution (bad)? |

**Two rules**
- Cross-check key numbers in **two sources**. If they differ by more than ~2%, find out why (period, GAAP vs adjusted, currency).
- Check market cap by hand: **price × shares outstanding**. Use `python3 tools/financial_rigor.py verify-market-cap`.

> **Term — GAAP vs adjusted.** GAAP is the official accounting profit. "Adjusted" strips out items management calls one-offs. Adjusted is usually higher; ask whether the "one-offs" really are. See the [cheat sheet §3](pe-ratio-cheat-sheet.md#3-the-versions-you-will-see).

## 2. Understand how it makes money

Write two sentences: **who pays the company, and for what**, then **what makes profit rise or fall**. If you can't, stop. You won't know when to worry.

Then list each revenue line and ask of each one: is it recurring? What is it sensitive to (interest rates, the economy, one big customer)?

> Example (LPL): "LPL is the back office for ~32,600 independent advisors and takes a cut of their clients' fees. It also earns interest on clients' idle cash, which falls when the Fed cuts rates."

## 3. Listen to the last earnings call

Read the transcript (free on many sites) or listen to the replay. Note:
- **What management is proud of** (the headline numbers).
- **What they're worried about** (cost increases, guidance cuts, slowing growth).
- **What analysts push back on.** The hardest questions usually point at the real risk.
- **Non-answers.** "We'll share more next year" on an important question is information.

## 4. Write the bear case

List the **three to five things** that would make this a bad investment. For each, write the mechanism and **one number you can watch** that would tell you it's happening.

| Risk | Mechanism | Number to watch |
|---|---|---|
| e.g. Rate cuts | Lower interest on client cash | Fed funds rate; company's cash yield |

Then steelman it: write the bear case as if you were short the stock. If you can't argue against it, wait.

> Munger: "Invert, always invert."

## 5. Set your price

Estimate **fair value**, then a **"buy below" price** that leaves a **20–30% cushion** (margin of safety) for being wrong.

**Quick way (no model):**
1. Pick a fair P/E for the business (use the [cheat sheet §5](pe-ratio-cheat-sheet.md#5-how-to-use-it-properly): compare with its history, peers, and growth).
2. Fair value ≈ fair P/E × normal earnings per share.
3. Buy below = fair value × 0.7 to 0.8.

**Thorough way:** run the repo's `/company-valuation` skill (`skills/company-valuation.md`). It builds a 10-year DCF with bear/base/bull cases, a reverse DCF ("what growth does today's price require?"), and a sensitivity table, and saves a reproducible `model.py`.

| Result | What it means |
|---|---|
| Price below buy-below | Candidate. Go to step 6. |
| Price between buy-below and fair value | Fair price, thin cushion. Set an alert; buy only if you accept the risk. |
| Price above fair value | Wait. |

> Term — **reverse DCF**: instead of guessing growth, solve for the growth the current price assumes. If the market needs 3%/yr and the company has done 10%, you have a cushion; if it needs 15%, you don't.

## 6. Size it

- Start small: **~2–5% of your non-retirement money** for a first position.
- Add only if the thesis holds (results confirm it, not just the price).
- Keep any single stock **under ~10%** of that money.
- Check overlap: if your index funds already hold it heavily, buying more is a bigger bet than it looks.

## 7. Write your sell rules first

Before buying, write down what would make you sell. Sell on a **broken thesis**, not on a price drop.

Good sell rules are specific:
- "Organic growth below 3% for four quarters."
- "Debt above 3x EBITDA without a clear payoff."
- "Management changes the strategy I bought into."

Track them with the repo's `/thesis-tracker` skill, and revisit every earnings report.

## 8. Buy in steps

Split the purchase into **2–4 pieces** over a few weeks, or around earnings dates. This avoids betting everything on one day's price and gives you a chance to learn from the next report before committing fully.

---

## One-page checklist

```
[ ] 1. Revenue, margins, FCF, debt, share count confirmed in 10-K/10-Q (2 sources)
[ ] 1. Market cap hand-checked: price × shares
[ ] 2. Two-sentence business description written
[ ] 3. Earnings call read: top worry + toughest analyst question noted
[ ] 4. 3–5 bear-case risks, each with a number to watch
[ ] 5. Fair value: ______   Buy below: ______   Today: ______
[ ] 6. Position size: ____% (≤5% to start, ≤10% max)
[ ] 7. Sell rules written (thesis-breakers, not price)
[ ] 8. Purchase split into ___ steps; dates: __________
```

---

*Educational reference, not investment advice.*

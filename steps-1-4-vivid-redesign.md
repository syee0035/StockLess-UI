# Steps 1–4 "vivid" redesign — data rules (4 Oct 2026)

Files in `FIT5120/I2/Claude outputs/`: StockLess-Step1-Upload, -Step2-Mapping, -Step3-Readiness, -Step4-Purchases (previous versions kept as `*-before-vivid.html`). Impact Dashboard numbers updated to match Step 4. Generator scripts live on Serene's machine only (Cowork VM `~/sv/`), not in the project.

All four pages now read the real `stockless_sample_file.csv` (1,226 rows, 14 columns, 28 products). The old 7-product demo set is retired.

## Step 3 readiness rules (analysis date 15 Sep 2026)
- Rows left out (6): unreadable date (rows 1,197 `2026-13-45`, 1,198 `04/05/2026`), sale dated after 15 Sep (1,201), non-numeric quantity (1,202 `minus-three`), no product code (1,205), duplicate (1,208 — identical to 1,209; **latest row kept automatically**, no user decision).
- Tidy-ups applied: extra spaces (1,206 `  MM0031  `), letter case (1,210 `mm0031`).
- Missing data (7): no stock, non-numeric stock, negative stock, no count date, count > 28 days old.
- Review (9): count 8–28 days old, count date after analysis date, two stock values, one code for two pack sizes, same product under two codes (007 / 7), unreadable expiry, a single sale ≥ 100 units.
- Ready: 12. Categories come from product names (Beverages, Staples, Snacks, Fresh & dairy, Cooking & canned, Non-food). Product cards show last stock count, stock age and weekly sales bars (restored at Serene's request); "What we found" sits below the products; the underlying numbers stay in a fold.

## Step 4 rules
- Expected 4-week range = 4 × mean ± 2 × SD of the last 8 full weeks' sales. Needs ≥ 4 weeks of history and ≥ 3 active weeks, else "Need data". **This is a stand-in for the team's E3 forecast.**
- Suggested = midpoint − stock − incoming. Status: available (stock + incoming + planned) < low → Order needed; > high → Check order; else Balanced.
- Supplier, lead time and case size come from the file; minimum order is typed. Arithmetic follows E6 (lift to minimum, then whole cases).
- Result: 1 order needed, 2 check order (Milo 3in1 MM0002 +24, Sardin MM0005 +2), 8 balanced, 17 need data → 26 units possible excess.

## Step 4 layout (Claude Design, 4 Oct 2026)
- Design canvas: "StockLess Step 4 purchase plan" (claude.ai/artifact/QGr7CgLaiQ9pGnaMJxKLvF), desktop + phone boards.
- Purchase plan ≈ two-thirds width on the left, compact product list on the right.
- "Why this estimate? Demand and stock" is first: past 8 weeks as bars, then a shaded "Forecast · next 4 weeks" area with one column per coming week (range ÷ 4, line = most likely). The engine forecasts one range for the 4-week total, so the weekly columns are that range spread evenly — not week-by-week predictions.
- Then Suggested restock (with working and "Use suggested") beside Your order (− / +, slider, incoming), purchase check bar + verdict, folded Expiry and Supplier terms, "Done · next product".
- Phone: chart labels collapse to "Past 8 weeks · Next 4 weeks ≈x a week". Malay forecast label shortened to "Ramalan · 4 minggu".

## Shared shell (all steps)
- Mint title band holds the step's buttons (back, progress, continue) and is sticky; it shrinks to one slim row on scroll (title + main button on phones).
- Top bar: no Prototype link. Logo and Homepage open `StockLess-Homepage.html` (the former StockLess-Prototype.html; the older homepage file was renamed StockLess-Homepage-old.html). The homepage's start buttons open Step 1; Step 4 → Impact Dashboard.
- Fonts: Manrope 700 names/labels, Source Sans 3 400 descriptions, uppercase Manrope 800 marks, Inter numbers.

## React patches (team repo HansYap/StockLess)
- `i18n-natural-translations.patch` (natural ms/zh copy) then `design-steps-1-4.patch` (this design, incl. new translated keys and updated tests). Apply in that order; both apply cleanly on main. Not run through `npm test` here (npm registry blocked) — the team must run tests. Typecheck was checked against a local shim and only showed one error that already exists on main.

## Impact Dashboard
26 units across 2 products. The sample file has no Unit cost column, so business impact shows "Not yet available" (per impact-dashboard-methodology.md); emissions stays "Not yet available".

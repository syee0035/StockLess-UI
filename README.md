# StockLess UI

**StockLess** is a web-based decision-support system that helps Malaysian micro and small food retailers make smarter stock purchasing decisions and reduce avoidable food waste.

StockLess turns historical sales data into demand insights and purchase checks. It helps retailers move from manual or rule-of-thumb stock decisions towards more informed restocking.

> **Sales data → Demand insights → Smarter restocking → 🌱 Less waste**

---

## 🌱 About StockLess

Small food retailers often rely on spreadsheets, manual calculations or personal experience when deciding how much stock to buy.

StockLess offers a simpler workflow that helps retailers understand their sales data before they place their next order.

It focuses on four questions:

- What products are selling?
- Is the sales data ready to use?
- Which products need attention?
- How much should the retailer consider buying?

StockLess sits between **simple spreadsheets** and **complex ERP systems**: a focused workflow for understanding demand and making restocking decisions.

---

## ✨ Key Features

### 1. Upload Sales Data

Retailers upload the sales export they already have, from a POS, a marketplace or a spreadsheet.

#### Required data

- Sale date
- Product identification
- Quantity sold

#### Product identification

StockLess can tell products apart using either:

- **One code column:** SKU, barcode or product code
- **Product name + pack size**

Optional attributes (stock on hand, stock count date, planned orders, incoming stock, expiry dates, supplier details, unit cost) unlock more insights.

#### File limits

- `.csv`, `.xlsx` or `.xls`
- Up to **10 MiB**
- Up to **100,000 rows**
- CSV files can be comma, semicolon or tab separated
- Excel files use the first worksheet that contains data

A built-in **sample file** lets new users try the full workflow without their own data.

---

### 2. Flexible Column Matching

After upload, StockLess suggests which of the retailer's columns match each StockLess field, so existing exports can be used without restructuring them first.

The matching screen shows:

- **Required** fields (needed to continue) and **Optional** fields (each one adds to the results) in separate groups
- A preview of the values in each matched column
- How products will be identified (one code column, or name + pack size)
- Any identity conflicts, such as one code covering two pack sizes
- **What this file unlocks**, based on the columns matched so far
- An **"All matches look right? Confirm all and continue"** shortcut

Nothing is applied until the retailer confirms it, and the original file is never changed.

---

### 3. Data Readiness Check

StockLess checks the data before it is used for purchase planning.

The readiness screen includes:

- **Summary tiles:** products that are ready, need review, or are missing data
- **Products by category:** product cards grouped into tabs (Beverages, Staples, Snacks, Fresh & dairy, Cooking & canned, Non-food). Each card shows the last stock count, stock age, a mini weekly-sales chart and the main issue. Products that need attention are listed first.
- **What we found:** issues grouped by type (dates, quantities, missing product, stock counts and more), each with what was found and what to do
- **Ready for planning:** how many rows are used, plus a reminder that missing weeks are never counted as zero sales
- **Show the underlying numbers and charts:** row reconciliation, issue charts, a data-quality breakdown and the full problems and tidy-ups table

Exact duplicate rows are handled automatically (the latest row is kept), and safe tidy-ups such as trimming extra spaces are listed so nothing changes silently.

StockLess explains issues in plain language:

**What was found → Why it matters → What to do**

---

### 4. Purchase Planning

Once the data is ready, StockLess turns sales into a purchase check for the next four weeks.

The planning screen has two parts:

- **Purchase plan (wide, left):** one product at a time
  - **Why this estimate? Demand and stock** at the top: the past 8 weeks of sales as bars, and a shaded **Forecast · next 4 weeks** area showing the expected range per week, with a line for the most likely value
  - Four quick facts: stock now, weekly average, weeks of cover and stock count date
  - **Suggested restock**, with its working shown (middle of the forecast − stock on hand − incoming stock) and a one-click "Use suggested"
  - **Your order:** − / + buttons, a slider and an exact-number box, plus incoming stock
  - **Purchase check:** stock + incoming + order compared with the expected range, with a plain verdict
  - Folded **Expiry** and **Supplier terms** sections, then **Done · next product**
- **Product list (narrow, right):** every product with its expected range, stock, order and status, plus search

Products are grouped as:

- **Order needed**
- **Check your order**
- **Looks balanced**
- **Need more data**

These groups support the retailer's decision. StockLess never places an order automatically.

The forecast is a range for the four-week total, worked out from recent weekly sales. The weekly columns show that range spread evenly across the four weeks; they are not separate week-by-week predictions.

---

### 5. Impact Dashboard

The Impact Dashboard connects the purchase plan with food-waste reduction. It follows the project's impact methodology:

- **Units of potential overstock avoided** are always shown: stock after the planned order, minus the top of the expected four-week range
- **Cost saving (RM)** is shown only for products whose unit cost was mapped in Step 2; other products are left out rather than guessed
- **Emissions (CO₂e)** stay "Not yet available", because converting needs each unit's weight and sales files record units only

All figures are **estimates** from the retailer's own file, meant to support decisions rather than report verified outcomes.

---

## 🧭 StockLess Workflow

| Step | Purpose |
| --- | --- |
| 🌱 **01 Upload** | Upload a CSV or Excel sales file, or use the sample |
| 🌿 **02 Map columns** | Match file columns to StockLess fields |
| 🪴 **03 Check readiness** | Review data readiness and product-level issues |
| 🌳 **04 Plan purchases** | Check a planned order against the four-week forecast |
| ♻️ **Impact** | See the overstock and cost the plan avoids |

Each step has a **sticky header**: the step title and its navigation buttons (back, progress, continue) stay at the top while scrolling, shrinking to one slim row.

---

## 🔒 Privacy

> **Your data stays on your device.**

Files are processed directly in the browser. Sales rows and product identifiers are not uploaded to an AI or API service. StockLess may save column headings and confirmed matching rules in the browser so returning users don't have to match columns again; these can be deleted from the Upload screen. Order quantities typed in Step 4 last for the current visit only.

---

## 📊 Data Requirements

### Required Attributes

| Attribute | Description |
| --- | --- |
| **Sale date** | The date each sale or return was recorded |
| **Product identification** | SKU, barcode or product code, or product name + pack size |
| **Quantity sold** | Units sold, with returns as negative numbers |

### Optional Attributes

| Attribute | Unlocks |
| --- | --- |
| **Stock on hand** + **Stock count date** | Stock freshness, weeks of cover, purchase check |
| **Planned orders** | Purchase check |
| **Incoming stock** | Purchase check |
| **Expiry dates** | Expiry-aware note |
| **Supplier details** | Supplier terms (case size, minimum order, delivery time) |
| **Unit cost** | Cost of the plan and cost saving in ringgit |

---

## 🌐 Languages

The interface is available in **English**, **Bahasa Melayu** and **Simplified Chinese (中文)**. Translations are written to read naturally rather than word for word. Retailer product names are never translated.

---

## 🎨 User Interface

StockLess uses a sustainability-focused visual language that makes data-heavy steps easier to follow:

- Teal and soft green palette, with amber for "check" and red for "missing" states
- A mint title band on every step, holding the step's buttons and sticking to the top on scroll
- Rounded cards, clear status pills and lightweight charts
- Tooltips for unfamiliar terms and progressive disclosure (details fold away until needed)
- Responsive layouts

### Typography

- **Manrope 700** for headings, product and attribute names, labels and buttons
- **Source Sans 3 400** for descriptions, notes and helper text
- **Uppercase Manrope 800** for small marks such as "REQUIRED", "OPTIONAL" and step eyebrows
- **Inter** for numbers and data values

### Workspace background

The workspace uses a quieter version of the homepage style: soft green waves, leaf illustrations and dot patterns in the side gutters, with a clear central reading area. The artwork is reduced in opacity and hidden on smaller screens.

---

## 📱 Responsive Design

StockLess works on desktop, tablet and mobile web. On smaller screens:

- Multi-column layouts stack into single sections
- Tables become product cards
- The sticky header shrinks to the title and main button
- Chart labels simplify (for example "Past 8 weeks · Next 4 weeks ≈4.5 a week") so text never overlaps
- Horizontal scrolling is avoided and touch targets stay at least 44 px
- Decorative artwork is reduced or removed

---

## 🖥️ Application Screens

| Screen | What the user does |
| --- | --- |
| **Homepage** | Learns what StockLess does and starts with their sales data |
| **Step 1 — Upload** | Sees which columns are needed and uploads a file or the sample |
| **Step 2 — Map columns** | Confirms how their columns match StockLess fields |
| **Step 3 — Check readiness** | Reviews product cards by category, issues found and underlying evidence |
| **Step 4 — Plan purchases** | Reviews the forecast and checks their planned order for each product |
| **Impact Dashboard** | Sees the overstock and cost the plan avoids, and how it links to SDG 12.3 |

---

## 🌍 Sustainability Context

StockLess focuses on **UN Sustainable Development Goal 12.3**, which aims to halve food waste at the retail and consumer levels.

The project targets avoidable food waste caused by over-ordering and inventory decisions in small food retailers. By helping retailers order closer to what actually sells, StockLess explores how data-driven decision support can reduce food waste at the shop counter.

---

## 🎯 Target Users

**Malaysian micro and small food retailers**, including:

- Neighbourhood grocery stores
- Minimarts
- Small food retailers

These retailers may not have sophisticated inventory systems but still need practical support when deciding what to buy.

---

## 🔍 Why StockLess?

Spreadsheets are flexible but leave the retailer to analyse sales and work out order quantities by hand. ERP systems offer broad business functions but bring cost and complexity.

StockLess focuses only on the purchasing decision, taking retailers from sales data to demand insights and a purchase check through a simple, guided interface.

---

## 🗂️ Repository Contents

This repository holds the **StockLess UI design**: clickable HTML pages for every screen, plus patches that bring the same design into the team's React app.

| File | What it is |
| --- | --- |
| `StockLess-Homepage.html` | Homepage. "Start with your sales data" opens Step 1 |
| `StockLess-Step1-Upload.html` | Step 1 — Upload |
| `StockLess-Step2-Mapping.html` | Step 2 — Map columns |
| `StockLess-Step3-Readiness.html` | Step 3 — Check readiness |
| `StockLess-Step4-Purchases.html` | Step 4 — Plan purchases (current design) |
| `StockLess-Impact-Dashboard.html` | Impact Dashboard |
| `*.patch` | Changes for the React app in the team repository |
| `WorkspaceDecor.tsx`, `stockless-step1/` | Supporting React component and Step 1 assets |

All pages link to each other: the logo and **Homepage** button open the homepage, the stepper moves between Steps 1–4, and Step 4's **See your impact** opens the dashboard. Each page works offline, keeps its language choice (English, Bahasa Melayu, 中文) between pages, and uses the bundled sample file so every screen shows real numbers.

---

## 🛠️ Technology

**Design pages (this repository)**

- Self-contained **HTML, CSS and JavaScript** files, one per screen
- Google Fonts: Manrope, Source Sans 3 and Inter
- No build step and no server needed

**StockLess app (team repository)**

- **React** and **TypeScript**, built with **Vite**
- Browser **Web Workers** for file parsing, readiness checks and forecasting
- **SheetJS** for reading Excel files
- **Vitest** and Testing Library for tests

---

## 🚀 Getting Started

### View the design

Clone the repository:

```bash
git clone https://github.com/syee0035/StockLess-UI.git
cd StockLess-UI
```

Open `StockLess-Homepage.html` in any modern browser (Chrome, Edge, Safari or Firefox), then follow the links through Steps 1–4 and the Impact Dashboard. You can also open any step's page directly.

### Apply a design patch to the React app

The `.patch` files are made against the team's StockLess app repository. From the root of that repository:

```bash
git checkout -b design-update
git apply --check path/to/StockLess-UI/<name>.patch   # confirm it applies cleanly
git apply path/to/StockLess-UI/<name>.patch
npm install
npm test
npm run dev
```

Run `npm test` before merging, since each patch also updates the tests that check the screens.

---

## 📄 Disclaimer

StockLess provides estimates to support purchasing decisions. It does not place orders, and its forecasts and impact figures are not guarantees of future sales or verified waste reductions.

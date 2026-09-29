# StockLess UI

**StockLess** is a web-based decision-support system designed to help Malaysian micro and small food retailers make smarter stock purchasing decisions and reduce avoidable food waste.

StockLess transforms historical sales data into demand insights and purchasing recommendations, helping retailers move from manual or rule-of-thumb stock decisions towards more informed replenishment.

> **Sales data → Demand insights → Smarter restocking → 🌱 Less waste**

---

## 🌱 About StockLess

Small food retailers often rely on spreadsheets, manual calculations, or personal experience when deciding how much inventory to purchase.

StockLess provides a simpler workflow that helps retailers understand their sales data before making their next purchasing decision.

The system focuses on four key questions:

- What products are selling?
- Is the sales data ready to use?
- Which products need attention?
- What should the retailer consider purchasing?

StockLess is designed to bridge the gap between **simple spreadsheets** and **complex ERP systems**, providing a focused workflow for demand understanding and restocking decisions.

---

## ✨ Key Features

### 1. Upload Sales Data

Retailers can upload their sales data using a CSV file.

#### Required data

- Sale date
- Product identification
- Quantity sold

#### Product identification

StockLess supports product identification using:

- SKU
- Barcode
- Product code
- Product name + pack size

Optional attributes can also be provided to unlock additional insights.

#### File limits

- `.CSV`
- Up to **10 MiB**
- Up to **100,000 rows**
- Comma, semicolon, or tab-separated files

---

### 2. Flexible Column Matching

After uploading a CSV file, StockLess helps users match their existing column names to the attributes required by the system.

This allows retailers to use their existing sales exports without having to manually restructure their data first.

The workflow helps users identify:

- Required attributes
- Optional attributes
- Unmatched columns
- Product identification fields
- Sales-related fields

---

### 3. Data Readiness Check

StockLess checks the uploaded data before it is used for purchasing analysis.

The readiness check helps identify issues such as:

- Missing information
- Invalid values
- Inconsistent data
- Product identification problems
- Stock-related issues
- Data that requires review

Instead of presenting only technical validation messages, StockLess aims to explain:

**What was found → Why it matters → What to do**

This allows retailers to understand their data problems before continuing to purchase planning.

---

### 4. Purchase Planning

Once the data is ready, StockLess turns sales information into purchasing insights.

The purchase planning workflow helps retailers identify products that may require:

- **Order Needed**
- **Check Your Order**
- **Looks Balanced**
- **Need More Data**

These categories are intended to support the retailer's decision-making rather than automatically place an order.

---

### 5. Sustainability Impact

StockLess connects purchasing decisions with food-waste reduction.

The system can present estimated impacts such as:

- Estimated cost savings
- Estimated food waste avoided
- Estimated emissions avoided

These figures are intended as **estimates** to help users understand the potential business and environmental impact of better stock decisions.

---

## 🧭 StockLess Workflow

StockLess uses a four-step workflow:

| Step | Purpose |
| --- | --- |
| 🌱 **01 Upload** | Upload sales data |
| 🌿 **02 Match** | Match CSV columns to StockLess attributes |
| 🍃 **03 Check** | Check data readiness and review issues |
| 🌳 **04 Plan** | Review purchasing recommendations |

The workflow progressively transforms raw sales data into actionable restocking information.

---

## 🔒 Privacy

StockLess is designed to keep users' sales data on their device where supported by the application.

The Upload screen communicates:

> **Your data stays on your device.**

CSV files are processed directly in the browser, and sales rows and product identifiers are not uploaded to an AI or API service.

---

## 📊 Data Requirements

### Required Attributes

| Attribute | Description |
| --- | --- |
| **Sale date** | The date associated with a sales transaction |
| **Product identification** | SKU, barcode, product code, or product name + pack size |
| **Quantity sold** | The number of units sold |

### Optional Attributes

Optional data can unlock additional insights within the StockLess workflow.

---

## 🎨 User Interface

StockLess uses a sustainability-focused visual language designed to make data-heavy workflows easier to understand.

The interface uses:

- Soft green and teal colours
- Rounded cards
- Clear status indicators
- Product-focused information
- Lightweight visualisations
- Tooltips for unfamiliar concepts
- Progressive disclosure
- Responsive layouts

The workspace uses a quieter version of the homepage visual style so that decorative elements support the experience without interfering with readability.

### Workspace background

The workspace includes a subtle decorative background inspired by the StockLess homepage:

- Soft green waves
- Leaf illustrations
- Dot patterns
- A clear central reading area

The artwork is intentionally reduced in opacity compared with the homepage and is hidden on smaller screens to maintain readability.

---

## 📱 Responsive Design

StockLess is designed for:

- Desktop
- Tablet
- Mobile web

The interface adapts its layout and information hierarchy according to screen size.

On smaller screens:

- Multi-column layouts become stacked sections
- Dense tables can become product cards
- Content is prioritised progressively
- Horizontal scrolling is avoided
- Touch targets remain accessible
- Decorative artwork is reduced or removed where necessary

The design aims to provide the same workflow across devices without simply shrinking the desktop interface.

---

## 🖥️ Application Screens

The StockLess workflow consists of the following main screens:

### Step 1 — Upload

Users learn what data they need and upload their CSV sales data.

### Step 2 — Match

Users match their uploaded columns with StockLess attributes.

### Step 3 — Check

Users review data readiness, product-level issues, and information that requires attention.

### Step 4 — Plan

Users review purchasing recommendations and determine what action to take.

---

## 🌍 Sustainability Context

StockLess focuses on **UN Sustainable Development Goal 12.3**, which targets the reduction of food waste at the retail and consumer levels.

The project focuses on avoidable food waste associated with purchasing and inventory decisions in small food retailers.

By helping retailers make more informed purchasing decisions, StockLess explores how data-driven decision support can contribute to more efficient inventory management and food-waste reduction.

---

## 🎯 Target Users

StockLess is primarily designed for:

**Malaysian micro and small food retailers**, including:

- Neighbourhood grocery stores
- Minimarts
- Small food retailers

The system is designed for retailers who may not have access to sophisticated inventory-management systems but still need practical support when making purchasing decisions.

---

## 🔍 Why StockLess?

StockLess is designed around the gap between:

**Spreadsheets**

and

**Enterprise Resource Planning (ERP) systems**

Traditional spreadsheets can provide flexibility but may require retailers to manually analyse sales information and calculate purchasing needs.

ERP systems can provide broader business functionality but may involve greater complexity and implementation requirements.

StockLess focuses specifically on the purchasing decision workflow, allowing retailers to move from sales data to demand insights and purchase planning through a simpler interface.

---

## 🛠️ Technology

The StockLess UI is built using:

- **React**
- **TypeScript**
- **CSS**
- **Vite**

The application is structured around reusable UI components and dedicated workflow screens.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Node.js and npm installed.

### Installation

Clone the repository:

```bash
<<<<<<< HEAD
git clone https://github.com/syee0035/StockLess-UI.git
=======
git clone https://github.com/syee0035/StockLess-UI.git
>>>>>>> 0ae82e6 (Latest updates of the design)

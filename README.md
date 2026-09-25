# 🌱 StockLess UI Prototype

> A user-centred web interface prototype for StockLess — a decision-support system designed to help Malaysian micro and small food retailers make better inventory purchasing decisions and reduce avoidable food waste.

---

## 📌 About StockLess

**StockLess** is a decision-support system developed to support small food retailers in making more informed inventory decisions.

Small retailers may rely on manual processes, past experience, or rule-of-thumb purchasing when deciding how much stock to purchase. This can result in excess inventory and avoidable food waste.

StockLess aims to help retailers move from:

**Historical Sales Data → Demand Understanding → Purchase Planning → Impact Awareness**

The project is aligned with **UN Sustainable Development Goal 12.3**, which focuses on reducing food loss and waste.

---

## 🎨 About This Repository

This repository contains the **StockLess UI Prototype**.

The prototype focuses on the visual design and user experience of the StockLess interface, including the landing page, navigation, workflow presentation, food-waste context, and responsive design.

The current prototype is implemented as a **standalone HTML file**, making it easy to open and demonstrate without requiring a backend or database.

---

## ✨ Key Features

### 🏠 StockLess Landing Page

The homepage introduces StockLess and communicates its purpose through a simple, sustainability-focused interface.

The design includes:

- StockLess branding
- Clear navigation
- Sustainability-focused visual elements
- Fresh produce imagery
- Clean and spacious layout
- Responsive design

---

### 📤 Data Upload Workflow

The prototype introduces the first stage of the StockLess workflow:

**Upload**

Retailers can begin the process by providing their sales data.

The intended workflow supports CSV-based sales data as the starting point for demand analysis.

---

### 📊 Data Analysis

The interface presents the analysis stage as part of the StockLess decision-making journey.

The goal is to help retailers understand:

- Historical sales patterns
- Product demand
- Data quality
- Potential inventory issues

---

### 🛒 Purchase Planning

StockLess connects demand analysis to purchasing decisions.

The purchase planning stage is designed to help retailers understand:

- Products that may require replenishment
- Potential overstock
- Potential understock
- Recommended purchasing quantities

---

### 🌱 Business & Environmental Impact

The interface also introduces the impact dimension of StockLess.

Potential indicators include:

**Business Impact**

- Potential cost savings
- Reduced excess inventory
- Improved purchasing decisions

**Environmental Impact**

- Food waste reduced
- Carbon emissions reduced
- Energy saved
- Reduced environmental impact

---

## 🔄 StockLess Workflow

```text
┌──────────────┐
│     HOME     │
│ Introduction │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    UPLOAD    │
│  Sales Data  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    ANALYSE   │
│ Demand Data  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     PLAN     │
│ Purchase Plan│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    IMPACT    │
│ Business +   │
│ Environment  │
└──────────────┘

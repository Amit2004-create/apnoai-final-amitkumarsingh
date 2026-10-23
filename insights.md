# ApnoMart Q2 2026 — Strategic Insights

**Analyst:** Amit Kumar Singh  
**Date:** October 2026  
**Tool Used:** Python (pandas, matplotlib) + interactive HTML dashboard (Chart.js)

**Headline numbers (Apr–Jun 2026):** Sales ₹133.2L · Profit ₹18.7L · 1,200 orders · Profit margin 14.0%

---

## Insight 1: Revenue Pattern

Electronics drives 56.5% of total revenue (₹75.3L of ₹133.2L), yet earns only ₹2,161 in profit, a margin of 0.03%. Office Supplies (48.0%) and Beauty (42.2%) earn far more per rupee sold, but together they are only 14.1% of sales. Monthly sales rose from ₹35.2L in April to ₹50.7L in May, then eased to ₹47.3L in June.

**So What:** More than half the business sits in a category that creates almost no profit. Growth in Electronics adds revenue and workload but not earnings, and the company's profit depends on much smaller categories.

---

## Insight 2: Profitability Pattern

All 200 loss-making orders are Electronics, and they lose ₹2.24L in total. Electronics orders with discounts above 20% (118 orders) lose ₹1.60L combined, an 8.2% negative margin. North is the weakest region: it is 25.1% of sales but has a 9.8% margin versus 14.7–16.1% elsewhere, driven by an average discount of 19.0% compared with 12.9% in the other regions. Electronics in North runs at -5.3% margin (₹0.99L loss).

**So What:** The profit leak is a discount-policy problem, concentrated in Electronics and amplified in North. It is not a demand problem.

---

## Insight 3: Customer Behavior Pattern

Corporate customers place 25.5% of orders (306 of 1,200) but contribute 40.7% of revenue (₹54.3L), with an average order value of ₹17,734, about 2.0x the Consumer segment's ₹8,840. Corporate margin (14.0%) matches the company average, so these larger orders are not being bought through deeper discounts. UPI is the dominant payment method at 39.8% of orders (38.5% of revenue), well ahead of Credit Card (19.8%).

**So What:** Corporate buyers deliver high-value, healthy-margin orders and are a natural segment to grow. UPI-first checkout is what most customers expect, so keep it fast and reliable.

---

## Strategic Recommendation

**Cap Electronics discounts at 15% across all regions, starting with North.** 269 of 381 Electronics orders (71%) were discounted above 15%, and together they lost ₹1.74L. Capping them at 15% would turn that into roughly ₹2.9L profit, an uplift of about **₹4.65L per quarter (+25% on total profit)** if volume holds, and about **₹3.9L (+21%)** even if a quarter of the affected orders are lost. Reinvest part of the gain into a Corporate B2B offer (volume pricing, invoicing) to grow the segment that already buys at 2x the order value.

*Method note: uplift = recomputing profit on Electronics orders with discount > 15% at a 15% discount, holding cost of goods constant. The data is a synthetic practice dataset, so treat the figures as illustrative.*

---

![Dashboard](dashboard.png)

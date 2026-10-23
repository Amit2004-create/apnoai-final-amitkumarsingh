# ApnoMart Q2 2026 Executive Dashboard

**The Insight Board** — ApnoAI Data Analytics Internship, Business Intelligence task  
**Author:** Amit Kumar Singh  
**Tool used:** Python (pandas, matplotlib) for the dashboard image; HTML + Chart.js for the interactive version

![Dashboard](dashboard.png)

## What's in this repo

| File | Description |
|---|---|
| `dashboard.png` | Executive dashboard screenshot (2304×1296) |
| `dashboard.html` | Interactive dashboard with Region and Category filters (open in any browser) |
| `insights.pdf` | Insights report with dashboard screenshot (main submission document) |
| `insights.md` | Same 3 insights + 1 strategic recommendation in Markdown |
| `apnomart_sales.csv` | 1,200-row ApnoMart sales dataset used |
| `build_dashboard.py` | Script that rebuilds `dashboard.png` from the CSV |

## Dashboard features

- KPI cards: Total Sales, Total Profit, Total Orders, Profit Margin % (calculated field: `SUM(Profit) / SUM(Sales)`)
- Sales by category, monthly trend, profit by region
- Bonus visuals: discount vs profit scatter, region × category margin heatmap, payment-method donut
- "One big thing" data-story callout at the top
- Interactive Region and Category filters (`dashboard.html`)

## Insights summary

1. **Revenue:** Electronics is 56.5% of revenue (₹75.3L) but earns a 0.03% margin.
2. **Profitability:** All 200 loss-making orders are Electronics; discounts above 20% lose money, and North (avg discount 19.0%) has the lowest margin at 9.8%.
3. **Customers:** Corporate is 25.5% of orders but 40.7% of revenue, at 2.0x the Consumer order value. UPI is 39.8% of orders.

**Recommendation:** Cap Electronics discounts at 15%, starting with North, for about +₹4.65L quarterly profit, and invest in a Corporate B2B offer.

## Reproduce

```bash
pip install pandas matplotlib
python build_dashboard.py
```

Built by Amit Kumar Singh · ApnoAI Data Analytics Intern · October 2026

"""ApnoMart Q2 2026 Executive Dashboard (static PNG).
Change NAME below, then run:  python build_dashboard.py
"""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

NAME = "Amit Kumar Singh"          # <-- put your name here

BLUE, GREEN, RED, GREY, INK, BG = "#2563EB", "#16A34A", "#DC2626", "#94A3B8", "#0F172A", "#F8FAFC"

df = pd.read_csv("apnomart_sales.csv", parse_dates=["Order_Date"])
S, P, N = df.Sales.sum(), df.Profit.sum(), len(df)
margin = P / S
lakh = lambda v: f"₹{v/1e5:,.1f}L"

fig = plt.figure(figsize=(19.2, 10.8), dpi=120, facecolor=BG)
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": "#CBD5E1"})

# ---- header
fig.text(0.03, 0.955, "ApnoMart Q2 2026 Executive Dashboard", fontsize=26, fontweight="bold", color=INK, va="center")
fig.text(0.03, 0.918, f"Prepared by {NAME}   ·   Apr–Jun 2026   ·   1,200 orders   ·   5 regions × 5 categories",
         fontsize=12, color="#475569", va="center")
fig.text(0.97, 0.955, "THE ONE BIG THING", fontsize=10, color=RED, fontweight="bold", ha="right", va="center")
fig.text(0.97, 0.925, "Electronics = 56.5% of revenue but 0.03% margin. Discounts above 20% make it loss-making.",
         fontsize=12, color=INK, ha="right", va="center", fontweight="bold")

# ---- KPI cards
kpis = [("TOTAL SALES", lakh(S), BLUE), ("TOTAL PROFIT", lakh(P), GREEN),
        ("TOTAL ORDERS", f"{N:,}", BLUE), ("PROFIT MARGIN %", f"{margin*100:.1f}%", GREEN),
        ("LOSS-MAKING ORDERS", f"{(df.Profit<0).sum()}  (all Electronics)", RED)]
x0, w, gap = 0.03, 0.178, 0.0125
for i, (lab, val, col) in enumerate(kpis):
    ax = fig.add_axes([x0 + i*(w+gap), 0.800, w, 0.088]); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0,rounding_size=0.08", fc="white", ec="#E2E8F0", transform=ax.transAxes))
    ax.add_patch(plt.Rectangle((0, 0.05), 0.018, 0.9, color=col, transform=ax.transAxes))
    ax.text(0.07, 0.72, lab, fontsize=10, color="#64748B", fontweight="bold", transform=ax.transAxes)
    ax.text(0.07, 0.25, val, fontsize=21 if len(val) < 12 else 16, color=col, fontweight="bold", transform=ax.transAxes)

def panel(rect, title):
    ax = fig.add_axes(rect, facecolor="white")
    ax.set_title(title, loc="left", fontsize=13, fontweight="bold", color=INK, pad=10)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(colors="#475569", labelsize=10)
    return ax

R1, R2, H = 0.46, 0.105, 0.27

# 1. Sales by category (bar) + margin label
ax = panel([0.10, R1, 0.24, H], "Sales by Category  (label = profit margin)")
c = df.groupby("Category").agg(S=("Sales", "sum"), P=("Profit", "sum")).sort_values("S")
ax.barh(c.index, c.S/1e5, color=BLUE)
for y, (s, p) in enumerate(zip(c.S, c.P)):
    m = p/s*100
    ax.text(s/1e5 + 0.8, y, f"{lakh(s)}  |  {m:.1f}%", va="center", fontsize=10, color=RED if m < 5 else INK, fontweight="bold" if m < 5 else "normal")
ax.set_xlim(0, c.S.max()/1e5*1.38); ax.set_xlabel("Sales (₹ lakh)", fontsize=10)

# 2. Monthly trend (line)
ax = panel([0.40, R1, 0.27, H], "Monthly Sales Trend")
m = df.groupby(df.Order_Date.dt.to_period("M")).agg(S=("Sales", "sum"), P=("Profit", "sum"))
lbl = [p.strftime("%b %Y") for p in m.index]
ax.plot(lbl, m.S/1e5, marker="o", lw=3, color=BLUE, label="Sales")
ax.plot(lbl, m.P/1e5, marker="o", lw=3, color=GREEN, label="Profit")
for xl, s, p in zip(lbl, m.S, m.P):
    ax.annotate(lakh(s), (xl, s/1e5), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9, color=BLUE)
    ax.annotate(lakh(p), (xl, p/1e5), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9, color=GREEN)
ax.set_ylim(0, m.S.max()/1e5*1.2); ax.legend(frameon=False, fontsize=10, loc="center right"); ax.set_ylabel("₹ lakh", fontsize=10)

# 3. Profit by region (bar, green/red)
ax = panel([0.735, R1, 0.235, H], "Profit by Region  (label = margin)")
r = df.groupby("Region").agg(S=("Sales", "sum"), P=("Profit", "sum")).sort_values("P", ascending=False)
ax.bar(r.index, r.P/1e5, color=[GREEN if p > 0 else RED for p in r.P])
for x, (s, p) in enumerate(zip(r.S, r.P)):
    ax.text(x, p/1e5 + 0.1, f"{lakh(p)}\n{p/s*100:.1f}%", ha="center", fontsize=10, color=INK)
ax.set_ylim(0, r.P.max()/1e5*1.25); ax.set_ylabel("Profit (₹ lakh)", fontsize=10)

# 4. Scatter: discount vs profit
ax = panel([0.075, R2, 0.265, H], "Discount vs Profit per Order")
for cat, g in df.groupby("Category"):
    pass
rest, el = df[df.Category != "Electronics"], df[df.Category == "Electronics"]
ax.scatter(rest.Discount*100 + np.random.default_rng(1).uniform(-.8, .8, len(rest)), rest.Profit/1e3, s=14, alpha=.45, color=GREY, label="Other categories")
ax.scatter(el.Discount*100 + np.random.default_rng(2).uniform(-.8, .8, len(el)), el.Profit/1e3, s=16, alpha=.6, color=BLUE, label="Electronics")
ax.axhline(0, color=RED, lw=1.2, ls="--")
ax.set_xlabel("Discount (%)", fontsize=10); ax.set_ylabel("Profit per order (₹ '000)", fontsize=10); ax.legend(frameon=False, fontsize=9, loc="upper right")

# 5. Heatmap region x category (margin %)
ax = panel([0.40, R2, 0.27, H], "Profit Margin %  Region × Category")
pv = df.pivot_table(index="Region", columns="Category", values=["Profit", "Sales"], aggfunc="sum")
hm = (pv["Profit"] / pv["Sales"] * 100)
im = ax.imshow(hm.values, cmap="RdYlGn", vmin=-10, vmax=50, aspect="auto")
ax.set_xticks(range(len(hm.columns))); ax.set_xticklabels([c.replace(" & ", " &\n").replace("Office ", "Office\n") for c in hm.columns], fontsize=9)
ax.set_yticks(range(len(hm.index))); ax.set_yticklabels(hm.index, fontsize=10)
for i in range(hm.shape[0]):
    for j in range(hm.shape[1]):
        ax.text(j, i, f"{hm.values[i,j]:.0f}%", ha="center", va="center", fontsize=10, fontweight="bold", color=INK)
for s in ax.spines.values(): s.set_visible(False)

# 6. Donut: payment methods
ax = panel([0.72, R2, 0.15, H], "Payment Methods (orders)")
ax.axis("off")
pm = df.Payment_Method.value_counts()
cols = [BLUE, "#60A5FA", "#93C5FD", "#BFDBFE", "#94A3B8", "#CBD5E1"]
wedges, _ = ax.pie(pm.values, colors=cols, startangle=90, counterclock=False, wedgeprops=dict(width=0.38, edgecolor="white"))
ax.legend(wedges, [f"{k}  {v/N*100:.0f}%" for k, v in pm.items()], loc="center left", bbox_to_anchor=(1.05, 0.5), frameon=False, fontsize=10)
ax.text(0, 0, "UPI\n40%", ha="center", va="center", fontsize=15, fontweight="bold", color=BLUE)

fig.text(0.5, 0.018, f"Built by {NAME} · ApnoAI Data Analytics Intern · October 2026", ha="center", fontsize=11, color="#64748B")
fig.savefig("dashboard.png", dpi=120, facecolor=BG)
print("saved dashboard.png", fig.get_size_inches()*120)

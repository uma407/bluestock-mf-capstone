import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

scheme = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nDataset Shape:")
print(scheme.shape)

print("\nColumns:")
print(scheme.columns)

print("\nMissing Values:")
print(scheme.isnull().sum())

print("\nSummary Statistics:")
print(scheme.describe())

print("\nTop 10 Funds by AUM:")

top_funds = scheme.sort_values(
    by="aum_crore",
    ascending=False
)[["scheme_name", "aum_crore"]]

print(top_funds.head(10))

top_funds.head(10).plot(
    x="scheme_name",
    y="aum_crore",
    kind="bar",
    figsize=(10,5)
)

plt.title("Top 10 Funds by AUM")
plt.tight_layout()
plt.show()

# SIP Inflow Trend

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\nSIP Dataset:")
print(sip.head())

plt.figure(figsize=(10,5))
plt.plot(sip.iloc[:,0], sip.iloc[:,1])

plt.title("Monthly SIP Inflows")
plt.xlabel("Month")
plt.ylabel("SIP Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# SIP Inflow Trend

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\nSIP Data:")
print(sip.head())

plt.figure(figsize=(10,5))

plt.plot(sip.iloc[:,0], sip.iloc[:,1])

plt.title("Monthly SIP Inflow Trend")
plt.xlabel("Month")
plt.ylabel("SIP Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Folio Count Growth

folio = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("\nFolio Data:")
print(folio.head())

plt.figure(figsize=(10,5))

plt.plot(folio.iloc[:,0], folio.iloc[:,1], marker="o")

plt.title("Industry Folio Count Growth")
plt.xlabel("Month")
plt.ylabel("Folio Count (Cr)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Category Inflow Heatmap

category = pd.read_csv("data/raw/05_category_inflows.csv")

print("\nCategory Inflows:")
print(category.head())

pivot_table = category.pivot(
    index=category.columns[0],
    columns=category.columns[1],
    values=category.columns[2]
)

plt.figure(figsize=(12,6))

sns.heatmap(
    pivot_table,
    cmap="YlGnBu",
    annot=False
)

plt.title("Category Inflow Heatmap")

plt.tight_layout()
plt.show()

# NAV Return Correlation Matrix

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio"
]

corr_matrix = scheme[numeric_cols].corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Fund Performance Correlation Matrix")

plt.tight_layout()
plt.show()

investor = pd.read_csv("data/raw/08_investor_transactions.csv")

plt.figure(figsize=(6,6))

investor["transaction_type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Transaction Type Distribution")
plt.ylabel("")
plt.show()

# State-wise SIP Amount

investor["amount_inr"] = pd.to_numeric(
    investor["amount_inr"],
    errors="coerce"
)

state_sip = investor.groupby("state")["amount_inr"].sum()

plt.figure(figsize=(10,6))

state_sip.sort_values().plot(kind="barh")

plt.title("State-wise SIP Amount")
plt.xlabel("Total SIP Amount (INR)")

plt.tight_layout()
plt.show()

# Age Group Distribution

plt.figure(figsize=(8,5))

investor["age_group"].value_counts().plot(
    kind="bar"
)

plt.title("Investor Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Investors")

plt.tight_layout()
plt.show()

# Gender Split

plt.figure(figsize=(6,6))

investor["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")
plt.ylabel("")

plt.show()

# T30 vs B30 City Tier Distribution

plt.figure(figsize=(6,6))

investor["city_tier"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 City Tier Distribution")
plt.ylabel("")

plt.show()

# SIP Amount by Age Group

investor["amount_inr"] = pd.to_numeric(
    investor["amount_inr"],
    errors="coerce"
)

plt.figure(figsize=(10,6))

sns.boxplot(
    data=investor,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount Distribution by Age Group")

plt.tight_layout()
plt.show()
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(aum.head())
print(aum.columns)

aum["date"] = pd.to_datetime(aum["date"])
aum["year"] = aum["date"].dt.year

plt.figure(figsize=(12,6))

sns.barplot(
    data=aum,
    x="year",
    y="aum_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House")
plt.ylabel("AUM (Crore)")
plt.tight_layout()

plt.show()

# Sector Allocation Donut Chart

portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print(portfolio.columns)
print(portfolio.head())

# Sector Allocation Donut Chart

portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

sector_alloc = portfolio.groupby("sector")["weight_pct"].sum()

plt.figure(figsize=(8,8))

plt.pie(
    sector_alloc,
    labels=sector_alloc.index,
    autopct="%1.1f%%"
)

centre_circle = plt.Circle((0,0), 0.70, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sector Allocation Across Equity Funds")

plt.tight_layout()
plt.show()
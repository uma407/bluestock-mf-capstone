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
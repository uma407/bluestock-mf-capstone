import pandas as pd
from pathlib import Path

data_path = Path("data/processed/cleaned_scheme_performance.csv")

perf_df = pd.read_csv(data_path)

risk_input = input("Enter risk appetite (Low / Moderate / High): ")

recommendations = (
    perf_df[perf_df["risk_grade"] == risk_input]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(
    recommendations[
        ["scheme_name", "risk_grade", "sharpe_ratio"]
    ]
)
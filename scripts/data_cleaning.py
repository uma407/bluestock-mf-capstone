import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

# Load NAV History
nav = pd.read_csv(raw_path / "02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort records
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only valid NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    processed_path / "cleaned_nav_history.csv",
    index=False
)

print("NAV cleaned successfully")

# Load Investor Transactions
transactions = pd.read_csv(
    raw_path / "08_investor_transactions.csv"
)

# Convert date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardize transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

transactions = transactions[
    transactions["transaction_type"].isin(valid_types)
]

# Keep valid amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Save cleaned file
transactions.to_csv(
    processed_path /
    "cleaned_investor_transactions.csv",
    index=False
)

print("Transactions cleaned successfully")

# Load Scheme Performance
performance = pd.read_csv(
    raw_path / "07_scheme_performance.csv"
)

# Keep valid expense ratios
performance = performance[
    performance["expense_ratio_pct"]
    .between(0.1, 2.5)
]

# Save cleaned file
performance.to_csv(
    processed_path /
    "cleaned_scheme_performance.csv",
    index=False
)

print("Performance cleaned successfully")
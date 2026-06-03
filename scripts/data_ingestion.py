from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

csv_files = sorted(raw_path.glob("*.csv"))

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"DATASET: {file.name}")

    try:
        df = pd.read_csv(file)

        print("Shape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")
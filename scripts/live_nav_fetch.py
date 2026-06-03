import requests
import pandas as pd
from pathlib import Path

output_dir = Path("data/raw")

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            nav_df.to_csv(
                output_dir / f"{name}_live_nav.csv",
                index=False
            )

            print(f"Downloaded: {name}")

        else:
            print(f"Failed: {name}")

    except Exception as e:
        print(f"Error for {name}: {e}")
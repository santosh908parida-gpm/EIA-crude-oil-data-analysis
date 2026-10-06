"""
This script does ONE thing: asks the EIA website for daily Brent crude
oil prices, and saves them into a file called brent_prices.csv that you
can open in Excel or any text editor.

HOW TO USE:
1. Paste your EIA API key into the API_KEY line below (between the quotes).
2. Run this file: python get_brent_prices.py
3. A file called brent_prices.csv will appear in the same folder.
"""

import requests
import csv

# PASTE YOUR API KEY HERE, between the quotes
API_KEY = "kMWwLaP6bX0Qwf2zdKR4cE4hVt4r2cDQjpRZJeCg"

# This is the specific "address" for Brent crude oil daily prices on EIA's site
URL = f"https://api.eia.gov/v2/seriesid/PET.RBRTE.D?api_key={API_KEY}"

print("Asking EIA for Brent oil price data...")
response = requests.get(URL)

if response.status_code != 200:
    print("Something went wrong. Here's what EIA's website said:")
    print(response.text)
else:
    data = response.json()
    rows = data["response"]["data"]

    print(f"Got {len(rows)} rows of data. Saving to brent_prices.csv ...")

    with open("brent_prices.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "price_usd_per_barrel"])
        for row in rows:
            writer.writerow([row["period"], row["value"]])

    print("Done! Open brent_prices.csv to see the data.")

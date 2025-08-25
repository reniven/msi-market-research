import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.environ.get("API_KEY")
url = (
    "https://api.census.gov/data/2023/acs/acs1"
    "?get=NAME,B19013_001E"
    "&for=state:*"
    f"&key={API_KEY}"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data[1:], columns=data[0])
df["B19013_001E"] = pd.to_numeric(df["B19013_001E"], errors="coerce")
df = df.dropna(subset=["B19013_001E"])
df_sorted = df.sort_values(by="B19013_001E", ascending=False)

print(df_sorted[["NAME", "B19013_001E"]].head(10))

import matplotlib.pyplot as plt

top10 = df_sorted.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top10["NAME"], top10["B19013_001E"])
plt.xlabel("State")
plt.ylabel("Median Household Income (USD)")
plt.title("Top 10 US States by Median Household Income (ACS 2022)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
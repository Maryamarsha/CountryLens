
import requests
import pandas as pd

# STEP 1: Extract data from API
url = "https://countries.dev/countries"

response = requests.get(url, timeout=30)
response.raise_for_status()
countries = response.json()

print("Data fetched successfully!")

# STEP 2: Convert JSON into a Pandas DataFrame
df = pd.DataFrame(countries)

# STEP 3: Select the columns we need
columns = [
    "name", "capital", "region",
    "subregion", "population", "area"
]

df = df[columns].copy()

# STEP 4: Remove duplicate countries
df = df.drop_duplicates(subset=["name"])

# STEP 5: Handle missing text values
for column in ["capital", "region", "subregion"]:
    df[column] = df[column].fillna("Unknown")
    df[column] = df[column].replace("", "Unknown")

# STEP 6: Convert numbers to numeric values
df["population"] = pd.to_numeric(
    df["population"], errors="coerce"
)
df["area"] = pd.to_numeric(
    df["area"], errors="coerce"
)

# Remove records with missing names or populations
df = df.dropna(subset=["name", "population"])

# Invalid or zero area cannot be used for density
df.loc[df["area"] <= 0, "area"] = float("nan")

# STEP 7: Calculate population density
df["population_density"] = (
    df["population"] / df["area"]
).round(2)

# Rename area column
df = df.rename(columns={"area": "area_km2"})

# STEP 8: Display cleaned data
print("\nTotal cleaned records:", len(df))
print("\nFirst 5 countries:")
print(df.head().to_string(index=False))

print("\nMissing density values:",
      df["population_density"].isna().sum())

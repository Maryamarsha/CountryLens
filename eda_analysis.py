
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# STEP 1: Read cleaned country data
df = pd.read_csv("data/countries.csv")

# Create a folder to save our results
Path("results").mkdir(exist_ok=True)

print("Welcome to CountryLens EDA!")
print("Total records:", len(df))

# STEP 2: Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df[["population", "area_km2",
          "population_density"]].describe())

# STEP 3: Top 10 countries by population
top_population = df.nlargest(10, "population")

print("\nTOP 10 MOST POPULATED COUNTRIES")
print(top_population[["name", "population"]])

plt.figure(figsize=(10, 6))
plt.barh(
    top_population["name"][::-1],
    top_population["population"][::-1] / 1_000_000
)
plt.title("Top 10 Most Populated Countries")
plt.xlabel("Population (Millions)")
plt.tight_layout()
plt.savefig("results/top_10_population.png")
plt.close()

# STEP 4: Top 10 countries by area
top_area = df.nlargest(10, "area_km2")

plt.figure(figsize=(10, 6))
plt.barh(
    top_area["name"][::-1],
    top_area["area_km2"][::-1]
)
plt.title("Top 10 Largest Countries by Area")
plt.xlabel("Area (Square Kilometres)")
plt.tight_layout()
plt.savefig("results/top_10_area.png")
plt.close()

# STEP 5: Top 10 countries by population density
# Exclude small territories with fewer than 1 million people
density_data = df[df["population"] >= 1_000_000]
top_density = density_data.nlargest(
    10, "population_density"
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_density["name"][::-1],
    top_density["population_density"][::-1]
)
plt.title("Highest Population Density (Population >= 1M)")
plt.xlabel("People per Square Kilometre")
plt.tight_layout()
plt.savefig("results/top_10_density.png")
plt.close()

# STEP 6: Regional population statistics
regional = df.groupby("region").agg(
    country_count=("name", "count"),
    total_population=("population", "sum"),
    average_density=("population_density", "mean")
).reset_index()

print("\nREGIONAL STATISTICS")
print(regional.to_string(index=False))

regional.to_csv(
    "results/regional_summary.csv", index=False
)

regional_sorted = regional.sort_values(
    "total_population"
)

plt.figure(figsize=(10, 6))
plt.barh(
    regional_sorted["region"],
    regional_sorted["total_population"] / 1_000_000
)
plt.title("Total Population by Region")
plt.xlabel("Population (Millions)")
plt.tight_layout()
plt.savefig("results/regional_population.png")
plt.close()

# STEP 7: Population distribution histogram
plt.figure(figsize=(10, 6))
plt.hist(
    df["population"].dropna() / 1_000_000,
    bins=25,
    edgecolor="black"
)
plt.title("Distribution of Country Populations")
plt.xlabel("Population (Millions)")
plt.ylabel("Number of Countries and Territories")
plt.tight_layout()
plt.savefig("results/population_distribution.png")
plt.close()

print("\nEDA completed successfully!")
print("5 charts saved in the results folder.")
print("Regional statistics saved as CSV.")

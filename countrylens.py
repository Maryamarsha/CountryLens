
import requests

# Step 1: Extract country information from an API

url = "https://countries.dev/countries"

print("Welcome to CountryLens!")
print("Fetching country data...")

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    countries = response.json()

    if not isinstance(countries, list) or not countries:
        raise ValueError("No country list was returned.")

    print("Data fetched successfully!")
    print("Total countries and territories:", len(countries))

    print("\nFirst 5 countries:")
    for country in countries[:5]:
        print(country["name"], "-", country.get("population"))

except (requests.RequestException, ValueError) as error:
    print("Error fetching data:", error)

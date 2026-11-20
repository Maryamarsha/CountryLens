
import pandas as pd
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from transform_data import df

# STEP 1: Define validation rules
class Country(BaseModel):
    name: str = Field(min_length=1)
    capital: str
    region: str
    subregion: str
    population: int = Field(ge=0)
    area_km2: float | None = Field(default=None, gt=0)
    population_density: float | None = Field(
        default=None, ge=0
    )

# STEP 2: Convert DataFrame into Python dictionaries
records = (
    df.astype(object)
    .where(pd.notna(df), None)
    .to_dict(orient="records")
)

# STEP 3: Validate each country
valid_countries = []
invalid_countries = []

for record in records:
    try:
        country = Country.model_validate(record)
        valid_countries.append(country.model_dump())

    except ValidationError as error:
        invalid_countries.append(record["name"])
        print("Invalid country:", record["name"])
        print(error)

# STEP 4: Convert validated data to DataFrame
validated_df = pd.DataFrame(
    valid_countries,
    columns=list(Country.model_fields)
)

print("\nValidation completed!")
print("Valid countries:", len(valid_countries))
print("Invalid countries:", len(invalid_countries))

# STEP 5: Save validated data to CSV
if not validated_df.empty:
    Path("data").mkdir(exist_ok=True)

    validated_df.to_csv(
        "data/countries.csv",
        index=False
    )

    print("\nCSV file saved successfully!")
    print("Location: data/countries.csv")
    print("\nFirst 5 validated countries:")
    print(validated_df.head().to_string(index=False))
else:
    print("No valid data available to save.")

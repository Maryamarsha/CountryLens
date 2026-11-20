
import subprocess
import sys
from pathlib import Path

# CountryLens Main Program
project_folder = Path(__file__).resolve().parent

print("=" * 45)
print("WELCOME TO COUNTRYLENS")
print("Global Country Data ETL & EDA System")
print("=" * 45)

def run_script(filename):
    subprocess.run(
        [sys.executable, str(project_folder / filename)],
        cwd=project_folder,
        check=True
    )

# STEP 1: Extract, clean, validate and save data
print("\nSTEP 1: Running ETL Pipeline...")
run_script("validate_data.py")

csv_file = project_folder / "data" / "countries.csv"

if not csv_file.exists():
    raise FileNotFoundError("Country dataset not found!")

print("\nETL Pipeline completed successfully!")

# STEP 2: Generate statistical analysis and charts
print("\nSTEP 2: Running EDA...")
run_script("eda_analysis.py")

# STEP 3: Verify generated outputs
files = [
    "results/top_10_population.png",
    "results/top_10_area.png",
    "results/top_10_density.png",
    "results/regional_population.png",
    "results/population_distribution.png",
    "results/regional_summary.csv"
]

missing = [
    file for file in files
    if not (project_folder / file).exists()
]

if missing:
    raise FileNotFoundError(
        f"Missing output files: {missing}"
    )

print("\n" + "=" * 45)
print("COUNTRYLENS COMPLETED SUCCESSFULLY!")
print("Cleaned data: data/countries.csv")
print("Charts and statistics: results/")
print("=" * 45)

# 🌍 CountryLens
### Global Country Data ETL & Exploratory Analysis System

CountryLens is a Python-based data analytics project that collects, cleans, validates, and analyzes geographical and demographic information about countries worldwide. It includes an interactive Streamlit dashboard for exploring and comparing countries.

## Project Objectives

- Automate country data extraction using a public API.
- Clean and transform raw data using Pandas.
- Validate data using Pydantic.
- Store the processed dataset in CSV format.
- Perform exploratory data analysis using Python.
- Visualize population, geographical area, and regional statistics.
- Provide an interactive country comparison dashboard.

## Data Source

**countries.dev API**

The project collects country names, capitals, regions, subregions, populations, and areas using a free country-data API.

Population density is calculated as:

**Population Density = Population / Area (km²)**

## ETL Pipeline

**1. Extract**

Country information is retrieved from the countries.dev API using Python Requests.

**2. Transform**

Pandas is used to:
- Remove duplicate records.
- Handle missing values.
- Standardize dataset columns.
- Convert numerical data into suitable formats.
- Calculate population density.

**3. Validate**

Pydantic checks country records against defined data types and validation rules.

**4. Load**

The cleaned dataset is saved to:

`data/countries.csv`

## Exploratory Data Analysis

The project generates five visualizations:

1. Top 10 most populated countries.
2. Top 10 largest countries by area.
3. Population density comparison for countries and territories with at least one million people.
4. Total population by geographical region.
5. Population distribution histogram.

Regional statistical summaries are also generated.

The outputs are stored in the `results/` folder.

## Interactive Streamlit Dashboard

The CountryLens dashboard provides:

- Country search and exploration.
- Region-based filtering.
- Country population and area comparisons.
- Population density comparisons.
- EDA charts and statistical visualizations.
- Downloadable cleaned country dataset.

## Technologies Used

- Python
- Pandas
- Pydantic
- Requests
- Matplotlib
- Streamlit
- Git and GitHub

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/Maryamarsha/CountryLens.git
cd CountryLens
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the ETL and EDA pipeline:

```bash
python main.py
```

Launch the interactive dashboard:

```bash
python -m streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Expected Output

- A cleaned and validated country dataset.
- Statistical summaries.
- Five EDA visualizations.
- An interactive country exploration dashboard.
- A reproducible ETL pipeline.

## Project Repository

https://github.com/Maryamarsha/CountryLens

## Conclusion

CountryLens demonstrates how Python can be used to extract real-world data, transform and validate it, perform meaningful statistical analysis, and present findings through interactive visualizations.
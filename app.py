
import streamlit as st
import pandas as pd
from pathlib import Path

# COUNTRYLENS VISUAL DASHBOARD

st.set_page_config(
    page_title="CountryLens",
    page_icon="🌍",
    layout="wide"
)

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "countries.csv"

if not DATA_FILE.exists():
    st.error("Dataset missing! Run python main.py first.")
    st.stop()

df = pd.read_csv(DATA_FILE)

# Heading
st.title("🌍 CountryLens")
st.subheader("Global Country Explorer & Analytics")
st.write("Explore, analyze and compare countries worldwide.")

# Sidebar
st.sidebar.title("🌍 CountryLens")
st.sidebar.header("Filter Countries")

regions = ["All Regions"] + sorted(
    df["region"].dropna().unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "Select Region", regions
)

if selected_region == "All Regions":
    filtered = df.copy()
else:
    filtered = df[df["region"] == selected_region]

# Dashboard statistics
col1, col2, col3 = st.columns(3)

col1.metric("Countries & Territories", len(filtered))
col2.metric(
    "Total Population",
    f"{filtered['population'].sum():,.0f}"
)
col3.metric(
    "Average Population Density",
    f"{filtered['population_density'].mean():,.2f}"
)

st.divider()

# Dashboard tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 Country Explorer",
    "📊 Country Comparison",
    "📈 EDA Analysis",
    "📁 Dataset"
])

# TAB 1 - Country Explorer
with tab1:
    st.header("Search Countries")

    search = st.text_input("Enter Country Name")

    result = filtered[
        filtered["name"].str.contains(
            search, case=False, na=False, regex=False
        )
    ]

    st.dataframe(result, hide_index=True)

    if not result.empty:
        country_name = st.selectbox(
            "Select a Country",
            sorted(result["name"].tolist())
        )

        country = result[
            result["name"] == country_name
        ].iloc[0]

        st.subheader("Country Information")

        st.write("Country:", country["name"])
        st.write("Capital:", country["capital"])
        st.write("Region:", country["region"])
        st.write("Subregion:", country["subregion"])
        st.write("Population:", f"{country['population']:,.0f}")
        st.write("Area (km²):", country["area_km2"])
        st.write("Population Density:", country["population_density"])

# TAB 2 - Compare Countries
with tab2:
    st.header("Compare Countries")

    selected = st.multiselect(
        "Choose Countries",
        sorted(df["name"].tolist()),
        default=[
            name for name in ["Pakistan", "India", "China"]
            if name in df["name"].values
        ]
    )

    comparison = df[df["name"].isin(selected)].copy()

    if not comparison.empty:
        st.subheader("Population Comparison")
        st.bar_chart(
            comparison.set_index("name")["population"]
        )

        st.subheader("Land Area Comparison")
        st.bar_chart(
            comparison.set_index("name")["area_km2"]
        )

        st.subheader("Population Density Comparison")
        st.bar_chart(
            comparison.set_index("name")["population_density"]
        )

        st.dataframe(comparison, hide_index=True)
    else:
        st.info("Select countries to compare.")

# TAB 3 - Exploratory Data Analysis
with tab3:
    st.header("Exploratory Data Analysis")

    charts = [
        ("Top 10 Most Populated Countries", "top_10_population.png"),
        ("Top 10 Largest Countries", "top_10_area.png"),
        ("Top 10 Population Densities", "top_10_density.png"),
        ("Population by Region", "regional_population.png"),
        ("Population Distribution", "population_distribution.png")
    ]

    for title, filename in charts:
        st.subheader(title)
        chart_path = BASE / "results" / filename

        if chart_path.exists():
            st.image(str(chart_path), width="stretch")
        else:
            st.warning(f"Chart not found: {filename}")

# TAB 4 - Dataset
with tab4:
    st.header("Cleaned Country Dataset")

    st.dataframe(df, hide_index=True)

    st.download_button(
        "Download CSV Dataset",
        data=DATA_FILE.read_bytes(),
        file_name="countries.csv",
        mime="text/csv"
    )

st.divider()
st.caption("CountryLens | Python • Pandas • Pydantic • Matplotlib")

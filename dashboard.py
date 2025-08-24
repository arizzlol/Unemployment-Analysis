import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
def dashboard_page():
    st.markdown(
        """
        <h1 style="
            text-align: center;
            background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 50%, #56ab2f 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Funnel Display SemiBold', sans-serif;
            padding: 20px 0;
        ">
         Global Analysis Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                              url("https://wallpaperbat.com/img/879351-analysis-wallpaper-top-free-analysis-background.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .stApp {
            font-family: 'Funnel Display SemiBold', sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            background-color: #f0f2f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.subheader("Explore global unemployment trends through interactive visualizations.")

    # --- Data Loading and Caching ---
    @st.cache_data
    def load_data(file_path):
        """Loads and preprocesses the unemployment data."""
        df = pd.read_csv(file_path)
        # Melt the dataframe to make it tidy (long format)
        id_vars = ['country_name', 'indicator_name', 'sex', 'age_group', 'age_categories']
        value_vars = [col for col in df.columns if col.startswith('20')]
        df_melted = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='year', value_name='unemployment_rate')
        df_melted['year'] = pd.to_numeric(df_melted['year'])
        # Drop rows with missing unemployment rates for cleaner visualizations
        df_melted.dropna(subset=['unemployment_rate'], inplace=True)
        return df_melted

    # --- Main Application ---
    st.title("🌍 Global Unemployment Comparative Analysis")
    st.markdown("""
    This report provides an interactive analysis of unemployment trends across the globe.
    The data, spanning from 2014 to 2024, allows for comparisons between countries based on various demographic factors.
    All visualizations are interactive; hover over the charts for detailed figures and use the legends to filter data.
    """)

    # Load the data
    try:
        data = load_data('global_unemployment_data.csv')
    except FileNotFoundError:
        st.error("Error: 'global_unemployment_data.csv' not found. Please ensure the data file is in the same directory as the script.")
        st.stop()


    # --- Section 1: Global Unemployment Map ---
    st.header("Global Unemployment Landscape")
    st.markdown("""
    **What this shows:** The world map below visualizes the average unemployment rate for a selected year across all available countries. Darker shades indicate higher unemployment rates.

    **Why it's important:** This provides a high-level overview of the global economic climate. It helps in quickly identifying regions or continents facing significant unemployment challenges, which can be linked to economic downturns, political instability, or long-term structural issues.
    """)

    year_for_map = st.slider(
        'Select a Year for the Global Map',
        min_value=int(data['year'].min()),
        max_value=int(data['year'].max()),
        value=int(data['year'].max()) -1, # Default to the second to last year for more complete data
        key='map_year_slider'
    )

    # Filter data for the map (averaging across sex and age groups for a single country value)
    map_data = data[(data['year'] == year_for_map)].groupby('country_name')['unemployment_rate'].mean().reset_index()

    fig_map = px.choropleth(
        map_data,
        locations="country_name",
        locationmode='country names',
        color="unemployment_rate",
        hover_name="country_name",
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f"Average Unemployment Rate in {year_for_map}"
    )
    fig_map.update_layout(
        geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'),
        margin={"r":0,"t":40,"l":0,"b":0}
    )
    st.plotly_chart(fig_map, use_container_width=True)


    # --- Section 2: Comparing Countries Side-by-Side ---
    st.header("Country-to-Country Comparison")
    st.markdown("""
    **What this shows:** The bar chart below directly compares the unemployment rates for a selection of countries in a specific year, filtered by sex and age group.

    **Why it's important:** Direct comparisons are crucial for benchmarking. Policymakers, economists, and researchers can use this to understand how one country's labor market performs relative to its peers, neighbors, or economic competitors. It helps answer questions like, "Is high youth unemployment a domestic issue or a regional trend?"
    """)

    # User selections
    col1, col2, col3 = st.columns(3)
    with col1:
        year_for_bar = st.selectbox(
            'Select Year',
            sorted(data['year'].unique(), reverse=True),
            key='bar_year_select'
        )
    with col2:
        sex_for_bar = st.selectbox(
            'Select Sex',
            data['sex'].unique(),
            key='bar_sex_select'
        )
    with col3:
        age_for_bar = st.selectbox(
            'Select Age Group',
            data['age_group'].unique(),
            key='bar_age_select'
        )

    countries_for_bar = st.multiselect(
        'Select Countries to Compare',
        sorted(data['country_name'].unique()),
        default=['United States', 'Germany', 'China', 'India', 'Brazil', 'Nigeria'],
        key='bar_country_multi'
    )

    if countries_for_bar:
        bar_data = data[
            (data['year'] == year_for_bar) &
            (data['sex'] == sex_for_bar) &
            (data['age_group'] == age_for_bar) &
            (data['country_name'].isin(countries_for_bar))
        ]

        if not bar_data.empty:
            fig_bar = px.bar(
                bar_data,
                x='country_name',
                y='unemployment_rate',
                color='country_name',
                title=f"Unemployment Rate Comparison ({sex_for_bar}, {age_for_bar}, {year_for_bar})",
                labels={'unemployment_rate': 'Unemployment Rate (%)', 'country_name': 'Country'}
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.warning("No data available for the selected combination of filters. Please try a different selection.")
    else:
        st.info("Please select at least one country to generate the comparison chart.")


    # --- Section 3: Youth vs. Adult Unemployment ---
    st.header("Youth vs. Adult Unemployment: A Structural Indicator")
    st.markdown("""
    **What this shows:** The scatter plot below plots Youth (15-24) unemployment against Adult (25+) unemployment for a given year. Each bubble represents a country.

    **Why it's important:** The relationship between youth and adult unemployment is a key indicator of a country's labor market health.
    - **Countries above the diagonal line** have a higher youth unemployment rate than the adult rate, which is typical but can be extreme.
    - **A large vertical distance from the line** suggests structural barriers for young people entering the workforce, such as a mismatch between skills taught in education and skills demanded by employers.
    """)

    year_for_scatter = st.selectbox(
        'Select Year for Youth vs. Adult Analysis',
        sorted(data['year'].unique(), reverse=True),
        key='scatter_year_select'
    )

    # Prepare data for the scatter plot
    youth_data = data[(data['year'] == year_for_scatter) & (data['age_group'] == '15-24')].groupby('country_name')['unemployment_rate'].mean().reset_index()
    youth_data.rename(columns={'unemployment_rate': 'Youth Unemployment'}, inplace=True)

    adult_data = data[(data['year'] == year_for_scatter) & (data['age_group'] == '25+')].groupby('country_name')['unemployment_rate'].mean().reset_index()
    adult_data.rename(columns={'unemployment_rate': 'Adult Unemployment'}, inplace=True)

    scatter_data = pd.merge(youth_data, adult_data, on='country_name')

    if not scatter_data.empty:
        fig_scatter = px.scatter(
            scatter_data,
            x='Adult Unemployment',
            y='Youth Unemployment',
            hover_name='country_name',
            size='Youth Unemployment', # Bubble size represents the magnitude of youth unemployment
            color='country_name',
            title=f'Youth vs. Adult Unemployment Rates in {year_for_scatter}'
        )
        # Add a y=x line for reference
        fig_scatter.add_shape(type='line', x0=0, y0=0, x1=scatter_data['Adult Unemployment'].max(), y1=scatter_data['Adult Unemployment'].max(), line=dict(color='Gray', dash='dash'))
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning(f"Could not generate Youth vs. Adult analysis for {year_for_scatter}. Data might be missing.")

        
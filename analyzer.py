import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def analyzer_page():
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
        <h1 style="
            text-align: center;
            background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 50%, #56ab2f 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Funnel Display SemiBold', sans-serif;
            padding: 20px 0;
        ">
         Country Employment Analyzer
        </h1>
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
    st.subheader("Analyze employment trends for specific countries.")
# Load data
    @st.cache_data
    def load_data(file_path):
        df = pd.read_csv(file_path)
        return df

    df = load_data('global_unemployment_data.csv')

    # --- Main Filter Options ---
    with st.expander("Filter Options", expanded=True):
        # Melt the dataframe to make it tidy
        id_vars = ['country_name', 'indicator_name', 'sex', 'age_group', 'age_categories']
        value_vars = [col for col in df.columns if col.startswith('20')]
        df_melted = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='year', value_name='unemployment_rate')
        df_melted['year'] = pd.to_numeric(df_melted['year'])

        # --- Graph 1: Unemployment Rate Trend ---
        st.subheader('1. Unemployment Rate Trend Over Time')
        selected_country_trend = st.selectbox('Select a Country', df_melted['country_name'].unique(), key='trend_country')
        selected_sex_trend = st.selectbox('Select Sex', df_melted['sex'].unique(), key='trend_sex')
        selected_age_trend = st.selectbox('Select Age Group', df_melted['age_group'].unique(), key='trend_age')

        if st.button('Generate Trend Plot', key='trend_button'):
            trend_data = df_melted[
                (df_melted['country_name'] == selected_country_trend) &
                (df_melted['sex'] == selected_sex_trend) &
                (df_melted['age_group'] == selected_age_trend)
            ]
            if not trend_data.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.lineplot(data=trend_data, x='year', y='unemployment_rate', marker='o', ax=ax)
                ax.set_title(f'Unemployment Rate Trend in {selected_country_trend} ({selected_sex_trend}, {selected_age_trend})')
                ax.set_xlabel('Year')
                ax.set_ylabel('Unemployment Rate (%)')
                ax.grid(True)
                st.pyplot(fig)
            else:
                st.write("No data available for the selected criteria.")

        # --- Graph 2: Compare Unemployment Rates Across Countries ---
        st.subheader('2. Compare Unemployment Rates Across Countries')
        selected_year_comp = st.slider('Select Year for Comparison', min_value=2014, max_value=2024, value=2023, key='comp_year')
        selected_sex_comp = st.selectbox('Select Sex', df_melted['sex'].unique(), key='comp_sex')
        selected_age_comp = st.selectbox('Select Age Group', df_melted['age_group'].unique(), key='comp_age')
        n_countries = st.slider('Top N Countries', min_value=5, max_value=20, value=10, key='n_countries')

        if st.button('Generate Comparison Plot', key='comp_button'):
            comp_data = df_melted[
                (df_melted['year'] == selected_year_comp) &
                (df_melted['sex'] == selected_sex_comp) &
                (df_melted['age_group'] == selected_age_comp)
            ].sort_values(by='unemployment_rate', ascending=False).head(n_countries)

            if not comp_data.empty:
                fig, ax = plt.subplots(figsize=(12, 8))
                sns.barplot(data=comp_data, x='unemployment_rate', y='country_name', ax=ax)
                ax.set_title(f'Top {n_countries} Countries by Unemployment Rate in {selected_year_comp}')
                ax.set_xlabel('Unemployment Rate (%)')
                ax.set_ylabel('Country')
                st.pyplot(fig)
            else:
                st.write("No data available for the selected criteria.")

        # --- Graph 3 & 4: Unemployment by Sex and Age Group ---
        st.subheader('3. Unemployment by Sex and Age Group in a Country')
        selected_country_detail = st.selectbox('Select a Country', df_melted['country_name'].unique(), key='detail_country')
        selected_year_detail = st.slider('Select Year', min_value=2014, max_value=2024, value=2023, key='detail_year')

        if st.button('Show Details', key='detail_button'):
            detail_data = df_melted[
                (df_melted['country_name'] == selected_country_detail) &
                (df_melted['year'] == selected_year_detail)
            ]
            if not detail_data.empty:
                # By Sex
                fig1, ax1 = plt.subplots(figsize=(8, 5))
                sns.barplot(data=detail_data, x='sex', y='unemployment_rate', ax=ax1, estimator=sum)
                ax1.set_title(f'Unemployment Rate by Sex in {selected_country_detail} ({selected_year_detail})')
                ax1.set_xlabel('Sex')
                ax1.set_ylabel('Unemployment Rate (%)')
                st.pyplot(fig1)

                # By Age Group
                fig2, ax2 = plt.subplots(figsize=(8, 5))
                sns.barplot(data=detail_data, x='age_group', y='unemployment_rate', ax=ax2, estimator=sum)
                ax2.set_title(f'Unemployment Rate by Age Group in {selected_country_detail} ({selected_year_detail})')
                ax2.set_xlabel('Age Group')
                ax2.set_ylabel('Unemployment Rate (%)')
                st.pyplot(fig2)
            else:
                st.write("No data available for the selected criteria.")

        # --- Graph 5: Distribution of Unemployment Rates ---
        st.subheader('4. Distribution of Unemployment Rates')
        selected_year_dist = st.slider('Select Year for Distribution', min_value=2014, max_value=2024, value=2023, key='dist_year')

        if st.button('Generate Distribution Plot', key='dist_button'):
            dist_data = df_melted[df_melted['year'] == selected_year_dist]
            if not dist_data.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(dist_data['unemployment_rate'], kde=True, ax=ax, bins=30)
                ax.set_title(f'Distribution of Unemployment Rates in {selected_year_dist}')
                ax.set_xlabel('Unemployment Rate (%)')
                ax.set_ylabel('Frequency')
                st.pyplot(fig)
            else:
                st.write("No data available for the selected criteria.")


        # --- Graph 6: Correlation Heatmap ---
        st.subheader('5. Correlation of Unemployment Rates Between Years')
        if st.button('Show Correlation Heatmap', key='corr_button'):
            year_cols = [col for col in df.columns if col.startswith('20')]
            corr_df = df[year_cols]

            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(corr_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
            ax.set_title('Correlation Heatmap of Unemployment Rates Between Years')
            st.pyplot(fig)
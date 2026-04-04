import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components


# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(
    page_title="Data Cleaning",
    layout="wide",
    page_icon="🧹",
)

st.title("🧹 sales Data Cleaning  transformation app for forecasting app")
st.write(
    " upload your sales dataset and perform:"
    " Data cleaning "
    "Missing value handling"
    "Outlier detection and removal"
    " Automatic EDA Report "
    " Data transformation for forecasting"
)

# ------------------------------------------
# File Upload
# ------------------------------------------
uploaded_file = st.file_uploader("Upload your sales data (CSV format)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # define pattern mapping
    columns_mapping = {
        "date": ["date", "day", "month", "year"],
        "revenue": ["revenue", "sales", "income"],
        "cost": ["cost", "cogs", "cost_of_goods_sold"],
        "operating_expenses": ["operating_expenses", "opex", "operating_costs"],
        "marketing_spend": ["marketing_spend", "marketing_spend", "advertising_costs"],
    }

    # inverse mapping for column detection
    standardized_columns = {}
    for standard_name, patterns in columns_mapping.items():
        for col in df.columns:
            if col in patterns:
                standardized_columns[col] = standard_name

    # rename columns based on detected mapping
    df.rename(columns=standardized_columns, inplace=True)
    tab1, tab2 = st.tabs([" Data cleaning & Transformation", " Automatic EDA Report"])

    with tab1:
        st.subheader("🧹 Data Cleaning and Transformation")
        st.write(
            "This section allows you to clean and transform your sales data for forecasting. You can select the relevant columns, handle missing values, remove outliers, and prepare the data for analysis."
        )
        st.dataframe(df.head())
        # select columns for forecasting
        select_columns = st.multiselect(
            "Select columns for forecasting", options=df.columns, default= list(df.columns)
        )

        if select_columns:
            df = df[select_columns].copy()

            # convert numeric columns to numeric type
            obj_cols = df.select_dtypes(include=["object"]).columns
            for col in obj_cols:
                cleaned_text  = (
                    df[col]
                    .astype(str)
                    .str.replace(",", "")
                    .str.replace("rupee", "", case = False)
                    .str.strip()
                )
                numeric_attempt = pd.to_numeric(cleaned_text, errors="coerce")
                if numeric_attempt.notna().any():
                    df[col] = numeric_attempt

            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"], errors="coerce")
                df.dropna(subset=["date"], inplace=True)
            st.subheader("🧹 Handling Missing Values")
            null_values = df.isnull().sum()
            nill_percent = (null_values / len(df)) * 100
            null_df = pd.DataFrame(
                {
                    "column": null_values.index,
                    "null_count": null_values.values,
                    "null_percent": nill_percent.round(2),
                }
            )

            st.dataframe(null_df)
            # missing value handling
            st.subheader("🧹 Missing Value Handling")
            method = st.selectbox(
                "Select method for handling missing values",
                options=[
                    "do nothing",
                    "Drop rows with missing values",
                    "Fill missing values with mean",
                    "Fill missing values with median",
                    "Fill missing values with mode",
                ],
            )

            if method == "Drop rows with missing values":
                df = df.dropna()
            elif method == "Fill missing values with mean":
                df.select_dtypes(include=["number"]).columns
                df = df.fillna(df.mean(numeric_only=True))
                
                
            elif method == "Fill missing values with median":
                df.select_dtypes(include=["number"]).columns
                df = df.fillna(df.median(numeric_only=True))
            elif method == "Fill missing values with mode":
                df = df.fillna(df.mode().iloc[0])
                
       

                # outlier detection and removal
        st.divider()        
        st.subheader("🧹 Outlier Detection and Removal")
        numeric_cols = df.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower) | (df[col] > upper)]
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"Column: {col}")
                st.write(f"Number of outliers: {len(outliers)}")
                st.write(f"Lower bound: {lower}")
                st.write(f"Upper bound: {upper}")
                remove = st.checkbox(f"Remove outliers from column: {col}")
            with col2:
                if not outliers.empty:
                    fig, ax = plt.subplots(figsize=(10, 2))
                    sns.boxplot(x=df[col], ax=ax, color="skyblue")
                    ax.set_title(f"Boxplot for {col}")
                    st.pyplot(fig)

            if remove:
                df = df[(df[col] >= lower) & (df[col] <= upper)]
                st.write(f"Outliers removed from column: {col}")

                # short and aggregated by date
        st.divider()
        if "date" in df.columns:
            st.subheader("🧹 Data Transformation for Forecasting")
            if st.checkbox("Sort and aggregate data by date *(sum)*"):
                df = df.sort_values("date")
                df = df.groupby("date").sum().reset_index()

        st.subheader("🧹 Cleaned and Transformed Data")
        st.dataframe(df.head())
        cleaned_df = df.copy()
        csv = cleaned_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name="cleaned_sales_data.csv",
            mime="text/csv",
        )

    # tab 2 - automatic EDA report

    with tab2:
        st.subheader("📊 Automatic EDA Report")
        st.write(
            "This section generates an automatic Exploratory Data Analysis (EDA) report for your sales data. The report includes insights into the distribution of variables, correlations, and potential issues in the dataset."
        )
       
        if st.button("Generate EDA Report"):
            with st.spinner("Generating EDA report..."):
                profile = ProfileReport( cleaned_df ,title = "sales data EDA report ", explorative=True)
                html = profile.to_html()
                components.html(html, height=800, scrolling=True)
                st.success("EDA report generated successfully!")
                st.download_button(
                    label="Download EDA Report (HTML)",
                    data=html,
             file_name="sales_data_eda_report.html",
                    mime="text/html",
                )

                
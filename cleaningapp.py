import streamlit as st
import pandas as pd 

# ------------------------------------------
# Page Configuration
# ------------------------------------------
st.set_page_config(
    page_title="Data Cleaning",
    layout="wide",
    page_icon="🧹",)

st.title("🧹 sales Data Cleaning  transformation app for forecasting app")
st.write(" upload your sales data to clean and transform it for forecasting " \
        "1.remove duplicates 2.handle missing values 3.standardize date format ")
# ------------------------------------------
# File Upload
# ------------------------------------------
uploaded_file = st.file_uploader("Upload your sales data (CSV format)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    #standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # define pattern mapping
    columns_mapping = {
        'date': ['date', 'day', 'month', 'year'],
        'revenue': ['revenue', 'sales', 'income'],
        'cost': ['cost', 'cogs', 'cost_of_goods_sold'],
        'operating_expenses': ['operating_expenses', 'opex', 'operating_costs'],
        'marketing_spend': ['marketing_spend', 'marketing_spend', 'advertising_costs']
    }

    # inverse mapping for column detection
    standardized_columns = {}
    for standard_name, patterns in columns_mapping.items():
        for col in df.columns:
            if col.lower().strip() in [p.lower().strip() for p in patterns]:
                standardized_columns[col] = standard_name
    # rename columns based on detected mapping
    df.rename(columns=standardized_columns, inplace=True)
    st.subheader("🧹 renamed data preview")
    st.dataframe(df.head())

            
            


    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    st.subheader("🧹 select required columns name ")
    columns = st.multiselect("select columns for forecasting", options=df.columns)
    if columns:
        df = df[columns]

        # convert date column to datetime
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df = df.dropna(subset=['date'])

            # convert numeric columns to numeric type
            numeric_cols = df.select_dtypes(include=['object']).columns
            for col in numeric_cols:
                df[col] = (df[col].astype(str).str.replace(',', '').str.replace('rupee', '').str.strip())
                df[col] = pd.to_numeric(df[col], errors='ignore')

                # drop missing values
            df = df.dropna()
            # remove duplicates
            df = df.drop_duplicates()
            #short by date
            if 'date' in df.columns:
                df = df.sort_values(by='date')  

                # aggregate data by date if there are multiple entries for the same date
                if "date" in df.columns:
                    df = df.groupby('date').sum().reset_index()
        st.subheader("🧹 Cleaned Data Preview")
        st.dataframe(df.head())
        st.success("Data cleaning and transformation completed successfully! You can now use this cleaned data for forecasting.")
        # download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name='cleaned_sales_data.csv',
            mime='text/csv',
        )

    



    
    
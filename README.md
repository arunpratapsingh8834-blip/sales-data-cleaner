# 📊 Enterprise Profit & Loss Intelligence System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Prophet-green.svg)

**Live Demo:** [Insert Your Live Streamlit Link Here]

## 📝 Overview
This project is an end-to-end Automated Data Engineering and AI Forecasting application built with Python. It empowers businesses to move beyond static spreadsheets by automatically cleaning raw financial data, performing advanced exploratory data analysis (EDA), and utilizing time-series machine learning to predict future profitability.

Designed with a robust ETL (Extract, Transform, Load) pipeline, the app intelligently handles messy data formats and generates interactive, recruiter-ready business insights.

## 🚀 Key Features

### 1. Automated Data Cleaning Pipeline (ETL)
* **Smart Dictionary Mapping:** Automatically detects and standardizes varied column names (e.g., mapping "Sales", "Income", or "Amount" to `revenue`).
* **Dynamic Type Casting:** Safely scrubs string-based currency formats (removing commas and text like "rupees") and converts them to usable numeric floats without dropping text-based categorical columns.
* **Missing Value Handling:** Provides an interactive UI to handle `NaN` values via dropping rows, or filling with mean, median, or mode.

### 2. Advanced Outlier Detection
* Implements the **Interquartile Range (IQR) method** to mathematically identify outliers in numerical columns.
* Dynamically generates Seaborn boxplots for visual confirmation before allowing the user to seamlessly drop outliers from the dataset.

### 3. Automated Exploratory Data Analysis (EDA)
* Integrates `ydata-profiling` to generate comprehensive, downloadable HTML reports.
* Includes interactive Plotly correlation matrices to uncover statistical relationships between financial metrics.

### 4. Machine Learning Forecasting
* Integrates **Facebook's Prophet** algorithm for robust time-series forecasting.
* Predicts net profit and revenue trends over dynamic 30-to-365-day horizons, adjusting for localized seasonal trends and automated noise reduction.

## 💻 Tech Stack
* **Frontend UI:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Plotly, Seaborn, Matplotlib
* **Machine Learning:** Prophet, Scikit-Learn
* **Automated Profiling:** ydata-profiling

## 📂 Repository Structure
* `forecasting_final.py`: The main Streamlit application containing the UI, cleaning pipeline, and forecasting models.
* `generate_dataset.py`: A custom Python script to randomly engineer mathematically sound mock financial datasets for testing.
* `requirements.txt`: The library dependencies required to run the application.
* `company_financial_data_main.csv`: A sample dataset for immediate testing.

## ⚙️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/profit_loss_forecasting.git](https://github.com/yourusername/profit_loss_forecasting.git)

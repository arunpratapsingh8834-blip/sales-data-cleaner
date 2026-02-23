📌 Problem Statement

Business sales data often contains:

Inconsistent column names (e.g., COGS, Cost of Goods, Goods)

Currency symbols and commas in numeric fields

Improper date formatting

Duplicate records

Missing values

These issues prevent accurate analytics and forecasting.

This application solves that by automatically cleaning and standardizing the dataset.
How It Works (Step-by-Step)
1️⃣ Upload Raw CSV

Users upload a company sales dataset in CSV format.

2️⃣ Column Standardization

Automatically maps inconsistent financial column names:

COGS / Cost of Goods / Goods → cost

Sales / Income → revenue

Opex / Operating Expenses → operating_expenses

Ad Spend / Marketing Spend → marketing_spend

3️⃣ Data Cleaning

Converts date column to datetime format

Removes currency symbols (₹, $, commas)

Converts financial columns to numeric

Removes missing values

Drops duplicates

4️⃣ Data Aggregation

Aggregates sales data by date for time-series analysis.

5️⃣ Export Clean Dataset

Users can download a cleaned CSV ready for forecasting models like Prophet.

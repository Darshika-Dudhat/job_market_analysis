import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("./pre_processed_data.csv")

# Convert date column to datetime format
df["published_date"] = pd.to_datetime(df["published_date"])
df["month_year"] = df["published_date"].dt.to_period("M")  # Extract month-year

# Count job postings per month per category
monthly_trends = df.groupby(["month_year", "final_category"])["title"].count().reset_index()

# Streamlit App Setup
st.title("Job Market Trends Dashboard")

# Dropdown for selecting a month
selected_month = st.selectbox("Select Month:", monthly_trends["month_year"].astype(str).unique())

# Filter data for selected month
filtered_data = monthly_trends[monthly_trends["month_year"].astype(str) == selected_month]

# Display data
st.write("### Job Market Trends for", selected_month)
st.dataframe(filtered_data)

# Plot job category trends
st.bar_chart(filtered_data.set_index("final_category")["title"])

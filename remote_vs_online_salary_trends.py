import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("all_upwork_jobs_2024-02-07-2024-03-24.csv")

# Convert date column to datetime format
df["published_date"] = pd.to_datetime(df["published_date"])
df["month_year"] = df["published_date"].dt.to_period("M")  # Extract month-year

# Identify remote jobs based on title keyword
remote_jobs = df[df["title"].str.contains("remote", case=False, na=False)]

# Calculate average hourly rate for remote & all jobs
df["average_pay"] = (df["hourly_low"] + df["hourly_high"]) / 2
remote_jobs["average_pay"] = (remote_jobs["hourly_low"] + remote_jobs["hourly_high"]) / 2

# Monthly salary trends for remote jobs
remote_salary_trend = remote_jobs.groupby("month_year")["average_pay"].mean().reset_index()

# Monthly salary trends for all jobs
total_salary_trend = df.groupby("month_year")["average_pay"].mean().reset_index()

# Merge for comparison
salary_comparison = total_salary_trend.merge(remote_salary_trend, on="month_year", suffixes=("_all_jobs", "_remote"))

# Streamlit UI
st.title("Job Market Trends Dashboard")

# Dropdown for selecting a month
selected_month = st.selectbox("Select Month:", salary_comparison["month_year"].astype(str).unique())

# Filter data for selected month
filtered_salary = salary_comparison[salary_comparison["month_year"].astype(str) == selected_month]

# Display data
st.write(f"### Salary Comparison for {selected_month}")
st.dataframe(filtered_salary)

# Plot salary trends
st.write("### Remote vs. Onsite Salary Trends")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(salary_comparison["month_year"].astype(str), salary_comparison["average_pay_all_jobs"], 
        marker="o", linestyle="dashed", color="gray", label="All Jobs Salary")

ax.plot(salary_comparison["month_year"].astype(str), salary_comparison["average_pay_remote"], 
        marker="o", linestyle="solid", color="blue", label="Remote Jobs Salary")


# Improve readability
ax.set_xlabel("Month-Year", fontsize=12)
ax.set_ylabel("Average Pay (USD)", fontsize=12)
ax.set_title("Remote vs. Onsite Salary Trends", fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)

st.pyplot(fig)

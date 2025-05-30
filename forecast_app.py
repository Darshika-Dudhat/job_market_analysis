import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load forecast data
future_trends = pd.read_csv("./future_job_demand_predictions.csv", index_col=0, parse_dates=True)

if future_trends.empty:
    st.error("⚠️ No data available! Check your dataset.")
else:
    st.write("✅ Data successfully loaded!")

# Streamlit UI
st.title("📊 Future Job Market Trends")

# Dropdown for selecting a category
selected_category = st.selectbox("Select Job Category:", future_trends.columns)

# Display data for selected category
st.write(f"### Future Demand for {selected_category}")
st.line_chart(future_trends[selected_category])

# Insights section
st.write("### 📑 Predictive Analytics Report")
# Re-save the file with UTF-8 encoding
with open("job_market_predictions.txt", "r", encoding="charmap") as file:
    report_text = file.read()

with open("job_market_predictions.txt", "w", encoding="utf-8") as file:
    file.write(report_text)

st.text(report_text)

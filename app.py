from pathlib import Path
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parent
DATA=ROOT/"data"/"retail_sales_eda.csv"
OUT=ROOT/"outputs"
st.set_page_config(page_title="Thiranex Task 3 | EDA",page_icon="📊",layout="wide")
st.title("Exploratory Data Analysis (EDA) Project")
st.caption("Thiranex Data Science Internship — Task 3")
st.warning("This demo uses a synthetic sample retail dataset, not official Thiranex data.")
df=pd.read_csv(DATA,parse_dates=["Order_Date"])
a,b,c,d=st.columns(4)
a.metric("Rows",len(df)); b.metric("Columns",len(df.columns))
c.metric("Missing cells",int(df.isna().sum().sum())); d.metric("Duplicate rows",int(df.duplicated().sum()))
st.subheader("Dataset Preview"); st.dataframe(df.head(20),use_container_width=True)
st.subheader("Statistical Summary"); st.dataframe(df.select_dtypes(include="number").describe().round(2),use_container_width=True)
for filename,title in [("revenue_by_category.png","Revenue by Category"),("revenue_by_region.png","Revenue by Region"),("monthly_revenue_trend.png","Monthly Revenue Trend"),("revenue_distribution.png","Revenue Distribution"),("correlation_heatmap.png","Correlation Heatmap")]:
    st.subheader(title); st.image(str(OUT/filename),use_container_width=True)
st.subheader("EDA Report"); st.text((OUT/"eda_report.txt").read_text(encoding="utf-8"))
st.info("If your internship provided an official dataset, replace the sample CSV and rerun the analysis.")

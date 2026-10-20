from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/"data"/"retail_sales_eda.csv"
OUT=ROOT/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(DATA,parse_dates=["Order_Date"])
print("Shape:",df.shape)
print("\nMissing values:\n",df.isna().sum())
print("\nDuplicates:",df.duplicated().sum())
eda=df.copy()
for c in ["Unit_Price","Units_Sold","Revenue","Cost","Profit"]:
    eda[c]=eda[c].fillna(eda[c].median())
eda["Region"]=eda["Region"].fillna("Unknown")
num=["Units_Sold","Unit_Price","Discount","Revenue","Cost","Profit","Customer_Count"]
print("\nStatistical summary:\n",eda[num].describe().round(2))
corr=eda[num].corr()
print("\nCorrelation matrix:\n",corr.round(3))
corr.to_csv(OUT/"correlation_matrix.csv")
eda.groupby("Category")["Revenue"].sum().sort_values().plot(kind="bar",figsize=(8,5))
plt.title("Total Revenue by Category"); plt.tight_layout(); plt.savefig(OUT/"revenue_by_category.png",dpi=150); plt.close()
eda.groupby("Region")["Revenue"].sum().sort_values().plot(kind="bar",figsize=(8,5))
plt.title("Total Revenue by Region"); plt.tight_layout(); plt.savefig(OUT/"revenue_by_region.png",dpi=150); plt.close()
eda["Month"]=eda["Order_Date"].dt.to_period("M").astype(str)
eda.groupby("Month")["Revenue"].sum().plot(kind="line",marker="o",figsize=(10,5))
plt.xticks(rotation=45); plt.title("Monthly Revenue Trend"); plt.tight_layout(); plt.savefig(OUT/"monthly_revenue_trend.png",dpi=150); plt.close()
eda["Revenue"].plot(kind="hist",bins=25,figsize=(8,5)); plt.title("Revenue Distribution")
plt.tight_layout(); plt.savefig(OUT/"revenue_distribution.png",dpi=150); plt.close()
print("EDA outputs saved in outputs/")

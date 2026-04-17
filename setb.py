import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# Q1: RETAIL SALES DATA
# ============================================

data = {
    "Product": [" Laptop ", "Shirt", "Mobile", "Laptop", None],
    "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing"],
    "Price": [50000, 2000, np.nan, 52000, 3000],
    "Quantity": [2, np.nan, 5, 1, 3]
}

df1 = pd.DataFrame(data)

# a) Handle missing values
df1["Price"].fillna(df1["Price"].median(), inplace=True)
df1["Quantity"].fillna(df1["Quantity"].median(), inplace=True)
df1["Product"].fillna(df1["Product"].mode()[0], inplace=True)
df1["Category"].fillna(df1["Category"].mode()[0], inplace=True)

# b) String operations
df1["Product"] = df1["Product"].str.strip().str.lower()
df1["Product_prefix"] = df1["Product"].str[:3]

# c) Data wrangling
df1["Total_Sales"] = df1["Price"] * df1["Quantity"]
sales_by_category = df1.groupby("Category")["Total_Sales"].sum()

print("\n===== Q1 OUTPUT =====")
print("\nCleaned Data:\n", df1)
print("\nSales by Category:\n", sales_by_category)


# ============================================
# Q2: MULTI-LEVEL GROUPING + PIVOT
# ============================================

data2 = {
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Product_Category": ["Electronics", "Clothing", "Electronics", "Grocery", "Clothing", "Electronics"],
    "Sales": [20000, 15000, 30000, 25000, 18000, 22000],
    "Quantity": [5, 3, 7, 6, 4, 5]
}

df2 = pd.DataFrame(data2)

# a) Multi-level grouping
grouped = df2.groupby(["Region", "Product_Category"]).agg({
    "Sales": "sum",
    "Quantity": "sum"
})

# b) Aggregations
print("\n===== Q2 OUTPUT =====")
print("\nMulti-level Grouping:\n", grouped)

# c) Pivot table
pivot = pd.pivot_table(
    df2,
    values="Sales",
    index="Region",
    columns="Product_Category",
    aggfunc="sum"
)

print("\nPivot Table:\n", pivot)


# ============================================
# Q3: DASHBOARD (4 VISUALS)
# ============================================

df3 = df2.copy()

print("\n===== Q3 OUTPUT =====")

# Visual 1: Sales by Region
plt.figure()
df3.groupby("Region")["Sales"].sum().plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Visual 2: Sales by Category
plt.figure()
df3.groupby("Product_Category")["Sales"].sum().plot(kind='bar')
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Visual 3: Sales vs Quantity
plt.figure()
plt.scatter(df3["Sales"], df3["Quantity"])
plt.title("Sales vs Quantity")
plt.xlabel("Sales")
plt.ylabel("Quantity")
plt.show()

# Visual 4: Sales Trend
plt.figure()
df3["Sales"].plot(kind='line')
plt.title("Sales Trend")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()


# ============================================
# Q3(b): TRENDS
# ============================================

print("\nTrends:")
print("1. Electronics category shows higher sales compared to others.")
print("2. North and East regions contribute significantly to total sales.")

# ============================================
# Q3(c): INSIGHTS
# ============================================

print("\nInsights:")
print("1. Increasing focus on Electronics can boost revenue.")
print("2. Regions with lower sales (like South/West) need targeted strategies.")
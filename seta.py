import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================================
# Q1: CUSTOMER DATA
# ================================

customer_data = {
    "Name": ["Alice", "Bob", None, "David", "Eva"],
    "Email": ["alice@gmail.com", "bob@yahoo.com", "charlie@hotmail.com", None, "eva@gmail.com"],
    "Age": [25, np.nan, 30, 22, np.nan],
    "City": ["Mumbai", "Delhi", "Mumbai", None, "Delhi"],
    "Income": [50000, 60000, np.nan, 45000, 70000]
}

df1 = pd.DataFrame(customer_data)

# Handle missing values
df1["Name"].fillna("Unknown", inplace=True)
df1["Email"].fillna("noemail@gmail.com", inplace=True)
df1["Age"].fillna(df1["Age"].mean(), inplace=True)
df1["City"].fillna(df1["City"].mode()[0], inplace=True)
df1["Income"].fillna(df1["Income"].mean(), inplace=True)

# String manipulation
df1["Name"] = df1["Name"].str.upper()
df1["Domain"] = df1["Email"].str.split("@").str[1]

# Data wrangling
avg_income_city = df1.groupby("City")["Income"].mean()
overall_avg = df1["Income"].mean()
high_income = df1[df1["Income"] > overall_avg]

print("\n===== Q1 OUTPUT =====")
print("\nCleaned Data:\n", df1)
print("\nAverage Income by City:\n", avg_income_city)
print("\nHigh Income Customers:\n", high_income)


# ================================
# Q2: SALES DATA
# ================================

sales_data = {
    "Product_ID": ["P101", "P102", "P103", "P104", "P105"],
    "Category": ["Electronics", "Clothing", "Electronics", "Grocery", "Clothing"],
    "Price": [15000, 2000, np.nan, 500, 3000],
    "Quantity": [10, np.nan, 5, 20, 15],
    "Discount": [5, 10, 8, np.nan, 12]
}

df2 = pd.DataFrame(sales_data)

# Handle missing values (Forward Fill + Backward Fill)
df2.fillna(method='ffill', inplace=True)
df2.fillna(method='bfill', inplace=True)

# Min-Max Normalization
df2["Price_norm"] = (df2["Price"] - df2["Price"].min()) / (df2["Price"].max() - df2["Price"].min())
df2["Quantity_norm"] = (df2["Quantity"] - df2["Quantity"].min()) / (df2["Quantity"].max() - df2["Quantity"].min())

# Revenue calculation
df2["Revenue"] = df2["Price"] * df2["Quantity"] * (1 - df2["Discount"]/100)

print("\n===== Q2 OUTPUT =====")
print("\nProcessed Sales Data:\n", df2)


# ================================
# Q3: BASIC VISUALIZATION (instead of Power BI)
# ================================

# Sample dataset
sales_perf = {
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Sales": [200, 150, 300, 250, 400, 350],
    "Profit": [20, 15, 40, 30, 50, 45]
}

df3 = pd.DataFrame(sales_perf)

print("\n===== Q3 OUTPUT =====")

# Filter example (Region = North)
filtered_df = df3[df3["Region"] == "North"]
print("\nFiltered Data (Region = North):\n", filtered_df)

# Visualization 1: Bar Chart
plt.figure()
df3.groupby("Region")["Sales"].sum().plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Visualization 2: Line Chart
plt.figure()
df3["Sales"].plot(kind='line')
plt.title("Sales Trend")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()

# Visualization 3: Scatter Plot
plt.figure()
plt.scatter(df3["Sales"], df3["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
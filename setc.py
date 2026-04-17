import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================
# Q1: STUDENT MARKS DATASET
# ============================================

data1 = {
    "Full_Name": ["John Doe", "Alice Smith", "Bob Lee", "Chris Evans", "Emma Watson"],
    "Department": ["cse", "CSE", "ece", "ECE", "cse"],
    "Maths": [80, 90, np.nan, 70, 85],
    "Science": [75, np.nan, 65, 80, 90],
    "English": [85, 88, 78, np.nan, 92]
}

df1 = pd.DataFrame(data1)

# a) Replace missing marks with subject-wise average
for col in ["Maths", "Science", "English"]:
    df1[col].fillna(df1[col].mean(), inplace=True)

# b) String manipulations
# i) Split full name
df1[["First_Name", "Last_Name"]] = df1["Full_Name"].str.split(" ", expand=True)

# ii) Standardize department names
df1["Department"] = df1["Department"].str.upper()

# c) Data wrangling
# i) Pivot (subjects vs marks)
pivot_df = df1.melt(
    id_vars=["Full_Name"],
    value_vars=["Maths", "Science", "English"],
    var_name="Subject",
    value_name="Marks"
)

# ii) Rank students based on total marks
df1["Total"] = df1[["Maths", "Science", "English"]].sum(axis=1)
df1["Rank"] = df1["Total"].rank(ascending=False)

print("\n===== Q1 OUTPUT =====")
print("\nProcessed Data:\n", df1)
print("\nPivot Table:\n", pivot_df)


# ============================================
# Q2: CUSTOMER ORDER DATA
# ============================================

data2 = {
    "Customer_Name": ["john doe", "Alice Smith", None, "Bob Lee", "Emma Watson"],
    "City": ["mumbai", "Delhi", "Chennai", None, "Delhi"],
    "Price": [1000, 2000, np.nan, 1500, 2500],
    "Quantity": [2, np.nan, 3, 1, 4],
    "Order_Date": ["2023-01-10", "2023-02-15", "2023-03-20", "2023-04-25", "2023-05-30"]
}

df2 = pd.DataFrame(data2)

# a) Handle missing values
df2["Price"].fillna(df2["Price"].mean(), inplace=True)
df2["Quantity"].fillna(df2["Quantity"].median(), inplace=True)
df2["Customer_Name"].fillna(df2["Customer_Name"].mode()[0], inplace=True)

# b) Standardize fields
df2["Customer_Name"] = df2["Customer_Name"].str.title()
df2["City"] = df2["City"].fillna(df2["City"].mode()[0]).str.title()

df2["Order_Date"] = pd.to_datetime(df2["Order_Date"])

# c) Create new features
df2["Total_Amount"] = df2["Price"] * df2["Quantity"]
df2["Order_Year"] = df2["Order_Date"].dt.year

print("\n===== Q2 OUTPUT =====")
print("\nProcessed Order Data:\n", df2)


# ============================================
# Q3: DASHBOARD (3 VISUALS + SORT + FILTER)
# ============================================

df3 = df2.copy()

print("\n===== Q3 OUTPUT =====")

# Filter example (Region not given → using City as proxy)
filtered_df = df3[df3["City"] == "Delhi"]
print("\nFiltered Data (City = Delhi):\n", filtered_df)

# Visual 1: Total Sales by City
plt.figure()
df3.groupby("City")["Total_Amount"].sum().plot(kind='bar')
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

# Visual 2: Sales Trend (Sorted)
plt.figure()
df3_sorted = df3.sort_values(by="Total_Amount", ascending=False)
df3_sorted["Total_Amount"].plot(kind='line')
plt.title("Sorted Sales Trend")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()

# Visual 3: Quantity vs Price
plt.figure()
plt.scatter(df3["Price"], df3["Quantity"])
plt.title("Price vs Quantity")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.show()
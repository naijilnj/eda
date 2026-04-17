# ================================
# Activity - 1 (EDA + Visualization)
# ================================

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("EDA.csv")

# Basic Info
print("Head:\n", data.head())
print("\nShape:", data.shape)
print("\nData Types:\n", data.dtypes)

# Separate Columns
categorical_cols = data.select_dtypes(include=['object']).columns
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

print("\nCategorical Columns:", categorical_cols)
print("Numerical Columns:", numerical_cols)

# Duplicate Check
print("\nDuplicate Rows:", data.duplicated().sum())

# Handle Missing Values
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'].fillna(data['TotalCharges'].median(), inplace=True)

print("\nMissing Values in TotalCharges:", data['TotalCharges'].isnull().sum())

# Unique Values in Categorical Columns
for col in categorical_cols:
    print("\nColumn:", col)
    print(data[col].unique())
    print("-" * 40)

# Replace Values (Example)
data['Churn'] = data['Churn'].replace({'No': 0, 'Yes': 1})

# Summary Statistics
print("\nMean Values:\n", data[['tenure', 'MonthlyCharges', 'TotalCharges']].mean())

# Value Counts (Percentage)
print("\nPayment Method Distribution (%):\n",
      data['PaymentMethod'].value_counts(normalize=True) * 100)

# Crosstab
print("\nCrosstab:\n",
      pd.crosstab(data['InternetService'], data['Churn']))

# ================================
# Visualization
# ================================

# 1. Tenure Distribution
plt.figure()
plt.hist(data['tenure'], bins=10)
plt.xlabel("Tenure")
plt.ylabel("Frequency")
plt.title("Distribution of Tenure")
plt.show()

# 2. Monthly Charges Distribution
plt.figure()
plt.hist(data['MonthlyCharges'], bins=10)
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.title("Distribution of Monthly Charges")
plt.show()

# 3. Churn Count Plot
sns.countplot(x='Churn', data=data)
plt.title("Churn Count")
plt.show()

# 4. Payment Method vs Churn
pd.crosstab(data['PaymentMethod'], data['Churn']).plot(
    kind='bar', stacked=True, figsize=(8,5)
)
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.title("Payment Method vs Churn")
plt.show()
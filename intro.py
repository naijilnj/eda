# Experiment 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("salary.csv")

# View first few rows
print(df.head())

# Check data types
print(df.dtypes)

# Access Salary column type
print(type(df['Salary']))

# Dataset info
print(df.info())

# Describe dataset
print(df.describe())

# Standard deviation of Salary
print(df['Salary'].std())

# Mean of Age
print(df['Age'].mean())

# Describe Salary separately
print(df['Salary'].describe())

# Count of Salary values
print(df['Salary'].count())

# Mean Salary
print(df['Salary'].mean())

# Group by Age and find mean Salary
print(df.groupby('Age')[['Salary']].mean())

# Filter rows where Salary > 2000
print(df[df['Salary'] > 2000].head())

# Select specific columns
print(df[['Name', 'Age', 'Job', 'Salary']])

# Row slicing
print(df[10:20])

# iloc examples
print(df.iloc[10:13][['Age', 'Salary']])
print(df.iloc[10:13, [0, 1, 2]])

# Another iloc example
print(df.iloc[2:3, [1, 4]])

# Filter where Job = Dentist
print(df[df['Job'] == 'Dentist'].head())

# Check missing values (column-wise)
print(df.isnull().sum())

# Check missing values (row-wise)
print(df.isnull().sum(axis=1).head(2))

# Total missing values
print(df.isnull().sum().sum())
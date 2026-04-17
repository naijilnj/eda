# ================================
# COMBINED FILE - All Codes
# ================================

# ================================
# EXPERIMENT 1 - INTRO
# ================================

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


# ================================
# VISUALIZATION
# ================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("salary.csv")

# -------------------------------
# 1. BOX PLOT (Salary - first 10 values)
# -------------------------------
sns.boxplot(df['Salary'].head(10))
plt.title("Boxplot with 10 values")
plt.xlabel("Salary")
plt.show()

# -------------------------------
# 2. BOX PLOT (Using iloc subset)
# -------------------------------
sns.boxplot(df['Salary'].iloc[1:3])
plt.title("Boxplot with index range")
plt.xlabel("Salary")
plt.show()

# -------------------------------
# 3. VIOLIN PLOT (Age)
# -------------------------------
sns.violinplot(df['Age'], palette='green')
plt.title("Violin Plot")
plt.xlabel("Age")
plt.show()

# -------------------------------
# 4. VIOLIN PLOT (Salary vs Job)
# -------------------------------
sns.violinplot(x='Job', y='Salary', data=df, palette='green')
plt.title("Violin Plot")
plt.xlabel("Job")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 5. VIOLIN PLOT (All numeric columns)
# -------------------------------
sns.violinplot(data=df)
plt.title("Violin plot for numerical cols")
plt.tight_layout()
plt.show()

# -------------------------------
# 6. JOINT PLOT (Age vs Salary)
# -------------------------------
sns.jointplot(x='Age', y='Salary', data=df)
plt.title("Joint Plot")
plt.show()

# -------------------------------
# 7. PIE CHART (Age)
# -------------------------------
plt.pie(df['Age'])
plt.title("Pie Chart")
plt.tight_layout()
plt.show()

# -------------------------------
# 8. HISTOGRAM (Salary)
# -------------------------------
plt.hist(df['Salary'], bins=10, color='blue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 9. BOX PLOT (Salary - again)
# -------------------------------
sns.boxplot(df['Salary'])
plt.title("Boxplot")
plt.xlabel("Salary")
plt.show()

# -------------------------------
# 10. SCATTER PLOT (Age vs Salary)
# -------------------------------
sns.scatterplot(x=df['Age'], y=df['Salary'])
plt.title("Scatter plot")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# -------------------------------
# 11. BAR GRAPH (Job vs Salary)
# -------------------------------
plt.bar(df['Job'], df['Salary'], color='green', edgecolor='black')
plt.title("Bar Graph")
plt.show()


# ================================
# FILE OPERATIONS
# ================================

# ================================
# 1. Exploring File Types
# ================================
fo = open("fo.txt", "wb")
print("File Name:", fo.name)
print("Is Closed:", fo.closed)
print("Mode:", fo.mode)
fo.close()


# ================================
# 2. Write and Read Text File
# ================================
file = open("sample.txt", "w")
file.write("EDA is good\nAll are good")
file.close()

file = open("sample.txt", "r")
print("\nFile Content:\n", file.read())
file.close()


# ================================
# 3. Pickle (Binary Storage)
# ================================
import pickle

data_pickle = [1, 2, 3, 4]

with open("data.pkl", "wb") as file:
    pickle.dump(data_pickle, file)

with open("data.pkl", "rb") as file:
    print("\nPickle Data:", pickle.load(file))


# ================================
# 4. API Request
# ================================
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print("\nAPI Status Code:", response.status_code)

response2 = requests.get("http://api.open-notify.org/astros")
print("API JSON Response:", response2.json())


# ================================
# 5. JSON Read & Write
# ================================
import json

data_json = {
    "Name": "Naijil",
    "Age": 21,
    "City": "Mumbai"
}

with open("data.json", "w") as file:
    json.dump(data_json, file)

with open("data.json", "r") as file:
    print("\nJSON Data:", json.load(file))


# ================================
# 6. Pandas DataFrame & CSV
# ================================
import pandas as pd

data_pd = {
    "Name": ["A", "B", "C"],
    "Age": [10, 20, 30],
    "Job": ["Accountant", "CEO", "Marketing"],
    "Salary": [50000, 100000, 60000]
}

df = pd.DataFrame(data_pd)
df.to_csv("sample.csv", index=False)

df_read = pd.read_csv("sample.csv")
print("\nCSV Data:\n", df_read)


# ================================
# 7. CSV to Excel
# ================================
df.to_excel("sample.xlsx", sheet_name="Data", index=False)

df_excel = pd.read_excel("sample.xlsx")
print("\nExcel Data:\n", df_excel)


# ================================
# 8. Dictionary Example
# ================================
people = [
    {"id": 1, "name": "Gaurav"},
    {"id": 2, "name": "Nikola"},
    {"id": 3, "name": "Priyog"}
]

print("\nPeople Data:")
for person in people:
    print(person["id"], person["name"])


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
# Visualization (Activity 1)
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


# ================================
# WEB SCRAPING & API
# ================================

# ================================
# Activity - 2 (API + Web Scraping)
# ================================

# Import Libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# ================================
# API Requests (CRUD Operations)
# ================================

# GET Request
get_resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET Response:", get_resp.json())

# POST Request
post_resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"id": 1, "title": "Hello", "body": "World"}
)
print("\nPOST Response:", post_resp.json())

# PUT Request
put_resp = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"id": 1, "title": "Updated", "body": "Updated Body"}
)
print("\nPUT Response:", put_resp.json())

# DELETE Request
delete_resp = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("\nDELETE Status Code:", delete_resp.status_code)

# HEAD Request
head_resp = requests.head("https://jsonplaceholder.typicode.com/posts/1")
print("\nHEAD Headers:", head_resp.headers)


# ================================
# Convert DataFrame to CSV
# ================================
# (Assuming filtered_data already exists)

df = pd.DataFrame(filtered_data)
df.to_csv("filtered_data.csv", index=False)


# ================================
# Web Scraping using BeautifulSoup - Midterm
# ================================

# Fetch Webpage
response = requests.get("https://www.geeksforgeeks.org/java/java/")
soup = BeautifulSoup(response.content, "html.parser")

# Pretty Print HTML
print("\nParsed HTML:\n", soup.prettify())

# Extract Article Content
content = soup.find("div", class_="article-content")

if content:
    for para in content.find_all("p"):
        print(para.text.strip())
else:
    print("No article content found")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# -------------------------------
# 1. Send Request
# -------------------------------
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# -------------------------------
# 2. Parse HTML
# -------------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------
# 3. Extract Data
# -------------------------------
quotes = []
authors = []
tags_list = []

items = soup.find_all("div", class_="quote")

for item in items:
    # Quote text
    quote = item.find("span", class_="text").text
    
    # Author
    author = item.find("small", class_="author").text
    
    # Tags
    tags = [tag.text for tag in item.find_all("a", class_="tag")]
    tags = ", ".join(tags)
    
    quotes.append(quote)
    authors.append(author)
    tags_list.append(tags)

# -------------------------------
# 4. Create DataFrame
# -------------------------------
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags_list
})

# -------------------------------
# 5. Data Cleaning
# -------------------------------

# Remove special quotes (“ ”)
df["Quote"] = df["Quote"].apply(lambda x: re.sub(r'[“”"]', '', x))

# Remove extra spaces
df["Quote"] = df["Quote"].str.strip()

# Clean author names
df["Author"] = df["Author"].str.strip()

# -------------------------------
# 6. Save to CSV
# -------------------------------
df.to_csv("quotes_data.csv", index=False)

# -------------------------------
# 7. Output
# -------------------------------
print(df.head())



# ================================
# OUTLIER DETECTION
# ================================

# ==========================================
# Outlier Detection using Python (All Methods)
# ==========================================

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. IQR Method
# ==========================================
data = {'Marks': [45, 50, 52, 48, 47, 90, 49, 46, 51, 44]}
df = pd.DataFrame(data)

# Boxplot
sns.boxplot(y=df['Marks'])
plt.title("Boxplot for Marks")
plt.show()

# IQR Calculation
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
df_clean_iqr = df[(df['Marks'] >= lower) & (df['Marks'] <= upper)]
print("IQR Cleaned Data:\n", df_clean_iqr)


# ==========================================
# 2. Z-Score Method
# ==========================================
data = {'Values': [12, 15, 14, 10, 9, 100, 8, 13, 10, 14, 11, 10]}
df = pd.DataFrame(data)

mean = df['Values'].mean()
std = df['Values'].std()

df['Z_score'] = (df['Values'] - mean) / std

# Keep data within threshold
df_clean_z = df[np.abs(df['Z_score']) <= 2]
print("\nZ-Score Cleaned Data:\n", df_clean_z)


# ==========================================
# 3. Scatter Plot (Before Cleaning)
# ==========================================
plt.scatter(range(len(df)), df['Values'])
plt.title("Original Scatter Plot")
plt.show()


# ==========================================
# 4. Grubbs Test (Outlier Detection)
# ==========================================
from scipy.stats import t

def grubbs_test(data, alpha=0.05):
    data = np.array(data)
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)

    G = np.max(np.abs(data - mean)) / std

    t_crit = t.ppf(1 - alpha/(2*n), n-2)
    G_crit = ((n-1)/np.sqrt(n)) * np.sqrt(t_crit**2 / (n-2 + t_crit**2))

    return G > G_crit

data_grubbs = np.array([5,14,15,15,14,19,17,16,20,22,28,21,28,11,9,20,40])
print("\nGrubbs Test Outlier Exists:", grubbs_test(data_grubbs))


# ==========================================
# 5. Mahalanobis Distance
# ==========================================
data = {
    'Feature1': [10,12,10,14,10,20,100],
    'Feature2': [20,24,20,28,22,30,110]
}

df = pd.DataFrame(data)

mean = df.mean()
cov = np.cov(df.values.T)
inv_cov = np.linalg.inv(cov)

distances = []

for row in df.values:
    diff = row - mean
    dist = np.sqrt(np.dot(np.dot(diff, inv_cov), diff.T))
    distances.append(dist)

df['Mahalanobis'] = distances

threshold = np.percentile(distances, 95)
df['Outlier'] = df['Mahalanobis'] > threshold

print("\nMahalanobis Outliers:\n", df)


# ==========================================
# 6. Isolation Forest
# ==========================================
from sklearn.ensemble import IsolationForest
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
X = iris.data[['sepal length (cm)', 'sepal width (cm)']]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

pred = model.predict(X)

# Outliers = -1
outliers = X[pred == -1]

plt.scatter(X.iloc[:,0], X.iloc[:,1])
plt.scatter(outliers.iloc[:,0], outliers.iloc[:,1])
plt.title("Isolation Forest Outliers")
plt.show()


#Local

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import LocalOutlierFactor

iris = load_iris(as_frame=True)
X = iris.data[['sepal length (cm)', 'sepal width (cm)']]

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outlier_labels = lof.fit_predict(X)
scores = lof.negative_outlier_factor_
outliers = np.where(outlier_labels == -1)[0]

plt.figure(figsize=(10, 6))
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], color='green', label='Normal Data')
plt.scatter(X.iloc[outliers, 0], X.iloc[outliers, 1],
            color='red', label='Outliers')

plt.xlabel('Sepal Length (cm)', fontsize=13)
plt.ylabel('Sepal Width (cm)', fontsize=13)
plt.title('Anomaly Detection using Local Outlier Factor', fontsize=16)
plt.legend()
plt.show()
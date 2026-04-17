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


#local

import pandas as pd
import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

data = {
    'Feature1': [10, 12, 10, 14, 10, 20, 100],
    'Feature2': [20, 24, 20, 28, 22, 30, 110],
    'Feature3': [5, 6, 5, 7, 5, 10, 50]
}

df = pd.DataFrame(data)
def mahalnobis_outlier_detection(df,confidence_level =0.95):
    mean_vector = df.mean().values
    cov_matrix = np.cov(df.values,rowvar = False)
    inv_cov_matrix = np.linalg.pinv(cov_matrix)
    distances = []
    for row in df.values:
        diff = row - mean_vector
        md = np.sqrt(diff.T@inv_cov_matrix@diff)
        distances.append(md)
    df_result = df.copy()
    df_result['Mahalnobis_Distance'] = distances
    df_degree = df.shape[1]
    threshold = np.sqrt(chi2.ppf(confidence_level,df=df_degree))
    df_result['outlier'] =  df_result['Mahalnobis_Distance'] > threshold
    return df_result,threshold
df_result,threshold = mahalnobis_outlier_detection(df)
print(df_result)
print(df_result[df_result['outlier']])
plt.figure()
plt.scatter(range(len(df_result)),   df_result['Mahalnobis_Distance'], label='Distance')

plt.axhline(threshold, linestyle='--', label='Threshold')
plt.title("Mahalanobis Distance Outlier Detection")
plt.xlabel("Index")
plt.ylabel("Mahalanobis Distance")
plt.legend()
plt.grid(True)
plt.show()
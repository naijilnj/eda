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
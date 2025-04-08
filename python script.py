# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
df = pd.read_csv('walmart_sales.csv')

df.shape

# Info about columns and types
df.info()

# Summary statistics
df.describe()

# Check for missing values
df.isnull().sum()

# Unique values per column
df.nunique()
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


# Optional renaming
df.rename(columns={'Weekly_Sales': 'WeeklySales'}, inplace=True)

plt.figure(figsize=(14, 6))
df.groupby('Date')['WeeklySales'].sum().plot()
plt.title('Total Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
#Sales by store
plt.figure(figsize=(10,5))
df.groupby('Store')['WeeklySales'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title('Total Sales by Store')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
#Holiday vs Non Holiday sales
sns.boxplot(x='Holiday_Flag', y='WeeklySales', data=df)
plt.title('Sales Distribution: Holiday vs Non-Holiday Weeks')
import os


os.makedirs('data/cleaned', exist_ok=True)


df.to_csv('data/cleaned/walmart_sales_cleaned.csv', index=False)






# %%
df.head()
df['Store'].unique()
df.head()
df.index


# %%
import sqlite3

# Connect to SQLite (or create one)
conn = sqlite3.connect('walmart_sales.db')

# Push DataFrame into a SQL table
df.to_sql('sales', conn, if_exists='replace', index=False)

# Query example
query = """
SELECT Store, AVG(WeeklySales) as AvgSales
FROM sales
GROUP BY Store
ORDER BY AvgSales DESC
"""
pd.read_sql_query(query, conn)




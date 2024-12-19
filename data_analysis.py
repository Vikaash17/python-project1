import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sales_data.csv')
print(df.head())

# Perform data manipulation
# Example: Filtering data
filtered_df = df[df['sales'] > 1000]
print(filtered_df)

# Example: Grouping data
grouped_df = df.groupby('region').sum()
print(grouped_df)

# Example: Aggregating data
average_sales = df['sales'].mean()
print(average_sales)

# Data visualization using Matplotlib
plt.plot(df['date'], df['sales'])
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Data visualization using Seaborn
sns.barplot(x='region', y='sales', data=df)
plt.title('Sales by Region')
plt.show()
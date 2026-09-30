# 1. Data Loading & Understanding

# Import data
import pandas as pd
import matplotlib.pyplot as plt
Data_set = pd.read_csv('C:/Users/DAVE/Downloads/amazon_sales_dataset.csv')

# View data
print(Data_set.head())
print(Data_set.tail())

#Shape of dataset
print(Data_set.shape)

# Column names
Data_set.columns

# Data types
Data_set.info()

# 2. Data Cleaning


# Check missing values
print(Data_set.isnull().sum())

# Check duplicates
print(Data_set.duplicated().sum())


#Convert date column
Data_set['order_date'] = pd.to_datetime(Data_set['order_date'])
print(Data_set['order_date'].head())


# Convert numeric columns
Data_set['sales'] = pd.to_numeric(Data_set['total_revenue'])
Data_set['quantity'] = pd.to_numeric(Data_set['quantity_sold'])

# 3.EDA QUESTIONS

#Overall Sales Performance: What is the total sales, total profit, and total quantity sold?
total_sales = Data_set['total_revenue'].sum()
total_quantity = Data_set['quantity_sold'].sum()

print(round(total_sales,2), total_quantity)

# Sales Trend Over Time: How do sales change over time (monthly or yearly trend)?
# Extract Year

   #Extract Year
# Convert to datetime (just in case)
Data_set['order_date'] = pd.to_datetime(Data_set['order_date'])

# Extract Month-Year
Data_set['Month'] = Data_set['order_date'].dt.to_period('M')

# Aggregate monthly sales
monthly_sales = Data_set.groupby('Month')['total_revenue'].sum()

# Convert index to string for better plotting
monthly_sales.index = monthly_sales.index.astype(str)

# Plot
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Monthly Sales Trend')

plt.tight_layout()
print(plt.show())

#Category Performance: Which product categories generate the highest sales and profit?
Top_Category = Data_set.groupby('product_category')[['total_revenue']].sum().sort_values(by='total_revenue', ascending=False)
print(Top_Category)

#Regional Performance: Which region performs best in terms of sales and profit?
import matplotlib.pyplot as plt

# Group by region and sum total revenue
Top_Regions = Data_set.groupby('customer_region')['total_revenue'].sum().sort_values(ascending=False)

# Create figure and axis
fig, ax = plt.subplots(figsize=(5,2))

# Plot the bar chart on the axis
Top_Regions.plot(kind='bar', ax=ax)
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)

# Add total revenue values on top of each bar
for i, value in enumerate(Top_Regions):
    ax.text(i, value, f'{value:,.2f}', ha='center', va='bottom')

print(plt.show())

'''7. Customer Purchasing Behavior
 What is the distribution of order quantities?
Do customers tend to buy in small or large quantities?'''

import matplotlib.pyplot as plt

# Count quantity frequency
quantity_counts = Data_set['quantity_sold'].value_counts().sort_index()

plt.figure(figsize=(10,5))

# Plot
ax = quantity_counts.plot(kind='bar')

plt.title('Distribution of Order Quantities')
plt.xlabel('Quantity Sold')
plt.ylabel('Number of Orders')

# 🔥 Add values on top of bars
for i, value in enumerate(quantity_counts):
    ax.text(i, value, str(value), ha='center', va='bottom')

print(plt.show())
print(Data_set['quantity_sold'].describe())

'''8. Relationship Analysis
• What is the relationship between Sales, Quantity, and Profit?
• Use correlation analysis and visualizations.'''

print(Data_set[['total_revenue','quantity_sold']].corr())
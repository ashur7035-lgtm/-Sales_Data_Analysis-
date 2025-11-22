# Sales Analysis
import pandas as pd

df = pd.read_csv('../Datasets/sample_sales_dataset.csv', parse_dates=['order_date'])
# Basic aggregations
sales_by_region = df.groupby('region')['total_price'].sum().reset_index().sort_values('total_price', ascending=False)
sales_by_product = df.groupby('product_id')['total_price'].sum().reset_index().sort_values('total_price', ascending=False)
monthly = df.set_index('order_date').resample('M')['total_price'].sum().reset_index()

print("Top regions by sales:")
print(sales_by_region.head())
print("\nTop products by sales:")
print(sales_by_product.head())
print("\nMonthly sales sample:")
print(monthly.head())
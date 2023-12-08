import pandas as pd

# Read the CSV file into a DataFrame
sales_data = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# List all unique values in the "PRODUCTLINE" column
unique_product_lines = sales_data['PRODUCTLINE'].unique()
print("Unique Product Lines:")
print(unique_product_lines)

# List all unique values in the "CUSTOMERNAME" column
unique_customer_names = sales_data['CUSTOMERNAME'].unique()
print("\nUnique Customer Names:")
print(unique_customer_names)

# Business Analytics Dashboard

This repository contains a Python-based Business Analytics Dashboard that allows users to analyze sales data from a CSV file.

Installation:
1. Clone the repository to your local machine.

2. Ensure you have Python installed.

3. Install required dependencies:
  pip install pandas matplotlib

Usage:
1. Run main.py.

2. Enter the file path to your sales data CSV when prompted.

3. Follow the on-screen instructions to navigate through the dashboard options:

- View Sales Report
- View Sales Trend Over Time

Under "View Sales Report":

- View Total Sales
- View Sales by Region
  - View Sales by State
  - View Sales by Country

Under "View Sales Trend Over Time":

- View Monthly Sales Trend
- View Yearly Sales Trend
- View Quarterly Sales Trend

Functionality:
main.py
- Handles user interactions through a command-line interface.
- Utilizes the SalesData class from sales_data.py to provide different analytics options.

sales_data.py
- Defines the SalesData class responsible for loading and analyzing sales data.

Methods include:
- total_sales(): Calculate total sales revenue.
- sales_by_country(): Calculate sales by country.
- sales_by_state(): Calculate sales by state.
- visualize_month_trends(): Visualize monthly sales trends.
- visualize_yearly_trends(): Visualize yearly sales trends.
- visualize_quarterly_trends(): Visualize quarterly sales trends.

sample data set used:
sales_data_sample.csv 
amazon.csv
source: Kaggle.com

Requirements:
Python 3.x
Pandas
Matplotlib

Contributing:
Contributions are welcome! Feel free to open an issue or create a pull request.

License:
This project is licensed under the MIT License.


import pandas as pd
import matplotlib.pyplot as plt


class SalesData:  #public class SalesData {}

  def __init__(self, file_path):
    self.data = pd.read_csv(file_path, encoding='latin1')
    self.data['ORDERDATE'] = pd.to_datetime(self.data['ORDERDATE'])

  def total_sales(self):  #public double totalSales()
    total_sales_generated = self.data["SALES"].sum()
    return total_sales_generated

  # def product_sales(self):
  #   unique_product_lines = self.data['PRODUCTLINE'].unique()
  #   for product_line in unique_product_lines:
  #     total_product_sales = self.data.groupby(str(product_line))["SALES"].sum()

  def sales_by_country(self):
    sales_by_country_generated = self.data.groupby("COUNTRY")["SALES"].sum()
    return sales_by_country_generated

  def sales_by_state(self):
    sales_by_state_generated = self.data.groupby("STATE")["SALES"].sum()
    return sales_by_state_generated

  def visualize_month_trends(self):
    monthly_sales = self.data.resample('M', on='ORDERDATE')['SALES'].sum()
    plt.plot(monthly_sales)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount ($)")
    plt.title("Monthly Sales Trend")
    plt.show()

  def visualize_yearly_trends(self):
    yearly_sales = self.data.resample('Y', on='ORDERDATE')['SALES'].sum()
    plt.plot(yearly_sales)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount ($)")
    plt.title("Yearly Sales Trend")
    plt.show()

  def visualize_quarterly_trends(self):
    quarterly_sales = self.data.resample('Q', on='ORDERDATE')['SALES'].sum()
    plt.plot(quarterly_sales)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount ($)")
    plt.title("Quarterly Sales Trend")
    plt.show()

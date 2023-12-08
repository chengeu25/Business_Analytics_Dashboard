import pandas as pd
import matplotlib.pyplot as plt


class SalesData:  #public class SalesData {}

  def __init__(self, file_path):
    self.data = pd.read_csv(file_path, encoding='latin1')
    self.data['ORDERDATE'] = pd.to_datetime(self.data['ORDERDATE'])

  def total_sales(self):  #public double totalSales()
    total_sales_generated = self.data["SALES"].sum()
    return total_sales_generated

  def sales_by_country(self):
    sales_by_country_generated = self.data.groupby("COUNTRY")["SALES"].sum()
    return sales_by_country_generated

  def sales_by_state(self):
    sales_by_state_generated = self.data.groupby("STATE")["SALES"].sum()
    return sales_by_state_generated

  def visualize_sales_trends(self):
    monthly_sales = self.data.resample('M', on='ORDERDATE')['SALES'].sum()
    plt.plot(monthly_sales)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount ($)")
    plt.title("Sales Trend Over Time")
    plt.show()

#PRODUCTLINE
#
import pandas as pd
import matplotlib.pyplot as plt

class SalesData: #public class SalesData {}

  def __init__(self, file_path):
    self.data = pd.read_csv(file_path, encoding='latin1')
    self.data['ORDERDATE'] = pd.to_datetime(self.data['ORDERDATE'])
    
  def total_sales(self): #public double totalSales()
    return self.data["PRICEEACH"].sum() #mutiply by number of sales for each item

  def sales_by_region(self):
    return self.data.groupby("STATE")["PRICEEACH"].sum()

  def visualize_sales_trends(self):
    monthly_sales = self.data.resample('M', on = 'ORDERDATE')['SALES'].sum()
    plt.plot(monthly_sales)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount ($)")
    plt.title("Sales Trend Over Time")
    plt.show()
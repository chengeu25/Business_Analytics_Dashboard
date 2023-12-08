import pandas as pd


class SalesData:

  def __init__(self, file_path):
    self.data = pd.read_csv(file_path, encoding='latin1')

  def total_sales(self):
    return self.data["PRICEEACH"].sum()

  def sales_by_region(self):
    return self.data.groupby("STATE")["PRICEEACH"].sum()

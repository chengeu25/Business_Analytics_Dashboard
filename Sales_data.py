import pandas as pd

class SalesData:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def total_sales(self):
        return self.data["Price"].sum()
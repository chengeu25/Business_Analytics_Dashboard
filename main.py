from sales_data import SalesData

data_set = input("Enter file path: ")

def main_menu(input_sales_data):
  print("Welcome to Business Analytics Dashboard")
  print("1. View Sales Report")
  print("2. View Sales by Region")
  choice = input("Enter you choice: ")

  if choice == "1":
    total_sales = input_sales_data.total_sales()
    print(total_sales)
  elif choice == "2":
    region_sales = input_sales_data.sales_by_region()
    print(region_sales)
  else:
    print("invalid choice: please try again")


if __name__ == "__main__":
  sales_data = SalesData(data_set)
  while True:
    main_menu(sales_data)

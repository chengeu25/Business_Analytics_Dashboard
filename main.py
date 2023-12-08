from sales_data import SalesData

data_set = input("Enter file path: ")  #java: StdIn


def main_menu(input_sales_data):
  print("Welcome to Business Analytics Dashboard")
  print("1. View Sales Report")
  print("2. View Sales by Region")
  print("3. View Sales Trend Over Time")
  choice = input("Enter your choice: ")

  if choice == "1":
    total_sales = input_sales_data.total_sales()
    print("\n\ntotal sales/revenue is: $" + str(total_sales) + ".\n\n")
  elif choice == "2":
    print("1. View Sales by State")
    print("2. View Sales by Country")
    choice2 = input("Enter your choice: ")
    if choice2 == "1":
      state_sales = input_sales_data.sales_by_state()
      print("\n\nSales by state: \n\n" + str(state_sales) + "\n\n")
    elif choice2 == "2":
      country_sales = input_sales_data.sales_by_country()
      print("\n\nSales by country: \n\n" + str(country_sales) + "\n\n")
    else:
      print("\n invalid choice: please try again\n\n")
  elif choice == "3":
    sales_data.visualize_sales_trends()
  else:
    print("\nInvalid choice: please try again\n\n")


if __name__ == "__main__":
  sales_data = SalesData(data_set) #object declaration: SalesData sales_data = new SalesData(data_set);
  while True:
    main_menu(sales_data)

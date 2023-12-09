from sales_data import SalesData

data_set = input("Enter file path: ")  #java: StdIn


def main_menu(input_sales_data):
  print("Welcome to Business Analytics Dashboard")
  print("1. View Sales Report")
  print("2. View Sales Trend Over Time")
  choice = input("Enter your choice: ")

  if choice == "1":
    print("1. View Total Sales")
    print("2. View Sales by Region")
    choice2 = input("Enter your choice: ")
    if choice2 == "1":
      total_sales = input_sales_data.total_sales()
      print("\n\ntotal sales/revenue is: $" + str(total_sales) + ".\n\n")
    elif choice2 == "2":
      print("1. View Sales by State")
      print("2. View Sales by Country")
      choice3 = input("Enter your choice: ")
      if choice3 == "1":
        state_sales = input_sales_data.sales_by_state()
        print("\n\nSales by state: \n\n" + str(state_sales) + "\n\n")
      elif choice3 == "2":
        country_sales = input_sales_data.sales_by_country()
        print("\n\nSales by country: \n\n" + str(country_sales) + "\n\n")
      else:
        print("\n invalid choice: please try again\n\n")
  elif choice == "2":
    print("1. View Monthly Sales Trend")
    print("2. View Yearly Sales Trend")
    print("3. View Quarterly Sales Trend")
    choice4 = input("Enter your choice: ")
    if choice4 == "1":
      input_sales_data.visualize_month_trends()
      print("\n\n")
    elif choice4 == "2":
      input_sales_data.visualize_yearly_trends()
      print("\n\n")
    elif choice4 == "3":
      input_sales_data.visualize_quarterly_trends()
      print("\n\n")
    else:
      print("\n invalid choice: please try again\n\n")
  else:
    print("\nInvalid choice: please try again\n\n")


if __name__ == "__main__":
  sales_data = SalesData(
      data_set
  )  #object declaration: SalesData sales_data = new SalesData(data_set);
  while True:
    main_menu(sales_data)

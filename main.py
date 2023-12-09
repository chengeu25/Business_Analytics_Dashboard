# @author Cheng Eu Sun
# Final Project
# main.py

from sales_data import SalesData
#utilize dictionaries?

def main_menu(input_sales_data):
  print("Welcome to Business Analytics Dashboard")
  while True:
    print("1. View Sales Report")
    print("2. View Sales Trend Over Time")
    choice = input("Enter your choice (q to quit): ")

    if choice == "q":
      break  # Exit the program
    elif choice == "1":
      sales_report_menu(input_sales_data)
    elif choice == "2":
      sales_trend_menu(input_sales_data)
    else:
      print("\nInvalid choice: please try again\n")


def sales_report_menu(input_sales_data):
  while True:
    print("1. View Total Sales")
    print("2. View Sales by Region")
    print("b. Back to Main Menu")
    choice = input("Enter your choice (b to go back): ")

    if choice == "b":
      break  # Go back to main menu
    elif choice == "1":
      total_sales = input_sales_data.total_sales()
      print("\n\ntotal sales/revenue is: $" + str(total_sales) + ".\n\n")
    elif choice == "2":
      sales_by_region_menu(input_sales_data)
    else:
      print("\nInvalid choice: please try again\n")


def sales_by_region_menu(input_sales_data):
  while True:
    print("1. View Sales by State")
    print("2. View Sales by Country")
    print("b. Back to Sales Report Menu")
    choice = input("Enter your choice (b to go back): ")

    if choice == "b":
      break  # Go back to sales report menu
    elif choice == "1":
      state_sales = input_sales_data.sales_by_state()
      print("\n\nSales by state: \n\n" + str(state_sales) + "\n\n")
    elif choice == "2":
      country_sales = input_sales_data.sales_by_country()
      print("\n\nSales by country: \n\n" + str(country_sales) + "\n\n")
    else:
      print("\nInvalid choice: please try again\n")


def sales_trend_menu(input_sales_data):
  while True:
    print("1. View Monthly Sales Trend")
    print("2. View Yearly Sales Trend")
    print("3. View Quarterly Sales Trend")
    print("b. Back to Main Menu")
    choice = input("Enter your choice (b to go back): ")

    if choice == "b":
      break  # Go back to main menu
    elif choice == "1":
      input_sales_data.visualize_month_trends()
      print("\n\n")
    elif choice == "2":
      input_sales_data.visualize_yearly_trends()
      print("\n\n")
    elif choice == "3":
      input_sales_data.visualize_quarterly_trends()
      print("\n\n")
    else:
      print("\nInvalid choice: please try again\n")


if __name__ == "__main__":
  data_set = input("Enter file path: ")
  sales_data = SalesData(data_set)
  while True:
    main_menu(sales_data)

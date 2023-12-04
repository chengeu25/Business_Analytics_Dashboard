from Sales_data import SalesData

def main_menu():
    print("Welcome to Business Analytics Dashboard")
    print("1. View Sales Report")
    print("2. View Sales Trends")
    choice = input("Enter you choice: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            print("execute sales report function")
        elif choice == "2":
            print("execute sales trend function")
        else:
            print("invalid choice: please try again")







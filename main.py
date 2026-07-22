from portfolio import (
    display_available_stocks,
    add_stock,
    display_portfolio,
)

from file_handler import (
    save_to_txt,
    save_to_csv,
)

from utils import (
    print_heading,
    save_menu,
)


def main():

    print_heading("STOCK PORTFOLIO TRACKER")

    display_available_stocks()

    while True:
        try:
            count = int(input("How many stocks do you want to add? "))

            if count > 0:
                break

            print("Enter a number greater than 0.")

        except ValueError:
            print("Invalid input.")

    portfolio = []

    for i in range(count):
        print_heading(f"Stock {i + 1}")
        portfolio.append(add_stock())

    total = display_portfolio(portfolio)

    choice = save_menu()

    if choice == "1":
        save_to_txt(portfolio, total)
        print("\nReport saved as portfolio.txt")

    elif choice == "2":
        save_to_csv(portfolio)
        print("\nReport saved as portfolio.csv")

    elif choice == "3":
        save_to_txt(portfolio, total)
        save_to_csv(portfolio)
        print("\nReport saved successfully.")

    else:
        print("\nReport was not saved.")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
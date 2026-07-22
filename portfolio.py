from stock_data import STOCK_PRICES


def display_available_stocks():
    print("\nAvailable Stocks")
    print("-" * 30)

    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<8} : ${price}")

    print("-" * 30)


def add_stock():
    while True:
        stock = input("Enter Stock Symbol: ").upper()

        if stock in STOCK_PRICES:
            break
        else:
            print("Invalid Stock Symbol! Try again.")

    while True:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    price = STOCK_PRICES[stock]
    investment = price * quantity

    return {
        "stock": stock,
        "price": price,
        "quantity": quantity,
        "investment": investment
    }


def display_portfolio(portfolio):

    print("\n" + "=" * 60)
    print("PORTFOLIO SUMMARY".center(60))
    print("=" * 60)

    print(f"{'Stock':<10}{'Price':<10}{'Qty':<10}{'Investment':<15}")
    print("-" * 60)

    total = 0

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"${item['price']:<9}"
            f"{item['quantity']:<10}"
            f"${item['investment']:<10}"
        )

        total += item["investment"]

    print("-" * 60)
    print(f"{'Total Investment':<30} ${total}")
    print("=" * 60)

    return total
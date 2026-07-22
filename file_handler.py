import csv
import os

def save_to_txt(portfolio, total):
    os.makedirs("data", exist_ok=True)

    with open("data/portfolio.txt", "w") as file:
        file.write("=" * 50 + "\n")
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        for item in portfolio:
            file.write(f"Stock: {item['stock']}\n")
            file.write(f"Price: ${item['price']}\n")
            file.write(f"Quantity: {item['quantity']}\n")
            file.write(f"Investment: ${item['investment']}\n")
            file.write("-" * 40 + "\n")

        file.write(f"\nTotal Investment: ${total}\n")


def save_to_csv(portfolio):
    os.makedirs("data", exist_ok=True)

    with open("data/portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock", "Price", "Quantity", "Investment"])

        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["price"],
                item["quantity"],
                item["investment"]
            ])
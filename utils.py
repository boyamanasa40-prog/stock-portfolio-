def print_heading(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def save_menu():
    print("\nChoose an option:")
    print("1. Save as TXT")
    print("2. Save as CSV")
    print("3. Save as BOTH")
    print("4. Don't Save")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("Invalid choice. Try again.")
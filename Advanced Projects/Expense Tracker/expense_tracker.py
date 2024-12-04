import json


def main():
    print("Welcome to the Expense Tracker!\n")
    while True:
        print("1. Add an Expense")
        print("2. View Summary of Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            expense = get_user_expense()
            save_expense_to_file(expense)
        elif choice == "2":
            summarize_expenses()
        elif choice == "3":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def get_user_expense():
    """
    Collects user input for expense details.
    Returns:
        dict: A dictionary containing expense details.
    """
    print("\n--- Add a New Expense ---")
    expense_name = input("Enter the expense name: ").strip()

    expense_categories = [
        "🍔 Food",
        "🚗 Transport",
        "💡 Bills",
        "🎬 Entertainment",
        "🎉 Fun",
        "🔧 Miscellaneous",
    ]

    while True:
        print("\nSelect the expense category:")
        for index, category in enumerate(expense_categories, start=1):
            print(f"{index}. {category}")
        try:
            category_index = int(input("Enter the category number: "))
            if 1 <= category_index <= len(expense_categories):
                break
            else:
                print("Invalid category number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            expense_amount = float(input("Enter the expense amount: $"))
            if expense_amount > 0:
                break
            else:
                print("Expense amount must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    expense = {
        "name": expense_name,
        "category": expense_categories[category_index - 1],
        "amount": expense_amount,
    }

    print(
        "\nExpense Added Successfully!",
        f"\nName: {expense['name']}",
        f"\nCategory: {expense['category']}",
        f"\nAmount: ${expense['amount']:.2f}\n",
    )
    return expense


def save_expense_to_file(expense):
    """
    Saves the expense to a JSON file.
    Args:
        expense (dict): The expense details to save.
    """
    print("Saving expense to file...\n")
    file_name = "expenses.json"
    try:
        # Read existing data
        try:
            with open(file_name, "r") as file:
                expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        # Append new expense
        expenses.append(expense)

        # Write back to file
        with open(file_name, "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving the expense: {e}")


def summarize_expenses():
    """
    Reads and summarizes expenses from the file.
    """
    print("\n--- Expense Summary ---")
    file_name = "expenses.json"
    try:
        with open(file_name, "r") as file:
            expenses = json.load(file)

        if not expenses:
            print("No expenses recorded yet.")
            return

        total_amount = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expenses: ${total_amount:.2f}\n")
        print("Detailed Expenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(
                f"{idx}. Name: {expense['name']}, "
                f"Category: {expense['category']}, "
                f"Amount: ${expense['amount']:.2f}"
            )
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")
    except json.JSONDecodeError:
        print("Error reading expenses. The file might be corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

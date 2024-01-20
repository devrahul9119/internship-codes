import datetime
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        today = datetime.date.today()
        date_str = today.strftime("%Y-%m-%d")

        if date_str not in self.expenses:
            self.expenses[date_str] = []

        self.expenses[date_str].append({"amount": amount, "category": category})
        print("Expense added successfully.")

    def view_expenses(self):
        for date, expenses in self.expenses.items():
            print(f"\nDate: {date}")
            for expense in expenses:
                print(f"  Amount: {expense['amount']}, Category: {expense['category']}")

    def view_spending_pattern(self):
        category_totals = {}
        for expenses in self.expenses.values():
            for expense in expenses:
                category = expense['category']
                amount = expense['amount']
                category_totals[category] = category_totals.get(category, 0) + amount

        if not category_totals:
            print("No spending data available.")
        else:
            print("\nSpending Pattern:")
            for category, total in category_totals.items():
                print(f"  {category}: {total}")
        
    def store_data(self):
        with open('expenses.json', 'a') as f:
            json.dump({key: value for key, value in self.expenses.items()}, f, indent=4)
            f.write('\n')            

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Quit")

        option = input("Enter your option(1-4): ")

        if option == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, category)
            tracker.store_data()
        elif option == "2":
            tracker.view_expenses()
        elif option == "3":
            tracker.view_spending_pattern()
        elif option == "4":
            print("Exiting the Expense Tracker System. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


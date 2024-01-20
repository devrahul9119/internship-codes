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
        try:
            # Load existing data from the file
            with open('expenses.json', 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # If the file is not found or not valid JSON, initialize with an empty list
            existing_data = []

        # Append the new entry to the existing data
        existing_data.append({key: value for key, value in self.expenses.items()})

        # Write the entire updated list back to the file
        with open('expenses.json', 'w') as f:
            json.dump(existing_data, f, indent=4) 
            
    def load_data(self):
        try:
            with open('expenses.json', 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print("File 'expenses.json' not found.")
            return {}

    def view_loaded_data(self):
        loaded_data = self.load_data()

        if loaded_data:
            print("\nLoaded Data:")
            for entry in loaded_data:
                for date, expenses in entry.items():
                    print(f"\nDate: {date}")
                    for expense in expenses:
                        print(f"  Amount: {expense['amount']}, Category: {expense['category']}")
        else:
            print("No data loaded.")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. To view data in database")
        print("5. Quit")

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
            tracker.view_loaded_data()
        elif option == "5":
            print("Exiting the Expense Tracker System. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


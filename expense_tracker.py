import datetime

def main():
    expense_file = "expenses.csv"
    budget = 200
    exp = input_expense()                                   #Input Expense
    save_expense(exp, expense_file)                         #Write expense to file
    display(expense_file,budget)                            #Read file

#Expense class
class Expense:
    def __init__(self, date, name, amt, category):
        self.date = date
        self.name = name
        self.category = category
        self.amt = amt

    def __repr__(self):
        return f"<{self.date}, {self.name}, ${self.amt}, {self.category}>"

#Input Function
def input_expense():
    exp_name = input("Enter expense name: ")
    exp_amt = float(input("Enter expense amount: "))

    categories = [
        "Food",
        "College",
        "Fun",
        "Misc"
    ]

    #Infinite loop that breaks once a valid category is chosen by the user.
    while True:
        print("Select a category: ")
        for i, name in enumerate(categories, start=1):
            print(f"    {i}. {name}")

        index = int(input(f"Enter category number [1-{len(categories)}]: ")) - 1
        if index in range(len(categories)):
            selected = categories[index]
            expense = Expense(datetime.date.today(), exp_name, exp_amt, selected)
            return expense
        else:
            print("Invalid category entered.")

#Save function to input data into a csv file
def save_expense(expense, expense_file):
    print(f"Saving the expense: {expense} to {expense_file}")
    with open(expense_file, "a") as file:
        file.write(f"{expense.date}, {expense.name}, {expense.amt}, {expense.category}\n")

#Output function to read the csv file.
def display(expense_file, budget):
    expenses = []
    with open(expense_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            expenseDate, expenseName, expenseAmt, expenseCategory = line.strip().split(",")
            expenseDate = expenseDate.strip()
            expenseName = expenseName.strip()
            expenseAmt = expenseAmt.strip()
            expenseCategory = expenseCategory.strip()
            line_expense = Expense(expenseDate, expenseName, float(expenseAmt), expenseCategory)
            expenses.append(line_expense)

    sort_category = {}
    for expense in expenses:
        key = expense.category
        if key in sort_category:
            sort_category[key] += expense.amt
        else:
            sort_category[key] = expense.amt

    print("Expenses by Category: ")
    for key, amount in sort_category.items():
        print(f"    {key}: ${amount}")

    total = sum([exp.amt for exp in expenses])
    remaining_budget = budget-total
    print(f"Total amount spent: ${total}\nRemaining budget left: ${remaining_budget}")


if __name__ == "__main__":
    main()

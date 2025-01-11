from expense_tracker import Expense, input_expense, save_expense, display
import datetime

def test_input_expense(monkeypatch):
    testInputs = ["Coffee", "6.50", "1"]
    currentInput = 0

    def mock_input(prompt):
        nonlocal currentInput
        response = testInputs[currentInput]
        currentInput += 1
        return response

    monkeypatch.setattr('builtins.input', mock_input)
    expense = input_expense()

    assert expense.name == "Coffee"
    assert expense.amt == 6.50
    assert expense.category == "Food"
    assert isinstance(expense.date, datetime.date)

def test_save_expense(tmp_path):
    test_file = tmp_path/"test_expenses.csv"
    today = datetime.date.today()
    test_expense = Expense(today, "Coffee", 6.50, "Food")

    save_expense(test_expense, str(test_file))

    with open(test_file, 'r') as file:
        saved = file.read().strip()
        expected = f'{today}, Coffee, 6.5, Food'
        assert saved == expected

def test_display(tmp_path, capsys):
    test_file = tmp_path/"test_expenses.csv"
    test_budget = 200
    today = datetime.date.today()

    with open(test_file, 'w') as file:
        file.write(f"{today},Coffee,2.5,Food\n")
        file.write(f"{today},Textbook,20.0,College\n")
        file.write(f"{today},Movie,10.0,Fun\n")
        file.write(f"{today},Coffee,2.5,Food\n")

    display(str(test_file), test_budget)
    printed = capsys.readouterr().out

    assert "Expenses by Category" in printed
    assert "Food: $5.0" in printed
    assert "College: $20.0" in printed
    assert "Fun: $10.0" in printed
    assert "Total amount spent: $35.0" in printed
    assert "Remaining budget left: " in printed

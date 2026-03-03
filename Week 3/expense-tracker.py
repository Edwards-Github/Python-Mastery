class Expense:

	def __init__(self, amount, category, description, date):
		self.amount = amount
		self.category = category
		self.description = description
		self.date = date

	def __repr__(self):
		return f'Expense({self.date}, {self.category}, {self.description}, ${self.amount})'

class ExpenseTracker:

	def __init__(self, expenses=None):
		self.expenses = expenses if expenses is not None else []

	def add(self, expense):
		self.expenses.append(expense)

	def list(self):
		for i, expense in enumerate(self.expenses, 1):
			print(f'{i}.Date: {expense.date} Category: {expense.category} Description: {expense.description} Price: ${expense.amount}')

	def total(self):
		return sum(expense.amount for expense in self.expenses)


amazon = Expense(23, 'Amazon', 'ear phones', 'March 2, 2026')
amazon_2 = Expense(160, 'Amazon', 'headphones', 'March 3, 2026')
tracker = ExpenseTracker()
tracker.add(amazon)
tracker.add(amazon_2)
tracker.list()
print(f'The total expense is: ${tracker.total()}')
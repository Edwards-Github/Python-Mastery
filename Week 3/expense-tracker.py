from collections import defaultdict
from datetime import date

class Expense:

	def __init__(self, amount, category, description, date):
		self.amount = amount
		self.category = category
		self.description = description
		self.date = date

	def __repr__(self):
		return f'{self.date}: [{self.category}] {self.description} ${self.amount}'

class ExpenseTracker:

	def __init__(self, expenses=None):
		self.expenses = expenses if expenses is not None else []

	def add(self, expense):
		"""
			adds expense to the list expenses
		"""
		self.expenses.append(expense)

	def display_expenses(self):
		"""
			displays all the expenses in the list expenses
		"""
		for i, expense in enumerate(self.expenses, 1):
			print(f'{i}.Date: {expense.date} Category: {expense.category} Description: {expense.description} Price: ${expense.amount}')

	# def group_by_category(self):
	# 	grouped = defaultdict(list)
	# 	for e in self.expenses:
	# 		grouped[e.category].append(e)
	# 	return dict(grouped)

	def group_by_category(self, category):
		"""
			groups expenses by category
		"""
		return [e for e in self.expenses if e.category == category]

	def filter_dates(self, start, end):
		"""
			sorts expenses by date range
		"""
		return sorted([d for d in self.expenses if start <= d.date <= end], key=lambda d: d.date)

	def monthly_totals(self):
		"""
			returns dictionary with month and year as a key and the total of the month as the value
		"""
		totals = defaultdict(float)
		for expense in self.expenses:
			month = (expense.date.year, expense.date.month)
			totals[month] += expense.amount
		return dict(totals)

	def monthly_summary(self):
		"""
			prints the months and expense details
		"""
		monthly_info = defaultdict(list)
		for expense in self.expenses:
			month = (expense.date.year, expense.date.month)
			monthly_info[month].append(expense)

		for month, expense in monthly_info.items():
			print(f'{month}: {expense}')

	def total(self):
		"""
			returns the total amount of all the expenses
		"""
		return sum(expense.amount for expense in self.expenses)

	def export_to_csv(self):
		"""
			exports the expenses in csv format to a text file
		"""
		try:
			with open('ExpenseTracker.txt', 'w') as f:
				f.write('date,category,description,amount\n')
				for expense in self.expenses:
					f.write(f'{expense.date},{expense.category},{expense.description},{expense.amount}\n')
		except IOError as e:
			print(f'Export failed: {e}')


	def expense_generator(self):
		"""
			creates a generator for the expenses
		"""
		for expense in self.expenses:
			yield expense

# while True:
# 	print('---------- Expense Tracker ----------\n')
# 	print('What would you like to do?')
# 	print('1. Add expense\n')
# 	print('2. Display expenses\n')
# 	print('3. Group expenses by category.')
# 	print('4. Filter expenses by date.')
# 	print('5. Filter expenses by date.')

amazon = Expense(23, 'Amazon', 'ear phones', date(2026, 3, 2))
amazon_2 = Expense(160, 'Amazon', 'headphones', date(2026, 3, 3))
gamestop = Expense(60, 'Gamestop', 'Resident Evil 9', date(2026, 3, 6))
gamestop2 = Expense(60, 'Gamestop', 'Resident Evil 9', date(2026, 4, 6))
tracker = ExpenseTracker()
tracker.add(amazon)
tracker.add(amazon_2)
tracker.add(gamestop)
tracker.add(gamestop2)

# tracker.display_expenses()
# print(f'The total expense is: ${tracker.total()}')
# print(tracker.group_by_category('Amazon'))
# print(tracker.monthly_totals())
# print(tracker.filter_dates(date(2026, 3, 1), date(2026, 4, 1)))
# tracker.export_to_csv()
# tracker.monthly_summary()
gen = tracker.expense_generator()
print(next(gen)) # expense 1
print(next(gen)) # expense 2
print(next(gen)) # expense 3
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
		self.expenses.append(expense)

	def display_expenses(self):
		for i, expense in enumerate(self.expenses, 1):
			print(f'{i}.Date: {expense.date} Category: {expense.category} Description: {expense.description} Price: ${expense.amount}')

	def group_by_category(self, category):
		grouped = defaultdict(list)
		for e in self.expenses:
			grouped[e.category].append(e)
		return dict(grouped)

	def filter_dates(self, start, end):
		return sorted([d for d in self.expenses if start <= d.date <= end], key=lambda d: d.date)

	def monthly_totals(self):
		totals = defaultdict(float)
		for expense in self.expenses:
			month = (expense.date.year, expense.date.month)
			totals[month] += expense.amount
		return dict(totals)

	def total(self):
		return sum(expense.amount for expense in self.expenses)

	def export_to_csv(self):
		with open('ExpenseTracker.txt', 'w') as f:
			f.write('date,category,description,amount\n')
			for expense in self.expenses:
				f.write(f'{expense.date},{expense.category},{expense.description},{expense.amount}\n')


amazon = Expense(23, 'Amazon', 'ear phones', date(2026, 3, 2))
amazon_2 = Expense(160, 'Amazon', 'headphones', date(2026, 3, 3))
gamestop = Expense(60, 'Gamestop', 'Resident Evil 9', date(2026, 3, 6))
gamestop2 = Expense(60, 'Gamestop', 'Resident Evil 9', date(2026, 4, 6))
tracker = ExpenseTracker()
tracker.add(amazon)
tracker.add(amazon_2)
tracker.add(gamestop)
tracker.add(gamestop2)
tracker.display_expenses()
print(f'The total expense is: ${tracker.total()}')
print(tracker.group_by_category('Amazon'))
print(tracker.monthly_totals())
print(tracker.filter_dates(date(2026, 3, 1), date(2026, 4, 1)))
tracker.export_to_csv()
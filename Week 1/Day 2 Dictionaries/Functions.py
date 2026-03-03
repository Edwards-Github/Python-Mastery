def hello_func():
	print('Hello Function!')

print(hello_func)
print(hello_func())

print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')

hello_func()
hello_func()
hello_func()
hello_func()

def hello_function():
	return 'Hello Function'

print(hello_function())
print(len('Test'))

# chaining with functions
print(hello_function().upper())

def hello_func(greeting):
	return '{} Function.'.format(greeting)

print(hello_func('Hi'))

# default value
def hello_function(greeting, name='You'):
	return '{}, {}'.format(greeting, name)

print(hello_function('Hi', name = 'Corey'))

# args and kwargs
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

# student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# * single star in front of our list
# ** double star in front of our dictionary
# will actually unpack these values and pass them in individually
student_info(courses, info) # prints {}
student_info(*courses, **info) # prints ('Math', 'Art') {'name': 'John', 'age': 22}

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return True for leap years, False for non-leap years."""
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	"""Return number of days in that month in that year."""

	if not 1 <= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 2))
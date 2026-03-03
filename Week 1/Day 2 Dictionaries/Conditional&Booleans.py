if True:
	print('Conditional was True')

if False:
	print('Conditional was True')

# Comparisons
# Equal:            ==
# Not Equal:        !=
# Greater Than:      >
# Less Than:         <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'

if language == 'Python':
	print('Conditional was True')
else:
	print('No match')

language = 'Java'

if language == 'Python':
	print('Conditional was True')
else:
	print('No match')

language = 'Java'

if language == 'Python':
	print('Conditional was True')
elif language == 'Java':
	print('Language is Java')
else:
	print('No match')

# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please Log In')
else:
	print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))

b = a
print(a is b)

condition = None # Evaluates to false too

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')
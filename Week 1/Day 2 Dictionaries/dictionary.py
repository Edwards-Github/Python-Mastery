student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# accessing a key
print(student['name'])

# get method
print(student.get('name'))
print(student.get('phone'))

# get method & default value if it does not exist
print(student.get('phone', 'Not Found'))

# adding new key / updating a new value with key
student['phone'] = '555-5555'
print(student)

# updating multiple values at a time
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

# deleting key value
del student['age']
print(student)
student['age'] = 26

# pop method
age = student.pop('age')
print(age)

# length of dictionary
print(len(student))

# looping through key and values
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
	print(key, value)
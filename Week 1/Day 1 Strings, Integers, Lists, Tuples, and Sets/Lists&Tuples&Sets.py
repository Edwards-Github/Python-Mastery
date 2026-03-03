# Lists
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# Size of list
print(len(courses))

# Access index
print(courses[3])
print(courses[-1])

# Access range of values
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# Append method
courses.append('Art')
print(courses)

# Insert method
courses.insert(0, 'Art')
print(courses)

# Extend method (adds multiple values)
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)

# Reset courses
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.extend(courses_2)
print(courses)

# Remove method
courses.remove('Math')
print(courses)

# Pop method (removes last item in list)
popped = courses.pop()
print(popped)

# Reverse method
courses.reverse()
print(courses)

# Sort method
courses.sort()
print(courses)

# Reverse sort
courses.sort(reverse=True)
print(courses)

# Sorted function (doesn't change original list)
sorted(courses)
print(courses)
sorted_courses = sorted(courses)
print(sorted_courses)

# Min and max methods
nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))

# Index methods 
print(courses)
print(courses.index('CompSci'))

# in operator
print('Art' in courses)
print('Math' in courses)

# for loop
for item in courses:
	print(item)

for index, course in enumerate(courses):
	print(index, course)

for index, course in enumerate(courses, start=1):
	print(index, course)

# Join method (join items in list with this string)
courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ', '.join(courses)
print(course_str)

# Split method
new_list = course_str.split(', ')
print(new_list)

# Tuples

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' can't change elements in a tuple
print(tuple_1)
print(tuple_2)

# Sets (doesn't care about order, throws away duplicates)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

# Intersect method (finds the common elements between two sets)
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))

# Difference methods
print(cs_courses.difference(art_courses))

# Union method
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
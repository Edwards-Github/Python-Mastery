print('Hello World')

my_message = 'Hello World'
print(my_message)

# Escape character
my_message = 'Bobby\'s World'
print(my_message)

# Alternative option
my_message = "Bobby's World"
print(my_message)

# Multiple Lines
message = """Bobby's World was a good
cartoon in the 1990's"""
print(message)

# Length of message
print(len(my_message))

# Accessing index
print(message[0])

# Access range of characters
print(message[0:7])
print(message[7:])

# Lowercase method
print(message.lower())

# Uppercase method
print(message.upper())

# Count method
print(message.count('Bobby\'s'))
print(message.count('a'))

# Find method
print(message.find('World'))
print(message.find('Hi'))

# Replace method
message.replace('World', 'Universe')
print(message)

new_message = message.replace('World', 'Universe')
print(new_message)

# Concatenate
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)

# Formatted string
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# f strings
message = f'{greeting}, {name}. Welcome!'
print(message)

# f strings with method
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# dir - tells us what attributes and methods are available to this variable
print(dir(name))

# help function
print(help(str))
print(help(str.lower))
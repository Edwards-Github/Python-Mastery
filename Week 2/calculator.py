def add(num_1, num_2):
	"""adds two numbers"""
	return num_1 + num_2

def subtract(num_1, num_2):
	"""subtracts two numbers"""
	return num_1 - num_2

def multiply(num_1, num_2):
	"""multiplies two numbers"""
	return num_1 * num_2

def divide(num_1, num_2):
	"""divides two numbers"""
	if num_2 == 0:
		return "Error: Cannot divide by zero"
	else:
		return num_1 / num_2

def print_history(history):
	"""prints history of results"""
	print("\n===== History =====")
	for i, entry in enumerate(history, 1):
		print(f"{i}. {entry}")

def is_valid_number(num):
	"""Returns True if value can be converted to a float, False otherwise."""
	try:
		float(num)
		return True
	except ValueError:
		return False

history = []

while True:
	print("\n==================== Calculator ====================")
	print("Please choose from the following options")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. History")
	print("6. Quit")
	choice = input("\nEnter here: ")

	if choice == "6":
		break
	elif choice == "5":
		print_history(history)
	else:
		raw_1 = input("Please enter the first number: ")
		raw_2 = input("Please enter the second number: ")

		if not is_valid_number(raw_1) or not is_valid_number(raw_2):
			print("Invalid input: please enter numbers only")
			continue

		num_1 = float(raw_1)
		num_2 = float(raw_2)

		if choice == "1":
			result = add(num_1, num_2)
		elif choice == "2":
			result = subtract(num_1, num_2)
		elif choice == "3":
			result = multiply(num_1, num_2)
		elif choice == "4":
			result = divide(num_1, num_2)
		else:
			print("Invalid choice")

		print(f"Answer: {result}")
		history.append(result)
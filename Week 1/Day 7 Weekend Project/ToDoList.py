todos = [] # List to store tasks

while True:
	print("\n=== TODO LIST ===")
	print("1. Add task")
	print("2. View tasks")
	print("3. Mark complete")
	print("4. Delete task")
	print("5. Exit")

	choice = input("\nChoose option (1-5): ")

	if choice == "1":
		task = input("Enter task: ")
		todos.append(task)
	elif choice == "2":
		if len(todos) == 0:
			print("No task to display.")
		else:
			print("\n=== Current tasks === ")
			for i, task in enumerate(todos):
				print(f"{i + 1}: {task}")
	elif choice == "3":
		if len(todos) == 0:
			print("No task to complete!")
		else:
			for i, task in enumerate(todos):
				print(f"{i + 1}: {task}")
			num = int(input("Which task should I mark completed? (enter number): "))
			if 1 <= num <= len(todos):
				todos[num - 1] = todos[num - 1] + " ✓"
				print(f"{todos[num - 1]} has been marked complete!")
			else:
				print("Invalid task number")
	elif choice == "4":
		if len(todos) == 0:
			print("No task to delete!")
		else:
			for i, task in enumerate(todos):
				print(f"{i + 1}: {task}")
			num = int(input("Which task should I delete? (enter number): "))
			if 1 <= num <= len(todos):
				deleted = todos.pop(num - 1)
				print(f"Deleted: {deleted}")
			else:
				print("Invalid task number")
	if choice == "5":
		print("Goodbye!")
		break
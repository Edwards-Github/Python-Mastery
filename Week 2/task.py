
import json

class InvalidPriorityError(Exception):
	pass

class Task:

	def __init__(self, title, description, priority, done=False):
		if not title or not title.strip():
			raise ValueError('Task title cannot be empty.')
		if not isinstance(priority, int) or priority < 1:
			raise InvalidPriorityError(f'Invalid priority: {priority}. Must be an integer >= 1')
		self.title = title
		self.description = description
		self.priority = priority
		self.done = done

	def complete(self):
		self.done = True

	def to_dict(self):
		return {
			'title' : self.title,
			'description' : self.description,
			'priority' : self.priority,
			'done' : self.done
		}

	@classmethod
	def from_dict(cls, data):
		return cls(data['title'], data['description'], data['priority'], data['done'])

	def __repr__(self):
		return f"[{self.title}] {self.description} (priority: {self.priority})"

class TaskManager:

	def __init__(self, tasks):
		self.tasks = tasks

	def add_task(self, task):
		if task not in self.tasks:
			self.tasks.append(task)

	def delete_task(self, title):
		for task in self.tasks:
			if task.title == title:
				self.tasks.remove(task)
				
	def complete_task(self, title):
		for task in self.tasks:
			if task.title == title:
				task.done = True

	def filter_by_priority(self):
		self.tasks.sort(key=lambda task: task.priority)

	def list_tasks(self):
		for task in self.tasks:
			status = "✓" if task.done else "○"
			print(f"[{status}] {task.title} (priority: {task.priority})")

	def save_to_file(self, filename):
		with open(filename, 'w') as file:
			task_list = [task.to_dict() for task in self.tasks] # list of dicts
			json.dump(task_list, file) # write to file

	def load_from_file(self, filename):
		try:
			with open(filename, 'r') as file:
				task_list = json.load(file) # file -> list of dicts
			self.tasks = [Task.from_dict(data) for data in task_list] # dicts -> Task objects
		except FileNotFoundError as e:
			print(e)
		except json.JSONDecodeError as e:
			print(e)
		except InvalidPriorityError as e:
			print(e)
		except ValueError as e:
			print(e)
		else:
			print("Task Manager updated successfully!")

task_manager = TaskManager([])

while True:
	print('\n---------- Welcome to the Task Manager ----------')
	print('1. Add task')
	print('2. List tasks')
	print('3. Complete task')
	print('4. Delete task')
	print('5. Quit')

	choice = input('\nWhat would you like to do (Please enter an integer): ')

	if choice == '5':
		break
	elif choice == '1':
		title = input('What task would you like to add? ')
		description = input('Enter a description for the task: ')
		priority = input('Enter priority number (highest: 1 lowest: 3): ')
		task = Task(title.lower(), description, int(priority))
		task_manager.add_task(task)
	elif choice == '2':
		task_manager.list_tasks()
	elif choice == '3':
		task_completed = input('What task did you want to complete? ')
		task_manager.complete_task(task_completed.lower())
	elif choice == '4':
		delete_task = input('What task did you want to delete? ')
		task_manager.delete_task(delete_task.lower())

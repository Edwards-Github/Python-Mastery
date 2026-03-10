import contacts.py, utils.py

def main():
	contacts = create_contacts()

	add_contacts(contacts, 'Edward', ['123-4567', 'edward@gmail.com'])
	add_contacts(contacts, 'Chris', ['456-7890', 'chris@gmail.com'])

	print(find(contacts, 'Edward'))
	print(find(contacts, 'Chris'))

	edit(contacts, 'John', ['111-2222', 'john@gmail.com'])
	add_contacts(contacts, 'John', ['111-2222', 'john@gmail.com'])
	edit(contacts, 'John', ['111-2222', 'john@gmail.com'])

	list_contacts(contacts)

if __name__ == '__main__':
	main()
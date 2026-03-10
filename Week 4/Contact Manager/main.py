from contacts import add_contact, find, edit, list_contacts, create_contacts
from utils import print_divider

def main():
	contacts = create_contacts()

	add_contact(contacts, 'Edward', ['123-4567', 'edward@gmail.com'])
	add_contact(contacts, 'Chris', ['456-7890', 'chris@gmail.com'])

	print(find(contacts, 'Edward'))
	print(find(contacts, 'Chris'))

	edit(contacts, 'John', ['111-2222', 'john@gmail.com'])
	add_contact(contacts, 'John', ['111-2222', 'john@gmail.com'])
	edit(contacts, 'John', ['111-2222', 'john@gmail.com'])

	list_contacts(contacts)

if __name__ == '__main__':
	main()
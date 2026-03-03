from collections import defaultdict

"""
	1. Build a Contact Manager: store contacts in a dict {name: [phone, email]}
	2. Functions: add_contact(), find(contact), list_contacts().
	3. Store contacts in a set of names for fast lookup
"""
def add_contact(contacts, name, info):
	"""
		1. contacts is a hashmap
		2. name is a string
		3. info is a list [phone, email]
		4. adds contact to hashmap
	"""
	contacts[name].extend(info)

def find(contacts, name):
	"""
		1. contacts is a hashmap
		2. name is a string
		3. finds contact in hashmap:
			a. EXISTS: return contact info
			b. NOT EXIST: return "No contact info found."
	"""
	return contacts.get(name, 'No contact info found.')

def edit(contacts, name, info):
	"""
		1. contacts is a hashmap
		2. name is a string
		3. info is a list [phone, email]
		4. updates contact in hashmap
	"""
	if name in contacts:
		print('Contact info has been updated.')
		contacts.update({name:info})
	else:
		print('No contact info found.')

def list_contacts(contacts):
	"""
		1. contacts is a hashmap
		2. prints all the contacts in the hashmap
	"""
	print('\n========== List of contacts ==========')
	for i, contact in enumerate(contacts.keys(), 1):
		print(f'{i}. {contact}')

contacts = defaultdict(list) # dict{name: [phone, email]}
add_contact(contacts, 'Edward', ['123-4567', 'edward@gmail.com'])
add_contact(contacts, 'Chris', ['456-7890', 'chris@gmail.com'])
print(find(contacts, 'Edward'))
print(find(contacts, 'Chris'))
edit(contacts, 'John', ['111-2222', 'john@gmail.com'])
add_contact(contacts, 'John', ['111-2222', 'john@gmail.com'])
edit(contacts, 'John', ['111-2222', 'john@gmail.com'])
list_contacts(contacts)
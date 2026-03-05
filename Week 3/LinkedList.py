class ListNode:

	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

	def __repr__(self):
		return f'{self.value}'

class LinkedList:

	def __init__(self, node=None):
		self.node = node

	def node_append(self, node):
		last_node = self.node # This would be the head

		while last_node.next != None:
			last_node = last_node.next

		last_node.next = node

	def node_prepend(self, node):
		node.next = self.node
		self.node = node


	def node_delete(self, node):
		prev = None
		curr = self.node

		while curr != node:
			prev = curr
			curr = curr.next

		if prev is None:
			self.node = curr.next
		else:
			prev.next = curr.next

	def node_search(self, node):
		target_node = self.node

		while target_node != node:
			target_node = target_node.next

		return target_node if target_node == node else None

	def node_to_list(self):
		dummy_node = self.node
		result = []

		while dummy_node:
			value = dummy_node.value
			result.append(value)
			dummy_node = dummy_node.next

		return result

fifth = ListNode(5, None)
fourth = ListNode(4, fifth)
third = ListNode(3, fourth)
second = ListNode(2, third)
first = ListNode(1, second)
head = LinkedList(first)

print('node_to_list() method')
print('--------------------')
sixth = ListNode(6, None)
linkedList = head.node_to_list()
for n in linkedList:
	print(n)
print('\n')

print('node_append() method')
print('--------------------')
head.node_append(sixth)
linkedList = head.node_to_list()
for n in linkedList:
	print(n)
print('\n')

print('node_delete() method')
print('--------------------')
head.node_delete(third) # node_delete isn't working
linkedList = head.node_to_list()
for n in linkedList:
	print(n)
print('\n')

print('node_prepend() method')
print('--------------------')
seven = ListNode(7, None)
head.node_prepend(seven)
linkedList = head.node_to_list()
for n in linkedList:
	print(n)
print('\n')

print('node_search() method')
print('--------------------')
target = head.node_search(sixth)
print(target.value)
print('\n')
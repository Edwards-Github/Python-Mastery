class TreeNode():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree():
	def __init__(self, root):
		self.root = root

	def insert(self, val):
		self.root = self.insert_node(self.root, val)

	def insert_node(self, current_node, val):
		if not current_node:
			return TreeNode(val) # had it as: return TreeNode(current_node)
		if current_node.val > val:
			current_node.left = self.insert_node(current_node.left, val) # forgot self in self.insert_node(current_node, val) # did insert_node(current_node, val)
		elif current_node.val < val:
			current_node.right = self.insert_node(current_node.right, val) # forgot self in self.insert_node(current_node, val) # did insert_node(current_node, val)
		return current_node

	def search(self, current_node, target):
		if not current_node:
			return None
		if current_node == target:
			return current_node
		return self.search(current_node.left, target) or self.search(current_node.right, target)

	def inorder_traversal(self, current_node):
		if not current_node:
			return None
		self.inorder_traversal(current_node.left)
		print(current_node.val)
		self.inorder_traversal(current_node.right)

tree = BinaryTree(None)
for n in [1,3,5,7,9]:
	tree.insert(n)
tree.inorder_traversal(tree.root) # did tree.inorder_traversal(tree)

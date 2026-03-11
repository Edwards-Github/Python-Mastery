class TreeNode():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree():
	def __init__(self, node):
		self.node = node

	def insert(self, val):
		self.node = self.insert_node(self.node, val)

	def insert_node(self, node, val):
		if not node:
			return TreeNode(val)
		if val < node.val:
			node.left = self.insert_node(node.left, val)
		elif val > node.val:
			node.right = self.insert_node(node.right, val)
		return node

	def search(self, node, target):
		if not node:
			return None

		if node == target:
			return node

		return self.search(node.left, target) or self.search(node.right, target)

	def inorder_traversal(self, root):
		if not root:
			return None

		self.inorder_traversal(root.left)
		print(root.val)
		self.inorder_traversal(root.right)

tree = BinaryTree(None)
for val in [5, 3, 7, 1, 4, 6, 8]:
	tree.insert(val)

tree.inorder_traversal(tree.node)
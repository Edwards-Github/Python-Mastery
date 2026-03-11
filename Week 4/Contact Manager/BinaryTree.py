class TreeNode():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree():
	def __init__(self, node):
		self.node = node

	# def insert_node(self, node):

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

left_left = TreeNode(4)
left = TreeNode(2, left_left)
right = TreeNode(3)
root = TreeNode(1, left, right)
head = BinaryTree(root)

head.inorder_traversal(root)
print(head.search(root, left_left).val)
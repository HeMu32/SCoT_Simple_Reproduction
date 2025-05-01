class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def __init__(self, data):
        self.root = self.build_tree(data)

    def build_tree(self, data):
        if not data:
            return None
        mid = len(data) // 2
        root = TreeNode(data[mid])
        root.left = self.build_tree(data[:mid])
        root.right = self.build_tree(data[mid+1:])
        return root

    def is_balanced(self, root):
        def check_balance(node):
            if not node:
                return 0
            left_height = check_balance(node.left)
            if left_height == -1:
                return -1
            right_height = check_balance(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return check_balance(root) != -1
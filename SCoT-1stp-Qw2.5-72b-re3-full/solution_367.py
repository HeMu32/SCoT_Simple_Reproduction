class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(root):
    def get_height(node):
        if node is None:
            return (0, True)
        
        left_height, is_left_balanced = get_height(node.left)
        right_height, is_right_balanced = get_height(node.right)
        
        if not is_left_balanced or not is_right_balanced or abs(left_height - right_height) > 1:
            return (max(left_height, right_height) + 1, False)
        
        return (max(left_height, right_height) + 1, True)
    
    return get_height(root)[1]

# Example usage:
# Constructing a balanced binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(is_tree_balanced(root))  # Output: True

# Constructing an unbalanced binary tree
#       1
#      / 
#     2   
#    / 
#   3   
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

print(is_tree_balanced(root))  # Output: False
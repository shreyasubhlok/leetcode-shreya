# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time is o(n), n is nodes in tree
    space is o(h), h is height of the tree
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        # Define the initial bounds for the BST validation.
        low = -math.inf
        high = math.inf
        return self.validateHelper(root, low, high)

    def validateHelper(self, node: TreeNode, low: float, high: float) -> bool:
        if node is None:
            return True  # An empty subtree is a valid BST.

        if node.val <= low or node.val >= high:
            return False  # Check if the current node value is within the bounds or not.

        # Recursively check the left and right subtrees with updated bounds.
        return self.validateHelper(node.left, low, node.val) and self.validateHelper(node.right, node.val, high)

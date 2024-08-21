# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) != -1
        
    def Height(self, root):
        if root is None:
            return 0

        left_height = self.Height(root.left)
        right_height = self.Height(root.right)

        # Check if the subtree is balanced
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

        

     
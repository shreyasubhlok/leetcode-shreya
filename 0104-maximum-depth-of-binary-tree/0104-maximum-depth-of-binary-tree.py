# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #DFS- Mostly tree questions are DFS(stack recursion)
    #Time Complexity: O(n) - where n is the number of nodes in the binary tree.
    #Space Complexity: O(h) - where h is the height of the binary tree, and in the worst case(linear tree), it       could be O(n).
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1

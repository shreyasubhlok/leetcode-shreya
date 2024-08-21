# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Balanced binary tree meaning the heght difference between left and subtrees is AT MOST 1
    Time complexity: O(N),N is no of nodes in tree. Coz each node is visited once, the overall time complexity is linear i.e O(N).
    Space Complexity: O(H),H is the height of the tree. This could be bad as O(N) in a skewed tree or O(log N) in a balanced tree.
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) != -1 #The tree is balanced if the height function does not return -1
        
    def Height(self, root):
        if root is None:
            return 0

        left_height = self.Height(root.left)
        right_height = self.Height(root.right)

        # If either subtree is unbalanced, propagate the -1 upwards
        if left_height == -1 or right_height == -1:
            return -1

        # If the current node is unbalanced (height difference > 1), return -1
        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

        

     
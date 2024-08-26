# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Logic Explanation:
    Base Case 1: If both nodes p and q are None, return True since two empty trees are the same.
    Base Case 2: If one of them is None or their values don't match, return False.
    Recursive Case: Recursively check if both the left and right subtrees are the same.
    Time is o(n), n is nodes in tree
    space is o(h), h is height of the tree
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both nodes are None , they are same
        if p is None and q is None:
            return True
        
        #if one of them is None or values differes, they are different
        if p is None or q is None or p.val!=q.val:
            return False
        
        # Recursively check left and right subtrees
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
      
        if left_same and right_same:
            return True
        else:
            return False
        
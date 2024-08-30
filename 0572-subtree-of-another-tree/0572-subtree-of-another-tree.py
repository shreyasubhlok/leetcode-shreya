# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time complexity: o(n*m)!=o(n2) and space is o(h1+h2)
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True  # An empty subtree is always a subtree of any tree.

        if root is None:
            return False  # If root is empty but subRoot is not, subRoot can't be a subtree

        # Check if the current root matches subRoot, if yes, return True
        if self.isSame(root , subRoot):
            return True
        
        #check if subRoot is a subtree of either the left or right child of root?
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r: TreeNode, s: TreeNode) -> bool:
        if r == None and s == None:
            return True  # Both trees are empty, so they are identical
        
        if r == None or s == None:
            return False  # One tree is empty and the other is not, so they are not identical.

        # Check if current nodes match and recursively check the left and right subtrees
        return r.val == s.val and self.isSame(r.right, s.right) and self.isSame(r.left, s.left)

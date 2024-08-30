# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n) - where n is the number of nodes in the binary tree.
    # Space Complexity: O(h) - where h is the height of the binary tree.
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)

    # Helper function to check if two subtrees are mirrors of each othe
    def isMirror(self, p: TreeNode, q: TreeNode) -> bool:
        # If both subtrees are empty, they are mirrors
        if p is None and q is None:
            return True

        # If only one of the subtrees is empty, they are not mirrors
        if p is None or q is None:
            return False

        # If the values at the current nodes are different, they are not mirrors
        if p.val != q.val:
            return False

        # Recursively check if the left subtree of p is a mirror of the right subtree of q, and vice versa
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    
'''
Execution:

1.isSymmetric(root) is called with the root node (1).
2. Since root is not None, it calls isMirror(root, root) with the same root node.
3.In isMirror(p, q), p and q are both 1. The values match, so it recursively checks isMirror(p.left, q.right) and isMirror(p.right, q.left).
Next, p = 2 (left child of 1), q = 2 (right child of 1). The values match, so it checks isMirror(p.left, q.right) and isMirror(p.right, q.left).
Now, p = 3 (left child of left 2), q = 3 (right child of right 2). The values match, and both children of these nodes are None, so the recursion returns True.
4.Similarly, it checks p = 4 (right child of left 2), q = 4 (left child of right 2) and returns True.
5.Since all checks are True, the tree is symmetric, and the final result is True.
'''

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#https://www.youtube.com/watch?v=_-QHfMDde90 - reference (striver)
class Solution:
    # Time complexity: O(N),N is no of nodes in tree. .
    # Space Complexity: O(H),H is the height of the tree.
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None or root == p or root == q:
            return root
        # Recursive search for p and q in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # If the left subtree returned None, it means p and q are not found in the left subtree.Therefore, the answer must be in the right subtree.
        if left == None:
            return right
        elif right == None:  # if the right subtree returned None, the answer must be in the left subtree.
            return left
        else:
            return root  # If both left and right are not None, it means p and q were found in both subtrees.Hence, the current node is the LCA.

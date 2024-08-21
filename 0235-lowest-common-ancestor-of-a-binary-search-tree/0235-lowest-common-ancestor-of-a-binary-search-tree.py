# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # time complexity: O(h)<o(n) - h is height of BST and n is no of nodes. In worst case o(h)=o(n) when all nodes on left (linear tree)
        # space complexity : o(n)- due to the space used by the recursive call stack
        if root == None:  # Base case: If root is null, return null
            return None

        curr = root.val
        if curr < p.val and curr < q.val:  # Case 1: Both nodes are on the right subtree
            return self.lowestCommonAncestor(root.right, p, q)

        if curr > p.val and curr > q.val:  # Case 2: Both nodes are on the left subtree
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 3 and 4: One node is on the left and the other on the right, or one of the nodes is the current root
        return root

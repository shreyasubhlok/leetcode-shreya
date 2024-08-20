# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #time is o(N) where N is nodes in the tree
    #space is o(H), where H is height of the tree (determined by the maximum depth of the recursion stack, which is proportional to      the height of the tree)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is None, simply return None
        # This handles the case where we've reached beyond the leaf nodes
        if root is None:
            return None

        # Swap the left and right children of the current node
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the left subtree
        # After swapping, the original right subtree has become the left subtree
        self.invertTree(root.left)

        # Recursively invert the right subtree
        # After swapping, the original left subtree has become the right subtree
        self.invertTree(root.right)

        #return root with it's subtrees inverted
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #DFS apprach
    # Time complexity: O(n), where n is the number of nodes in the tree
    # Space complexity: O(h), where h is the height of the tree (due to the recursion stack)
    '''
    Diameter of a tree definition: The diameter is the longest path between any two nodes in a tree.
    This path may or may not pass through the root of the tree.
    '''
    def __init__(self):
        self.diameter = 0  # Initialize diameter as a class attribute to track the maximum diameter found

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root) #DFS traversal to calculate height and update the diameter
        return self.diameter # Return the maximum diameter found

    def height(self, root) -> int:
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # Update the diameter: this is the sum of the heights of the left and right subtrees
        self.diameter = max(self.diameter, left_height + right_height)

        # Return the height of the current node, which is 1 + the height of the taller subtree
        return 1 + max(left_height, right_height)
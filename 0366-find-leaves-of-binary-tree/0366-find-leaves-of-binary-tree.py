# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Time: O(n) and space O(n)
    Algo:
    Post-order Traversal: Recursively calculate the height of each node (max(leftHeight, rightHeight) + 1).
    Group by Height: Use the height to group nodes in a result list.
    Return Result: The grouped list contains leaves in the order they are removed.
    '''

    def findLeaves(self, root: TreeNode) -> list[list[int]]:
        result = []

        def getHeightOfNode(node):
            if node is None:
                return -1  # Base case: height of an empty node is -1

            # Recursively get the height of the left and right children
            leftHeight = getHeightOfNode(node.left)
            rightHeight = getHeightOfNode(node.right)

            # Current node's level is 1 + the max height of its children
            level = max(leftHeight, rightHeight) + 1

            # Ensure the result list has enough sublists for the current level
            if len(result) == level:
                result.append([])

            # Add the current node's value to the corresponding level
            result[level].append(node.val)

            return level  # Return the height of the current node

        # Start the recursive function from the root
        getHeightOfNode(root)

        return result
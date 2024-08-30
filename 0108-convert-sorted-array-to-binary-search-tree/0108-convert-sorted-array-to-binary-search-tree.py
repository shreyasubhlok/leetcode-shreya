# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
      time complexity = o(n), The sortedArrayToBST method processes each element of the 
      nums array exactly once
      space complexity= olog(n), O(log n) for a balanced binary search tree (BST): The recursion
      stack depth is proportional to the height of the tree. For a balanced BST, the height is
      O(log n), where n is the number of elements in the array.
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.isHelper(nums, 0, len(nums) - 1)

    def isHelper(self, nums: List[int], left: int, right: int) -> TreeNode:
        '''
        Helper function to build the BST recursively.

        :param nums: List of integers.
        :param left: Left index of the current subarray.
        :param right: Right index of the current subarray.
        :return: Root of the subtree built from the subarray.
        '''
        # Base case: if the left index exceeds the right index, return None
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid]) 
        root.left = self.isHelper(nums, left, mid - 1)
        root.right = self.isHelper(nums, mid + 1, right)

        return root
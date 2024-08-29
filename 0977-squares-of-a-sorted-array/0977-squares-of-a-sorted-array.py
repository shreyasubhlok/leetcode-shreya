class Solution:
    # two pointer approach
    # time is o(n)-in place comparison and space is o(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize the result list with zeros, the same size as the input list
        res = [0] * len(nums)

        start = 0
        end = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):  # reverse order iteration (from the last index to the first)
            # Compare the absolute values of the elements at the start and end pointers.
            # The larger square will be placed at the current index `i` in the result list.
            if abs(nums[start]) > abs(nums[end]):
                res[i] = nums[start] * nums[start]  # Square the start element and place it at the current index
                start = start + 1  # Move the start pointer to the right
            else:
                # If the element at the end pointer is larger or equal in absolute value
                res[i] = nums[end] * nums[end]  # Square the end element and place it at the current index.
                end = end - 1  # Move the end pointer to the left.

        return res
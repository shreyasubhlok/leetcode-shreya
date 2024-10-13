from typing import List
import math


class Solution:
    #Time: o(n)
    #Space: o(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # If the sum of the entire array is less than the target, no subarray can meet the condition, so return 0.
        if sum(nums) < target:
            return 0

        # Initialize pointers for the sliding window (i and j),
        # windowsum to keep track of the current window's sum,
        # and minlen to store the minimum length of the subarray found (initialized to infinity).
        i = 0  # Left pointer
        j = 0  # Right pointer
        windowsum = 0  # Current window sum
        minlen = float("inf")  # To track the minimum subarray length

        # Start the sliding window process, moving the right pointer (j).
        while j < len(nums):
            windowsum = windowsum + nums[j]  # Expand the window by adding the current element

            # Shrink the window from the left while the sum is greater than or equal to the target
            while windowsum >= target:
                currlen = j - i + 1  # Calculate the current window length
                minlen = min(minlen, currlen)  # Update the minimum length if the current one is smaller
                windowsum = windowsum - nums[i]  # Shrink the window from the left
                i = i + 1  # Move the left pointer to the right

            j = j + 1  # Move the right pointer to expand the window

        # If no valid subarray was found, return 0, otherwise return the minimum length.
        if minlen == float("inf"):
            return 0
        else:
            return minlen


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    res = sol.minSubArrayLen(target, nums)
    print("209. Minimum Size Subarray Sum: ", res)

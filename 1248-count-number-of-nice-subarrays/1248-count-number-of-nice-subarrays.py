from typing import List


class Solution:
    # Time is o(n)
    # Space is o(1)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize the sliding window pointers and counters
        i = 0  # 'i' is the start pointer (shrink window)
        j = 0  # 'j' is the end pointer (expand window)
        oddcount = 0
        finalcount = 0  # To store the total number of 'nice' subarrays found
        tempcount = 0  # Temporary counter to count subarrays that end at index 'j'

        # Expand the window using 'j'
        while j < len(nums):
            # If nums[j] is odd, increment the oddcount and reset tempcount
            # tempcount is to keep track of only valid subarrays
            if nums[j] % 2 != 0:
                oddcount = oddcount + 1
                tempcount = 0

            # Once we have exactly 'k' odd numbers, start shrinking the window from the left
            while oddcount == k:
                # Increment tempcount, since the subarray from 'i' to 'j' is valid
                tempcount = tempcount + 1
                # If nums[i] is odd, reduce the oddcount before moving 'i'
                if nums[i] % 2 != 0:
                    oddcount = oddcount - 1
                # Shrink the window by moving the 'i' pointer to the right
                i = i + 1

            # Add the number of valid subarrays ending at 'j' to the final count
            finalcount = finalcount + tempcount
            j = j + 1  # Move the 'j' pointer to the right to expand the window

        return finalcount

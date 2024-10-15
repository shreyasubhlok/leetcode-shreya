class Solution:
    # sliding window fixed length
    # Time is o(n) and space is o(n)
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mySet = set()  # Set to store unique elements within the sliding window
        i = 0  # slinding window start pointer
        j = 0  # slinding window end pointer
        maxsum = 0
        windowsum = 0

        while j < len(nums):
            # If the current element (nums[j]) is not in the set, add it to the window (expand)
            if nums[j] not in mySet:
                mySet.add(nums[j])  # add to track unique elements
                windowsum = windowsum + nums[j]

                # Check if the current window has exactly k element, update maxsum
                if len(mySet) == k:
                    maxsum = max(maxsum, windowsum)
                    mySet.remove(nums[i])  # Subtract nums[i] from the window sum
                    windowsum = windowsum - nums[i]  # Remove the leftmost element to slide the window forward
                    i = i + 1

                j = j + 1  # Expand the window by moving the right pointer forward
                
            else:
                # If nums[j] is already in the set (duplicate element), shrink the window
                mySet.remove(nums[i])  # Remove nums[i] from the set to remove the duplicate
                windowsum = windowsum - nums[i]  # Subtract nums[i] from the window sum
                i = i + 1  # Move the left pointer forward to shrink the window

        return maxsum

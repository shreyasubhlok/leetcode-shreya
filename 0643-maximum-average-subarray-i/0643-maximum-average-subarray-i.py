class Solution:
    #Slidinf window fixed size problem
    # Time : o(n)
    # space:o(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return -1
        windowSum = 0
        # Calculate the sum of the first 'k' elements (initial window)
        for i in range(k):
            windowSum = windowSum + nums[i]
        maxsum = windowSum  # Initialize maxSum with the sum of the first window

        # Slide the window across the array and calculate new sums
        for i in range(k, len(nums)):  # start from kth index i.e 4 and The loop iterates from k to len(nums) - 1
            windowSum = windowSum + nums[i] - nums[i - k]
            maxsum = max(windowSum, maxsum)
        return maxsum / k  # Use normal division to return a float. '//' is integer division and truncates the decimal portion.


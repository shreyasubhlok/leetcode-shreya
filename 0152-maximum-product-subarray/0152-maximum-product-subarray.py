class Solution:
    # Time Complexity: O(n), where n is the length of the input array `nums`. We iterate through the list once.
    # Space Complexity: O(1), as we are using only a constant amount of extra space for variables `currMax`, `currMin`, and  `res`.
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Observe the patterns..1.all positive...2.positive with some negative....3.zeros multiply.
        It's kind of DP problem as we are maintaining the currmin and currmax at each num[i] iteration. Coz of negative no it's DB. Otherwise it 
        could have been a sliding window problem.
        currMin is crucial here because a negative number can turn a previously small product into a large positive one.
        
        Summary Cheat Sheet:
        Track currMax and currMin for flips.
        Reset on zero.
        Check "new-start-or-flip" (num, num * currMax, num * currMin).
        Update res as the "best score."
        '''
        # Initialize the result with the maximum element in the array, to handle cases of all negative numbers or a single number
        res = max(nums)

        # Initialize current maximum and minimum products to 1 (neutral for multiplication)
        currMax = 1
        currMin = 1
        for num in nums:
            # Reset current max and min to 1 if we encounter a zero (a break in the product sequence)
            if num == 0:
                currMax = 1
                currMin = 1
                continue  # Skip further calculations for this zero

            # Store current max product in a temporary variable for calculation of currMin
            temp = num * currMax
            # Update currMax and currMin with the maximum and minimum of three cases:
            # 1. num itself (starting a new subarray)
            # 2. num * currMax (extending the max product)
            # 3. num * currMin (considering the min product in case of a negative num)
            currMax = max(num, temp, num * currMin)
            currMin = min(num, temp, num * currMin)
            res = max(res, currMax)  # Update the result with the highest product encountered so far

        return res




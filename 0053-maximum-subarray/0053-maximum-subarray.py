class Solution:
    #time complexity: o(n) and space is o(1) -Kadan's algorithm (dynamic programming technique)
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]  # Initialize maxSum with the first element
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = nums[i]  # Start a new subarray if currSum is negative
            else:
                currSum = currSum + nums[i]  # Continue with the existing subarray
            maxSum = max(currSum, maxSum)  # Update maxSum if currSum is greater

        return maxSum
        
'''
Dry Run:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Index	Element	currSum Calculation	currSum	maxSum
0	-2	Initial value	-2	-2
1	1	max(1, -2 + 1) = 1	1	1
2	-3	max(-3, 1 + (-3)) = -2	-2	1
3	4	max(4, -2 + 4) = 4	4	4
4	-1	max(-1, 4 + (-1)) = 3	3	4
5	2	max(2, 3 + 2) = 5	5	5
6	1	max(1, 5 + 1) = 6	6	6
7	-5	max(-5, 6 + (-5)) = 1	1	6
8	4	max(4, 1 + 4) = 5	5	6
Output: maxSum = 6 (which is the sum of subarray [4,-1,2,1])
'''

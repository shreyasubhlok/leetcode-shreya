class Solution:
    # Time Complexity: O(n^2) - We iterate over each pair of elements (i, j) with nested loops.
    # Space Complexity: O(n) - We use a DP array of size n to store the LIS values.
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        # Initialize a DP array where each element starts with a length of 1,
        # because the minimum LIS ending at each element is the element itself
        dp = [1] * len(nums)

        # Loop through each element in nums, starting from the second element
        for i in range(1, len(nums)):
            # For each nums[i], check all previous elements nums[j] (j < i)
            for j in range(i):
                # If nums[i] can extend the increasing subsequence ending at nums[j]
                if nums[i] > nums[j]:
                    # Update dp[i] to be the maximum of its current value
                    # and the LIS length ending at nums[j] + 1 (including nums[i])
                    dp[i] = max(dp[i], dp[j] + 1)


        # The length of the longest increasing subsequence is the maximum value in dp
        return max(dp)


sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
res = sol.lengthOfLIS(nums)
print("300. Longest Increasing Subsequence: ", res)


'''
Main Loop:

For each element nums[i], look back at all previous elements nums[j] (where j < i).
If nums[i] > nums[j], it means nums[i] can extend the LIS ending at nums[j].
Update dp[i] to be the maximum of its current value and dp[j] + 1.
Result: The longest increasing subsequence length for the entire list is the maximum value in dp, so max(dp) gives the answer.


'''
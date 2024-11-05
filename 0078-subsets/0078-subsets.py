from typing import List


class Solution:
    #Time is O(2^n), 2 choices and n is no of elements
    #Space Complexity: o(n), for the recursive call stack depth
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list to store all subsets
        res = []
        # Temporary list to hold the current subset
        subset = []

        # Define the backtracking function
        def backtrack(i):
            # Base case: if we reach the end of the nums list
            if i >= len(nums):
                # Add a copy of the current subset to the result list
                res.append(subset.copy())
                return
            # Include nums[i] in the subset and move to the next element
            subset.append(nums[i])
            backtrack(i + 1)

            # Exclude nums[i] from the subset (backtrack) and explore the next option
            subset.pop()
            backtrack(i + 1)

        # Start the backtracking from the first element
        backtrack(0)
        return res


sol = Solution()
nums = [1, 2, 3]
res = sol.subsets(nums)
print("78. Subsets: ", res)


'''
Explanation of Each Part
1. Initialization: res is used to collect all subsets, and subset temporarily holds the current subset.
2. Backtracking Function backtrack(i):
   - Base Case: When i equals the length of nums, add a copy of the subset list to res.
   - Recursive Steps:
       Include Current Element: Add nums[i] to subset, call backtrack(i + 1) to explore further choices with this element included.
       Exclude Current Element: Remove nums[i] from subset using subset.pop(), then call backtrack(i + 1) to explore choices without the current element.
3.Result: After all calls complete, res contains every possible subset of nums.


Key Pointers to Remember
1. Include-Exclude Pattern: For each element, make two recursive calls – one including it in the subset and one excluding it.
2. Backtracking after Adding: Add to the subset and backtrack, then remove it to backtrack properly.
3. Use Copy for Final Subsets: Always add a copy of subset to res to avoid modifications in later recursive calls.
4. Base Case Importance: Ensure that the base case correctly defines when to add the subset to res and end recursion.
'''
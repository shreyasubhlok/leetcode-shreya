class Solution:
    # Time: O(2^n+nlogn)=~ O(2^n)
    # space: O(n*2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort nums to ensure that duplicates are adjacent
        nums.sort()
        # Initialize result list to store all unique subsets
        res = []
        # Temporary list to hold the current subset
        subset = []

        # Define the backtracking function
        def backtrack(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                # Add a copy of the current subset to the result list
                res.append(subset.copy())
                return

            # Include nums[i] in the subset
            subset.append(nums[i])
            # Move to the next element
            backtrack(i + 1)
            # Backtrack by removing the last element from the subset
            subset.pop()

            # Skip over any duplicate elements
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # Exclude nums[i] and move to the next unique element
            backtrack(i + 1)

        # Start backtracking from the first element
        backtrack(0)
        return res


# Test case
sol = Solution()
nums = [1, 2, 2, 3]
res = sol.subsetsWithDup(nums)
print("Subsets with duplicates handled:", res)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         # Initialize the result list
        result = []
        
        # Define a helper function for backtracking
        def backtrack(current_permutation):
            # Check if the current permutation is complete
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])  # Add a copy of the current permutation
                return
            
            # Iterate over each number in nums
            for num in nums:
                # Skip if the number is already in the current permutation
                if num in current_permutation:
                    continue
                # Add the number to the current permutation
                current_permutation.append(num)
                # Recurse to build further
                backtrack(current_permutation)
                # Remove the last number to backtrack
                current_permutation.pop()
        
        # Start the backtracking with an empty permutation
        backtrack([])
        return result
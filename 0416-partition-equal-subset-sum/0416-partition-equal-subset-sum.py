class Solution:
    # time : O(n * S), where n is the number of elements in nums, and S is the target sum (which is half the sum of all elements in nums).
    # O(S), where S is the target sum.
    def canPartition(self, nums: List[int]) -> bool:
        # Step 1: Check if the sum of nums is even. If it's odd, partitioning into equal subsets is impossible.
        if sum(nums) % 2 != 0:
            return False

        # Step 2: Initialize a set to store reachable subset sums.
        dp = set()
        dp.add(0)  # Start with zero as a reachable sum

        # The target sum for each subset is half of the total sum of nums.
        target = sum(nums) // 2

        # Step 3: Iterate over each number in nums in reverse order.
        for i in range(len(nums) - 1, -1, -1):
            # Create a new set to store the updated subset sums for the current iteration.
            nextDp = set()

            # Step 4: For each reachable sum t in the current dp set:
            # - Add t + nums[i] to nextDp (considering the current number)
            # - Add t to nextDp (ignoring the current number)
            for t in dp:
                nextDp.add(t + nums[i])  # Include current number
                nextDp.add(t)  # Exclude current number

            # Update dp to be the new set of reachable subset sums for the next iteration.
            dp = nextDp

        # Step 5: If the target sum is in dp, then we can partition nums into two subsets with equal sum.
        if target in dp:
            return True
        else:
            return False
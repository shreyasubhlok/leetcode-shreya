from typing import List

class Solution:
    #Time is O(n) and space is O(1)
    def firstMissingPositive(self,nums:List[int])->int:
        if len(nums)==0:
            return 0

        n = len(nums)  # Get the length of the array

        for i in range(n):
            # Place each number in its correct position
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            # Find the first position where the number is not i+1
            if nums[i] != i + 1:
                return i + 1  # Return the missing positive integer

        return n + 1  # If all numbers are in place, return n+1


sol=Solution()
nums = [3,4,-1,1]
res=sol.firstMissingPositive(nums)
print("41. First Missing Positive: ",res)
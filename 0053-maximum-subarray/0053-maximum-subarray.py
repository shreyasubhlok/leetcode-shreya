class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=nums[0]
        for i in range(len(nums)):
            if currSum < 0:
                currSum=nums[i]
            else:
                currSum=currSum+nums[i]
            maxSum=max(currSum,maxSum)
        
        return maxSum
        
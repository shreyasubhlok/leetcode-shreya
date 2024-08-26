class Solution:
    #time is o(n)
    #space is o(1)
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum=0
        for num in nums:
            actualSum=actualSum+num
        
        return expectedSum-actualSum
        
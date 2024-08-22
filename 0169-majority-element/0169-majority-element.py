class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #using sorting
        nums.sort()
        n=len(nums) // 2
        return nums[n]
    
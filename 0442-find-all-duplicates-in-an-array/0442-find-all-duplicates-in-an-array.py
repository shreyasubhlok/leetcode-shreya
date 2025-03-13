class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=[]
        i=0
        while i < len(nums):
            val = abs(nums[i])
            if nums[val-1] < 0:
                duplicates.append(val)
            else:
                nums[val-1] = -nums[val-1]
            i += 1
        return duplicates
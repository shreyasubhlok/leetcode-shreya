class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        if len(nums)==1 or nums[0]<nums[len(nums)-1]:
            return nums[0]
        
        start=0
        end=len(nums)-1
        
        while start<end:
            mid= (start+end) // 2
            if nums[mid]<nums[end]:
                end=mid
            else:
                start=mid+1
                
        return nums[start]
                
            
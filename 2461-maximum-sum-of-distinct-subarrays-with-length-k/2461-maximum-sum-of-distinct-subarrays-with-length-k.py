class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mySet=set()
        i=0
        j=0
        maxsum=0
        windowsum=0
        
        while j<len(nums):
            if nums[j] not in mySet:
                mySet.add(nums[j])
                windowsum=windowsum+nums[j]
                
                if len(mySet)==k:
                    maxsum=max(maxsum,windowsum)
                    mySet.remove(nums[i])
                    windowsum=windowsum-nums[i]
                    i=i+1
                
                j=j+1
            else:
                mySet.remove(nums[i])
                windowsum=windowsum-nums[i]
                i=i+1
                
                
        return maxsum
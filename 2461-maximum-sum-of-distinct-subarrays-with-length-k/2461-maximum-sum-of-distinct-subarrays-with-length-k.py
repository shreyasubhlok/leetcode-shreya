class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return 0
        maxsum=0
        windowsum=0
        hm={}
        for i in range(k):
            if nums[i] not in hm:
                hm[nums[i]]=1
            else:
                hm[nums[i]]=hm[nums[i]]+1
            windowsum+=nums[i]
            if len(hm)==k:
                maxsum=windowsum
                break
        
        i=k
        while i<len(nums):
            toRemove=nums[i-k]
            hm[toRemove]-=1
            if hm[toRemove]==0:
                del hm[toRemove]  
            curr=nums[i]
            if curr not in hm:
                hm[nums[i]]=1
            else:
                hm[nums[i]]=hm[nums[i]]+1
            windowsum=windowsum+curr-toRemove
            if len(hm)==k:
                maxsum=max(windowsum,maxsum)
            i=i+1
            
        return maxsum
            
            
            
                
        
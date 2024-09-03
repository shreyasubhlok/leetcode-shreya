class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            
            while start<end:
                sum=nums[i]+nums[start]+nums[end]
                if sum<0:
                    start=start+1
                elif sum>0:
                    end=end-1
                else:
                    temp=[nums[i],nums[start],nums[end]]
                    res.append(temp)
                    start=start+1
                    end=end-1
                
                    while start<end and nums[start]==nums[start-1]:
                        start=start+1
                    while start<end and nums[end]==nums[end+1]:
                        end=end-1
          
                    
        return res
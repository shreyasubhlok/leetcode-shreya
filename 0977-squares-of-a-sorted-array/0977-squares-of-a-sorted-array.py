class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start=0
        end=len(nums)-1
        res=[0]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[start])<abs(nums[end]):
                res[i]=nums[end]*nums[end]
                end=end-1
            else:
                res[i]=nums[start]*nums[start]
                start=start+1
                
        return res
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Observe the patterns..1.all positive...2.positive with some negative....3.zeros multiply
        It's kind of SP problem as we are mainitainign th
        '''
        res=max(nums)
        currMax=1
        currMin=1
        for num in nums:
            if num==0:
                currMax=1
                currMin=1
            
            temp=num*currMax
            currMax=max(num,temp,num*currMin)
            currMin=min(num,temp,num*currMin)
            res=max(res,currMax)
            
        return res
        
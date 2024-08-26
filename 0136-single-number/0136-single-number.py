class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans=ans^num
        return ans
        
    
    #time complexity = o(n)
    #space complexity =o(n)
    def singleNumberUsingHashSet(self, nums: List[int]) -> int:
        mySet=set()
        for num in nums:
            if num in mySet:
                mySet.remove(num)
            else:
                mySet.add(num)
                
        return mySet.pop()
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mySet=set()
        for num in nums:
            if num in mySet:
                mySet.remove(num)
            else:
                mySet.add(num)
                
        return mySet.pop()
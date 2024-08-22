class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myMap={}
        for num in nums:
            if num in myMap:
                return True
            else:
                myMap[num]=1
        
        return False
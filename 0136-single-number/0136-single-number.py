class Solution:
    #Preferred Solution-Bitwise XOR
    '''
    Time:o(n) and space o(1)
    Logic:
     # XOR each number with the current result
     # This works because XOR of a number with itself cancels out to 0,
     # and XOR with 0 leaves the number unchanged. 
     # Thus, all numbers appearing twice cancel out, leaving only the unique number.
     Example- 
     nums=[2,2,1]
     i=0, ans=ans^nums[0]=0^2=2
     i=1, ans=ans^nums[1]=2^2=0
     i=2, ans=ans^nums[2]=0^1=1 (all duplictes will cancel out in the end)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        ans=0 # Initialize the result variable to 0
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
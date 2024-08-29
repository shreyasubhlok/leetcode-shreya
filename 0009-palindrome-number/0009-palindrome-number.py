class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : 
            return False
        
        orignalNo=abs(x)
        reverseNo=0
        
        while x!=0:
            rem=x%10
            reverseNo=reverseNo*10+rem
            x=x//10
        
        return  orignalNo==reverseNo
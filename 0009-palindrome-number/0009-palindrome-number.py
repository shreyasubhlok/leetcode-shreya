class Solution:
    #Time Complexity: O(log10(n)) and Space Complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        orignalNo = abs(x)
        reversedNo = 0

        while x != 0:
            remainder = x % 10  # Get the last digit of the number
            reversedNo = reversedNo * 10 + remainder # Build the reversed number
            x = x // 10 # Remove the last digit from the original number

        return orignalNo == reversedNo

    def isPalindromeUsingStringConcept(self, x:int)->bool:
        s=str(x)
        if s==s[::-1]:
            return True
        return False


'''
res=0

x=125
125 != 0 :
   rem=125%10 = 5
   res=0*10+5=5
   x=x//10=125//10=12

12 != 0 :
   rem=12%10=2
   res=5*10+2=52
   x=x//10=1

1!=0:
    rem=1%10=1
    res=52*10+1=521
    x=0
out of while loop

res=521
orignalNo = 125

521 != 125 so False


'''


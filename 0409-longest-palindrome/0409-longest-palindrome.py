class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        oddcount=0
        myMap={}
        for ch in s:
            if ch in myMap:
                myMap[ch]=myMap[ch]+1
            else:
                myMap[ch]=1
                
        for value in myMap.values():
            if value%2==0:
                res=res+value
            else:
                res=res+value-1
                oddcount=1
        
        
        return oddcount+res
        
        
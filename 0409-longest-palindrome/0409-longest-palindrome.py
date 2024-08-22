class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        mySet=set()
        for ch in s:
            if ch in mySet:
                res=res+2
                mySet.remove(ch)
            else:
                mySet.add(ch)
                
        if len(mySet)>0:
            res=res+1
        
        return res
        
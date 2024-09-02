class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        i=0
        maxLen=0
        myMap={}
        
        for j in range(len(s)):
            if s[j] in myMap:
                i=max(i,myMap[s[j]]+1)
            myMap[s[j]]=j
            currLen=j-i+1
            maxLen=max(maxLen,currLen)
            
        
        return maxLen
            
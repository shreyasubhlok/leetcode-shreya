class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        i=0
        j=0
        myset=set()
        maxlen=0
        
        while j<len(s):
            if s[j] not in myset:
                myset.add(s[j])
                currlen=len(myset)
                maxlen=max(currlen,maxlen)
                j=j+1
            else:
                myset.remove(s[i])
                i=i+1
        return maxlen
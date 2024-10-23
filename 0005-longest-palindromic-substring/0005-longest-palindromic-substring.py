class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""

        res=""
        maxlen=0
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                currlen=right-left+1
                if currlen>maxlen:
                    maxlen=currlen
                    res=s[left:right+1]
                left=left-1
                right=right+1

            left=i
            right=i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currlen = right - left + 1
                if currlen > maxlen:
                    maxlen = currlen
                    res=s[left:right+1]
                left = left - 1
                right = right + 1


        return res
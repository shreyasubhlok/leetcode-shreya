class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left, right, res, maxlen):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currlen = right - left + 1
                if currlen > maxlen:
                    maxlen = currlen
                    res = s[left:right + 1]
                left = left - 1
                right = right + 1
            return res, maxlen

        if len(s) == 0:
            return s
        res = ""
        maxlen = 0

        for i in range(len(s)):
            # oddcheck
            res, maxlen = expandFromCenter(i, i, res, maxlen)

            # evencheck
            res, maxlen = expandFromCenter(i, i + 1, res, maxlen)

        return res
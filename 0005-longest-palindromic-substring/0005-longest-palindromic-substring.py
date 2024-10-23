class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left, right):
            nonlocal res, maxlen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

        if len(s) == 0:
            return ""

        res = ""
        maxlen = 0
        
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            expandFromCenter(i, i)
            # Even length palindromes (two characters center)
            expandFromCenter(i, i + 1)

        return res


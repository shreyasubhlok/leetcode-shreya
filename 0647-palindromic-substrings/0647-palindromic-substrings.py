class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        def countPalindrome(left, right, res):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = res + 1
                left = left - 1
                right = right + 1
            return res


        res = 0
        for i in range(len(s)):
            # odd length
            res = countPalindrome(i, i, res)

            # even length
            res = countPalindrome(i, i + 1, res)

        return res
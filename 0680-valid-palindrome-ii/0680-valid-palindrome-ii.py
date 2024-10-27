class Solution:
    #time o(n) and space o(1)
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        def checkPalindrome(s, i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(s, i, j - 1) or checkPalindrome(s, i + 1, j)
            i += 1
            j -= 1

        return True

class Solution:
    # Time is o(n2) , o(n) for forloop and o(n) for expandfromceneter call . o(n)*o(n)=o(n2)
    # space is o(1)
    def longestPalindrome(self, s: str) -> str:
        # Base case: If the input string is empty, return it as is.
        if len(s) == 0:
            return s

        # Helper function to expand around the center (for both odd and even palindromes)
        def expandFromCenter(left, right, res, maxlen):
            # Expand as long as the left and right pointers are within bounds and characters are equal.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currlen = right - left + 1
                # If the current palindrome is longer than the max found so far, update the result.
                if currlen > maxlen:
                    maxlen = currlen
                    res = s[left:right + 1]  # Update result with the current palindrome substring.
                left = left - 1  # Move left pointer outwards.
                right = right + 1  # Move right pointer outwards.
            return res, maxlen

        res = ""
        maxlen = 0

        for i in range(len(s)):
            # Odd-length palindromes (single character center at i).
            res, maxlen = expandFromCenter(i, i, res, maxlen)

            # Even-length palindromes (two consecutive characters as center).
            res, maxlen = expandFromCenter(i, i + 1, res, maxlen)

        return res


class Solution:
    # Time is o(n2) , o(n) for forloop and o(n) for expandfromceneter call . o(n)*o(n)=o(n2)
    # space is o(1)
    def countSubstrings(self, s: str) -> int:
        # Base case: If the input string is empty, return 0 since there are no substrings.
        if len(s) == 0:
            return 0

        # Helper function to count palindromic substrings expanding from the center
        def countPalindrome(left, right, res):
            # Expand as long as the left and right pointers are within bounds and characters are equal.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res = res + 1
                left = left - 1 # Move the left pointer outward.
                right = right + 1 # Move the right pointer outward.
            return res


        res = 0
        for i in range(len(s)):
            # Count odd-length palindromic substrings (single character center at i).
            res = countPalindrome(i, i, res)

            # Count even-length palindromic substrings (two consecutive characters as center)
            res = countPalindrome(i, i + 1, res)

        return res


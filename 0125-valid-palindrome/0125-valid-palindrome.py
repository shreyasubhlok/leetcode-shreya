class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(1), constant space used beyond input.

        Algorithm:
        - Use two pointers (`i` from the start and `j` from the end) to compare characters.
        - Skip non-alphanumeric characters(?,#,*,@ and even whitespace) by moving pointers (`i` and `j`) accordingly.
        - Compare characters ignoring case sensitivity using `s[i].lower() == s[j].lower()`.
        - Return True if the entire string is a palindrome, False otherwise.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i = i + 1
                continue

            if not s[j].isalnum():
                j = j - 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i = i + 1
            j = j - 1
        return True

'''
isalnum() Method vs isalpha() Method
Key Differences:
isalnum() allows both letters and numbers, while isalpha() allows only letters.
Strings with digits (e.g., "123") will return True with isalnum() but False with isalpha().


Why Use isalnum():
isalnum() checks if a character is either a letter (alphabetic) or a digit (numeric). This is important because the problem specifies that the palindrome check should consider both letters and numbers.
isalpha(), on the other hand, only checks if a character is a letter. It would ignore numeric characters, which are still relevant to the palindrome check.
'''
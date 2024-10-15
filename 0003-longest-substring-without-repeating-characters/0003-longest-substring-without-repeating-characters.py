class Solution:
    # Time is o(n) and space is o(n)
    # sliding window technique
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize two pointers, i and j, to represent the current window's start and end
        i = 0  # Start of the sliding window
        j = 0  # End of the sliding window
        mySet = set()  # Set to store unique characters in the current window
        maxlen = 0  
        
        # Traverse the string using the 'j' pointer
        while j < len(s):
            # If the current character at 'j' is not already in the set, it means no repetition
            if s[j] not in mySet:
                mySet.add(s[j])  # Add the character to the set (expanding the window)
                # Update maxlen with the length of the current window (size of the set)
                maxlen = max(maxlen, len(mySet))
                j = j + 1  # Move the 'j' pointer to expand the window
            else:
                # If the character at 'j' is already in the set (repetition found),
                # Remove the character at 'i' (start of the window) to shrink the window
                if s[i] != s[j] or s[i] == s[j]:
                    mySet.remove(s[i])
                i = i + 1  # Move the 'i' pointer to shrink the window

        return maxlen
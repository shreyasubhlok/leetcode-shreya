class Solution:
    # Time is o(n) and space is o(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = 0  # Initialize the starting index of the current window
        maxLen = 0
        myMap = {}

        for j in range(len(s)):
            # If the current character is already in the map, it means we found a repeating character
            if s[j] in myMap:
                # Update the start of the window (i) to be the maximum of the current i
                # and one position after the last occurrence of the current character
                # This ensures that i only moves forward and doesn't move backward
                i = max(i, myMap[s[j]] + 1)

            myMap[s[j]] = j  # update the current character's index in the map
            currLen = j - i + 1  # Calculate the length of the current window (substring without repeating characters)
            maxLen = max(maxLen, currLen)

        return maxLen

            
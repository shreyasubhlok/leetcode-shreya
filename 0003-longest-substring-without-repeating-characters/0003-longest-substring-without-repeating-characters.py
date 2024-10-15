class Solution:
    # Time is o(n) and space is o(n)
    # sliding window technique- variable length
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i = 0  # start pointer of the sliding window
        j = 0  # end pointer of the sliding window
        myset = set()  # Set to store unique characters in the current window
        maxlen = 0

        # Traverse the string using the end pointer
        while j < len(s):
            # If the current character at index end is not in the set
            if s[j] not in myset:
                myset.add(s[j])  # Add the character to the set (expand the window)
                currlen = len(myset)  # Calculate the current length of the substring
                # Update maxlen if the current length is greater
                maxlen = max(currlen, maxlen)
                j = j + 1
            else:
                # If the character is a duplicate (already in the set)
                # Remove the character at index start (shrink the window)
                myset.remove(s[i])
                i = i + 1

        return maxlen

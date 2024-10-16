class Solution:
    # Sliding window variable length
    # time is o(n) and space is o(n)
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) == 0:
            return 0

        i = 0  # Left pointer for the sliding window
        j = 0  # Right pointer for the sliding window
        maxlen = 0
        hm = {}
        maxFreq = 0

        # Iterate with the right pointer j over each character in the string
        while j < len(s):
            # Add character to the hashmap and update its frequency
            if s[j] not in hm:
                hm[s[j]] = 1
            else:
                hm[s[j]] += 1

            # Update the maximum frequency of a single character in the current window
            maxFreq = max(maxFreq, hm[s[j]])

            # Shrink the window from the left if it is no longer valid
            while (j - i + 1) - maxFreq > k:
                hm[s[i]] -= 1
                i += 1

            # Calculate maxlen after ensuring the window is valid
            maxlen = max(maxlen, j - i + 1)
            j = j + 1

        return maxlen
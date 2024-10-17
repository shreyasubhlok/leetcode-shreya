class Solution:
    # Time is o(n), where n is the length of s2
    # Space is o(26) = o(1), because we only store at most 26 characters in the hash map (fixed size)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1.
        if len(s1) > len(s2):
            return False

        # Initialize the hash map (hm) to track the frequency of each character in s1.
        hm = {}
        for i in range(len(s1)):
            if s1[i] not in hm:
                hm[s1[i]] = 1
            else:
                hm[s1[i]] = hm[s1[i]] + 1

        # `requiredMatches` keeps track of how many characters we need to match exactly.
        requiredMatches = len(hm)

        # sliding window technique, Initialize the left and right pointers for the sliding window.
        left = 0
        right = 0

        # Sliding window: iterate over the characters in s2 with the right pointer.
        while right < len(s2):
            # Check if the character at the right pointer is in s1
            if s2[right] in hm:
                hm[s2[right]] = hm[s2[right]] - 1
                if hm[s2[right]] == 0:  # If the count reaches zero, we've fully matched this character.
                    requiredMatches = requiredMatches - 1

            # If the window size exceeds the size of s1, adjust the left side of the window.
            if right >= len(s1):
                if s2[left] in hm:
                    # When sliding the window, restore the count of the character at the left pointer.
                    if hm[s2[left]] == 0:
                        requiredMatches = requiredMatches + 1  # We need to match this character again.
                    hm[s2[left]] = hm[s2[
                        left]] + 1  # Increment the count for the character being removed from the window.
                left = left + 1  # Move the left pointer to shrink the window.

            # If `requiredMatches` becomes 0, it means all characters in the current window match s1's character frequencies.
            if requiredMatches == 0:
                return True

            right = right + 1  # Move the right pointer to expand the window.

        return False




class Solution:
    # sliding window
    # time O(n) and space o(n)
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(t) > len(s):
            return ""

        tFreq = Counter(t)
        required = len(tFreq)
        left = 0
        right = 0
        windowCount = {}
        formed = 0

        minLen = float('inf')
        minWindowStart = 0

        while right < len(s):
            char = s[right]
            windowCount[char] = windowCount.get(char, 0) + 1

            if char in tFreq and windowCount[char] == tFreq[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    minWindowStart = left

                windowCount[char] -= 1
                if char in tFreq and windowCount[char] < tFreq[char]:
                    formed -= 1

                left += 1
            right += 1

        if minLen != float('inf'):
            return s[minWindowStart:minWindowStart + minLen]
        else:
            return ""

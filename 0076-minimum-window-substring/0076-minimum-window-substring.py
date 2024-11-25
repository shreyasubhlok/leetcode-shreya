from collections import Counter

class Solution:
    # Sliding window approach to solve the Minimum Window Substring problem
    # Time Complexity: O(n) - Each character is visited at most twice (once by 'right' and once by 'left')
    # Space Complexity: O(n) - For storing the frequency maps
    
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If t is empty or t is longer than s, return an empty string
        if len(t) == 0 or len(t) > len(s):
            return ""
        
        # Frequency map of characters in t
        tFreq = Counter(t)
        required = len(tFreq)  # Number of unique characters in t that must be present in the window
        
        # Initialize sliding window pointers
        left = 0
        right = 0
        
        # Frequency map for the current window
        windowCount = {}
        formed = 0  # Number of unique characters in the current window that meet the required frequency in tFreq
        
        # Variables to track the minimum window
        minLen = float('inf')  # Initialize to infinity for comparison
        minWindowStart = 0     # Start index of the minimum window substring
        
        # Expand the window by moving the right pointer
        while right < len(s):
            char = s[right]
            
            # Add the current character to the window frequency map
            windowCount[char] = windowCount.get(char, 0) + 1
            
            # If the current character's count matches the required frequency in tFreq, increment formed
            if char in tFreq and windowCount[char] == tFreq[char]:
                formed += 1
            
            # Try to contract the window by moving the left pointer
            while left <= right and formed == required:
                char = s[left]  # Character at the left pointer
                
                # Update the minimum window if the current window is smaller
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    minWindowStart = left
                
                # Remove the leftmost character from the window frequency map
                windowCount[char] -= 1
                # If the removed character causes the window to become invalid, decrement formed
                if char in tFreq and windowCount[char] < tFreq[char]:
                    formed -= 1
                
                # Move the left pointer to shrink the window
                left += 1
            
            # Expand the window by moving the right pointer
            right += 1
        
        # If a valid window was found, return it; otherwise, return an empty string
        if minLen != float('inf'):
            return s[minWindowStart:minWindowStart + minLen]
        else:
            return ""

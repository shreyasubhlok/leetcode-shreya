class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time complexity o(n) and space complexity is O(n)-not sure why leetcode is saying o(1)
        if len(s) == 0:
            return 0
        charSet = set() #initialize set in python
        res = 0
        
        for ch in s:
            if ch in charSet:
                # If the character is already in the set, it forms a palindrome pair
                # Add 2 to the result and remove the character from the set
                res += 2
                charSet.remove(ch)
            else:
                # If the character is not in the set, add it to the set
                charSet.add(ch)

        # Check if there is any character left in charSet that can be the center of the palindrome
        if len(charSet) > 0:
            res = res + 1 # Add 1 to the result (for the center character of the palindrome)

        return res


"""
def longestPalindrome(self, s: str) -> int:
        #time complexity o(n) and space complexity is O(n)
        if len(s) == 0:
            return 0

        myMap = {}  # Dictionary to store character frequencies
        oddCount = 0  # Flag to track if there is an odd frequency character
        res = 0  # Flag to track if there is an odd frequency character

        # Count frequencies of each character in the string
        for ch in s:
            if ch in myMap:
                myMap[ch] += 1
            else:
                myMap[ch] = 1

        # Iterate through the frequency map to calculate the longest palindrome length
        for value in myMap.values():
            if value % 2 == 0:
                res = res + value  # Add all characters with even frequencies directly to the result
            else:
                res =  res + value - 1  # For characters with odd frequencies, add (value - 1) to the result
                oddCount = 1  # Set oddCount to 1 to indicate there's at least one odd frequency character

        return oddCount + res

        return count

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time is o(n)
        # space is o(n)
        if len(s) != len(t):
            return False

        myMap = {}
        # Count occurrences of each character in string s
        for char in s:
            if char in myMap:
                myMap[char] = myMap[char] + 1  # myMap[char] = myMap.get(char) + 1 -> this is also correct in python
            else:
                myMap[char] = 1

        # Compare counts of characters in string t
        for char in t:
            if char in myMap:
                myMap[char] = myMap[char] - 1
                if myMap[char] == 0:
                    del myMap[char] #delete a specific key-value pair from a dictionary
            else:
                return False

        # Check if all characters are matched
        if len(myMap) == 0:
            return True
        else:
            return False

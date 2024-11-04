class Solution:
    # Time Complexity: O(n), where n is the length of the pattern or the number of words in the string `s`
    # Space Complexity: O(m), where m is the number of unique characters in `pattern` and unique words in `s`

    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string `s` by spaces to create a list of words
        words = s.split(" ")

        # Base case- If the number of characters in `pattern` does not match the number of words, return False
        if len(pattern) != len(words):
            return False

        # Dictionary to map each character in `pattern` to a word in `s`
        patternMap = {}

        # Set to track words that have already been assigned to a pattern character
        wordSet = set()

        # Loop through each character in `pattern` and corresponding word in `words`
        for i in range(len(words)):
            # If the character is already mapped to a word
            if pattern[i] in patternMap:
                # Check if it matches the current word; if not, return False
                if patternMap[pattern[i]] != words[i]:
                    return False
            else:
                # If the word is already mapped to another character, return False
                if words[i] in wordSet:
                    return False
               
                # Map the character to the word and add the word to the set
                patternMap[pattern[i]] = words[i]
                wordSet.add(words[i])

        # Return True if the pattern matches the sequence of words
        return True
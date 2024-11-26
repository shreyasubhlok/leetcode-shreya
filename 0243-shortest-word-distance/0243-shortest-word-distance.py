class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        firstWordIndex = -1  # Last seen index of word1
        secondWordIndex = -1  # Last seen index of word2
        minDistance = float('inf')
        # Traverse the list using a regular loop with an index
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                firstWordIndex = i  # Update index for word1
            elif wordsDict[i] == word2:
                secondWordIndex = i  # Update index for word2

             # If both indices are valid, calculate the distance
            if firstWordIndex != -1 and secondWordIndex != -1:
                minDistance = min(minDistance, abs(firstWordIndex - secondWordIndex))

        return minDistance 
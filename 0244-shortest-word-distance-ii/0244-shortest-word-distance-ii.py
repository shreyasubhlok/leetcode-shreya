class WordDistance:
    #Time: O(n), space:O(n)
    def __init__(self, wordsDict: List[str]):
        """
        Preprocess the list of words to store the indices of each word for quick access.

        :param wordsDict: List of words in the dictionary.
        """
        self.indexMap = {}  # Dictionary to store word and its indices

        # Traverse the words and store their indices in the dictionary
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.indexMap:
                self.indexMap[wordsDict[i]] = []  # Initialize a list if word is not already present
            self.indexMap[wordsDict[i]].append(i)  # Append the current index of the word

    def shortest(self, word1: str, word2: str) -> int:
        """
        Find the shortest distance between two words in the list.

        :param word1: The first word.
        :param word2: The second word.
        :return: The shortest distance between the two words.
        """
        # Retrieve the list of indices for word1 and word2
        indexListWord1 = self.indexMap[word1]
        indexListWord2 = self.indexMap[word2]

        # Initialize pointers for both index lists
        i = 0
        j = 0

        # Initialize minimum length to infinity
        minLen = float("inf")

        # Use two pointers to find the minimum distance
        while i < len(indexListWord1) and j < len(indexListWord2):
            # Calculate the distance between the current indices
            minLen = min(minLen, abs(indexListWord1[i] - indexListWord2[j]))

            # Move the pointer for the smaller index to explore other possibilities
            if indexListWord1[i] < indexListWord2[j]:
                i += 1  # Increment pointer for word1
            else:
                j += 1  # Increment pointer for word2

        return minLen  # Return the shortest distance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

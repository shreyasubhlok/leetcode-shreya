class Solution:
    #time: O(n*mlogm), sorting is mlogm . N words in total so o(n*mlogm)
    #space: o(n*m),myMap takes up space to store the anagram groups, which is proportional to the total number of characters        in the input, i.e., O(n * m)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalRes = []
        
        # Create a dictionary to map , key as sorted word and value as list of strs
        myMap = {}
        
        for word in strs:
            sortedWord = "".join(sorted(word))  # Sort the word to use as the key in the dictionary

            # If the sorted word is already a key in the dictionary, append the original word to the list
            if sortedWord in myMap:
                myMap[sortedWord].append(word)
            else:
                myMap[sortedWord] = [word]

        # Iterate through the values of the dictionary and add them to the final result list
        for value in myMap.values():
            finalRes.append(value)

        return finalRes
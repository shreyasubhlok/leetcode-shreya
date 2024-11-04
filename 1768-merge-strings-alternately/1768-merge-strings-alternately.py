class Solution:
    '''
    Time : o(n+m)
    Space: o(1)
    Space Complexity: Instead of creating a new string with each concatenation, we use a single list, which accumulates all characters. The join method only creates one final string, resulting in a more space-efficient solution, effectively keeping it at O(n + m) for the final string.     
    '''
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            res.append(word1[i])
            i += 1
        while j < len(word2):
            res.append(word2[j])
            j += 1

         # Join list into a single string at the end
        return ''.join(res)
    
    #Time : o(n+m)
    #Space: o(n)
    def mergeAlternatelyUsingEmptyString(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            res = res + word1[i] + word2[j]
            i += 1
            j += 1
        while i < len(word1):
            res = res + word1[i]
            i += 1
        while j < len(word2):
            res = res + word2[j]
            j += 1
        return res

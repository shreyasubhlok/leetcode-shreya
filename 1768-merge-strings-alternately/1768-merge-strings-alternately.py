class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            res=res+word1[i]+word2[j]
            i+=1
            j+=1
        while i<len(word1):
            res=res+word1[i]
            i+=1
        while j<len(word2):
            res=res+word2[j]
            j+=1
        
            
        print(res)
        return res
        
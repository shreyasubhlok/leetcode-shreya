class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myMap={}
        
        for char in ransomNote:
            if char in myMap:
                myMap[char]=1+myMap[char]
            else:
                myMap[char]=1
                
        for char in magazine:
            if char in myMap:
                myMap[char]=myMap[char]-1
                if myMap[char]==0:
                    del myMap[char]
        
        return len(myMap)==0
                
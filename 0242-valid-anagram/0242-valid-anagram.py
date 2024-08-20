class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        myMap={}
        for char in s:
            if char in myMap:
                myMap[char]=myMap[char]+1
            else:
                myMap[char]=1
        
        for char in t:
            if char in myMap:
                myMap[char]=myMap[char]-1
                if myMap[char]==0:
                    del myMap[char]
            else:
                return False
        
        return len(myMap)==0
            
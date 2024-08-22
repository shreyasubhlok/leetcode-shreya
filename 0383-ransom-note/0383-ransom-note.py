class Solution:
     #time is o(n+m)=o(n)
    #space is o(1) 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False

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
        
        
                
#More optimized - optional :Time and space both same for both appraches. So any approach is fine
'''
        #from collections import Counter
        #magazine_count = Counter(magazine) creates a Counter object that counts the occurrences of each character in the magazine string, 
        providing a straightforward way to analyze and manipulate frequency data in Python.
        magazine_counts = Counter(magazine)
        for ch in ransomNote:
            if magazine_counts[ch]>0:
                magazine_counts[ch]=magazine_counts[ch]-1
            else:
                return False
        return True
'''        
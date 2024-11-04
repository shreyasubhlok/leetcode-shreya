class Solution:
    #Time is o(n) and space is o(1)
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        patternMap = {}
        wordSet=set()

        for i in range(len(words)):
            if pattern[i] in patternMap:
                if patternMap[pattern[i]]!=words[i]:
                    return False
            else:
                if words[i] not in wordSet:
                    patternMap[pattern[i]]=words[i]
                    wordSet.add(words[i])
                else:
                    return False
        return True


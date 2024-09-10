class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.isEndOfWord=False
        
class Trie:

    def __init__(self):
        self.root=TrieNode()
    
    def charToIndex(self,char:str)->int:
        return ord(char)-ord('a')
    
    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            index=self.charToIndex(char)
            if not node.child[index]:
                node.child[index]=TrieNode()
            node=node.child[index]
        node.isEndOfWord=True

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            index=self.charToIndex(char)
            if not node.child[index]:
                return False
            node=node.child[index]
        return node.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            index=self.charToIndex(char)
            if not node.child[index]:
                return False
            node=node.child[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
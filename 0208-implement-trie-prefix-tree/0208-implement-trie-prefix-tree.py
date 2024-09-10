class TrieNode:
    def __init__(self):
        # Initialize an array of size 26 (for each letter in the alphabet).
        # Each element points to a child TrieNode, initialized as None.
        self.child=[None]*26
        # Boolean to indicate whether this node marks the end of a word.
        self.isEndOfWord=False
     
class Trie:

    def __init__(self):
        self.root=TrieNode()   # Root node represents the starting point of the Trie.
    
    def charToIndex(self,char:str)->int:
        return ord(char)-ord('a')  # Convert a character to its corresponding index (0 for 'a', 1 for 'b', etc.).
    
    def insert(self, word: str) -> None:
        node=self.root    # Start at the root node for each word insertion.
        for char in word:    # Traverse each character in the word.
            index=self.charToIndex(char)
            # If the child node for this character doesn't exist, create a new TrieNode.
            if not node.child[index]:
                node.child[index]=TrieNode()
            node=node.child[index]  # Traversal Move to the child node.
        node.isEndOfWord=True     # Mark the end of the word after the last character.

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            index=self.charToIndex(char)
            # If the corresponding child node doesn't exist, return False
            if not node.child[index]:
                return False
            node=node.child[index] # Traversal Move to the child node.
        # After traversing the word, check if it's marked as the end of a word.
        return node.isEndOfWord #this will have resultant value
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root    # Start at the root node for checking the prefix.
        for char in prefix:
            index=self.charToIndex(char)
           # If the corresponding child node doesn't exist, return False.
            if not node.child[index]:
                return False
            node=node.child[index] # Traversal Move to the child node.
        return True         # If the prefix is found, return True.
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
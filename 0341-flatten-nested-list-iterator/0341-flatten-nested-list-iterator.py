#time and space O(n)
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Stack to hold elements
        self.stack = []
        self.pushList(nestedList)  # Push all elements in reverse order

    def pushList(self, lst):
        """Helper function to push elements onto the stack in reverse order."""
        index = len(lst) - 1  # Start at the last element
        while index >= 0:  # Keep going until we reach the start
            self.stack.append(lst[index])  # Push NestedInteger objects onto the stack
            index -= 1  # Decrement index

    def next(self) -> int:
        """Return the next integer from the nested list."""
        return self.stack.pop().getInteger()  # Extract integer value

    def hasNext(self) -> bool:
        """Check if there is a next integer available."""
        while self.stack:
            top = self.stack[-1]  # Look at the top element
            if top.isInteger():  # If it's an integer, we can return True
                return True
            else:
                self.stack.pop()  # Remove the list object
                self.pushList(top.getList())  # Expand its elements
        return False  # No more elements left
    
# Usage
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

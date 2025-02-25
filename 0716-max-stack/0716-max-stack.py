import heapq  # Importing heapq to implement a max-heap

class MaxStack:
    def __init__(self):
        """
        Initialize the MaxStack.
        - `stack` stores (value, unique_id) tuples.
        - `heap` (max heap) stores (-value, -unique_id) to maintain max order.
        - `removed` set keeps track of deleted elements.
        - `cnt` provides unique IDs to track insertion order.
        """
        self.stack = []  # Stack to store elements in insertion order
        self.heap = []   # Max heap to store elements for efficient max retrieval
        self.removed = set()  # Tracks removed elements
        self.cnt = 0  # Unique counter to distinguish duplicate values

    def push(self, x: int) -> None:
        """
        Push a new element onto the stack.
        - Insert (x, cnt) into `stack`.
        - Push (-x, -cnt) into `heap` to maintain a max heap.
        - Increment `cnt` to maintain unique order.
        """
        heapq.heappush(self.heap, (-x, -self.cnt))  # Max heap stores negative values
        self.stack.append((x, self.cnt))  # Add to stack with unique ID
        self.cnt += 1  # Increase unique counter
    
    def pop(self) -> int:
        """
        Remove and return the top element from the stack.
        - If the top element has been marked deleted, remove it first.
        - Mark the popped element as deleted in `removed` set.
        """
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()  # Remove stale elements

        num, ind = self.stack.pop()  # Get the actual top element
        self.removed.add(ind)  # Mark as removed
        return num
        
    def top(self) -> int:
        """
        Return the top element without removing it.
        - Ensure the stack does not contain deleted elements.
        """
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()  # Remove stale elements

        num, ind = self.stack[-1]  # Get the valid top element
        return num
        
    def peekMax(self) -> int:
        """
        Return the maximum element in the stack without removing it.
        - Ensure that the max element retrieved from `heap` is valid.
        - Remove stale elements if necessary.
        """
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)  # Remove stale elements from heap

        num, ind = self.heap[0]  # Get the max element
        return -num  # Convert back to positive
    
    def popMax(self) -> int:
        """
        Remove and return the maximum element.
        - Ensure that the max element retrieved is valid.
        - Mark it as removed and clean up the stack accordingly.
        """
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)  # Remove stale elements from heap

        num, ind = heapq.heappop(self.heap)  # Get and remove max element
        self.removed.add(-ind)  # Mark as deleted
        return -num  # Convert back to positive

# Usage:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

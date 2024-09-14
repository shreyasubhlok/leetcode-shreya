class MinStack:
    # time complexity: o(1) for each operation.
    # spcace complexity:O(n), where n is the number of elements stored in the stack.
    def __init__(self):
        # Initialize two stacks: one for storing values, the other for tracking minimums.
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the main stack anyways
        # For the minStack, push the smaller value between the current value and the top of minStack.If minStack is empty, just push the current value.
        
        if self.minStack:
            val = min(val, self.minStack[-1])
            
        self.minStack.append(val)  # Append the new minimum (or current value if minStack is empty)

    def pop(self):
        # Pop the top elements from both the main stack and the minStack. This ensures the minimum value is always in sync with the current stack's values.
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]  # Return the top element of the main stack.

    def getMin(self) -> int:
        return self.minStack[-1]  # Return the top element of the minStack.

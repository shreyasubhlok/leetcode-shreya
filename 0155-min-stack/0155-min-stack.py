class MinStack:

    def __init__(self):
        # Initialize the minimum value as infinity.
        self.min_val = float('inf')
        # Initialize the stack.
        self.stack = []

    def push(self, x: int) -> None:
        # If the value to be pushed is less than or equal to the current minimum,
        # push the current minimum first and then update the minimum value.
        if x <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = x
        # Push the value.
        self.stack.append(x)

    def pop(self) -> None:
        # Pop the top element.
        if self.stack.pop() == self.min_val:
            # If the popped element is the current minimum,
            # the next popped value will be the previous minimum.
            self.min_val = self.stack.pop()

    def top(self) -> int:
        # Return the top element of the stack.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the minimum value.
        return self.min_val

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
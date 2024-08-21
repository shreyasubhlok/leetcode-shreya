class MyQueue:
    #Time complexity: O(1) amortized(almost every time) for each operation - push,pop and peek
    #Space complexity: O(2n)=O(n), where nnn is the number of elements in the queue
    
    def __init__(self):
        # Initialize two stacks
        self.inputStack = []  # inputStack to perform push operations
        self.outputStack = []  # outputStack to perfrom pop and peek operations
        print(f"Initialized am empty queue. InputStack:{self.inputStack}, outputStack:{self.outputStack}")

    def push(self, x: int) -> None:
        #push x into the inputStack
        self.inputStack.append(x)
        print(f"pushed {x} to the inputStack. InputStack:{self.inputStack}, outputStack:{self.outputStack}")

    def pop(self) -> int:
        #if the outputStack is empty, pop all the elements from inputStack and push it to the outputStack
        if not self.outputStack: #if not self.outputStack: means that self.outputStack is empty.
            while len(self.inputStack) != 0:
                val = self.inputStack.pop()
                self.outputStack.append(val)
        #Pop and return the top value from outputStack
        popped_value = self.outputStack.pop()
        print(f"Popped {popped_value} from outputStack. InputStack:{self.inputStack}, outputStack:{self.outputStack} ")
        return popped_value

    def peek(self) -> int:
        #if the outputStack is empty, pop all the elements from inputStack and push it to the outputStack
        if not self.outputStack:
            while len(self.inputStack) != 0:
                val = self.inputStack.pop()
                self.outputStack.append(val)
        # Return the top element from the output stack
        peek_value = self.outputStack[-1] #means accessing the last element (top element)
        print(f"Peeked {peek_value} from outputStack. InputStack:{self.inputStack}, outputStack:{self.outputStack} ")
        return peek_value

    def empty(self) -> bool:
        if not self.outputStack and not self.inputStack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

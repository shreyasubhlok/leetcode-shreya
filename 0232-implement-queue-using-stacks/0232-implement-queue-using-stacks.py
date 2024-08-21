class MyQueue:

    def __init__(self):
        #Here i will initialize inputstack and outputstack
        self.inputstack = []
        self.outputstack=[]
        print(f"inputstack and outputstack initailized. Inputstack = {self.inputstack} and outputstack = {self.outputstack}")
        

    def push(self, x: int) -> None:
        #push elements to input stack
        self.inputstack.append(x)
        print(f"Pushed element {x} to inputstack. Inputstack = {self.inputstack} and outputStack = {self.outputstack}")
        

    def pop(self) -> int:
        if not self.outputstack:
            while len(self.inputstack)!=0 :
                val=self.inputstack.pop()
                self.outputstack.append(val)
        popped_value=self.outputstack.pop()
        print(f"popped value {popped_value} from outputstack. Inputstack = {self.inputstack} and outputStack = {self.outputstack}")
        return popped_value
        

    def peek(self) -> int:
        if not self.outputstack:
              while len(self.inputstack)!=0:
                val=self.inputstack.pop()
                self.outputstack.append(val)
        peek_value=self.outputstack[-1]
        print(f"PeekedValue is {peek_value} from outputstack. Inputstack = {self.inputstack} and outputStack = {self.outputstack}")
        return peek_value
        
              
        

    def empty(self) -> bool:
        if not self.inputstack and not self.outputstack:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.cnt = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1
    
    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, ind = self.stack.pop()
        self.removed.add(ind)
        return num
        
    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        
        num, ind = self.stack[-1]
        return num
        
    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, ind = self.heap[0]
        return -num

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, ind = heapq.heappop(self.heap)
        self.removed.add(-ind)
        return -num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# class MaxStack:

#     def __init__(self):
#         self.stack = []
#         self.maxstack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         maxi = 0
#         if self.maxstack:
#             maxi = max(self.stack[-1], self.maxstack[-1])
#         else:
#             maxi = self.stack[-1]
#         self.maxstack.append(maxi)  

#     def pop(self) -> int:
#         self.maxstack.pop()
#         return self.stack.pop()
        
#     def top(self) -> int:
#         return self.stack[-1] if self.stack else None

#     def peekMax(self) -> int:
#         return self.maxstack[-1] if self.maxstack else None

#     def popMax(self) -> int:
#         buffer = []
#         tbr = self.maxstack[-1]
#         while self.stack[-1] != tbr:
#             buffer.append(self.stack.pop())
#             self.maxstack.pop()
#         self.stack.pop()
#         self.maxstack.pop()
#         while buffer:
#             self.stack.append(buffer.pop())
#             maxi = 0
#             if self.maxstack:
#                 maxi = max(self.stack[-1], self.maxstack[-1])
#             else:
#                 maxi = self.stack[-1]
#             self.maxstack.append(maxi)
        
#         return tbr
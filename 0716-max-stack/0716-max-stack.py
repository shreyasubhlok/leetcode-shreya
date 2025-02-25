import heapq

class MaxStack:
    def __init__(self):
        self.stack = []  # Stores (value, unique_id)
        self.maxHeap = []  # Stores (-value, unique_id) for max retrieval
        self.deleted = set()  # Tracks deleted elements
        self.idCounter = 0  # Unique ID for each element

    def push(self, x: int) -> None:
        self.stack.append((x, self.idCounter))
        heapq.heappush(self.maxHeap, (-x, self.idCounter))
        self.idCounter += 1

    def pop(self) -> int:
        while self.stack:
            val, uid = self.stack.pop()
            if uid not in self.deleted:
                self.deleted.add(uid)  # Mark deleted
                return val

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()  # Remove stale elements
        return self.stack[-1][0] if self.stack else -1

    def peekMax(self) -> int:
        while self.maxHeap and self.maxHeap[0][1] in self.deleted:
            heapq.heappop(self.maxHeap)  # Remove stale elements
        return -self.maxHeap[0][0] if self.maxHeap else -1

    def popMax(self) -> int:
        while self.maxHeap:
            maxVal, uid = heapq.heappop(self.maxHeap)
            if uid not in self.deleted:
                self.deleted.add(uid)  # Mark deleted
                return -maxVal
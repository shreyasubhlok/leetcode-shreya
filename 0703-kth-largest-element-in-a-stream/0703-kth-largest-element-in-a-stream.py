class KthLargest:
    '''
    Time: O(nlogk)
    Space: o(k) The space used by the min-heap is O(k)
    '''
    def __init__(self,k:int,nums:List[int]):
        self.min_heap=[]
        self.k=k
        # Add the initial numbers to the min heap
        for num in nums:
            self.add(num)  # Use the add method to maintain the size of the heap

    def add(self,val:int)->int:
        heapq.heappush(self.min_heap,val) # Add the new value to the min heap

        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)
            
        # Return the k-th largest element, which is the smallest in the heap
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)